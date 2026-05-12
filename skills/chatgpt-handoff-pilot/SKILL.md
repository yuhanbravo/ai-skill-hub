---
name: chatgpt-handoff-pilot
description: "Use when preparing a handoff task package, bounded execution, or execution report across AI agents."
metadata:
   triggers:
      - prepare a handoff task package
      - bounded execution with execution report
      - split planning and implementation across AI agents
      - update the project handoff manual
      - enforce task boundaries for another agent
   side_effects:
      - read_only
      - write_files
---
# ChatGPT Handoff Pilot

This execution-focused skill definition keeps the behavior, invocation shape, and adapter-facing contract unchanged while moving explanation-oriented content into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Review-packet prompts: [prompts/review_packet_prompts.md](prompts/review_packet_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- Templates: [templates/](templates/)
- Shared assessment output protocol: [../_protocol/skill_assessment_output.md](../_protocol/skill_assessment_output.md)

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
- execution report evidence / risk_priority awareness when assessment output is involved

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
   若有阻塞项或未完成项，应明确写出原因。涉及 assessment 输出时，可引用 shared assessment output protocol 的 `evidence` 与 `risk_priority` 口径，但本 skill 仍只拥有 task package、bounded execution 和 execution report protocol，不重定义 assessment protocol。

当任务进入“把本轮施工反馈交给上游或 ChatGPT 审阅”的场景时，可以额外整理一个 `review packet`，只收敛本轮值得审的增量摘要、关键文件、验证摘要和审阅重点，用来减少重复粘贴；它不重新定义任务，也不替代 `task package` 与 `execution report`。

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
- `review packet` 只作为审阅侧的轻量辅助资产，不替代 `task package` 或 `execution report`

## Invocation

### When to use

- 当你需要把方案制定与落地执行拆给不同 AI，并要求实施侧严格按任务包施工时使用。


### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Review-packet prompts: [prompts/review_packet_prompts.md](prompts/review_packet_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- Templates: [templates/](templates/)


