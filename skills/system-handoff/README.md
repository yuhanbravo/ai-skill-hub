# System Handoff

## What is this

`system-handoff` 是一个面向 `ai-skill-hub` 本体的 system-level wrapper skill，用来以系统口径维护 [docs/HANDOFF.md](../../../docs/HANDOFF.md) ，而不是把 handoff 退化成一次普通摘要或全文重写。

它复用 canonical skill `chatgpt-handoff-pilot` 的 bounded execution 与 section-aware merge 思路，但把目标对象固定为 `skill-hub as system`，并把输出约束到 phase、boundaries、design decisions、intentional gaps 和 next-phase direction。

这是一个 system-level wrapper skill，不分叉 canonical logic，不引入 orchestration、controller 或 auto-fix，只增加 system-level section constraints。

## When to use

- 需要增量更新 `ai-skill-hub` 的 `docs/HANDOFF.md`
- 需要用 system 角度维护 `Current Status`、`Hard Boundaries` 等章节
- 需要保持 section-aware merge，而不是重写整份 handoff 文档

## Quick Start

```text
Use `system-handoff` for this task.

Target document:
- docs/HANDOFF.md

Required sections:
- Current Status
- Hard Boundaries
- Key Design Decisions
- Intentional Gaps
- Next Phase Direction
```

## Relation To Canonical Skill

- Canonical dependency: `chatgpt-handoff-pilot`
- Canonical skill path: `skills/chatgpt-handoff-pilot/`
- This wrapper reuses the canonical skill instead of replacing or forking it.
- It only narrows the target to `ai-skill-hub` and adds system-oriented section constraints.

详细执行约束见 [SKILL.md](SKILL.md)。

## Minimal Coordination Rules

- 若可用，读取 `docs/status/skill-hub-status.md` 的 `Updated at` 作为 handoff 本轮 status baseline，并在更新日志中保留该日期。
- 与 `system-status-update` 联动时，handoff 落盘前必须完成 phase consistency 检查，确保两份系统文档阶段口径一致。

## Detailed Guidance Moved From SKILL.md

The sections below were moved out of `SKILL.md` during the semantic split so the README can carry explanation-oriented material while `SKILL.md` stays execution-focused.

## 1. 背景（Problem Context）

这个 skill 用来解决 `ai-skill-hub` 进入 system 维护阶段后的另一个问题：handoff 更新本身已经有 canonical 方法，但如果没有 system-level wrapper，维护者仍容易用一次性 prompt 去改 `docs/HANDOFF.md`，导致 section 漂移、表达口径不一致，或者把 handoff 退化成全文重写。

`system-handoff` 不是新的 handoff 框架，而是一个 system-level wrapper skill。它的 canonical dependency 是 `chatgpt-handoff-pilot` 这个 canonical skill；当前 wrapper 继续复用该 skill 的 `bounded execution + section-aware merge` 方法，不分叉 canonical logic，不引入 orchestration、controller 或 auto-fix，只把更新目标固定为 `ai-skill-hub` 自身的 handoff 主文档，并增加 system-oriented section constraints。

它在 skill-hub 中属于 `system` 型 skill：重点不是说明“这轮改了哪些文件”，而是让 `docs/HANDOFF.md` 持续表达当前 phase、hard boundaries、key design decisions、intentional gaps 和 next-phase direction。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要更新 `ai-skill-hub` 的 `docs/HANDOFF.md`
- 需要把 handoff 内容按 system sections 增量合并，而不是整篇改写
- 需要稳定维护 `Current Status`、`Hard Boundaries`、`Key Design Decisions`、`Intentional Gaps`、`Next Phase Direction`
- 需要保留 canonical handoff flow，但把对象收口到 `skill-hub as system`
- 需要避免 handoff 输出退化为普通摘要或逐文件说明

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用这个 skill：

- 目标只是生成普通任务包或执行回执，此时应直接使用 `chatgpt-handoff-pilot`
- 目标是重写整份 `docs/HANDOFF.md`，而不是 section-aware merge
- 需要维护的是业务项目 handoff，而不是 `ai-skill-hub` 自身
- 任务要求输出代码 diff、文件清单或 implementation walkthrough
- 需要设计新的 handoff framework，而不是复用现有 canonical flow

## 8. 风险（Risks）

- 如果忽略 section-aware merge，容易覆盖掉已有系统边界和人工判断
- 如果 handoff 输出回到文件级或 diff 级叙述，未来维护者会再次依赖临时 prompt 对齐口径
- 如果把这个 wrapper 当成新的 handoff framework，容易削弱 `chatgpt-handoff-pilot` 的 canonical 角色
- 如果 `Intentional Gaps` 写得不清楚，后续系统扩展会更容易 scope creep

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准 system handoff 更新

```text
请使用 `system-handoff` 处理以下任务。

背景：
- 目标对象是 `ai-skill-hub` 自身的 handoff 主文档

目标：
- 以 section-aware merge 的方式更新 system handoff

范围：
- `docs/HANDOFF.md`
- 当前 phase
- system capabilities
- hard boundaries

约束：
- 复用 `chatgpt-handoff-pilot`
- 不全文重写
- 不输出代码 diff 或逐文件说明

预期输出：
- Current Status
- Hard Boundaries
- Key Design Decisions
- Intentional Gaps
- Next Phase Direction
```

### 模板 2：严格 section-aware merge 调用

```text
请按 `system-handoff` 的方法执行本次任务。

要求：
- 先读取 `docs/HANDOFF.md`
- 复用 `chatgpt-handoff-pilot` 的 section-aware merge 思路
- 只增量更新 `Current Status`、`Hard Boundaries`、`Key Design Decisions`、`Intentional Gaps`、`Next Phase Direction`
- 不全文重写
- `Next Phase Direction` 只写方向级演进

任务内容：
- Handoff document: docs/HANDOFF.md
- System phase: <phase>
- New system facts: <facts>
```

## 10. 总结（Summary）

`system-handoff` 最适合解决“如何以 system 口径持续维护 skill-hub 自身的 handoff 主文档，而不重新发明 handoff 机制”这一类问题。它不是新框架，而是对 canonical skill `chatgpt-handoff-pilot` 的系统包装入口。

使用时最重要的边界有两条：第一，必须坚持 section-aware merge；第二，必须让 handoff 内容围绕 system phase、boundaries、design decisions 和 intentional gaps 组织，而不是围绕文件改动组织。

## Supporting Assets

- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)

## 文档语言与 SSOT 说明（2026-05-11）

- 本文档面向开发人员（developer-facing），统一采用**中文为主、英文术语辅助**（例如：`Pattern`、`Invocation`、`Constraints`、`read_only`、`write_files`）。
- 本仓库的 **SSOT（Single Source of Truth）** 仍是当前 skill 目录下的 `SKILL.md`；`README.md` 仅提供可读性说明与快速上手，不得与 `SKILL.md` 发生规则分叉。
- 若 `README.md` 与 `SKILL.md` 出现冲突，必须以 `SKILL.md` 为准，并在后续修订中消除偏差。
- 本节为当前状态声明，更新日期：**2026-05-11**。

