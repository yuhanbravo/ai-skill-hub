# Project-Side Runtime Pack Template Sketch (Phase 3A)

Status: this is a canonical sketch asset for a **future project-side runtime pack**.

This document does **not** create any real project-side runtime pack files in this repository.

## Purpose

Convert the Phase 2 entrypoint drafts into a bounded Phase 3A template sketch for a future project-side runtime pack v1.

This sketch stays at the canonical layer and answers:

- which files are required in v1;
- which files are optional;
- which files should stay out of v1 for now;
- how canonical backreferences should be expressed in consumer repos;
- how to keep the runtime pack from turning into a second rulebook.

## Inclusion Decision Matrix (V1)

| File or file family | Role | V1 status | Why |
| --- | --- | --- | --- |
| `AGENTS.md` | unified project-side master entrypoint | Required | Phase 2 already established it as the thinnest cross-agent entrypoint. |
| `.github/copilot-instructions.md` | Copilot-specific thin adapter | Required | Keeps Copilot discoverability thin while backreferencing `AGENTS.md`. |
| `.github/instructions/*.instructions.md` | topic- or path-specific supplements | Optional | Useful only when repo complexity clearly exceeds what a thin `AGENTS.md` plus thin Copilot adapter can carry. |
| `.github/agents/*.agent.md` | role-specific convenience entrypoints | Not recommended in v1 | Adds role surface area early and risks duplicating guidance before the base entrypoint pair is proven stable. |

## V1 Recommendation

Future project-side runtime pack v1 should stay minimal:

1. Required:
   - `AGENTS.md`
   - `.github/copilot-instructions.md`
2. Optional:
   - `.github/instructions/*.instructions.md`
3. Not recommended in v1:
   - `.github/agents/*.agent.md`

This keeps v1 centered on a single master entrypoint plus a single thin consumer adapter.

## Why `.github/instructions/*.instructions.md` Is Optional

Use path- or topic-specific instructions only if all of the following are true:

1. The repo has a stable sub-area with materially different operating rules.
2. Those rules cannot stay as a short reference from `AGENTS.md`.
3. The extra file reduces ambiguity more than it increases duplication risk.
4. The content still points back to canonical guidance instead of restating it locally.

If these conditions are not met, v1 should avoid adding instruction fragments just to feel complete.

## Why `.github/agents/*.agent.md` Is Not Recommended In V1

Role-specific agent files should stay out of v1 because:

1. Phase 2 only stabilized the master entrypoint and thin adapter pair.
2. Agent files would add another entry surface before the base pair is validated.
3. They are more likely to drift into role-specific mini rulebooks.
4. Their value depends on a later project-side runtime surface that this phase is explicitly not implementing.

Reconsider them only after v1 entrypoints are proven stable in a real consumer repo.

## Template Boundary For V1

Future project-side runtime pack v1 should be treated as an entry layer only.

Allowed in v1:

- entrypoint identity;
- required canonical reading list;
- thin dispatch hints;
- high-frequency constraints for the specific consumer;
- conflict precedence and anti-duplication boundaries.

Not allowed in v1:

- full workflow handbook content;
- full governance handbook content;
- skill-by-skill local restatement;
- role-specific deep guidance unless later authorized;
- local-only edits that silently diverge from canonical guidance.

## Path Backreference Expression Sketch

### Objective

Consumer repos need backreferences that are concrete enough to execute but not so brittle that they assume one exact local packaging shape forever.

### Recommended path expression pattern

Use explicit file paths with stable placeholder slots:

- `<canonical-workflow-guidance-path>`
- `<canonical-handoff-guidance-path>`
- `<project-local-canonical-skill-path>`

Recommended example form inside future project-side files:

```md
Required canonical reading:

- `<canonical-workflow-guidance-path>` (workflow bootstrap guidance)
- `<canonical-handoff-guidance-path>` (handoff / bounded execution guidance)
- `<project-local-canonical-skill-path>` (if present)
```

### Preferred placeholder resolution

Projects should resolve those placeholders to concrete file paths during project-side implementation, for example:

- `skills/workflow-bootstrap/SKILL.md`
- `skills/chatgpt-handoff-pilot/SKILL.md`
- `skills/<project-skill>/SKILL.md`

### What should stay project-filled

The following should remain project-supplied, not hardcoded in this sketch:

- the concrete path to project-local canonical skill payload;
- any project-local path to additional instructions;
- any project-local path that depends on repo packaging or vendor sync layout.

### What should not be done

Avoid:

- directory-only references such as `skills/`;
- host-specific absolute paths;
- editor-session assumptions;
- paths that imply the hub and consumer repo always share the same layout.

Concrete relative file paths are preferred, but the template sketch should still use placeholders where project-side layout is not guaranteed yet.

## Anti-Second-Rulebook Constraints

Future project-side runtime pack v1 should explicitly retain all of the following constraints:

1. Do not copy full canonical workflow guidance into project-side runtime files.
2. If project-side entry text conflicts with canonical guidance, canonical guidance wins.
3. Keep only thin dispatch or adapter information locally.
4. Any reusable rule that is not project-specific should be updated in canonical guidance first, not patched only in project-side files.

### Required change-routing rule

Use this decision rule for future maintenance:

- if a rule is reusable across repos, update canonical guidance;
- if a rule is only about one project's local structure or constraints, keep it project-local;
- if a project-side rule starts growing beyond thin dispatch value, stop and move the reusable part back into canonical guidance.

## Suggested Phase 3A Output Shape

This phase only needs three canonical sketch assets:

1. this runtime pack inclusion sketch;
2. an `AGENTS.md` template sketch;
3. a `.github/copilot-instructions.md` template sketch.

No separate Phase 3A sketch files are needed for `.github/instructions/*.instructions.md` or `.github/agents/*.agent.md`, because v1 does not require them and dedicated sketches would over-commit the current scope.
