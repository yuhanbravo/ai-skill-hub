from __future__ import annotations

import argparse
import re
from difflib import unified_diff
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEMANTIC_MIRROR_PAIRS = [
    {
        "source": Path("docs/HANDOFF.md"),
        "mirror": Path("docs/bridge/HANDOFF.md"),
    },
    {
        "source": Path("docs/status/skill-hub-status.md"),
        "mirror": Path("docs/bridge/status/skill-hub-status.md"),
    },
]
ALLOWED_BRIDGE_COPY_PATHS = [
    Path("docs/bridge/SKILLS_INDEX.md"),
    Path("docs/bridge/templates/EXECUTION_REPORT_TEMPLATE.md"),
    Path("docs/bridge/templates/TASK_PACKAGE_TEMPLATE.md"),
]
INLINE_INPUT_EXAMPLE_PATTERN = re.compile(r"^### Input Example\s*$", re.MULTILINE)


def normalize_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized_lines = [line.rstrip() for line in normalized.split("\n")]
    return "\n".join(normalized_lines).strip() + "\n"


def strip_allowed_bridge_preamble(text: str) -> tuple[str, bool]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if len(lines) < 2:
        return text, False

    title_line = lines[0].rstrip()
    index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1

    preamble_start = index
    saw_blockquote = False
    while index < len(lines):
        stripped = lines[index].lstrip()
        if stripped.startswith(">"):
            saw_blockquote = True
            index += 1
            continue
        if saw_blockquote and not stripped:
            index += 1
            continue
        break

    if not saw_blockquote:
        return text, False

    remainder = "\n".join(lines[index:]).lstrip("\n")
    if not remainder:
        return f"{title_line}\n", True
    return f"{title_line}\n\n{remainder}\n", True


def build_diff_preview(source_text: str, mirror_text: str, source_rel: Path, mirror_rel: Path, *, max_lines: int) -> list[str]:
    diff_lines = list(
        unified_diff(
            source_text.splitlines(),
            mirror_text.splitlines(),
            fromfile=source_rel.as_posix(),
            tofile=mirror_rel.as_posix(),
            lineterm="",
        )
    )
    return diff_lines[:max_lines]


def audit_bridge_semantic_mirrors(root: Path, *, preview_lines: int = 12) -> dict[str, object]:
    pair_results: list[dict[str, object]] = []
    for pair in SEMANTIC_MIRROR_PAIRS:
        source_rel = Path(pair["source"])
        mirror_rel = Path(pair["mirror"])
        source_path = root / source_rel
        mirror_path = root / mirror_rel

        if not source_path.exists():
            pair_results.append(
                {
                    "status": "ERROR",
                    "source": source_rel.as_posix(),
                    "mirror": mirror_rel.as_posix(),
                    "message": "Active source is missing; semantic mirror audit could not run.",
                    "preamble_stripped": False,
                    "diff_preview": [],
                }
            )
            continue

        if not mirror_path.exists():
            pair_results.append(
                {
                    "status": "ERROR",
                    "source": source_rel.as_posix(),
                    "mirror": mirror_rel.as_posix(),
                    "message": "Bridge semantic mirror is missing; semantic mirror audit could not run.",
                    "preamble_stripped": False,
                    "diff_preview": [],
                }
            )
            continue

        normalized_source = normalize_text(source_path.read_text(encoding="utf-8"))
        stripped_mirror_text, preamble_stripped = strip_allowed_bridge_preamble(
            mirror_path.read_text(encoding="utf-8")
        )
        normalized_mirror = normalize_text(stripped_mirror_text)

        if normalized_source == normalized_mirror:
            pair_results.append(
                {
                    "status": "INFO",
                    "source": source_rel.as_posix(),
                    "mirror": mirror_rel.as_posix(),
                    "message": "No semantic drift detected after stripping the allowed bridge preamble.",
                    "preamble_stripped": preamble_stripped,
                    "diff_preview": [],
                }
            )
            continue

        pair_results.append(
            {
                "status": "ERROR",
                "source": source_rel.as_posix(),
                "mirror": mirror_rel.as_posix(),
                "message": "Semantic drift detected after stripping the allowed bridge preamble.",
                "preamble_stripped": preamble_stripped,
                "diff_preview": build_diff_preview(
                    normalized_source,
                    normalized_mirror,
                    source_rel,
                    mirror_rel,
                    max_lines=preview_lines,
                ),
            }
        )

    skip_results = [
        {
            "status": "SKIP",
            "path": path.as_posix(),
            "message": "Intentional bridge copy; excluded from semantic mirror drift comparison.",
        }
        for path in ALLOWED_BRIDGE_COPY_PATHS
    ]

    return {
        "pair_results": pair_results,
        "skip_results": skip_results,
    }


def iter_skill_directories(root: Path) -> list[Path]:
    skills_dir = root / "skills"
    if not skills_dir.exists():
        return []

    return sorted(
        skill_dir
        for skill_dir in skills_dir.iterdir()
        if skill_dir.is_dir() and not skill_dir.name.startswith("_")
    )


def audit_invocation_example_sources(root: Path) -> dict[str, object]:
    skill_dirs = iter_skill_directories(root)
    example_file_hits: list[str] = []
    inline_skill_hits: list[str] = []
    missing_example_files: list[str] = []

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        example_file = skill_dir / "examples" / "invocation_examples.md"

        skill_text = skill_file.read_text(encoding="utf-8") if skill_file.exists() else ""
        if INLINE_INPUT_EXAMPLE_PATTERN.search(skill_text):
            inline_skill_hits.append(skill_dir.name)

        if not example_file.exists():
            missing_example_files.append(skill_dir.name)
            continue

        example_text = example_file.read_text(encoding="utf-8")
        if INLINE_INPUT_EXAMPLE_PATTERN.search(example_text):
            example_file_hits.append(skill_dir.name)

    extractor_file = root / "tools" / "generate_skill_metadata.py"
    extractor_text = extractor_file.read_text(encoding="utf-8") if extractor_file.exists() else ""
    extractor_expects_inline_skill_examples = (
        "def extract_invocation_example" in extractor_text
        and "## Invocation" in extractor_text
        and "### Input Example" in extractor_text
        and "invocation_examples.md" not in extractor_text
    )

    stale_assumption = bool(example_file_hits) and not inline_skill_hits and extractor_expects_inline_skill_examples
    fresh_regeneration_risk = stale_assumption

    return {
        "skill_count": len(skill_dirs),
        "skills_with_example_file_input_examples": example_file_hits,
        "skills_with_inline_input_examples": inline_skill_hits,
        "skills_missing_example_files": missing_example_files,
        "extractor_expects_inline_skill_examples": extractor_expects_inline_skill_examples,
        "stale_assumption": stale_assumption,
        "fresh_regeneration_risk": fresh_regeneration_risk,
        "extractor_path": extractor_file.relative_to(root).as_posix() if extractor_file.exists() else "tools/generate_skill_metadata.py",
    }


def render_report(root: Path, bridge_audit: dict[str, object], metadata_audit: dict[str, object]) -> str:
    lines = [
        "[Derivative Surface Audit]",
        "Mode: read-only / non-gating",
        f"Repository root: {root}",
        "",
        "== Bridge Semantic Mirror Drift Audit ==",
    ]

    for result in bridge_audit["pair_results"]:
        if result["preamble_stripped"]:
            lines.append(
                f"INFO stripped allowed bridge preamble before comparison: {result['mirror']}"
            )
        lines.append(
            f"{result['status']} {result['source']} -> {result['mirror']}: {result['message']}"
        )
        for diff_line in result["diff_preview"]:
            lines.append(f"  {diff_line}")

    for skip in bridge_audit["skip_results"]:
        lines.append(f"{skip['status']} {skip['path']}: {skip['message']}")

    lines.extend(
        [
            "",
            "== Invocation-Example Source Drift Audit ==",
            f"INFO scanned canonical skills: {metadata_audit['skill_count']}",
            (
                "INFO canonical example files with Input Example blocks: "
                f"{len(metadata_audit['skills_with_example_file_input_examples'])}/"
                f"{metadata_audit['skill_count']}"
            ),
            (
                "INFO inline SKILL.md Input Example blocks: "
                f"{len(metadata_audit['skills_with_inline_input_examples'])}/"
                f"{metadata_audit['skill_count']}"
            ),
        ]
    )

    missing_example_files = metadata_audit["skills_missing_example_files"]
    if missing_example_files:
        lines.append(
            "ERROR missing canonical invocation example files: "
            + ", ".join(missing_example_files)
        )
    else:
        lines.append("INFO every scanned canonical skill has an invocation_examples.md file.")

    if metadata_audit["extractor_expects_inline_skill_examples"]:
        lines.append(
            "ERROR stale extractor assumption: "
            f"{metadata_audit['extractor_path']} still expects an inline SKILL.md "
            "'### Input Example' block."
        )
    else:
        lines.append(
            "INFO extractor does not require the legacy inline SKILL.md Input Example pattern."
        )

    if metadata_audit["fresh_regeneration_risk"]:
        lines.append(
            "ERROR fresh regeneration risk: canonical invocation examples live in example files, "
            "but the metadata extractor still reads the legacy inline location."
        )
    else:
        lines.append("INFO no fresh-regeneration source drift detected.")

    lines.extend(
        [
            "",
            "Summary:",
            "INFO findings are report-only; this audit does not rewrite mirrors, refresh metadata, or block by default.",
            (
                "INFO bridge semantic drift findings: "
                + str(
                    sum(
                        1
                        for result in bridge_audit["pair_results"]
                        if result["status"] == "ERROR"
                    )
                )
            ),
            (
                "INFO metadata source drift findings: "
                + str(
                    int(bool(missing_example_files))
                    + int(bool(metadata_audit["stale_assumption"]))
                    + int(bool(metadata_audit["fresh_regeneration_risk"]))
                )
            ),
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Read-only audit for bridge semantic mirror drift and invocation-example source drift."
    )
    parser.add_argument(
        "--root",
        default=str(ROOT),
        help="Repository root to audit. Defaults to the current repository root.",
    )
    parser.add_argument(
        "--preview-lines",
        type=int,
        default=12,
        help="Maximum number of unified-diff preview lines to show for each semantic drift.",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    bridge_audit = audit_bridge_semantic_mirrors(root, preview_lines=max(args.preview_lines, 0))
    metadata_audit = audit_invocation_example_sources(root)
    print(render_report(root, bridge_audit, metadata_audit), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
