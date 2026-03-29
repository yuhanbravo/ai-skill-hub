# SkillHub Status Template

Use this template when the repository is primarily a skill-hub project rather than a product or business application.

This template is intended for repositories whose main outputs are skills, adapters, invocation contracts, governance assets, indexes, tests, and automation utilities.

## Current SkillHub Status

- Summarize the repository as a skill engineering system.
- State the current phase, major direction of evolution, and the most important status signals.
- Avoid feature-shipping language from ordinary application projects.

## Skill Coverage

- Describe what skill families or capability areas are currently represented.
- Note whether the iteration expanded coverage, standardized existing skills, or reorganized canonical assets.
- Focus on repository-level coverage rather than end-user product features.

## Invocation Readiness

- Summarize whether skills are directly callable by AI tools.
- Mention invocation contracts, examples, metadata completeness, routing readiness, or orchestration readiness when relevant.
- Distinguish between “discoverable”, “callable”, and “reliably invokable”.

## Adapter / Discovery Coverage

- Describe how the repository is exposed to different AI discovery layers.
- Note the existence or completeness of `.agents/`, `.github/`, flat indexes, machine-readable indexes, or other adapter surfaces.
- Focus on discoverability and consistency between adapter layers and canonical sources.

## Governance & Testing Status

- Summarize structure checks, governance rules, validation scripts, or quality-control mechanisms.
- Mention whether governance is manual, script-assisted, or CI-backed.
- Call out gaps in validation coverage or drift protection.

## Automation Readiness

- Describe generators, sync tools, routers, pipelines, metadata builders, or automation scripts that make the skill-hub maintainable.
- Focus on whether automation is usable, partial, or fully trusted.
- Highlight if the current iteration moved work from manual to repeatable.

## Open Gaps

- Capture unresolved governance, discoverability, quality, or automation issues.
- Prefer repository risks and structural gaps over product backlog language.
- Make it easy for the next maintainer or AI agent to see what is still weak.

## Next Recommended Moves

- Provide the next structural or governance-oriented actions.
- Prefer actions that improve reuse, consistency, automation, testing, or cross-AI interoperability.
- Keep the recommendations repository-oriented rather than feature-oriented.
