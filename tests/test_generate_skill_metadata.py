from __future__ import annotations

import importlib.util
import shutil
from contextlib import contextmanager
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "tools" / "generate_skill_metadata.py"
LOCAL_TMP_ROOT = ROOT / ".tmp" / "test_generate_skill_metadata"


def assert_equal(actual: object, expected: object, message: str) -> None:
    if actual != expected:
        raise AssertionError(f"{message}: expected={expected!r}, actual={actual!r}")


def load_module():
    spec = importlib.util.spec_from_file_location("generate_skill_metadata", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Failed to load generate_skill_metadata module.")

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


def test_example_file_takes_priority_over_inline_fallback() -> None:
    module = load_module()

    with temporary_directory() as temp_dir:
        skill_dir = temp_dir / "skills" / "alpha"
        write_file(
            skill_dir / "examples" / "invocation_examples.md",
            "# Invocation Examples\n\n### Input Example\n\n```text\nUse alpha from examples.\n\ncontext_files:\n- docs/\n```\n",
        )
        skill_text = (
            "# Alpha\n\n## Invocation\n\n### Input Example\n\n```text\n"
            "Use alpha from inline.\n```\n"
        )

        result = module.extract_invocation_example(skill_dir, skill_text)
        assert_equal(
            result,
            "Use alpha from examples. context_files: - docs/",
            "example-file invocation example should take priority",
        )


def test_inline_fallback_still_works_without_example_file() -> None:
    module = load_module()

    with temporary_directory() as temp_dir:
        skill_dir = temp_dir / "skills" / "beta"
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_text = (
            "# Beta\n\n## Invocation\n\n### Input Example\n\n```text\n"
            "Use beta from inline.\n\nconstraints:\n- Keep changes narrow.\n```\n"
        )

        result = module.extract_invocation_example(skill_dir, skill_text)
        assert_equal(
            result,
            "Use beta from inline. constraints: - Keep changes narrow.",
            "inline invocation example should remain a valid fallback",
        )


def test_missing_example_sources_stays_stable() -> None:
    module = load_module()

    with temporary_directory() as temp_dir:
        skill_dir = temp_dir / "skills" / "gamma"
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_text = "# Gamma\n\n## Invocation\n\n### When to use\n\n- Use gamma.\n"

        result = module.extract_invocation_example(skill_dir, skill_text)
        assert_equal(result, "", "missing example sources should return an empty string")


def main() -> int:
    test_example_file_takes_priority_over_inline_fallback()
    test_inline_fallback_still_works_without_example_file()
    test_missing_example_sources_stays_stable()
    print("generate_skill_metadata extraction tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
