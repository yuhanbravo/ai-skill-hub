# Single Consumer Repo File Layout Sketch (Phase 3B)

Status: this is a canonical layout sketch for a **future** single consumer-repo pilot.

This file is not an implementation plan and does not create any real consumer-repo files.

## Validation Profile Context

Applies only to the Phase 3B validation profile:

- Python script / analysis-oriented Git repository;
- baseline structure includes `README` / `docs` / `src` / `tests`;
- future runtime-pack entrypoint pair under validation.

## Sketch Layout (Future Candidate Placement Only)

```text
<consumer-repo-root>/
├── README.md
├── docs/
├── src/
├── tests/
├── AGENTS.md                              # required (future, not created here)
└── .github/
    ├── copilot-instructions.md            # required (future, not created here)
    ├── instructions/
    │   └── *.instructions.md              # optional (future, conditional)
    └── agents/
        └── *.agent.md                     # deferred/not recommended for v1
```

## Required / Optional / Deferred Mapping

### Required (V1)

1. `AGENTS.md`
2. `.github/copilot-instructions.md`

### Optional (V1+ only when justified)

1. `.github/instructions/*.instructions.md`

Use only if one stable project sub-area has distinct constraints that cannot remain thinly referenced from `AGENTS.md`.

### Deferred / Not Recommended in V1

1. `.github/agents/*.agent.md`

Defer until a later phase after v1 entrypoint-pair behavior is validated in real implementation scope.

## Placeholder and Project-Fill Path Notes

### Placeholder-based references (sketch stage)

- `<canonical-workflow-guidance-path>`
- `<canonical-handoff-guidance-path>`
- `<project-local-canonical-skill-path>`

### Must be project-filled in implementation stage

1. Concrete resolved paths for canonical workflow/handoff guidance.
2. Project-local canonical payload path (if the consumer repo has one).

## Boundary Reminder

This document is a canonical Phase 3B validation layout sketch only.

It does not authorize creation of `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/*`, or `.github/agents/*` in any real consumer repository.
