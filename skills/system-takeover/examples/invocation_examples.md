# Invocation Examples

These examples were split out of `SKILL.md` to keep the execution contract focused.

### Input Example

```text
Use system-takeover for this task.

task_description:
- Analyze this skill-hub system and evaluate its capability architecture.

constraints:
- Do not modify protocol, router, pipeline, or existing skills.
- Treat this as a system-level takeover, not a business-project audit.

expected_output:
- System structure
- Capability map
- Layered maturity assessment
- Top bottlenecks
- Evolution plan

context_files:
- skills/
- tools/
- docs/
- .agents/
- .github/
- tests/
```

### Output Example

```text
execution_plan:
- Map the capability system structure and discovery layers.
- Assess invocation, routing, pipeline, adapter, tooling, and governance maturity.
- Synthesize bottlenecks and the next evolution phase.

changes_made:
- No source files were modified.
- Produced a structured system takeover analysis.

files_touched:
- skills/
- tools/
- docs/
- .agents/
- .github/
- tests/

risks:
- Some maturity judgments may remain provisional if enforcement evidence is incomplete.
- Adapter coverage can drift if canonical and compatibility layers are not continuously checked.
```

### Shared Assessment Protocol Example

```text
Use system-takeover for a system-level assessment.
Align the assessment output with the shared assessment output protocol.

expected_output:
- capability_fit
- evidence:
  - confirmed
  - inferred
  - pending
- inference
- risk_priority
- impact_scope
- next_action
- maturity_score only when applicable

constraints:
- Do not force maturity_score for status / handoff-style outputs.
- Do not replace system-status-update or system-handoff.
- Do not modify files unless separately authorized by the user.
```
