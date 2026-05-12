# Title
P0 Shared Assessment Output Protocol

## Background
本任务包来源于一次全库 canonical skills 的只读扫描结果。扫描结论显示当前 skills 体系整体可用，短板并不集中在某一个 skill 的能力缺失，而在于 assessment / review / takeover 相关输出缺少统一口径，导致跨技能结果在评分、证据、推断、风险分级与影响范围上不够一致。

因此本轮定位为 **P0 横向增强**：通过新增共享 assessment output protocol，最小接入到关键技能，并在其他相关技能中做薄引用或场景化引用，以提升结果的可判定性、可审计性与可比较性。

本轮不是单个 skill 重构轮，不进行自动化体系扩展。

## Objective
本轮实施目标限定为：

1. 新增共享协议文件：`skills/_protocol/skill_assessment_output.md`。
2. 让核心 assessment / takeover / governance 类 skill 最小接入共享协议。
3. 让其他相关 skill 做薄引用或场景化引用，不扩大改造面。
4. 提高输出的可判定性（decidable）、可审计性（auditable）、可比较性（comparable）。

## Authorized Files
> 说明：以下为**后续 implementation 轮次**的授权范围，不代表本轮（task package drafting）可修改。

- `skills/_protocol/skill_assessment_output.md`
- `skills/system-takeover/SKILL.md`
- `skills/project-takeover/SKILL.md`
- `skills/skill-governance/SKILL.md`
- `skills/documentation-governance/SKILL.md`
- `skills/file-structure-check/SKILL.md`
- `skills/financial-data-project-migration/SKILL.md`
- `skills/chatgpt-handoff-pilot/SKILL.md`
- `skills/system-status-update/SKILL.md`
- `skills/system-handoff/SKILL.md`
- `skills/update-project-status/SKILL.md`
- `skills/workflow-bootstrap/SKILL.md`
- `tasks/p0_shared_assessment_output_protocol_execution_report.md`

## Out of Scope
本轮明确排除以下事项：

- 不新增 tools / scripts。
- 不新增 tests。
- 不接入 CI。
- 不修改 router / pipeline。
- 不修改 `.agents` / `.github` adapters。
- 不修改 `docs/HANDOFF.md` 或 `docs/status`。
- 不重写任何 skill 主体。
- 不改变 `workflow-bootstrap` 与 `chatgpt-handoff-pilot` 的 ownership boundary。
- 不把 `maturity_score` 强制应用到所有 skill。
- 不引入 auto-fix / auto-remediation / deterministic orchestration 叙事。

## Proposed Implementation Plan

### Step 1: 新增共享协议文件
创建 `skills/_protocol/skill_assessment_output.md`，定义统一 assessment output protocol 的字段、适用范围与裁剪规则。

### Step 2: 核心三类 skill 接入
对以下核心 skill 做最小接入：
- `skills/system-takeover/SKILL.md`
- `skills/project-takeover/SKILL.md`
- `skills/skill-governance/SKILL.md`

要求其 assessment/review/takeover 输出明确引用共享协议，并使用核心字段。

### Step 3: 其他相关 skill 薄引用
对以下 skill 做薄引用或场景化引用，不做主体改写：
- `documentation-governance`
- `file-structure-check`
- `financial-data-project-migration`
- `system-status-update`
- `system-handoff`
- `update-project-status`
- `chatgpt-handoff-pilot`
- `workflow-bootstrap`

### Step 4: 生成 execution report
完成后输出 `tasks/p0_shared_assessment_output_protocol_execution_report.md`，记录 changed / unchanged / deferred 与边界遵守情况。

### Step 5: 只读检查与 final boundary review
在提交前执行只读与差异检查，确认无越权改动、无范围外扩展。

## Protocol Content Requirements
`skills/_protocol/skill_assessment_output.md` 必须定义以下字段：

- `capability_fit`
- `maturity_score`（only when applicable）
- `evidence`
- `inference`
- `open_questions`
- `risk_priority`
- `impact_scope`
- `next_action`

### maturity_score 标尺（建议 1–5）
- 1: only conceptual
- 2: usable but output varies by executor
- 3: stable steps and output structure
- 4: evidence / risk / fallback rules included
- 5: supported by automated or strong validation

必须明确声明：
- P0 目标不是把所有 skill 提升到 5。
- `maturity_score` 为 optional / where applicable。
- status / handoff 类 skill 不应被强制打分。

### evidence 分类
`evidence` 必须区分：
- `confirmed`
- `inferred`
- `pending`

### risk_priority 分类
- `P0`: affects repeatability, auditability, or safe use
- `P1`: affects workflow linkage, consistency, or usability
- `P2`: automation, CI, scripts, or long-term maintainability

### impact_scope 分类
- `local`
- `layer`
- `system`

## Per-skill Guidance

### Core takeover/governance skills
`system-takeover` / `project-takeover` / `skill-governance`：
- 必须明确引用 shared assessment output protocol。
- 在 assessment/review/takeover 输出中使用：`maturity_score`、`evidence`、`inference`、`open_questions`、`risk_priority`、`impact_scope`、`next_action`。

### Audit / migration skills
`documentation-governance` / `file-structure-check` / `financial-data-project-migration`：
- 应引用协议。
- 允许按场景裁剪评分项，不强制所有字段满配。

### Status / handoff skills
`system-status-update` / `system-handoff` / `update-project-status`：
- 只接入 `evidence` / `risk` / `open_questions` / `phase or freshness risk` 口径。
- 不强制 `maturity_score`。

### chatgpt-handoff-pilot
- 仅补 execution report 的风险分级与 evidence awareness。
- 不重定义 task package / bounded execution / execution report 协议。

### workflow-bootstrap
- 仅补 assessment output 与 handoff-status 的衔接意识。
- 不重新定义 `chatgpt-handoff-pilot` 已拥有的协议。

## Acceptance Criteria
满足以下条件方可验收：

1. 新增共享协议文件 `skills/_protocol/skill_assessment_output.md`。
2. 核心三 skill（system-takeover / project-takeover / skill-governance）明确接入共享协议。
3. 其他相关 skill 仅做薄引用或场景化引用，无主体重写。
4. 没有新增 automation / CI / validators。
5. 没有修改 router / pipeline。
6. 没有重写 skill 主体。
7. 没有改变 canonical / adapter / protocol ownership boundary。
8. execution report 能清楚记录 changed / unchanged / deferred items。

## Validation Plan
后续 implementation 至少执行以下检查：

- `git diff -- skills/_protocol skills tasks`
- `git status --short`
- `rg "skill_assessment_output" skills`
- `rg "maturity_score|risk_priority|impact_scope|open_questions" skills/_protocol skills`
- 只读检查是否误改：`tools/`、`tests/`、router/pipeline 相关路径、`docs/HANDOFF.md`、`docs/status/`

说明：本轮不要求新增测试。

## Expected Execution Report
后续 execution report 建议落盘：
- `tasks/p0_shared_assessment_output_protocol_execution_report.md`

建议包含章节：
1. Scope Restatement
2. Files Changed
3. What Changed
4. What Did Not Change
5. Validation Performed
6. Boundary Checks
7. Deferred P1/P2 Items
8. Recommended Commit Message

## Recommended Commit Message
`docs(skills): standardize assessment evidence and risk output`
