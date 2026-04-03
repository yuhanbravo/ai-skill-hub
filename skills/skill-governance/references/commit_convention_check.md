# Commit Convention Check

## Purpose

`commit-convention-check` validates repository commit messages against the formats already used in `ai-skill-hub` and documented in [docs/governance/COMMIT_CONVENTION.md](../../../docs/governance/COMMIT_CONVENTION.md).

## Accepted Subject Formats

- `<type>: <action>`
- `<type>(<scope>): <action>`
- `<type>: Phase <n>[.<m>] - <scope> - <action>`

## Accepted Types

- `docs`
- `feat`
- `fix`
- `refactor`
- `test`
- `chore`

## Body Rules

- If a body exists, it must be separated from the subject by one blank line.
- The body may use plain paragraphs or `- ` list items.
- The body must contain at least one non-empty descriptive line after the blank separator.
- Avoid filler-only body lines such as `misc`, `stuff`, or `update`.

## Phase Boundary

- `Phase` is reserved for repository or system evolution commits.
- Execution phases such as `scan`, `understand`, `audit`, or `report` are not treated as commit `Phase` values.
- If a subject starts with `Phase`, it must use the numeric phase format.

## Expansion Policy

- Add new `type` values only after a stable repository usage pattern appears.
- Keep `docs/governance/COMMIT_CONVENTION.md`, this rule, the validator script, and tests in sync.
