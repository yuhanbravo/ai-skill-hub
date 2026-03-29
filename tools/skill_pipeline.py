from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from skill_router import route_task


PIPELINE_ORDER = [
    "project-takeover",
    "file-structure-check",
    "documentation-governance",
    "financial-data-project-migration",
    "skill-governance",
    "update-project-status",
    "chatgpt-handoff-pilot",
]

FOLLOW_UP_RULES: dict[str, list[str]] = {
    "project-takeover": ["update-project-status"],
    "documentation-governance": ["update-project-status"],
    "file-structure-check": ["update-project-status"],
}


def split_task(task_description: str) -> list[str]:
    parts = re.split(r"\b(?:and|then|after|with)\b|[，,、；;]|并且|并|然后|再|以及", task_description)
    cleaned = [part.strip() for part in parts if part.strip()]
    return cleaned or [task_description.strip()]


def order_skills(skills: list[str]) -> list[str]:
    rank = {name: index for index, name in enumerate(PIPELINE_ORDER)}
    return sorted(dict.fromkeys(skills), key=lambda item: rank.get(item, len(rank)))


def build_pipeline(task_description: str) -> dict[str, object]:
    sub_tasks = split_task(task_description)
    routed_sub_tasks: list[dict[str, object]] = []
    selected_skills: list[str] = []

    for sub_task in sub_tasks:
        result = route_task(sub_task, top_k=2)
        if result["selected_skill"] is None:
            continue

        routed_sub_tasks.append(
            {
                "sub_task": sub_task,
                "selected_skill": result["selected_skill"],
                "confidence": result["confidence"],
                "reason": result["reason"],
            }
        )
        selected_skills.append(str(result["selected_skill"]))

    ordered_skills = order_skills(selected_skills)
    for skill in list(ordered_skills):
        follow_ups = FOLLOW_UP_RULES.get(skill, [])
        if (
            skill == "project-takeover"
            and "documentation-governance" in ordered_skills
            and "update-project-status" not in ordered_skills
        ):
            ordered_skills.extend(follow_ups)
            continue

        if skill in {"documentation-governance", "file-structure-check"} and "update-project-status" not in ordered_skills:
            ordered_skills.extend(follow_ups)

    ordered_skills = order_skills(ordered_skills)
    pipeline_mode = len(ordered_skills) > 1

    execution_steps = [
        {
            "step": index,
            "skill": skill,
            "purpose": next(
                (item["sub_task"] for item in routed_sub_tasks if item["selected_skill"] == skill),
                f"follow-up step derived from pipeline strategy for {skill}",
            ),
        }
        for index, skill in enumerate(ordered_skills, start=1)
    ]

    return {
        "task_description": task_description,
        "pipeline_mode": pipeline_mode,
        "sub_tasks": routed_sub_tasks,
        "ordered_skills": ordered_skills,
        "execution_steps": execution_steps,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a lightweight skill pipeline.")
    parser.add_argument("task_description", help="Complex task description to split and route.")
    args = parser.parse_args()

    result = build_pipeline(args.task_description)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())