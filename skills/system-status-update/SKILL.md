---
name: system-status-update
description: "Use when refreshing ai-skill-hub as a capability system and the output must stay layer-oriented instead of file-oriented."
metadata:
   triggers:
      - refresh ai-skill-hub system status
      - update skill-hub layer status and phase
      - generate a capability-system status summary
      - produce layer-oriented status for ai-skill-hub
      - summarize canonical distribution governance and tooling layers
   side_effects:
      - read_only
      - write_files
      - requires_git
---

# System Status Update

## 1. 背景（Problem Context）

这个 skill 用来解决 `ai-skill-hub` 在进入 `Controlled System` 阶段后出现的一个系统问题：底层状态刷新能力已经存在，但系统层状态表达仍然容易退化成普通项目摘要、文件改动列表或一次性 prompt 口径。

`system-status-update` 不是新的状态引擎，而是一个 system-level wrapper skill。它的 canonical dependency 是 `update-project-status` 这个 canonical skill；当前 wrapper 直接复用该 skill 的状态采集、整理和写入能力，不分叉 canonical logic，不引入 orchestration、controller 或 auto-fix，只把目标对象固定为 `skill-hub as system`，并增加围绕 layer、phase、capabilities 和 stability 的 system-level output constraints。

它在 skill-hub 中属于 `system` 型 skill：重点不是报告“改了哪些文件”，而是报告“系统当前处于哪个阶段、哪些层稳定、哪些能力已经形成、哪些层仍在演进”。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要刷新 `ai-skill-hub` 自身的系统状态，而不是普通项目周报
- 需要按 `Canonical Skill Layer`、`Distribution Layer`、`Governance Layer`、`Tooling Layer` 输出状态
- 需要明确当前 phase、capabilities 和 stability 口径
- 需要把已有 Git 信号、文档和工具链变化收口到 system-level summary
- 需要更新 `docs/status/skill-hub-status.md` 一类系统状态文档

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用这个 skill：

- 目标只是刷新普通项目状态或周报，此时应直接使用 `update-project-status`
- 目标是分析系统结构、瓶颈和演进策略，而不是刷新状态，此时更接近 `system-takeover`
- 任务要求输出文件级变更清单、函数级实现说明或施工日报
- 当前不允许写入状态文档，也不需要形成 system-level status artifact
- 需要扩展新的状态框架，而不是复用现有 canonical skill

## 4. 核心模式（Pattern）

### System Layer Status Refresh Pattern（系统分层状态刷新模式）

这个 pattern 的核心是：

- 复用 `update-project-status` 收集近期系统信号
- 把信号映射到 system layers，而不是文件列表
- 用 phase、capabilities 和 stability 组织状态输出

Input:
- `ai-skill-hub` 根目录
- Git history 与 working tree 信号
- `skills/`、`.agents/`、`.github/`、`tools/`、`docs/status/`

Process:
- `scan`
- `understand`
- `structure`
- `output`

Output:
- `Layer Status`
- `Current Phase`
- `Capabilities`
- `Stability`

这样组织的原因是，system status 的价值在于说明系统边界和成熟度，而不是把最近提交翻译成文件级流水账。底层刷新能力继续由 canonical skill `update-project-status` 提供，这个 wrapper 只负责 system-oriented 收口。

## 5. 核心原则（Principles）

- 先复用 canonical status engine，再收口到 system output。  
  Reuse the canonical status engine before adding system-level framing.

- 输出必须按层表达，而不是按文件表达。  
  Express status by layers, not by files.

- phase、capabilities 和 stability 是主口径。  
  Make phase, capabilities, and stability the primary vocabulary.

- 不把 system status 退化成项目日报。  
  Do not degrade system status into a project activity report.

- 写入动作仍保持最小化。  
  Keep writes minimal and scoped to system status artifacts.

## 6. 执行流程（Execution Steps）

1. 读取 system context。  
   先把目标对象确认为 `ai-skill-hub` 自身，并读取 `docs/status/skill-hub-status.md`、`README.md`、`skills/`、distribution surfaces 和 tooling 入口。

2. 调用 canonical status logic。  
   复用 `update-project-status` 的 `scan -> understand -> structure -> output` 方法收集 Git、working tree 和系统资产信号，但不要沿用普通项目视角输出。

3. 建立 layer mapping。  
   把近期变化映射到 `Canonical Skill Layer`、`Distribution Layer`、`Governance Layer`、`Tooling Layer` 四层，并判断 phase 与 stability。

4. 组织 system-oriented output。  
   输出必须至少包含 `Layer Status`、`Current Phase`、`Capabilities`、`Stability`；若需要写入状态文档，也应按这个结构落盘。

5. 回传风险与未确认项。  
   若证据不足，应明确说明哪些判断来自代码与文档证据，哪些仍需后续验证，避免把推断写成确定事实。

## 7. 约束（Constraints）

- 必须复用 `update-project-status` 作为 canonical dependency，不得复制出第二套状态刷新逻辑
- 这是一个 system-level wrapper skill，只复用 canonical skill，不得分叉 canonical logic
- 不得引入 orchestration、controller、auto-fix 或其他新的 system framework 机制
- 当前 wrapper 只允许增加 system-level output constraints，不允许扩展底层状态能力
- 主输出不得列文件修改、函数实现细节或逐项施工记录
- 不得发明新的 phase 体系，必须沿用仓库已有 system-phase 语义
- 不得把 layer status 退化为代码清单或提交列表
- 除状态文档本身外，不应顺带修改其他系统资产

## 8. 风险（Risks）

- 如果直接沿用普通项目状态模板，输出会丢失 system layer 语义
- 如果把 Git 变更等同于 layer 变化，可能高估系统成熟度
- 如果输出回到文件级叙述，未来维护者会再次依赖手工 prompt 对齐口径
- 如果把这个 wrapper 误当成新引擎，容易分叉 `update-project-status` 的 canonical 角色

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准 system status 调用

```text
请使用 `system-status-update` 处理以下任务。

背景：
- 目标对象是 `ai-skill-hub` 自身，不是普通业务项目

目标：
- 刷新 system status，并按 layer / phase / capabilities / stability 输出

范围：
- `skills/`
- `.agents/`
- `.github/`
- `tools/`
- `docs/status/`

约束：
- 复用 `update-project-status`
- 不输出文件级变更清单
- 不退化为项目施工日报

预期输出：
- Layer Status
- Current Phase
- Capabilities
- Stability
```

### 模板 2：严格 system-layer 输出调用

```text
请按 `system-status-update` 的方法执行本次任务。

要求：
- 先确认目标对象是 capability system
- 复用 `update-project-status` 的状态刷新过程
- 输出必须包含 `Canonical Skill Layer`、`Distribution Layer`、`Governance Layer`、`Tooling Layer`
- 明确当前 `Phase`、`Capabilities`、`Stability`
- 不输出文件级改动摘要

任务内容：
- System root: <project-root>
- Status artifact: <path-or-none>
- Dry run: <yes-or-no>
```

## 10. 总结（Summary）

`system-status-update` 最适合解决“如何把 skill-hub 自身的状态刷新稳定表达为 system-layer 结论，而不是普通项目更新”这一类问题。它不是新能力引擎，而是对 canonical skill `update-project-status` 的系统包装入口。

使用时最重要的边界有两条：第一，必须坚持 system-layer 表达；第二，必须复用 canonical status skill，而不是分叉出第二套状态机制。

## Invocation

### When to use

- 当你需要刷新 `ai-skill-hub` 自身的状态，并强制输出 layer / phase / capability / stability 结构时使用。

### Input Example

```text
Use system-status-update for this task.

task_description:
- Refresh ai-skill-hub as a capability system and report the current layer status.

constraints:
- Reuse update-project-status as the canonical status engine.
- Do not output file-level change lists.

expected_output:
- Layer Status
- Current Phase
- Capabilities
- Stability

context_files:
- docs/status/skill-hub-status.md
- skills/
- .agents/
- .github/
- tools/
```

### Output Example

```text
Layer Status:
- Canonical Skill Layer: stable
- Distribution Layer: evolving
- Governance Layer: evolving
- Tooling Layer: evolving

Current Phase:
- Phase 3 - Controlled System

Capabilities:
- Stable canonical source of truth
- Repeatable project-local distribution
- Read-only drift detection

Stability:
- canonical: stable
- system rollout: evolving

Risks:
- Some maturity judgments may remain provisional if enforcement evidence is incomplete.
```