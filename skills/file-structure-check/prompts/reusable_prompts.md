# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准结构审计模板

```text
请使用 `file-structure-check` 处理以下任务。

背景：
- 需要检查仓库目录结构是否符合当前项目约定

目标：
- 审计结构问题，并输出结构化报告

范围：
- 检查目录布局
- 检查 required paths
- 识别错位文件
- 输出建议修复项，但默认不执行修复

约束：
- 默认只做 audit 和 report
- fix 必须显式触发

预期输出：
- 按 `audit -> report -> fix(optional)` 推进
- 审计结果
- 问题清单
- 建议修复项
```

### 模板 2：严格审计执行模板

```text
请按 `file-structure-check` 的方法执行本次任务。

要求：
- 先总结你对审计目标的理解
- 按 `audit -> report -> fix(optional)` 三段执行
- 明确当前使用的 profile、strictness 和配置来源
- 报告中区分“已发现问题”和“建议修复”
- 未显式授权时，不执行任何 fix

任务内容：
- Project root: <project-root>
- Profile: <application | data-project | docs-only | monorepo | custom>
- Strictness: <relaxed | standard | strict>
- Config path: <path-or-none>
- JSON output: <yes-or-no>
```
