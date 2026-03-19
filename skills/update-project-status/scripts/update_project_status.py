from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import subprocess
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from html import escape
from pathlib import Path
from typing import Any


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "references" / "default_status_config.json"
PROJECT_OVERRIDE_PATH = Path(".codex/skill-config/update-project-status.json")


@dataclass
class CommitEntry:
    sha: str
    subject: str
    author: str
    date: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a project status update from Git and optional extra sources.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root to process.")
    parser.add_argument("--config", type=Path, help="Optional JSON config path overriding the default status rules.")
    parser.add_argument("--status-file", type=Path, help="Override the configured status markdown output path.")
    parser.add_argument("--log-file", type=Path, help="Override the configured status log output path.")
    parser.add_argument("--shared-doc", type=Path, help="Optional legacy shared document path to copy the generated status file to.")
    parser.add_argument("--limit", type=int, default=10, help="Number of recent commits to inspect.")
    parser.add_argument("--dry-run", action="store_true", help="Preview outputs and sync operations without writing changes.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def merge_config(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            merged[key] = merge_config(base[key], value)
        else:
            merged[key] = value
    return merged


def resolve_config(root: Path, explicit_config: Path | None) -> tuple[dict[str, Any], Path]:
    config = load_json(DEFAULT_CONFIG_PATH)
    config_path = DEFAULT_CONFIG_PATH
    project_override = root / PROJECT_OVERRIDE_PATH
    if project_override.exists():
        config = merge_config(config, load_json(project_override))
        config_path = project_override
    if explicit_config is not None:
        path = explicit_config if explicit_config.is_absolute() else root / explicit_config
        config = merge_config(config, load_json(path))
        config_path = path
    return config, config_path


def run_git(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace")


def run_command(root: Path, command: list[str], stdin_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace", input=stdin_text)


def detect_git_repository(root: Path) -> bool:
    return run_git(root, ["rev-parse", "--show-toplevel"]).returncode == 0


def load_commits(root: Path, limit: int) -> list[CommitEntry]:
    result = run_git(root, ["log", f"-n{limit}", "--pretty=format:%H%x1f%s%x1f%an%x1f%ad", "--date=short"])
    if result.returncode != 0:
        return []
    commits: list[CommitEntry] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        sha, subject, author, date = (line.split("\x1f") + ["", "", "", ""])[:4]
        commits.append(CommitEntry(sha=sha[:8], subject=subject.strip(), author=author.strip(), date=date.strip()))
    return commits


def classify_commits(commits: list[CommitEntry], config: dict[str, Any]) -> tuple[list[CommitEntry], list[CommitEntry], list[CommitEntry], list[CommitEntry]]:
    feature_keywords = tuple(keyword.lower() for keyword in config.get("feature_keywords", []))
    bugfix_keywords = tuple(keyword.lower() for keyword in config.get("bugfix_keywords", []))
    next_task_keywords = tuple(keyword.lower() for keyword in config.get("next_task_keywords", []))
    features: list[CommitEntry] = []
    bugfixes: list[CommitEntry] = []
    next_tasks: list[CommitEntry] = []
    others: list[CommitEntry] = []
    for commit in commits:
        text = commit.subject.lower()
        if any(keyword in text for keyword in feature_keywords):
            features.append(commit)
        elif any(keyword in text for keyword in bugfix_keywords):
            bugfixes.append(commit)
        elif any(keyword in text for keyword in next_task_keywords):
            next_tasks.append(commit)
        else:
            others.append(commit)
    return features, bugfixes, next_tasks, others


def normalize_task_line(text: str, prefix: str | None = None) -> str:
    task = text.strip()
    return f"{prefix}: {task}" if prefix else task


def extract_tasks_from_text(text: str, max_items: int, prefix: str | None = None) -> list[str]:
    tasks: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("-"):
            tasks.append(normalize_task_line(line.lstrip("- ").strip(), prefix))
        elif line.startswith("*"):
            tasks.append(normalize_task_line(line.lstrip("* ").strip(), prefix))
        elif len(line) > 2 and line[0].isdigit() and line[1] in ".)":
            tasks.append(normalize_task_line(line[2:].strip(), prefix))
        if len(tasks) >= max_items:
            return tasks
    return tasks


def extract_tasks_from_file_glob(root: Path, pattern: str, max_items: int, prefix: str | None = None) -> list[str]:
    tasks: list[str] = []
    for path in sorted(root.glob(pattern)):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        item_prefix = prefix or path.relative_to(root).as_posix()
        tasks.extend(extract_tasks_from_text(text, max_items=max_items - len(tasks), prefix=item_prefix))
        if len(tasks) >= max_items:
            break
    return tasks


def extract_tasks_from_jira_json(root: Path, source: dict[str, Any], max_items: int) -> list[str]:
    path_value = source.get("path")
    if not path_value:
        return []
    path = Path(path_value)
    path = path if path.is_absolute() else root / path
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    issues = payload.get("issues", payload if isinstance(payload, list) else [])
    status_field = str(source.get("status_field", "status"))
    title_field = str(source.get("title_field", "summary"))
    key_field = str(source.get("key_field", "key"))
    accepted_statuses = {item.lower() for item in source.get("accepted_statuses", [])}
    tasks: list[str] = []
    for issue in issues:
        fields = issue.get("fields", issue)
        status_value = fields.get(status_field, "")
        if isinstance(status_value, dict):
            status_value = status_value.get("name", "")
        if accepted_statuses and str(status_value).lower() not in accepted_statuses:
            continue
        title = fields.get(title_field) or issue.get(title_field)
        key = issue.get(key_field) or fields.get(key_field)
        if title:
            prefix = f"Jira {key}" if key else "Jira"
            tasks.append(normalize_task_line(str(title), prefix))
        if len(tasks) >= max_items:
            break
    return tasks


def extract_tasks_from_trello_json(root: Path, source: dict[str, Any], max_items: int) -> list[str]:
    path_value = source.get("path")
    if not path_value:
        return []
    path = Path(path_value)
    path = path if path.is_absolute() else root / path
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    cards = payload.get("cards", payload if isinstance(payload, list) else [])
    include_closed = bool(source.get("include_closed", False))
    allowed_lists = {str(item) for item in source.get("list_names", [])}
    tasks: list[str] = []
    for card in cards:
        if card.get("closed") and not include_closed:
            continue
        list_name = card.get("list", {}).get("name") or card.get("listName") or ""
        if allowed_lists and list_name not in allowed_lists:
            continue
        title = card.get("name") or card.get("title")
        if title:
            prefix = f"Trello {list_name}" if list_name else "Trello"
            tasks.append(normalize_task_line(str(title), prefix))
        if len(tasks) >= max_items:
            break
    return tasks


def extract_tasks_from_command(root: Path, source: dict[str, Any], max_items: int) -> list[str]:
    command = source.get("command")
    if not isinstance(command, list) or not command:
        return []
    output_format = str(source.get("format", "lines"))
    result = run_command(root, [str(item) for item in command])
    if result.returncode != 0:
        return [f"Command source failed: {' '.join(str(item) for item in command)} -> {result.stderr.strip() or result.stdout.strip()}"]
    if output_format == "json":
        payload = json.loads(result.stdout or "[]")
        if isinstance(payload, list):
            return [str(item) for item in payload[:max_items]]
        return [str(payload)]
    return extract_tasks_from_text(result.stdout, max_items=max_items, prefix=source.get("prefix"))


def resolve_task_sources(config: dict[str, Any]) -> list[dict[str, Any]]:
    sources = list(config.get("task_sources", []))
    if not sources:
        for pattern in config.get("extra_source_globs", []):
            sources.append({"type": "file_glob", "pattern": pattern})
    return sources


def collect_external_tasks(root: Path, config: dict[str, Any]) -> list[str]:
    max_items = int(config.get("max_extra_tasks", 5))
    tasks: list[str] = []
    for source in resolve_task_sources(config):
        source_type = str(source.get("type", "file_glob"))
        remaining = max_items - len(tasks)
        if remaining <= 0:
            break
        if source_type == "file_glob":
            tasks.extend(extract_tasks_from_file_glob(root, str(source.get("pattern", "")), remaining, prefix=source.get("prefix")))
        elif source_type == "jira_json":
            tasks.extend(extract_tasks_from_jira_json(root, source, remaining))
        elif source_type == "trello_json":
            tasks.extend(extract_tasks_from_trello_json(root, source, remaining))
        elif source_type == "command":
            tasks.extend(extract_tasks_from_command(root, source, remaining))
    return tasks[:max_items]


def infer_next_tasks(features: list[CommitEntry], bugfixes: list[CommitEntry], others: list[CommitEntry], extra_tasks: list[str]) -> list[str]:
    tasks: list[str] = []
    tasks.extend(extra_tasks)
    if features:
        tasks.append("Review the latest feature work and add follow-up validation or docs where needed.")
    if bugfixes:
        tasks.append("Verify recently fixed bugs with regression checks.")
    if others:
        tasks.append("Refine uncategorized recent commits into clearer feature or maintenance follow-ups.")
    if not tasks:
        tasks.append("No recent Git commits or task sources were available; confirm repository state and update plans manually.")
    return tasks


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def build_status_content(git_available: bool, config_path: Path, commits: list[CommitEntry], features: list[CommitEntry], bugfixes: list[CommitEntry], next_task_items: list[str], extra_tasks: list[str], sync_targets: list[dict[str, Any]]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Project Status",
        "",
        f"- Updated at: `{now}`",
        f"- Git data available: `{'yes' if git_available else 'no'}`",
        f"- Config: `{config_path}`",
        f"- Recent commits inspected: `{len(commits)}`",
        "",
        "## Recent Features",
        "",
    ]
    if features:
        lines.extend(f"- `{commit.sha}` {commit.subject} ({commit.author}, {commit.date})" for commit in features)
    else:
        lines.append("- No recent feature commits detected")
    lines.extend(["", "## Fixed Bugs", ""])
    if bugfixes:
        lines.extend(f"- `{commit.sha}` {commit.subject} ({commit.author}, {commit.date})" for commit in bugfixes)
    else:
        lines.append("- No recent bug-fix commits detected")
    lines.extend(["", "## Upcoming Tasks", ""])
    lines.extend(f"- {item}" for item in next_task_items)
    lines.extend(["", "## Additional Sources", ""])
    if extra_tasks:
        lines.extend(f"- {item}" for item in extra_tasks)
    else:
        lines.append("- No extra task sources contributed items")
    lines.extend(["", "## Sync Targets", ""])
    if sync_targets:
        lines.extend(f"- {target.get('type', 'unknown')}" for target in sync_targets)
    else:
        lines.append("- No configured sync targets")
    lines.extend(["", "## Notes", ""])
    lines.append("- Status generation combines Git commit subjects with optional configured task sources.")
    if not git_available:
        lines.append("- Git repository metadata was not available in the target root, so the status relies on fallback task sources.")
    return "\n".join(lines) + "\n"


def append_log_line(git_available: bool, commits: list[CommitEntry], status_file: Path, sync_targets: list[dict[str, Any]]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sync_desc = ",".join(str(target.get("type", "unknown")) for target in sync_targets) if sync_targets else "none"
    return f"[{now}] status updated -> {status_file.as_posix()} | git={'yes' if git_available else 'no'} | commits={len(commits)} | sync={sync_desc}\n"


def write_outputs(status_file: Path, log_file: Path, status_content: str, log_line: str, dry_run: bool) -> None:
    if dry_run:
        return
    ensure_parent(status_file)
    status_file.write_text(status_content, encoding="utf-8")
    ensure_parent(log_file)
    with log_file.open("a", encoding="utf-8") as handle:
        handle.write(log_line)


def legacy_sync_target(shared_doc: Path | None, shared_mode: str) -> list[dict[str, Any]]:
    if shared_doc is None:
        return []
    return [{"type": "local_copy", "path": str(shared_doc), "mode": shared_mode}]


def build_sync_targets(config: dict[str, Any], shared_doc: Path | None) -> list[dict[str, Any]]:
    sync_targets = list(config.get("sync_targets", []))
    if shared_doc is not None:
        sync_targets.extend(legacy_sync_target(shared_doc, str(config.get("shared_mode", "local_copy"))))
    return sync_targets


def sync_local_copy(status_file: Path, target: dict[str, Any], dry_run: bool) -> str:
    path_value = str(target.get("path", "")).strip()
    if not path_value:
        raise ValueError("local_copy sync target requires path")
    path = Path(path_value)
    if dry_run:
        return f"Dry run: would copy status file to {path}"
    ensure_parent(path)
    shutil.copyfile(status_file, path)
    return f"Copied status file to {path}"


def sync_command(status_content: str, root: Path, target: dict[str, Any], dry_run: bool) -> str:
    command = target.get("command")
    if not isinstance(command, list) or not command:
        raise ValueError("command sync target requires a command list")
    if dry_run:
        return f"Dry run: would run sync command {' '.join(str(item) for item in command)}"
    result = run_command(root, [str(item) for item in command], stdin_text=status_content)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "command sync failed")
    return f"Ran sync command {' '.join(str(item) for item in command)}"


def request_json(url: str, method: str, headers: dict[str, str], payload: dict[str, Any] | None = None) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8")
    return json.loads(body) if body else {}


def confluence_headers(target: dict[str, Any]) -> dict[str, str]:
    token = os.environ.get(str(target.get("token_env", "CONFLUENCE_TOKEN")))
    username = os.environ.get(str(target.get("username_env", "CONFLUENCE_USERNAME")))
    auth_mode = str(target.get("auth_mode", "bearer"))
    headers = {"Content-Type": "application/json"}
    if auth_mode == "basic":
        if not token or not username:
            raise RuntimeError("Confluence basic auth requires username and token environment variables")
        token_bytes = base64.b64encode(f"{username}:{token}".encode("utf-8")).decode("ascii")
        headers["Authorization"] = f"Basic {token_bytes}"
    else:
        if not token:
            raise RuntimeError("Confluence bearer auth requires the configured token environment variable")
        headers["Authorization"] = f"Bearer {token}"
    return headers


def sync_confluence(status_content: str, target: dict[str, Any], dry_run: bool) -> str:
    base_url = str(target.get("base_url", "")).rstrip("/")
    page_id = str(target.get("page_id", ""))
    if not base_url or not page_id:
        raise ValueError("confluence_rest sync target requires base_url and page_id")
    if dry_run:
        return f"Dry run: would sync status content to Confluence page {page_id}"
    headers = confluence_headers(target)
    page_url = f"{base_url}/rest/api/content/{page_id}?expand=version,title"
    current = request_json(page_url, "GET", headers)
    next_version = int(current.get("version", {}).get("number", 0)) + 1
    title = str(target.get("title") or current.get("title") or "Project Status")
    html_value = f"<pre>{escape(status_content)}</pre>"
    payload = {
        "id": page_id,
        "type": "page",
        "title": title,
        "version": {"number": next_version},
        "body": {"storage": {"value": html_value, "representation": "storage"}},
    }
    request_json(f"{base_url}/rest/api/content/{page_id}", "PUT", headers, payload)
    return f"Synced status content to Confluence page {page_id}"


def sync_google_docs(status_content: str, target: dict[str, Any], dry_run: bool) -> str:
    document_id = str(target.get("document_id", ""))
    token = os.environ.get(str(target.get("token_env", "GOOGLE_DOCS_TOKEN")))
    if not document_id:
        raise ValueError("google_docs_rest sync target requires document_id")
    if dry_run:
        return f"Dry run: would sync status content to Google Docs document {document_id}"
    if not token:
        raise RuntimeError("Google Docs sync requires the configured bearer token environment variable")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    document = request_json(f"https://docs.googleapis.com/v1/documents/{document_id}", "GET", headers)
    body_items = document.get("body", {}).get("content", [])
    end_index = body_items[-1].get("endIndex", 1) if body_items else 1
    requests: list[dict[str, Any]] = []
    if end_index > 1:
        requests.append({"deleteContentRange": {"range": {"startIndex": 1, "endIndex": end_index - 1}}})
    requests.append({"insertText": {"location": {"index": 1}, "text": status_content}})
    request_json(f"https://docs.googleapis.com/v1/documents/{document_id}:batchUpdate", "POST", headers, {"requests": requests})
    return f"Synced status content to Google Docs document {document_id}"


def sync_targets(status_file: Path, status_content: str, root: Path, targets: list[dict[str, Any]], dry_run: bool) -> list[str]:
    results: list[str] = []
    for target in targets:
        target_type = str(target.get("type", "local_copy"))
        if target_type == "local_copy":
            results.append(sync_local_copy(status_file, target, dry_run))
        elif target_type == "command":
            results.append(sync_command(status_content, root, target, dry_run))
        elif target_type == "confluence_rest":
            results.append(sync_confluence(status_content, target, dry_run))
        elif target_type == "google_docs_rest":
            results.append(sync_google_docs(status_content, target, dry_run))
        else:
            raise ValueError(f"Unsupported sync target type: {target_type}")
    return results


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    config, config_path = resolve_config(root, args.config)
    status_file = args.status_file if args.status_file else Path(config.get("status_file", "docs/status.md"))
    log_file = args.log_file if args.log_file else Path(config.get("log_file", "docs/status_updates.log"))
    status_file = status_file if status_file.is_absolute() else root / status_file
    log_file = log_file if log_file.is_absolute() else root / log_file
    shared_doc = None if args.shared_doc is None else (args.shared_doc if args.shared_doc.is_absolute() else root / args.shared_doc)

    git_available = detect_git_repository(root)
    commits = load_commits(root, args.limit) if git_available else []
    features, bugfixes, explicit_next_tasks, others = classify_commits(commits, config)
    extra_tasks = collect_external_tasks(root, config)
    next_task_items = [commit.subject for commit in explicit_next_tasks] or infer_next_tasks(features, bugfixes, others, extra_tasks)
    sync_target_config = build_sync_targets(config, shared_doc)
    status_content = build_status_content(git_available, config_path, commits, features, bugfixes, next_task_items, extra_tasks, sync_target_config)
    log_line = append_log_line(git_available, commits, status_file, sync_target_config)

    if args.dry_run:
        print("Status file preview:")
        print(status_content)
        print("Log preview:")
        print(log_line.rstrip())
    else:
        write_outputs(status_file, log_file, status_content, log_line, dry_run=False)

    sync_messages = sync_targets(status_file, status_content, root, sync_target_config, dry_run=args.dry_run) if sync_target_config else []

    if args.dry_run:
        print(f"Dry run status file target: {status_file}")
        print(f"Dry run log file target: {log_file}")
    else:
        print(f"Status file updated: {status_file}")
        print(f"Status log updated: {log_file}")
    for message in sync_messages:
        print(message)
    if not git_available:
        print("Warning: Git repository metadata was not available; fallback task sources were used when possible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
