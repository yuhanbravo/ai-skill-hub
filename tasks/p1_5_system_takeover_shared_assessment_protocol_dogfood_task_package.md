# P1.5 System Takeover Shared Assessment Protocol Dogfood Task Package

## 1. Background

P0 added `skills/_protocol/skill_assessment_output.md` as the shared assessment output vocabulary for assessment, review, takeover, governance, audit, migration, status, and handoff outputs.

P1 adoption validation concluded `Accept with light follow-up`, with the shared assessment protocol suitable to continue as an active horizontal protocol.

P1 light follow-up added protocol mini examples, a `system-takeover` invocation example aligned with the shared protocol, and clearer wording that `risk_priority` belongs to the assessment output layer rather than a project phase gate or freshness / staleness label.

This P1.5 round dogfoods the protocol through a read-only `system-takeover` assessment of the current `ai-skill-hub` system. It also dogfoods the `Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer` workflow shell while preserving `chatgpt-handoff-pilot` ownership of task package, bounded execution, and execution report protocol.

## 2. Goal

Validate whether the shared assessment output protocol can support a system-level takeover review of `ai-skill-hub` without protocol changes, automation, validators, CI, router / pipeline integration, or second-rulebook expansion.

The review must answer:

- whether `system-takeover` output can accurately match the current repository state;
- whether `capability_fit`, optional `maturity_score`, `evidence`, `inference`, `open_questions`, `risk_priority`, `impact_scope`, and `next_action` are sufficient for system-level takeover output;
- whether `evidence.confirmed`, `evidence.inferred`, and `evidence.pending` remain clearly separated;
- whether `risk_priority` is used as assessment output risk, not as `phase_risk` or `freshness_risk`;
- whether `next_action` is specific and executable;
- whether the full role chain can close cleanly from task package through final review.

Final decision must be one of:

- `Pass: protocol works for system-level takeover`
- `Pass with light follow-up`
- `Needs protocol adjustment`
- `No-Go for system-level adoption`

## 3. In Scope

- Read current repository evidence needed for a read-only `system-takeover` assessment.
- Use `workflow-bootstrap` orchestration guidance only as role-shell guidance.
- Use `chatgpt-handoff-pilot` only as task package, bounded execution, and execution report protocol owner.
- Use `system-takeover` only as a read-only system-level assessment skill.
- Use the shared assessment output protocol as output vocabulary.
- Create the authorized task package, review memo, and execution report.
- Run and record the specified validation commands.

## 4. Out of Scope

- No changes to `skills/`.
- No changes to `skills/_protocol/skill_assessment_output.md`.
- No changes to `skills/system-takeover/SKILL.md`.
- No changes to `skills/system-takeover/examples/invocation_examples.md`.
- No changes to `tools/`.
- No changes to `tests/`.
- No changes to CI or GitHub workflows.
- No changes to router / pipeline behavior.
- No changes to `.agents/` or `.github/`.
- No changes to `docs/HANDOFF.md`.
- No changes to `docs/status/`.
- No validators, automation, scripts, auto-fix, auto-remediation, destructive cleanup, or broad mandatory maturity scoring.
- No commit, push, pull, fetch, merge, or rebase.

## 5. Target files/areas

Read-only evidence areas:

- `skills/workflow-bootstrap/orchestration_snippets.md`
- `skills/workflow-bootstrap/examples/invocation_examples.md`
- `skills/_protocol/skill_assessment_output.md`
- `skills/system-takeover/SKILL.md`
- `skills/system-takeover/examples/invocation_examples.md`
- `tasks/p0_shared_assessment_output_protocol_execution_report.md`
- `docs/reviews/shared_assessment_protocol_adoption_review.md`
- `tasks/p1_shared_assessment_protocol_adoption_validation_execution_report.md`
- `tasks/p1_shared_assessment_protocol_examples_execution_report.md`
- `docs/HANDOFF.md`
- `docs/status/skill-hub-status.md`
- `SKILLS_INDEX.md`
- `README.md`

Authorized output files only:

- `tasks/p1_5_system_takeover_shared_assessment_protocol_dogfood_task_package.md`
- `docs/reviews/system_takeover_shared_assessment_protocol_dogfood_review.md`
- `tasks/p1_5_system_takeover_shared_assessment_protocol_dogfood_execution_report.md`

## 6. Acceptance checks

- Task package exists at the authorized path and uses only the existing `chatgpt-handoff-pilot` template fields.
- Reviewer Safety Gate returns `Pass` before Implementer work begins.
- Review memo exists at the authorized path and contains:
  - Executive Summary
  - Scope and Method
  - Repository State Match Check
  - System Takeover Assessment Using Shared Protocol
  - Protocol Dogfood Evaluation
  - Final Recommendation
  - Recommended Next Action
- Review memo includes at least 5 findings using:
  - `capability_fit`
  - `maturity_score`, only when applicable
  - `evidence.confirmed`
  - `evidence.inferred`
  - `evidence.pending`
  - `inference`
  - `open_questions`
  - `risk_priority`
  - `impact_scope`
  - `next_action`
- Execution report exists at the authorized path and separates changed, unchanged, deferred, validation, risks, and assumptions.
- Final Reviewer returns `Go`, `Go with Conditions`, or `No-Go` with explicit closure findings.
- No restricted files are modified.

Required validation commands:

```powershell
git diff -- docs/reviews tasks
git diff --name-only
git status --short
rg "capability_fit|maturity_score|risk_priority|impact_scope|open_questions|next_action" docs/reviews/system_takeover_shared_assessment_protocol_dogfood_review.md
rg "confirmed|inferred|pending" docs/reviews/system_takeover_shared_assessment_protocol_dogfood_review.md
rg "P0 shared|P1 adoption|P1 light|workflow-bootstrap|chatgpt-handoff-pilot|validator|CI|automation" docs/reviews/system_takeover_shared_assessment_protocol_dogfood_review.md
git diff --name-only | rg "^(skills/|tools/|tests/|\.agents/|\.github/|docs/HANDOFF.md|docs/status/)" || true
```

## 7. Constraints

- Boundary lock is frozen for the run.
- Only the three authorized artifact files may be written.
- `workflow-bootstrap` remains shell and role-boundary owner.
- `chatgpt-handoff-pilot` remains task package, bounded execution, and execution report protocol owner.
- `system-takeover` is used only for read-only assessment.
- The shared assessment output protocol is tested, not modified.
- Do not copy protocol body into other files.
- Use Chinese as the primary execution language while preserving specified English role, protocol, field, and path terms.
- If unrelated local changes appear, stop and report rather than mixing this run with other work.

## 8. Output requirements

Drafter output:

- task package path
- brief task package summary

Reviewer output:

- Safety Gate decision
- findings
- required fixes if not `Pass`
- re-review checklist

Implementer output:

- implementation summary
- review memo path
- validation summary
- files created / changed
- out-of-scope findings, if any

Reporter output:

- execution report path
- short report summary
- remaining risks or assumptions
- final git status

Final Reviewer output:

- Closure Gate decision
- closure findings
- conditions or required follow-ups
- rollback target if `No-Go`
- commit readiness
- recommended commit message

## 9. Assumptions

- The repository state at this checkout is the source of truth for the dogfood run.
- The P1 light follow-up has been committed before this run, as indicated by the current recent Git history.
- `docs/reviews/` already exists; if it did not, creating it would be permitted only to hold the authorized review memo.
- `.pytest_cache/` permission warnings are treated as environment noise unless changed files appear outside the authorized scope.
