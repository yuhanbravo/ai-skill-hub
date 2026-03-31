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
