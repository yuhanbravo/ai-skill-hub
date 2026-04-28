# Non-Git / Low-Git Runtime Profile

Status: this is a supporting asset for bounded project-side trials, not a universal requirement for every repository.

## When To Use

Use this profile when a project-side trial cannot rely on Git history, branch structure, pull requests, or clean diffs as the primary evidence path for each bounded task.

Typical cases:

- non-git repositories
- low-git projects where history is partial or not trustworthy as per-task evidence
- pilot rounds that need explicit task-level artifacts before any broader runtime-pack expansion

## Core Conventions

### `tasks/` as the primary trace path

For non-git / low-git bounded work, `tasks/` may serve as the preferred project-local evidence path for task packages and execution reports unless the project already has a clearer established location, so the active workflow line stays easy to inspect without depending on Git metadata.

Recommended minimum convention:

- one task package per bounded task
- one execution report per bounded task
- shared date or task-name prefix when pairing task package and execution report

An optional `tasks/README.md` or similar index may help navigation once artifacts accumulate, but it should stay lightweight and should not replace the task artifacts themselves.

### Execution report as the main evidence trail

When Git evidence is weak, treat the execution report as the primary per-task evidence trail. It should capture:

- scope restatement
- files changed
- validation performed or skipped
- assumptions, risks, and explicit non-goals

This keeps evidence local to the bounded task without redefining the handoff protocol.

### Minimal closure for handoff and status

`docs/HANDOFF.md` and status-like surfaces should receive only the smallest useful closure facts for cross-round continuity. They should not become the primary per-task trace log.

### `archive/` remains historical

If a project keeps `archive/` or similar directories, treat them as historical or inactive reference only. Do not restore them as the active workflow line for current bounded execution.

## Boundary With `chatgpt-handoff-pilot`

`workflow-bootstrap` may describe this runtime profile as workflow-shell guidance, but `chatgpt-handoff-pilot` still owns:

- task package structure
- bounded execution behavior
- execution report protocol

In other words, this profile explains where project-side evidence can live in non-git / low-git conditions; it does not create a second handoff protocol.

## Relation To Thin Project-Side Entries

If a project later adopts thin project-side entries, keep the split conservative:

- `AGENTS.md` remains the master thin entry
- `.github/copilot-instructions.md` remains a Copilot-specific thin adapter
- both may point to `tasks/` as the evidence directory in non-git / low-git contexts
- neither should become a duplicated repository rulebook

## Out Of Scope

This supporting asset does not authorize:

- changes to `chatgpt-handoff-pilot`
- new task-package schemas
- validators, automation, CI, hooks, or rollout tooling
- turning non-git conventions into a mandatory rule for normal Git-first repositories
