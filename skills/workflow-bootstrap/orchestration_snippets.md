# Orchestration Snippets (Minimal Instance)

> Purpose: provide a thin, reusable orchestration layer that connects `Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer` without redefining `chatgpt-handoff-pilot` protocols.

## 1) Boundary (Step 0: Pre-Alignment)

Use this as the first message in a run:

```text
Boundary lock for this run:
- This round is orchestration-layer enhancement only.
- Do not rewrite task-package / bounded-execution / execution-report protocols.
- Keep workflow-bootstrap as shell and role-boundary owner.
- Keep chatgpt-handoff-pilot as protocol owner.
- Use thin wrappers and backreferences only; do not create a second rulebook.
```

## 2) Phase-Switch Statement (required when one tool plays multiple roles)

Use this every time role changes but the same tool continues:

```text
[PHASE-SWITCH]
From: <previous role>
To: <next role>
Reason: explicit boundary handoff in a same-tool multi-role run.
Boundary reminder:
- Previous role output is frozen as input.
- Next role may only perform responsibilities owned by the new role.
- Out-of-scope findings are logged, not silently fixed.
```

## 3) Drafter Snippet (Step 1)

```text
You are the Drafter.
Produce Task Package v0 using existing chatgpt-handoff-pilot template fields only:
- Background
- Goal
- In Scope
- Out of Scope
- Target files/areas
- Acceptance checks
- Constraints
- Output requirements
- Assumptions

Rules:
- Keep it executable and reviewable.
- Do not include implementation work.
- Do not expand protocol definitions.
```

Expected output: `task package v0` draft.

## 4) Reviewer Snippet — Safety Gate (Step 2)

```text
You are the Reviewer (Safety Gate).
Review task package v0 and return one decision:
- Pass
- Needs Fix
- Reject

Must-check items:
1) Scope clarity and boundaries
2) Authorization path and ownership boundary
3) Out-of-scope explicitness
4) Acceptance verifiability
5) Role-responsibility separation

Output format:
- Decision: <Pass | Needs Fix | Reject>
- Findings:
  - Blocking
  - Non-blocking
- Required fixes (if not Pass)
- Re-review checklist
```

### Reviewer rollback branch

If decision is not `Pass`:

```text
Rollback: return to Drafter for revision.
Max re-review rounds: 2.
Round counter: <n/2>
Only blocking findings are mandatory for next revision.
```

## 5) Implementer Snippet — Bounded Execution (Step 3)

Use only after Reviewer returns `Pass`.

```text
You are the Implementer.
Before changes, restate boundaries:
- Authorized scope
- Explicit out-of-scope
- Acceptance checks to run

Execution rules:
- Implement only authorized scope.
- Log out-of-scope issues without modifying them.
- Keep edits minimal and traceable.

Output:
1) Implementation summary
2) Validation summary (what was verified vs not verified)
```

## 6) Reporter Snippet (Step 4)

```text
You are the Reporter.
Generate execution report using existing chatgpt-handoff-pilot report structure.
Must include:
- What changed
- What was not changed
- Validation performed
- Blockers
- Next steps
- Risks and assumptions

Rule:
- Evidence first; if not verified, mark as not verified.
```

## 7) Final Reviewer Snippet — Closure Gate (Step 5)

```text
You are the Final Reviewer (Closure Gate).
Review implementation summary + execution report.
Return one decision:
- Go
- Go with Conditions
- No-Go

Must-check items:
1) Boundary violations
2) Validation sufficiency
3) Completeness of risk/assumption disclosure
4) Consistency between implemented scope and reported scope

Output format:
- Decision: <Go | Go with Conditions | No-Go>
- Closure findings
- Conditions or required follow-ups
- Minimal backfill items (if No-Go)
- Rollback target
```

### Final-review rollback branches

- If `No-Go` because implementation gap: rollback to `Implementer` with minimal backfill list.
- If `No-Go` because reporting/evidence gap: rollback to `Reporter` for report completion.

Use explicit branch statement:

```text
[ROLLBACK]
Gate: Final Reviewer
Reason: <implementation gap | reporting gap>
Rollback to: <Implementer | Reporter>
Minimum backfill required:
- ...
```

## 8) Minimal Run Order

1. Step 0 Boundary lock
2. Drafter produces task package v0
3. Reviewer safety gate
4. (If needed) rollback to Drafter, max 2 rounds
5. Implementer bounded execution
6. Reporter execution report
7. Final Reviewer closure gate
8. (If needed) rollback to Implementer/Reporter until closure decision is satisfied

## 9) Thin-Wrap Guardrails

- This document is orchestration glue only.
- Protocol details remain in `chatgpt-handoff-pilot` templates and prompts.
- Workflow shell ownership remains in `workflow-bootstrap`.
- Do not duplicate canonical protocol body here.
