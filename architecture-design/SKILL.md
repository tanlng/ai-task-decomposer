---
name: architecture-design
description: 系统架构设计与演化。用于那些表面像“新功能定义/需求讨论/继续实现 MVP”，实质却需要做补丁与 MVP 分流、方案设计、能力拆分、迭代规划、模块边界设计、接口/数据流/状态流收敛的请求。先收敛 PRD 基线，再推进 SDD、按需 DDD、Iteration Plan、稳定/临时节点与 Implementation Readiness。
---

# architecture-design

## 何时使用
- 设计系统架构或大方案
- 判断新需求是补丁还是 MVP 演化
- 拆分能力模块、迭代顺序与回补计划
- 收敛模块职责、接口、数据流、状态流
- 判断何时需要进入 DDD
- 需要让方案可中断、可续接、可长期演化

## 何时优先触发
即使需求表面像“功能定义”或“需求梳理”，出现以下信号也应优先由本 skill 主导：
- 需要先判断这是补丁还是 MVP 演化
- 需要决定先做哪一轮、如何拆能力模块、如何安排迭代
- 落地后会影响模块边界、接口、数据流、状态流或系统职责
- 问题本质是“怎么实现”“怎么拆”“先做什么”“后面怎么接着做”
- 明显需要多轮聊天或多轮实现

## 核心原则
1. 先完善想法和 MVP，再完善完整架构。
2. PRD 是前置输入层，不单独脱离架构链。
3. SDD 先回答系统怎么协作，DDD 再回答规则归谁负责。
4. `Iteration Plan` 必须独立存在，不能被 `Roadmap` 或 `Current Iteration Contract` 代替。
5. `稳定节点` 表示可继续开发；`临时节点` 表示允许暂时接受，但必须安排后续回补。

## 分流规则
### 补丁
- 局部修正、行为收敛、缺陷修复
- 不需要新的 MVP 能力拆分
- 不需要完整迭代计划
- 默认走轻量 `PRD -> SDD -> 按需 DDD -> 实现映射`

### MVP 演化
- 需要验证或扩展核心想法
- 会新增或重排能力模块
- 会影响职责、接口、数据流、状态流或演进方向
- 必须进入完整迭代架构链

### 可停留在 PRD / 轻量路径的情况
- 需求主要是产品规则澄清
- 交互口径、协议语义、文案或验收标准调整
- 变化局限在单模块，且不会改变模块职责、接口边界或状态流
- 不需要能力拆分、迭代规划或节点回补

## 工作流
### MVP 大方案
1. `Requirement Intake & Triage`
2. `MVP / Idea Baseline`
3. `PRD Baseline`
4. `Global Architecture Charter / SDD`
5. `Capability Roadmap`
6. `Iteration Plan`
7. `Current Capability Design Packet`
8. `Current Iteration Contract`
9. `ADR`
10. `Iteration Freeze & Resume Note`

### 补丁 / 简单任务
1. `Requirement Intake & Triage`
2. 校验 PRD 或需求约束
3. 轻量 SDD
4. 按需 DDD
5. 实现映射

## 最小输出
### MVP 大方案
1. 结论摘要
2. `Requirement Intake & Triage`
3. `MVP / Idea Baseline`
4. `PRD Baseline`
5. `Global Architecture Charter / SDD`
6. `Capability Roadmap`
7. `Iteration Plan`
8. `Current Capability Design Packet`
9. `Current Iteration Contract`
10. `ADRs`
11. `Iteration Freeze & Resume Note`
12. 风险与后续建议

### 补丁 / 简单任务
1. 结论摘要
2. `Requirement Intake & Triage`
3. 约束分析
4. SDD
5. DDD 判断或 DDD 内容
6. 实现映射
7. 风险与取舍

## 执行纪律
- 触发后必须显式说明正在使用 `architecture-design`，并说明当前处于哪一步。
- 若需求属于 MVP 演化，编码前必须留下最小可见设计产物；至少包含 `Triage`、当前能力边界、代码落点。
- 若复用已有文档结论，必须说明复用了什么、当前改动影响什么，不能静默跳过。
- 用户即使直接要求“开始实现”，只要本质上是 MVP 演化，也必须先锁定当前轮能力边界。
- 每个实质性阶段结束后，必须留下可续接状态，例如：`Triage complete`、`Baseline frozen`、`Capability packet ready`、`Implementation in progress`、`Freeze note updated`。

## 读取参考
- 详细判断规则、检查清单、文档最小字段，读取 `references/ddd-sdd-best-practice.md`。
- 主文档负责说明主线；reference 负责模板与展开细节。

## 反模式
- 不做补丁 / MVP 分流，直接开始设计或编码
- 只有 `Capability Roadmap`，没有独立 `Iteration Plan`
- 明明是 MVP 演化，却跳过当前能力包直接改代码
- 接受临时节点，却不安排后续回补
- 把 PRD、SDD、DDD 写成互不推导的并列文档
