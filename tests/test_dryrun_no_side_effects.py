from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "tools" / "sync_skills_to_nongit_project.ps1"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def snapshot_tree(root: Path) -> list[str]:
    if not root.exists():
        return []

    snapshot: list[str] = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative_path = path.relative_to(root).as_posix()
        snapshot.append(f"{relative_path}|{path.read_text(encoding='utf-8')}")
    return snapshot


def test_sync_dryrun_has_no_side_effects() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir)
        agents_root = project_path / ".agents" / "skills"
        github_root = project_path / ".github" / "skills"
        codex_skills_root = project_path / ".codex" / "skills"

        write_file(agents_root / "custom-note.md", "keep this agent file\n")
        write_file(github_root / "custom-note.md", "keep this github file\n")

        before_agents = snapshot_tree(agents_root)
        before_github = snapshot_tree(github_root)

        result = subprocess.run(
            [
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
                "-DryRun",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        after_agents = snapshot_tree(agents_root)
        after_github = snapshot_tree(github_root)

        assert result.returncode == 0, result.stderr
        assert "[PLAN]" in result.stdout
        assert not codex_skills_root.exists()
        assert before_agents == after_agents
        assert before_github == after_github


def test_sync_dryrun_preserves_existing_codex_and_adapters() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir)
        codex_skills_root = project_path / ".codex" / "skills"
        agents_root = project_path / ".agents" / "skills"
        github_root = project_path / ".github" / "skills"

        write_file(codex_skills_root / "existing-skill" / "SKILL.md", "# existing skill\n")
        write_file(codex_skills_root / "_skillset_version.txt", "skillset_version=existing\n")
        write_file(agents_root / "custom-note.md", "keep this agent file\n")
        write_file(github_root / "custom-note.md", "keep this github file\n")

        before_codex = snapshot_tree(codex_skills_root)
        before_agents = snapshot_tree(agents_root)
        before_github = snapshot_tree(github_root)

        result = subprocess.run(
            [
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
                "-DryRun",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        after_codex = snapshot_tree(codex_skills_root)
        after_agents = snapshot_tree(agents_root)
        after_github = snapshot_tree(github_root)

        assert result.returncode == 0, result.stderr
        assert "[PLAN]" in result.stdout
        assert before_codex == after_codex
        assert before_agents == after_agents
        assert before_github == after_github
