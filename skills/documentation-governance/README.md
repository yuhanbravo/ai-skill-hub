# Documentation Governance OS

## Purpose

`documentation-governance` helps audit and reorganize repository markdown using a dual-layer model:

- `docs/` for engineering source documents
- `docs_readable/` for reader-oriented derivatives

This README is a usage guide only. The rule authority lives in `SKILL.md`.

## When To Use It

Use the skill when you need to:

- audit markdown structure
- review duplicate or conflicting topic docs
- identify merge or archive candidates
- check whether `docs_readable/` is correctly separated from `docs/`
- generate focused governance reports in dry-run mode

## Execution Model

The skill uses one central engine plus focused wrappers:

- engine: `scripts/check_documentation_governance.py`
- wrappers: `scan_documents.py`, `classify_documents.py`, `deduplicate_documents.py`, `archive_documents.py`, `generate_readable_docs.py`

The wrappers expose filtered outputs from the same governance engine. They are task-oriented views, not separate rule engines.

## Commands

Central engine:

```powershell
python .codex/skills/documentation-governance/scripts/check_documentation_governance.py --root <project-root> --dry-run
```

Focused wrappers:

```powershell
python .codex/skills/documentation-governance/scripts/scan_documents.py --root <project-root> --dry-run
python .codex/skills/documentation-governance/scripts/classify_documents.py --root <project-root> --dry-run
python .codex/skills/documentation-governance/scripts/deduplicate_documents.py --root <project-root> --dry-run
python .codex/skills/documentation-governance/scripts/archive_documents.py --root <project-root> --dry-run
python .codex/skills/documentation-governance/scripts/generate_readable_docs.py --root <project-root> --dry-run
```

## Outputs

Depending on the wrapper, the skill can report:

- layer summaries
- category placement
- forbidden filenames
- duplicate-topic findings
- source-of-truth conflicts
- archive candidates
- readable-summary targets
- readable-layer authority risks
