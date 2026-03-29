from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from skill_pipeline import build_pipeline
from skill_router import route_task


def assert_equal(actual: object, expected: object, message: str) -> None:
    if actual != expected:
        raise AssertionError(f"{message}: expected={expected!r}, actual={actual!r}")


def main() -> int:
    cases = [
        {
            "task": "Prepare a takeover packet for this unfamiliar repository.",
            "expected_skill": "project-takeover",
        },
        {
            "task": "Audit duplicate markdown docs and README governance issues.",
            "expected_skill": "documentation-governance",
        },
        {
            "task": "Refresh the weekly project status from recent Git history.",
            "expected_skill": "update-project-status",
        },
        {
            "task": "接管项目并整理文档",
            "expected_skill": "project-takeover",
        },
        {
            "task": "接管仓库并更新状态",
            "expected_skill": "project-takeover",
        },
    ]

    for case in cases:
        result = route_task(case["task"])
        assert_equal(
            result["selected_skill"],
            case["expected_skill"],
            f"router selected wrong skill for task: {case['task']}",
        )

    pipeline = build_pipeline("接管项目并整理文档")
    expected_pipeline = [
        "project-takeover",
        "documentation-governance",
        "update-project-status",
    ]
    assert_equal(
        pipeline["ordered_skills"],
        expected_pipeline,
        "pipeline selected the wrong ordered skills",
    )

    status_pipeline = build_pipeline("接管仓库并更新状态")
    assert_equal(
        status_pipeline["ordered_skills"],
        ["project-takeover", "update-project-status"],
        "status pipeline selected the wrong ordered skills",
    )

    print("All skill router tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())