from __future__ import annotations

import argparse
import sys
from pathlib import Path


CONTRACTS: dict[str, dict[str, str]] = {
    "consumer": {
        "canonical_dir": ".codex/skills",
        "canonical_label": "codex skills",
        "agents_reference": "../../../.codex/skills/",
        "github_reference": "../../.codex/skills/",
        "contract_label": ".codex/skills -> .agents/.github",
    },
    "hub": {
        "canonical_dir": "skills",
        "canonical_label": "canonical skills",
        "agents_reference": "../../../skills/",
        "github_reference": "../../skills/",
        "contract_label": "skills/ -> .agents/.github",
    },
}


def get_contract(mode: str) -> dict[str, str]:
    if mode not in CONTRACTS:
        raise ValueError(f"Unsupported mode: {mode}")
    return CONTRACTS[mode]


def list_canonical_skills(project_root, mode: str) -> set[str]:
    root = Path(project_root)
    canonical_dir = root / Path(get_contract(mode)["canonical_dir"])
    if not canonical_dir.is_dir():
        return set()

    return {
        entry.name
        for entry in canonical_dir.iterdir()
        if entry.is_dir() and not entry.name.startswith("_") and (entry / "SKILL.md").is_file()
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


def check_agents_reference(file_path, expected_reference: str) -> bool:
    path = Path(file_path)
    if not path.is_file():
        return False

    return expected_reference in path.read_text(encoding="utf-8")


def check_github_reference(file_path, expected_reference: str) -> bool:
    path = Path(file_path)
    if not path.is_file():
        return False

    return expected_reference in path.read_text(encoding="utf-8")


def check_consistency(project_root, mode: str = "consumer") -> dict:
    root = Path(project_root)
    contract = get_contract(mode)
    canonical_skills = list_canonical_skills(root, mode)
    agents_entries = list_agents_entries(root)
    github_entries = list_github_entries(root)

    wrong_reference_agents = sorted(
        skill_name
        for skill_name in agents_entries
        if not check_agents_reference(
            root / ".agents" / "skills" / skill_name / "SKILL.md",
            contract["agents_reference"],
        )
    )
    wrong_reference_github = sorted(
        skill_name
        for skill_name in github_entries
        if not check_github_reference(
            root / ".github" / "skills" / f"{skill_name}.md",
            contract["github_reference"],
        )
    )

    return {
        "missing_agents": sorted(canonical_skills - agents_entries),
        "missing_github": sorted(canonical_skills - github_entries),
        "orphan_agents": sorted(agents_entries - canonical_skills),
        "orphan_github": sorted(github_entries - canonical_skills),
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


def print_report(project_root: Path, result: dict, mode: str = "consumer") -> None:
    contract = get_contract(mode)
    canonical_skills = list_canonical_skills(project_root, mode)
    agents_entries = list_agents_entries(project_root)
    github_entries = list_github_entries(project_root)
    issue_count = sum(len(items) for items in result.values())
    ok_marker = get_status_marker("✔", "OK")
    fail_marker = get_status_marker("❌", "FAIL")

    print("[Adapter Governance Report]")
    print()
    print(f"Project root: {project_root.resolve()}")
    print(f"Mode: {mode}")
    print(f"Contract: {contract['contract_label']}")
    print(f"Expected agents reference prefix: {contract['agents_reference']}")
    print(f"Expected github reference prefix: {contract['github_reference']}")
    print(f"{ok_marker} {contract['canonical_label']}: {len(canonical_skills)}")
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
        description="Check adapter consistency for consumer-project adapters or hub-local wrappers."
    )
    parser.add_argument(
        "project_root",
        nargs="?",
        default=".",
        help="Project root to inspect. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--mode",
        choices=sorted(CONTRACTS),
        default="consumer",
        help="Select the adapter contract to validate. Defaults to consumer.",
    )
    args = parser.parse_args()

    project_root = Path(args.project_root)
    result = check_consistency(project_root, mode=args.mode)
    print_report(project_root, result, mode=args.mode)

    if any(result.values()):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
