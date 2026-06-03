# Governance Decisions

This directory holds repository-level decision records for stable governance boundaries. It is an ADR-lite home for decisions that should be easier to find than task evidence, without introducing a new approval workflow or toolchain.

## Relationship to Other Documents

- `docs/governance/decisions/`: stable repository-level decision records
- `docs/HANDOFF.md` and `docs/status/**`: current status, phase snapshots, and handoff state
- `docs/ai/PATTERNS/**`: reusable implementation patterns
- `docs/TEMPLATE_REGISTRY.md` and `docs/SKILL_CATALOG.md`: indexes, not ADR body text
- `tasks/**` and `docs/reviews/**`: execution or review evidence that does not automatically become a decision

## ADR-Lite Format

Decision records in this directory should stay small and use this shape:

- Status
- Date
- Context
- Decision
- Consequences
- Non-Goals
- Follow-up Candidates

Do not add a complex state machine, approval flow, numbering automation, or ADR toolchain here.
