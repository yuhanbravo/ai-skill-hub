from __future__ import annotations

import importlib.util
import io
import shutil
from contextlib import contextmanager, redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "tools" / "audit_derivative_surfaces.py"
LOCAL_TMP_ROOT = ROOT / ".tmp" / "test_derivative_surface_audit"


def assert_equal(actual: object, expected: object, message: str) -> None:
    if actual != expected:
        raise AssertionError(f"{message}: expected={expected!r}, actual={actual!r}")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_module():
    spec = importlib.util.spec_from_file_location("audit_derivative_surfaces", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Failed to load derivative surface audit module.")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


@contextmanager
def temporary_directory():
    LOCAL_TMP_ROOT.mkdir(parents=True, exist_ok=True)
    temp_dir = LOCAL_TMP_ROOT / "workdir"
    shutil.rmtree(temp_dir, ignore_errors=True)
    temp_dir.mkdir(parents=True, exist_ok=True)
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


def build_sample_repo(root: Path) -> None:
    write_file(
        root / "docs" / "HANDOFF.md",
        "# HANDOFF\n\nThis file is the single source of truth for project handoff.\n\n## Current Status\n\nActive handoff body.\n",
    )
    write_file(
        root / "docs" / "bridge" / "HANDOFF.md",
        "# HANDOFF\n\n> Status: semantic mirror of active source [../HANDOFF.md](../HANDOFF.md)\n>\n> Ownership: active updates continue in `docs/HANDOFF.md`\n>\n> Purpose: bridge-facing handoff continuity\n\nThis file is the single source of truth for project handoff.\n\n## Current Status\n\nBridge copy drifted body.\n",
    )
    write_file(
        root / "docs" / "status" / "skill-hub-status.md",
        "# Skill Hub Status\n\n- Updated at: `2026-04-07`\n- Scope: `ai-skill-hub`\n",
    )
    write_file(
        root / "docs" / "bridge" / "status" / "skill-hub-status.md",
        "# Skill Hub Status\n\n> Status: semantic mirror of active source [../../status/skill-hub-status.md](../../status/skill-hub-status.md)\n>\n> Ownership: active updates continue in `docs/status/skill-hub-status.md`\n>\n> Purpose: bridge-facing status continuity\n\n- Updated at: `2026-04-01`\n- Scope: `ai-skill-hub`\n",
    )
    write_file(
        root / "docs" / "bridge" / "SKILLS_INDEX.md",
        "# SKILLS_INDEX\n\n> Status: bridge-facing copy of active source [../../SKILLS_INDEX.md](../../SKILLS_INDEX.md)\n",
    )
    write_file(
        root / "docs" / "bridge" / "templates" / "EXECUTION_REPORT_TEMPLATE.md",
        "# EXECUTION REPORT TEMPLATE\n\n> Status: bridge-facing copy of active source\n",
    )
    write_file(
        root / "docs" / "bridge" / "templates" / "TASK_PACKAGE_TEMPLATE.md",
        "# TASK PACKAGE TEMPLATE\n\n> Status: bridge-facing copy of active source\n",
    )
    write_file(
        root / "skills" / "alpha" / "SKILL.md",
        "# Alpha\n\n## Invocation\n\n### When to use\n\n- Use alpha.\n",
    )
    write_file(
        root / "skills" / "alpha" / "examples" / "invocation_examples.md",
        "# Invocation Examples\n\n### Input Example\n\n```text\nUse alpha for this task.\n```\n",
    )
    write_file(
        root / "skills" / "beta" / "SKILL.md",
        "# Beta\n\n## Invocation\n\n### When to use\n\n- Use beta.\n",
    )
    write_file(
        root / "skills" / "beta" / "examples" / "invocation_examples.md",
        "# Invocation Examples\n\n### Input Example\n\n```text\nUse beta for this task.\n```\n",
    )
    write_file(
        root / "tools" / "generate_skill_metadata.py",
        "import re\n\n"
        "def extract_invocation_example(text: str) -> str:\n"
        "    match = re.search(\n"
        '        r"## Invocation\\\\s+.*?### Input Example\\\\s+```text\\\\n(.*?)```",\n'
        "        text,\n"
        "        re.DOTALL,\n"
        "    )\n"
        '    return match.group(1) if match else ""\n',
    )


def test_bridge_audit_detects_semantic_drift_and_skip_allowlist() -> None:
    module = load_module()

    with temporary_directory() as project_root:
        build_sample_repo(project_root)
        audit = module.audit_bridge_semantic_mirrors(project_root, preview_lines=6)

        error_pairs = [item for item in audit["pair_results"] if item["status"] == "ERROR"]
        assert_equal(len(error_pairs), 2, "semantic bridge drift pair count mismatch")
        assert_true(
            all(item["preamble_stripped"] for item in audit["pair_results"]),
            "semantic mirror audit must strip allowed bridge preambles",
        )
        skipped_paths = [item["path"] for item in audit["skip_results"]]
        assert_true(
            "docs/bridge/SKILLS_INDEX.md" in skipped_paths,
            "bridge SKILLS_INDEX must be skipped as an intentional bridge copy",
        )
        assert_true(
            "docs/bridge/templates/EXECUTION_REPORT_TEMPLATE.md" in skipped_paths,
            "bridge execution-report template must be skipped as an intentional bridge copy",
        )
        assert_true(
            "docs/bridge/templates/TASK_PACKAGE_TEMPLATE.md" in skipped_paths,
            "bridge task-package template must be skipped as an intentional bridge copy",
        )


def test_metadata_audit_detects_stale_extractor_assumption() -> None:
    module = load_module()

    with temporary_directory() as project_root:
        build_sample_repo(project_root)
        audit = module.audit_invocation_example_sources(project_root)

        assert_equal(audit["skill_count"], 2, "skill count mismatch")
        assert_equal(
            audit["skills_with_example_file_input_examples"],
            ["alpha", "beta"],
            "example-file Input Example detection mismatch",
        )
        assert_equal(
            audit["skills_with_inline_input_examples"],
            [],
            "inline SKILL.md Input Example detection mismatch",
        )
        assert_true(
            audit["extractor_expects_inline_skill_examples"],
            "extractor should still be detected as using the legacy inline assumption",
        )
        assert_true(
            audit["fresh_regeneration_risk"],
            "fresh regeneration risk must be raised when example files exist but extractor still reads inline blocks",
        )


def test_cli_report_is_human_readable_and_non_gating() -> None:
    module = load_module()

    with temporary_directory() as project_root:
        build_sample_repo(project_root)
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = module.main(["--root", str(project_root), "--preview-lines", "4"])

        report = buffer.getvalue()
        assert_equal(exit_code, 0, "read-only derivative audit should remain non-gating")
        assert_true("ERROR docs/HANDOFF.md -> docs/bridge/HANDOFF.md" in report, "handoff drift must be reported")
        assert_true(
            "ERROR docs/status/skill-hub-status.md -> docs/bridge/status/skill-hub-status.md" in report,
            "status drift must be reported",
        )
        assert_true(
            "SKIP docs/bridge/SKILLS_INDEX.md" in report,
            "bridge SKILLS_INDEX skip entry must appear in the report",
        )
        assert_true(
            "ERROR stale extractor assumption:" in report,
            "stale extractor assumption must be reported",
        )
        assert_true(
            "Mode: read-only / non-gating" in report,
            "report must describe the non-gating read-only mode",
        )


def main() -> int:
    test_bridge_audit_detects_semantic_drift_and_skip_allowlist()
    test_metadata_audit_detects_stale_extractor_assumption()
    test_cli_report_is_human_readable_and_non_gating()
    print("derivative surface audit smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
