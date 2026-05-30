---
name: complexity-degradation
description: 复杂任务降级协议。适用于任务超出 AI 当前稳定能力、需求链路过长或一次性落地风险过高时，拆成 capability split、staged delivery、partial implementation 与 temporary node 的请求；不负责替代正常 MVP 规划。
---

# complexity-degradation

## What To Use It For
- 任务太大、太长、太不确定时的安全降级
- 把一次性目标切成可稳定完成的局部切片
- 允许 partial delivery，但不允许失控重构
- 为复杂任务建立 temporary node 和回补路径

## Core Heuristics
1. AI 不会稳定完成的任务，先降级，不硬做。
2. 降级后的切片必须能独立验证，而不是只把工作拆小。
3. partial implementation 必须保持未来可续接。
4. temporary node 不是偷懒标签，而是带退出条件的协议。
5. 本 skill 解决“做不稳怎么办”，不替代正常的 MVP 基线设计。

## Workflow
1. 识别超载信号：链路过长、依赖过多、根因不清、影响面过大、需要跨多轮才能稳定完成。
2. 定义当前最安全的 capability split。
3. 为当前轮选择 staged delivery 或 partial implementation。
4. 写清 temporary node、验证门槛和回补触发条件。
5. 产出安全切片后，把正常执行交给 `iteration-execution`。

## Minimal Output
1. 超载原因
2. capability split
3. 当前安全切片
4. staged delivery / partial implementation 方案
5. temporary 节点
6. 验证门槛
7. 回补触发条件

## Anti-Patterns
- 明知任务超出稳定能力还一次性硬做
- 只说“分阶段做”，但没有当前安全切片
- 用降级协议逃避应该先做的 MVP 规划
- 创建 temporary 节点却不定义退出条件
