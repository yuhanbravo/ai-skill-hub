# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准文档治理审计模板

```text
请使用 `documentation-governance` 处理以下任务。

背景：
- 需要检查仓库文档结构、事实源关系和重复问题

目标：
- 输出文档治理审计结果，并给出建议动作

范围：
- 检查 `docs/` 与 `docs_readable/` 的层级关系
- 检查重复主题、命名违规、归档候选和 README 缺口
- 默认只做 audit 和 report

约束：
- 默认不改变项目，只做观察和结构化输出
- fix 必须显式触发

预期输出：
- 按 `audit -> report -> fix(optional)` 推进
- 治理报告
- 高优先级问题
- 建议动作与待确认项
```

### 模板 2：严格治理执行模板

```text
请按 `documentation-governance` 的方法执行本次任务。

要求：
- 先总结你对治理目标的理解
- 按 `audit -> report -> fix(optional)` 三段执行
- 明确当前使用的配置来源、扫描范围和输出方式
- 报告中区分“问题发现”和“建议修复”
- 未显式授权时，不执行任何 fix

任务内容：
- Project root: <project-root>
- Config path: <path-or-none>
- Dry run: <yes-or-no>
- JSON output: <yes-or-no>
- Report path: <path-or-none>
- Write README sections: <yes-or-no>
```
