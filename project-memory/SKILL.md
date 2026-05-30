---
name: project-memory
description: 项目历史与决策记忆。适用于回答“为什么现在这样设计”、记录 ADR、rejected options、失败路线、稳定原则与临时妥协的请求；不负责当前轮推进或新能力规划。
---

# project-memory

## What To Use It For
- 记录重要设计决策和背后的原因
- 保存 rejected options 和失败路线
- 说明哪些原则已经稳定，哪些妥协只是阶段性的
- 让未来 session 能理解“为什么系统会变成现在这样”

## Core Heuristics
1. 记录决策原因，比复述代码现状更重要。
2. 只记录会影响未来选择的历史，不堆砌流水账。
3. stable 原则、temporary 妥协、失败路线必须分开写。
4. 没有证据就标记 `TO_BE_CONFIRMED`，不要伪造历史。
5. 本 skill 关注历史连续性，不代替 MVP 规划或当前执行推进。

## Workflow
1. 确认要记录的事件：决策、妥协、失败、回退或原则固化。
2. 写清当时背景、约束和触发原因。
3. 记录最终决策、被拒绝选项和理由。
4. 标记这条记忆属于 stable 原则还是 temporary 妥协。
5. 写清未来什么信号会触发重审。

## Minimal Output
1. 事件名称
2. 背景与约束
3. 最终决策
4. rejected options / failed paths
5. stable / temporary 标记
6. 重审触发条件

## Anti-Patterns
- 只写“做了什么”，不写“为什么这么做”
- 把当前进度状态误记成历史决策
- 把一次性讨论纪要当成稳定原则
- 默认所有旧决定都不可推翻
