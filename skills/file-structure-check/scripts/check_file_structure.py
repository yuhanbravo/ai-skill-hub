from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "references" / "default_rules.json"
PROJECT_OVERRIDE_PATH = Path(".codex/skill-config/file-structure-check.json")


@dataclass
class StructureReport:
    root: str
    profile: str
    strictness: str
    required_directories: dict[str, bool]
    optional_directories: dict[str, bool]
    missing_directories: list[str]
    required_paths: dict[str, bool]
    missing_required_paths: list[str]
    misplaced_source_files: list[str]
    misplaced_config_files: list[str]
    misplaced_test_files: list[str]
    misplaced_doc_files: list[str]
    suggested_fixes: list[str]
    config_path: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan a project and compare it with a configurable source/config/tests/docs layout."
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root to scan.")
    parser.add_argument("--config", type=Path, help="Optional JSON config path overriding the default rules.")
    parser.add_argument("--profile", help="Optional project profile override.")
    parser.add_argument("--strictness", choices=["relaxed", "standard", "strict"], help="Optional strictness override.")
    parser.add_argument("--dry-run", action="store_true", help="Preview the structure audit without side effects. This checker is read-only.")
    parser.add_argument("--json", action="store_true", help="Emit the report as JSON.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def merge_config(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            merged[key] = merge_config(base[key], value)
        else:
            merged[key] = value
    return merged


def apply_profile(config: dict[str, Any], profile: str) -> dict[str, Any]:
    profiles = dict(config.get("profiles", {}))
    if not profile or profile not in profiles:
        return config
    profile_config = dict(profiles[profile])
    merged = merge_config({key: value for key, value in config.items() if key != "profiles"}, profile_config)
    merged["project_profile"] = profile
    return merged


def resolve_config(root: Path, explicit_config: Path | None, profile: str | None, strictness: str | None) -> tuple[dict[str, Any], Path]:
    default_config = load_json(DEFAULT_CONFIG_PATH)
    config_path = DEFAULT_CONFIG_PATH
    project_override_data: dict[str, Any] | None = None
    explicit_override_data: dict[str, Any] | None = None
    project_override = root / PROJECT_OVERRIDE_PATH
    if project_override.exists():
        project_override_data = load_json(project_override)
        config_path = project_override
    if explicit_config is not None:
        path = explicit_config if explicit_config.is_absolute() else root / explicit_config
        explicit_override_data = load_json(path)
        config_path = path

    # Expand the selected default profile first, then layer project/explicit overrides on top.
    # This lets project-local list fields fully replace the profile defaults when provided.
    effective_profile = profile
    if not effective_profile and explicit_override_data is not None:
        effective_profile = explicit_override_data.get("project_profile")
    if not effective_profile and project_override_data is not None:
        effective_profile = project_override_data.get("project_profile")
    if not effective_profile:
        effective_profile = str(default_config.get("project_profile", "application"))

    config = apply_profile(default_config, str(effective_profile))
    if project_override_data is not None:
        config = merge_config(config, project_override_data)
    if explicit_override_data is not None:
        config = merge_config(config, explicit_override_data)
    config["project_profile"] = str(effective_profile)
    if strictness:
        config["strictness"] = strictness
    return config, config_path


def should_skip_parts(parts: tuple[str, ...], skip_dirs: set[str]) -> bool:
    return any(part in skip_dirs for part in parts)


def is_config_file(path: Path, config_extensions: set[str], root_config_allowlist: set[str]) -> bool:
    name = path.name
    lowered = name.lower()
    return name in root_config_allowlist or path.suffix.lower() in config_extensions or lowered == ".env" or lowered.startswith(".env.")


def is_doc_file(path: Path, doc_extensions: set[str]) -> bool:
    return path.suffix.lower() in doc_extensions


def is_test_file(path: Path, relative_parts: tuple[str, ...], allowed_test_dirs: set[str]) -> bool:
    name = path.name.lower()
    return any(part in allowed_test_dirs for part in relative_parts) or name.startswith("test_") or "_test." in name or name.endswith("_test.py")


def is_source_file(path: Path, source_extensions: set[str]) -> bool:
    name = path.name.lower()
    if name.startswith("test_") or "_test." in name:
        return False
    return path.suffix.lower() in source_extensions


def top_level_allowed(parts: tuple[str, ...], allowed_dirs: set[str]) -> bool:
    return bool(parts) and parts[0] in allowed_dirs


def category_has_files(required_dir: str, metrics: dict[str, int], allowed_source_dirs: set[str], allowed_test_dirs: set[str], allowed_doc_dirs: set[str], allowed_config_dirs: set[str]) -> bool:
    if required_dir in allowed_source_dirs:
        return metrics["source"] > 0
    if required_dir in allowed_test_dirs:
        return metrics["test"] > 0
    if required_dir in allowed_doc_dirs:
        return metrics["doc"] > 0
    if required_dir in allowed_config_dirs:
        return metrics["config"] > 0
    return True


def scan_project(root: Path, config: dict[str, Any], config_path: Path) -> StructureReport:
    required_dirs = tuple(config.get("required_directories", []))
    optional_dirs = tuple(config.get("optional_directories", []))
    required_paths = tuple(config.get("required_paths", []))
    allowed_source_dirs = set(config.get("allowed_source_directories", ["src"]))
    allowed_test_dirs = set(config.get("allowed_test_directories", ["tests"]))
    allowed_doc_dirs = set(config.get("allowed_doc_directories", ["docs"]))
    allowed_config_dirs = set(config.get("allowed_config_directories", ["config"]))
    root_doc_allowlist = set(config.get("root_doc_allowlist", []))
    root_config_allowlist = set(config.get("root_config_allowlist", []))
    skip_dirs = set(config.get("skip_directories", []))
    source_extensions = set(config.get("source_extensions", []))
    config_extensions = set(config.get("config_extensions", []))
    doc_extensions = set(config.get("doc_extensions", []))
    strictness = str(config.get("strictness", "standard"))
    profile = str(config.get("project_profile", "application"))

    required_directory_state = {name: (root / name).is_dir() for name in required_dirs}
    optional_directory_state = {name: (root / name).is_dir() for name in optional_dirs}
    required_path_state = {name: (root / name).exists() for name in required_paths}

    misplaced_source_files: list[str] = []
    misplaced_config_files: list[str] = []
    misplaced_test_files: list[str] = []
    misplaced_doc_files: list[str] = []
    metrics = {"source": 0, "config": 0, "test": 0, "doc": 0}

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        parts = relative.parts
        if should_skip_parts(parts[:-1], skip_dirs):
            continue

        rel = relative.as_posix()

        if is_test_file(path, parts, allowed_test_dirs):
            metrics["test"] += 1
            if not top_level_allowed(parts, allowed_test_dirs):
                misplaced_test_files.append(rel)
            continue

        if is_config_file(path, config_extensions, root_config_allowlist):
            metrics["config"] += 1
            if len(parts) == 1 and path.name in root_config_allowlist:
                continue
            if not top_level_allowed(parts, allowed_config_dirs):
                misplaced_config_files.append(rel)
            continue

        if is_doc_file(path, doc_extensions):
            metrics["doc"] += 1
            if len(parts) == 1 and path.name in root_doc_allowlist:
                continue
            if not top_level_allowed(parts, allowed_doc_dirs):
                misplaced_doc_files.append(rel)
            continue

        if is_source_file(path, source_extensions):
            metrics["source"] += 1
            if not top_level_allowed(parts, allowed_source_dirs):
                misplaced_source_files.append(rel)

    missing_directories: list[str] = []
    for name, exists in required_directory_state.items():
        if exists:
            continue
        if strictness == "relaxed" and not category_has_files(name, metrics, allowed_source_dirs, allowed_test_dirs, allowed_doc_dirs, allowed_config_dirs):
            continue
        missing_directories.append(name)

    missing_required_paths = [name for name, exists in required_path_state.items() if not exists]

    suggested_fixes: list[str] = []
    for name in missing_directories:
        suggested_fixes.append(f"Create missing directory: {name}/")
    for name in missing_required_paths:
        suggested_fixes.append(f"Add required path or update the profile/config: {name}")
    if misplaced_source_files:
        suggested_fixes.append(f"Move implementation files into one of: {', '.join(sorted(allowed_source_dirs))}")
    if misplaced_config_files:
        suggested_fixes.append(f"Move configuration files into one of: {', '.join(sorted(allowed_config_dirs))} or add a root allowlist entry")
    if misplaced_test_files:
        suggested_fixes.append(f"Move test files into one of: {', '.join(sorted(allowed_test_dirs))}")
    if misplaced_doc_files:
        suggested_fixes.append(f"Move documentation files into one of: {', '.join(sorted(allowed_doc_dirs))} or allowlist approved root docs")

    return StructureReport(
        root=str(root),
        profile=profile,
        strictness=strictness,
        required_directories=required_directory_state,
        optional_directories=optional_directory_state,
        missing_directories=missing_directories,
        required_paths=required_path_state,
        missing_required_paths=missing_required_paths,
        misplaced_source_files=sorted(misplaced_source_files),
        misplaced_config_files=sorted(misplaced_config_files),
        misplaced_test_files=sorted(misplaced_test_files),
        misplaced_doc_files=sorted(misplaced_doc_files),
        suggested_fixes=suggested_fixes,
        config_path=str(config_path),
    )


def print_text_report(report: StructureReport) -> None:
    print("File Structure Check")
    print(f"Root: {report.root}")
    print(f"Config: {report.config_path}")
    print(f"Profile: {report.profile}")
    print(f"Strictness: {report.strictness}")
    print()
    print("Required directories:")
    for name, exists in report.required_directories.items():
        print(f"- {name}/: {'OK' if exists else 'MISSING'}")
    if report.required_paths:
        print()
        print("Required paths:")
        for name, exists in report.required_paths.items():
            print(f"- {name}: {'OK' if exists else 'MISSING'}")
    if report.optional_directories:
        print()
        print("Optional directories:")
        for name, exists in report.optional_directories.items():
            print(f"- {name}/: {'PRESENT' if exists else 'ABSENT'}")

    sections = [
        ("Missing directories", report.missing_directories),
        ("Missing required paths", report.missing_required_paths),
        ("Misplaced source files", report.misplaced_source_files),
        ("Misplaced config files", report.misplaced_config_files),
        ("Misplaced test files", report.misplaced_test_files),
        ("Misplaced doc files", report.misplaced_doc_files),
    ]
    for title, items in sections:
        print()
        print(f"{title}: {len(items)}")
        for item in items:
            suffix = "/" if title == "Missing directories" else ""
            print(f"- {item}{suffix}")

    print()
    print("Suggested fixes:")
    for item in report.suggested_fixes or ["No structural issues detected"]:
        print(f"- {item}")


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    config, config_path = resolve_config(root, args.config, args.profile, args.strictness)
    report = scan_project(root, config, config_path)
    if args.json:
        print(json.dumps(asdict(report), ensure_ascii=True, indent=2))
    else:
        print_text_report(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

