from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
AGENTS_DIR = ROOT / ".agents" / "skills"
OUTPUT_JSON = ROOT / "skills_index.json"


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing frontmatter in {path}")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"Unclosed frontmatter in {path}")

    frontmatter = text[4:end].splitlines()
    data: dict[str, object] = {}
    metadata: dict[str, object] = {}
    active_block: str | None = None

    for raw_line in frontmatter:
        if not raw_line.strip():
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()

        if indent == 0:
            if line == "metadata:":
                active_block = "metadata"
                data["metadata"] = metadata
                continue

            key, _, value = line.partition(":")
            data[key] = value.strip().strip('"')
            active_block = None
            continue

        if data.get("metadata") is metadata and indent > 0:
            if not line.startswith("- ") and line.endswith(":"):
                block_name = line[:-1]
                metadata[block_name] = []
                active_block = block_name
                continue

            if isinstance(metadata.get(active_block), list) and line.startswith("- "):
                metadata[active_block].append(line[2:].strip())
                continue

            if not line.startswith("- ") and ":" in line:
                key, _, value = line.partition(":")
                metadata[key] = value.strip().strip('"')
                active_block = "metadata"

    return data


def suggest_triggers(skill_name: str, description: str) -> list[str]:
    base = skill_name.replace("-", " ")
    summary = description.rstrip(".")
    return [
        f"use {skill_name}",
        f"run the {base} workflow",
        summary,
    ]


def extract_invocation_example(text: str) -> str:
    match = re.search(
        r"## Invocation\s+.*?### Input Example\s+```text\n(.*?)```",
        text,
        re.DOTALL,
    )
    if not match:
        return ""
    return " ".join(line.strip() for line in match.group(1).strip().splitlines() if line.strip())


def detect_category(skill_name: str) -> str:
    if skill_name == "chatgpt-handoff-pilot":
        return "template"
    if skill_name in {"documentation-governance", "file-structure-check"}:
        return "audit"
    if skill_name == "skill-governance":
        return "governance"
    if skill_name in {"system-handoff", "system-status-update", "system-takeover"}:
        return "system"
    return "project"


def main() -> int:
    skill_entries: list[dict[str, object]] = []

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue

        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue

        frontmatter = read_frontmatter(skill_file)
        metadata = frontmatter.get("metadata", {})
        triggers = list(metadata.get("triggers", [])) or suggest_triggers(
            frontmatter.get("name", skill_dir.name),
            frontmatter.get("description", skill_dir.name),
        )
        side_effects = list(metadata.get("side_effects", []))
        text = skill_file.read_text(encoding="utf-8")

        skill_entries.append(
            {
                "name": frontmatter.get("name", skill_dir.name),
                "path": f"skills/{skill_dir.name}",
                "category": detect_category(skill_dir.name),
                "triggers": triggers,
                "side_effects": side_effects,
                "invocation_example": extract_invocation_example(text),
            }
        )

    OUTPUT_JSON.write_text(
        json.dumps(skill_entries, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    for entry in skill_entries:
        summary_path = AGENTS_DIR / f"{entry['name']}.md"
        # Rebuild using known values instead of relying on dict iteration order.
        frontmatter = read_frontmatter(ROOT / entry["path"] / "SKILL.md")
        description = frontmatter.get("description", "")
        trigger_text = ", ".join(entry["triggers"])
        lines = [
            f"# {entry['name']}",
            "",
            f"- name: `{entry['name']}`",
            f"- description: `{description}`",
            f"- triggers: `{trigger_text}`",
            f"- path: `{entry['path']}`",
            "",
            "Read the canonical SKILL.md before execution.",
            "",
        ]
        summary_path.write_text("\n".join(lines), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
