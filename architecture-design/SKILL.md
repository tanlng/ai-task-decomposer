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
### MVP 大方案四步法
#### Step 1. Baseline
- 产物：
  - `Requirement Intake & Triage`
  - `MVP / Idea Baseline`
  - `PRD Baseline`
- Gate：
  - 未完成这 3 项，不进入架构拆分或代码实现

#### Step 2. Planning
- 产物：
  - `Global Architecture Charter / SDD`
  - `Capability Roadmap`
  - `Iteration Plan`
- Gate：
  - 未完成拆分工作文档，不进入具体能力实现
  - 若用户追问“拆分工作文档在哪里”，直接判定当前仍停留在 Step 2 未完成

#### Step 3. Current Iteration
- 产物：
  - `Current Capability Design Packet`
  - `Current Iteration Contract`
  - 按需 `ADR`
- Gate：
  - 未完成当前能力包和当前轮契约，不进入代码修改

#### Step 4. Implementation & Freeze
- 产物：
  - 代码实现
  - `Iteration Freeze & Resume Note`
- Gate：
  - 实现完成后必须更新冻结点
  - 不能只报测试通过或口头标记 `Freeze note updated`

### 补丁 / 简单任务
1. `Requirement Intake & Triage`
2. 校验 PRD 或需求约束
3. 轻量 SDD
4. 按需 DDD
5. 实现映射

## 最小输出
### MVP 大方案
1. 结论摘要
2. 当前 Step
3. `Requirement Intake & Triage`
4. `MVP / Idea Baseline`
5. `PRD Baseline`
6. `Global Architecture Charter / SDD`
7. `Capability Roadmap`
8. `Iteration Plan`
9. `Current Capability Design Packet`
10. `Current Iteration Contract`
11. `ADRs`
12. `Iteration Freeze & Resume Note`
13. 风险与后续建议

### 补丁 / 简单任务
1. 结论摘要
2. `Requirement Intake & Triage`
3. 约束分析
4. SDD
5. DDD 判断或 DDD 内容
6. 实现映射
7. 风险与取舍

## 文档落盘要求
- 若需求属于 `MVP 演化`，上述核心产物不能只出现在回复里，必须写入项目内可追踪文档。
- 优先复用目标项目已有文档目录与命名习惯；若没有明确约定，默认在目标项目下使用：
  - `docs/architecture/mvp-baseline.md`
  - `docs/architecture/iteration-plan.md`
  - `docs/architecture/capabilities/<capability-slug>.md`
  - `docs/architecture/freeze-notes.md`
  - `docs/architecture/adr/<adr-slug>.md`
- 本轮若只实现一个能力切片，至少要落盘：
  - `mvp-baseline.md` 中与当前切片相关的目标/范围更新
  - `iteration-plan.md` 中当前轮与后续回补信息
  - 对应能力包文档
  - `freeze-notes.md` 中本轮冻结点
- 若用户要求“继续实现”，也要先更新受影响文档，再进入代码修改。

## 执行纪律
- 触发后必须显式说明正在使用 `architecture-design`，并说明当前处于哪一步。
- 若需求属于 MVP 演化，编码前必须留下最小可见设计产物，并完成对应文档落盘；至少包含 `Triage`、当前能力边界、代码落点与文档路径。
- 若复用已有文档结论，必须说明复用了什么、当前改动影响什么，不能静默跳过。
- 用户即使直接要求“开始实现”，只要本质上是 MVP 演化，也必须先锁定当前轮能力边界。
- 每个实质性阶段结束后，必须留下可续接状态，例如：`Triage complete`、`Baseline frozen`、`Capability packet ready`、`Implementation in progress`、`Freeze note updated`。
- 阶段状态不能只写在回复里；对 MVP 演化，至少同步到对应的 freeze note 或 iteration plan 文档。
- 对 MVP 演化，不允许跳 Step。
- 若 Step 2 的 `Capability Roadmap` 或 `Iteration Plan` 缺失，就不能声称“开始实现新的 MVP”。
- 若 Step 4 已发生，但前置 Step 文档缺失，必须先承认当前实现违反技能流程，再回补文档，不得把这种情况表述成“只是这轮漏了”。

## 读取参考
- 详细判断规则、检查清单、文档最小字段，读取 `references/ddd-sdd-best-practice.md`。
- 主文档负责说明主线；reference 负责模板与展开细节。

## 反模式
- 不做补丁 / MVP 分流，直接开始设计或编码
- 只有 `Capability Roadmap`，没有独立 `Iteration Plan`
- 明明是 MVP 演化，却跳过当前能力包直接改代码
- 接受临时节点，却不安排后续回补
- 把 PRD、SDD、DDD 写成互不推导的并列文档
- 只在回复里口头给出 `Triage` / `Iteration Plan` / `Freeze note`，却没有写入项目文档
- 用“我这轮漏了”来掩盖 Step Gate 实际未通过
