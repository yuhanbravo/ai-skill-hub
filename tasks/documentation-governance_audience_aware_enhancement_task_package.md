# 任务包：documentation-governance audience-aware enhancement（修正版，补齐 Catalog / Registry Dogfood）

> 状态：当前有效 task package（如后续出现同主题任务包，应在新包中显式声明 supersede/merge 关系）。

## 1. 任务目的
本任务包用于修正本轮出包记录，补齐 `Skill Catalog / Template Registry Dogfood` 必要证据。  
本轮是 **task package 修正**，不是 roadmap 重设计，不是 skill 本体施工。
本文件用于 Round 1 实施前置校正；真正 Round 1 施工应由后续 implementation task 执行。

## 2. 输入与引用
- `docs/SKILL_CATALOG.md`
- `docs/TEMPLATE_REGISTRY.md`
- `tasks/documentation-governance_audience_aware_roadmap.md`

## 3. 本轮范围（In Scope）
- 修正并明确记录本轮 dogfood check（Catalog / Registry / source-surface boundary）。
- 明确 primary skill 与 supporting skill 的选择依据。
- 给出后续施工流程提示（从审包到 execution report 再到 AI_Workbench 状态回填）。

## 4. 明确不做（Out of Scope）
- 不修改 `skills/documentation-governance` 本体。
- 不开始 Round 1 implementation。
- 不引入 Round 2 external checkers：`markdownlint`、`lychee`、`Vale`、`textlint`。
- 不配置或运行任何外部 lint/link/style/terminology 工具链。
- 不修改 `docs/SKILL_CATALOG.md`。
- 不修改 `docs/TEMPLATE_REGISTRY.md`。
- 不做 template migration。
- 不做 adapter sync。
- 不做 bridge refresh。
- 不做 validator / CI / automation。
- 不做 historical task candidate promotion。
- 不扫描或修改 AMS_Report。

## 5. Catalog / Registry Dogfood Check

### 5.1 Catalog / Registry 查阅情况
- `docs/SKILL_CATALOG.md`: **checked**
  - 结论：`skills/documentation-governance/` 与本轮“文档治理模型增强”目标直接匹配；`workflow-bootstrap`、`chatgpt-handoff-pilot` 属于流程/交接支撑，不替代文档治理主责。
- `docs/TEMPLATE_REGISTRY.md`: **checked**
  - 结论：已检索模板索引，但未发现可直接覆盖“audience-aware enhancement task package 修正”的现成模板；可复用内容主要是通用 task package / execution report 组织方式，仍需本轮按场景落地。

### 5.2 Skill 选择结果
- Primary skill：`documentation-governance`
- Supporting skill：
  - `chatgpt-handoff-pilot`（用于 task package -> bounded execution -> execution report 证据链）
  - `workflow-bootstrap`（用于 role split / workflow shell / execution boundary 约束理解）
- Near-skill / boundary risk：
  - 存在近义或易混技能：`workflow-bootstrap`、`chatgpt-handoff-pilot`
  - 本轮主 skill 不是 `workflow-bootstrap`：因为本轮核心是文档治理模型增强（audience/authority/intent/conflict/report fields），不是 workflow shell 设计。
  - 本轮主 skill 不是 `chatgpt-handoff-pilot`：因为其负责交接协议与执行回执结构，不拥有文档事实权威边界治理。
  - 边界结论：`documentation-governance` 负责文档事实权威边界；workflow/handoff skills 只负责流程壳层与交接结构。

### 5.3 Template / Registry 结果
- 可复用 template/snippet/prompt：**未发现可直接复用到本次“audience-aware enhancement package 修正”的精确资产**。
- 记录语句（强制保留）：
  - `No directly reusable template/snippet/prompt found for this exact audience-aware enhancement package.`
- 处理方式：仅记录 follow-up，不在本轮新增或迁移 template。

### 5.4 Source-surface 边界检查
| Check | Result | Note |
|---|---|---|
| skills/ canonical source | Pass | Authoring target remains `skills/documentation-governance` for future implementation rounds. |
| adapter authoring avoided | Pass | No `.agents/.github` skills adapter used as canonical source. |
| bridge active-source avoided | Pass | Bridge docs are not treated as active source. |
| historical task promotion avoided | Pass | Historical tasks used only as reference, not promoted to canonical rules. |

补充说明：
- 本轮仅修正 task package 记录，不修改 adapter / bridge / historical task 作为 source。

### 5.5 Dogfood 结论
- Catalog/Registry 对本轮有帮助：
  - 降低了 primary skill 选择成本；
  - 明确了 supporting skill 的职责边界；
  - 降低了把 adapter / bridge / historical task 误当 canonical source 的风险。
- 暴露的 follow-up（只记录，不混改）：
  - 可补强 maintenance guidance（Catalog/Registry 更新节奏与责任人）。
  - 可补强 scenario index（按任务类型快速映射技能与模板）。
  - 可补强 candidate review（模板候选的纳入/淘汰标准）。
  - 可补强 reusable template coverage（面向 audience-aware enhancement 的专门 task package 模板）。

## 6. 建议流程（本轮修正版）
1. 先读 Catalog / Registry。
2. 判断本轮 primary skill 和 supporting skill。
3. 修正 task package。
4. 在 task package 内记录 dogfood check。
5. 审包。
6. 施工。
7. execution report 再记录 dogfood result。
8. PR final review。
9. 回到 AI_Workbench，把 pending_trigger 更新为 `dogfood_recorded / done`。
   - If the target project has no AI_Workbench / pending_trigger management entry, skip this step or record the dogfood state in the PR checklist, issue checklist, or execution report instead.

## 7. 验证要求
- 轻量检查：
  - `git diff --name-only`
  - `git diff -- tasks/documentation-governance_audience_aware_enhancement_task_package.md`
- 如无 markdown-only 强制约定，不额外运行测试。
