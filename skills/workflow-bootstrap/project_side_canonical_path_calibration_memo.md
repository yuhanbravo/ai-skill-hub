# Project-Side Canonical Path Calibration Memo (Phase 3D)

Status: this is a bounded calibration memo for the current single consumer repo pilot context.

This document does **not** authorize multi-repo rollout, distribution, or expansion of the project-side runtime surface.

## Purpose

Calibrate how project-side entrypoints should express canonical guidance paths after the Phase 3C real-repo implementation pilot.

This memo focuses only on path stability, placeholder control, and anti-drift behavior for the current pilot repo.

## Current Pilot Repo Context

Current pilot repo facts relevant to path calibration:

1. `AGENTS.md` already exists as the thin project-side master entrypoint.
2. `.github/copilot-instructions.md` already exists as the Copilot-specific thin adapter.
3. Concrete canonical guidance paths already exist for:
   - `skills/workflow-bootstrap/SKILL.md`
   - `skills/chatgpt-handoff-pilot/SKILL.md`
   - the active task package under `tasks/`
4. The repo does **not** currently define a separate project-local canonical payload artifact beyond those concrete canonical references.

## Calibration Goal

The goal is to make canonical path expression:

1. clearer than the Phase 3C wording;
2. less likely to drift;
3. still thin and reference-first;
4. still incompatible with second-rulebook expansion.

## Decision

### Decision Summary

For the current pilot repo, `<project-local-canonical-skill-path>` should **not** be materialized into a concrete path yet.

### Why Not Materialize Now

1. There is no distinct project-local canonical payload file to point at today.
2. Converting the placeholder into an invented local path would create false certainty rather than reduce ambiguity.
3. Repointing the placeholder to an already-listed canonical file would blur the difference between:
   - required concrete canonical references; and
   - a conditional project-local payload reference.
4. Creating a new file only to satisfy the placeholder would violate the bounded goal of this phase and increase second-rulebook risk.

## Recommended Path Strategy

Use a **controlled placeholder** strategy in the current pilot repo:

1. Keep concrete relative file paths for the already-existing required canonical guidance.
2. Keep `<project-local-canonical-skill-path>` only as a conditional placeholder.
3. State explicitly that the placeholder is maintainer-filled only.
4. State explicitly that it may remain unresolved only while no distinct project-local canonical payload artifact exists.
5. State explicitly that if such an artifact is later introduced, `AGENTS.md` is the place where its path must be declared first.

## Recommended Wording Direction

### For `AGENTS.md`

`AGENTS.md` should express the path model as:

1. concrete file paths for current required canonical guidance;
2. a controlled conditional placeholder for a future project-local canonical payload path;
3. a short statement covering:
   - who fills it;
   - when it may be filled;
   - when it may remain unresolved.

### For `.github/copilot-instructions.md`

The Copilot adapter should stay thinner than `AGENTS.md` and only tighten backreference behavior by clarifying:

1. `AGENTS.md` remains the source for repo-wide entrypoint guidance;
2. any future project-local canonical payload reference must be declared in `AGENTS.md`, not invented in the adapter;
3. the adapter should only mirror the already-declared path model, not define a new one.

## Fields That Still Need Maintainer Confirmation

The following must remain maintainer-confirmed, not AI-invented:

1. whether the repo ever adds a distinct project-local canonical payload artifact;
2. the exact path of that artifact if it is later created;
3. whether the artifact is truly canonical payload rather than a local note or convenience document;
4. whether the future path belongs in `AGENTS.md` only, or also needs to appear in `.github/copilot-instructions.md`.

## Highest Drift Risks

The highest-risk drift points are:

1. inventing a placeholder replacement before a real canonical payload artifact exists;
2. copying canonical guidance text into local entry files instead of keeping references;
3. letting `.github/copilot-instructions.md` define path policy separately from `AGENTS.md`;
4. leaving the placeholder unexplained so later editors fill it inconsistently;
5. treating the current single-repo decision as if it were already a multi-repo template standard.

## Boundary Reminder

This memo supports only single consumer repo pilot follow-up calibration.

It does **not** mean:

1. rollout readiness is complete;
2. distribution has started;
3. the general template is finalized;
4. `.github/instructions/*.instructions.md` or `.github/agents/*.agent.md` should be introduced now.
