from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}

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

    return data


def main() -> int:
    failures: list[str] = []

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue

        skill_file = skill_dir / "SKILL.md"
        readme_file = skill_dir / "README.md"

        if not skill_file.exists():
            failures.append(f"{skill_dir.name}: missing SKILL.md")
            continue

        if not readme_file.exists():
            failures.append(f"{skill_dir.name}: missing README.md")

        frontmatter = read_frontmatter(skill_file)
        metadata = frontmatter.get("metadata", {}) if isinstance(frontmatter.get("metadata"), dict) else {}
        triggers = frontmatter.get("triggers") or metadata.get("triggers") or []
        description = str(frontmatter.get("description", "")).strip()
        name = str(frontmatter.get("name", "")).strip()

        if not name:
            failures.append(f"{skill_dir.name}: missing name")

        if not description:
            failures.append(f"{skill_dir.name}: empty description")

        if not isinstance(triggers, list) or not triggers:
            failures.append(f"{skill_dir.name}: missing triggers")
        elif len(triggers) < 3:
            failures.append(f"{skill_dir.name}: triggers count < 3")

    if failures:
        print("fail list:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("All skills passed structure validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())