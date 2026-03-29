---
name: file-structure-check
description: "Adapter entry for folder-structure audits, missing paths, and misplaced-file detection. Canonical source is in skills/file-structure-check."
metadata:
  triggers:
    - audit repository folder structure
    - check required directories and paths
    - detect misplaced files in a repo
    - validate project layout against a profile
    - generate a structure audit report
  side_effects:
    - read_only
    - write_files
  canonical_path: ../../../skills/file-structure-check
  adapter_type: thin-wrapper
---

# file-structure-check

- Canonical skill directory: `../../../skills/file-structure-check`
- Canonical skill definition: `../../../skills/file-structure-check/SKILL.md`
- Use this wrapper for discovery only. Read the canonical skill before execution.
