# 任务包：workflow-bootstrap Phase 2 Review Tier Guidance

## 任务标识

- task id: `WF-BOOTSTRAP-PHASE2-REVIEW-TIER-GUIDANCE-V1`
- 名称：workflow-bootstrap Phase 2 / Review Tier Guidance
- 阶段：`Phase 2`
- 提交方：Drafter
- 日期：`2026-04-29`
- 前置输入：
  - `skills/workflow-bootstrap/SKILL.md`
  - `skills/workflow-bootstrap/role_split_and_integration.md`
  - `skills/workflow-bootstrap/non_git_runtime_profile.md`
  - `skills/workflow-bootstrap/examples/invocation_examples.md`
  - `skills/chatgpt-handoff-pilot/SKILL.md`
  - `tasks/workflow-bootstrap_phase1_role_split_canonicalization_task_package.md`
  - `tasks/workflow-bootstrap_phase1_role_split_canonicalization_execution_report.md`

---

## Scope Restatement

本轮只为 `workflow-bootstrap` 的 Reviewer 角色补充一份 `review tier guidance` 任务包，供后续正式施工时新增分层审包 guidance：

```text
Light Review -> Standard Review -> Heavy Review
```

在 task-package generation 与 review 阶段，本轮只生成并审阅 task package，不直接施工 Phase 2，不修改任何 `workflow-bootstrap` skill 文件，也不新增 execution report。

只有在后续显式切换到 `Implementer` 角色后，本任务包才作为 Phase 2 bounded execution 的授权输入；届时 Implementer 只能创建或更新本任务包 `Authorized Files` 中列出的文件。

本轮任务包的目标是为后续 bounded execution 提供清晰授权边界，使实施侧能够在不重定义 `chatgpt-handoff-pilot` 协议的前提下，为 Reviewer 增加 advisory review strength guidance。

本轮应明确：

1. review tiers 只是 advisory guidance，不是 CI enforcement，不是 validator，不是 hard failure rule。
2. `workflow-bootstrap` 继续只负责 workflow shell / role split / runtime profile / review tier guidance。
3. task package / bounded execution / execution report 协议仍由 `chatgpt-handoff-pilot` 负责。
4. review tier guidance 不替代 Reviewer 的上下文判断，也不替代 `chatgpt-handoff-pilot` 的 bounded execution protocol。

---

## Background

Phase 0 已完成 non-git / low-git runtime profile absorption，建立了 `workflow-bootstrap` 对项目侧试跑环境的保守 runtime-profile guidance，并明确 `tasks/` 可作为 non-git / low-git 场景下的主要证据路径，但不是所有项目的强制路径。

Phase 1 已完成 role split canonicalization，将默认协作链路稳定抽象为：

```text
Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer
```

其中 `Reviewer` 已被明确定位为 bounded execution 前的 safety gate，用于在 implementation 之前审清 scope、authorized files、ownership boundary、acceptance criteria 和 out-of-scope 约束。

当前 Phase 2 的目标不是发明新的协议层，而是在既有 role split 基础上，为 Reviewer 提供更可操作的审包强度分层 guidance，使后续任务能根据改动类型和风险级别选择 `Light Review`、`Standard Review` 或 `Heavy Review`。

本轮必须维持以下边界：

- `workflow-bootstrap` 不拥有 handoff protocol。
- `chatgpt-handoff-pilot` 仍拥有 task package / bounded execution / execution report protocol。
- review tiers 只描述审包建议强度，不把审包写成自动强制机制。
- canonical skill 修改、跨项目规则、runtime pack design、automation / validator candidates 默认进入 `Heavy Review`；这些只是 review tier classification examples，不授权在 Phase 2 设计或实现 runtime pack、automation、validators、scripts、tests 或 CI。

---

## Target Files

优先目标文件：

- `skills/workflow-bootstrap/review_tiers.md`

允许做最小回指或示例补充的文件：

- `skills/workflow-bootstrap/SKILL.md`
- `skills/workflow-bootstrap/role_split_and_integration.md`
- `skills/workflow-bootstrap/examples/invocation_examples.md`

后续正式施工的执行回执推荐落点：

- `tasks/workflow-bootstrap_phase2_review_tier_guidance_execution_report.md`

本轮 task package 文件落点：

- `tasks/workflow-bootstrap_phase2_review_tier_guidance_task_package.md`

---

## Authorized Files

若后续进入 Phase 2 正式施工，本任务包仅授权修改以下文件：

- `skills/workflow-bootstrap/review_tiers.md`（优先新增）
- `skills/workflow-bootstrap/SKILL.md`（仅允许最小回指，不复制 `review_tiers.md` 正文）
- `skills/workflow-bootstrap/role_split_and_integration.md`（仅允许最小回指，不复制 `review_tiers.md` 正文）
- `skills/workflow-bootstrap/examples/invocation_examples.md`（仅允许增加最小示例或短提示，不复制 `review_tiers.md` 正文）
- `tasks/workflow-bootstrap_phase2_review_tier_guidance_execution_report.md`（正式施工完成后新增）

除上述路径外，默认无权修改其他文件或目录。

---

## Out of Scope

本轮及后续 Phase 2 正式施工均明确不做以下事项：

- 不修改 `chatgpt-handoff-pilot`。
- 不重定义 task package / bounded execution / execution report schema。
- 不新增 validator / scripts / tests / CI。
- 不把 review tiers 写成 hard enforcement。
- 不创建 `tool_adapters/`。
- 不进入 Phase 3 runtime pack minimal manifest。
- 不修改 `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`。
- 不新增 `.github/instructions/` 或 `.github/agents/`。
- 不把 `tasks/` 写成所有项目强制路径。
- 不修改 `README.md`、`docs/HANDOFF.md`、status surfaces 或其他未授权文件。
- 不把当前工具订阅差异、模型强弱或工具偏好写入 canonical guidance。
- 不复制 `review_tiers.md` 正文到 `SKILL.md`、`role_split_and_integration.md` 或 `examples/invocation_examples.md`。
- 不把 review tiers 写成可替代 Reviewer 上下文判断的简化决策树。

---

## Required Content

后续正式施工时，`skills/workflow-bootstrap/review_tiers.md` 至少应包含以下内容：

1. 定义三层 review tier：
   - `Light Review`
   - `Standard Review`
   - `Heavy Review`

2. 每个 tier 至少说明：
   - 中文定位
   - 适用场景
   - 核心检查项
   - 是否建议 second role / second tool review
   - 不适用场景
   - 典型例子

3. 明确 review tiers 只是 advisory guidance，不是 CI enforcement，不是 validator，不是 hard failure rule。

4. 明确 canonical skill 修改、跨项目规则、runtime pack design、automation / validator candidates 默认应进入 `Heavy Review`；这些只是分类示例，不授权在 Phase 2 设计或实现 runtime pack、automation、validators、scripts、tests 或 CI。

5. 明确 README 小更新、单文件非核心文档、索引更新等可进入 `Light Review`。

6. 明确 workflow supporting asset、project adapter、`AGENTS.md`、handoff/status 小更新等通常进入 `Standard Review`。

7. 明确 review tier guidance 不替代 Reviewer 的上下文判断，也不替代 `chatgpt-handoff-pilot` 的 task package / bounded execution / execution report 协议。

8. 明确 `workflow-bootstrap` 仍只定义 workflow shell / role split / runtime profile / review tier guidance，不拥有 handoff 协议。

9. 若 `SKILL.md`、`role_split_and_integration.md`、`examples/invocation_examples.md` 需要补充，只能做最小回指或短示例：
   - `SKILL.md` 只补 supporting asset 回指。
   - `role_split_and_integration.md` 只补 Reviewer 可参考 review tier guidance 的最小说明。
   - `examples/invocation_examples.md` 只补一个与 review tier selection 相关的短例。

---

## Acceptance Criteria

本轮 task package 及其后续正式施工必须满足以下条件：

1. `review_tiers.md` 的定位被明确写为 advisory guidance。
2. `Light Review`、`Standard Review`、`Heavy Review` 三层定义清楚且可操作。
3. `Heavy Review` 明确适用于 canonical skill 修改、跨项目规则、runtime pack design、automation / validator candidates，并明确这些只是分类示例，不构成 Phase 2 runtime pack、automation、validator、scripts、tests 或 CI 的设计或实现授权。
4. `Light` / `Standard` / `Heavy` 的适用边界不会鼓励跳过必要审包。
5. 未引入 CI、validator、scripts、tests 或 hard failure rule。
6. `workflow-bootstrap` / `chatgpt-handoff-pilot` ownership boundary 仍清楚。
7. `SKILL.md`、`role_split_and_integration.md`、`invocation_examples.md` 若被补充，只能做最小回指，不得复制 `review_tiers.md` 正文。
8. review tier guidance 被写成 Reviewer 的辅助判断层，而不是新的协议 owner、自动 gate 或替代 bounded execution 的规则层。

---

## Validation Plan

后续正式施工完成后，至少执行以下验证：

1. 检查是否新增或授权了 scripts/tests/CI/validator。
2. 检查是否把 review tiers 写成 mandatory enforcement。
3. 检查是否仍明确 `chatgpt-handoff-pilot` 是 task package / bounded execution / execution report protocol owner。
4. 检查是否没有进入 runtime pack manifest 或 tool adapter 设计。
5. 检查 `Authorized Files` 是否保持足够窄。
6. 检查 `Light Review` / `Standard Review` / `Heavy Review` 三层是否都有适用场景和不适用边界。
7. 检查 `Heavy Review` 是否覆盖 canonical skill 修改、跨项目规则、runtime pack design、automation / validator candidates，并确认这些内容只作为分类示例出现，没有授权 runtime pack、automation、validator、scripts、tests 或 CI 的设计或实现。
8. 检查 `Light Review` 是否覆盖 README 小更新、单文件非核心文档、索引更新等低风险变更。
9. 检查 `Standard Review` 是否覆盖 workflow supporting asset、project adapter、`AGENTS.md`、handoff/status 小更新等中等风险变更。
10. 检查最小补充文件是否只做回指或短例，没有复制 `review_tiers.md` 主体内容。
11. 检查 `review_tiers.md` 是否没有使用 `must fail`、`required gate`、`mandatory blocker` 或类似 hard-failure / enforcement-style wording。

若环境允许，可辅以最小文本检查；若无自动化验证，则至少在 execution report 中报告上述人工检查结果。

---

## Execution Report Requirement

若后续进入 Phase 2 正式施工，执行完成后必须新增：

- `tasks/workflow-bootstrap_phase2_review_tier_guidance_execution_report.md`

该 execution report 至少包含：

1. 本次改了什么。
2. 本次没改什么。
3. 实际验证了什么。
4. 是否发现 advisory / enforcement 边界混淆。
5. 是否发现 ownership boundary 漂移。
6. 是否需要后续 follow-up。

当前这一轮只生成 task package，不创建该 execution report。

---

## Recommended Commit Message

```text
docs(workflow-bootstrap): add review tier guidance
```

---

## Execution Notes

后续正式施工建议遵循以下顺序：

1. 先读取本任务包并复述边界，确认本轮是 advisory review guidance，不是 protocol redesign。
2. 优先新增 `skills/workflow-bootstrap/review_tiers.md`，完整写清三层 review tier 的定位、场景、检查项、second review 建议、不适用场景和例子。
3. 仅在确有必要时，对 `SKILL.md`、`role_split_and_integration.md`、`examples/invocation_examples.md` 做最小回指或短示例补充。
4. 检查文案是否把 `workflow-bootstrap` 写成 handoff protocol owner；如有，应收回到 advisory workflow-shell guidance。
5. 检查文案是否把 review tier guidance 写成 mandatory gate、hard failure rule、CI 或 validator；如有，应回退到 advisory 表述。
6. 完成后执行最小验证。
7. 最后输出 execution report。

本轮 task package 的目的，是为 Reviewer 增加可迁移、可操作、但仍保留上下文判断空间的审包强度 guidance，而不是把 review 简化成自动决策表或把 `workflow-bootstrap` 扩写成第二协议层。
