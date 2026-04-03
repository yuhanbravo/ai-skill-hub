from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONVENTION_PATH = ROOT / "docs" / "governance" / "COMMIT_CONVENTION.md"
ALLOWED_TYPES = ("docs", "feat", "fix", "refactor", "test", "chore")
GENERIC_BODY_TOKENS = {"misc", "stuff", "update", "updates", "todo", "wip", "note", "notes"}
TYPE_PATTERN = "|".join(ALLOWED_TYPES)
SIMPLE_SUBJECT_RE = re.compile(rf"^(?P<type>{TYPE_PATTERN}): (?P<action>\S.+)$")
SCOPED_SUBJECT_RE = re.compile(
    rf"^(?P<type>{TYPE_PATTERN})\((?P<scope>[a-z0-9][a-z0-9\-]*)\): (?P<action>\S.+)$"
)
PHASE_SUBJECT_RE = re.compile(
    rf"^(?P<type>{TYPE_PATTERN}): Phase (?P<phase>\d+(?:\.\d+)?) - "
    rf"(?P<scope>[A-Za-z0-9][A-Za-z0-9\-]*) - (?P<action>\S.+)$"
)


def strip_comment_lines(lines: list[str]) -> list[str]:
    return [line.rstrip("\n") for line in lines if not line.startswith("#")]


def read_commit_message_file(path: Path) -> list[str]:
    return strip_comment_lines(path.read_text(encoding="utf-8").splitlines())


def extract_subject_and_body(lines: list[str]) -> tuple[str, list[str]]:
    meaningful_lines = [line for line in lines if line.strip()]
    if not meaningful_lines:
        raise ValueError("Commit message cannot be empty.")

    subject = meaningful_lines[0].strip()
    return subject, lines[1:]


def validate_subject(subject: str) -> list[str]:
    errors: list[str] = []
    phase_match = PHASE_SUBJECT_RE.match(subject)
    if phase_match:
        action = phase_match.group("action").lower()
        if any(token in action for token in ("scan", "understand", "audit", "report", "fix")):
            errors.append(
                "Phase subject appears to describe execution phases; reserve `Phase` for repository/system evolution."
            )
        return errors

    simple_match = SIMPLE_SUBJECT_RE.match(subject)
    if simple_match:
        if simple_match.group("action").startswith("Phase "):
            errors.append(
                "If subject starts with `Phase`, it must use `<type>: Phase <n>[.<m>] - <scope> - <action>`."
            )
        return errors

    scoped_match = SCOPED_SUBJECT_RE.match(subject)
    if scoped_match:
        if scoped_match.group("action").startswith("Phase "):
            errors.append(
                "If subject starts with `Phase`, it must use `<type>: Phase <n>[.<m>] - <scope> - <action>`."
            )
        return errors

    errors.append(
        "Subject must match `<type>: <action>`, `<type>(<scope>): <action>`, "
        "or `<type>: Phase <n>[.<m>] - <scope> - <action>`."
    )
    return errors


def validate_body(lines: list[str]) -> list[str]:
    errors: list[str] = []
    if not any(line.strip() for line in lines):
        return errors

    if lines and lines[0].strip():
        errors.append("Commit body must be separated from the subject by one blank line.")
        return errors

    body_lines = lines[1:]
    if not any(line.strip() for line in body_lines):
        errors.append("Commit body must include descriptive content after the blank separator.")
        return errors

    for line in body_lines:
        stripped = line.strip()
        if not stripped:
            continue

        content = stripped[2:].strip() if stripped.startswith("- ") else stripped
        if len(content) < 5:
            errors.append("Commit body lines must be descriptive text or `- ` list items.")
            break

        normalized = re.sub(r"[^a-z]+", "", content.lower())
        if normalized in GENERIC_BODY_TOKENS:
            errors.append("Commit body lines must be descriptive; avoid filler lines like `misc`, `stuff`, or `update`.")
            break

    return errors


def validate_message_lines(lines: list[str]) -> list[str]:
    subject, body_lines = extract_subject_and_body(lines)
    errors = validate_subject(subject)
    errors.extend(validate_body(body_lines))
    return errors


def validate_message_text(message_text: str) -> list[str]:
    return validate_message_lines(strip_comment_lines(message_text.splitlines()))


def get_latest_commit_message(repo_path: Path | None = None) -> str:
    command = ["git"]
    if repo_path is not None:
        command.extend(["-C", str(repo_path)])
    command.extend(["log", "-1", "--pretty=%B"])
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Failed to read latest commit message.")
    return result.stdout


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate ai-skill-hub commit messages.")
    parser.add_argument("message_file", nargs="?", help="Path to the commit message file from git commit-msg hook.")
    parser.add_argument(
        "--message",
        help="Validate an explicit commit message string instead of reading a file or git history.",
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="Repository path used when reading the latest commit message with --latest.",
    )
    parser.add_argument(
        "--latest",
        action="store_true",
        help="Validate the latest git commit message from the target repository.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.message is not None:
            errors = validate_message_text(args.message)
        elif args.latest:
            message = get_latest_commit_message(Path(args.repo).resolve())
            errors = validate_message_text(message)
        elif args.message_file:
            errors = validate_message_lines(read_commit_message_file(Path(args.message_file)))
        else:
            raise ValueError("Provide a commit message file, `--message`, or `--latest`.")
    except Exception as exc:  # pragma: no cover - CLI safety path
        print(f"[commit-convention-check] {exc}", file=sys.stderr)
        return 1

    if errors:
        print("[commit-convention-check] Commit message validation failed.", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        print(f"- See {CONVENTION_PATH}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
