# Reusable Prompts

This file preserves the prompt templates split out of `SKILL.md` during the AI/Human/Bridge semantic split.

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准迁移评估模板

```text
请使用 `financial-data-project-migration` 处理以下任务。

背景：
- 这是一个金融数据 Python 项目，当前结构可能处于脚本堆积或迁移过渡状态

目标：
- 判断项目类型与迁移阶段，并输出最小安全迁移建议

范围：
- 扫描目录结构、脚本分布、Excel 资产和运行耦合信号
- 输出目标结构建议、文件角色分类和最小 TODO

约束：
- 默认不改变项目，只做观察和结构化输出
- 不直接执行文件迁移或 package-first 重构

预期输出：
- 按 `scan -> understand -> structure -> output` 推进
- 项目类型判断
- 迁移阶段判断
- 固定风险
- 目标结构建议
- 最小迁移 TODO
```

### 模板 2：严格阶段化执行模板

```text
请按 `financial-data-project-migration` 的方法执行本次任务。

要求：
- 先总结你对当前迁移评估目标的理解
- 按 `scan -> understand -> structure -> output` 四个阶段推进
- 显式说明是否存在 Excel / Wind / 网络盘 / 当前工作目录依赖
- 如果项目风险较高，优先输出保守建议，而不是直接建议迁移到 `src`
- 输出结果、风险和待确认项

任务内容：
- Project root: <project-root>
- Special context: <none-or-extra-notes>
- Need mapping candidates: <yes-or-no>
- Need minimal TODO: <yes-or-no>
```
