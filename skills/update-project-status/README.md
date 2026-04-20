# Update Project Status

## What is this

`update-project-status` 是一个项目状态更新型 skill，用来把 **Git-first 信号**、workspace 信号与可用任务来源整理为状态文档、状态日志和可选同步结果。

它默认面向普通项目状态更新，但也支持 `skill-hub` 这种“以 skills、adapters、indexes、tests 和 automation 为主要产物”的仓库形态。

## When to use

适合在需要刷新项目状态、整理近期变更、准备阶段汇报或 handoff 状态摘要时使用；如果目标是首次接管项目，应优先考虑 `project-takeover`。

支持三种最小模式（兼容 Git-first 默认行为）：

- `git`：优先使用 Git 历史（默认）
- `workspace`：在无 Git 或 Git 不可用时，基于 workspace/task signals 刷新当前状态
- `hybrid`：同时吸收 Git + workspace/task signals

> 本 skill 当前仅提供 **SSOT-lite**（如 `primary_status_doc`、`workspace_signal_paths`、`truth_precedence`），不是 full SSOT governance engine。

当目标仓库本身是一个 `skill-hub project`，并且你更关心 `skill coverage`、`invocation readiness`、`adapter/discovery coverage`、`governance readiness` 和 `automation readiness` 时，应使用 `template_type=skillhub`。

## Quick Start

```text
Use the `update-project-status` skill for this repository and refresh the status report.
Project root: <project-root>

# optional
# Config path: <path-or-none>
# Dry run: yes/no
```

## SkillHub Template

如果目标仓库是 skill-hub，可在配置中切换：

```json
{
  "template_type": "skillhub"
}
```

对应模板结构位于 [templates/skillhub_status_template.md](templates/skillhub_status_template.md)。

切换后，状态输出会采用 skill-hub 口径，而不会继续使用普通项目的 `Recent Features / Fixed Bugs / Upcoming Tasks` 主视角。

详细阶段化执行方式见 [SKILL.md](SKILL.md)。

## Detailed Guidance Moved From SKILL.md

The sections below were moved out of `SKILL.md` during the semantic split so the README can carry explanation-oriented material while `SKILL.md` stays execution-focused.

## 1. 背景（Problem Context）

这个 skill 用来解决项目状态维护中的一个常见问题：仓库里有提交历史，也可能有任务板、Jira 导出、Trello 导出或命令行来源，但这些信息通常是分散的。每次要做周报、阶段总结、handoff 状态说明或对外发布时，都要重复读取提交、筛任务、整理重点，再把结果写进状态文档。

`update-project-status` 的作用不是发明新的状态体系，而是把“收集近期变化并生成状态输出”的流程稳定下来。它保留原有 CLI、默认输出和同步机制，通过配置、Git 历史和外部任务源生成项目状态文档、状态日志，以及按配置触发的同步结果。

它在 skill-hub 中更适合被视为 `project` 型 skill，因为重点不是单个命令本身，而是围绕项目状态更新这一过程组织输入、判断、结构化输出和发布动作。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要基于近期 Git 提交生成或刷新项目状态报告（Git-first）
- 需要在无 Git 项目中基于 workspace/task signals 刷新“当前状态”
- 希望把仓库提交与任务来源信息合并成统一状态文档
- 需要准备阶段总结、handoff 状态说明或对外同步的项目更新
- 需要按配置把状态输出同步到本地副本、命令目标或远程文档目标
- 希望在不改变原始项目结构的前提下，持续生成可追踪的状态文档和日志

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用这个 skill：

- 当前目标是首次接管仓库，而不是更新持续状态，那更接近 `project-takeover`
- 项目没有可用的 Git 历史，且没有任何 workspace/task signals，无法形成有效状态摘要
- 任务只需要解释某个提交或某个文件变化，而不是输出完整状态文档
- 当前不允许写入状态文件、日志文件或执行同步动作
- 团队已有强制的本地状态发布流程，且不需要额外的共享 skill 封装

## 8. 风险（Risks）

- 如果把提交分类结果当成精确事实，而忽略其关键字启发式本质，状态总结可能产生偏差
- 如果外部任务源过旧、缺失或格式不一致，状态报告可能遗漏真实进展或待办
- 如果未区分“本地写入”和“外部同步”，可能在未审阅内容前就发布到共享目标
- 如果忽略非侵入原则，可能把状态刷新误当成允许任意修改项目的操作
- 如果只看 README 而不看完整 SKILL，调用方可能低估 hook 安装和同步动作的边界

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准状态刷新模板

```text
请使用 `update-project-status` 处理以下任务。

背景：
- 需要根据近期 Git 提交和可用任务来源刷新项目状态

目标：
- 生成或更新状态文档，并整理关键进展、风险和待办

范围：
- 读取最近提交
- 合并可用任务源
- 生成状态 markdown 与状态日志
- 如已授权，再执行同步

约束：
- 默认不改变项目，只做观察和结构化输出
- 未明确授权时，不安装 hook，不做额外发布

预期输出：
- 按 `scan -> understand -> structure -> output` 推进
- 刷新的状态文档
- 刷新的状态日志
- 风险、待办与后续动作摘要
```

### 模板 2：严格阶段化执行模板

```text
请按 `update-project-status` 的方法执行本次任务。

要求：
- 先总结你对本次状态更新目标的理解
- 按 `scan -> understand -> structure -> output` 四个阶段推进
- 显式说明 `Phase -> Execution Mapping`
- 明确哪些动作只是观察，哪些动作会写文件或同步
- 输出结果、风险和待确认项

任务内容：
- Project root: <project-root>
- Primary goal: <status refresh | recent change summary | publish status>
- Config path: <path-or-none>
- Status file override: <path-or-none>
- Log file override: <path-or-none>
- Shared doc override: <path-or-none>
- Commit limit: <n-or-default>
- Dry run: <yes-or-no>
- Install post-commit hook: <yes-or-no>
```

## 10. 总结（Summary）

`update-project-status` 最适合解决“如何把近期 Git 变化与任务来源整理成持续可维护的项目状态输出”这一类问题。它的价值不只是写一份状态文档，而是把状态采集、理解、结构化和发布串成稳定流程。

使用时最重要的边界有两条：第一，先按 `scan → understand → structure → output` 建立状态结论，再进入写入与同步；第二，默认坚持非侵入原则，只在显式授权时执行额外发布或 hook 安装动作。

## Supporting Assets

- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- Templates: [templates/](templates/)
- References: [references/](references/)
