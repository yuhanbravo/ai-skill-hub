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
