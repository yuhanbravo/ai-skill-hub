from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


HOOK_TEMPLATE = """#!/usr/bin/env python3
import subprocess
from pathlib import Path

script_path = Path({script_path})
repo_root = Path({repo_root})
command = [{python_executable}, str(script_path), "--root", str(repo_root)]
result = subprocess.run(command, cwd=repo_root)
raise SystemExit(result.returncode)
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install a post-commit hook that refreshes the project status document.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Git repository root or a path inside it.")
    parser.add_argument("--script-path", type=Path, help="Override the status update script path written into the hook.")
    parser.add_argument("--python", type=Path, help="Override the Python executable written into the hook.")
    parser.add_argument("--dry-run", action="store_true", help="Preview the hook contents without writing the file.")
    return parser.parse_args()


def git_toplevel(root: Path) -> Path | None:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        return None
    return Path(result.stdout.strip())


def build_hook_text(repo_root: Path, script_path: Path, python_executable: Path) -> str:
    return HOOK_TEMPLATE.format(
        script_path=json.dumps(str(script_path)),
        repo_root=json.dumps(str(repo_root)),
        python_executable=json.dumps(str(python_executable)),
    )


def main() -> int:
    args = parse_args()
    top = git_toplevel(args.root.resolve())
    if top is None:
        print("No Git repository detected. Cannot install post-commit hook.")
        return 1

    script_path = args.script_path.resolve() if args.script_path else (Path(__file__).resolve().parents[0] / "update_project_status.py")
    python_executable = args.python.resolve() if args.python else Path(sys.executable).resolve()
    hook_path = top / ".git" / "hooks" / "post-commit"
    hook_text = build_hook_text(top, script_path, python_executable)

    if args.dry_run:
        print(f"Dry run hook target: {hook_path}")
        print(hook_text)
        return 0

    hook_path.parent.mkdir(parents=True, exist_ok=True)
    hook_path.write_text(hook_text, encoding="utf-8")
    print(f"Installed post-commit hook: {hook_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
