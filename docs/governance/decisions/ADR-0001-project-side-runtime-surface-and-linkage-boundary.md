# ADR-0001: Project-side Runtime Surface and Workspace Linkage Boundary

## Status

Accepted

## Date

2026-06-03

## Context

`ai-skill-hub` uses `skills/` as the canonical source for skill guidance.
The `.agents/skills/` and `.github/skills/` trees are derivative adapter and discovery surfaces, not authoring sources.

Target projects may already contain AI-facing files such as `AGENTS.md`, `.github/copilot-instructions.md`, `.agents/**`, `.github/instructions/**`, or `tasks/**`. Re-initializing or rewriting those local AI files can create path invention, second-rulebook drift, canonical skill body copies, and unsupported rollout or distribution claims.

Phase 4 pilot work, review packets, and execution evidence are useful inputs, but they do not automatically authorize multi-repository rollout, distribution readiness, or canonical guidance changes.

## Decision

### Existing AI Repositories Use Incremental Linkage

Existing AI file repositories should be scanned first and linked incrementally. Implementation should use the smallest patch that preserves existing local rules instead of reinitializing or rewriting the local AI file system.

### Project-side Runtime Surfaces Must Remain Thin

Project-side runtime surfaces may act as thin entries, adapters, routing notes, or evidence indexes. They must not become a second rulebook, copy canonical skill bodies, or redefine the `chatgpt-handoff-pilot` task package, bounded execution, or execution report protocol.

### Canonical Guidance Must Be Referenced, Not Copied

Project-side entries and adapters should point back to canonical guidance under `skills/`. They must not copy full skill bodies into local project entries, and adapter layers must not become the authoring source.

### No Invented Project-local Canonical Path

Do not invent `<project-local-canonical-skill-path>`. Reference it only when a maintainer has provided a real project-local canonical payload artifact. Do not make any adjacent workspace location a globally applicable default.

### Forbidden or Deferred Runtime Surfaces Remain Deferred

This decision does not create or authorize default use of these surfaces or mechanisms:

- `.github/instructions/**`
- `.github/agents/**`
- `.agents/skills/**`
- `.github/skills/**`
- `skills_index.json`
- `SKILLS_INDEX.md`
- tool adapters
- validators
- automation
- CI

Future introduction of any of these requires a separate task package and review.

### Evidence Mode Is Project-aware

Git-first projects may prioritize branch, commit, pull request, and diff evidence. Non-git or low-git projects may use task packages and execution reports as the primary evidence path. `tasks/` may be a preferred project-local evidence path, but it is not a mandatory global path for every project.

### Pilot Evidence Does Not Imply Wider Readiness

Phase 4 pilot work and review evidence remain evidence. They do not automatically promote content into canonical guidance and do not establish readiness for multi-repository rollout, distribution, adoption, validators, CI, or automation.

### Future Promotion Requires a Separate Reviewed Task

Any promotion from review evidence, prompts, patterns, or task reports into canonical guidance requires a separate task package and final review.

## Consequences

Positive effects:

- Reduces AI-driven path invention risk.
- Reduces second-rulebook and skill body copy risk.
- Makes linkage for existing AI file repositories more conservative.
- Keeps `skills/` ownership clear.
- Allows Git-first and low-git projects to use different evidence modes.

Costs:

- The repository cannot claim broad rollout readiness from this decision alone.
- Each project still needs maintainer confirmation of linkage mode.
- Some runtime surfaces still require future independent review.
- This ADR does not replace task packages, execution reports, status refreshes, or review memos.

## Non-Goals

This ADR does not:

- Implement a project-side runtime pack generator.
- Add `.github/instructions/**` or `.github/agents/**`.
- Add tool adapters, validators, automation, or CI.
- Modify skill execution logic.
- Modify adapter generation logic.
- Change `chatgpt-handoff-pilot` ownership of task package, bounded execution, or execution report protocol.
- Change `workflow-bootstrap` ownership of workflow shell and runtime surface guidance.
- Force `tasks/` as the path for all projects.
- Declare distribution, rollout, or adoption as complete.

## Follow-up Candidates

These are possible future tasks, not actions authorized by this ADR:

- Phase 4 runtime pack wording audit
- Template Registry indexing review for the workspace linkage prompt
- AI file inventory checklist
- Thin runtime surface pattern
- Git-first versus non-git evidence pattern
- Project-side runtime surface promotion checklist
