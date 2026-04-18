# AGENTS.md

## Repository purpose

This repository is a shared multi-AI skill hub.

It is not a normal application repo. Its primary purpose is to maintain:
- canonical skills
- adapter / distribution layers for different AI consumers
- governance and indexing mechanisms
- docs for AI, human, and bridge audiences
- tooling that keeps the above consistent

When working here, optimize for clarity, stability, reuse, and low-drift maintenance.

---

## Working priorities

Prefer this order of importance:

1. Preserve correct repository structure and layer boundaries
2. Keep canonical skill content stable and clear
3. Reduce doc drift and adapter inconsistency
4. Improve newcomer usability without causing structural churn
5. Prefer low-risk, incremental improvements over broad refactors

Do not assume that “less files” or “flatter structure” is automatically better.

---

## Main repository layers

Typical areas you should inspect before proposing changes:

- `skills/`
  - canonical skill definitions and source-of-truth content

- `.agents/skills/`
  - adapter / consumer-facing distribution layer

- `.github/skills/`
  - GitHub/Copilot-facing fallback or distribution layer

- `docs/ai/`
  - instructions and protocol docs written for AI consumption

- `docs/human/`
  - documentation written primarily for human readers

- `docs/bridge/`
  - bridge-layer docs between human and AI operating models

- governance-related docs and tools
  - indexing
  - metadata generation
  - adapter consistency checks
  - sync/export/import tooling
  - validation and smoke tests

If a task touches one layer, check whether neighboring layers need aligned updates.

---

## Default working mode

For complex or repo-wide tasks:
- inventory first
- assess second
- plan before implementation

Do not jump straight into edits when the task involves:
- many skills
- multiple layers
- governance rules
- doc restructuring
- naming or taxonomy changes

If the task is ambiguous, produce a short plan before making changes.

---

## Change boundaries

Unless the task explicitly asks for broader work:

- do not do large repo-wide renames
- do not collapse distinct layers into one without strong justification
- do not rewrite docs wholesale
- do not move canonical content and adapter content together unless necessary
- do not introduce new tooling if a smaller documentation or validation fix is enough
- do not change historical or governance documents casually

Prefer section-aware, targeted edits.

---

## Source-of-truth rules

When there is tension between code/scripts and docs:
- verify the current implementation first
- align documentation to actual current behavior unless the task explicitly asks to change behavior

When there is tension between canonical skill content and distribution copies:
- treat canonical content as the source of truth
- update adapters/distribution carefully and consistently

Do not silently let duplicated content drift.

---

## Expectations for proposals

When proposing improvements, separate them into:
- low-risk / high-value improvements
- medium-scope governance improvements
- high-disruption structural changes

For each proposal, explain:
- why it matters
- expected benefit
- likely cost or risk
- whether it should be done now

Do not recommend large restructuring without showing the concrete maintenance pain it solves.

---

## Validation expectations

When making changes, validate proportionally.

Possible validation includes:
- targeted smoke tests
- consistency checks
- metadata/index regeneration checks
- adapter/distribution alignment checks
- basic doc reference sanity checks

If you change commands, paths, filenames, or repo structure, verify references that could break.

Do not claim validation you did not actually run.

---

## Documentation expectations

Keep documentation:
- accurate
- scoped
- non-redundant
- audience-aware

Respect the intended split between:
- AI-facing docs
- human-facing docs
- bridge docs

Do not merge these audiences casually.

If documentation gets too large, keep the top-level explanation concise and point to deeper docs rather than duplicating everything.

---

## Output expectations for substantial tasks

For substantial tasks, prefer outputs in this order:
1. brief repo understanding
2. identified issues
3. recommended plan
4. implementation only after scope is clear
5. concise execution summary after changes

If the task is planning-only, do not edit files.

---

## Done means

A task is done only when:
- the requested scope is satisfied
- changes stay within the intended layer boundaries
- any updated docs match actual current behavior
- validation appropriate to the change has been run
- the final summary clearly states what changed and what was not changed

If something remains uncertain, say so explicitly.