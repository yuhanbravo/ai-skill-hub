---
name: project-takeover
description: Prepare a repository for a new developer or AI maintainer by checking environment readiness, running configurable structure and documentation audits, summarizing key docs and task sources, and generating onboarding artifacts. Use when Codex needs to support project handoff, new-maintainer onboarding, repository takeover, or requests like "prepare a handoff", "generate onboarding docs", or "take over this repo".
---

# Project Takeover

Use this skill to create a portable takeover packet for many kinds of repositories without assuming this repo's document names or environment tools.

## Trigger Keywords

- project takeover
- onboarding pack
- handoff prep
- repository takeover
- new maintainer onboarding
- generate onboarding docs
- prepare handoff

## Side Effects

- Default mode writes three markdown outputs to the configured report directory.
- `--shared-dir` copies those markdown files to another local directory.
- `--apply-safe-fixes` can create low-risk top-level directories.
- `--install` can run configured or inferred local install commands.
- `--dry-run` previews actions without writing files.

## Workflow

1. Resolve project-local config and optional support scripts.
2. Check environment readiness with soft-fail detection for Python, pip, and conda.
3. Run structure and documentation audits if those scripts are available.
4. Summarize configured documentation and task sources.
5. Generate takeover outputs and optionally sync them to a shared local directory.

## Commands

```powershell
python .codex/skills/project-takeover/scripts/project_takeover.py --root <project-root>
```

```powershell
conda run -n <env> python .codex/skills/project-takeover/scripts/project_takeover.py --root <project-root> --dry-run
```

Useful flags:

- `--config <path>` for a project-specific takeover config
- `--structure-script <path>` and `--docs-script <path>` to point at external audit tools
- `--report-dir <path>` to override output location
- `--shared-dir <path>` for local shared-copy sync
- `--apply-safe-fixes`
- `--install`
- `--dry-run`

## Prompt Template

Use or adapt this request when invoking the skill:

```text
Use the `project-takeover` skill for this repository and prepare a takeover packet.

Project root: <project-root>
Primary goal: <new-maintainer onboarding | repository handoff | takeover audit>

Please:
- inspect the repo and relevant docs
- check environment readiness
- run the available structure/documentation audits if appropriate
- generate the takeover outputs
- summarize the highest-priority risks and next steps

Options:
- config path: <path-or-none>
- report dir: <path-or-default>
- shared dir: <path-or-none>
- dry run: <yes-or-no>
- apply safe fixes: <yes-or-no>
- install: <yes-or-no>
- structure script override: <path-or-none>
- docs script override: <path-or-none>
```

## Config Notes

- Default config lives in `references/default_takeover_config.json`.
- Projects can override it with `.codex/skill-config/project-takeover.json` or `--config`.
- `doc_candidate_globs` controls which docs are summarized.
- `priority_task_globs` controls which task files are scanned.
- `support_scripts` can point at non-bundled structure or documentation audit scripts.

## Safety Rules

- Treat `--apply-safe-fixes` as limited to low-risk directory creation only.
- Review generated onboarding material before sharing it broadly.
- Prefer config changes over hard-coding repository-specific filenames into the shared skill.
