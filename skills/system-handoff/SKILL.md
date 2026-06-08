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

This execution-focused skill definition keeps the behavior, invocation shape, and adapter-facing contract unchanged while moving explanation-oriented content into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- System status-first linked refresh entry: [../system-status-update/prompts/system_status_to_handoff_refresh_prompt.md](../system-status-update/prompts/system_status_to_handoff_refresh_prompt.md)
- Shared assessment output protocol: [../_protocol/skill_assessment_output.md](../_protocol/skill_assessment_output.md)

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
- handoff evidence / open_questions / risk_priority / phase_risk / freshness_risk awareness; do not force `maturity_score`

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
   先读取 `docs/HANDOFF.md`、当前 system status、phase 和相关 system docs，确认本轮更新对象是 `ai-skill-hub` 自身；若存在 `docs/status/skill-hub-status.md`，同步记录其 `Updated at` 作为本次 handoff 的 status baseline。

2. 对齐 canonical handoff method。  
   复用 `chatgpt-handoff-pilot` 的 `read input -> restate boundaries -> bounded execution -> execution report` 方法，不新增第二套 handoff 机制。

3. 定位必需 sections。  
   优先定位并增量更新 `Current Status`、`Hard Boundaries`、`Key Design Decisions`、`Intentional Gaps`、`Next Phase Direction`，必要时补 `Update Log`。

4. 执行 section-aware merge。  
   只把新的 system facts 合并到相关 section，保留既有结构和人工内容；不得整体重排或全文重写 `docs/HANDOFF.md`。

5. 输出简短回执。  
   回执应说明哪些 system sections 被更新、哪些 hard boundaries 保持不变、哪些 intentional gaps 继续保留，以及当前 next-phase direction。`Next Phase Direction` 必须保持方向级表达，不得写成任务清单、逐项施工 next steps 或 implementation backlog。handoff 回执可引用 shared assessment output protocol 的 `evidence`、`open_questions`、`risk_priority` 口径，并保留 phase / freshness risk awareness；不要强制使用 `maturity_score`。

6. 执行 phase consistency check。  
   若本轮同时刷新了 `docs/status/skill-hub-status.md`，则 `docs/HANDOFF.md` 中的 phase 表达必须与最新 status 一致；若不一致，应先修正再落盘。

## 7. 约束（Constraints）

- 必须复用 `chatgpt-handoff-pilot` 作为 canonical dependency，不得分叉 handoff flow
- 这是一个 system-level wrapper skill，只复用 canonical skill，不得分叉 canonical logic
- 不得引入 orchestration、controller、auto-fix 或其他新的 handoff framework 机制
- 当前 wrapper 只允许增加 system-level section constraints，不允许扩展底层 handoff 能力
- 更新 `docs/HANDOFF.md` 时必须坚持 section-aware merge，不得全文重写
- 主输出不得列代码 diff、逐文件说明或 implementation walkthrough
- `Current Status` 必须按 system phase 和 capabilities 表达，而不是施工进度表达
- `Next Phase Direction` 只能写方向级演进，不得退化成任务清单、逐项施工 next steps 或实现待办列表
- 若读取到 `docs/status/skill-hub-status.md`，本轮 handoff 更新日志应记录 status baseline 日期
- 若与 `system-status-update` 联动执行，handoff 落盘前必须完成 phase consistency 检查

## Invocation

### When to use

- 当你需要增量更新 `ai-skill-hub` 的 handoff 主文档，并保持 system-oriented section 输出时使用。


### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- System status-first linked refresh entry: [../system-status-update/prompts/system_status_to_handoff_refresh_prompt.md](../system-status-update/prompts/system_status_to_handoff_refresh_prompt.md)
