from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    "node_modules",
}


def collect_python_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.py"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def top_level_entries(root: Path) -> list[str]:
    return sorted(path.name for path in root.iterdir())


def detect_documents(root: Path) -> list[str]:
    candidates = [
        root / "README.md",
        root / "README.rst",
        root / "docs",
        root / "MIGRATION_PLAN.md",
        root / "docs" / "HANDOFF.md",
        root / "docs" / "TASKBOARD.md",
    ]
    found: list[str] = []
    for path in candidates:
        if path.exists():
            found.append(str(path.relative_to(root)))
    return found


def contains_keywords(name: str, keywords: set[str]) -> bool:
    lowered = name.lower()
    return any(keyword in lowered for keyword in keywords)


def classify_project_types(python_files: list[Path]) -> list[str]:
    extraction_keywords = {"fetch", "download", "ingest", "pull", "extract", "api", "loader", "scrape"}
    analysis_keywords = {"analysis", "report", "summary", "factor", "alpha", "signal", "analytics", "dashboard"}
    pipeline_keywords = {"pipeline", "batch", "daily", "weekly", "monthly", "job", "schedule", "etl", "runner"}

    labels: list[str] = []
    names = [path.name for path in python_files]

    if any(contains_keywords(name, extraction_keywords) for name in names):
        labels.append("data-extraction")
    if any(contains_keywords(name, analysis_keywords) for name in names):
        labels.append("analysis-reporting")
    if any(contains_keywords(name, pipeline_keywords) for name in names):
        labels.append("batch-pipeline")
    if not labels:
        labels.append("migration-transition")

    return labels


def detect_migration_stage(root: Path, python_files: list[Path]) -> str:
    has_src = (root / "src").exists()
    root_scripts = [path for path in python_files if path.parent == root]

    if not has_src and len(root_scripts) >= 2:
        return "script-sprawl"
    if has_src and root_scripts:
        return "hybrid-transition"
    if has_src:
        return "src-structured"
    return "early-transition"


def classify_file_roles(root: Path, python_files: list[Path]) -> dict[str, list[str]]:
    roles: dict[str, list[str]] = {
        "entry_scripts": [],
        "package_code": [],
        "tests": [],
        "docs": [],
        "configs": [],
    }

    for path in python_files:
        rel = str(path.relative_to(root))
        if path.parent == root:
            roles["entry_scripts"].append(rel)
        elif "tests" in path.parts:
            roles["tests"].append(rel)
        else:
            roles["package_code"].append(rel)

    for doc in detect_documents(root):
        roles["docs"].append(doc)

    for candidate in ["pyproject.toml", "requirements.txt", "setup.py", ".env.example"]:
        path = root / candidate
        if path.exists():
            roles["configs"].append(candidate)

    return roles


def target_structure(project_types: list[str]) -> dict[str, list[str]]:
    package_name = "financial_data_project"
    suggestions = {
        "root": [
            "src/",
            "tests/",
            "docs/",
            "scripts/",
            "data/",
            "reports/",
        ],
        "src_package": [
            f"src/{package_name}/ingestion",
            f"src/{package_name}/processing",
            f"src/{package_name}/analytics",
            f"src/{package_name}/reporting",
        ],
        "notes": [
            "Keep runnable compatibility wrappers in scripts/ during migration.",
            "Keep generated data and reports outside src/.",
        ],
    }

    if "batch-pipeline" in project_types:
        suggestions["src_package"].append(f"src/{package_name}/pipelines")
    return suggestions


def minimal_todo(stage: str, roles: dict[str, list[str]]) -> list[str]:
    todo = [
        "Create a src/ package and choose a stable package name.",
        "Move reusable business logic out of root scripts into package modules.",
        "Keep thin wrapper scripts for current entrypoints until callers are updated.",
    ]

    if not roles["docs"]:
        todo.append("Add README.md or docs/ to explain the current run path and migration intent.")
    if not roles["tests"]:
        todo.append("Add at least one smoke test around the main extraction or reporting path.")
    if stage == "script-sprawl":
        todo.append("Start by migrating one high-value root script cluster instead of rewriting everything at once.")
    if stage == "hybrid-transition":
        todo.append("Normalize imports so root scripts call into src/ modules instead of duplicating logic.")

    return todo


def build_plan(root: Path) -> dict[str, Any]:
    python_files = collect_python_files(root)
    project_types = classify_project_types(python_files)
    stage = detect_migration_stage(root, python_files)
    roles = classify_file_roles(root, python_files)

    return {
        "project_root": str(root.resolve()),
        "input_summary": {
            "top_level_entries": top_level_entries(root),
            "python_file_count": len(python_files),
            "document_entrypoints": detect_documents(root),
        },
        "project_type_judgment": project_types,
        "migration_stage_judgment": stage,
        "target_structure_recommendation": target_structure(project_types),
        "file_role_classification": roles,
        "minimal_migration_todo": minimal_todo(stage, roles),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a minimal migration advisory for a financial-data Python project."
    )
    parser.add_argument("project_root", help="Path to the target project root.")
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    return parser.parse_args()


def render_text(plan: dict[str, Any]) -> str:
    lines = [
        "Financial Data Project Migration Plan",
        f"Project Root: {plan['project_root']}",
        f"Project Types: {', '.join(plan['project_type_judgment'])}",
        f"Migration Stage: {plan['migration_stage_judgment']}",
        "",
        "Document Entrypoints:",
    ]

    docs = plan["input_summary"]["document_entrypoints"] or ["<none>"]
    lines.extend(f"- {item}" for item in docs)
    lines.append("")
    lines.append("File Roles:")
    for role, items in plan["file_role_classification"].items():
        lines.append(f"- {role}: {', '.join(items) if items else '<none>'}")
    lines.append("")
    lines.append("Minimal Migration TODO:")
    lines.extend(f"- {item}" for item in plan["minimal_migration_todo"])
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    root = Path(args.project_root).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Project root does not exist or is not a directory: {root}")

    plan = build_plan(root)
    if args.json:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        return
    print(render_text(plan))


if __name__ == "__main__":
    main()
