# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准文档治理审计模板

```text
请使用 `documentation-governance` 处理以下任务。

背景：
- 需要检查仓库文档结构、事实源关系和重复问题

目标：
- 输出文档治理审计结果，并给出建议动作

范围：
- 检查 `docs/` 与 `docs_readable/` 的层级关系
- 检查重复主题、命名违规、归档候选和 README 缺口
- 执行 Mutable Status SSOT Check：检查 README、docs/README、docs/technical、CLAUDE.md、AGENTS.md、blueprint docs 是否硬编码 current phase、completed phase list、next phase、latest validation result、blocker/pending-merge status
- 默认只做 audit 和 report

约束：
- 默认不改变项目，只做观察和结构化输出
- fix 必须显式触发
- mutable project-status facts 应保留在 HANDOFF/status SSOT 中；navigation / onboarding / agent-wrapper / blueprint docs 优先链接到 SSOT，而不是复制这些事实

预期输出：
- 按 `audit -> report -> fix(optional)` 推进
- 治理报告
- 高优先级问题
- 建议动作与待确认项
```

### 模板 2：严格治理执行模板

```text
请按 `documentation-governance` 的方法执行本次任务。

要求：
- 先总结你对治理目标的理解
- 按 `audit -> report -> fix(optional)` 三段执行
- 明确当前使用的配置来源、扫描范围和输出方式
- 报告中区分“问题发现”和“建议修复”
- 明确检查 mutable project-status facts 是否从 current-state SSOT 泄漏到 README、technical docs、agent wrapper 或 blueprint docs
- 未显式授权时，不执行任何 fix

任务内容：
- Project root: <project-root>
- Config path: <path-or-none>
- Dry run: <yes-or-no>
- JSON output: <yes-or-no>
- Report path: <path-or-none>
- Write README sections: <yes-or-no>
```

### 模板 3：Mutable Status SSOT Check

```text
请使用 `documentation-governance` 做一次 Mutable Status SSOT Check。

目标：
- 确认 current project status 的 SSOT 是哪一个文档，例如 HANDOFF 或 status 文件
- 检查 navigation / onboarding / agent-wrapper / blueprint docs 是否复制了可变项目状态事实

重点检查：
- README.md
- docs/README.md
- docs/technical/
- CLAUDE.md / AGENTS.md
- docs/blueprint/

需要识别的 mutable project-status facts：
- current phase / active phase status
- completed phase list
- next phase / next-step decision
- latest validation result
- blocker status
- pending-merge state

推荐修复：
- 将可变状态事实保留在已声明的 HANDOFF/status SSOT 中
- 其他文档只保留稳定说明、阅读路径和 SSOT 链接
- 不把 README 或 technical onboarding 写成 parallel status tracker
```


## Audience-aware Round 1

- Built-in audience model: `human_machine_shared`, `human_primary_archive`, `ai_only_wrapper`, `unknown_or_mixed`.
- Built-in authority roles and doc intents are emitted in report fields without replacing existing `document_layer` model.
- Built-in conflict checks include AI-only SSOT misuse, shared-doc agent-only instructions, archive-as-current-fact references, navigation status duplication, and language mismatch for shared docs.
- Round 1 remains internal-only and does not integrate markdownlint/lychee/Vale/textlint.
