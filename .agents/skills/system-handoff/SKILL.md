---
name: system-handoff
description: "Adapter entry for updating ai-skill-hub handoff with section-aware system-level merge constraints. Canonical source is in skills/system-handoff."
metadata:
  triggers:
    - update ai-skill-hub system handoff
    - maintain skill-hub handoff sections
    - refresh system boundaries in docs HANDOFF md
    - capture next phase direction for ai capability system
    - merge system-level handoff updates without full rewrite
  side_effects:
    - read_only
    - write_files
  canonical_path: ../../../skills/system-handoff
  adapter_type: thin-wrapper
---

# system-handoff

- Canonical skill directory: `../../../skills/system-handoff`
- Canonical skill definition: `../../../skills/system-handoff/SKILL.md`
- Use this wrapper for discovery only. Read the canonical skill before execution.