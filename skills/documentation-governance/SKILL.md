---
name: documentation-governance
description: Documentation Governance OS for repository documentation structure, dual-layer docs governance, source-of-truth control, deduplication, archiving, and readable-doc generation. Use when Codex needs to audit or reorganize project documentation, separate engineering docs from human-readable docs, prevent document sprawl, detect duplicate or conflicting markdown files, enforce naming rules, or generate docs_readable from docs.
---

# Documentation Governance OS

Use this skill to govern repository documentation as a two-layer system with one rule source, one execution engine, and one engineering source of truth per topic.

## Authority Model

Treat this file as the only top-level rule authority for the skill.

Use the rest of the skill folder by role only:

- `README.md`
  usage guide and operator-facing explanation only
- `references/*.md`
  explanatory supporting material only
- `references/default_governance.json`
  machine configuration only
- `scripts/check_documentation_governance.py`
  central execution engine
- other `scripts/*.py`
  focused wrappers over the central engine

If any supporting file appears to define a different rule than this file, follow this file and then fix the supporting file.

## Layer Model

Treat documentation as two layers:

- `docs/`
  engineering layer and canonical source-of-truth layer
- `docs_readable/`
  human-readable derivative layer

Apply these non-negotiable rules:

- keep one engineering source of truth per topic
- never let `docs_readable/` become an independent authority
- prefer merge over creating a new sibling markdown file
- treat `README.md` as the project entrypoint, not the full authority archive

## Category Model

Use one shared category vocabulary across the skill:

- `architecture`
- `design`
- `decisions`
- `runbooks`
- `reference`
- `api`
- `onboarding`

Apply category-to-layer rules:

- engineering-first categories:
  `architecture`, `design`, `decisions`, `runbooks`, `reference`, `api`
- readable-first category:
  `onboarding`
- dual-layer categories when a readable companion is justified:
  `architecture`, `design`, `decisions`, `reference`, `api`
- do not require readable mirrors for every category
- do not place canonical runbooks in `docs_readable/` unless the file is explicitly a reader-oriented summary

## Trigger Conditions

Use this skill when the repository has any of these goals or problems:

- markdown files are growing without a stable structure
- the project needs a clean split between maintainer docs and reader docs
- multiple documents appear to cover the same topic
- version-suffixed markdown files are appearing
- Codex needs to decide merge vs archive vs create vs readable-summary
- Codex needs to verify whether a new document should exist at all

## Single Source Of Truth Rules

Before creating any new markdown file, answer all three checks:

1. does a same-topic document already exist?
2. should the new content be merged into that document instead?
3. would the new file create a second engineering-layer source of truth?

If the answer to any check is yes, do not create the new standalone file.

## Hard Constraints

Enforce these constraints without exception:

- do not create `*_v2.md`
- do not create `*_final.md`
- do not create `*_updated.md`
- do not create two engineering-layer docs for the same topic unless the split is explicit and category-driven
- do not place canonical engineering content in `docs_readable/`
- do not place reader-facing derivative summaries in `docs/` when they belong in `docs_readable/`
- do not let `docs_readable/` introduce current-state, decision, or status claims that are absent from the engineering source

## Execution Model

Use a single execution engine with focused wrappers:

- central engine:
  `scripts/check_documentation_governance.py`
- focused wrappers:
  `scan_documents.py`, `classify_documents.py`, `deduplicate_documents.py`, `archive_documents.py`, `generate_readable_docs.py`

The wrappers do not implement independent governance engines. They invoke the central engine and expose focused views for specific tasks.

## Workflow

1. run the central engine or the correct focused wrapper in `--dry-run`
2. inspect layer placement, duplicate findings, forbidden names, archive candidates, and readable-layer risks
3. decide the canonical engineering document for each topic
4. archive or merge non-canonical files
5. generate or refresh `docs_readable/` only when a real reading need exists
6. patch README only after structure decisions are already stable

## Inputs

Typical inputs are:

- project root
- optional governance config
- markdown tree
- optional style guide

## Outputs

The governance engine may report:

- engineering-layer summary
- readable-layer summary
- forbidden filename findings
- duplicate-topic findings
- engineering-layer source-of-truth conflicts
- readable-layer second-truth conflicts
- archive candidates
- missing readable-summary targets
- concrete merge, rename, archive, or readable-summary actions

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

Useful flags:

- `--config <path>`
- `--dry-run`
- `--json`
- `--report <path>`
- `--write` only for README section patching after governance is already clear

## Resource Map

Use these files as support, not as alternate law sources:

- `references/document_structure_standard.md`
  explains the category and placement model from this file
- `references/naming_rules.md`
  explains naming examples and anti-examples from this file
- `references/anti_pattern.md`
  explains typical failure modes covered by this file
- `references/default_governance.json`
  stores machine-readable defaults derived from this file

## Safety Rules

- prefer merge over creation
- prefer archive over silent deletion
- prefer one canonical engineering document plus one readable derivative over multiple peer files
- keep the readable layer concise
- if the project has protected operational docs, preserve filenames and improve placement or linkage around them instead of renaming casually
