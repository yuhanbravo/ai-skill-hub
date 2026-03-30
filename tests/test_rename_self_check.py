from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_not_contains(text: str, needle: str, message: str) -> None:
    if needle in text:
        raise AssertionError(message)


def check_no_old_hardcoded_paths() -> None:
    active_files = [
        "README.md",
        "AI_USAGE.md",
        "SKILLS_INDEX.md",
        "SYNC.md",
        "tools/README.zh-CN.md",
        "tools/export_bundle.ps1",
        "tools/import_bundle.ps1",
        "tools/sync_skill_from_project_to_hub.ps1",
        "tools/sync_skills_to_nongit_project.ps1",
    ]

    old_path = r"D:\dev\codex-skill-hub"
    failures: list[str] = []
    for relative_path in active_files:
        text = read_text(relative_path)
        if old_path in text:
            failures.append(f"{relative_path}: contains old hardcoded path {old_path}")

    if failures:
        raise AssertionError("\n".join(failures))


def check_bundle_defaults_use_new_name() -> None:
    bundle_related_files = [
        "tools/export_bundle.ps1",
        "tools/import_bundle.ps1",
        "tools/README.zh-CN.md",
        "SYNC.md",
    ]

    forbidden_fragments = [
        "codex-skill-hub_latest.bundle",
        "codex-skill-hub_",
        "codex-skill-hub.bundle",
    ]

    failures: list[str] = []
    for relative_path in bundle_related_files:
        text = read_text(relative_path)
        for fragment in forbidden_fragments:
            if fragment in text:
                failures.append(f"{relative_path}: still contains old bundle fragment {fragment}")

    if failures:
        raise AssertionError("\n".join(failures))


def check_canonical_name_in_entry_docs() -> None:
    readme_text = read_text("README.md")
    assert_true(readme_text.startswith("# ai-skill-hub\n"), "README.md must use ai-skill-hub as the H1 title")

    for relative_path in ["README.md", "AI_USAGE.md", "SKILLS_INDEX.md", "SYNC.md"]:
        text = read_text(relative_path)
        assert_true(
            "ai-skill-hub" in text,
            f"{relative_path} must mention ai-skill-hub as the canonical repository name",
        )


def check_legacy_name_is_not_primary_name() -> None:
    entry_files = [
        "README.md",
        "AI_USAGE.md",
        "SKILLS_INDEX.md",
        "SYNC.md",
    ]
    allowed_legacy_markers = [
        "legacy name",
        "Legacy repository name",
        "legacy 名称",
        "legacy 目录名",
    ]

    failures: list[str] = []
    for relative_path in entry_files:
        for line in read_text(relative_path).splitlines():
            if "codex-skill-hub" not in line:
                continue

            if any(marker in line for marker in allowed_legacy_markers):
                continue

            failures.append(f"{relative_path}: unexpected primary-name style legacy reference: {line.strip()}")

    if failures:
        raise AssertionError("\n".join(failures))


def main() -> int:
    check_no_old_hardcoded_paths()
    check_bundle_defaults_use_new_name()
    check_canonical_name_in_entry_docs()
    check_legacy_name_is_not_primary_name()
    print("Rename self-check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())