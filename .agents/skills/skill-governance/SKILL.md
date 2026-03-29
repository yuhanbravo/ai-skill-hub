---
name: skill-governance
description: "Adapter entry for evaluating, scoring, diagnosing, and controlled refactoring of a single skill. Canonical source is in skills/skill-governance."
metadata:
  triggers:
    - evaluate a skill against the template
    - diagnose skill maturity and structure
    - score a skill and decide rewrite level
    - govern a single skill before refactor
    - perform a controlled skill rewrite
  side_effects:
    - read_only
    - write_files
  canonical_path: ../../../skills/skill-governance
  adapter_type: thin-wrapper
---

# skill-governance

- Canonical skill directory: `../../../skills/skill-governance`
- Canonical skill definition: `../../../skills/skill-governance/SKILL.md`
- Use this wrapper for discovery only. Read the canonical skill before execution.
