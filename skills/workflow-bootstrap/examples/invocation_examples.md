# Invocation Examples

These examples show how to use `workflow-bootstrap` to frame the workflow shell and runtime-profile boundary before handing task-package protocol work to `chatgpt-handoff-pilot`.

## Example 1: Review a non-git project-side trial

Use `workflow-bootstrap` to review whether a project-side trial keeps the right split among thin entries, task artifacts, and historical material.

Example prompt:

```text
Use workflow-bootstrap to review a non-git project-side trial.
Confirm that AGENTS.md stays the master thin entry, .github/copilot-instructions.md stays a Copilot-specific thin adapter, tasks/ is the primary trace path for task packages and execution reports, docs/HANDOFF.md and status surfaces only keep minimal closure, and archive/ remains historical-only.
Do not redefine the handoff protocol.
```

Expected framing:

- workflow shell and role split are in scope
- task package / bounded execution / execution report protocol remains owned by `chatgpt-handoff-pilot`
- project-local facts stay project-local

## Example 2: Prepare non-git runtime conventions

Use `workflow-bootstrap` to describe generic non-git / low-git conventions before any project-side thin-entry change.

Example prompt:

```text
Use workflow-bootstrap to draft a generic non-git runtime profile for a project-side pilot.
Keep tasks/ as the primary evidence directory, execution reports as the main per-task evidence trail, docs/HANDOFF.md and status docs as minimal closure only, and archive/ as inactive history.
Do not add new validators, automation, CI, hooks, or rollout tooling.
```

Expected framing:

- the result stays at workflow-shell and runtime-profile level
- the guidance is conservative and optional, not universal for all repos
- no new task-package schema is introduced

## Example 3: Hand off bounded execution cleanly

Use `workflow-bootstrap` first to align the shell, then switch to `chatgpt-handoff-pilot` for the actual bounded-execution protocol.

Example prompt:

```text
First use workflow-bootstrap to align the default Copilot planner / Codex implementer workflow shell for a low-git project-side task.
Then prepare the actual task package through chatgpt-handoff-pilot, keeping tasks/ as the artifact path and execution reports as the main evidence line.
Do not move per-task detail into docs/HANDOFF.md or reactivate archive/ as the active workflow line.
```

Expected framing:

- `workflow-bootstrap` defines the shell, boundaries, and artifact placement guidance
- `chatgpt-handoff-pilot` owns the task package, bounded execution, and execution report protocol
- the active workflow line remains in current task artifacts rather than historical surfaces
