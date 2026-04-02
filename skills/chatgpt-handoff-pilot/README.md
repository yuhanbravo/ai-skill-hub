# ChatGPT Handoff Pilot

## What is this

`chatgpt-handoff-pilot` 是一个最小可用的 handoff 母版，用来建立“上游产出任务包，下游按边界实施，并在完成后回传 execution report”的协作基线。

当它被用于项目 handoff 文档时，默认策略是把内容收口到 `docs/HANDOFF.md`，并按 V2 规则持续维护：

- 如果 `docs/HANDOFF.md` 已存在，默认做 section-aware 增量更新
- 如果 `docs/HANDOFF.md` 不存在，默认创建该文件
- 默认维护 `## Update Log`
- 默认不再生成新的 `minimal_handoff_manual.md`

## When to use

适合在已经明确分离“方案制定”和“实施落地”，并且希望每轮执行都保留清晰边界与回执时使用；如果项目已有 `AGENTS.md`、`docs/HANDOFF.md` 或 `ai/tasks/` 等本地机制，这个 skill 应作为轻量壳层接入，并优先服从本地规则。

## Quick Start

```text
Use the `chatgpt-handoff-pilot` skill to generate a task package, execute within scope, and return an execution report.

# For project handoff docs (V2):
# - update docs/HANDOFF.md incrementally if it exists
# - merge by section instead of rewriting the whole file
# - append an Update Log entry
# - do not generate minimal_handoff_manual.md by default
```

详细模板见 [SKILL.md](SKILL.md)。

## Detailed Guidance Moved From SKILL.md

The sections below were moved out of `SKILL.md` during the semantic split so the README can carry explanation-oriented material while `SKILL.md` stays execution-focused.

## 1. 背景（Problem Context）

这个 skill 用来解决多代理或多人协作中的一个高频问题：上游已经有了方案意图，但交接给实施侧后，常常会出现输入不完整、边界漂移、实施过程自行扩写、完成后回执不足等问题。

`chatgpt-handoff-pilot` 提供的是一个最小可执行的 handoff 母版。它不试图替代项目管理体系，也不绑定具体仓库结构，而是先把一次交接中最关键的三件事稳定下来：

- 上游交付什么样的 `task package`
- 下游如何在边界内执行 `bounded execution`
- 完成后如何回传 `execution report`

它在 skill-hub 中的定位更接近协作模式基线，而不是自动化框架。目标是让这套方法可以先在真实项目里小范围试跑，再根据反馈决定是否继续增强。

当前版本已升级到 V2：在保持 `docs/HANDOFF.md` 作为默认单一主文档的前提下，进一步补齐了长期维护机制，包括 `Update Log`、section-aware merge、legacy/generated 资产标记，以及正式并入主流程的 execution report 要求。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 上游负责人已经明确，希望先产出任务包，再交给 Codex、Copilot 或其他实施侧代理执行
- 希望把“方案制定”和“代码或文档落地”清晰分离
- 希望实施侧严格按授权范围施工，避免顺手扩展
- 希望每轮执行后都有统一结构的 `execution report`
- 希望在真实项目中先验证最小 handoff 流，再决定是否增加脚本、检查或更细模板
- 希望把 handoff 文档持续收口到项目内唯一主文档，而不是反复生成新入口
- 希望 handoff 主文档能被连续多次增量维护，而不是每轮重写

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用：

- 任务非常小，由同一个人或同一个代理直接完成更高效
- 项目已经存在更成熟且强制执行的本地 handoff 机制
- 上游无法提供最基本的目标、范围、约束或验收要求
- 当前任务需要开放式探索、快速试错或边做边收敛，而不是边界明确的交付执行
- 团队当前需要的是完整项目治理方案，而不是最小交接模式

## 8. 风险（Risks）

- 任务包字段不完整时，实施侧可能基于错误假设开始执行
- 范围和“不做事项”不清晰时，容易发生 scope creep
- 实施前没有复述理解时，上下游对目标文件和交付边界的理解可能不一致
- `execution report` 过于笼统时，上游很难判断是否真正完成验收要求
- 如果把这个 skill 误当成完整框架，容易过早引入只适用于单一项目的复杂机制
- 如果忽略 section-aware merge 原则，可能覆盖掉 `docs/HANDOFF.md` 中已有的人工编辑内容
- 如果继续生成新的 handoff 文件名，项目会再次出现多个“像主文档”的入口
- 如果不维护 `Update Log`，多次增量更新后会难以追踪 handoff 文档的变化来源

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：生成任务包

```text
请使用 `chatgpt-handoff-pilot` 的方法，为下面的任务生成一份可直接交给 Codex / Copilot 执行的 task package。

背景：
- <背景>

目标：
- <目标>

本次范围：
- <范围>

明确不做：
- <不做事项>

目标文件或目录：
- <文件或目录>

验收标准：
- <验收标准>

约束条件：
- <约束>

输出要求：
- 先形成边界清晰的 `task package`
- 生成结构清晰、边界明确的任务包
- 如果上下文不完整，单列“假设前提”
- 任务包应能直接用于 handoff
```

### 模板 2：执行任务包

```text
请按 `chatgpt-handoff-pilot` 的方法执行下面的任务包。

要求：
- 先完整阅读任务包和其中引用的本地规则
- 按“读取输入 -> 复述边界 -> bounded execution -> execution report”推进
- 动手前先用 2-4 句话复述目标、边界、修改范围和不做事项
- 只在授权范围内实施
- 完成后输出 execution report

任务包：
<粘贴任务包正文>
```

### 模板 3：生成或更新项目 handoff 主文档

```text
请使用 `chatgpt-handoff-pilot` 更新本项目的 handoff 主文档。

要求：
- 先读取 `docs/HANDOFF.md`（如果存在）
- 优先按 section 进行增量合并，而不是全文重写
- 重点更新：`Update Log`、`Current Status/当前状态`、`Hard Boundaries/边界`、`Recommended Next Steps/下一步建议`、`Environment Blockers/环境阻塞`
- 保留已有结构和人工编辑内容
- 若缺少合适章节，可以补 section，但不要整体重排
- 若 `docs/HANDOFF.md` 不存在，则创建它
- 不要默认生成 `minimal_handoff_manual.md`
- 如有历史 `minimal_handoff_manual.md`，仅标记为 legacy/generated，不再更新
- 追加一条 `Update Log` 记录

输出：
- 更新后的 `docs/HANDOFF.md`
- 简短 execution report
```

### 模板 4：生成 execution report

```text
请基于本次实施结果输出 execution report。

请至少覆盖以下内容：
- 本次改了什么
- 本次没改什么
- 如何验证
- 当前阻塞
- 下一步建议
- 假设清单

附加要求：
- 如果有阻塞项，单列说明
- 如果有未完成项，说明原因
- 额外发现的问题只记录，不混入本次完成项
```

## 10. 总结（Summary）

`chatgpt-handoff-pilot` 最适合解决“先由上游把任务说清楚，再由下游代理按边界执行并回传结果”这一类协作问题。它不是普通 prompt 模板，而是一套稳定的 handoff 协作协议。

使用时最重要的边界有三条：必须先明确任务包、必须先复述边界、必须输出 execution report。若任务本身不具备明确范围，就不应把它伪装成 bounded execution。

## Supporting Assets

- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Templates: [templates/](templates/)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)

