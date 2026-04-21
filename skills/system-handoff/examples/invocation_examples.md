# Invocation Examples

These examples were split out of `SKILL.md` to keep the execution contract focused.

### Input Example

```text
Use system-handoff for this task.

task_description:
- Update ai-skill-hub handoff as a system document without rewriting the whole file.

constraints:
- Reuse chatgpt-handoff-pilot as the canonical handoff flow.
- Keep docs/HANDOFF.md section-aware and system-oriented.
- Read `docs/status/skill-hub-status.md` first and keep phase consistent with the latest status baseline.

expected_output:
- Current Status
- Hard Boundaries
- Key Design Decisions
- Intentional Gaps
- Next Phase Direction

context_files:
- docs/HANDOFF.md
- docs/status/skill-hub-status.md
- README.md
```

### Output Example

```text
Current Status:
- Phase 3 - Controlled System
- Stable canonical layer with evolving governance and tooling

Hard Boundaries:
- skills/ remains the only canonical source of truth
- adapter layers remain derivative surfaces

Key Design Decisions:
- thin adapters preserve discoverability without duplicating content

Intentional Gaps:
- no auto-fix
- no orchestration controller

Next Phase Direction:
- move from controlled local governance toward controlled enforcement

Risks:
- section merges still depend on accurate identification of existing system sections.
```
