# Task Package: financial_migration_skill_refactor_phase1

## Scope
- Enhance `skills/financial-data-project-migration/SKILL.md` to strengthen migration planning from financial desktop scripts to Python `src/` package layouts.
- Produce one bounded execution report for this refactor.

## In Scope
- Add stronger guidance sections for coupling taxonomy, readiness classes, decision tree, target `src/` profiles, legacy wrapper strategy, minimal tests, and first executable migration task-package output.
- Keep the skill advisory and non-destructive.

## Out of Scope
- No new skill creation.
- No changes to `python-data-project-scaffold` or `data-pipeline-quality-gate`.
- No downstream project migration execution.
- No automation/validator/CI/script additions.

## Files to Inspect
- `skills/financial-data-project-migration/SKILL.md`
- `docs/reviews/external_skill_benchmark_2026-05-16.md`
- `tasks/external_skill_benchmark_landing_execution_report.md`

## Files Allowed to Change
- `skills/financial-data-project-migration/SKILL.md`
- `tasks/financial_migration_skill_refactor_phase1_task_package.md`
- `tasks/financial_migration_skill_refactor_phase1_execution_report.md`

## Files Not Allowed to Change
- Real downstream financial projects
- Non-target skills
- `docs/HANDOFF.md`
- `docs/status/`

## Acceptance Criteria
- Skill remains advisory and non-destructive by default.
- Assessment and execution are explicitly separated.
- Readiness classification is present and actionable.
- Minimal test safety net guidance is present.
- First executable migration task package template is present.

## Validation Commands
- `git diff -- skills/financial-data-project-migration/SKILL.md SKILLS_INDEX.md README.md tasks/financial_migration_skill_refactor_phase1_task_package.md tasks/financial_migration_skill_refactor_phase1_execution_report.md`
- `git diff --name-only`
- `git status --short`
- `rg "Coupling Taxonomy|Readiness|Desktop Script|src|Legacy Wrapper|Minimal Test|Task Package" skills/financial-data-project-migration/SKILL.md`
- `rg "python-data-project-scaffold|data-pipeline-quality-gate" skills/financial-data-project-migration/SKILL.md docs/reviews/external_skill_benchmark_2026-05-16.md`

## Execution Report Requirement
- Must include:
  - Scope Restatement
  - Files Changed
  - What Changed
  - What Did Not Change
  - Validation Performed
  - Boundary Checks
  - Risks and Assumptions
  - Deferred Follow-ups
  - Recommended Commit Message
