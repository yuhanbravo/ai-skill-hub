from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT_PATH = REPO_ROOT / "skills" / "update-project-status" / "scripts" / "update_project_status.py"


def run_command(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def load_expected(path: Path) -> dict[str, list[str]]:
    return json.loads(path.read_text(encoding="utf-8"))


def assert_stdout_contains(stdout: str, expected: dict[str, list[str]]) -> list[str]:
    diffs: list[str] = []
    for item in expected.get("stdout_contains", []):
        if item not in stdout:
            diffs.append(f"missing stdout fragment: {item}")
    return diffs


def copy_sample_repo(source: Path) -> Path:
    temp_dir = Path(tempfile.mkdtemp(prefix="update-project-status-test-"))
    shutil.copytree(source, temp_dir / "repo", dirs_exist_ok=True)
    return temp_dir / "repo"


def run_git(temp_repo: Path, *args: str) -> None:
    result = run_command(["git", *args], temp_repo)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or f"git {' '.join(args)} failed")


def initialize_git_history(temp_repo: Path) -> None:
    run_git(temp_repo, "init")
    run_git(temp_repo, "config", "user.name", "Skill Test")
    run_git(temp_repo, "config", "user.email", "skill-test@example.com")
    run_git(temp_repo, "add", ".")
    run_git(temp_repo, "commit", "-m", "feat: add sample feature")
    notes_path = temp_repo / "BUGFIX.md"
    notes_path.write_text("# Bugfix\n\nPatched sample issue.\n", encoding="utf-8")
    run_git(temp_repo, "add", "BUGFIX.md")
    run_git(temp_repo, "commit", "-m", "fix: patch sample bug")


def run_git_mode_test(base_dir: Path) -> list[str]:
    expected = load_expected(base_dir / "expected_output.json")
    temp_repo = copy_sample_repo(base_dir / "sample_repo")
    try:
        initialize_git_history(temp_repo)
        command = [
            sys.executable,
            str(SCRIPT_PATH),
            "--root",
            str(temp_repo),
            "--config",
            str(base_dir / "status_config.json"),
            "--dry-run",
            "--limit",
            "5",
        ]
        result = run_command(command, REPO_ROOT)
        diffs = []
        if result.returncode != 0:
            diffs.append(f"git mode command returned {result.returncode}")
        diffs.extend(assert_stdout_contains(result.stdout, expected))
        return diffs
    finally:
        shutil.rmtree(temp_repo.parent, ignore_errors=True)


def run_workspace_mode_test(base_dir: Path) -> list[str]:
    expected = load_expected(base_dir / "expected_output_no_git.json")
    temp_repo = copy_sample_repo(base_dir / "sample_repo")
    try:
        command = [
            sys.executable,
            str(SCRIPT_PATH),
            "--root",
            str(temp_repo),
            "--config",
            str(base_dir / "status_config_no_git.json"),
            "--dry-run",
            "--limit",
            "5",
        ]
        result = run_command(command, REPO_ROOT)
        diffs = []
        if result.returncode != 0:
            diffs.append(f"workspace mode command returned {result.returncode}")
        diffs.extend(assert_stdout_contains(result.stdout, expected))
        if (temp_repo / "reports" / "no_git_status.md").exists() or (temp_repo / "reports" / "no_git_status.log").exists():
            diffs.append("dry-run wrote no-git status outputs")
        return diffs
    finally:
        shutil.rmtree(temp_repo.parent, ignore_errors=True)


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    diffs = [*run_git_mode_test(base_dir), *run_workspace_mode_test(base_dir)]
    if diffs:
        print("[FAIL] update-project-status")
        for diff in diffs:
            print(f"- {diff}")
        return 1
    print("[PASS] update-project-status")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
