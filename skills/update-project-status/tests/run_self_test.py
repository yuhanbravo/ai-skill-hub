from __future__ import annotations

from pathlib import Path

from test_support import (
    REPO_ROOT,
    cleanup_temp_dir,
    compare_stdout,
    copy_sample_repo,
    format_result,
    load_expected,
    python_command,
    run_command,
)


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


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    expected = load_expected(base_dir / "expected_output.json")
    temp_repo = copy_sample_repo(base_dir / "sample_repo")
    diffs: list[str] = []
    try:
        initialize_git_history(temp_repo)
        command = python_command(
            str(REPO_ROOT / ".codex" / "skills" / "update-project-status" / "scripts" / "update_project_status.py"),
            "--root",
            str(temp_repo),
            "--config",
            str(base_dir / "status_config.json"),
            "--dry-run",
            "--limit",
            "5",
        )
        result = run_command(command, REPO_ROOT)
        if result.returncode != 0:
            diffs.append(f"command returned {result.returncode}")
        diffs.extend(compare_stdout(result.stdout, expected))
        passed, message = format_result("update-project-status", diffs, result.stderr)
        print(message)
        return 0 if passed else 1
    except RuntimeError as exc:
        passed, message = format_result("update-project-status", [str(exc)])
        print(message)
        return 1
    finally:
        cleanup_temp_dir(temp_repo)


if __name__ == "__main__":
    raise SystemExit(main())
