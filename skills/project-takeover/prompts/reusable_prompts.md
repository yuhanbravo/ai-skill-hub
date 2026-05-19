# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准接管调用

```text
请使用 `project-takeover` 处理以下仓库接管任务。

背景：
- 这是一个需要接手或 onboarding 的项目

目标：
- 生成 takeover packet，并帮助新维护者快速理解仓库

范围：
- 扫描项目环境、关键文档、任务来源和可用审计脚本
- 整理接手所需的结构化输出

约束：
- 保留项目本地配置优先级
- 不做未授权的高风险副作用

预期输出：
- 按 `scan -> understand -> structure -> output` 推进
- `project_takeover_report.md`
- `project_onboarding_summary.md`
- `welcome_email.md`
- 风险与下一步建议
```

### 模板 2：严格阶段化执行模板

```text
请按 `project-takeover` 的方法执行本次任务。

要求：
- 先总结你对项目接管目标的理解
- 按 `scan -> understand -> structure -> output` 四个阶段推进
- 明确当前使用的配置、脚本和可选参数
- 输出结果、风险和待确认项

任务内容：
- Project root: <project-root>
- Primary goal: <takeover | onboarding | handoff prep>
- Config path: <path-or-none>
- Report dir: <path-or-default>
- Shared dir: <path-or-none>
- Dry run: <yes-or-no>
- Apply safe fixes: <yes-or-no>
- Install: <yes-or-no>
- Structure script override: <path-or-none>
- Docs script override: <path-or-none>
```

### 模板 3：增量接管更新（post-takeover delta）

```text
请使用 `project-takeover` 执行“增量接管更新”，不要重做全量 takeover packet。

背景：
- 仓库中已存在历史 takeover 产物（如 `docs/takeover/`）
- 本轮目标是识别“变化项”，而不是重复生成全部 onboarding 内容

目标：
- 仅输出与上次接管结论相比的 delta
- 帮助维护者快速判断：哪些结论可沿用，哪些结论需要更新

范围：
- 继续按 `scan -> understand -> structure -> output` 推进
- 重点比较：关键文档入口、任务来源、环境 readiness、阻塞项与风险优先级

约束：
- 明确区分：`沿用结论` / `新增结论` / `待确认项`
- 若无显著变化，直接给出“无需重跑全量接管”的结论与依据
- 不执行未授权高风险动作

预期输出：
- Delta summary（相对历史接管产物）
- Updated risks & next actions
- 是否建议重跑全量 takeover（yes/no + reason）
```

### 模板 4：重跑必要性评估（dry-run gate）

```text
请使用 `project-takeover` 进行“重跑必要性评估”，以 dry-run 方式执行。

目标：
- 判断当前仓库是否需要重跑完整 takeover
- 给出最小可行的下一步执行参数

要求：
- 显式说明当前参数：`--config` `--report-dir` `--shared-dir` `--structure-script` `--docs-script` `--dry-run`
- 评估维度至少包括：
  1) 文档入口变化
  2) 任务来源变化
  3) 环境依赖或可执行性变化
  4) 风险与阻塞变化
- 输出 `rerun_recommendation: yes|no` 与简要证据

约束：
- 本轮只做 dry-run 判断，不落盘正式 takeover 文档
- 缺失工具或脚本时保持 soft-fail，并写入结论

预期输出：
- Rerun decision
- Evidence list
- Suggested minimal command/params for next run
```

### 模板 5：风险驱动后续动作提炼（post-takeover risk focus）

```text
请使用 `project-takeover` 的结果视角，生成“风险驱动后续动作”摘要。

背景：
- takeover 基线已存在
- 当前重点是推进后续接手，而非重做接管文档

目标：
- 仅针对高优先级风险提炼可执行动作

要求：
- 每条风险输出：影响范围、最小缓解动作、验证方法、是否需要人工决策
- 给出建议执行顺序（先低风险快收敛，再处理中高风险）
- 保留 `open_questions` 与 `next_action` 字段意识

约束：
- 不扩展为完整项目管理计划
- 不重写历史接管产物，仅补充风险导向结论

预期输出：
- Prioritized risk actions
- Validation checklist
- Decision-needed items
```

### 模板 6：跨技能衔接提示（handoff redirect）

```text
当你的目标从“接管理解”转为“按边界实施任务”时，请停止扩展 `project-takeover` 输出，
并改用 `chatgpt-handoff-pilot` 生成 task package + bounded execution + execution report。

触发条件（任一满足即可切换）：
- 需要把任务分配给另一个 AI/成员执行
- 需要严格定义本轮修改范围、明确不做项和验收标准
- 需要结构化施工回执用于审阅

输出要求：
- 先给出切换建议与原因
- 再给出建议使用的 handoff 输入骨架（任务目标 / 范围 / 不做 / 验收 / 回执格式）
```
