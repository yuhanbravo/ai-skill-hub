# Project Takeover

## What is this

`project-takeover` 是一个项目接管型 skill，用来为陌生仓库生成最小可用的 takeover packet，帮助新维护者或 AI 代理快速进入项目。

## When to use

适合在首次接手仓库、准备 onboarding 材料、生成 handoff 输出，或者需要快速盘点环境、文档和任务来源时使用；如果目标只是更新项目进度，应优先考虑 `update-project-status`。

## Quick Start

```text
Use the `project-takeover` skill on this repository and prepare a takeover packet.
Project root: <project-root>

# optional
# Config path: <path-or-none>
# Dry run: yes/no
```

详细执行方式见 [SKILL.md](SKILL.md)。

## Detailed Guidance Moved From SKILL.md

The sections below were moved out of `SKILL.md` during the semantic split so the README can carry explanation-oriented material while `SKILL.md` stays execution-focused.

## 1. 背景（Problem Context）

这个 skill 用来解决项目接管时最常见的一类问题：新维护者或 AI 代理第一次进入仓库时，往往不知道环境是否可用、文档在哪里、任务从哪里来、哪些信息值得优先看，也不知道该如何快速整理出一份可继续协作的接手材料。

`project-takeover` 的目标不是替代项目本身的治理文档，而是把“首次进入一个仓库并生成接手资料”的过程阶段化、可执行化。它保留项目差异，不强依赖固定文件名，通过配置、脚本和文档扫描来生成 takeover packet，帮助后续的 onboarding、handoff 和维护接手。

它在 skill-hub 中更偏向 `project` 型 skill：重点不是单次命令，而是围绕项目接管过程组织输入、判断、整理和输出。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要为一个陌生仓库准备接手资料、onboarding 材料或 handoff 输出
- 新开发者、新维护者或 AI 代理第一次进入项目，需要快速建立项目理解
- 希望同时检查环境 readiness、结构审计、文档概览和任务来源
- 希望生成可落盘、可共享的 takeover report、onboarding summary 和欢迎说明
- 希望复用项目本地配置或外部审计脚本，而不是把规则硬编码进共享 skill

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用这个 skill：

- 任务只是回答单个代码问题，而不是接管整个仓库
- 项目已经有更成熟且固定的接管流程，并且不需要额外 takeover packet
- 当前目标是持续状态更新或阶段进度同步，那更接近 `update-project-status`
- 仓库上下文极少，无法读取关键文档、配置或目录结构
- 当前不允许生成任何输出文件或执行任何检查动作

## 8. 风险（Risks）

- 如果把这个 skill 当成普通仓库扫描器使用，可能忽略其“生成接手材料”的核心目标
- 如果文档候选模式或任务来源模式配置不当，输出会遗漏关键上下文
- 如果直接运行 `--install` 或 `--apply-safe-fixes` 而未确认范围，可能带来不必要副作用
- 如果把扫描结果直接当成完整事实，而不区分已确认与待验证信息，接手报告容易误导新维护者
- 如果 README 与 SKILL 职责不分，调用方可能只看到命令而不了解完整阶段流程

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准接管调用

```text
请使用 `project-takeover` 处理以下仓库接管任务。

背景：
- 这是一个需要接手或 onboarding 的项目

目标：
- 生成 takeover packet，并帮助新维护者快速理解仓库

范围：
- 扫描项目环境、关键文档、任务来源和可用审计脚本
- 整理接手所需的结构化输出

约束：
- 保留项目本地配置优先级
- 不做未授权的高风险副作用

预期输出：
- 按 `scan -> understand -> structure -> output` 推进
- `project_takeover_report.md`
- `project_onboarding_summary.md`
- `welcome_email.md`
- 风险与下一步建议
```

### 模板 2：严格阶段化执行模板

```text
请按 `project-takeover` 的方法执行本次任务。

要求：
- 先总结你对项目接管目标的理解
- 按 `scan -> understand -> structure -> output` 四个阶段推进
- 明确当前使用的配置、脚本和可选参数
- 输出结果、风险和待确认项

任务内容：
- Project root: <project-root>
- Primary goal: <takeover | onboarding | handoff prep>
- Config path: <path-or-none>
- Report dir: <path-or-default>
- Shared dir: <path-or-none>
- Dry run: <yes-or-no>
- Apply safe fixes: <yes-or-no>
- Install: <yes-or-no>
- Structure script override: <path-or-none>
- Docs script override: <path-or-none>
```

## 10. 总结（Summary）

`project-takeover` 最适合解决“第一次进入一个仓库，如何快速建立接手理解并生成可交付的 onboarding 材料”这一类问题。它的价值不只是扫描，而是把扫描结果组织成真正可用于交接的结构化产物。

使用时最重要的边界有两条：第一，优先尊重项目本地配置和本地工具链；第二，把整个过程按 `scan → understand → structure → output` 推进，而不是跳过理解阶段直接生成报告。

## Supporting Assets

- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)

## 文档语言与 SSOT 说明（2026-05-11）

- 本文档面向开发人员（developer-facing），统一采用**中文为主、英文术语辅助**（例如：`Pattern`、`Invocation`、`Constraints`、`read_only`、`write_files`）。
- 本仓库的 **SSOT（Single Source of Truth）** 仍是当前 skill 目录下的 `SKILL.md`；`README.md` 仅提供可读性说明与快速上手，不得与 `SKILL.md` 发生规则分叉。
- 若 `README.md` 与 `SKILL.md` 出现冲突，必须以 `SKILL.md` 为准，并在后续修订中消除偏差。
- 本节为当前状态声明，更新日期：**2026-05-11**。

