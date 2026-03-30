from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SCRIPT_PATH = ROOT / "tools" / "sync_skills_to_nongit_project.ps1"


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_sync(project_path: Path, *extra_args: str) -> subprocess.CompletedProcess[str]:
    command = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(SCRIPT_PATH),
        "-SkillHubPath",
        str(ROOT),
        "-ProjectPath",
        str(project_path),
        *extra_args,
    ]
    return subprocess.run(command, capture_output=True, text=True, check=True)


def get_skill_names() -> list[str]:
    return sorted(
        path.name
        for path in SKILLS_DIR.iterdir()
        if path.is_dir() and not path.name.startswith("_") and (path / "SKILL.md").exists()
    )


def assert_project_local_wrapper(wrapper_path: Path, expected_skill: str) -> None:
    text = wrapper_path.read_text(encoding="utf-8")
    assert_true(
        f"canonical_path: ../../../.codex/skills/{expected_skill}" in text,
        f"{wrapper_path} must point to project-local .codex skill path",
    )
    assert_true(
        "../../../skills/" not in text,
        f"{wrapper_path} must not point back to hub skills/",
    )


def assert_project_local_github_entry(entry_path: Path, expected_skill: str) -> None:
    text = entry_path.read_text(encoding="utf-8")
    assert_true(
        f"../../.codex/skills/{expected_skill}" in text,
        f"{entry_path} must point to project-local .codex skill path",
    )
    assert_true(
        "../../skills/" not in text,
        f"{entry_path} must not point back to hub skills/",
    )


def test_all_sync() -> None:
    expected_skills = get_skill_names()

    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir)
        (project_path / ".agents" / "skills" / "stale-skill").mkdir(parents=True, exist_ok=True)
        (project_path / ".agents" / "skills" / "stale-skill" / "SKILL.md").write_text(
            "canonical_path: ../../../.codex/skills/stale-skill\n- Read the project-local skill before execution.\n",
            encoding="utf-8",
        )
        (project_path / ".agents" / "skills" / "stale-skill.md").write_text(
            "- path: `.codex/skills/stale-skill`\nRead the project-local SKILL.md before execution.\n",
            encoding="utf-8",
        )
        (project_path / ".github" / "skills").mkdir(parents=True, exist_ok=True)
        (project_path / ".github" / "skills" / "stale-skill.md").write_text(
            "- Canonical skill path: `../../.codex/skills/stale-skill`\n- This compatibility entry is generated from the project-local .codex skill copy.\n",
            encoding="utf-8",
        )

        run_sync(project_path)

        codex_skills_root = project_path / ".codex" / "skills"
        agents_root = project_path / ".agents" / "skills"
        github_root = project_path / ".github" / "skills"

        actual_codex_skills = sorted(
            path.name
            for path in codex_skills_root.iterdir()
            if path.is_dir() and not path.name.startswith("_") and (path / "SKILL.md").exists()
        )
        actual_agents_wrappers = sorted(
            path.name
            for path in agents_root.iterdir()
            if path.is_dir() and (path / "SKILL.md").exists()
        )
        actual_github_entries = sorted(path.stem for path in github_root.glob("*.md"))

        assert_true(actual_codex_skills == expected_skills, "all sync must preserve full .codex skill coverage")
        assert_true(actual_agents_wrappers == expected_skills, "all sync must emit .agents wrappers for all skills")
        assert_true(actual_github_entries == expected_skills, "all sync must emit .github entries for all skills")
        assert_true((codex_skills_root / "_protocol").is_dir(), "all sync must keep _protocol under .codex/skills")
        assert_true((codex_skills_root / "_skillset_version.txt").is_file(), "all sync must write version metadata")

        for skill_name in expected_skills:
            assert_true((agents_root / f"{skill_name}.md").is_file(), f"missing flat .agents summary for {skill_name}")
            assert_project_local_wrapper(agents_root / skill_name / "SKILL.md", skill_name)
            assert_project_local_github_entry(github_root / f"{skill_name}.md", skill_name)

        assert_true(not (agents_root / "stale-skill").exists(), "all sync must remove stale generated .agents wrapper directories")
        assert_true(not (agents_root / "stale-skill.md").exists(), "all sync must remove stale generated .agents summaries")
        assert_true(not (github_root / "stale-skill.md").exists(), "all sync must remove stale generated .github entries")


def test_single_skill_sync() -> None:
    target_skill = "project-takeover"

    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir)
        run_sync(project_path, "-SkillName", target_skill)

        codex_skills_root = project_path / ".codex" / "skills"
        agents_root = project_path / ".agents" / "skills"
        github_root = project_path / ".github" / "skills"

        actual_codex_skills = sorted(
            path.name
            for path in codex_skills_root.iterdir()
            if path.is_dir() and not path.name.startswith("_") and (path / "SKILL.md").exists()
        )
        actual_agents_wrappers = sorted(
            path.name
            for path in agents_root.iterdir()
            if path.is_dir() and (path / "SKILL.md").exists()
        )
        actual_github_entries = sorted(path.stem for path in github_root.glob("*.md"))

        assert_true(actual_codex_skills == [target_skill], "single-skill sync must only materialize the requested .codex skill")
        assert_true(actual_agents_wrappers == [target_skill], "single-skill sync must only emit the requested .agents wrapper")
        assert_true(actual_github_entries == [target_skill], "single-skill sync must only emit the requested .github entry")
        assert_true((agents_root / f"{target_skill}.md").is_file(), "single-skill sync must emit the requested flat .agents summary")
        assert_true((codex_skills_root / "_skillset_version.txt").is_file(), "single-skill sync must still write version metadata")

        assert_project_local_wrapper(agents_root / target_skill / "SKILL.md", target_skill)
        assert_project_local_github_entry(github_root / f"{target_skill}.md", target_skill)


def main() -> int:
    test_all_sync()
    test_single_skill_sync()
    print("sync_skills_to_nongit_project smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())