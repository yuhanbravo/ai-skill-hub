---
name: file-structure-check
description: Audit repository layout with configurable profiles, required paths, and strictness levels for application repos, data projects, docs-only repos, and monorepos. Use when Codex needs to review file layout, detect misplaced source/config/test/doc files, validate required directories, or respond to requests like "check project structure", "audit repo layout", "find misplaced files", or "verify monorepo structure".
---

# File Structure Check

Use this skill to compare a repository against a configurable structure contract instead of assuming every project must look the same.

## Trigger Keywords

- file structure check
- repo layout audit
- project structure
- misplaced files
- monorepo structure
- docs-only repo audit
- data project layout

## Side Effects

- Read-only. The script reports structure issues and suggested fixes.
- Follow-up remediation should happen separately after reviewing project constraints.

## Workflow

1. Choose the closest project profile.
2. Run the bundled script against the target root.
3. Review missing directories, missing required paths, misplaced files, and suggested fixes.
4. If needed, add or override project rules with a project-local config rather than changing the bundled defaults.

## Commands

```powershell
python .codex/skills/file-structure-check/scripts/check_file_structure.py --root <project-root>
```

```powershell
conda run -n <env> python .codex/skills/file-structure-check/scripts/check_file_structure.py --root <project-root>
```

Useful flags:

- `--profile <name>` to switch profiles such as `application`, `data-project`, `docs-only`, or `monorepo`
- `--strictness relaxed|standard|strict`
- `--config <path>` to load a project-specific ruleset
- `--json` for machine-readable output

## Config Notes

- Default rules live in `references/default_rules.json`.
- Projects can override them with `.codex/skill-config/file-structure-check.json` or `--config`.
- `required_paths` supports file-level structure contracts in addition to directories.
- `profiles` defines reusable layout presets.
- `strictness=relaxed` suppresses missing-directory noise when the corresponding file category is absent entirely.

## Safety Rules

- Treat the report as governance input, not an automatic refactor order.
- Prefer config changes when a repository intentionally diverges from a default profile.
- Preserve compatibility wrappers and operational root files when the project relies on them.
