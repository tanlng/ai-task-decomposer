---
name: mvp-evolution
description: MVP 验证与能力拆分。适用于新想法、新能力或核心实验需要明确当前验证目标、MVP baseline、capability roadmap 和 iteration plan 的请求；不负责历史解释、当前进度播报或复杂任务降级。
---

# mvp-evolution

## What To Use It For
- 定义当前到底在验证什么
- 把一个想法收敛成 MVP baseline
- 拆 capability roadmap 和 iteration 顺序
- 规定当前轮只做哪一个验证切片

## Core Heuristics
1. 先收敛验证目标，再拆能力，不先画完整未来系统。
2. roadmap 解决“将来可能做什么”，iteration plan 解决“这轮具体做什么”。
3. 未验证能力默认允许 temporary 方案，但必须显式标记。
4. 每一轮都要能回答“如果这轮成功，我们学到什么”。
5. 本 skill 不负责解释历史，也不负责播报当前执行状态。

## Workflow
1. 写清当前想法、假设和要验证的核心问题。
2. 给出 MVP baseline：
   - 这轮必须验证的能力
   - 这轮明确不做的能力
3. 拆 capability roadmap，只保留和验证目标直接相关的模块。
4. 写 iteration plan，明确当前轮、下一轮和后续回补点。
5. 标记 stable 内容和 temporary 内容，并把执行入口交给 `iteration-execution`。

## Minimal Output
1. 当前验证目标
2. MVP baseline
3. capability roadmap
4. current iteration
5. next iteration
6. temporary 节点与回补时机

## Anti-Patterns
- 一上来就设计完整系统
- 只有 roadmap，没有 current iteration
- 把“未来可能需要”混进“这轮必须验证”
- 用本 skill 代替历史决策记录或当前轮状态管理
