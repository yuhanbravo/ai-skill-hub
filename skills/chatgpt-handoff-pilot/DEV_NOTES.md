# 开发备注

## 为什么当前保持最小

这个 skill 的职责不是定义一整套项目管理体系，而是提供一个最小可执行的 handoff 协作壳层。

当前保持最小，主要是为了：

- 先验证上游任务包到实施回执的输入输出流是否顺畅
- 降低复制到真实项目中的接入成本
- 避免在还没有试跑反馈前，过早设计过多字段、脚本或流程

## V2 新增点

在已实现 `docs/HANDOFF.md` 单一主文档策略的基础上，V2 进一步补齐了长期维护机制：

- 引入固定 `## Update Log` section 及稳定追加规则
- 引入 section-aware merge，而不是泛化全文重写
- 明确 `Current Status / Hard Boundaries / Recommended Next Steps / Environment Blockers / Update Log` 为优先更新 section
- 对历史 generated handoff 资产给出统一 legacy/generated 标记策略
- 将 execution report 模板正式并入主流程，要求明确写出改动、未改动、验证、阻塞与下一步建议

## 输出策略更新

当前默认 handoff 文档策略已经统一为：

- `docs/HANDOFF.md` 是项目内唯一权威 handoff 主文档（SSOT）
- 若该文件存在，默认做 section-aware 增量更新
- 若该文件不存在，默认创建 `docs/HANDOFF.md`
- 默认维护 `## Update Log`
- `minimal_handoff_manual.md` 不再作为默认输出文件
- 若历史已有 `minimal_handoff_manual.md`，保留但不再更新，可在 `docs/HANDOFF.md` 中标记为 legacy/generated

这次调整仍然只改变输出策略和文件落盘策略，不改变这个 skill 生成 handoff 内容、task package 和 execution report 的核心能力。

## 这次准备在真实项目里验证什么

本轮不是验证复杂自动化，而是验证下面几个最小问题：

- 上游是否能稳定写出边界清晰的任务包
- 实施侧是否会先总结理解，再按范围施工
- execution report 是否足够支撑上游做验收和下一轮拆解
- 在真实项目中，这套最小模板是否容易被新同事和 AI 直接拿来使用
- handoff 信息是否能稳定收口到 `docs/HANDOFF.md`，而不是继续产生平行主文档
- 连续两次更新时，是否只会在现有 `docs/HANDOFF.md` 内做 section-aware 增量更新并追加 `Update Log`

## 暂时刻意不做的内容

- 不做自动生成器
- 不做任务状态机
- 不做固定字段校验脚本
- 不绑定任何业务项目结构
- 不把 execution report 扩写成完整设计文档
- 不为了追求模板统一而重排项目已有 `docs/HANDOFF.md`

## 维护提醒

如果后续要同步到 skill-hub，建议优先保留：

- 最小边界
- 最小模板
- 单一主文档策略
- `Update Log + section-aware merge` 的维护方式

不建议过早引入只适用于单一项目的强绑定规则。
