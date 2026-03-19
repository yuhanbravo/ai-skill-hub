# File Structure Check Skill

## Purpose

`file-structure-check` audits repository layout across multiple project types instead of assuming a single `src/tests/docs` convention. It supports profiles, file-level required paths, and strictness tuning.

## Supported Profiles

- `application`: typical package or service repository
- `data-project`: data or notebook-centric repository
- `docs-only`: documentation-first repository
- `monorepo`: package or service collection repository

Projects can define their own additional profiles in `.codex/skill-config/file-structure-check.json`.

## Running The Script

```powershell
python .codex/skills/file-structure-check/scripts/check_file_structure.py --root <project-root>
```

```powershell
python .codex/skills/file-structure-check/scripts/check_file_structure.py --root <project-root> --profile monorepo --strictness relaxed
```

Optional flags:
- `--config <path>`
- `--profile <name>`
- `--strictness relaxed|standard|strict`
- `--json`

## Configuration

Key config fields:
- `project_profile`
- `strictness`
- `required_directories`
- `optional_directories`
- `required_paths`
- `allowed_*_directories`
- `profiles`

`required_paths` is useful for repositories that need files such as `README.md`, `mkdocs.yml`, or `pnpm-workspace.yaml`.

## Side Effects

This skill is read-only. It does not move files or create directories.

## Cross-Project Notes

- Use profiles to model different repository shapes.
- Use `strictness=relaxed` when auditing repositories with intentionally sparse layouts.
- Prefer project-local config over editing the shared defaults when adapting to a new organization.
