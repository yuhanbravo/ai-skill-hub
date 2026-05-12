# System Status Update

## What is this

`system-status-update` 是一个面向 `ai-skill-hub` 本体的 system-level wrapper skill，用来把状态更新收口为 layer / phase / capability / stability 口径，而不是普通项目状态摘要。

它复用 canonical skill `update-project-status` 的状态采集与写入能力，但把目标对象固定为 `skill-hub as system`，并把输出约束为系统层表达。

这是一个 system-level wrapper skill，不分叉 canonical logic，不引入 orchestration、controller 或 auto-fix，只增加 system-level output constraints。

## When to use

- 需要刷新 `ai-skill-hub` 的系统状态，而不是业务项目周报
- 需要按 `Canonical / Distribution / Governance / Tooling` 四层表达现状
- 需要输出当前 phase、capabilities 和 stability，而不是文件变更清单

## Quick Start

```text
Use `system-status-update` for this task.

System root:
- <project-root>

Expected output:
- Layer Status
- Current Phase
- Capabilities
- Stability
```

## Relation To Canonical Skill

- Canonical dependency: `update-project-status`
- Canonical skill path: `skills/update-project-status/`
- This wrapper reuses the canonical skill instead of replacing or forking it.
- It narrows the target to `ai-skill-hub` itself and only adds system-oriented output constraints.

详细执行约束见 [SKILL.md](SKILL.md)。

## Minimal Coordination Rules

- Freshness gate: 以 `14` 天为默认时效门槛；若 `Updated at` 超过门槛，输出必须显式给出 `Staleness` 风险提示。
- 与 `system-handoff` 联动时，必须先刷新 status，再交由 handoff 合并；handoff 落盘前要做 phase consistency 检查。

## Detailed Guidance Moved From SKILL.md

The sections below were moved out of `SKILL.md` during the semantic split so the README can carry explanation-oriented material while `SKILL.md` stays execution-focused.

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

## Supporting Assets

- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)

## 文档语言与 SSOT 说明（2026-05-11）

- 本文档面向开发人员（developer-facing），统一采用**中文为主、英文术语辅助**（例如：`Pattern`、`Invocation`、`Constraints`、`read_only`、`write_files`）。
- 本仓库的 **SSOT（Single Source of Truth）** 仍是当前 skill 目录下的 `SKILL.md`；`README.md` 仅提供可读性说明与快速上手，不得与 `SKILL.md` 发生规则分叉。
- 若 `README.md` 与 `SKILL.md` 出现冲突，必须以 `SKILL.md` 为准，并在后续修订中消除偏差。
- 本节为当前状态声明，更新日期：**2026-05-11**。

