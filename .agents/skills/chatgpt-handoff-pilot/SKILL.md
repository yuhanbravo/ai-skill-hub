---
name: chatgpt-handoff-pilot
description: "Adapter entry for handoff task packages, bounded execution, and execution reports. Canonical source is in skills/chatgpt-handoff-pilot."
metadata:
  triggers:
    - prepare a handoff task package
    - bounded execution with execution report
    - split planning and implementation across AI agents
    - update the project handoff manual
    - enforce task boundaries for another agent
  side_effects:
    - read_only
    - write_files
  canonical_path: ../../../skills/chatgpt-handoff-pilot
  adapter_type: thin-wrapper
---

# chatgpt-handoff-pilot

- Canonical skill directory: `../../../skills/chatgpt-handoff-pilot`
- Canonical skill definition: `../../../skills/chatgpt-handoff-pilot/SKILL.md`
- Use this wrapper for discovery only. Read the canonical skill before execution.
