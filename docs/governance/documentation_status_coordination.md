# documentation-governance x update-project-status Coordination

`《documentation-governance × update-project-status 联动治理约定（最小版）》`

## 1. Purpose

This document defines the minimum coordination rules between the canonical skills `skills/documentation-governance` and `skills/update-project-status`.

Its goal is to reduce manual invocation conflicts, document-role confusion, and avoidable drift when both skills operate in the same repository.

This is a minimum governance note, not a full cross-skill orchestration specification.

## 2. Scope

This note applies to the canonical skills:

- `skills/documentation-governance`
- `skills/update-project-status`

It covers:

- role boundaries
- recommended invocation order
- shared document-role vocabulary
- minimum conflict-avoidance rules
- a small documentation-layer coordination example

It does not redefine:

- `SKILL.md` execution contracts
- existing CLI parameters or config semantics
- wrapper behavior under `.agents/skills/`
- automation, hooks, or repo-wide enforcement mechanisms

## 3. Skill Roles

`documentation-governance` owns documentation structure governance. Its primary concern is document layout, single-source-of-truth boundaries, duplicate-topic control, readable-layer boundaries, and README governance. It should answer questions such as "which layer should own this topic", "is this a duplicate", and "is this file a report, a readable derivative, or an active source".

`update-project-status` owns project status refresh. Its primary concern is collecting recent signals and producing current-state outputs such as status snapshots, status logs, and handoff-ready status summaries. It should answer questions such as "what changed recently", "what is the current status", and "which status artifact should be refreshed".

The two skills are complementary rather than competing:

- `documentation-governance` decides or audits document roles and boundaries
- `update-project-status` refreshes state-oriented artifacts within those boundaries

## 4. Recommended Invocation Order

### First-time adoption or repo re-orientation

Recommended order:

1. `documentation-governance audit`
2. `update-project-status refresh`

Why this is steadier:

- the audit pass clarifies which file is the primary current-state source
- it distinguishes status artifacts from governance reports, readable derivatives, and mirror copies
- it reduces the chance that a later governance pass treats valid status outputs as generic topic duplicates

The reverse order is not a hard conflict. A repository can still run `update-project-status` first. The risk is mostly governance noise: a later documentation audit may need extra work to classify fresh status files, logs, or mirrored outputs that were produced before role boundaries were made explicit.

### Day-to-day operation

Recommended default:

- run `update-project-status` at higher frequency for routine freshness
- run `documentation-governance` at lower frequency as an audit pass

They do not need to run together every time. Daily or routine work usually needs a fresh status output more often than it needs a structural document audit. Governance should re-enter when the repo adds new document families, naming drift appears, duplicate-topic risk increases, or status/readable/mirror roles start to blur.

## 5. Shared Document Roles

The two skills should use the same role vocabulary when they refer to status-related files.

| Role | Meaning | Typical owner or producer | What it is not |
| --- | --- | --- | --- |
| `primary status doc / current-state SSOT` | The main current-state document used to understand the repository's active status or handoff state. In this repository, `docs/HANDOFF.md` is the current example. | Repo-defined active source, optionally refreshed in explicit managed sections | Not a generic duplicate of snapshot pages, not a readable summary, not a mirror copy |
| `status snapshot docs` | Refreshable point-in-time or template-shaped status outputs. In this repository, `docs/status/skill-hub-status.md` is the clearest example. | `update-project-status` | Not the append-only log, not the repository-governance report layer |
| `status log` | Chronological update trail for status refresh activity. It records status evolution over time rather than owning the current-state narrative. | `update-project-status` | Not a topic doc, not a README substitute, not a dedupe target in the same sense as normal prose docs |
| `governance reports` | Audit results, governance notes, and structure or role decisions. This includes documentation-governance outputs and repository-governance notes. | `documentation-governance` or maintainers | Not the current project state SSOT, not a status snapshot |
| `readable / derived docs` | Audience-oriented derivatives that improve readability or onboarding while staying downstream from engineering or governance facts. In repositories that use it, `docs_readable/` is this layer. | Human or AI documentation workflows | Not a new authority layer and not the primary current-state owner |
| `bridge / mirror docs` | Optional continuity or navigation copies that mirror an active source without taking ownership. In this repository, `docs/bridge/` contains this kind of artifact. | Mirror / bridge maintenance flow | Not the active source when drift exists, not a default write target for status refresh |

## 6. Conflict-Avoidance Rules

The minimum coordination rules are:

- `documentation-governance` should not treat status docs, status logs, or governance reports as ordinary duplicate-topic documents by default.
- `documentation-governance` may still audit those files for placement, naming, ownership clarity, and mirror boundaries.
- `update-project-status` should not default to modifying `README.md`, readable-layer docs, or bridge/mirror docs.
- `update-project-status` should only write status snapshots, status logs, and explicitly authorized managed sections inside the primary status doc.
- if a repository keeps both an active source and a bridge or mirror copy, the active source remains authoritative unless an explicit migration changes ownership.
- both skills should keep the same non-invasive default posture: observe first, then write only when `fix`, `write`, or another explicit output action has been requested.

## 7. Minimal Coordination Example

The example below is a documentation-layer coordination note. It is not a required runtime schema and does not change either skill's current execution contract.

```json
{
  "primary_status_doc": "docs/HANDOFF.md",
  "snapshot_docs": [
    "docs/status/skill-hub-status.md"
  ],
  "status_logs": [
    "docs/status_updates.log"
  ],
  "governance_reports": [
    "docs/governance/*.md"
  ],
  "readable_layer": [
    "docs_readable/**/*.md"
  ],
  "exclude_from_duplicate_topic_checks": [
    "docs/HANDOFF.md",
    "docs/status/**/*.md",
    "docs/status_updates.log",
    "docs/governance/**/*.md",
    "docs/bridge/**/*.md"
  ]
}
```

Notes:

- `primary_status_doc` aligns with the existing SSOT-lite language already used by `update-project-status`
- the other keys are a small coordination expression for humans and AI operators, not a new enforced config contract
- repositories without a readable layer or bridge layer can omit those parts rather than inventing placeholder paths

## 8. Non-Goals

This document is intentionally small. It does not:

- define a full orchestration framework between the two skills
- introduce a new automation protocol, hook, or controller layer
- force both skills to run in a single pipeline
- change the canonical behavior described in either `SKILL.md`
- turn documentation-role hints into hard runtime enforcement

## 9. Suggested Operating Pattern

Use the following lightweight pattern:

1. When entering a repository for the first time, or after structural doc changes, run `documentation-governance` first to clarify role boundaries.
2. After role boundaries are clear, run `update-project-status` to refresh the primary status doc, snapshot docs, or status log within the approved write scope.
3. During normal maintenance, run `update-project-status` whenever status freshness matters, and only bring `documentation-governance` back when structure, ownership, or duplication risk needs another audit.

In short: governance defines the lanes; status refresh drives inside those lanes.
