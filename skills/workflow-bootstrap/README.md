# Workflow Bootstrap

## What is this

`workflow-bootstrap` 是一个 canonical workflow skill，用来为仓库定义默认的 `Copilot 主控 / Codex 施工` 协作壳层，并把最小角色分工、canonical guidance 与 future runtime pack 的映射写清楚。

## Why this exists

这个 skill 解决的是“默认 workflow 壳层不够明确”的问题，而不是再发明一套新的协议或治理工具。它把高频协作关系先定下来，方便 planner、implementer、reviewer 在同一条最小链路上工作。

## Relationship to Existing Skills

| Skill | Relationship |
| --- | --- |
| `chatgpt-handoff-pilot` | 提供 task package、bounded execution、execution report 协议；`workflow-bootstrap` 只复用，不替代。 |
| `project-takeover` | 负责陌生仓库接管与 onboarding；`workflow-bootstrap` 不承担 takeover 输出。 |
| `update-project-status` | 负责状态刷新与 status signal 汇总；`workflow-bootstrap` 不负责状态维护。 |
| `documentation-governance` | 负责文档层级、SSOT 和重复风险治理；`workflow-bootstrap` 不做治理审计。 |
| `file-structure-check` | 负责目录结构与错位文件审计；`workflow-bootstrap` 不做结构检查。 |

## Layering

- Canonical layer: `skills/workflow-bootstrap/` 是 source of truth，负责 workflow 壳层、角色分工和 runtime-pack 映射说明。
- Adapter layer: `.agents/skills/` 与 `.github/skills/` 只做 discoverability / compatibility 入口，不复制大段 canonical 内容。
- Future runtime pack: 项目侧可考虑 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 等最小文件族；这些本轮只文档化，不在 hub 内实现。

## Quick Start

1. 先让 planner 收敛方案、边界和 task package。
2. 再让 implementer 按 `chatgpt-handoff-pilot` 做 bounded execution。
3. 最后由 reviewer 检查边界、文档、索引和验证结果是否闭环。

更细的角色衔接见 [role_split_and_integration.md](role_split_and_integration.md)，future runtime pack 的项目侧目标见 [runtime_pack_minimal_manifest.md](runtime_pack_minimal_manifest.md)。

首轮可复用的五角色编排胶水见 [orchestration_snippets.md](orchestration_snippets.md)（薄封装，不重写 handoff 协议）。

## Phase 2 Draft Assets (Canonical Only)

- [canonical_backreference_rules_draft.md](canonical_backreference_rules_draft.md)
- [agents_md_thin_entrypoint_draft.md](agents_md_thin_entrypoint_draft.md)
- [copilot_instructions_thin_adapter_draft.md](copilot_instructions_thin_adapter_draft.md)

这些文件用于 future project-side runtime pack 设计；它们是 canonical drafts，不代表当前仓库已实现 project-side runtime files。

## Phase 3A Sketch Assets (Canonical Only)

- [project_side_runtime_pack_template_sketch.md](project_side_runtime_pack_template_sketch.md)
- [project_side_agents_md_template_sketch.md](project_side_agents_md_template_sketch.md)
- [project_side_copilot_instructions_template_sketch.md](project_side_copilot_instructions_template_sketch.md)

这些文件用于 future project-side runtime pack 的 template sketch；它们仍然只是 canonical sketch assets，不代表当前仓库已实现 project-side runtime files。

## Phase 3B Validation Assets (Canonical Only)

- [pilot_repo_validation_sketch.md](pilot_repo_validation_sketch.md)
- [single_consumer_repo_file_layout_sketch.md](single_consumer_repo_file_layout_sketch.md)

这些文件仅用于 future single consumer repo pilot validation；它们是 canonical validation sketches，不代表当前仓库已进入 single consumer repo implementation。
