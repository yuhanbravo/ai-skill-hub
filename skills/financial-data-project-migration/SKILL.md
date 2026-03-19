---
name: financial-data-project-migration
description: Plan migration of financial data projects from scattered scripts into a standard src-based repository layout, with directory planning, migration sequencing, and coordination guidance for related structure, documentation, takeover, and status-update skills.
---

# Financial Data Project Migration

Use this skill to turn a finance-focused script collection into a standard `src` project blueprint before deeper refactoring begins.

## Goal

- Migrate projects built from scattered scripts into a maintainable `src`-oriented structure.
- Focus on financial data extraction, transformation, analysis, reporting, and export workflows.
- Produce a migration blueprint before code movement starts.

## Applicable Scenarios

- Data acquisition projects that mix API pulls, file ingestion, and ad hoc analysis scripts.
- Quant or reporting repositories that grew from notebooks or task scripts into semi-structured codebases.
- Financial data pipelines that need clearer separation between source code, configs, outputs, tests, and docs.

## Input

- Existing project tree, including root scripts, notebooks, config files, and generated outputs.
- Current entrypoints for extraction, analysis, report generation, or export tasks.
- Known operational constraints such as scheduled jobs, local data directories, or environment requirements.

## Output

- Recommended target structure centered on `src/`.
- Migration blueprint describing which files move, which modules emerge, and which wrappers remain temporarily.
- Directory planning for code, tests, configs, docs, data artifacts, and generated reports.

## Suggested Workflow

1. Inspect the current repository layout and identify script clusters by responsibility.
2. Separate stable source code from runtime outputs, one-off experiments, and reference material.
3. Draft a target `src` package layout for ingestion, processing, analytics, and output layers.
4. Define a phased migration plan that preserves runnable entrypoints while modules are reorganized.
5. Hand off follow-up checks to the related structure, documentation, onboarding, and status skills.

## Relationship To Existing Skills

- `file-structure-check`: validate the proposed or migrated directory layout against explicit rules.
- `documentation-governance`: standardize migration docs, architecture notes, and operational guidance after the layout changes.
- `project-takeover`: package the post-migration repository for new maintainers once the structure is stabilized.
- `update-project-status`: keep taskboards and status artifacts current while migration phases are executed.

## Safety Notes

- Start with planning, not automated file moves.
- Preserve backwards-compatible wrappers when jobs or operators still depend on old script entrypoints.
- Keep generated financial outputs and sensitive data directories outside the planned source package.