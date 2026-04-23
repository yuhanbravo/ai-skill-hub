# Skill Hub Status

- Updated at: `2026-04-22`
- Scope: `ai-skill-hub`
- Method: `system-status-update` wrapper over `update-project-status`
- Config: `.codex/skill-config/update-project-status.json`
- Data sources: Git history, working tree, `skills/`, `.agents/`, `.github/`, `tools/`, `docs/status/`

## Layer Status

### Canonical Skill Layer (`skills/`)

- Status: `stable`
- Canonical layer 仍然是唯一事实源；当前 `workflow-bootstrap` 已完成 Phase 2 的薄入口 canonical drafts：`AGENTS.md` 主入口草案、`.github/copilot-instructions.md` 薄适配草案，以及 canonical backreference rules 草案。它们都明确是 future project-side runtime pack 设计资产，而不是当前仓库已实现的 project-side runtime files。
- `workflow-bootstrap` 当前只承载三类最小能力：`planner / implementer / reviewer` role split、canonical guidance 到 future runtime pack 的映射说明、以及 bounded execution 协同方式；Phase 2 新增薄入口草案后，这一定位仍保持不变。它没有替代 `chatgpt-handoff-pilot`，后者仍然是 handoff / bounded execution / execution report 的协议层。
- 本轮变化没有引入第二套 status 机制，也没有改变 `update-project-status` 作为 canonical status engine 的依赖关系；future runtime pack 仍未在 hub 内实现，当前仍不存在真正落地的 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 仓库层。

### Distribution Layer (`.agents/` / `.github/` / bridge-facing continuity)

- Status: `evolving`
- Hub-side thin wrapper 与 GitHub fallback surface 仍保持可发现性；本轮 `workflow-bootstrap` 已补齐 `.agents/skills/` 与 `.github/skills/` 的最小 discoverability / compatibility 入口，并继续通过 adapter 指回 canonical source，而不是复制完整实现。
- `SKILLS_INDEX.md` 已纳入 `workflow-bootstrap`，因此 hub 内的人工发现面已经补齐；`skills_index.json` 则被有意 deferred，因为仓库当前的生成链会联动重写 `.agents/skills/*.md` flat summaries，超出本轮白名单范围。
- 最近的 bridge mirror refresh 说明 handoff/status 的 continuity surface 仍在维护，但 active ownership 依然留在 `docs/HANDOFF.md` 与 `docs/status/skill-hub-status.md`；这一层可用性是稳定的，自动一致性仍然不强。

### Governance Layer

- Status: `evolving`
- Governance 已不只是 adapter drift check；当前还具备 commit convention、hub-vs-consumer dual-mode adapter guidance，以及新增的 derivative-surface drift audit，能以只读方式审视 bridge / metadata 这类派生面是否发生语义漂移。
- 本轮与 `workflow-bootstrap` 直接相关的治理验证已实际执行并补跑通过：hub adapter contract 检查通过，`run_local_checks.ps1 -Checks governance` 也已通过；这说明新增 canonical skill 与 `.agents/.github` 入口没有破坏现有 hub adapter contract。
- 同时，本轮没有改动任何 `sync / export / import / check` 工具逻辑，也没有改动现有五个相关 skills 的核心契约；新增的是 canonical workflow 表达和 discoverability，而不是治理机制升级。
- 当前 working tree 还显示了一份 `documentation-governance` 与 `update-project-status` 的最小联动约定，说明文档角色边界正在继续收口，但它目前仍应视为 in-progress signal，而不是已强制落地的仓库规则。

### Tooling Layer (`tools/`)

- Status: `evolving`
- Tooling layer 现在覆盖 sync、router、pipeline、metadata generation、local checks、adapter consistency、re-seed audit、derivative-surface audit，以及面向 skill-hub 模板的 status refresh。
- 最近一轮强化主要体现在两点：`generate_skill_metadata.py` 对 example-file layout 的提取更稳，`update_project_status.py` 在 no-git / workspace-driven 场景下也能给出结构化 refresh，而不需要退回普通项目口径。
- 与 `workflow-bootstrap` 相关的本轮落地没有扩张工具层职责：没有新增 runtime pack 生成器、没有引入 controller / orchestration framework，也没有把 project-side 文件模板写进工具链默认产物。

## Current Phase

- Current phase: `Phase 3 - Controlled System`
- Phase judgment: 当前系统已经具备稳定 canonical source、可用 distribution surfaces、read-only governance、repeatable tooling，以及 system-level wrapper entrypoints；本轮新增的是最小 canonical workflow 表达，而不是 project-side runtime pack 实现，因此还没有进入 CI-backed enforcement、controller-style orchestration 或更重的 runtime phase。
- Why unchanged: 最近增强的是 workflow shell 的 canonical 表达能力，以及 role split / future runtime pack mapping 的说明清晰度；这些变化补齐了原来缺失的 workflow 表达，但没有改变当前 phase 的边界定义。
- Main direction: 继续在不打破层边界的前提下，把本地可重复流程推进到更可信的跨层治理与更低漂移维护；当前已在 canonical 层完成最薄入口草案与回指规则草案，下一阶段应保持“不直接实现真实 runtime pack / 不进入 rollout”的硬边界，并在需要时再做受控模板提案。

## Capabilities

- Layered capability system: canonical skills、distribution adapters、governance checks 与 tooling 仍保持清晰分层，没有重新混成单层仓库。
- Minimal canonical workflow expression: 仓库现在已经具备 `Copilot 主控 / Codex 施工` 默认链路的最小 canonical 表达，并且把 `planner / implementer / reviewer` 作为默认的最小角色分工写入 canonical skill。
- Workflow-shell coordination: `workflow-bootstrap` 现在能够把 workflow 壳层、bounded execution 协同方式，以及 `chatgpt-handoff-pilot` 的协议层职责区分开来，减少“谁负责链路、谁负责 handoff 协议”的歧义。
- Canonical-to-runtime-pack mapping: 仓库现在已经把 future runtime pack 的最小文件族作为 canonical 文档化目标表达清楚，但仍明确停留在 mapping / manifest 层，而不是当前仓库的已实现层。
- Thin-entry draft set (Phase 2): `workflow-bootstrap` 已新增 `AGENTS.md` 薄主入口草案、`.github/copilot-instructions.md` 薄适配草案、以及 canonical backreference rules 草案，并在 execution report 中记录“仅 canonical drafts、未实现 project-side runtime pack、未进入 rollout/distribution/template pack”。
- Workspace-aware status refresh: `update-project-status` 现在可以基于 `git`、`workspace` 或 `hybrid` 信号刷新状态，并明确 `primary status doc`、snapshot 与 truth precedence 这类 SSOT-lite 角色。
- Derivative-surface auditing: 仓库现在能只读检查 bridge / metadata 这类派生面的语义漂移，而不把 mirror surface 提升为新的 active source。
- Invocation metadata resilience: invocation example extraction 已经适配 example-file layout，降低了 metadata build 与 discovery surface 因布局差异产生的抽取漂移。
- Bridge continuity: handoff/status 的 bridge-facing mirror 现在可以按语义刷新，并保持 active source 与 continuity copy 的边界明确。
- Local-first validation: 系统仍以本地入口和脚本化检查为主，但这些入口已经足够支持 status、metadata、adapter、mirror 等关键维护面上的重复执行。
- Wrapper coordination baseline: `system-status-update` 与 `system-handoff` 现在具备最小联动规则（14 天 freshness gate、status 先于 handoff、handoff phase consistency 检查），用于降低双文档口径漂移。

## Stability

- Overall maturity: `evolving`
- Stable: canonical ownership、wrapper-only system skills、active-source documentation ownership、hub-vs-consumer contract separation，以及“`skills/` 是唯一 canonical source、`.agents/.github` 是 adapter / discoverability layer、bridge 是 continuity / mirror layer”的基本边界表达。
- Evolving: distribution freshness、derivative-surface governance、workspace-aware status refresh ergonomics、metadata/discovery robustness，以及 workflow shell 到 project-side runtime pack 的衔接判断。
- Not yet stable: CI-backed enforcement、automatic mirror consistency、automatic governance-mode detection、deterministic orchestration，以及真正的 project-side runtime pack 实现；当前仍没有落地 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 这一组项目侧入口文件。
- Evidence boundary: 本次刷新结合了当前 working tree、新增的 `workflow-bootstrap` 资产、`SKILLS_INDEX.md` 的 discoverability 更新，以及 execution report 中记录的实际验证结果；`skills_index.json` 未刷新这一点被视为有意 deferred，而不是遗漏事实。
- Freshness gate: `Updated at` 已通过 14 天时效门槛检查（当前年龄 0 天），本次无需新增 `Staleness` 风险项。

## Recommended Next Steps

- 在保持 canonical-only 边界的前提下，评估是否需要进入“受控 project-side 模板提案”阶段；若未授权，则继续停留在薄入口草案层。
- 不直接铺开 `.github/instructions/*.instructions.md` 或 `.github/agents/*.agent.md` 模板集合，避免把 canonical workflow mapping 过早升级为 project-side 模板面。
- 继续保持 `workflow-bootstrap` 的 workflow-shell 定位，让它与 `chatgpt-handoff-pilot`、`project-takeover`、`update-project-status`、`documentation-governance`、`file-structure-check` 的边界维持清晰，而不是把它扩张为新的控制层。
