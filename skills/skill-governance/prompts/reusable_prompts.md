# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

本 skill 复用以下三个 prompt 资产：

- `prompts/skill-governor.md`：治理入口，负责路由 `rewrite=true/false`
- `prompts/skill-evaluator.md`：只做评分与诊断，不允许重写
- `prompts/skill-refactor.md`：基于评估结果执行受控重写
- `prompts/skill-refinement.md`：只做表达层收口，不进入结构重写
- `prompts/skill-batch-evaluator.md`：按顺序批量评估 `skills/` 下的一级 skill
- `prompts/skill-invocation.md`：定义统一 skill 调用协议，规范 `skill / target / parameters` 的传递方式

### 模板 1：标准治理调用

```text
Use skill-governance on <skill-path>
rewrite=false

Goal:
- Evaluate one skill against SKILL_TEMPLATE and governance rules

Expected output:
- SCORECARD
- DIAGNOSIS
- LEVEL
```

### 模板 2：受控重写调用

```text
Use skill-governance on <skill-path>
rewrite=true

Requirements:
- Evaluate first
- Show SCORECARD and DIAGNOSIS
- Refactor only the target skill
- Keep the rewrite non-intrusive
- Preserve the skill type alignment
```
