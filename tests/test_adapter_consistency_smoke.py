from __future__ import annotations

import importlib.util
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "tools" / "check_adapter_consistency.py"


def assert_equal(actual: object, expected: object, message: str) -> None:
    if actual != expected:
        raise AssertionError(f"{message}: expected={expected!r}, actual={actual!r}")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_module():
    spec = importlib.util.spec_from_file_location("check_adapter_consistency", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Failed to load check_adapter_consistency module.")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_sample_project(project_root: Path) -> None:
    write_file(project_root / ".codex" / "skills" / "alpha" / "SKILL.md", "# alpha\n")
    write_file(project_root / ".codex" / "skills" / "beta" / "SKILL.md", "# beta\n")
    write_file(project_root / ".codex" / "skills" / "_protocol" / "skill_invocation.md", "protocol\n")

    write_file(
        project_root / ".agents" / "skills" / "alpha" / "SKILL.md",
        "canonical_path: ../../../skills/alpha\n",
    )
    write_file(
        project_root / ".agents" / "skills" / "gamma" / "SKILL.md",
        "canonical_path: ../../../.codex/skills/gamma\n",
    )

    write_file(
        project_root / ".github" / "skills" / "alpha.md",
        "- Canonical skill path: `../../skills/alpha`\n",
    )
    write_file(
        project_root / ".github" / "skills" / "gamma.md",
        "- Canonical skill path: `../../.codex/skills/gamma`\n",
    )


def test_check_consistency() -> None:
    module = load_module()

    with tempfile.TemporaryDirectory() as temp_dir:
        project_root = Path(temp_dir)
        build_sample_project(project_root)
        result = module.check_consistency(project_root)

        assert_equal(result["missing_agents"], ["beta"], "missing agents mismatch")
        assert_equal(result["missing_github"], ["beta"], "missing github mismatch")
        assert_equal(result["orphan_agents"], ["gamma"], "orphan agents mismatch")
        assert_equal(result["orphan_github"], ["gamma"], "orphan github mismatch")
        assert_equal(result["wrong_reference_agents"], ["alpha"], "wrong agents reference mismatch")
        assert_equal(result["wrong_reference_github"], ["alpha"], "wrong github reference mismatch")


def test_cli_exit_code_and_output() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        project_root = Path(temp_dir)
        build_sample_project(project_root)

        result = subprocess.run(
            ["python", str(SCRIPT_PATH), str(project_root)],
            capture_output=True,
            text=True,
            check=False,
        )

        assert_equal(result.returncode, 1, "CLI must exit with code 1 when issues are detected")
        assert_true("[Adapter Governance Report]" in result.stdout, "CLI report header missing")
        assert_true("codex skills: 2" in result.stdout, "CLI codex count missing")
        assert_true("[Missing]" in result.stdout, "CLI missing section missing")
        assert_true("[Orphan]" in result.stdout, "CLI orphan section missing")
        assert_true("[Wrong Reference]" in result.stdout, "CLI wrong-reference section missing")
        assert_true("Issues detected: 6" in result.stdout, "CLI summary count mismatch")


def main() -> int:
    test_check_consistency()
    test_cli_exit_code_and_output()
    print("adapter consistency smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())