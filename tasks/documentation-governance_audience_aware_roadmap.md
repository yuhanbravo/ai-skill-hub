# documentation-governance Audience-Aware Roadmap

## 1. Background
本路线图用于增强 `skills/documentation-governance` 的治理能力，目标是在**不破坏现有审计主线**（`audit -> report -> fix(optional)`）的前提下，引入更清晰的人机受众（audience）与文档治理维度。  
本计划为规划文档（plan-only），不在本 PR 中修改 skill 行为、脚本、测试或现有治理逻辑。

## 2. Current Skill Baseline
当前 skill 已具备的能力（作为本路线图前提）包括：
- `docs/` 与 `docs_readable/` 的 engineering/readable 治理
- README 治理
- 重复主题（duplicate topic）检查
- mutable status SSOT 检查

本路线图仅定义后续增强回合（rounds）、验证预期与非目标，不改变上述已存在能力。

## 3. Design Decision: Keep audience independent from layer
核心设计决策：`audience` 与 `document_layer` 保持独立维度，不互相覆盖。
- `document_layer` 继续回答“文档处于什么层次/目录角色”
- `audience` 回答“文档主要服务于谁（human/AI/shared）”

这样可避免“目录结构推断受众”的强绑定错误，并支持同一层中存在不同 audience 的现实场景。

## 4. Round 1 — Built-in Governance Model
> **优先级最高，必须先于 Round 2 执行完成。**

### 4.1 新增内置分类维度（内建，不依赖外部工具）
1) `audience`（独立维度）
- `human_machine_shared`
- `human_primary_archive`
- `ai_only_wrapper`
- `unknown_or_mixed`

2) `authority_role`
- `current_status_ssot`
- `handoff_ssot`
- `navigation_index`
- `stable_reference`
- `script_map`
- `migration_blueprint`
- `decision_record`
- `archive_reference`
- `agent_wrapper`
- `derived_summary`

3) `doc_intent`（受 Diátaxis 启发，但**不强制目录布局**）
- `navigation`
- `status`
- `handoff`
- `how_to`
- `reference`
- `explanation`
- `decision_record`
- `archive`
- `agent_instruction`

### 4.2 新增内置冲突检查
- `ai_only_doc_carries_business_ssot`
- `shared_doc_contains_agent_only_instruction`
- `archive_referenced_as_current_fact`
- `navigation_doc_duplicates_mutable_status`
- `language_mismatch_for_shared_doc`

### 4.3 报告字段扩展（内置输出）
- `audience_classification`
- `ai_only_docs`
- `human_primary_docs`
- `shared_docs`
- `audience_conflicts`
- `language_findings`

### 4.4 Round 1 验证预期
- Round 1 实施前置（task package）阶段不引入 Round 2 工具（`markdownlint` / `lychee` / `Vale` / `textlint`）。
- 分类可在典型项目文档集中稳定落地（非空、可解释、可复核）
- 冲突检查可输出明确命中项与上下文证据
- 报告字段可与现有 report 结构共存，不破坏既有消费者
- `audit -> report -> fix(optional)` 流程保持不变

## 5. Round 2 — Optional External Checkers
> **仅在 Round 1 完成并稳定后启动。**

### 5.1 可选集成点（默认关闭）
- `markdownlint`
- `lychee`
- `Vale`
- `textlint`

### 5.2 集成原则
- 全部 external checkers 必须可选（opt-in）
- 默认禁用（disabled by default）
- 不得成为 core documentation-governance 的前置依赖
- 缺少外部工具时，核心审计仍可完整执行

### 5.3 未来报告字段（外部检查维度）
- `format_findings`
- `link_findings`
- `style_findings`
- `terminology_findings`

### 5.4 Round 2 验证预期
- 在未安装外部工具时，核心治理行为与 Round 1 等价
- 在开启单个/多个外部工具时，结果可分层归档到新增字段
- 外部工具失败或缺失不导致核心治理失败（只降级可选输出）

## 6. Round 3 — Project-Level Governance Recommendations
在不改变核心治理判定边界的前提下，生成“建议型（advisory）”输出：
- 项目是否需要 `AGENTS.md`
- 是否需要 ADR / decision records
- `README.md` 与 `docs/README.md` 是否保持 navigation-only
- `docs/status.md` 与 `docs/HANDOFF.md` 是否正确承担 SSOT 角色
- `docs/archive/**` 是否被错误当作 current fact 引用
- shared docs 是否应采用 Chinese-first prose，并保留 English technical terms

### Round 3 验证预期
- 建议项与“强规则判定”分离，不误报为硬阻断
- 建议项可追溯到 Round 1 的分类/冲突证据
- 建议输出适用于不同项目，不硬编码单一项目路径与名称

## 7. Dogfood Scenario: AMS_Report Read-Only Audit
本场景用于验证路线图可用性，不作为硬编码特例。

### 7.1 场景假设（仅作为审计样本）
- 项目为中文业务语境、脚本风格的财务报告工作区
- 计划进行 read-only audit
- 预期 SSOT：
  - `docs/status.md` = mutable project status SSOT
  - `docs/HANDOFF.md` = handoff context / operating boundaries SSOT
  - `README.md` 与 `docs/README.md` = navigation only
  - `docs/archive/**` = historical / human-primary archive
- 当前未观察到 `AGENTS.md` / `CLAUDE.md` / `.agents`，但需本地扫描确认
- shared docs 倾向中文优先，保留英文技术术语

### 7.2 适配约束
- 不将 AMS_Report 规则写死到核心逻辑
- 通过配置或项目上下文输入表达偏好
- 保持跨项目复用能力

## 8. Validation Plan
按 round 分层验证：

1) Round 1（内置模型）
- 覆盖分类正确性、冲突命中质量、报告字段兼容性
- 重点验证“受众维度独立于层级维度”

2) Round 2（可选外部检查）
- 覆盖“默认关闭/按需开启/工具缺失降级”三种模式
- 验证核心审计不被外部依赖阻断

3) Round 3（项目级建议）
- 覆盖建议可解释性与非阻断性
- 验证建议可追溯、可关闭、可按项目偏好调整

统一验收要求：
- 明确每轮输入、输出、失败模式、降级策略
- 保持 `audit -> report -> fix(optional)` 不变

## 9. Non-Goals
以下内容不在本路线图实施范围内：
- 在本 PR 中修改 `documentation-governance` 现有行为
- 在本 PR 中新增/修改脚本与测试
- 强制 Diátaxis 目录结构迁移
- 将外部 lint/link/style 工具设为强依赖
- 把单一 dogfood 项目（如 AMS_Report）硬编码为默认规则

## 10. Open Questions
1. `audience` 与 `authority_role` 的冲突优先级如何定义（告警级别矩阵）？
2. `language_mismatch_for_shared_doc` 是否需要项目级 language policy 配置文件？
3. Round 2 外部工具输出的统一 schema 是否需要版本号（例如 `report_schema_version`）？
4. Round 3 建议项是否需要“建议强度分级”（info/suggest/recommend）？
5. 对历史项目的回溯审计，是否需要单独的“legacy tolerance”开关？
6. 同主题 task package 的 supersede/merge 规则是否需要模板化字段（如 package_id / supersedes）？
