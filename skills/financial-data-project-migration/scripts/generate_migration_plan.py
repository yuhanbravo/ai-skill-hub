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
IGNORE_DIR_PREFIXES = (".codex_tmp",)
FIXED_RISK_NAMES = [
    "外部桌面环境依赖",
    "网络盘依赖",
    "当前工作目录依赖",
    "Excel 资产角色不清",
]


def should_ignore_path(root: Path, path: Path) -> bool:
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        parts = path.parts
    return any(part in IGNORE_DIRS or part.startswith(IGNORE_DIR_PREFIXES) for part in parts)


def collect_files(root: Path, suffixes: tuple[str, ...]) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or should_ignore_path(root, path):
            continue
        if path.suffix.lower() in suffixes:
            files.append(path)
    return sorted(files)


def collect_python_files(root: Path) -> list[Path]:
    return collect_files(root, (".py",))


def collect_excel_files(root: Path) -> list[Path]:
    return collect_files(root, (".xlsx", ".xls", ".xlsm", ".xlsb", ".csv"))


def top_level_paths(root: Path) -> list[Path]:
    return sorted(
        [path for path in root.iterdir() if not path.name.startswith(IGNORE_DIR_PREFIXES)],
        key=lambda item: item.name,
    )


def top_level_entries(root: Path) -> list[str]:
    return [path.name for path in top_level_paths(root)]


def detect_documents(root: Path) -> list[str]:
    candidates = [
        root / "README.md",
        root / "README.rst",
        root / "docs",
        root / "MIGRATION_PLAN.md",
        root / "docs" / "HANDOFF.md",
        root / "docs" / "TASKBOARD.md",
        root / "docs" / "MIGRATION_BLUEPRINT.md",
        root / "docs" / "SCRIPT_MAP.md",
        root / "docs" / "TECH_DEBT.md",
    ]
    found: list[str] = []
    for path in candidates:
        if path.exists():
            found.append(str(path.relative_to(root)))
    return found


def contains_keywords(name: str, keywords: set[str]) -> bool:
    lowered = name.lower()
    return any(keyword in lowered for keyword in keywords)


def read_text_safe(path: Path, limit: int = 200_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit]
    except OSError:
        return ""


def rel(root: Path, path: Path) -> str:
    return str(path.relative_to(root))


def is_generated_output_rel(rel_path: str) -> bool:
    lowered = rel_path.lower()
    return any(
        token in lowered
        for token in ("output", "reports", "monthly_contribution", "归档", "archive", "收益贡献")
    )


def build_signal_summary(root: Path, python_files: list[Path], excel_files: list[Path]) -> dict[str, Any]:
    root_scripts = [path for path in python_files if path.parent == root]
    root_script_names = [path.name.lower() for path in root_scripts]
    texts = {path: read_text_safe(path) for path in python_files}
    lower_texts = {path: text.lower() for path, text in texts.items()}

    has_src = (root / "src").exists()
    has_windpy = any("from windpy import" in text or "import windpy" in text for text in lower_texts.values())
    has_excel_lib = any(
        any(token in text for token in ("import xlwings", "from openpyxl import", "import openpyxl"))
        for text in lower_texts.values()
    )
    has_desktop_excel = any("import xlwings" in text for text in lower_texts.values())
    has_openpyxl = any("openpyxl" in text for text in lower_texts.values())
    has_network_path = any("\\\\" in text for text in texts.values())
    has_cwd_dependency = any(
        any(token in text for token in ("path.cwd()", "os.getcwd()", "chdir(", "sys.path.append(str(path.cwd())"))
        for text in lower_texts.values()
    )
    has_script_orchestrator = any(
        contains_keywords(name, {"task", "runner", "batch", "loop", "monthly", "daily"})
        for name in root_script_names
    ) and any(
        any(token in text for token in ("subprocess", "input(", "sys.argv", "argparse"))
        for text in lower_texts.values()
    )

    monolithic_examples: list[str] = []
    for path in root_scripts:
        text = lower_texts[path]
        has_fetch = any(token in text for token in ("w.wpf(", "w.wps(", "w.wss(", "w.wsd(", "wind_call_with_retry"))
        has_compute = any(token in text for token in ("groupby(", "pivot_table(", "merge(", "fillna(", "np.", "pd."))
        has_excel_write = any(token in text for token in ("to_excel(", "books.open(", "openpyxl", "workbook("))
        if has_fetch and has_compute and has_excel_write:
            monolithic_examples.append(rel(root, path))

    top_level_static_assets = [
        path.name
        for path in top_level_paths(root)
        if path.suffix.lower() != ".py" and path.name not in {"docs", "tests", "src", "scripts"}
    ]

    return {
        "has_src": has_src,
        "root_script_count": len(root_scripts),
        "excel_file_count": len(excel_files),
        "has_windpy": has_windpy,
        "has_excel_lib": has_excel_lib,
        "has_desktop_excel": has_desktop_excel,
        "has_openpyxl": has_openpyxl,
        "has_network_path": has_network_path,
        "has_cwd_dependency": has_cwd_dependency,
        "has_script_orchestrator": has_script_orchestrator,
        "root_static_asset_count": len(top_level_static_assets),
        "monolithic_script_examples": monolithic_examples[:5],
    }


def classify_project_types(python_files: list[Path], signals: dict[str, Any]) -> list[str]:
    extraction_keywords = {"fetch", "download", "ingest", "pull", "extract", "api", "loader", "scrape"}
    analysis_keywords = {"analysis", "report", "summary", "factor", "alpha", "signal", "analytics", "dashboard"}
    pipeline_keywords = {"pipeline", "batch", "daily", "weekly", "monthly", "job", "schedule", "etl", "runner", "task"}

    labels: list[str] = []
    names = [path.name for path in python_files]

    is_desktop_excel_wind = all(
        [
            signals["has_windpy"],
            signals["has_excel_lib"],
            signals["excel_file_count"] >= 10,
            signals["has_script_orchestrator"] or signals["root_script_count"] >= 5,
            not signals["has_src"],
            signals["root_static_asset_count"] >= 6,
        ]
    )
    if is_desktop_excel_wind:
        labels.append("desktop_excel_wind_script_project")

    if any(contains_keywords(name, extraction_keywords) for name in names):
        labels.append("data-extraction")
    if any(contains_keywords(name, analysis_keywords) for name in names):
        labels.append("analysis-reporting")
    if any(contains_keywords(name, pipeline_keywords) for name in names):
        labels.append("batch-pipeline")
    if not labels:
        labels.append("migration-transition")

    return labels


def detect_migration_stage(root: Path, python_files: list[Path], signals: dict[str, Any]) -> str:
    has_src = (root / "src").exists()
    root_scripts = [path for path in python_files if path.parent == root]

    high_risk = any(
        [
            signals["excel_file_count"] >= 10,
            signals["has_desktop_excel"],
            signals["has_network_path"],
            signals["has_cwd_dependency"],
            bool(signals["monolithic_script_examples"]),
        ]
    )
    if high_risk:
        return "冻结现状 / 建立清单 / 边界识别"
    if not has_src and len(root_scripts) >= 2:
        return "script-sprawl"
    if has_src and root_scripts:
        return "hybrid-transition"
    if has_src:
        return "src-structured"
    return "early-transition"


def classify_file_roles(root: Path, python_files: list[Path], excel_files: list[Path]) -> dict[str, list[str]]:
    roles: dict[str, list[str]] = {
        "entry_scripts": [],
        "package_code": [],
        "tests": [],
        "docs": [],
        "configs": [],
        "excel_assets": [],
        "generated_outputs": [],
    }

    for path in python_files:
        rel_path = rel(root, path)
        lowered = path.name.lower()
        if path.parent == root and not lowered.startswith("test_") and not lowered.startswith("verify"):
            roles["entry_scripts"].append(rel_path)
        elif "tests" in path.parts or lowered.startswith("test_"):
            roles["tests"].append(rel_path)
        else:
            roles["package_code"].append(rel_path)

    for doc in detect_documents(root):
        roles["docs"].append(doc)

    for candidate in ["pyproject.toml", "requirements.txt", "setup.py", ".env.example"]:
        path = root / candidate
        if path.exists():
            roles["configs"].append(candidate)

    non_generated_assets: list[str] = []
    generated_assets: list[str] = []
    for path in excel_files:
        rel_path = rel(root, path)
        if is_generated_output_rel(rel_path):
            generated_assets.append(rel_path)
        else:
            non_generated_assets.append(rel_path)
    roles["excel_assets"] = non_generated_assets[:12]
    roles["generated_outputs"] = generated_assets[:12]

    return roles


def pick_examples(items: list[str], limit: int = 5) -> list[str]:
    seen: list[str] = []
    for item in items:
        if item not in seen:
            seen.append(item)
        if len(seen) >= limit:
            break
    return seen


def build_example_mapping_candidates(root: Path, roles: dict[str, list[str]], project_types: list[str]) -> dict[str, list[str]]:
    top_paths = top_level_paths(root)
    docs_candidates = roles["docs"]
    tests_candidates = roles["tests"]
    script_candidates = roles["entry_scripts"]

    data_candidates = [
        path.name
        for path in top_paths
        if (
            path.is_dir() and any(token in path.name.lower() for token in ("data", "historical", "时间序列", "brinson"))
        )
        or (
            path.is_file()
            and path.suffix.lower() in {".xlsx", ".xls", ".csv", ".db"}
            and any(token in path.name for token in ("产品列表", "股票分类", "股票行业调整", "行业主题对应关系", "A&H"))
        )
    ]
    report_candidates = [
        path.name
        for path in top_paths
        if (
            path.is_dir()
            and any(token in path.name.lower() for token in ("report", "output", "monthly_contribution", "归档", "贡献数据"))
        )
        or (
            path.is_file()
            and path.suffix.lower() in {".xlsx", ".xls"}
            and any(token in path.name for token in ("收益贡献", "净值曲线", "月度调仓"))
        )
    ]
    config_candidates = [
        path.name
        for path in top_paths
        if path.suffix.lower() in {".json", ".jsonc", ".db"}
        or any(token in path.name for token in ("产品列表", "股票分类", "股票行业调整", "行业主题对应关系"))
    ]

    if "desktop_excel_wind_script_project" in project_types:
        script_candidates = [
            item
            for item in roles["entry_scripts"]
            if any(token in item.lower() for token in ("task_", "monthly_", "yuanzhou", "strategy_", "portfolio"))
        ] or roles["entry_scripts"]

    return {
        "scripts/": pick_examples(script_candidates, 5),
        "docs/": pick_examples(docs_candidates, 5),
        "tests/": pick_examples(tests_candidates, 5),
        "data/": pick_examples(data_candidates, 5),
        "reports/": pick_examples(report_candidates, 5),
        "config/": pick_examples(config_candidates, 5),
    }


def target_structure(root: Path, project_types: list[str], roles: dict[str, list[str]]) -> dict[str, Any]:
    package_name = "financial_data_project"
    suggestions: dict[str, Any] = {
        "root": [
            "src/",
            "config/",
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
        "example_mapping_candidates": build_example_mapping_candidates(root, roles, project_types),
    }

    if "batch-pipeline" in project_types:
        suggestions["src_package"].append(f"src/{package_name}/pipelines")
    if "desktop_excel_wind_script_project" in project_types:
        suggestions["notes"].append(
            "For desktop Excel + Wind projects, document runtime contracts before moving files."
        )
    return suggestions


def minimal_todo(stage: str, roles: dict[str, list[str]], project_types: list[str]) -> list[str]:
    if stage == "冻结现状 / 建立清单 / 边界识别":
        todo = [
            "Document the current entry scripts and operator-facing run order before changing structure.",
            "Inventory external runtime dependencies such as Wind, Excel desktop automation, templates, and network shares.",
            "Classify Excel assets into input/reference/template/output/archive before proposing file moves.",
            "Choose one script cluster as the first migration pilot and leave the remaining entry scripts untouched for now.",
        ]
        if not roles["docs"]:
            todo.append("Add a minimal README.md or docs/ note that records the current run path and external dependencies.")
        return todo

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
    if "desktop_excel_wind_script_project" in project_types:
        todo.insert(0, "Record runtime assumptions for Wind, Excel desktop, and path-dependent assets before packaging anything.")

    return todo


def build_risk_assessment(signals: dict[str, Any]) -> list[dict[str, Any]]:
    risk_hits = {
        "外部桌面环境依赖": signals["has_desktop_excel"],
        "网络盘依赖": signals["has_network_path"],
        "当前工作目录依赖": signals["has_cwd_dependency"],
        "Excel 资产角色不清": signals["excel_file_count"] >= 10,
    }
    evidence_map = {
        "外部桌面环境依赖": ["Detected xlwings usage"] if signals["has_desktop_excel"] else [],
        "网络盘依赖": ["Detected UNC-style path literals"] if signals["has_network_path"] else [],
        "当前工作目录依赖": ["Detected Path.cwd()/os.getcwd()/relative execution assumptions"] if signals["has_cwd_dependency"] else [],
        "Excel 资产角色不清": [f"Detected {signals['excel_file_count']} Excel-like files"] if signals["excel_file_count"] >= 10 else [],
    }

    return [
        {
            "name": name,
            "detected": bool(risk_hits[name]),
            "evidence": evidence_map[name],
        }
        for name in FIXED_RISK_NAMES
    ]


def build_plan(root: Path) -> dict[str, Any]:
    python_files = collect_python_files(root)
    excel_files = collect_excel_files(root)
    signals = build_signal_summary(root, python_files, excel_files)
    project_types = classify_project_types(python_files, signals)
    stage = detect_migration_stage(root, python_files, signals)
    roles = classify_file_roles(root, python_files, excel_files)

    return {
        "project_root": str(root.resolve()),
        "input_summary": {
            "top_level_entries": top_level_entries(root),
            "python_file_count": len(python_files),
            "excel_file_count": len(excel_files),
            "document_entrypoints": detect_documents(root),
        },
        "signal_summary": signals,
        "project_type_judgment": project_types,
        "migration_stage_judgment": stage,
        "risk_assessment": build_risk_assessment(signals),
        "target_structure_recommendation": target_structure(root, project_types, roles),
        "file_role_classification": roles,
        "minimal_migration_todo": minimal_todo(stage, roles, project_types),
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
        f"Excel File Count: {plan['input_summary']['excel_file_count']}",
        "",
        "Document Entrypoints:",
    ]

    docs = plan["input_summary"]["document_entrypoints"] or ["<none>"]
    lines.extend(f"- {item}" for item in docs)
    lines.append("")
    lines.append("Fixed Risks:")
    for item in plan["risk_assessment"]:
        evidence = f" ({'; '.join(item['evidence'])})" if item["evidence"] else ""
        lines.append(f"- {item['name']}: {'detected' if item['detected'] else 'not detected'}{evidence}")
    lines.append("")
    lines.append("File Roles:")
    for role, items in plan["file_role_classification"].items():
        lines.append(f"- {role}: {', '.join(items) if items else '<none>'}")
    lines.append("")
    lines.append("Example Mapping Candidates:")
    for target, items in plan["target_structure_recommendation"]["example_mapping_candidates"].items():
        lines.append(f"- {target}: {', '.join(items) if items else '<none>'}")
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
