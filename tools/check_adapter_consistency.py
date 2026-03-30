from __future__ import annotations

import argparse
import sys
from pathlib import Path


def list_codex_skills(project_root) -> set[str]:
    root = Path(project_root)
    codex_skills_dir = root / ".codex" / "skills"
    if not codex_skills_dir.is_dir():
        return set()

    return {
        entry.name
        for entry in codex_skills_dir.iterdir()
        if entry.is_dir() and entry.name != "_protocol" and (entry / "SKILL.md").is_file()
    }


def list_agents_entries(project_root) -> set[str]:
    root = Path(project_root)
    agents_dir = root / ".agents" / "skills"
    if not agents_dir.is_dir():
        return set()

    return {
        entry.name
        for entry in agents_dir.iterdir()
        if entry.is_dir() and (entry / "SKILL.md").is_file()
    }


def list_github_entries(project_root) -> set[str]:
    root = Path(project_root)
    github_dir = root / ".github" / "skills"
    if not github_dir.is_dir():
        return set()

    return {
        entry.stem
        for entry in github_dir.glob("*.md")
        if entry.stem.lower() != "readme"
    }


def check_agents_reference(file_path) -> bool:
    path = Path(file_path)
    if not path.is_file():
        return False

    return "../../../.codex/skills/" in path.read_text(encoding="utf-8")


def check_github_reference(file_path) -> bool:
    path = Path(file_path)
    if not path.is_file():
        return False

    return "../../.codex/skills/" in path.read_text(encoding="utf-8")


def check_consistency(project_root) -> dict:
    root = Path(project_root)
    codex_skills = list_codex_skills(root)
    agents_entries = list_agents_entries(root)
    github_entries = list_github_entries(root)

    wrong_reference_agents = sorted(
        skill_name
        for skill_name in agents_entries
        if not check_agents_reference(root / ".agents" / "skills" / skill_name / "SKILL.md")
    )
    wrong_reference_github = sorted(
        skill_name
        for skill_name in github_entries
        if not check_github_reference(root / ".github" / "skills" / f"{skill_name}.md")
    )

    return {
        "missing_agents": sorted(codex_skills - agents_entries),
        "missing_github": sorted(codex_skills - github_entries),
        "orphan_agents": sorted(agents_entries - codex_skills),
        "orphan_github": sorted(github_entries - codex_skills),
        "wrong_reference_agents": wrong_reference_agents,
        "wrong_reference_github": wrong_reference_github,
    }


def format_items(items: list[str]) -> str:
    return ", ".join(items) if items else "none"


def get_status_marker(unicode_marker: str, ascii_marker: str) -> str:
    encoding = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        unicode_marker.encode(encoding)
    except UnicodeEncodeError:
        return ascii_marker
    return unicode_marker


def print_report(project_root: Path, result: dict) -> None:
    codex_skills = list_codex_skills(project_root)
    agents_entries = list_agents_entries(project_root)
    github_entries = list_github_entries(project_root)
    issue_count = sum(len(items) for items in result.values())
    ok_marker = get_status_marker("✔", "OK")
    fail_marker = get_status_marker("❌", "FAIL")

    print("[Adapter Governance Report]")
    print()
    print(f"Project root: {project_root.resolve()}")
    print(f"{ok_marker} codex skills: {len(codex_skills)}")
    print(f"{ok_marker} agents entries: {len(agents_entries)}")
    print(f"{ok_marker} github entries: {len(github_entries)}")
    print()
    print("[Missing]")
    print(f"- agents: {format_items(result['missing_agents'])}")
    print(f"- github: {format_items(result['missing_github'])}")
    print()
    print("[Orphan]")
    print(f"- agents: {format_items(result['orphan_agents'])}")
    print(f"- github: {format_items(result['orphan_github'])}")
    print()
    print("[Wrong Reference]")
    print(f"- agents: {format_items(result['wrong_reference_agents'])}")
    print(f"- github: {format_items(result['wrong_reference_github'])}")
    print()
    print("Summary:")
    if issue_count == 0:
        print(f"{ok_marker} No issues detected.")
    else:
        print(f"{fail_marker} Issues detected: {issue_count}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check adapter consistency between .codex/skills and project-local .agents/.github adapters."
    )
    parser.add_argument(
        "project_root",
        nargs="?",
        default=".",
        help="Project root to inspect. Defaults to the current working directory.",
    )
    args = parser.parse_args()

    project_root = Path(args.project_root)
    result = check_consistency(project_root)
    print_report(project_root, result)

    if any(result.values()):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())