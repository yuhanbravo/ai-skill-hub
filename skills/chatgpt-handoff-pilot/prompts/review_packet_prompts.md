# Review Packet Prompts

这组 prompt 只服务于 `review packet` 的生成与审阅。

- `review packet` 不替代 `task package`
- `review packet` 不替代 `execution report`
- 目标是收敛“本轮值得审的增量”，减少长聊天记录复制粘贴

## 模板 1：让 Codex 生成 review packet

```text
请基于本轮已经完成的实施结果，生成一份最小 `review packet`。

要求：
- 只服务于审阅，不重新定义任务
- 不替代 `task package`，不替代 `execution report`
- 只保留本轮值得给 ChatGPT / 上游审阅侧查看的增量摘要
- 字段尽量少，但要覆盖目标、实际改动、涉及文件、未改范围、验证摘要、风险和审阅重点
- 不要补写无关长篇背景
- 如果信息不足，明确写“待补充”，不要编造

请优先参考：
- `templates/REVIEW_PACKET_TEMPLATE.md`

输入材料：
- 本轮 task package
- 本轮 execution report
- changed files summary
- 必要的验证结果或日志片段
```

## 模板 2：让 Copilot 生成 review packet

```text
请按 `chatgpt-handoff-pilot` 的最小边界，为当前这轮实施整理一份 `review packet`。

要求：
- 面向 ChatGPT / 上游审阅侧
- 只总结本轮值得审的增量
- 不把 `task package` 原样重写一遍
- 不把 `execution report` 全量机械复制一遍
- 保持中文为主、简洁、可直接上传
- 如果某项没有证据，写“未验证”或“待确认”

输出结构：
- 使用 `REVIEW_PACKET` 标题
- 按模板字段填写
- 最后一节明确“希望审阅者重点审什么”

参考文件：
- `templates/REVIEW_PACKET_TEMPLATE.md`
- `examples/example_review_packet.md`
```

## 模板 3：让 ChatGPT 基于 review packet 做审阅

```text
请基于我提供的 `review packet` 进行审阅。

审阅要求：
- 重点看边界是否被写清
- 重点看本轮完成度是否与目标一致
- 重点看验证是否足够支持当前结论
- 重点看风险、阻塞、待确认项是否遗漏
- 如果发现表达过重、越界、证据不足或结论跳跃，请直接指出

边界要求：
- `review packet` 只服务于审阅，不替代 `task package` 与 `execution report`
- 不要要求我补写无关长篇背景
- 如果现有材料不足，请只指出“还缺什么最小信息”

输出建议：
- 审阅结论
- 主要问题 / 风险
- 建议补充的信息
- 是否可以进入下一步
```
