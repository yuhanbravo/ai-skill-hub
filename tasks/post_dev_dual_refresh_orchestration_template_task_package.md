# Task Package: Post-Dev Dual Refresh Orchestration Template

## 1. Task Objective

Add a reusable "Post-Dev Dual Refresh Orchestration Template" to the `workflow-bootstrap` orchestration layer.

The template chains two existing delegated skills:

1. Step 1: `update-project-status`
2. Step 2: `chatgpt-handoff-pilot`

The template must preserve both delegated skills' boundaries. It is an invocation template / orchestration snippet only. It is not a new skill, not a replacement protocol, and not an execution of a real project status or handoff refresh.

## 2. Source Draft Status

The upstream prompt references a cloud draft placeholder:

```text
[PASTE CLOUD DRAFT HERE]
```

No separate draft body was included in the local task input. Therefore this task package treats the current request's explicit structure, gates, and boundaries as the usable source draft. Any implementation must preserve this assumption in the execution report.

## 3. Canonical Context Read

Minimum canonical and relevant files inspected before drafting:

- `skills/workflow-bootstrap/SKILL.md`
- `skills/workflow-bootstrap/orchestration_snippets.md`
- `skills/update-project-status/SKILL.md`
- `skills/chatgpt-handoff-pilot/SKILL.md`
- `tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_task_package.md`
- `docs/governance/adapter_governance.md`
- `docs/governance/COMMIT_CONVENTION.md`
- `docs/governance/documentation_status_coordination.md`
- `skills/workflow-bootstrap/examples/invocation_examples.md`
- `skills/update-project-status/examples/invocation_examples.md`
- `skills/chatgpt-handoff-pilot/examples/invocation_examples.md`

Observed repository conventions:

- `workflow-bootstrap` owns workflow shell, role boundaries, and orchestration glue.
- `chatgpt-handoff-pilot` owns task package, bounded execution, handoff maintenance, and execution report protocol.
- `update-project-status` owns project status refresh from Git/workspace/task signals and must keep dry-run/write/sync behavior explicit.
- `tasks/` is an accepted trace path for task packages and execution reports.
- Adapter layers under `.agents/skills/**` and `.github/skills/**` are thin wrappers and must not be modified unless explicitly approved.

## 4. Non-Goals

- Do not create a new skill.
- Do not rewrite `update-project-status` protocol.
- Do not rewrite `chatgpt-handoff-pilot` protocol.
- Do not turn the snippet into a third rule system.
- Do not execute a real status refresh.
- Do not execute a real handoff refresh.
- Do not update a real project `docs/HANDOFF.md` while authoring this template.
- Do not install git hooks.
- Do not commit.
- Do not push.
- Do not sync or modify adapter layers unless separately justified and approved.

## 5. Proposed File Changes

### Required Files

- `tasks/post_dev_dual_refresh_orchestration_template_task_package.md`
  - This task package.

### Implementation Target After Human Approval

- `skills/workflow-bootstrap/orchestration_snippets.md`
  - Preferred landing location.
  - Add one new section by appending or inserting section-aware near existing orchestration snippets.
  - Preserve the current Chinese-first active canonical style with retained English terms.

### Optional Files Only If HUMAN_GATE_1 Approves

- `skills/workflow-bootstrap/examples/invocation_examples.md`
- `skills/update-project-status/examples/invocation_examples.md`
- `skills/chatgpt-handoff-pilot/examples/invocation_examples.md`

Optional example files should only receive short invocation examples. They must not duplicate the full orchestration snippet or delegated skill protocols.

### Forbidden Or Gate-Required Files

Do not modify these files in this run unless a later human gate explicitly approves the exact change:

- `skills/update-project-status/SKILL.md`
- `skills/chatgpt-handoff-pilot/SKILL.md`
- `skills/workflow-bootstrap/SKILL.md`
- `README.md`
- `SKILLS_INDEX.md`
- `skills_index.json`
- `.agents/skills/**`
- `.github/skills/**`
- `docs/HANDOFF.md`
- `docs/status/**`
- `docs/status_updates.log`
- `.git/hooks/**`

## 6. Proposed Snippet Structure

The implementation snippet should include the following sections:

- Template name: `Post-Dev Dual Refresh Orchestration`
- Template type: `orchestration snippet / invocation template`
- Owner layer: `workflow-bootstrap`
- Delegated skills:
  - `update-project-status`
  - `chatgpt-handoff-pilot`
- Input parameters:
  - repository path
  - status source mode: `git | workspace | hybrid | unknown`
  - refresh mode: `dry-run | write`
  - status output paths, if known
  - sync authorization: `yes | no`
  - handoff target path, if a real handoff refresh is later authorized
  - evidence pointers
  - assumptions
- Side-effect matrix:
  - dry-run status refresh: observe / preview only
  - write-mode status refresh: may write status snapshot/log within delegated authorization
  - sync: opt-in only
  - handoff refresh: only if separately authorized by `chatgpt-handoff-pilot` task scope
  - template authoring: no real status or handoff writes
- Step 0: preflight and boundary confirmation
- Step 1: `update-project-status` invocation
- Step 1 -> Step 2 structured handoff input block
- Step 2: `chatgpt-handoff-pilot` invocation
- Step 3: merged round receipt
- Stop conditions
- Output requirements

The snippet must state that it is an invocation template. It must not replace either delegated skill or copy either delegated protocol body.

## 7. Required Structured Handoff Block

The implementation snippet must include a YAML-style block shaped like this:

```yaml
handoff_input:
  status_headline:
  key_progress:
    -
  open_risks_blockers:
    -
  recommended_next_steps:
    -
  evidence_pointers:
    files:
      -
    commits:
      -
  source_mode: git | workspace | hybrid | unknown
  writes_performed:
    -
  sync_performed: yes | no
  freshness_note:
  assumptions:
    -
```

The block is a transfer payload from status-refresh output into handoff-refresh input. It is not a new schema, validator, or third protocol.

## 8. Human Gates

### HUMAN_GATE_1 - Landing Location Gate

Decision needed:

- Option A: land the snippet only in `skills/workflow-bootstrap/orchestration_snippets.md`.
- Option B: land the snippet in `skills/workflow-bootstrap/orchestration_snippets.md` and add short examples to one or more approved example files.

Recommended decision: Option A. The existing target file already owns minimal orchestration snippets, and a single-file landing keeps the change thin.

### HUMAN_GATE_2 - Boundary Gate

Decision needed:

- Confirm this remains a thin orchestration snippet.
- Confirm no delegated skill protocol body is copied or rewritten.
- Confirm no real `docs/HANDOFF.md` refresh is performed.
- Confirm no real status refresh is performed while authoring this template.
- Confirm no adapter layers are touched.

Recommended decision: approve these boundaries exactly as written.

### HUMAN_GATE_3 - Implementation Gate

Implementation may proceed only after explicit human approval containing:

```text
HUMAN_APPROVAL: PROCEED_TO_IMPLEMENTATION
```

If approval is not present, stop after task package creation.

### HUMAN_GATE_4 - Post-Implementation Review Gate

After implementation, a human reviews the diff before any commit.

No commit or push is authorized in this run.

## 9. Implementation Guidance After Approval

If `HUMAN_APPROVAL: PROCEED_TO_IMPLEMENTATION` is present in a later prompt:

1. Re-read this task package and `skills/workflow-bootstrap/orchestration_snippets.md`.
2. Add one section named consistently with the existing file style, such as:
   - `## Post-Dev Dual Refresh Orchestration`
3. Use section-aware editing.
4. Preserve existing heading style, wording density, boundary language, and active canonical policy.
5. Reference delegated skills by name and responsibility.
6. Do not copy full delegated protocol rules.
7. Create an execution report at:
   - `tasks/post_dev_dual_refresh_orchestration_template_execution_report.md`

## 10. Validation Plan

Minimum checks:

- Read the resulting task package and implementation section to confirm markdown structure.
- Search for accidental delegated protocol duplication.
- Confirm no forbidden files changed.
- Run `git diff --name-only`.
- Optionally run local markdown or repository checks only if already standard, safe, and non-invasive.

Suggested search checks:

```powershell
rg -n "Post-Dev Dual Refresh|handoff_input|third rule system|new skill" skills\workflow-bootstrap\orchestration_snippets.md tasks\post_dev_dual_refresh_orchestration_template_task_package.md
rg -n "install_post_commit_hook|docs/HANDOFF.md" skills\workflow-bootstrap\orchestration_snippets.md
git diff --name-only
```

## 11. Stop Conditions

Stop and report before implementation if any of these occur:

- Cannot locate expected workflow-bootstrap files.
- Existing orchestration snippets have a different canonical structure than observed in Phase A.
- Implementing the snippet requires changing delegated skill protocols.
- Updating the target file would require a full rewrite.
- Draft ambiguity creates risk of changing actual status or handoff docs.
- Any forbidden file change appears necessary.
- Adapter modification appears necessary.
- Human gate approval is absent.

## 12. Output Requirements For This Phase

After creating this task package, stop and output:

- task package path
- recommended landing location
- files inspected
- proposed files to change
- exact HUMAN_GATE_1 / HUMAN_GATE_2 decision needed

Do not implement the orchestration snippet unless a later prompt explicitly includes:

```text
HUMAN_APPROVAL: PROCEED_TO_IMPLEMENTATION
```
