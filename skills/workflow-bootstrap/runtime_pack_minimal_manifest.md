# Runtime Pack Minimal Manifest

Status: project-side thin runtime surface guidance. This document describes a minimal, optional, project-aware runtime-pack shape; it does not implement project-side files in this hub.

`workflow-bootstrap` uses this manifest to explain how a project may expose thin runtime surfaces that route humans and agents back to canonical guidance. It is not a second rulebook, not a copy layer for canonical skills, not a new execution protocol, and not a CI / validator / automation mechanism.

## Canonical Ownership

- `skills/` remains the canonical source of truth.
- `workflow-bootstrap` defines the workflow shell, role split, runtime profile, review tier guidance, and runtime pack manifest guidance.
- `chatgpt-handoff-pilot` owns task package, bounded execution, and execution report protocols.
- Project-side runtime surfaces only help readers find and apply canonical guidance in a local repository context.

## Thin Entry Principles

Project-side runtime surfaces should stay thin:

- Discover: make the relevant entry point easy to find.
- Route: point to the right canonical skill, task artifact, or project-local evidence path.
- Reference: summarize only the smallest boundary needed to avoid misrouting.

They should not:

- copy canonical skill bodies;
- create a parallel rule set;
- turn one project's local facts into global workflow rules;
- redefine task package, bounded execution, or execution report protocols;
- imply that this hub has created the project-side files listed below.

## Minimal Candidate Surfaces

The following surfaces are project-side runtime pack candidates only. Listing them here does not authorize creating these files in the current `ai-skill-hub` repository.

### `AGENTS.md`

- 中文定位：仓库级薄入口和项目侧 runtime master entry。
- 主要用途：说明本项目的 local constraints, authorized workflow entry points, and where canonical guidance lives.
- 应回指哪些 canonical guidance：`skills/workflow-bootstrap/SKILL.md`, `skills/workflow-bootstrap/role_split_and_integration.md`, and any project-relevant canonical skills; when bounded execution is involved, point to `skills/chatgpt-handoff-pilot/SKILL.md`.
- 不应包含什么：不复制 full skill text，不重定义 role chain，不重写 task package / execution report protocol，不把 project-local preferences 写成 global rules.
- Git-first / non-git / low-git 适用边界：Git-first projects may pair this thin entry with branch / commit / PR review conventions; non-git / low-git projects may also point to project-local task artifacts as the main evidence line.

### `.github/copilot-instructions.md`

- 中文定位：Copilot-specific thin adapter。
- 主要用途：给 Copilot 提供高频、短格式的 local routing hints while preserving canonical ownership elsewhere.
- 应回指哪些 canonical guidance：`AGENTS.md` when present, `skills/workflow-bootstrap/SKILL.md`, and `skills/chatgpt-handoff-pilot/SKILL.md` for handoff protocol ownership.
- 不应包含什么：不复制 `AGENTS.md` 或 canonical skill 正文，不把 Copilot-specific behavior 写成 tool-agnostic canonical rule，不创建独立执行协议。
- Git-first / non-git / low-git 适用边界：Git-first projects can mention PR-style review expectations if local policy requires it; non-git / low-git projects can point to the preferred project-local evidence path without making it universal.

### `.github/copilot-instructions.zh-CN.md`

- 中文定位：中文 Copilot thin adapter。
- 主要用途：为中文协作环境提供同等薄入口，降低语言切换造成的 routing loss.
- 应回指哪些 canonical guidance：same canonical guidance as `.github/copilot-instructions.md`, plus any local language-specific routing note maintained by the project.
- 不应包含什么：不成为英文 adapter 的扩写规则库，不复制 canonical skill 正文，不引入和英文入口不一致的 protocol ownership.
- Git-first / non-git / low-git 适用边界：适用性取决于项目语言需求；Git evidence and non-git evidence rules remain project-aware, not mandatory for all repositories.

### `tasks/README.md`

- 中文定位：project-local task artifact index。
- 主要用途：在 task artifacts 累积后帮助读者找到 active task packages, execution reports, and naming conventions.
- 应回指哪些 canonical guidance：`skills/chatgpt-handoff-pilot/SKILL.md` for task package / execution report protocol and `skills/workflow-bootstrap/non_git_runtime_profile.md` for non-git / low-git evidence placement.
- 不应包含什么：不替代 task package 或 execution report，不定义新的 report schema，不把 `tasks/` 写成所有项目 mandatory global path.
- Git-first / non-git / low-git 适用边界：Optional in Git-first projects when Git and PR history are sufficient; more useful in non-git / low-git projects where task artifacts are the preferred project-local evidence path.

### `tasks/<task-package>.md`

- 中文定位：单轮 bounded work 的 task package artifact。
- 主要用途：记录 scope, authorized files, out-of-scope items, acceptance criteria, and validation expectations before implementation.
- 应回指哪些 canonical guidance：`skills/chatgpt-handoff-pilot/SKILL.md` for protocol shape and `skills/workflow-bootstrap/role_split_and_integration.md` for role-stage ownership.
- 不应包含什么：不作为 canonical skill source，不授权未列入范围的 project-side runtime file creation，不把 draft intent 写成 implementation permission before review.
- Git-first / non-git / low-git 适用边界：Git-first projects may pair task packages with issue / branch / PR context; non-git / low-git projects may rely on the task package as the main pre-execution boundary.

### `tasks/<execution-report>.md`

- 中文定位：单轮 bounded execution 的 evidence report。
- 主要用途：记录 changed files, skipped work, validation performed, risks, assumptions, and follow-up recommendations after implementation.
- 应回指哪些 canonical guidance：`skills/chatgpt-handoff-pilot/SKILL.md` for execution report protocol and the reviewed task package for scope.
- 不应包含什么：不补写新的 rules to justify out-of-scope changes，不替代 final review，不成为 canonical source of truth.
- Git-first / non-git / low-git 适用边界：Git-first projects may use reports alongside commits and PR review; non-git / low-git projects may treat reports as the primary per-task evidence trail.

## Git-First And Non-Git Boundaries

Runtime pack guidance is project-aware, not one-size-fits-all.

- Git-first projects can combine thin runtime surfaces with branch names, commits, diffs, and PR-style review.
- Non-git / low-git projects may depend more heavily on task package / execution report pairing.
- `tasks/` may serve as the preferred project-local evidence path in non-git / low-git work, but it is not a mandatory global path for all projects.
- The runtime pack should describe the smallest useful local surface combination instead of forcing every repository to adopt the same files.

## Deferred Future Surfaces

The following are deferred or out-of-scope candidates for future work. They are not part of the Phase 3 minimal manifest and should not be treated as implementation targets here:

- `.github/instructions/`
- `.github/agents/`
- tool adapters
- validators / automation / CI
- Phase 4 multi-project pilot
- Phase 5 tool adapter candidates
- optional project-local skill payloads and adapters

If future work revisits these surfaces, it should use a separately reviewed task package and preserve the same ownership boundary: `skills/` remains canonical, `workflow-bootstrap` explains the workflow shell and runtime-pack guidance, and `chatgpt-handoff-pilot` owns bounded execution protocols.
