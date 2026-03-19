from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "references" / "default_takeover_config.json"
PROJECT_OVERRIDE_PATH = Path(".codex/skill-config/project-takeover.json")
SKILLS_ROOT = Path(__file__).resolve().parents[2]


@dataclass
class CommandResult:
    returncode: int
    stdout: str
    stderr: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize project takeover, generate onboarding outputs, and optionally apply safe fixes.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root to process.")
    parser.add_argument("--config", type=Path, help="Optional JSON config path overriding the default takeover rules.")
    parser.add_argument("--report-dir", type=Path, help="Directory to write takeover outputs to.")
    parser.add_argument("--shared-dir", type=Path, help="Optional shared directory to copy generated takeover outputs to.")
    parser.add_argument("--apply-safe-fixes", action="store_true", help="Create missing configured directories when safe.")
    parser.add_argument("--install", action="store_true", help="Run inferred or configured install commands.")
    parser.add_argument("--dry-run", action="store_true", help="Preview outputs and actions without writing files.")
    parser.add_argument("--structure-script", type=Path, help="Optional path to a structure-check script returning JSON.")
    parser.add_argument("--docs-script", type=Path, help="Optional path to a documentation-governance script returning JSON.")
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


def run_command(command: list[str], cwd: Path) -> CommandResult:
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    try:
        result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    except FileNotFoundError as exc:
        return CommandResult(127, "", str(exc))
    except OSError as exc:
        return CommandResult(126, "", str(exc))
    return CommandResult(result.returncode, result.stdout, result.stderr)


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def summarize_lines(text: str, limit: int = 6) -> list[str]:
    items: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#") or line.startswith("-") or (len(line) > 2 and line[:2].isdigit() and line[1] == "."):
            items.append(line.lstrip("#").strip())
        if len(items) >= limit:
            break
    return items


def gather_environment(root: Path) -> dict[str, str]:
    python_result = run_command([sys.executable, "--version"], root)
    pip_result = run_command([sys.executable, "-m", "pip", "--version"], root)
    conda_value = "not found"
    conda_path = shutil.which("conda")
    if conda_path:
        conda_result = run_command([conda_path, "--version"], root)
        conda_value = conda_result.stdout.strip() or conda_result.stderr.strip() or "not found"
    return {
        "python": python_result.stdout.strip() or python_result.stderr.strip() or "unavailable",
        "pip": pip_result.stdout.strip() or pip_result.stderr.strip() or "unavailable",
        "conda": conda_value,
    }


def infer_install_commands(root: Path) -> list[list[str]]:
    commands: list[list[str]] = []
    if (root / "pyproject.toml").exists():
        commands.append([sys.executable, "-m", "pip", "install", "-e", "."])
    elif (root / "package.json").exists():
        commands.append(["npm", "install"])
    return commands


def resolve_install_commands(config: dict[str, Any], root: Path) -> list[list[str]]:
    configured = config.get("install_commands", [])
    if configured:
        return [item if isinstance(item, list) else [str(item)] for item in configured]
    if config.get("infer_install_commands", True):
        return infer_install_commands(root)
    return []


def maybe_install(root: Path, commands: list[list[str]], dry_run: bool) -> list[CommandResult]:
    if dry_run:
        return [CommandResult(0, "dry-run", "") for _ in commands]
    return [run_command(command, root) for command in commands]


def safe_fix_directories(root: Path, config: dict[str, Any], dry_run: bool) -> list[str]:
    created: list[str] = []
    for name in config.get("safe_directories", []):
        path = root / name
        if not path.exists():
            if not dry_run:
                path.mkdir(parents=True, exist_ok=True)
            created.append(name)
    return created


def run_json_script(script: Path, cwd: Path) -> dict[str, Any]:
    if not script.exists():
        return {"error": f"Missing script: {script}"}
    result = run_command([sys.executable, str(script), "--root", str(cwd), "--json"], cwd)
    if result.returncode != 0:
        return {"error": result.stderr.strip() or result.stdout.strip()}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON output", "raw": result.stdout}


def resolve_support_script(config: dict[str, Any], key: str, explicit_path: Path | None, fallback_path: Path) -> Path:
    if explicit_path is not None:
        return explicit_path.resolve()
    support_scripts = dict(config.get("support_scripts", {}))
    configured = support_scripts.get(key)
    if configured:
        configured_path = Path(configured)
        return configured_path if configured_path.is_absolute() else configured_path.resolve()
    return fallback_path


def expand_candidate_patterns(root: Path, patterns: list[str], limit: int) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for pattern in patterns:
        for path in sorted(root.glob(pattern)):
            if not path.is_file():
                continue
            rel = path.relative_to(root).as_posix()
            if rel in seen:
                continue
            seen.add(rel)
            found.append(rel)
            if len(found) >= limit:
                return found
    return found


def build_doc_summary(root: Path, candidates: list[str]) -> list[str]:
    items: list[str] = []
    for relative in candidates:
        text = load_text(root / relative)
        if not text:
            continue
        for line in summarize_lines(text, limit=3):
            items.append(f"[{relative}] {line}")
            if len(items) >= 12:
                return items
    return items


def extract_task_summary(root: Path, doc_candidates: list[str]) -> list[str]:
    items: list[str] = []
    for relative in doc_candidates:
        text = load_text(root / relative)
        if not text:
            continue
        for raw in text.splitlines():
            line = raw.strip()
            if line.startswith("-"):
                items.append(line.lstrip("- ").strip())
            if len(items) >= 8:
                return items
    return items


def write_markdown(path: Path, content: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy_outputs(report_dir: Path, shared_dir: Path, mode: str, dry_run: bool) -> list[str]:
    if mode == "none":
        return []
    if mode != "local_copy":
        raise ValueError(f"Unsupported shared copy mode: {mode}")
    copied: list[str] = []
    for path in report_dir.glob("*.md"):
        target = shared_dir / path.name
        copied.append(target.as_posix())
        if not dry_run:
            shared_dir.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
    return copied


def build_welcome_email(language: str, tasks: list[str], doc_hints: list[str]) -> list[str]:
    if language.lower().startswith("zh"):
        lines = [
            "# Welcome To The Project",
            "",
            "你好，",
            "",
            "欢迎加入这个项目。下面是接手时最值得先阅读的内容和当前优先任务。",
            "",
            "建议优先阅读：",
            "",
        ]
        lines.extend(f"- {item}" for item in doc_hints[:4] or ["阅读项目 README 和开发文档。"])
        lines.extend(["", "当前优先任务：", ""])
        lines.extend(f"- {item}" for item in tasks[:5] or ["当前没有自动发现任务，请查看项目任务板。"])
        return lines

    lines = [
        "# Welcome To The Project",
        "",
        "Hello,",
        "",
        "Welcome to the project. Here are the most useful documents and current priorities for your takeover.",
        "",
        "Suggested reading order:",
        "",
    ]
    lines.extend(f"- {item}" for item in doc_hints[:4] or ["Start with the project README and onboarding docs."])
    lines.extend(["", "Current priorities:", ""])
    lines.extend(f"- {item}" for item in tasks[:5] or ["No task summary was detected automatically."])
    return lines


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    config, config_path = resolve_config(root, args.config)
    report_dir = args.report_dir if args.report_dir else Path(config.get("report_dir", "docs/takeover"))
    report_dir = report_dir if report_dir.is_absolute() else root / report_dir
    shared_dir = None if args.shared_dir is None else (args.shared_dir if args.shared_dir.is_absolute() else root / args.shared_dir)

    structure_script = resolve_support_script(
        config,
        "structure",
        args.structure_script,
        SKILLS_ROOT / "file-structure-check" / "scripts" / "check_file_structure.py",
    )
    docs_script = resolve_support_script(
        config,
        "docs",
        args.docs_script,
        SKILLS_ROOT / "documentation-governance" / "scripts" / "check_documentation_governance.py",
    )

    env_info = gather_environment(root)
    created_dirs = safe_fix_directories(root, config, args.dry_run) if args.apply_safe_fixes else []
    install_commands = resolve_install_commands(config, root)
    install_results = maybe_install(root, install_commands, args.dry_run) if args.install and install_commands else []

    structure_report = run_json_script(structure_script, root)
    docs_report = run_json_script(docs_script, root)

    doc_candidates = expand_candidate_patterns(root, list(config.get("doc_candidate_globs", [])), limit=16)
    priority_task_docs = expand_candidate_patterns(root, list(config.get("priority_task_globs", [])), limit=12)
    dev_rules = build_doc_summary(root, doc_candidates)
    tasks = extract_task_summary(root, priority_task_docs)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    takeover_report = [
        "# Project Takeover Report",
        "",
        f"- Generated at: `{now}`",
        f"- Root: `{root}`",
        f"- Config: `{config_path}`",
        f"- Structure script: `{structure_script}`",
        f"- Docs script: `{docs_script}`",
        f"- Dry run: `{'yes' if args.dry_run else 'no'}`",
        "",
        "## Environment Readiness",
        "",
        f"- Python: `{env_info['python']}`",
        f"- Pip: `{env_info['pip']}`",
        f"- Conda: `{env_info['conda']}`",
        "",
        "## Safe Fixes",
        "",
    ]
    takeover_report.extend(f"- Would create missing directory: `{name}/`" if args.dry_run else f"- Created missing directory: `{name}/`" for name in created_dirs or [])
    if not created_dirs:
        takeover_report.append("- No safe directory fixes applied")

    takeover_report.extend(["", "## Structure Check", ""])
    if structure_report.get("error"):
        takeover_report.append(f"- Structure check unavailable: `{structure_report['error']}`")
    else:
        takeover_report.append(f"- Profile: `{structure_report.get('profile', 'unknown')}`")
        takeover_report.append(f"- Missing directories: `{len(structure_report.get('missing_directories', []))}`")
        takeover_report.extend(f"- Missing: `{item}/`" for item in structure_report.get("missing_directories", []))
        takeover_report.extend(f"- Suggestion: {item}" for item in structure_report.get("suggested_fixes", [])[:6])

    takeover_report.extend(["", "## Documentation Governance", ""])
    if docs_report.get("error"):
        takeover_report.append(f"- Documentation governance unavailable: `{docs_report['error']}`")
    else:
        missing_sections = docs_report.get("readme", {}).get("missing_sections", [])
        takeover_report.append(f"- README missing sections: `{len(missing_sections)}`")
        takeover_report.extend(f"- Missing README section: `{item}`" for item in missing_sections)
        takeover_report.append(f"- Heading issues: `{len(docs_report.get('heading_issues', []))}`")

    takeover_report.extend(["", "## Current Development Rules", ""])
    takeover_report.extend(f"- {item}" for item in dev_rules or ["No development-rule summary available from configured document candidates"])
    takeover_report.extend(["", "## Current Task Summary", ""])
    takeover_report.extend(f"- {item}" for item in tasks or ["No task summary available from configured task documents"])

    if args.install:
        takeover_report.extend(["", "## Install Step", ""])
        if not install_commands:
            takeover_report.append("- No install commands were configured or inferred for this project")
        else:
            for command, result in zip(install_commands, install_results):
                verb = "Would run" if args.dry_run else "Command"
                takeover_report.append(f"- {verb}: `{' '.join(command)}` -> return code `{result.returncode}`")

    onboarding_summary = [
        "# Project Onboarding Summary",
        "",
        "## Suggested Reading",
        "",
    ]
    onboarding_summary.extend(f"- {item}" for item in dev_rules[:6] or ["Review the configured project documents for onboarding."])
    onboarding_summary.extend(["", "## Current Priorities", ""])
    onboarding_summary.extend(f"- {item}" for item in tasks[:5] or ["Review the configured task documents for current priorities."])

    welcome_email = build_welcome_email(str(config.get("welcome_language", "en")), tasks, dev_rules)

    report_path = report_dir / "project_takeover_report.md"
    onboarding_path = report_dir / "project_onboarding_summary.md"
    welcome_path = report_dir / "welcome_email.md"
    write_markdown(report_path, "\n".join(takeover_report) + "\n", args.dry_run)
    write_markdown(onboarding_path, "\n".join(onboarding_summary) + "\n", args.dry_run)
    write_markdown(welcome_path, "\n".join(welcome_email) + "\n", args.dry_run)

    copied: list[str] = []
    if shared_dir is not None:
        copied = copy_outputs(report_dir, shared_dir, str(config.get("shared_copy_mode", "local_copy")), args.dry_run)

    action = "Planned" if args.dry_run else "Takeover"
    print(f"{action} report: {report_path}")
    print(f"{action} onboarding summary: {onboarding_path}")
    print(f"{action} welcome email: {welcome_path}")
    if copied:
        print(f"Shared sync targets: {len(copied)}")
        for item in copied:
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
