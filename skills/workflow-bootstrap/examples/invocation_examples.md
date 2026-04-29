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
First use workflow-bootstrap to align a role-based workflow shell for a low-git project-side task, using Copilot-as-Drafter and Codex-as-Implementer only as adapter examples if useful.
Then prepare the actual task package through chatgpt-handoff-pilot, keeping tasks/ as the artifact path and execution reports as the main evidence line.
Do not move per-task detail into docs/HANDOFF.md or reactivate archive/ as the active workflow line.
```

Expected framing:

- `workflow-bootstrap` defines the shell, boundaries, and artifact placement guidance
- `chatgpt-handoff-pilot` owns the task package, bounded execution, and execution report protocol
- the active workflow line remains in current task artifacts rather than historical surfaces

## Example 4: Move from tool-name workflow to role-based handoff

Use `workflow-bootstrap` to convert a tool-name workflow into explicit role phases before handing execution protocol details to `chatgpt-handoff-pilot`.

Example prompt:

```text
Use workflow-bootstrap to restate this workflow as Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer.
Treat Copilot, Codex, ChatGPT, Cline, and DeepSeek only as adapter examples, not canonical requirements.
Keep task package, bounded execution, and execution report protocol ownership with chatgpt-handoff-pilot.
```

Expected framing:

- role boundaries and stage switches are explicit
- task package review is the safety gate before implementation
- tool names remain examples rather than requirements

## Example 5: Select review tier before bounded execution

Use `workflow-bootstrap` review tier guidance to choose an advisory review strength before implementation.

Example prompt:

```text
Use workflow-bootstrap as Reviewer to classify this task package as Light Review, Standard Review, or Heavy Review.
Keep the tier advisory, preserve chatgpt-handoff-pilot protocol ownership, and do not treat runtime pack or automation examples as implementation authorization.
```

Expected framing:

- review tier selection supports Reviewer judgment
- `chatgpt-handoff-pilot` remains protocol owner
- runtime pack and automation mentions stay classification examples only

## Example 6: Review runtime pack minimal surfaces

Use `workflow-bootstrap` to check whether project-side runtime surfaces stay thin and optional.

Example prompt:

```text
Use workflow-bootstrap to review runtime pack minimal surface guidance.
Confirm that AGENTS.md, Copilot instructions, and task artifacts are treated as project-side thin entries or evidence indexes, not canonical copies or mandatory global files.
Keep task package and execution report protocol ownership with chatgpt-handoff-pilot.
```

Expected framing:

- runtime pack guidance stays project-aware and optional
- `skills/` remains the canonical source
- deferred surfaces such as .github/instructions, .github/agents, tool adapters, validators, and automation are not implementation targets
