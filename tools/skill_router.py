from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_INDEX_PATH = ROOT / "skills_index.json"

# Lightweight intent hints for Chinese and short-form task descriptions.
SKILL_ALIASES: dict[str, list[str]] = {
    "chatgpt-handoff-pilot": [
        "handoff",
        "task package",
        "execution report",
        "任务包",
        "交接包",
        "回执",
        "执行回执",
    ],
    "documentation-governance": [
        "documentation",
        "readme",
        "markdown",
        "docs readable",
        "文档",
        "整理文档",
        "归档文档",
        "README 治理",
    ],
    "file-structure-check": [
        "folder structure",
        "project layout",
        "missing paths",
        "目录结构",
        "文件结构",
        "缺失目录",
        "错位文件",
    ],
    "financial-data-project-migration": [
        "financial data",
        "excel",
        "wind",
        "migration",
        "金融数据",
        "excel 资产",
        "wind 耦合",
        "迁移评估",
    ],
    "project-takeover": [
        "takeover",
        "take over this project",
        "take over this repository",
        "onboarding",
        "unfamiliar repository",
        "接管项目",
        "接管这个项目",
        "接管这个业务项目",
        "接管仓库",
        "仓库接管",
        "项目接手",
        "交接包",
        "首次进入仓库",
    ],
    "skill-governance": [
        "skill governance",
        "skill rewrite",
        "score a skill",
        "治理 skill",
        "重写 skill",
        "skill 评分",
    ],
    "system-handoff": [
        "system handoff",
        "skill hub handoff",
        "system level handoff",
        "更新 system handoff",
        "更新 skill hub handoff",
        "系统交接",
    ],
    "system-status-update": [
        "system status",
        "skill hub status",
        "layer status",
        "phase status",
        "系统状态",
        "层状态",
        "阶段状态",
    ],
    "update-project-status": [
        "project status",
        "weekly summary",
        "git history",
        "更新状态",
        "刷新状态",
        "项目状态",
        "状态同步",
        "更新进度",
        "周报",
        "最近变更",
    ],
    "system-takeover": [
        "system takeover",
        "skill hub takeover",
        "capability system takeover",
        "接管 skill hub",
        "接管这个 skill hub",
        "接管系统工作空间",
        "接管能力系统",
    ],
}


def load_skill_index(path: Path = SKILL_INDEX_PATH) -> list[dict[str, object]]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_text(text: str) -> str:
    lowered = text.lower().replace("-", " ")
    return re.sub(r"\s+", " ", lowered).strip()


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9\u4e00-\u9fff]+", normalize_text(text)))


def overlap_ratio(task_tokens: set[str], candidate_tokens: set[str]) -> float:
    if not task_tokens or not candidate_tokens:
        return 0.0
    return len(task_tokens & candidate_tokens) / len(candidate_tokens)


def jaccard_similarity(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def best_phrase_score(task_text: str, phrases: list[str]) -> tuple[float, list[str], int]:
    task_tokens = tokenize(task_text)
    best_score = 0.0
    matched: list[str] = []
    earliest_position = len(task_text) + 1

    for phrase in phrases:
        normalized_phrase = normalize_text(phrase)
        phrase_tokens = tokenize(phrase)
        score = 0.0
        position = len(task_text) + 1

        if normalized_phrase and normalized_phrase in task_text:
            score = 1.0
            position = task_text.index(normalized_phrase)
        elif phrase_tokens:
            score = overlap_ratio(task_tokens, phrase_tokens)

        if score > best_score:
            best_score = score

        if score >= 0.45:
            matched.append(phrase)
            earliest_position = min(earliest_position, position)

    deduped_matches = list(dict.fromkeys(matched))
    return best_score, deduped_matches, earliest_position


def explicit_name_score(task_description: str, skill_name: str) -> tuple[float, list[str], int]:
    normalized_task = normalize_text(task_description)
    compact_task = normalized_task.replace(" ", "")
    normalized_name = normalize_text(skill_name)
    compact_name = normalized_name.replace(" ", "")
    candidate_forms = [normalized_name, compact_name]

    matched_forms: list[str] = []
    earliest_position = len(normalized_task) + 1
    score = 0.0

    for form in candidate_forms:
        if not form:
            continue

        if " " in form:
            if form in normalized_task:
                matched_forms.append(form)
                earliest_position = min(earliest_position, normalized_task.index(form))
                score = 1.0
        elif form in compact_task:
            matched_forms.append(form)
            earliest_position = min(earliest_position, compact_task.index(form))
            score = 1.0

    return score, list(dict.fromkeys(matched_forms)), earliest_position


def build_skill_keywords(entry: dict[str, object]) -> set[str]:
    parts: list[str] = [
        str(entry.get("name", "")),
        str(entry.get("category", "")),
        str(entry.get("path", "")),
        str(entry.get("invocation_example", "")),
    ]
    parts.extend(str(item) for item in entry.get("triggers", []))
    parts.extend(SKILL_ALIASES.get(str(entry.get("name", "")), []))

    skill_tokens: set[str] = set()
    for part in parts:
        skill_tokens.update(tokenize(part))
    return skill_tokens


def score_skill(task_description: str, entry: dict[str, object]) -> dict[str, object]:
    normalized_task = normalize_text(task_description)
    task_tokens = tokenize(task_description)
    skill_name = str(entry.get("name", ""))
    triggers = [str(item) for item in entry.get("triggers", [])]
    aliases = SKILL_ALIASES.get(skill_name, [])
    skill_tokens = build_skill_keywords(entry)
    explicit_score, explicit_hits, explicit_position = explicit_name_score(task_description, skill_name)

    trigger_score, trigger_hits, trigger_position = best_phrase_score(normalized_task, triggers)
    alias_score, alias_hits, alias_position = best_phrase_score(normalized_task, aliases)
    keyword_score = jaccard_similarity(task_tokens, skill_tokens)
    match_position = min(trigger_position, alias_position, explicit_position)

    confidence = round(
        min(
            0.99,
            0.42 * explicit_score + 0.62 * trigger_score + 0.23 * alias_score + 0.15 * keyword_score,
        ),
        3,
    )

    matched_keywords = sorted((task_tokens & skill_tokens))[:8]
    reasons: list[str] = []
    if explicit_hits:
        reasons.append("explicit skill name: " + ", ".join(explicit_hits[:2]))
    if trigger_hits:
        reasons.append("trigger hits: " + ", ".join(trigger_hits[:3]))
    if alias_hits:
        reasons.append("alias hits: " + ", ".join(alias_hits[:3]))
    if matched_keywords:
        reasons.append("keyword overlap: " + ", ".join(matched_keywords))
    if not reasons:
        reasons.append("matched by low-confidence keyword similarity only")

    return {
        "skill": entry.get("name"),
        "path": entry.get("path"),
        "confidence": confidence,
        "reason": "; ".join(reasons),
        "explicit_name_hits": explicit_hits,
        "trigger_hits": trigger_hits,
        "alias_hits": alias_hits,
        "keyword_overlap": matched_keywords,
        "match_position": match_position,
    }


def route_task(
    task_description: str,
    *,
    top_k: int = 2,
    confidence_floor: float = 0.18,
) -> dict[str, object]:
    entries = load_skill_index()
    ranked = sorted(
        (score_skill(task_description, entry) for entry in entries),
        key=lambda item: (
            -item["confidence"],
            item["match_position"],
            -(len(item["explicit_name_hits"]) + len(item["trigger_hits"]) + len(item["alias_hits"])),
            str(item["skill"]),
        ),
    )

    viable_matches = [item for item in ranked if item["confidence"] >= confidence_floor]
    if not viable_matches:
        return {
            "task_description": task_description,
            "selected_skill": None,
            "confidence": 0.0,
            "reason": "No skill passed the confidence floor.",
            "top_matches": ranked[:top_k],
            "pipeline_candidate": False,
        }

    top_matches = viable_matches[:top_k]
    best_match = top_matches[0]
    second_confidence = top_matches[1]["confidence"] if len(top_matches) > 1 else 0.0
    pipeline_candidate = (
        len(top_matches) > 1
        and best_match["confidence"] >= 0.2
        and second_confidence >= 0.2
        and abs(best_match["confidence"] - second_confidence) <= 0.12
    )

    return {
        "task_description": task_description,
        "selected_skill": best_match["skill"],
        "confidence": best_match["confidence"],
        "reason": best_match["reason"],
        "top_matches": top_matches,
        "pipeline_candidate": pipeline_candidate,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Route a task to the best skill.")
    parser.add_argument("task_description", help="Task description to match against skills.")
    parser.add_argument("--top-k", type=int, default=2, help="How many matches to return.")
    args = parser.parse_args()

    result = route_task(args.task_description, top_k=max(1, args.top_k))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
