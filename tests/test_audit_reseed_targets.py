from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "tools" / "audit_reseed_targets.ps1"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run_audit(output_path: Path, *project_paths: Path | str) -> subprocess.CompletedProcess[str]:
    command = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(SCRIPT_PATH),
        "-ProjectPaths",
        *[str(path) for path in project_paths],
        "-Format",
        "json",
        "-OutputPath",
        str(output_path),
    ]
    return subprocess.run(command, capture_output=True, text=True, check=False)


def run_audit_from_projects_file(output_path: Path, projects_file: Path) -> subprocess.CompletedProcess[str]:
    command = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(SCRIPT_PATH),
        "-ProjectsFile",
        str(projects_file),
        "-Format",
        "json",
        "-OutputPath",
        str(output_path),
    ]
    return subprocess.run(command, capture_output=True, text=True, check=False)


def load_projects(output_path: Path) -> list[dict[str, object]]:
    payload = json.loads(output_path.read_text(encoding="utf-8-sig"))
    return payload["projects"]


def get_project_record(projects: list[dict[str, object]], project_path: Path | str) -> dict[str, object]:
    expected_path = str(project_path)
    for project in projects:
        if project["ProjectPath"] == expected_path:
            return project
    raise AssertionError(f"missing audit record for {expected_path}")


def test_already_seeded_detection() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir) / "already-seeded"
        write_file(project_path / ".codex" / "skills" / "project-takeover" / "SKILL.md", "# skill\n")
        write_file(
            project_path / ".codex" / "skills" / "_skillset_version.txt",
            "source_hub=ai-skill-hub\nsource_path=D:\\dev\\ai-skill-hub\nsynced_at=2026-04-01T10:00:00+08:00\nrobocopy_exit_code=1\n",
        )
        write_file(project_path / ".codex" / "skill-config" / "project-takeover.json", "{}\n")
        output_path = Path(temp_dir) / "already_seeded.json"

        result = run_audit(output_path, project_path)

        assert result.returncode == 0, result.stderr
        project = get_project_record(load_projects(output_path), project_path)
        assert project["SeedStatus"] == "already_seeded"
        assert project["RiskLevel"] == "low"
        assert project["HasSkillsetVersion"] is True
        assert project["SourceHub"] == "ai-skill-hub"
        assert project["SourcePath"] == "D:\\dev\\ai-skill-hub"


def test_ready_for_reseed_detection() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir) / "ready-for-reseed"
        write_file(project_path / ".codex" / "skills" / "project-takeover" / "SKILL.md", "# skill\n")
        write_file(
            project_path / ".codex" / "skills" / "_skillset_version.txt",
            "source_hub=codex-skill-hub\nsource_path=D:\\dev\\codex-skill-hub\n",
        )
        write_file(project_path / ".codex" / "skill-config" / "project-takeover.json", "{}\n")
        output_path = Path(temp_dir) / "ready_for_reseed.json"

        result = run_audit(output_path, project_path)

        assert result.returncode == 0, result.stderr
        project = get_project_record(load_projects(output_path), project_path)
        assert project["SeedStatus"] == "ready_for_reseed"
        assert project["RecommendedAction"] == "dryrun_then_reseed"
        assert project["SourceHub"] == "codex-skill-hub"


def test_missing_config_detection() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir) / "missing-config"
        write_file(project_path / ".agents" / "skills" / "project-takeover" / "SKILL.md", "# skill\n")
        write_file(project_path / ".github" / "skills" / "project-takeover.md", "# wrapper\n")
        output_path = Path(temp_dir) / "missing_config.json"

        result = run_audit(output_path, project_path)

        assert result.returncode == 0, result.stderr
        project = get_project_record(load_projects(output_path), project_path)
        assert project["SeedStatus"] == "missing_config"
        assert project["RecommendedAction"] == "restore_or_create_skill_config"


def test_risky_manual_review_detection() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir) / "risky-review"
        write_file(project_path / ".codex" / "skills" / "project-takeover" / "SKILL.md", "# skill\n")
        write_file(project_path / ".codex" / "skill-config" / "project-takeover.json", "{}\n")
        (project_path / ".codex" / "_backup_before_reset").mkdir(parents=True, exist_ok=True)
        output_path = Path(temp_dir) / "risky_manual_review.json"

        result = run_audit(output_path, project_path)

        assert result.returncode == 0, result.stderr
        project = get_project_record(load_projects(output_path), project_path)
        assert project["SeedStatus"] == "risky_manual_review"
        assert project["RecommendedAction"] == "manual_review_backup"
        assert project["HasBackupDir"] is True


def test_no_skill_structure_detection() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir) / "no-skills"
        project_path.mkdir(parents=True, exist_ok=True)
        output_path = Path(temp_dir) / "no_skill_structure.json"

        result = run_audit(output_path, project_path)

        assert result.returncode == 0, result.stderr
        project = get_project_record(load_projects(output_path), project_path)
        assert project["SeedStatus"] == "no_skill_structure"
        assert project["RecommendedAction"] == "verify_project_first"


def test_hub_repository_detection() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir) / "hub-repository"
        (project_path / "skills").mkdir(parents=True, exist_ok=True)
        write_file(project_path / "tools" / "sync_skills_to_nongit_project.ps1", "# sync\n")
        write_file(project_path / "VERSION", "1\n")
        write_file(project_path / "README.md", "# hub\n")
        output_path = Path(temp_dir) / "hub_repository.json"

        result = run_audit(output_path, project_path)

        assert result.returncode == 0, result.stderr
        project = get_project_record(load_projects(output_path), project_path)
        assert project["SeedStatus"] == "hub_repository"
        assert project["RecommendedAction"] == "skip_hub_repo"
        assert project["IsHubRepository"] is True
        assert "skills_root" in project["HubSignals"]
        assert "sync_script" in project["HubSignals"]
        assert project["SeedStatus"] != "ready_for_reseed"


def test_inaccessible_project_does_not_break_batch() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        seeded_project = Path(temp_dir) / "seeded"
        missing_project = Path(temp_dir) / "missing"
        write_file(seeded_project / ".codex" / "skills" / "project-takeover" / "SKILL.md", "# skill\n")
        write_file(seeded_project / ".codex" / "skills" / "_skillset_version.txt", "source_hub=ai-skill-hub\n")
        write_file(seeded_project / ".codex" / "skill-config" / "project-takeover.json", "{}\n")
        projects_file = Path(temp_dir) / "projects.txt"
        projects_file.write_text(f"{seeded_project}\n{missing_project}\n", encoding="utf-8")
        output_path = Path(temp_dir) / "batch.json"

        result = run_audit_from_projects_file(output_path, projects_file)

        assert result.returncode == 0, result.stderr
        projects = load_projects(output_path)
        seeded_record = get_project_record(projects, seeded_project)
        missing_record = get_project_record(projects, missing_project)
        assert seeded_record["SeedStatus"] == "already_seeded"
        assert missing_record["SeedStatus"] == "inaccessible"
        assert len(projects) == 2


if __name__ == "__main__":
    for name, value in sorted(globals().items()):
        if name.startswith("test_") and callable(value):
            value()
    print("ok")
