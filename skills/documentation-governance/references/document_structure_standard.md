# Document Structure Standard

This file explains the structure model defined in `SKILL.md`.
It does not define an alternative rule system.

## Layers

- `docs/`: engineering and source-of-truth layer
- `docs_readable/`: reader-oriented derivative layer

## Shared Category Vocabulary

Use the same category names referenced in `SKILL.md` and `default_governance.json`:

- `architecture`
- `design`
- `decisions`
- `runbooks`
- `reference`
- `api`
- `onboarding`

## Placement Guidance

Prefer these placements:

- `docs/architecture/`
- `docs/design/`
- `docs/decisions/`
- `docs/runbooks/`
- `docs/reference/`
- `docs/api/`
- `docs_readable/architecture/`
- `docs_readable/design/`
- `docs_readable/decisions/`
- `docs_readable/reference/`
- `docs_readable/api/`
- `docs_readable/onboarding/`

`onboarding` is readable-first.
`runbooks` are engineering-first unless a file is explicitly a reader summary.

## Reading Rule

Do not mirror the whole engineering tree into `docs_readable/`.
Only create readable derivatives when there is a real reading need.
