from __future__ import annotations

"""Central governance engine for Documentation Governance OS.

This module is the single execution engine for documentation governance checks.
Focused wrapper scripts import and reuse `build_governance_report(...)` from here;
they do not implement independent rule engines.
"""

import argparse
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "references" / "default_governance.json"
PROJECT_OVERRIDE_PATH = Path(".codex/skill-config/documentation-governance.json")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


@dataclass
class HeadingIssue:
    path: str
    line: int
    message: str


@dataclass
class ReadmeCheck:
    path: str
    missing_sections: list[str] = field(default_factory=list)
    generated_sections: list[str] = field(default_factory=list)


@dataclass
class LayerSummary:
    expected_root: str
    exists: bool
    files: list[str] = field(default_factory=list)
    category_counts: dict[str, int] = field(default_factory=dict)


@dataclass
class DuplicateCandidate:
    canonical_key: str
    paths: list[str] = field(default_factory=list)
    reason: str = ""


@dataclass
class PlacementIssue:
    path: str
    category: str
    layer: str
    allowed_layers: list[str] = field(default_factory=list)
    message: str = ""


@dataclass
class GovernanceReport:
    root: str
    config_path: str
    styleguide_path: str | None
    styleguide_found: bool
    template_language: str
    scanned_files: list[str]
    readme: ReadmeCheck
    engineering_docs: LayerSummary
    readable_docs: LayerSummary
    heading_issues: list[HeadingIssue]
    api_docs_found: list[str]
    forbidden_documents: list[str]
    duplicate_candidates: list[DuplicateCandidate]
    ssot_conflicts: list[DuplicateCandidate]
    layer_placement_conflicts: list[PlacementIssue]
    archive_candidates: list[str]
    readable_generation_targets: list[str]
    readable_second_truth_conflicts: list[DuplicateCandidate]
    high_priority_issues: list[str]
    suggestions: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit repository documentation with a dual-layer governance model.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root to scan.")
    parser.add_argument("--config", type=Path, help="Optional JSON config path overriding the default governance rules.")
    parser.add_argument("--dry-run", action="store_true", help="Preview the audit without writing changes. This is a no-op unless combined with --write.")
    parser.add_argument("--write", action="store_true", help="Patch missing README sections.")
    parser.add_argument("--report", type=Path, help="Write the governance report to a markdown file.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
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


def resolve_config(root: Path, explicit_config: Path | None) -> tuple[dict[str, Any], Path]:
    config = load_json(DEFAULT_CONFIG_PATH)
    config_path = DEFAULT_CONFIG_PATH
    project_override = root / PROJECT_OVERRIDE_PATH
    if project_override.exists():
        config = merge_config(config, load_json(project_override))
        config_path = project_override
    if explicit_config is not None:
        path = explicit_config if explicit_config.is_absolute() else root / explicit_config
        config = merge_config(config, load_json(path))
        config_path = path
    return config, config_path


def normalize_heading(value: str) -> str:
    lowered = value.strip().lower()
    lowered = re.sub(r"[`*_~]+", "", lowered)
    lowered = re.sub(r"[\s:：/\\|,.;!?()\[\]{}-]+", " ", lowered)
    return lowered.strip()


def normalize_doc_key(path: str) -> str:
    stem = Path(path).stem.lower()
    stem = re.sub(r"(^copy-of-|^copy_|^draft-)", "", stem)
    stem = re.sub(r"[_\-\s]+", " ", stem)
    stem = re.sub(r"\b(readable|human|summary|notes|draft|temp)\b", "", stem)
    stem = re.sub(r"\s+", " ", stem)
    return stem.strip()


def extract_markdown_headings(text: str) -> list[tuple[int, str, str, int]]:
    headings: list[tuple[int, str, str, int]] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        match = HEADING_RE.match(raw_line)
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        headings.append((level, title, normalize_heading(title), line_number))
    return headings


def resolve_styleguide_candidates(config: dict[str, Any]) -> list[Path]:
    candidates = [Path(item) for item in config.get("styleguide_paths", [])]
    single = config.get("styleguide_path")
    if single:
        candidates.append(Path(single))
    if not candidates:
        candidates.append(Path("docs/STYLEGUIDE.md"))
    return candidates


def load_styleguide(root: Path, config: dict[str, Any]) -> tuple[Path | None, bool, list[str]]:
    default_sections = list(config.get("required_readme_sections", []))
    styleguide_path: Path | None = None
    for candidate in resolve_styleguide_candidates(config):
        resolved = candidate if candidate.is_absolute() else root / candidate
        if resolved.exists():
            styleguide_path = resolved
            break
    if styleguide_path is None:
        return None, False, default_sections

    configured_titles = config.get(
        "styleguide_required_section_headings",
        ["required readme sections", "readme sections", "必需的readme章节", "readme 必需章节", "readme 章节要求"],
    )
    accepted_titles = {normalize_heading(item) for item in configured_titles}
    lines = styleguide_path.read_text(encoding="utf-8", errors="replace").splitlines()
    headings = extract_markdown_headings("\n".join(lines))
    required_sections: list[str] = []
    current_start = None
    current_level = 0

    for level, _title, normalized, line_number in headings:
        if normalized in accepted_titles:
            current_start = line_number
            current_level = level
            continue
        if current_start is not None and level <= current_level:
            break

    if current_start is not None:
        for raw_line in lines[current_start:]:
            stripped = raw_line.strip()
            if HEADING_RE.match(stripped):
                match = HEADING_RE.match(stripped)
                assert match is not None
                if len(match.group(1)) <= current_level:
                    break
            if stripped.startswith(("-", "*")):
                required_sections.append(stripped[1:].strip())
                continue
            numbered = re.match(r"^\d+[.)]\s+(.*)$", stripped)
            if numbered:
                required_sections.append(numbered.group(1).strip())

    return styleguide_path, True, required_sections or default_sections


def collect_markdown_files(root: Path, config: dict[str, Any]) -> list[Path]:
    results: list[Path] = []
    seen: set[Path] = set()
    for pattern in config.get("scan_globs", ["README.md", "docs/**/*.md"]):
        for path in root.glob(pattern):
            if path.is_file() and path not in seen:
                seen.add(path)
                results.append(path)
    return sorted(results)


def readme_has_section(content: str, section_name: str, aliases_map: dict[str, list[str]], allow_substring: bool) -> bool:
    headings = extract_markdown_headings(content)
    normalized_heading_set = {item[2] for item in headings}
    aliases = aliases_map.get(section_name, [section_name])
    normalized_aliases = {normalize_heading(alias) for alias in aliases}
    if normalized_heading_set & normalized_aliases:
        return True
    if allow_substring:
        lowered = content.lower()
        return any(alias.lower() in lowered for alias in aliases)
    return False


def analyze_headings(path: Path, root: Path) -> list[HeadingIssue]:
    issues: list[HeadingIssue] = []
    last_level = 0
    first_heading_seen = False
    for index, raw_line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        match = HEADING_RE.match(raw_line)
        if not match:
            continue
        level = len(match.group(1))
        if not first_heading_seen:
            first_heading_seen = True
            if level != 1:
                issues.append(HeadingIssue(path=path.relative_to(root).as_posix(), line=index, message="Document should start with a single level-1 heading."))
        if last_level and level > last_level + 1:
            issues.append(HeadingIssue(path=path.relative_to(root).as_posix(), line=index, message=f"Heading level jumps from H{last_level} to H{level}."))
        last_level = level
    return issues


def detect_project_commands(root: Path) -> list[str]:
    commands: list[str] = []
    if (root / "pyproject.toml").exists():
        commands.append("python -m pip install -e .")
    if (root / "package.json").exists():
        commands.append("npm install")
        commands.append("npm test")
    if (root / "Makefile").exists():
        commands.append("make test")
    return commands[:3]


def detect_template_language(config: dict[str, Any], readme_content: str) -> str:
    requested = str(config.get("template_language", "auto")).lower()
    if requested != "auto":
        return requested
    cjk_count = sum(1 for char in readme_content if "\u4e00" <= char <= "\u9fff")
    latin_count = sum(1 for char in readme_content if "a" <= char.lower() <= "z")
    return "zh" if cjk_count > latin_count / 4 else "en"


def get_templates_for_language(config: dict[str, Any], language: str) -> dict[str, str]:
    localized = config.get("localized_templates", {})
    if language in localized and isinstance(localized[language], dict):
        return dict(localized[language])
    return dict(config.get("default_templates", {}))


def generate_section_content(root: Path, config: dict[str, Any], section: str, language: str) -> str:
    templates = get_templates_for_language(config, language)
    content = templates.get(section, f"## {section}\n\n[TODO: Add project-specific content here.]\n")
    commands = detect_project_commands(root)
    usage_aliases = {normalize_heading(alias) for alias in config.get("readme_section_aliases", {}).get("usage", ["usage"])}
    if normalize_heading(section) in usage_aliases and commands:
        if language.startswith("zh"):
            content = content.rstrip() + "\n\n可参考的常见命令：\n\n" + "\n".join(f"- `{cmd}`" for cmd in commands) + "\n"
        else:
            content = content.rstrip() + "\n\nCommon commands:\n\n" + "\n".join(f"- `{cmd}`" for cmd in commands) + "\n"
    return content


def patch_readme(root: Path, readme_path: Path, config: dict[str, Any], missing_sections: list[str], language: str) -> list[str]:
    if not missing_sections:
        return []
    original = readme_path.read_text(encoding="utf-8", errors="replace")
    additions = [generate_section_content(root, config, section, language) for section in missing_sections]
    readme_path.write_text(original.rstrip() + "\n\n" + "\n\n".join(additions).rstrip() + "\n", encoding="utf-8")
    return missing_sections.copy()


def find_api_docs(root: Path, config: dict[str, Any]) -> list[str]:
    found: list[str] = []
    for relative in config.get("api_doc_paths", []):
        path = root / relative
        if path.exists():
            found.append(path.relative_to(root).as_posix())
    return found


def path_layer_name(relative: str, config: dict[str, Any]) -> str:
    engineering_root = str(config.get("doc_layers", {}).get("engineering", {}).get("root", "docs"))
    readable_root = str(config.get("doc_layers", {}).get("readable", {}).get("root", "docs_readable"))
    if relative.startswith(f"{engineering_root}/"):
        return "engineering"
    if relative.startswith(f"{readable_root}/"):
        return "readable"
    return "general"


def category_config_items(config: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    return [(name, dict(data)) for name, data in dict(config.get("categories", {})).items()]


def categorize_document(path: Path, root: Path, config: dict[str, Any]) -> str:
    for category, metadata in category_config_items(config):
        for pattern in metadata.get("globs", []):
            if path.match(pattern):
                return category
    return "general"


def summarize_layer(root: Path, files: list[Path], config: dict[str, Any], layer_name: str) -> LayerSummary:
    layer_config = config.get("doc_layers", {}).get(layer_name, {})
    expected_root = str(layer_config.get("root", layer_name))
    layer_root = root / expected_root
    category_counts: dict[str, int] = {}
    visible_files: list[str] = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        visible_files.append(rel)
        category = categorize_document(path, root, config)
        category_counts[category] = category_counts.get(category, 0) + 1
    return LayerSummary(expected_root=expected_root, exists=layer_root.exists(), files=visible_files, category_counts=category_counts)


def find_forbidden_documents(files: list[Path], root: Path, config: dict[str, Any]) -> list[str]:
    patterns = [re.compile(item, re.IGNORECASE) for item in config.get("forbidden_name_patterns", [])]
    matches: list[str] = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        if any(pattern.search(path.name) for pattern in patterns):
            matches.append(rel)
    return sorted(matches)


def is_ignored_for_dedupe(path: str, config: dict[str, Any]) -> bool:
    ignored_names = {item.lower() for item in config.get("dedupe_ignore_names", [])}
    return Path(path).name.lower() in ignored_names


def find_duplicate_candidates(files: list[Path], root: Path, config: dict[str, Any], include_readable: bool) -> list[DuplicateCandidate]:
    groups: dict[str, list[str]] = {}
    for path in files:
        rel = path.relative_to(root).as_posix()
        if is_ignored_for_dedupe(rel, config):
            continue
        in_readable = path_layer_name(rel, config) == "readable"
        if in_readable and not include_readable:
            continue
        key = normalize_doc_key(rel)
        if not key:
            continue
        groups.setdefault(key, []).append(rel)
    duplicates: list[DuplicateCandidate] = []
    for key, paths in sorted(groups.items()):
        unique_paths = sorted(set(paths))
        if len(unique_paths) > 1:
            duplicates.append(DuplicateCandidate(canonical_key=key, paths=unique_paths, reason="Potential duplicate topic or split source of truth."))
    return duplicates


def find_ssot_conflicts(files: list[Path], root: Path, config: dict[str, Any]) -> list[DuplicateCandidate]:
    duplicates = find_duplicate_candidates(files, root, config, include_readable=False)
    authoritative_roots = tuple(config.get("authoritative_layer_roots", ["docs/"]))
    conflicts: list[DuplicateCandidate] = []
    for item in duplicates:
        authoritative = [path for path in item.paths if path.startswith(authoritative_roots)]
        if len(authoritative) > 1:
            conflicts.append(DuplicateCandidate(canonical_key=item.canonical_key, paths=authoritative, reason="Multiple engineering-layer documents appear to claim the same topic."))
    return conflicts


def find_layer_placement_conflicts(files: list[Path], root: Path, config: dict[str, Any]) -> list[PlacementIssue]:
    issues: list[PlacementIssue] = []
    categories = dict(config.get("categories", {}))
    for path in files:
        rel = path.relative_to(root).as_posix()
        layer = path_layer_name(rel, config)
        if layer not in {"engineering", "readable"}:
            continue
        category = categorize_document(path, root, config)
        if category == "general":
            continue
        allowed_layers = list(categories.get(category, {}).get("allowed_layers", []))
        if allowed_layers and layer not in allowed_layers:
            issues.append(
                PlacementIssue(
                    path=rel,
                    category=category,
                    layer=layer,
                    allowed_layers=allowed_layers,
                    message=f"Category '{category}' should not live in {layer} layer.",
                )
            )
    return issues


def find_archive_candidates(files: list[Path], root: Path, config: dict[str, Any]) -> list[str]:
    patterns = [re.compile(item, re.IGNORECASE) for item in config.get("archive_candidate_patterns", [])]
    candidates: list[str] = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        if any(pattern.search(rel) for pattern in patterns):
            candidates.append(rel)
    return sorted(candidates)


def find_readable_generation_targets(root: Path, engineering_files: list[Path], readable_files: list[Path], config: dict[str, Any]) -> list[str]:
    readable_keys = {normalize_doc_key(path.relative_to(root).as_posix()) for path in readable_files}
    target_categories = set(config.get("readable_target_categories", []))
    targets: list[str] = []
    for path in engineering_files:
        rel = path.relative_to(root).as_posix()
        category = categorize_document(path, root, config)
        if category not in target_categories:
            continue
        key = normalize_doc_key(rel)
        if key and key not in readable_keys:
            targets.append(rel)
    return sorted(set(targets))


def collect_sensitive_lines(text: str, terms: list[str]) -> list[str]:
    lowered_terms = [term.lower() for term in terms]
    found: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        lowered = line.lower()
        if line and any(term in lowered for term in lowered_terms):
            found.append(line)
    return found


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def find_readable_second_truth_conflicts(root: Path, engineering_files: list[Path], readable_files: list[Path], config: dict[str, Any]) -> list[DuplicateCandidate]:
    engineering_by_key: dict[str, list[tuple[str, str]]] = {}
    for path in engineering_files:
        rel = path.relative_to(root).as_posix()
        key = normalize_doc_key(rel)
        if not key:
            continue
        engineering_by_key.setdefault(key, []).append((rel, load_text(path)))

    authority_terms = list(config.get("current_state_terms", [])) + list(config.get("decision_terms", []))
    conflicts: list[DuplicateCandidate] = []

    for path in readable_files:
        rel = path.relative_to(root).as_posix()
        key = normalize_doc_key(rel)
        if not key:
            continue
        readable_text = load_text(path)
        sensitive_lines = collect_sensitive_lines(readable_text, authority_terms)
        if not sensitive_lines:
            continue

        engineering_matches = engineering_by_key.get(key, [])
        if not engineering_matches:
            conflicts.append(
                DuplicateCandidate(
                    canonical_key=key,
                    paths=[rel],
                    reason="Readable document contains authority-like current-state or decision statements without a same-topic engineering source.",
                )
            )
            continue

        engineering_text = "\n".join(text for _, text in engineering_matches).lower()
        unmatched_lines = [line for line in sensitive_lines if line.lower() not in engineering_text]
        if unmatched_lines:
            conflict_paths = [match[0] for match in engineering_matches] + [rel]
            reason = "Readable document appears to introduce authority-like statements not found in the engineering source: " + "; ".join(unmatched_lines[:3])
            conflicts.append(
                DuplicateCandidate(
                    canonical_key=key,
                    paths=conflict_paths,
                    reason=reason,
                )
            )
    return conflicts


def build_markdown_report(report: GovernanceReport) -> str:
    lines = [
        "# Documentation Governance OS Report",
        "",
        f"- Root: `{report.root}`",
        f"- Config: `{report.config_path}`",
        f"- Style guide found: `{'yes' if report.styleguide_found else 'no'}`",
        f"- Template language: `{report.template_language}`",
    ]
    if report.styleguide_path:
        lines.append(f"- Style guide: `{report.styleguide_path}`")
    lines.extend([
        f"- Scanned files: `{len(report.scanned_files)}`",
        "",
        "## High Priority Issues",
        "",
    ])
    if report.high_priority_issues:
        for item in report.high_priority_issues:
            lines.append(f"- {item}")
    else:
        lines.append("- No high-priority governance issues detected")
    lines.extend([
        "",
        "## Layer Model",
        "",
        f"- Engineering docs root: `{report.engineering_docs.expected_root}` ({'present' if report.engineering_docs.exists else 'missing'})",
        f"- Readable docs root: `{report.readable_docs.expected_root}` ({'present' if report.readable_docs.exists else 'missing'})",
        f"- Engineering docs count: `{len(report.engineering_docs.files)}`",
        f"- Readable docs count: `{len(report.readable_docs.files)}`",
        "",
        "## README Check",
        "",
        f"- Path: `{report.readme.path}`",
        f"- Missing sections: `{len(report.readme.missing_sections)}`",
    ])
    for item in report.readme.missing_sections:
        lines.append(f"- Missing: `{item}`")
    for item in report.readme.generated_sections:
        lines.append(f"- Generated: `{item}`")
    lines.extend(["", "## Forbidden Documents", ""])
    if report.forbidden_documents:
        for item in report.forbidden_documents:
            lines.append(f"- Forbidden: `{item}`")
    else:
        lines.append("- No forbidden versioned/finalized filenames detected")
    lines.extend(["", "## Layer Placement Conflicts", ""])
    if report.layer_placement_conflicts:
        for item in report.layer_placement_conflicts:
            lines.append(f"- `{item.path}` -> {item.message} Allowed layers: {', '.join(item.allowed_layers)}")
    else:
        lines.append("- No layer placement conflicts detected")
    lines.extend(["", "## Duplicate Candidates", ""])
    if report.duplicate_candidates:
        for item in report.duplicate_candidates:
            lines.append(f"- `{item.canonical_key}` -> {', '.join(f'`{path}`' for path in item.paths)}")
    else:
        lines.append("- No duplicate topic candidates detected")
    lines.extend(["", "## SSOT Conflicts", ""])
    if report.ssot_conflicts:
        for item in report.ssot_conflicts:
            lines.append(f"- `{item.canonical_key}` -> {', '.join(f'`{path}`' for path in item.paths)}")
    else:
        lines.append("- No engineering-layer source-of-truth conflicts detected")
    lines.extend(["", "## Readable Second-Truth Conflicts", ""])
    if report.readable_second_truth_conflicts:
        for item in report.readable_second_truth_conflicts:
            lines.append(f"- `{item.canonical_key}` -> {', '.join(f'`{path}`' for path in item.paths)}")
            lines.append(f"- Reason: {item.reason}")
    else:
        lines.append("- No readable-layer second-truth conflicts detected")
    lines.extend(["", "## Readable Generation Targets", ""])
    if report.readable_generation_targets:
        for item in report.readable_generation_targets:
            lines.append(f"- Needs readable summary: `{item}`")
    else:
        lines.append("- No missing readable summaries detected for configured categories")
    lines.extend(["", "## Archive Candidates", ""])
    if report.archive_candidates:
        for item in report.archive_candidates:
            lines.append(f"- Archive candidate: `{item}`")
    else:
        lines.append("- No archive candidates detected")
    lines.extend(["", "## API Docs", ""])
    if report.api_docs_found:
        for item in report.api_docs_found:
            lines.append(f"- Found: `{item}`")
    else:
        lines.append("- No API docs detected in configured paths")
    lines.extend(["", "## Heading Issues", ""])
    if report.heading_issues:
        for issue in report.heading_issues:
            lines.append(f"- `{issue.path}:{issue.line}` {issue.message}")
    else:
        lines.append("- No heading hierarchy issues detected")
    lines.extend(["", "## Suggestions", ""])
    for item in report.suggestions:
        lines.append(f"- {item}")
    return "\n".join(lines) + "\n"


def build_governance_report(root: Path, config: dict[str, Any], config_path: Path, args: argparse.Namespace) -> GovernanceReport:
    styleguide_path, styleguide_found, required_sections = load_styleguide(root, config)
    markdown_files = collect_markdown_files(root, config)
    aliases_map = dict(config.get("readme_section_aliases", {}))
    readme_relative = Path(config.get("root_readme", "README.md"))
    readme_path = readme_relative if readme_relative.is_absolute() else root / readme_relative
    readme_content = readme_path.read_text(encoding="utf-8", errors="replace") if readme_path.exists() else ""
    template_language = detect_template_language(config, readme_content)
    allow_substring = bool(config.get("allow_section_substring_match", True))
    missing_sections = [section for section in required_sections if not readme_has_section(readme_content, section, aliases_map, allow_substring)]
    generated_sections: list[str] = []
    if args.write and readme_path.exists() and not args.dry_run:
        generated_sections = patch_readme(root, readme_path, config, missing_sections, template_language)
        readme_content = readme_path.read_text(encoding="utf-8", errors="replace")
        missing_sections = [section for section in required_sections if not readme_has_section(readme_content, section, aliases_map, allow_substring)]

    heading_issues: list[HeadingIssue] = []
    for path in markdown_files:
        heading_issues.extend(analyze_headings(path, root))

    engineering_root = str(config.get("doc_layers", {}).get("engineering", {}).get("root", "docs"))
    readable_root = str(config.get("doc_layers", {}).get("readable", {}).get("root", "docs_readable"))
    engineering_files = [path for path in markdown_files if path.relative_to(root).as_posix().startswith(f"{engineering_root}/")]
    readable_files = [path for path in markdown_files if path.relative_to(root).as_posix().startswith(f"{readable_root}/")]

    api_docs_found = find_api_docs(root, config)
    forbidden_documents = find_forbidden_documents(markdown_files, root, config)
    duplicate_candidates = find_duplicate_candidates(markdown_files, root, config, include_readable=False)
    ssot_conflicts = find_ssot_conflicts(markdown_files, root, config)
    layer_placement_conflicts = find_layer_placement_conflicts(markdown_files, root, config)
    archive_candidates = find_archive_candidates(markdown_files, root, config)
    readable_generation_targets = find_readable_generation_targets(root, engineering_files, readable_files, config)
    readable_second_truth_conflicts = find_readable_second_truth_conflicts(root, engineering_files, readable_files, config)

    high_priority_issues: list[str] = []
    high_priority_issues.extend(f"Forbidden filename: {item}" for item in forbidden_documents)
    high_priority_issues.extend(f"Engineering SSOT conflict: {', '.join(item.paths)}" for item in ssot_conflicts)
    high_priority_issues.extend(f"Readable second-truth conflict: {', '.join(item.paths)}" for item in readable_second_truth_conflicts)
    high_priority_issues.extend(f"Layer placement conflict: {item.path}" for item in layer_placement_conflicts)

    suggestions: list[str] = []
    if not styleguide_found:
        suggestions.append("Add a project style guide so the governance rules have a local authority source.")
    if missing_sections:
        suggestions.append("Fill the missing README sections before creating new standalone docs.")
    if forbidden_documents:
        suggestions.append("Rename forbidden versioned/finalized documents and merge their content into canonical files.")
    if ssot_conflicts:
        suggestions.append("Merge overlapping engineering-layer documents so each topic has one source of truth.")
    if layer_placement_conflicts:
        suggestions.append("Move documents into allowed layers so category placement matches the governance model.")
    if readable_second_truth_conflicts:
        suggestions.append("Reduce readable-layer authority drift so docs_readable stays derivative rather than authoritative.")
    if readable_generation_targets:
        suggestions.append("Generate or refresh docs_readable summaries for engineering docs that need reader-oriented companions.")
    if heading_issues:
        suggestions.append("Normalize markdown heading levels to keep document structure machine-checkable.")
    if config.get("require_api_docs") and not api_docs_found:
        suggestions.append("Add API/reference documentation in one of the configured API doc paths.")
    if generated_sections:
        suggestions.append("Review generated README sections and replace placeholders with project-specific details.")
    if not suggestions:
        suggestions.append("Documentation Governance OS baseline looks healthy; keep docs, docs_readable, and the style guide aligned.")

    return GovernanceReport(
        root=str(root),
        config_path=str(config_path),
        styleguide_path=str(styleguide_path) if styleguide_path else None,
        styleguide_found=styleguide_found,
        template_language=template_language,
        scanned_files=[path.relative_to(root).as_posix() for path in markdown_files],
        readme=ReadmeCheck(path=readme_path.relative_to(root).as_posix() if readme_path.exists() else str(readme_relative), missing_sections=missing_sections, generated_sections=generated_sections),
        engineering_docs=summarize_layer(root, engineering_files, config, "engineering"),
        readable_docs=summarize_layer(root, readable_files, config, "readable"),
        heading_issues=heading_issues,
        api_docs_found=api_docs_found,
        forbidden_documents=forbidden_documents,
        duplicate_candidates=duplicate_candidates,
        ssot_conflicts=ssot_conflicts,
        layer_placement_conflicts=layer_placement_conflicts,
        archive_candidates=archive_candidates,
        readable_generation_targets=readable_generation_targets,
        readable_second_truth_conflicts=readable_second_truth_conflicts,
        high_priority_issues=high_priority_issues,
        suggestions=suggestions,
    )


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    config, config_path = resolve_config(root, args.config)
    report = build_governance_report(root, config, config_path, args)
    markdown_report = build_markdown_report(report)
    if args.report:
        report_path = args.report if args.report.is_absolute() else root / args.report
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(markdown_report, encoding="utf-8")
    if args.json:
        print(json.dumps(asdict(report), ensure_ascii=True, indent=2))
    else:
        print(markdown_report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
