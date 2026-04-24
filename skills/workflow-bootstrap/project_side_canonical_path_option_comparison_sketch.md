# Project-Side Canonical Path Option Comparison Sketch (Phase 3D)

Status: this is a bounded comparison sketch for the current pilot repo only.

This document does **not** authorize new project-side file families, rollout, or distribution.

## Purpose

Compare the smallest viable options for handling `<project-local-canonical-skill-path>` after the Phase 3C real-repo pilot.

## Current Constraint

The current pilot repo already has concrete required canonical references, but it does **not** have a separate project-local canonical payload artifact.

## Option 1: Keep a Controlled Placeholder

### Shape

Keep:

- `<project-local-canonical-skill-path>`

but label it as conditional, maintainer-filled, and unresolved by design until a real project-local canonical payload artifact exists.

### Advantages

1. Matches the real repo state without inventing a fake path.
2. Preserves the distinction between concrete required references and optional future project-local payload.
3. Minimizes drift by making the unresolved state explicit instead of implicit.
4. Avoids widening the project-side runtime surface.

### Risks

1. Future editors may still misunderstand it if the control language is weak.
2. Placeholder state can linger too long if nobody re-evaluates it after the repo changes.

### Maintainer Confirmation Needed

1. Whether the repo later gains a distinct project-local canonical payload artifact.
2. Whether the placeholder should then be replaced in `AGENTS.md`.

### Recommendation

`Recommended now`

## Option 2: Materialize as a Repo-Local Path Immediately

### Shape

Replace the placeholder with a concrete repo-local path in the current repo now.

### Advantages

1. Removes the visual placeholder.
2. Can look more final at a glance.

### Risks

1. No valid distinct target currently exists.
2. Any immediate replacement would either duplicate an already-listed canonical path or invent a new pseudo-canonical artifact.
3. This increases wrong-copy and second-rulebook risk.

### Maintainer Confirmation Needed

1. Proof that a distinct repo-local canonical payload artifact already exists.
2. Confirmation that the target is canonical payload rather than a convenience note.

### Recommendation

`Not recommended now`

## Option 3: Materialize as a Project-Local Canonical Payload Path

### Shape

Replace the placeholder with the path to a dedicated project-local canonical payload artifact.

### Advantages

1. Cleanest long-term expression if such an artifact truly exists.
2. Makes the project-fill field concrete and unambiguous.

### Risks

1. The current pilot repo does not define such an artifact.
2. Creating one just to satisfy the placeholder would expand scope.
3. If created carelessly, it could become a second local rulebook.

### Maintainer Confirmation Needed

1. That a distinct payload artifact is necessary.
2. That its ownership and canonical status are intentional.
3. That its content stays narrower than a second rulebook.

### Recommendation

`Potential later option, not recommended now`

## Option 4: Remove the Placeholder Entirely

### Shape

Delete the placeholder and keep only the currently concrete canonical references.

### Advantages

1. Simplifies the file visually.
2. Removes a future fill point.

### Risks

1. Loses the already-established project-fill slot from Phase 3A / 3B / 3C.
2. Makes future addition of a real project-local canonical payload path less legible.
3. Hides rather than resolves the calibration question.

### Maintainer Confirmation Needed

1. Confirmation that the repo should never carry a project-local canonical payload slot.

### Recommendation

`Not recommended now`

## Comparison Summary

| Option | Drift risk | Scope risk | Current fit | Recommendation |
| --- | --- | --- | --- | --- |
| Controlled placeholder | Low-to-moderate | Low | Strong | Recommended now |
| Immediate repo-local path | High | Moderate | Weak | Not recommended now |
| Dedicated project-local payload path | Moderate | High | Weak today | Later only if needed |
| Remove placeholder entirely | Moderate | Low | Weak | Not recommended now |

## Final Recommendation

Keep `<project-local-canonical-skill-path>` as a **controlled placeholder** for the current pilot repo.

Use concrete paths for the already-existing required canonical guidance, and reserve placeholder materialization for a later point only if a distinct project-local canonical payload artifact is intentionally introduced and maintainer-confirmed.
