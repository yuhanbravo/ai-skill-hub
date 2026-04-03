# Human Layer

This directory holds explanation-oriented material for maintainers and reviewers.

## Ownership

- Status: canonical home for human-facing explanation guides created by the semantic split
- Owns: repository reading guidance, lifecycle explanation, and phase vocabulary
- Does not own: active handoff/status artifacts, AI invocation rules, or governance policy docs

## Contents

- `REPOSITORY_OVERVIEW.md`: human-readable repository overview mirrored from the root `README.md`
- `PROJECT_LIFECYCLE.md`: lifecycle explanation for project-type work
- `PHASE_MODEL.md`: stable phase vocabulary reference
- `REPOSITORY_CONSUMPTION_GUIDE.md`: human-facing guidance split out of `AI_USAGE.md`

## Quick Start

1. In each new clone or worktree, run `powershell.exe -NoProfile -ExecutionPolicy Bypass -File tools\install_git_hooks.ps1`.
2. Read [`../governance/COMMIT_CONVENTION.md`](../governance/COMMIT_CONVENTION.md) before the first commit.
3. If the hook rejects a message, fix the subject or body and retry the commit.

Governance-specific docs now live under `docs/governance/`.
This layer remains an explicit semantic grouping rather than a runtime surface.
