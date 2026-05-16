# Documentation SSOT and Staleness Audit (P2-preflight)

## 1. Executive Summary

- 本轮为 **audit-only** 文档治理审计，未执行文档修复、重构、迁移、删除或重命名。
- `skills/` 作为 canonical skill source 的边界总体清晰；`.agents/` 与 `.github/skills/` 多数保持 wrapper/adapter 定位。
- `docs/HANDOFF.md` 与 `docs/status/skill-hub-status.md` 已被多处声明为 active current-state surfaces，但根目录部分文档仍包含易变状态事实摘要，存在复制与漂移风险。
- 发现的高优先级风险以 **SSOT 边界弱化与 stale 可能性** 为主，暂未发现“同一硬事实直接自相矛盾”的明确冲突证据。
- 建议进入后续修复轮（targeted），优先做根目录入口降噪与状态引用收口，而非大范围重写。

## 2. Scope and Method

### 扫描范围

- Root docs: `README.md`, `AI_USAGE.md`, `SKILLS_INDEX.md`, `CHANGELOG.md`, `SYNC.md`, `AGENTS.md`。
- Core docs: `docs/**/*.md`。
- Skill docs: `skills/**/*.md`。
- Adapter docs: `.agents/**/*.md`, `.github/**/*.md`。
- Supporting surfaces (read-only): `tools/**/*.py`, `tools/**/*.ps1`, `tests/**/*.py`（只用于一致性判断）。

### 扫描命令（只读）

- `git branch --show-current`
- `git status --short`
- `git log --oneline -8`
- `rg --files`
- `rg --files | rg "(\.md$|\.txt$|\.yaml$|\.yml$|\.json$|\.ps1$|\.py$)"`
- `rg --files | rg "^(README.md|AI_USAGE.md|SKILLS_INDEX.md|CHANGELOG.md|SYNC.md|AGENTS.md|CLAUDE.md)$"`
- `rg --files docs | rg "\.md$"`
- `rg --files skills | rg "\.md$"`
- `rg --files .agents .github 2>/dev/null || true`
- `rg "SSOT|single source|canonical|handoff|status|bridge|archive|deprecated|stale|historical|mirror|source of truth|current status|phase|next phase|todo|pending" README.md AI_USAGE.md SKILLS_INDEX.md CHANGELOG.md SYNC.md docs skills .agents .github`
- `rg "workflow-bootstrap|chatgpt-handoff-pilot|system-takeover|project-takeover|shared assessment|skill_assessment_output|documentation-governance" README.md AI_USAGE.md SKILLS_INDEX.md CHANGELOG.md SYNC.md docs skills .agents .github`

### Not verified / 限制

- 未逐行校验所有历史 task/review 文档中的每个时间点事实真值，仅做 SSOT/权威层级与 stale 风险审计。
- `archive/` 根目录不存在（本仓当前未发现）；因此对 archive 判定主要依据 `docs/reviews/`、`tasks/` 的 evidence 属性。

## 3. Authority Matrix

| Category | Definition | Likely Paths | Expected Update Behavior | May Contain Current-State Facts | Risk if Stale |
|---|---|---|---|---|---|
| active_ssot | 该主题的主事实源 | `skills/**/SKILL.md`, `skills/_protocol/*.md`, `docs/HANDOFF.md`（handoff） | 持续增量更新，保持边界声明 | 可以（但应限定在职责范围） | 高 |
| active_index_or_router | 索引/入口/路由，不承载主事实 | `SKILLS_INDEX.md`, `AI_USAGE.md`, `.agents/skills/README.md` | 低频更新，随结构变化 | 少量，可引用不复制 | 中 |
| active_guidance | 当前可执行指导，但非最终协议源 | `README.md`, `docs/ai/*.md`, `docs/human/*.md`, `docs/governance/*.md` | 周期更新 | 可有摘要，但应指向 SSOT | 中-高 |
| project_or_repo_status_surface | 当前状态面 | `docs/status/skill-hub-status.md`, `docs/HANDOFF.md` | 高频/按轮次更新 | 是（核心职责） | 高 |
| evidence_trail | 审计/评审/执行证据链 | `docs/reviews/*.md`, `tasks/*execution_report*.md`, `tasks/*task_package*.md` | 追加，不回写为现态 | 可包含“当时状态” | 中（被误当现态时高） |
| design_or_blueprint | 设计草案/蓝图 | `docs/design/*.md`, `skills/*/*sketch*.md`, `*draft*.md` | 按阶段演化 | 可以含阶段假设 | 中 |
| mirror_or_bridge | mirror/exchange 层 | `docs/bridge/**` | 与上游同步，标注 mirror | 不应作为 canonical current-state | 高 |
| adapter_or_wrapper | 薄适配层 | `.agents/skills/**`, `.github/skills/**`, `.github/copilot-instructions.md` | 保持薄层，路径回指 | 不应复制可变事实 | 高 |
| historical_or_archive | 历史资料 | 语义上 `docs/reviews/`, `tasks/`；显式 archive 若未来出现 | 只追加不“复活”为现态 | 可保留历史事实 | 中 |
| generated_or_derived | 生成/导出/兼容产物 | bridge templates、工具生成的索引/元数据 | 可再生成 | 不应新增规则 | 中 |
| unknown_or_needs_human_decision | 角色混杂、需维护者定性 | 根目录长文档中的状态叙述块 | 人工决策后收口 | 可能有 | 中-高 |

## 4. Root Docs Audit

### `README.md`
- current_role: 仓库总入口 + 结构说明 + 运行建议。
- likely_authority_level: active_guidance / onboarding。
- stale_risk: **medium-high**。
- evidence:
  - confirmed: 明确声明 `skills/` canonical、adapter 分层、工具入口。
  - inferred: 含较多“当前能力状态”描述，可能随阶段变化滞后。
  - pending: 未逐条核对与最新 status 的每个细粒度事实一致性。
- possible_conflicts: 与 `docs/status/skill-hub-status.md`、`docs/HANDOFF.md` 可能出现“当前状态”重复。
- recommended_action: `convert_to_index` + `point_to_ssot`。

### `AI_USAGE.md`
- current_role: compatibility entry / quick router。
- likely_authority_level: active_index_or_router。
- stale_risk: **low-medium**。
- evidence:
  - confirmed: 文件内显式声明非 canonical rule source。
  - inferred: 若下游 canonical path 变动，可能出现链接漂移。
  - pending: 未验证全部外部消费者是否依赖旧路径。
- possible_conflicts: 低；主要是链接老化风险。
- recommended_action: `keep_as_is`。

### `SKILLS_INDEX.md`
- current_role: cross-AI skill index + invocation overview。
- likely_authority_level: active_index_or_router。
- stale_risk: **medium**。
- evidence:
  - confirmed: 声明 canonical 在 `skills/`，自身为索引。
  - inferred: 每新增/调整 skill 后需要同步更新，易发生目录对齐滞后。
  - pending: 未逐条验证表内每项与 wrapper 文件实时一致。
- possible_conflicts: 与 `.agents/skills/skills_index.md`、`.github/skills/*` 的索引信息漂移。
- recommended_action: `keep_as_is` + `update_short_notice`（后续可加“状态事实请看 status/handoff”短提示）。

### `CHANGELOG.md`
- current_role: 变更记录入口。
- likely_authority_level: historical_or_archive（轻量）。
- stale_risk: **high**（当前仅少量早期条目）。
- evidence:
  - confirmed: 内容较短且未覆盖近期大量迭代。
  - inferred: 可能不再作为实际变更主线。
  - pending: 未确认是否仍被维护流程使用。
- possible_conflicts: 与 git history、tasks execution reports 的时间线不一致感。
- recommended_action: `add_stale_notice` 或 `archive_candidate`（需人工决策）。

### `SYNC.md`
- current_role: 双机同步操作指南。
- likely_authority_level: active_guidance（操作层）。
- stale_risk: **medium**。
- evidence:
  - confirmed: 提供 bundle 同步流程，偏稳定。
  - inferred: 若主协作方式变化，此文可能与实际流程偏离。
  - pending: 未验证是否仍为主要同步通道。
- possible_conflicts: 与当前 Git 工作流工具链实践差异。
- recommended_action: `keep_as_is`。

### `AGENTS.md`
- current_role: project-side runtime master entrypoint（thin dispatch）。
- likely_authority_level: active_index_or_router（高优先入口但非 canonical body）。
- stale_risk: **low**。
- evidence:
  - confirmed: 明确“not canonical source-of-truth”且回指 canonical 文件。
  - inferred: 若引用路径未来迁移需同步。
  - pending: 无。
- possible_conflicts: 低。
- recommended_action: `keep_as_is`。

## 5. docs/ Directory Audit

### `docs/HANDOFF.md`
- role: handoff 主事实面。
- authority level: project_or_repo_status_surface（active_ssot 子类）。
- staleness/drift risk: medium（体量大，长期追加易混入历史段落）。
- current-state facts appropriateness: 高（应在此承载）。
- treatment: active。
- recommended next action: 后续可做 targeted cleanup（分区“current”与“history”可读性增强）。

### `docs/status/`
- role: 状态追踪面。
- authority level: project_or_repo_status_surface。
- risk: medium（若更新频率下降会快速过时）。
- current-state facts appropriateness: 高（应集中在这里）。
- treatment: active。
- recommended next action: `point_to_ssot` from root/docs index files.

### `docs/reviews/`
- role: review evidence trail。
- authority level: evidence_trail。
- risk: medium-high（被误读为 current state）。
- current-state facts appropriateness: 仅限“当时判断”。
- treatment: historical/evidence。
- recommended next action: `add_stale_notice`（目录级或模板级，标注历史审计语义）。

### `docs/design/`
- role: design/blueprint/draft。
- authority level: design_or_blueprint。
- risk: medium（draft 与 active guidance 可能错位）。
- current-state facts appropriateness: 低-中（可含假设，不宜当现态）。
- treatment: active design + historical mix。
- recommended next action: `update_short_notice`（标注 draft/active plan 状态）。

### `docs/bridge/`
- role: mirror/exchange 层。
- authority level: mirror_or_bridge。
- risk: high（若被当 canonical 会产生边界冲突）。
- current-state facts appropriateness: 低（仅镜像/交换）。
- treatment: mirror。
- recommended next action: `add_stale_notice` 或显式 mirror banner（后续修复轮）。

### `docs/ai/`
- role: AI-facing 协议与调用指导。
- authority level: active_guidance（协议说明面）。
- risk: medium（与 skills canonical 规则重复风险）。
- current-state facts appropriateness: 中（应偏稳定协议，少放易变状态）。
- treatment: active guidance。
- recommended next action: 检查是否复制 status facts，倾向 `point_to_ssot`。

### `docs/governance/`
- role: 仓库治理规则文档。
- authority level: active_guidance。
- risk: low-medium。
- current-state facts appropriateness: 中（规则可有，状态应少）。
- treatment: active。
- recommended next action: `keep_as_is`。

### `docs/human/`
- role: 人类读者解释层与导航。
- authority level: active_guidance/onboarding。
- risk: medium（解释层复制现态风险）。
- current-state facts appropriateness: 低-中（宜短引用）。
- treatment: active guidance。
- recommended next action: `convert_to_index` for mutable facts。

### `docs/architecture` 或 archive
- 未发现 `docs/architecture/` 主目录；发现 `docs/DOCUMENTATION_ARCHITECTURE.md`（单文件）与 `docs/design/` 并行。
- 根目录未发现 `archive/`；`docs/reviews/` 与 `tasks/` 实际承担历史证据层角色。

## 6. Skill Docs and Adapter Audit

### `skills/**/*.md`
- 判断：整体符合 canonical source 定位。
- 风险点：部分 README/examples 包含阶段性叙述（历史上下文），若被外部当“当前状态”读取可能误判。
- 结论：保留现状，后续仅做必要的 stale/context 标注，不改变 ownership。

### `.agents/**/*.md`
- 判断：多数为 wrapper，显式要求回读 canonical path。
- 风险点：存在 wrapper + flat entries + skills_index 多层镜像，存在同步漂移可能。
- 结论：边界总体清晰，但需要定期一致性检查（future candidate，不在本轮实施）。

### `.github/**/*.md`
- 判断：以 Copilot adapter 为主，`.github/copilot-instructions.md` 保持 thin。
- 风险点：`.github/skills/*.md` 与 canonical 目录关系需持续对齐。
- 结论：未发现其“升级为第二规则库”的明确证据。

### ownership boundary 专项结论
- `workflow-bootstrap` vs `chatgpt-handoff-pilot`：当前文档多数保持壳层/协议边界，未见明显倒置。
- shared assessment protocol：多数文档将其定位为 output vocabulary；未见其被写成 controller/validator 的强证据。

## 7. SSOT Conflict and Staleness Findings

- finding_id: F-001
- title: Root entry docs may over-carry mutable current-state facts
- capability_fit: documentation-governance / SSOT boundary audit
- evidence:
  - confirmed: `README.md` 含大量“当前能力/状态”叙述；`docs/HANDOFF.md` 与 `docs/status/` 已是明确状态面。
  - inferred: 若不收口，根入口与状态面会出现时间漂移。
  - pending: 尚未逐段比较每条状态是否已过期。
- inference: 需要把 root docs 更明确定位为入口/索引，减少可变事实复制。
- open_questions: 是否要求 README 仅保留极简状态摘要（需维护者定）。
- risk_priority: P1
- impact_scope: root docs, onboarding accuracy
- affected_paths: `README.md`, `docs/HANDOFF.md`, `docs/status/skill-hub-status.md`
- recommended_action: convert root mutable status blocks to short pointer-to-SSOT notices
- suggested_follow_up_phase: P1 targeted root-docs cleanup

- finding_id: F-002
- title: Bridge layer boundary can be misread as active source
- capability_fit: mirror/boundary governance
- evidence:
  - confirmed: `docs/bridge/` 包含 `HANDOFF.md`, `status/skill-hub-status.md`, `SKILLS_INDEX.md` 等高敏感命名镜像。
  - inferred: 即使当前语义是 mirror，命名层面仍可能被误解为 active counterpart。
  - pending: 尚未统一审阅 bridge 每页顶部是否有足够 mirror notice。
- inference: 需要更强可见的 mirror/non-canonical 标记策略。
- open_questions: 是否在 bridge 全层增加统一 banner（人工决策）。
- risk_priority: P0
- impact_scope: boundary clarity, cross-layer ownership
- affected_paths: `docs/bridge/**`
- recommended_action: add explicit mirror notices + canonical pointer
- suggested_follow_up_phase: P0 bridge/mirror cleanup

- finding_id: F-003
- title: Evidence documents may be treated as current-state references
- capability_fit: evidence-trail governance
- evidence:
  - confirmed: `docs/reviews/`、`tasks/` 存在大量 phase/task 结果文档。
  - inferred: 无显式“historical evidence”标记时，后续读者可能引用过期结论。
  - pending: 未统计全部文档是否带日期/phase disclaimer。
- inference: 应强化 evidence 文档“历史性”定位。
- open_questions: 是否采用目录 README 声明而非逐文件改动。
- risk_priority: P1
- impact_scope: review interpretation, planning inputs
- affected_paths: `docs/reviews/**`, `tasks/**`
- recommended_action: historical-reference labeling strategy
- suggested_follow_up_phase: P1 docs review/task evidence labeling cleanup

- finding_id: F-004
- title: CHANGELOG appears under-maintained relative to repository activity
- capability_fit: staleness detection
- evidence:
  - confirmed: `CHANGELOG.md` 内容与近期高频迭代不匹配。
  - inferred: 可能已经被 `tasks`/git log 取代。
  - pending: 未确认 maintainer 是否仍计划维护 changelog。
- inference: 若不维护，应显式声明其定位，避免误导。
- open_questions: 保留但降级，还是改为历史说明。
- risk_priority: P1
- impact_scope: release/history discoverability
- affected_paths: `CHANGELOG.md`
- recommended_action: add stale notice or archive candidate decision
- suggested_follow_up_phase: P1 root docs cleanup

## 8. Recommended Remediation Plan

> 本节仅给后续建议，本轮不执行修复。

### P0 follow-up candidates
- bridge/mirror 边界显式化：避免 `docs/bridge/` 被误读为 active SSOT。
- 明确高敏感命名镜像（HANDOFF/status/index）的 canonical pointer 规则。

### P1 follow-up candidates
- Root docs 去状态复制：`README.md` 将 mutable current-state 内容缩减为短引用并指向 `docs/HANDOFF.md` 与 `docs/status/`。
- `CHANGELOG.md` 定位决策：维护、降级、或历史化说明。
- `docs/reviews/` 与 `tasks/` 增加“historical evidence”目录级提示策略。

### P2 follow-up candidates
- 文档 stale marker 批量化策略（仅候选，不落地）。
- validator/CI/automation 的可行性评估（默认 deferred）。
- metadata extraction 驱动的“status-fact duplication detector”探索（future candidate only）。

## 9. Explicit Non-actions

- 本轮未修改任何现有文档内容。
- 本轮未修复 stale docs。
- 本轮未新增 automation / validator / CI。
- 本轮未调整 canonical/adapter/bridge ownership boundary。

## 10. Final Recommendation

**Proceed to multi-phase documentation SSOT remediation**.

