# Task Package v0 — workflow-bootstrap orchestration snippets consistency pass

## Background
`workflow-bootstrap` recently added `orchestration_snippets.md` and linked it from supporting assets and usage surfaces. This follow-up checks whether the orchestration layer remains discoverable, internally consistent, and thin, while preserving protocol ownership in `chatgpt-handoff-pilot`.

## Goal
Validate and minimally polish (only if needed) workflow-bootstrap orchestration snippets integration for consistency and thin-wrapper discipline.

## In Scope
- Consistency review across:
  - `skills/workflow-bootstrap/orchestration_snippets.md`
  - `skills/workflow-bootstrap/SKILL.md`
  - `skills/workflow-bootstrap/examples/invocation_examples.md`
  - `skills/workflow-bootstrap/README.md`
- Minimal wording edits only when they resolve clear consistency issues.
- Add this round's execution report under `tasks/`.

## Out of Scope
- Any protocol rewrite for task package / bounded execution / execution report.
- Any changes under `skills/chatgpt-handoff-pilot/`.
- Validators, scripts, hooks, CI, automation, tests, tool adapters.
- New `.github/instructions/**` or `.github/agents/**` assets.
- Project-side runtime files, status docs, or `docs/HANDOFF.md` updates.
- Broad rewrites, file moves, or renames.

## Target files/areas
- `skills/workflow-bootstrap/orchestration_snippets.md`
- `skills/workflow-bootstrap/SKILL.md`
- `skills/workflow-bootstrap/examples/invocation_examples.md`
- `skills/workflow-bootstrap/README.md`
- `tasks/workflow-bootstrap_orchestration_snippets_consistency_task_package.md`
- `tasks/workflow-bootstrap_orchestration_snippets_consistency_execution_report.md`

## Acceptance checks
1. `orchestration_snippets.md` remains thin orchestration glue and does not duplicate protocol body text.
2. Reviewer Safety Gate and Final Reviewer Closure Gate remain distinct.
3. Rollback branches are explicit (Reviewer→Drafter, Final Reviewer→Implementer/Reporter).
4. `[PHASE-SWITCH]` guidance remains explicit for same-tool multi-role execution.
5. `chatgpt-handoff-pilot` remains protocol owner.
6. No unauthorized file changes.

## Constraints
- Orchestration-layer consistency only.
- Thin wrappers and backreferences only; no second rulebook.
- Keep edits minimal and traceable.

## Output requirements
- If consistency is already sufficient, produce no-op canonical changes and document no-op in execution report.
- If clear inconsistency exists, apply only minimum necessary edits in authorized files.
- Produce execution report with evidence-first validation and boundary confirmation.
- Include recommended commit message.

## Assumptions
- Current branch contains latest intended orchestration snippets integration.
- Local repository state is authoritative for this bounded pass.
