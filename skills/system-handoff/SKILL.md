---
name: system-handoff
description: "Use when updating ai-skill-hub handoff as a system document and the merge must stay section-aware instead of becoming a full rewrite."
metadata:
   triggers:
      - update ai-skill-hub system handoff
      - maintain skill-hub handoff sections
      - refresh system boundaries in docs HANDOFF md
      - capture next phase direction for ai capability system
      - merge system-level handoff updates without full rewrite
   side_effects:
      - read_only
      - write_files
---

# System Handoff

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

## 4. 核心模式（Pattern）

### System Handoff Section Merge Pattern（系统交接章节合并模式）

这个 pattern 的核心是：

- 复用 `chatgpt-handoff-pilot` 的 bounded execution 与 section-aware merge
- 把 handoff 更新限制在系统层关键 sections
- 用 system boundaries 和 next-phase direction 维护长期可读性

Input:
- `docs/HANDOFF.md`
- 当前 phase 与 system capabilities
- system boundaries、design decisions 和 intentional gaps

Process:
- `read`
- `locate sections`
- `merge incrementally`
- `report`

Output:
- 增量更新后的 system handoff sections
- 简短 execution report

这样组织的原因是，handoff 在 system repo 中的作用是保持长期边界清晰，而不是每轮都重新生成一份说明文档。底层 merge 方法继续来自 canonical skill `chatgpt-handoff-pilot`，这个 wrapper 只负责 system-oriented 收口。

## 5. 核心原则（Principles）

- 先复用 canonical handoff flow，再施加 system constraints。  
  Reuse the canonical handoff flow before adding system constraints.

- 只做 section-aware merge，不做全文重写。  
  Use section-aware merge and avoid full rewrites.

- 章节内容必须服务系统边界与阶段表达。  
  Keep sections focused on system boundaries and phase expression.

- `Next Phase Direction` 只写方向，不写任务清单。  
  Keep next-phase content directional, not task-list oriented.

- handoff 不得退化为 diff 摘要。  
  Do not degrade handoff into a diff summary.

## 6. 执行流程（Execution Steps）

1. 读取 system handoff context。  
   先读取 `docs/HANDOFF.md`、当前 system status、phase 和相关 system docs，确认本轮更新对象是 `ai-skill-hub` 自身。

2. 对齐 canonical handoff method。  
   复用 `chatgpt-handoff-pilot` 的 `read input -> restate boundaries -> bounded execution -> execution report` 方法，不新增第二套 handoff 机制。

3. 定位必需 sections。  
   优先定位并增量更新 `Current Status`、`Hard Boundaries`、`Key Design Decisions`、`Intentional Gaps`、`Next Phase Direction`，必要时补 `Update Log`。

4. 执行 section-aware merge。  
   只把新的 system facts 合并到相关 section，保留既有结构和人工内容；不得整体重排或全文重写 `docs/HANDOFF.md`。

5. 输出简短回执。  
   回执应说明哪些 system sections 被更新、哪些 hard boundaries 保持不变、哪些 intentional gaps 继续保留，以及当前 next-phase direction。`Next Phase Direction` 必须保持方向级表达，不得写成任务清单、逐项施工 next steps 或 implementation backlog。

## 7. 约束（Constraints）

- 必须复用 `chatgpt-handoff-pilot` 作为 canonical dependency，不得分叉 handoff flow
- 这是一个 system-level wrapper skill，只复用 canonical skill，不得分叉 canonical logic
- 不得引入 orchestration、controller、auto-fix 或其他新的 handoff framework 机制
- 当前 wrapper 只允许增加 system-level section constraints，不允许扩展底层 handoff 能力
- 更新 `docs/HANDOFF.md` 时必须坚持 section-aware merge，不得全文重写
- 主输出不得列代码 diff、逐文件说明或 implementation walkthrough
- `Current Status` 必须按 system phase 和 capabilities 表达，而不是施工进度表达
- `Next Phase Direction` 只能写方向级演进，不得退化成任务清单、逐项施工 next steps 或实现待办列表

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

## Invocation

### When to use

- 当你需要增量更新 `ai-skill-hub` 的 handoff 主文档，并保持 system-oriented section 输出时使用。

### Input Example

```text
Use system-handoff for this task.

task_description:
- Update ai-skill-hub handoff as a system document without rewriting the whole file.

constraints:
- Reuse chatgpt-handoff-pilot as the canonical handoff flow.
- Keep docs/HANDOFF.md section-aware and system-oriented.

expected_output:
- Current Status
- Hard Boundaries
- Key Design Decisions
- Intentional Gaps
- Next Phase Direction

context_files:
- docs/HANDOFF.md
- docs/status/skill-hub-status.md
- README.md
```

### Output Example

```text
Current Status:
- Phase 3 - Controlled System
- Stable canonical layer with evolving governance and tooling

Hard Boundaries:
- skills/ remains the only canonical source of truth
- adapter layers remain derivative surfaces

Key Design Decisions:
- thin adapters preserve discoverability without duplicating content

Intentional Gaps:
- no auto-fix
- no orchestration controller

Next Phase Direction:
- move from controlled local governance toward controlled enforcement

Risks:
- section merges still depend on accurate identification of existing system sections.
```