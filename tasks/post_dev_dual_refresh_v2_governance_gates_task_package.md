# Post-Dev Dual Refresh v2 Governance Gates

## 1. Task Objective

Create a bounded follow-up implementation plan for a v2 governance enhancement of the existing `Post-Dev Dual Refresh Orchestration` snippet in `skills/workflow-bootstrap/orchestration_snippets.md`.

The later enhancement should refine the existing snippet into a more governed reusable invocation/orchestration pattern. It must remain:

- an orchestration-layer template owned by `workflow-bootstrap`;
- a thin invocation pattern over existing delegated skills;
- not a new skill;
- not a replacement for `update-project-status`;
- not a replacement for `chatgpt-handoff-pilot`;
- not a delegated protocol rewrite or third protocol.

This task package is planning only. It does not authorize implementation of the v2 snippet update.

## 2. Dogfood Evidence Summary

Two downstream dogfood rounds showed that the basic post-development dual-refresh chain can work:

1. Run `update-project-status` to refresh status-oriented outputs.
2. Transfer a bounded status summary into `chatgpt-handoff-pilot`.
3. Refresh handoff-oriented outputs and produce a merged round receipt.

The latest dogfood also identified generic mechanism-level governance gaps that should be addressed before the snippet is treated as a reusable pattern:

- Payload persistence ambiguity: the template needs an explicit decision point for whether a transfer payload stays transient or is persisted somewhere.
- Validation provenance ambiguity: the template must distinguish PR-reported validation, locally rerun source/test validation, refresh-level checks, skipped validation, partial validation, and failed validation.
- Stale wording scan layering: the template must distinguish current-state sections from historical update-log entries so historical wording is not over-normalized while current snapshot wording is not left stale.
- Status / HANDOFF / log role separation: the template needs clearer guidance that status remains a snapshot, handoff remains the operational takeover interface, and logs remain terse timelines.
- Branch/head provenance distinction: the template must distinguish the project mainline baseline or merged PR commit from documentation refresh branch HEAD, and distinguish pre-write observations from post-write branch state.
- Final reviewer gate need: the final review should include explicit governance checks rather than only broad boundary and validation checks.
- Evidence pointer narrowing: evidence pointers should be useful for review without turning a status snapshot into a file-level changelog or copying unrelated runtime artifacts.

This summary is intentionally generic. Do not embed downstream project names, PR numbers, commit hashes, project phase names, domain boundaries, validation counts, storage policies, or allowed-file lists in the reusable template.

## 3. Non-Goals

This v2 governance task explicitly does not authorize:

- no new skill;
- no rewrite of `update-project-status`;
- no rewrite of `chatgpt-handoff-pilot`;
- no delegated protocol duplication;
- no real status refresh;
- no real handoff refresh;
- no adapter sync;
- no generated metadata update;
- no implementation in this planning run;
- no modification of `skills/workflow-bootstrap/orchestration_snippets.md` during this planning run;
- no modification of `README.md`, `SKILLS_INDEX.md`, `skills_index.json`, repository status files, repository handoff files, or status logs during this planning run;
- no hook installation;
- no push.

## 4. Proposed Implementation Scope For Later

### Primary target

- `skills/workflow-bootstrap/orchestration_snippets.md`

### Allowed optional target only if later approved

- `skills/workflow-bootstrap/examples/invocation_examples.md`

### Forbidden unless separately approved

- `skills/update-project-status/SKILL.md`
- `skills/chatgpt-handoff-pilot/SKILL.md`
- adapter layers, including `.agents/**`, `.github/**`, and equivalent runtime wrappers
- generated indexes or metadata, including `SKILLS_INDEX.md` and `skills_index.json`
- repository status files, handoff files, or logs, including `docs/status.md`, `docs/status/**`, `docs/status_updates.log`, and `docs/HANDOFF.md`

## 5. Required v2 Additions

The later implementation should add or refine the following blocks inside the existing `Post-Dev Dual Refresh Orchestration` snippet without copying delegated skill protocol bodies.

### A. Payload persistence policy

The later snippet should include a structured decision block:

```yaml
payload_persistence_decision:
  mode: transient | status_snapshot | status_log | trial_notes | pr_body_only
  reason:
```

Required rules:

- default mode should be `transient`;
- `status_snapshot` requires an explicit reason;
- `trial_notes` is preferred for dogfood or mechanism evidence;
- never persist a full transfer payload into the status snapshot by default;
- if payload persistence is not explicitly approved, treat the payload as transient handoff input only.

### B. Validation provenance

The later snippet should include a validation provenance block:

```yaml
validation_provenance:
  pr_reported:
    status: present | absent
    source:
    commands:
      -
  locally_rerun:
    status: not_run | passed | failed | partial
    commands:
      -
  refresh_validation:
    status: not_run | passed | failed | partial
    commands:
      -
  note:
```

Required rules:

- do not represent PR-reported validation as locally rerun validation;
- refresh-level checks such as `git diff --check` must be separated from source/test validation;
- skipped or unavailable validation must be marked explicitly rather than implied;
- failed validation must remain visible in the final receipt and final reviewer checklist.

### C. Stale wording scan layering

The later snippet should include a stale wording scan block:

```yaml
stale_wording_scan:
  checked: yes | no
  current_state_sections_clean: yes | no
  historical_update_log_references:
    -
  accidental_stale_references:
    -
  action_taken:
    -
```

Required rules:

- historical update-log entries may preserve old branch or pending wording if clearly historical;
- current-state sections must not retain pending, branch-only, pre-merge, or pre-refresh wording after merge or refresh facts are known;
- the scan should report both preserved historical references and accidental stale references;
- the scan should not force full-file rewrites of status or handoff documents.

### D. Branch/head provenance distinction

The later snippet should distinguish:

- merged PR commit / mainline baseline;
- current documentation refresh branch HEAD;
- pre-write observation;
- post-write branch state.

Required rules:

- do not claim the refresh branch HEAD equals the mainline baseline after docs-only commits are added;
- distinguish facts observed before writing from the branch state after documentation refresh commits;
- prefer wording such as:
  - `project mainline baseline observed at <merge commit>`;
  - `documentation refresh branch contains docs-only commit(s) on top of that baseline`;
- if the exact baseline cannot be verified, mark it as unknown or observed from available evidence rather than inventing a commit relationship.

### E. Status / HANDOFF / log role separation

Required rules:

- `status.md` = snapshot;
- `status_updates.log` = terse timeline;
- `HANDOFF.md` = operational SSOT / takeover interface;
- trial notes or task report = mechanism evidence;
- do not put large transfer payloads in status by default;
- do not turn a status snapshot into a project-level changelog;
- do not use the handoff document as a raw runtime artifact dump.

### F. Evidence pointer rules

Required rules:

- include target PR, merge commit, task package, changed files, and refreshed docs when available and appropriate;
- keep pointers narrow and review-oriented;
- avoid raw runtime artifacts, local absolute paths, real data, credentials, or broad unrelated file changelogs;
- summarize changed file categories where possible instead of enumerating unrelated or noisy files;
- avoid copying downstream project-specific facts into the reusable template.

### G. Final reviewer checklist

The later snippet must add a final reviewer checklist covering:

- file scope;
- source/runtime safety;
- payload persistence;
- validation provenance;
- stale wording scan;
- branch/head wording;
- status snapshot integrity;
- generic vs project-specific separation.

The checklist should function as a closure gate for the orchestration run, not as a new delegated protocol.

## 6. Human Gates

### HUMAN_GATE_1: Confirm landing location

Decision needed:

- Confirm the v2 governance additions land in `skills/workflow-bootstrap/orchestration_snippets.md`.
- Confirm whether `skills/workflow-bootstrap/examples/invocation_examples.md` remains out of scope or is separately approved for a short example update.

Recommended decision: land only in `skills/workflow-bootstrap/orchestration_snippets.md` for the first v2 governance pass.

### HUMAN_GATE_2: Confirm v2 additions stay in workflow-bootstrap orchestration layer

Decision needed:

- Confirm the additions remain thin orchestration guidance.
- Confirm the additions do not become a schema validator, third protocol, or delegated skill replacement.
- Confirm the additions do not require real status or handoff refreshes during snippet authoring.

Recommended decision: approve workflow-bootstrap-only orchestration-layer changes.

### HUMAN_GATE_3: Confirm no delegated skill protocol rewrite

Decision needed:

- Confirm no changes to `skills/update-project-status/SKILL.md`.
- Confirm no changes to `skills/chatgpt-handoff-pilot/SKILL.md`.
- Confirm no copied delegated protocol bodies in `orchestration_snippets.md`.

Recommended decision: preserve delegated skill boundaries exactly.

### HUMAN_GATE_4: Approve implementation

Implementation may proceed only after a later prompt includes the exact approval text:

```text
HUMAN_APPROVAL: PROCEED_TO_IMPLEMENTATION
```

Without that exact approval text, stop after planning and do not update the orchestration snippet.

## 7. Later Implementation Plan

After explicit implementation approval:

1. Read canonical files before editing:
   - `AGENTS.md`
   - `skills/workflow-bootstrap/SKILL.md`
   - `skills/workflow-bootstrap/orchestration_snippets.md`
   - `skills/update-project-status/SKILL.md`
   - `skills/chatgpt-handoff-pilot/SKILL.md`
   - this task package
2. Locate the existing `Post-Dev Dual Refresh Orchestration` section and edit it section-aware.
3. Update `skills/workflow-bootstrap/orchestration_snippets.md` only, unless a separate gate approves the optional example file.
4. Preserve delegated skill boundaries:
   - `update-project-status` owns status refresh behavior;
   - `chatgpt-handoff-pilot` owns handoff refresh and execution report behavior;
   - `workflow-bootstrap` owns the invocation shell and role-boundary glue.
5. Do not duplicate delegated protocols or introduce a third protocol.
6. Add the v2 governance blocks in a concise reusable form.
7. Add or refine final reviewer closure checks for the v2 gates.
8. Create an execution report after implementation if separately authorized by the implementation task scope.
9. Run text searches and diff checks to verify scope, wording, and boundary compliance.
10. Report explicitly what was changed and what was not implemented.

## 8. Validation Plan For Later Implementation

Minimum checks for the later implementation:

```powershell
git diff --name-only
rg -n "payload_persistence_decision|validation_provenance|stale_wording_scan|Branch/head|Final reviewer" skills/workflow-bootstrap/orchestration_snippets.md
rg -n "new skill|replacement protocol|third protocol|rewrite update-project-status|rewrite chatgpt-handoff-pilot" skills/workflow-bootstrap/orchestration_snippets.md tasks/post_dev_dual_refresh_v2_governance_gates_task_package.md
```

Additional recommended checks:

```powershell
git diff --check
rg -n "<maintainer-supplied-downstream-project-term>|<maintainer-supplied-domain-term>|<specific-pr-or-commit-pattern>" skills/workflow-bootstrap/orchestration_snippets.md tasks/post_dev_dual_refresh_v2_governance_gates_task_package.md
rg -n "docs/HANDOFF.md|docs/status|docs/status_updates.log|SKILLS_INDEX.md|skills_index.json|\.agents/|\.github/" --glob '!*tasks/post_dev_dual_refresh_v2_governance_gates_task_package.md' --glob '!skills/workflow-bootstrap/orchestration_snippets.md'
```

Interpretation notes:

- The boundary search may return intentional non-goal language; review matches for accidental protocol replacement wording.
- The downstream-specific search should return no embedded project facts in reusable template content.
- `git diff --name-only` should show only approved files for the later implementation.

## 9. Stop Conditions

Stop before or during later implementation if:

- expected files cannot be located;
- existing snippet structure is incompatible with a section-aware update;
- planning or implementation requires modifying delegated skills;
- adapter updates appear necessary;
- task scope would expand beyond v2 governance gates;
- project-specific downstream facts would need to be embedded;
- the change would create a new skill, schema validator, replacement protocol, or third protocol;
- the change would require real status refresh or real handoff refresh;
- generated metadata or indexes appear to need updates;
- forbidden files would need to be modified.

## 10. Output Requirements

After writing this task package, output:

- task package path: `tasks/post_dev_dual_refresh_v2_governance_gates_task_package.md`;
- files inspected;
- exact proposed later target files:
  - primary: `skills/workflow-bootstrap/orchestration_snippets.md`;
  - optional only if later approved: `skills/workflow-bootstrap/examples/invocation_examples.md`;
- human gate decisions needed:
  - `HUMAN_GATE_1`: confirm landing location;
  - `HUMAN_GATE_2`: confirm v2 additions stay in workflow-bootstrap orchestration layer;
  - `HUMAN_GATE_3`: confirm no delegated skill protocol rewrite;
  - `HUMAN_GATE_4`: approve implementation only with `HUMAN_APPROVAL: PROCEED_TO_IMPLEMENTATION`;
- implementation not performed;
- changed files;
- suggested commit message.

Suggested commit message:

```text
docs(workflow-bootstrap): plan dual refresh v2 governance gates
```

Suggested PR title:

```text
docs(workflow-bootstrap): plan dual refresh v2 governance gates
```

## 11. Planning-Run Completion Checklist

Before closing this planning run, verify:

1. Only one task package was added.
2. `skills/workflow-bootstrap/orchestration_snippets.md` was not modified.
3. Branch/head provenance is included in the v2 plan.
4. No downstream project-specific facts were copied into this generic template plan.
