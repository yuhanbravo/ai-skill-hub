---
name: chatgpt-handoff-pilot
description: 最小可用的 handoff skill 母版，用于上游先产出任务包、下游按边界实施并回传 execution report 的协作场景。
---

# ChatGPT Handoff Pilot

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

## 4. 核心模式（Pattern）

### Task Package Handoff Pattern（任务包交接模式）

这个 pattern 的核心是把一次协作稳定组织成一条清晰的输入到输出链路：

- 输入对象是 `task package`，负责说明背景、目标、范围、限制、验收标准和预期产物
- 中间动作是 `bounded execution`，实施侧先复述理解，再只在授权范围内落地
- 输出对象是 `execution report`，负责回传实际改动、边界遵守情况、验证结果、风险和假设

Input:
- `task package`
- 本地 handoff 规则
- 目标文件或目录

Process:
- 读取任务包
- 复述边界
- `bounded execution`
- 输出 `execution report`

Output:
- 边界明确的实施结果
- 结构化 `execution report`
- 风险与假设记录

这样组织的原因是，handoff 失败往往不是因为能力不足，而是因为输入模糊、边界失控、回执缺失。把这三类对象明确下来后，协作就更容易执行、复盘和迁移。

如果项目已经有 `AGENTS.md`、`docs/HANDOFF.md`、`ai/tasks/`、任务板或其他本地约定，这个 pattern 应作为壳层接入，并优先服从本地规则。

### SSOT Handoff Maintenance Pattern（单一主文档维护模式）

当本 skill 被用于“生成或更新项目 handoff 文档”时，默认输出策略固定为：

- 若存在 `docs/HANDOFF.md`：读取该文件，并在原结构内做增量更新
- 若不存在 `docs/HANDOFF.md`：创建该文件，并以最小 handoff 手册模板作为初始内容
- 默认不再生成新的 `minimal_handoff_manual.md`
- 若历史存在 `minimal_handoff_manual.md` 或其他历史 handoff 生成物：保留但不再更新，只在 `docs/HANDOFF.md` 中做 legacy/generated 标记

这里的关键要求是：优先保留已有结构与人工编辑内容，把新增信息合并进对应章节；若没有合适章节，则补充新 section，但不要重排整份文档。

### Section-Aware Merge Pattern（按章节感知的增量合并模式）

V2 版本明确要求 handoff 主文档更新默认按 section 定位，而不是全文泛化改写。优先识别和增量更新这些 section：

- `Update Log`
- `Current Status` / `当前状态`
- `Hard Boundaries` / `边界`
- `Recommended Next Steps` / `下一步建议`
- `Environment Blockers` / `环境阻塞`

如果对应 section 不存在，可以补充缺失 section；但不要因为模板不一致而整体覆盖 `docs/HANDOFF.md`。

## 5. 核心原则（Principles）

- 先把输入说清楚，再开始执行。  
  Define the handoff input before execution starts.

- 先复述边界，再进行改动。  
  Restate the scope before making changes.

- 只交付被授权的内容。  
  Deliver only what is explicitly in scope.

- 所有假设都要显式记录。  
  Make every assumption explicit.

- 回执服务验收与下一轮协作。  
  Use the execution report to support acceptance and the next handoff.

- 项目 handoff 文档默认收口到单一主文档。  
  Default to a single authoritative handoff document.

- handoff 主文档默认按章节增量维护。  
  Update the handoff document section by section, not by full rewrite.

## 6. 执行流程（Execution Steps）

1. 读取交接输入。  
   完整阅读上游提供的任务包，以及其中引用的本地规则、目录、模板和验收说明；如果任务包引用了 `AGENTS.md`、`docs/HANDOFF.md`、`ai/tasks/` 或类似文档，也一并纳入上下文。

2. 检查任务包是否具备最小可执行字段。  
   至少确认以下内容是否存在且足够清晰：任务名称、背景与目标、本次范围、明确不做事项、目标文件或目录、验收标准、约束条件、输出要求。若字段缺失，应先记录缺口或补充假设，再进入实施。

3. 输出实施前理解摘要。  
   在真正改动前，用简短摘要说明本轮目标、明确不做什么、计划涉及哪些文件或目录、完成后要交付什么。这一步的作用是降低误解和越界风险。

4. 按边界执行。  
   仅在任务包授权的范围内修改代码、文档或配置；优先完成直接目标，不顺手整理无关内容，不把额外发现的问题混入本轮交付。

5. 处理范围外问题。  
   如果发现额外问题，应按以下方式处理：与本轮目标直接冲突的阻塞项要单列说明；可以顺手修但未被授权的内容默认不做；可能影响验收但暂时无法解决的事项应记录为风险或待确认项。

6. 处理 handoff 主文档落盘。  
   当本轮输出包含项目 handoff 文档时，默认先检查 `docs/HANDOFF.md`：
   - 若文件存在：读取、识别现有结构、在对应章节做增量更新，并尽量保留人工内容
   - 若文件不存在：创建 `docs/HANDOFF.md`，以最小 handoff 手册为初始模板
   - 若仓库中已有 `minimal_handoff_manual.md` 或其他历史 handoff 生成物：不删除、不继续更新；需要时仅在 `docs/HANDOFF.md` 中标记为 legacy/generated
   - 如 `docs/HANDOFF.md` 顶部尚无主文档提示，可补充：`This file is the single source of truth for project handoff.`
   - 如仓库中存在历史生成 handoff 文件，可在合适位置补充：`Historical generated handoff artifacts may exist, but this file is the single source of truth.`

7. 执行 section-aware merge。  
   更新 `docs/HANDOFF.md` 时，优先定位以下 section 并增量维护：
   - `## Update Log`
   - `## Current Status` / `## 当前状态`
   - `## Hard Boundaries` / `## 边界`
   - `## Recommended Next Steps` / `## 下一步建议`
   - `## Environment Blockers` / `## 环境阻塞`
   若缺失则补 section；若存在则只合并新增事实，不整体重写全文件。

8. 维护 `Update Log`。  
   每次更新 handoff 主文档时，默认追加一条简短记录到 `## Update Log`。推荐格式保持稳定，至少包含：
   - 日期
   - 本次新增/更新主题
   - 是否存在环境阻塞
   如果该 section 不存在，则补建，但不要重排整份文档。

9. 输出 execution report。  
   完成后提供结构化回执，至少包含：
   - 本次改了什么
   - 本次没改什么
   - 如何验证
   - 当前阻塞
   - 下一步建议
   若有阻塞项或未完成项，应明确写出原因。

## 7. 约束（Constraints）

- 这是一个最小母版 skill，只定义 handoff 的最小协作壳层，不提供完整项目治理方案
- 不绑定固定业务目录、固定文件名或固定仓库结构
- 不内置自动生成器、字段校验器或任务状态机
- 不替代项目本地的正式设计文档、交接文档、任务系统或协作规则
- 当项目已有成熟规则时，默认优先遵守项目本地规则
- 当项目已存在 `docs/HANDOFF.md` 时，默认必须增量更新该文件，而不是另起新的 handoff 主文档
- 默认不再把 `minimal_handoff_manual.md` 作为输出文件名
- 默认按 section 感知方式更新 `docs/HANDOFF.md`，而不是全文重写
- 不要为了贴合模板而重排整份 `docs/HANDOFF.md`

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

`chatgpt-handoff-pilot` 最适合解决“任务需要先拆清楚，再交给另一个实施侧严格落地”的协作问题。它的价值不在于流程复杂，而在于稳定输入、边界和回执。

使用这个 skill 时，最重要的边界是保持最小化定位，不把它扩写成完整框架；最重要的规则是先明确任务包，再按范围执行，并在结束后回传结构化 `execution report`。当它被用于项目 handoff 文档时，默认应把内容收口到 `docs/HANDOFF.md` 这一份单一主文档，并通过 `Update Log + section-aware merge` 的方式长期维护，而不是继续产生新的平行手册。
