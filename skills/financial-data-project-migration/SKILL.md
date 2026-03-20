---
name: financial-data-project-migration
description: Advise financial-data Python projects that are migrating from scattered scripts, root-level functions, and transitional repositories into a standard src-based engineering layout. Use when Codex needs to inspect a project's current directory structure, script distribution, document entrypoints, Excel-heavy runtime assets, and desktop/Wind coupling; classify the project type and migration stage; recommend a target structure; classify file roles; produce a minimal migration TODO; and coordinate follow-up work with file-structure-check, documentation-governance, project-takeover, and update-project-status.
---

# Financial Data Project Migration

Turn a finance-oriented Python repository into a migration advisory pass before deeper refactoring begins.

## Focus

- Inspect script-heavy or transition-state repositories.
- Judge what kind of financial-data project the repository is today.
- Judge how far the repository has already moved toward a standard `src` layout.
- Detect when the project is actually a desktop Excel + Wind + network-share coupled script system.
- Recommend the smallest useful next migration step instead of attempting a full refactor in one pass.

## Cover These Project Types

- Data extraction projects.
- Analysis and reporting projects.
- Batch pipeline projects.
- Migration-transition projects that mix old scripts with newer package structure.
- Desktop Excel + Wind script projects with strong environment coupling.

## Use These Inputs

- Read the current project directory structure.
- Inspect where Python scripts are distributed across the root, subdirectories, and any emerging `src/` package.
- Inspect whether Excel assets dominate the repository.
- Detect document entrypoints such as `README.md`, `docs/`, migration notes, or task/status files.
- Detect runtime coupling signals such as `WindPy`, `xlwings`, `openpyxl`, network-share paths, and current-working-directory assumptions.

## Produce These Outputs

- Project type judgment.
- Migration stage judgment.
- Fixed risk assessment.
- Target structure recommendation.
- Example mapping candidates.
- File role classification.
- Minimal migration TODO.

## Follow This Workflow

1. Inspect the repository tree and note whether logic lives mainly in root scripts, grouped folders, notebooks, or `src/`.
2. Cluster the current files into rough roles such as extraction, transformation, analytics, reporting, orchestration, configuration, tests, docs, and generated output.
3. Infer the dominant project type from directory names, script names, execution patterns, and dependency signals.
4. If the repository shows Excel-heavy assets plus Wind/desktop/runtime coupling, bias the stage judgment toward `冻结现状 / 建立清单 / 边界识别`.
5. Recommend a target layout that keeps runtime data and generated artifacts outside the source package.
6. Add example mapping candidates so the recommendation stays concrete for the current project.
7. Produce the smallest safe TODO list that helps the project move one stage forward without forcing a disruptive rewrite.

## Coordinate With Other Skills

- Use `file-structure-check` after drafting the target layout to validate whether the proposed or migrated structure is coherent.
- Use `documentation-governance` when migration notes, architecture documents, handoff docs, or runbooks need cleanup after structure changes.
- Use `project-takeover` after the repository becomes understandable enough to generate onboarding and takeover materials.
- Use `update-project-status` to keep migration status, taskboards, and progress artifacts aligned with the current stage.

## Guardrails

- Start with advisory analysis, not automated file movement.
- Preserve old entry scripts as temporary wrappers when jobs, schedulers, or operators still depend on them.
- Keep generated reports, exports, cache files, and local data directories outside the `src/` package.
- Prefer minimal viable structure changes over abstract perfection.
- If desktop Excel automation, Wind, network paths, or Excel asset ambiguity dominate the repo, avoid package-first recommendations and prioritize inventory-first guidance.
