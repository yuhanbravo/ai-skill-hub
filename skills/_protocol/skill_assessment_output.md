# Skill Assessment Output Protocol

This shared protocol defines a common output vocabulary for skill assessment, review, governance, takeover, audit, migration, status, and handoff work. It is the single horizontal reference for assessment output fields; individual skills should reference it and trim fields by scenario instead of copying the protocol into each `SKILL.md`.

## Scope

- Use this protocol when an output includes assessment, review, takeover, governance, audit, migration, status, or handoff judgment.
- Use only the fields that fit the skill scenario; status / handoff skills should not be forced into scoring.
- Keep local skill instructions thin. Do not duplicate this protocol as another rulebook.

## Priority Vocabulary Boundary

The P0 task priority for this implementation round is not the same layer as `risk_priority`.

- Task priority `P0` describes why this repository change is urgent in the current work plan.
- `risk_priority` `P0` / `P1` / `P2` classifies risk inside an assessment output.
- A P0 task can create or update guidance for P1/P2 risks, and a P1/P2 task can still report a `risk_priority: P0` finding if safe use or auditability is affected.
- `risk_priority` belongs to the assessment output layer.
- `risk_priority` is not the same as a project phase gate.
- `risk_priority` is not the same as a freshness or staleness label.
- `phase_risk` and `freshness_risk` may appear in status / handoff outputs as scenario vocabulary, but they do not replace `risk_priority`.

## Fields

### capability_fit

Describe whether the assessed skill, workflow, project, or system capability fits the requested use case.

Use concise values such as:

- `fit`
- `partial`
- `misfit`
- `not verified`

### maturity_score

Optional / where applicable. Use this only when scoring maturity is natural for the skill output, such as skill governance, takeover, or structured assessment.

Suggested 1-5 scale:

- `1`: only conceptual
- `2`: usable but output varies by executor
- `3`: stable steps and output structure
- `4`: evidence / risk / fallback rules included
- `5`: supported by automated or strong validation

Important boundaries:

- The P0 objective is not to raise every skill to score 5.
- `maturity_score` is optional / where applicable.
- status / handoff skills should not be forced to use `maturity_score`.

### evidence

Record the evidence behind the output and classify it by certainty:

- `confirmed`: directly observed in files, commands, repository state, tool output, or user-provided source material.
- `inferred`: reasoned from confirmed facts but not directly observed.
- `pending`: not yet verified or blocked by missing access, missing input, or skipped validation.

### inference

Separate reasoning from evidence. Use this field for conclusions drawn from confirmed facts, and mark uncertainty when the reasoning depends on assumptions.

### open_questions

List questions that remain unresolved and could affect implementation, review, handoff, or future planning.

### risk_priority

Classify risk by effect, not by task priority:

- `P0`: affects repeatability, auditability, or safe use
- `P1`: affects workflow linkage, consistency, or usability
- `P2`: automation, CI, scripts, or long-term maintainability

### impact_scope

Classify how widely a finding or recommendation applies:

- `local`: one file, one skill, one project, or one bounded task surface
- `layer`: one capability layer, documentation layer, status layer, adapter layer, or similar grouped surface
- `system`: cross-layer or repository/system-wide effect

### next_action

State the next concrete action. Prefer bounded actions such as:

- `accept`
- `revise`
- `defer`
- `verify`
- `escalate`
- `prepare task package`

## Usage Rules

- Core assessment / takeover / governance skills should use `maturity_score`, `evidence`, `inference`, `open_questions`, `risk_priority`, `impact_scope`, and `next_action` where applicable.
- Audit and migration skills may trim fields to the scenario while keeping evidence, risk, scope, and next action explicit.
- Status and handoff skills should favor `evidence`, `open_questions`, `risk_priority`, `phase_risk`, and `freshness_risk`; do not force `maturity_score`.
- `workflow-bootstrap` may reference this protocol only for assessment output and handoff/status linkage awareness. It does not own task package, bounded execution, or execution report protocol.
- `chatgpt-handoff-pilot` may reference this protocol for execution report risk and evidence awareness. It remains the owner of task package, bounded execution, and execution report protocol.

## Mini Examples

### Example A: takeover / governance assessment

```yaml
capability_fit: fit
maturity_score: 4
evidence:
  confirmed:
    - The skill defines a system-level assessment scope and explicit non-ownership boundaries.
    - The output contract already includes capability mapping, maturity review, bottlenecks, and next steps.
  inferred:
    - The skill can use this shared protocol without replacing its domain-specific takeover guidance.
  pending:
    - Cross-run consistency still depends on executor discipline because no validator is in scope.
inference: The skill is mature enough for structured governance-style assessment, with light example alignment needed to reduce output drift.
open_questions: not applicable
risk_priority: P1
impact_scope: layer
next_action: revise
```

### Example B: status / handoff assessment

```yaml
capability_fit: partial
maturity_score: not applicable
evidence:
  confirmed:
    - The handoff/status output identifies freshness and phase consistency concerns.
    - The task package limits the work to documentation-only follow-up.
  inferred:
    - A maturity score would add little value because the output is checking current state continuity, not capability maturity.
open_questions: not applicable
risk_priority: P1
impact_scope: local
next_action: verify
```

`maturity_score` is not applicable in this status / handoff example because the scenario primarily evaluates freshness, phase consistency, and unresolved gaps. Status / handoff outputs should not be forced into maturity scoring.
