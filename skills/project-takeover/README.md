# Project Takeover Skill

## Purpose

`project-takeover` creates onboarding outputs for a new developer or AI maintainer. It can reuse bundled audit scripts or point at external tools through config or CLI flags.

## Generated Outputs

By default the script writes these markdown files into `docs/takeover`:
- `project_takeover_report.md`
- `project_onboarding_summary.md`
- `welcome_email.md`

## Running The Script

```powershell
python .codex/skills/project-takeover/scripts/project_takeover.py --root <project-root>
```

```powershell
python .codex/skills/project-takeover/scripts/project_takeover.py --root <project-root> --dry-run
```

Optional flags:
- `--config <path>`
- `--report-dir <path>`
- `--shared-dir <path>`
- `--apply-safe-fixes`
- `--install`
- `--dry-run`
- `--structure-script <path>`
- `--docs-script <path>`

## Prompt Template

Use this template when you want Codex to apply the skill for a repository:

```text
Use the `project-takeover` skill on this repository.

Goal:
- Prepare a takeover/onboarding packet for the project.

Target project root:
- <project-root>

What to focus on:
- summarize the most important docs
- identify likely task sources
- check environment readiness
- generate onboarding outputs

Optional constraints:
- config: <path-or-none>
- report dir: <path-or-default>
- shared dir: <path-or-none>
- use dry run: <yes-or-no>
- apply safe fixes: <yes-or-no>
- run install commands: <yes-or-no>
- external structure script: <path-or-none>
- external docs script: <path-or-none>

Expected result:
- explain what you found
- generate the takeover artifacts
- call out risks, missing docs, and follow-up actions
```

## Configuration

Project-local overrides can live at `.codex/skill-config/project-takeover.json`.

Key settings:
- `doc_candidate_globs`
- `priority_task_globs`
- `safe_directories`
- `install_commands`
- `infer_install_commands`
- `support_scripts`
- `welcome_language`

## Environment Handling

The script performs soft-fail environment checks.
- Python and pip are checked via `sys.executable`.
- Conda is checked only if it is discoverable on `PATH`.
- Missing tools are reported in the generated report instead of crashing the run.

## Side Effects

The script writes outputs unless `--dry-run` is used.

Additional side effects are opt-in:
- `--apply-safe-fixes` can create directories
- `--install` can run package installation commands
- `--shared-dir` copies generated markdown files to another local directory

## Cross-Project Notes

- This skill no longer assumes filenames such as `docs/HANDOFF.md` or `docs/TASKBOARD.md`.
- Use glob patterns to adapt document discovery to each repository.
- Use `support_scripts` or CLI overrides when the project already has a preferred audit toolchain.
