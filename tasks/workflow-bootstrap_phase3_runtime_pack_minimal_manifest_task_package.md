# 任务包：workflow-bootstrap Phase 3 Runtime Pack Minimal Manifest

## 任务标识

- task id: `WF-BOOTSTRAP-PHASE3-RUNTIME-PACK-MINIMAL-MANIFEST-V1`
- 名称：workflow-bootstrap Phase 3 / Runtime Pack Minimal Manifest
- 阶段：`Phase 3`
- 提交方：Drafter
- 日期：`2026-04-29`
- 前置输入：
  - `skills/workflow-bootstrap/SKILL.md`
  - `skills/workflow-bootstrap/role_split_and_integration.md`
  - `skills/workflow-bootstrap/review_tiers.md`
  - `skills/workflow-bootstrap/non_git_runtime_profile.md`
  - `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
  - `skills/workflow-bootstrap/examples/invocation_examples.md`
  - `skills/chatgpt-handoff-pilot/SKILL.md`
  - `tasks/workflow-bootstrap_phase1_role_split_canonicalization_task_package.md`
  - `tasks/workflow-bootstrap_phase1_role_split_canonicalization_execution_report.md`
  - `tasks/workflow-bootstrap_phase2_review_tier_guidance_task_package.md`
  - `tasks/workflow-bootstrap_phase2_review_tier_guidance_execution_report.md`

---

## Scope Restatement

本轮只生成 `workflow-bootstrap` 的 Phase 3 task package：`Runtime Pack Minimal Manifest`。

本轮不进入正式施工，不修改任何 `workflow-bootstrap` 或 `chatgpt-handoff-pilot` skill 文件，不新增 execution report，不创建任何 project-side runtime files。

本任务包的目的，是为后续正式施工提供清晰、收窄、可审阅的授权边界，使实施侧能够在不扩写协议 ownership 的前提下，为 `workflow-bootstrap` 补充一份关于 project-side runtime pack minimal manifest 的 guidance。

本轮 task package 应确保后续正式施工只讨论以下问题：

1. runtime pack minimal manifest 在 `workflow-bootstrap` 中的定位是什么。
2. 它与 canonical skills、task package、execution report 的关系是什么。
3. project-side runtime surfaces 的最小候选组成与薄入口边界是什么。
4. Git-first 与 non-git / low-git 项目在 runtime pack 证据放置上的差异如何被保守表述。

只有在后续显式切换到 `Implementer` 角色后，本任务包才可作为 Phase 3 bounded execution 的授权输入；届时 Implementer 只能在本任务包 `Authorized Files` 列出的路径内施工。

---

## Background

`workflow-bootstrap` 的前序阶段已经形成如下基线：

- Phase 0 已完成 non-git / low-git runtime profile absorption，并明确 `tasks/` 在 non-git / low-git 场景下可作为 preferred project-local evidence path，但不是所有项目的 mandatory global path。
- Phase 1 已完成 role split canonicalization，默认协作链路已经稳定抽象为：

  ```text
  Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer
  ```

- Phase 2 已完成 review tier guidance，已经定义：

  ```text
  Light Review -> Standard Review -> Heavy Review
  ```

当前 `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md` 已存在，但其现状仍偏向 future project-side target 的概览说明，且当前正文仍列出较宽的候选面，例如：

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/instructions/*.instructions.md`
- `.github/agents/*.agent.md`
- optional project-local skill payload and adapters

Phase 3 的目标不是把这些更宽的 future surfaces 全部实体化或制度化，而是把 runtime pack minimal manifest guidance 收敛为更清楚的 project-side thin runtime surface guidance，明确最小候选组成、canonical ownership、thin adapter boundary，以及它与 `chatgpt-handoff-pilot` 的协议边界。

本次起草前的实际发现如下：

- 用户点名要求读取的相关文件均存在，未发现缺失输入文件。
- 推荐 task package 路径 `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_task_package.md` 在起草前不存在。
- 推荐 execution report 路径 `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_execution_report.md` 在起草前不存在。

因此，本轮适合只产出 task package，把 Phase 3 的实施边界先锁定，再由后续 bounded execution 按白名单施工。

---

## Target Files

后续正式施工的优先目标文件：

- `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`

允许做最小回指、短例或边界补充的文件：

- `skills/workflow-bootstrap/SKILL.md`
- `skills/workflow-bootstrap/role_split_and_integration.md`
- `skills/workflow-bootstrap/review_tiers.md`
- `skills/workflow-bootstrap/non_git_runtime_profile.md`
- `skills/workflow-bootstrap/examples/invocation_examples.md`

后续正式施工的执行回执推荐落点：

- `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_execution_report.md`

本轮 task package 落点：

- `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_task_package.md`

---

## Authorized Files

若后续进入 Phase 3 正式施工，本任务包仅授权修改以下文件：

- `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
- `skills/workflow-bootstrap/SKILL.md`（仅允许最小回指，不复制 `runtime_pack_minimal_manifest.md` 正文）
- `skills/workflow-bootstrap/role_split_and_integration.md`（仅允许最小回指，不复制 `runtime_pack_minimal_manifest.md` 正文）
- `skills/workflow-bootstrap/review_tiers.md`（仅允许最小回指，不复制 `runtime_pack_minimal_manifest.md` 正文）
- `skills/workflow-bootstrap/non_git_runtime_profile.md`（仅允许最小边界澄清，不复制 `runtime_pack_minimal_manifest.md` 正文）
- `skills/workflow-bootstrap/examples/invocation_examples.md`（仅允许增加最小短例，不复制 `runtime_pack_minimal_manifest.md` 正文）
- `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_execution_report.md`（正式施工完成后新增）

本任务包文件保留于：

- `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_task_package.md`

除上述路径外，默认无权修改其他文件或目录。

---

## Out of Scope

本轮 task package 生成，以及后续 Phase 3 正式施工，均明确不做以下事项：

- 不修改 `chatgpt-handoff-pilot`。
- 不重定义 task package / bounded execution / execution report schema。
- 不新增 validator / scripts / tests / CI / hooks / automation。
- 不创建 `tool_adapters/`。
- 不进入 Phase 4 multi-project pilot。
- 不进入 Phase 5 tool adapter candidates。
- 不新增 `.github/instructions/` 或 `.github/agents/`。
- 不在 `ai-skill-hub` 中创建 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/copilot-instructions.zh-CN.md` 或 `tasks/README.md`。
- 不把 runtime pack 写成所有项目强制标准。
- 不把 project-side runtime surfaces 写成第二 canonical source。
- 不把 `tasks/` 写成所有项目强制路径。
- 不修改 `README.md`、`docs/HANDOFF.md`、status surfaces 或其他未授权文件。
- 不把当前工具订阅差异、模型强弱或工具偏好写入 canonical guidance。
- 不把 `.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 或其他 project-side runtime entities 写成当前 Phase 3 必须落地的实体创建项。
- 不把 runtime pack 扩写成新的 execution protocol。
- 不把 runtime pack 写成 CI / validator / automation 机制。

---

## Required Content

后续正式施工时，`skills/workflow-bootstrap/runtime_pack_minimal_manifest.md` 至少应补齐或重组以下内容：

1. 明确 runtime pack minimal manifest 的定位：
   - 它是 project-side runtime surface guidance。
   - 它不是第二规则库。
   - 它不是 canonical skill 的复制层。
   - 它不是新的 execution protocol。
   - 它不是 CI / validator / automation 机制。

2. 明确 canonical ownership：
   - `skills/` 仍是 canonical source。
   - `workflow-bootstrap` 只定义 workflow shell / role split / runtime profile / review tier / runtime pack manifest guidance。
   - `chatgpt-handoff-pilot` 仍拥有 task package / bounded execution / execution report protocol。

3. 定义 runtime pack 的最小 candidate surfaces，并明确这些只是 project-side runtime pack candidate surfaces，不授权在当前 `ai-skill-hub` 仓库中创建这些项目侧文件：
   - `AGENTS.md`
   - `.github/copilot-instructions.md`
   - `.github/copilot-instructions.zh-CN.md`
   - `tasks/README.md`
   - `tasks/<task-package>.md`
   - `tasks/<execution-report>.md`

4. 为每个 candidate surface 至少说明：
   - 中文定位
   - 主要用途
   - 应回指哪些 canonical guidance
   - 不应包含什么
   - 是否适用于 Git-first / non-git / low-git 项目

5. 明确 thin adapter / thin entry 原则：
   - 只做发现、路由、回指。
   - 不复制 canonical skill 正文。
   - 不形成 parallel rule set。
   - 不把项目侧事实写成通用规则。

6. 明确 `tasks/` 的边界：
   - 在 non-git / low-git 场景中，`tasks/` 可作为 preferred project-local evidence path。
   - 不把 `tasks/` 写成所有项目 mandatory global path。
   - task package / execution report 协议仍归 `chatgpt-handoff-pilot`。

7. 明确 Git-first 项目与 non-git / low-git 项目的差异：
   - Git-first 项目可以结合 branch / commit / PR-style review。
   - non-git / low-git 项目更依赖 task package / execution report pairing。
   - runtime pack 只给出最小 project-side surface guidance，不强制所有项目采用同一文件组合。

8. 明确本 Phase 3 不进入：
   - tool adapter design
   - validator / automation / CI
   - `.github/instructions/` 实体创建
   - `.github/agents/` 实体创建
   - Phase 4 multi-project pilot
   - Phase 5 tool adapter candidates

9. 若现有 `runtime_pack_minimal_manifest.md` 中仍出现 `.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 或 `optional project-local skill payload and adapters` 等更宽 future surfaces，应在 Phase 3 正式施工中收窄其表述：
   - 可以保留为 deferred / future candidate note。
   - 不能把它们写成当前 minimal manifest 的必选组成。
   - 不能把它们写成当前 hub 内应创建的实体文件。

10. 若 `SKILL.md`、`role_split_and_integration.md`、`review_tiers.md`、`non_git_runtime_profile.md`、`examples/invocation_examples.md` 需要补充，只能做最小回指或短例：
    - `SKILL.md` 只补 supporting asset 或一句边界回指。
    - `role_split_and_integration.md` 只补 thin runtime surface 与 protocol boundary 的最小说明。
    - `review_tiers.md` 只补 runtime-pack-related wording 应按 `Heavy Review` 审看的一句回指或边界提示。
    - `non_git_runtime_profile.md` 只补 `tasks/` 作为 evidence path 与 runtime pack minimal guidance 的衔接说明。
    - `examples/invocation_examples.md` 只补一个短例，不复制主体内容。

---

## Acceptance Criteria

后续 Phase 3 正式施工完成后，至少必须满足以下条件：

1. `runtime_pack_minimal_manifest.md` 的定位被明确写为 project-side thin runtime surface guidance。
2. runtime pack 被写成 minimal / optional / project-aware guidance，而不是 mandatory global rule。
3. `AGENTS.md`、`.github/copilot-instructions.md`、`.github/copilot-instructions.zh-CN.md`、`tasks/README.md`、task package、execution report 等 candidate surfaces 的用途和边界清楚。
4. 所有 project-side surfaces 都被描述为 thin entry / thin adapter / evidence index，而不是第二规则库。
5. 没有创建任何实际 project-side runtime files。
6. 没有新增 scripts、tests、CI、validators、hooks 或 automation。
7. 没有创建 `tool_adapters/`。
8. 没有修改 `chatgpt-handoff-pilot`。
9. `workflow-bootstrap` / `chatgpt-handoff-pilot` ownership boundary 仍清楚。
10. `tasks/` 被写成 non-git / low-git 的 preferred project-local evidence path，而不是所有项目的强制路径。
11. Git-first 与 non-git / low-git 的差异被清楚写明，但没有把任一模式升级为所有项目必须遵守的统一组合。
12. `SKILL.md`、`role_split_and_integration.md`、`review_tiers.md`、`non_git_runtime_profile.md`、`examples/invocation_examples.md` 若被补充，只能做最小回指或短例，不得复制 `runtime_pack_minimal_manifest.md` 正文。
13. `.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 或 `optional project-local skill payload / adapters` 若被提及，只能以 deferred / future note 方式出现，不能被写成当前 minimal manifest 的必选组成。

---

## Validation Plan

后续正式施工完成后，至少执行以下验证：

1. 检查是否新增了 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/copilot-instructions.zh-CN.md`、`.github/instructions/`、`.github/agents/` 或 `tasks/README.md`。
2. 检查是否新增 scripts / tests / CI / validator / hooks / automation。
3. 检查是否创建 `tool_adapters/`。
4. 检查是否修改 `chatgpt-handoff-pilot`。
5. 检查是否把 runtime pack 写成 mandatory global rule。
6. 检查是否把 project-side runtime surfaces 写成 parallel canonical source。
7. 检查是否把 `tasks/` 写成所有项目强制路径。
8. 检查是否仍明确 `chatgpt-handoff-pilot` 是 task package / bounded execution / execution report protocol owner。
9. 检查 supporting files 是否只做最小回指或短例，没有复制 `runtime_pack_minimal_manifest.md` 主体内容。
10. 检查是否没有进入 Phase 4 multi-project pilot、Phase 5 tool adapter candidates 或 validator / automation preflight。
11. 检查 `AGENTS.md`、`.github/copilot-instructions.md`、`.github/copilot-instructions.zh-CN.md`、`tasks/README.md`、`tasks/<task-package>.md`、`tasks/<execution-report>.md` 等 candidate surfaces 是否都写明了用途、应回指的 canonical guidance、不得包含的内容，以及 Git-first / non-git / low-git 适用边界。
12. 检查 `.github/instructions/*.instructions.md`、`.github/agents/*.agent.md` 或 `optional project-local skill payload / adapters` 若仍被提及，是否已被明确降级为 deferred / future note，而不是当前 Phase 3 minimal manifest 的必选组成。
13. 检查是否没有把 runtime pack 写成新的 execution protocol、CI policy、validator contract 或 automation rollout plan。
14. 检查 `non_git_runtime_profile.md` 与 `runtime_pack_minimal_manifest.md` 之间的 `tasks/` evidence wording 是否一致，且仍保守。
15. 检查若 `review_tiers.md` 被补充，runtime-pack-related wording 是否仍保持 advisory / `Heavy Review` 分类语义，而非 implementation authorization。

若环境允许，可辅以最小文本检查；若无自动化验证，则至少在 execution report 中报告上述人工检查结果。

---

## Execution Report Requirement

若后续进入 Phase 3 正式施工，执行完成后必须新增：

- `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_execution_report.md`

该 execution report 至少应包含：

1. 本次改了什么。
2. 本次没改什么。
3. 实际验证了什么。
4. 是否发现 runtime pack boundary、thin adapter boundary 或 ownership wording 歧义。
5. 是否明确保留了哪些 deferred / future surfaces。
6. 是否需要后续 follow-up。

当前这一轮只生成 task package，不创建该 execution report。

---

## Recommended Commit Message

```text
docs(workflow-bootstrap): add runtime pack minimal manifest
```

---

## Execution Notes

实际发现说明：

1. 本轮起草前，用户要求读取的上下文文件均存在。
2. 本轮起草前，Phase 3 task package 推荐路径不存在，因此本次输出为新建 task package，而不是覆盖或修订已有 Phase 3 task package。
3. 本轮起草前，Phase 3 execution report 推荐路径不存在，且本轮明确不创建 execution report。
4. 现有 `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md` 已存在，但其内容仍偏 future project-side target 概览；后续正式施工应把它收窄为更清楚的 minimal manifest guidance，而不是沿着 `.github/instructions/`、`.github/agents/` 或 optional local adapters 扩写成更大的 runtime-pack design。

后续正式施工建议遵循以下顺序：

1. 先读取本任务包并复述边界，确认本轮是 runtime pack minimal manifest guidance，不是 protocol redesign、tool adapter design 或 automation rollout。
2. 优先修改 `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`，把定位、candidate surfaces、thin adapter boundary、ownership boundary、Git-first / non-git / low-git 差异写完整。
3. 若确有必要，再对 `SKILL.md`、`role_split_and_integration.md`、`review_tiers.md`、`non_git_runtime_profile.md`、`examples/invocation_examples.md` 做最小回指或短例补充。
4. 检查文案是否把 runtime pack 写成 mandatory rule、parallel canonical source、new protocol、CI / validator / automation mechanism；如有，应回退到 thin project-side guidance。
5. 检查文案是否误把 `.github/instructions/`、`.github/agents/`、`optional local adapters` 写成当前 minimal manifest 的必选组成；如有，应降级为 deferred / future note 或直接移出当前最小组成。
6. 完成后执行最小验证。
7. 最后输出 execution report。

根据 `review_tiers.md` 的既有 guidance，runtime pack design、cross-project wording 和 project-side runtime surfaces 属于高风险边界主题；后续正式施工建议按 `Heavy Review` 的审包强度处理，但这条建议不构成当前 task package generation 轮次的施工授权。
