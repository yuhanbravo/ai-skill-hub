# Skill Hub Status

- Updated at: `2026-04-23`
- Scope: `ai-skill-hub`
- Method: `system-status-update` wrapper over `update-project-status`
- Config: `.codex/skill-config/update-project-status.json`
- Data sources: Git history, working tree, `skills/`, `.agents/`, `.github/`, `tools/`, `docs/status/`

## Layer Status

### Canonical Skill Layer (`skills/`)

- Status: `stable`
- Canonical layer 仍然是唯一事实源；`workflow-bootstrap` 现已从 Phase 2 的薄入口 canonical drafts 推进到 Phase 3A 的 project-side runtime pack template sketch。新增的 canonical sketch assets 包括 `project_side_runtime_pack_template_sketch.md`、`project_side_agents_md_template_sketch.md`、`project_side_copilot_instructions_template_sketch.md`，它们都明确只是 future project-side runtime pack 的设计输入，而不是当前仓库已实现的 project-side runtime files。
- 当前 canonical sketch 已把 v1 project-side runtime pack 的文件集合进一步收敛为 `required / optional / not recommended` 三层，并明确了 `AGENTS.md` 的 fixed vs project-fill 字段、`.github/copilot-instructions.md` 的最薄边界、consumer repo 中 canonical guidance 的 path backreference 表达方式，以及 anti-second-rulebook 约束。
- `workflow-bootstrap` 仍只承载 workflow 壳层、canonical guidance 到 future runtime pack 的映射说明与 template sketch，不替代 `chatgpt-handoff-pilot`；后者仍然是 handoff / bounded execution / execution report 的协议层。本轮也没有引入第二套 status 机制，没有改变 `update-project-status` 作为 canonical status engine 的依赖关系，future runtime pack 仍未在 hub 内实现，当前仍不存在真正落地的 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 仓库层。

### Distribution Layer (`.agents/` / `.github/` / bridge-facing continuity)

- Status: `evolving`
- Hub-side thin wrapper 与 GitHub fallback surface 仍保持可发现性，但本轮没有新增任何新的 skill、adapter / discoverability 入口或 index 更新；`.agents/skills/` 与 `.github/skills/` 继续只承担 derivative discoverability 角色，而不是 authorship surface。
- `SKILLS_INDEX.md` 与 `skills_index.json` 本轮均未更新；Phase 3A 的推进只发生在 `workflow-bootstrap` canonical layer 内，没有把 project-side template sketch 扩展为 hub-side discoverability 变化。
- 最近的 bridge mirror refresh 说明 handoff/status 的 continuity surface 仍在维护，但 active ownership 依然留在 `docs/HANDOFF.md` 与 `docs/status/skill-hub-status.md`；这一层可用性是稳定的，自动一致性仍然不强。

### Governance Layer

- Status: `evolving`
- Governance 已不只是 adapter drift check；当前还具备 commit convention、hub-vs-consumer dual-mode adapter guidance，以及新增的 derivative-surface drift audit，能以只读方式审视 bridge / metadata 这类派生面是否发生语义漂移。
- 本轮没有改动任何 `sync / export / import / check` 工具逻辑，也没有改动现有相关 skills 的核心契约；新增的是 canonical template sketch，而不是治理机制升级。
- Phase 3A execution report 已明确说明：本轮是纯文档 sketch 改动，因此未额外运行工具脚本验证，以避免扩大 bounded scope；这应被视为受控范围选择，而不是遗漏的 rollout-ready 验证。
- 当前 working tree 还显示了一份 `documentation-governance` 与 `update-project-status` 的最小联动约定，说明文档角色边界正在继续收口，但它目前仍应视为 in-progress signal，而不是已强制落地的仓库规则。

### Tooling Layer (`tools/`)

- Status: `evolving`
- Tooling layer 现在覆盖 sync、router、pipeline、metadata generation、local checks、adapter consistency、re-seed audit、derivative-surface audit，以及面向 skill-hub 模板的 status refresh。
- 最近一轮强化主要体现在两点：`generate_skill_metadata.py` 对 example-file layout 的提取更稳，`update_project_status.py` 在 no-git / workspace-driven 场景下也能给出结构化 refresh，而不需要退回普通项目口径。
- 与 `workflow-bootstrap` 相关的本轮落地没有扩张工具层职责：没有新增 runtime pack 生成器、没有引入 controller / orchestration framework，也没有把 project-side 文件模板写进工具链默认产物。Phase 3A 仍只是在 canonical 文档层新增 template sketch 资产。

## Current Phase

- Current phase: `Phase 3 - Controlled System`
- Phase judgment: 当前系统已经具备稳定 canonical source、可用 distribution surfaces、read-only governance、repeatable tooling，以及 system-level wrapper entrypoints；本轮新增的是 Phase 3A canonical template sketches，而不是 project-side runtime pack 实现，因此还没有进入 single consumer repo implementation、distribution / rollout，或更重的 runtime phase。
- Why unchanged: 最近增强的是 `workflow-bootstrap` 从 Phase 2 薄入口草案推进到 Phase 3A template sketch 的表达能力，补齐了原来尚未成型的 project-side template 问题，但没有改变当前 phase 的边界定义，也没有把 future runtime pack 从 canonical 设计层推进到已实现层。
- Main direction: 继续在不打破层边界的前提下，把 canonical template sketch 推进到更小范围的单仓试点 implementation task package；下一阶段应先解析一个真实 consumer repo 的具体路径占位符与入口组合，而不是直接进入 distribution 或多仓 rollout。

## Capabilities

- Layered capability system: canonical skills、distribution adapters、governance checks 与 tooling 仍保持清晰分层，没有重新混成单层仓库。
- Minimal canonical workflow expression: 仓库现在已经具备 `Copilot 主控 / Codex 施工` 默认链路的最小 canonical 表达，并且把 `planner / implementer / reviewer` 作为默认的最小角色分工写入 canonical skill。
- Workflow-shell coordination: `workflow-bootstrap` 现在能够把 workflow 壳层、bounded execution 协同方式，以及 `chatgpt-handoff-pilot` 的协议层职责区分开来，减少“谁负责链路、谁负责 handoff 协议”的歧义。
- Canonical-to-runtime-pack mapping: 仓库现在已经把 future runtime pack 的最小文件族从 mapping / manifest 层进一步推进到 template sketch 层，但仍明确停留在 canonical 设计资产层，而不是当前仓库的已实现层。
- Thin-entry draft set (Phase 2): `workflow-bootstrap` 已具备 `AGENTS.md` 薄主入口草案、`.github/copilot-instructions.md` 薄适配草案、以及 canonical backreference rules 草案，这些仍然是 Phase 3A template sketch 的前置输入，而不是被替换掉的历史结论。
- Template sketch set (Phase 3A): `workflow-bootstrap` 现在已明确 v1 project-side runtime pack 的 `required / optional / not recommended` 文件集合分层，并形成了 `AGENTS.md` fixed vs project-fill 字段草案、`.github/copilot-instructions.md` 最薄适配边界草案、canonical path backreference 表达草案，以及 anti-second-rulebook 约束草案。
- Workspace-aware status refresh: `update-project-status` 现在可以基于 `git`、`workspace` 或 `hybrid` 信号刷新状态，并明确 `primary status doc`、snapshot 与 truth precedence 这类 SSOT-lite 角色。
- Derivative-surface auditing: 仓库现在能只读检查 bridge / metadata 这类派生面的语义漂移，而不把 mirror surface 提升为新的 active source。
- Invocation metadata resilience: invocation example extraction 已经适配 example-file layout，降低了 metadata build 与 discovery surface 因布局差异产生的抽取漂移。
- Bridge continuity: handoff/status 的 bridge-facing mirror 现在可以按语义刷新，并保持 active source 与 continuity copy 的边界明确。
- Local-first validation: 系统仍以本地入口和脚本化检查为主，但这些入口已经足够支持 status、metadata、adapter、mirror 等关键维护面上的重复执行。
- Wrapper coordination baseline: `system-status-update` 与 `system-handoff` 现在具备最小联动规则（14 天 freshness gate、status 先于 handoff、handoff phase consistency 检查），用于降低双文档口径漂移。

## Stability

- Overall maturity: `evolving`
- Stable: canonical ownership、wrapper-only system skills、active-source documentation ownership、hub-vs-consumer contract separation，以及“`skills/` 是唯一 canonical source、`.agents/.github` 是 adapter / discoverability layer、bridge 是 continuity / mirror layer”的基本边界表达。
- Evolving: distribution freshness、derivative-surface governance、workspace-aware status refresh ergonomics、metadata/discovery robustness，以及 workflow shell 到 project-side runtime pack template sketch 的衔接判断。
- Not yet stable: CI-backed enforcement、automatic mirror consistency、automatic governance-mode detection、deterministic orchestration、single consumer repo pilot implementation，以及真正的 project-side runtime pack 实现；当前仍没有落地 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 这一组项目侧入口文件。
- Evidence boundary: 本次刷新结合了当前 working tree、Phase 3A 新增的 `workflow-bootstrap` canonical sketch 资产、`README.md` 的最小导航补充，以及 execution report 中记录的边界与验证说明；`SKILLS_INDEX.md` 与 `skills_index.json` 本轮未更新，这一点被视为有意保持 scope，而不是遗漏事实。
- Freshness gate: `Updated at` 已通过 14 天时效门槛检查（当前年龄 0 天），本次无需新增 `Staleness` 风险项。

## Recommended Next Steps

- 在保持 canonical-only 边界的前提下，优先进入一个更小范围的 single consumer repo pilot implementation task package，而不是直接进入 distribution 或多仓 rollout。
- 该试点应只解析一个真实 consumer repo 的具体 canonical path 占位符与入口组合，不应一次性铺开 `.github/instructions/*.instructions.md` 或 `.github/agents/*.agent.md` 模板集合。
- 继续保持 `workflow-bootstrap` 的 workflow-shell 定位，让它与 `chatgpt-handoff-pilot`、`project-takeover`、`update-project-status`、`documentation-governance`、`file-structure-check` 的边界维持清晰，而不是把它扩张为新的控制层。
