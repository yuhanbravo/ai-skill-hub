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


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    expected = load_expected(base_dir / "expected_output.json")
    temp_repo = copy_sample_repo(base_dir / "sample_repo")
    command = python_command(
        str(REPO_ROOT / ".codex" / "skills" / "project-takeover" / "scripts" / "project_takeover.py"),
        "--root",
        str(temp_repo),
        "--config",
        str(base_dir / "takeover_config.json"),
        "--dry-run",
    )
    result = run_command(command, REPO_ROOT)
    diffs: list[str] = []
    if result.returncode != 0:
        diffs.append(f"command returned {result.returncode}")
    diffs.extend(compare_stdout(result.stdout, expected))
    passed, message = format_result("project-takeover", diffs, result.stderr)
    print(message)
    cleanup_temp_dir(temp_repo)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
