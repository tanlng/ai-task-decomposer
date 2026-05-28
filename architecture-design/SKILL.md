---
name: architecture-design
description: 系统架构设计与演化。优先处理那些表面像“新功能定义/需求讨论”，实质却需要做补丁与 MVP 分流、方案设计、能力拆分、迭代规划、模块边界设计、接口/数据流/状态流收敛的请求；先把新需求分流为补丁或 MVP 演化，再用 MVP 作为最高筛选器，把想法收敛为可迭代交付的架构方案，并按能力模块推进 PRD、SDD、按需 DDD、显式 Iteration Plan、稳定/临时节点管理与 Implementation Readiness。适用于项目早期方案设计、架构改造、职责重划、跨模块链路调整、外部系统接入，以及需要多轮协作的大方案。
---

# architecture-design

## 何时使用
- 设计系统架构或大方案
- 处理表面像 PRD、实质需要先做方案设计或 MVP 演化判断的需求
- 判断新需求应该走补丁处理，还是进入 MVP 演化链路
- 拆分能力模块、迭代顺序与回补计划
- 收敛跨模块职责、数据流、接口和状态流
- 判断何时需要进入 DDD
- 需要让方案可中断、可续接、可长期演化

## 读取参考
- 需要详细判断规则、检查清单或输出模板时，读取 `references/ddd-sdd-best-practice.md`。
- 需要先澄清产品行为、交互规则、协议语义或验收标准时，在本 skill 内先补齐 PRD 基线，不要跳过 PRD 直接做架构。

## 核心定位
1. 先完善想法和 MVP，再完善完整架构。
2. 先做补丁 / MVP 分流，再决定是否进入完整迭代架构链。
3. 让 PRD、SDD、DDD 形成逐层收敛链，不把三者拆成并列附件。
4. 让 `Iteration Plan` 成为独立文档层，负责安排整个 MVP 期的多轮推进。
5. 用 `稳定节点 / 临时节点` 标记哪些工作可直接继续，哪些必须在后续迭代中回补。
6. 沿用既有边界；仅在职责不清、扩展点缺失、同类逻辑散落或数据流绕路时提出架构演化。

## PRD 内嵌原则
在本 skill 内，PRD 不再作为独立 owner，而作为架构收敛链的前置输入层。

默认规则：
1. 先对齐 PRD，再进入 SDD / DDD 或实现映射。
2. 若已有 PRD 已覆盖当前能力，则按已有 PRD 收敛后续设计。
3. 若需求与已有 PRD 冲突，先更新 `PRD Baseline`，再继续架构收敛。
4. 若多文档口径冲突，先收敛出单一 PRD 基线，不要带着冲突进入架构设计。
5. 若需求只涉及产品规则、交互逻辑、协议语义、文案口径或验收标准，且不影响模块边界、接口、数据流、状态流或迭代顺序，可停留在 PRD 或轻量 `PRD -> SDD` 路径。
6. 若 PRD 一旦变更就会影响模块边界、数据流、职责划分、状态流、迭代顺序或性能模型，必须升级为完整 architecture-design 主导链路。

## 优先触发信号
出现以下信号时，即使需求表面在谈“功能定义”或“需求梳理”，也应优先由 architecture-design 主导：
- 需要先判断这是补丁还是 MVP 演化
- 需要决定先做哪一轮、如何拆能力模块、如何安排迭代
- 需求一旦落地就会影响模块边界、接口、数据流、状态流或系统职责
- 请求包含“怎么实现”“怎么拆”“先做什么”“后面怎么接着做”这类方案问题
- 需求明显需要多轮聊天或多轮实现
- 若只用 PRD 收敛，会掩盖真实的系统协作和演进问题

## Requirement Intake & Triage
收到需求后，先判断它属于哪一类：

- `补丁`
  - 局部修正、行为收敛、缺陷修复
  - 不需要新的 MVP 能力拆分
  - 不需要完整迭代计划
- `MVP 演化`
  - 需要验证或扩展核心想法
  - 会新增或重排能力模块
  - 会影响职责、接口、数据流、状态流或演进方向
  - 明显需要多轮聊天或多轮实现

默认规则：
- 补丁走轻量 `PRD -> 轻量 SDD -> 按需 DDD -> 实现映射`
- MVP 演化必须进入完整迭代架构链

## PRD-only / 轻量路径判定
以下情况允许停留在 PRD 或轻量路径，而不必展开完整 MVP 迭代架构：
- 需求主要是产品规则澄清
- 交互口径、协议语义、文案或验收标准调整
- 行为变化局限在单模块，且不会改变模块职责、接口边界或状态流
- 不需要能力模块拆分、迭代规划或节点回补计划

## 任务规模判定
- 简单任务：
  - 单模块或短链路
  - 一轮内可以稳定闭环
  - 不需要独立 `Iteration Plan`
- 大方案：
  - 跨多个模块或服务
  - 明显需要多轮聊天或多轮实现
  - 先后顺序会影响边界、接口或状态流
  - 若不先拆分，容易先跑通再返工

## 集成原则
1. 不新增平行的 SDD skill；SDD 仍然是 architecture-design 的前半段，DDD 是后半段。
2. PRD 定义要什么，SDD 定义系统如何协作，DDD 定义稳定业务规则和 ownership 归谁负责。
3. 项目早期或大方案未形成 `MVP / Idea Baseline` 前，不进入详细架构设计。
4. 未通过 `MVP Alignment` 的能力模块，不进入当前轮 `PRD -> SDD -> DDD` 设计链。
5. `Iteration Plan` 必须独立于 `Capability Roadmap` 和 `Current Iteration Contract` 存在。
6. DDD 不是所有模块必经步骤，但必须显式判断“是否需要 DDD”及其理由。
7. `稳定节点` 表示可直接继续开发；`临时节点` 表示为推进当前迭代暂时接受，但必须在后续迭代中显式回补。
8. 不为未来可能永远不会做的扩展提前设计重型边界；只保留支撑 MVP 演进所需的最小扩展点。

## MVP 大方案默认工作流
1. 产出 `Requirement Intake & Triage`，先判定这是补丁还是 MVP 演化。
2. 冻结 `MVP / Idea Baseline`，明确当前要验证的核心想法、MVP 成功标准、范围与非范围。
3. 产出全局 `PRD Baseline`，说明当前 MVP 到底要什么、要验证什么行为和验收口径。
4. 基于 MVP 产出 `Global Architecture Charter / SDD`，只定义当前阶段必须稳定的系统目标、模块版图和主协作链。
5. 建立 `Capability Roadmap`，把大问题拆成能力模块，并标记模块依赖、推荐顺序、DDD 需求以及临时节点风险。
6. 产出独立 `Iteration Plan`：
   - 排完整个 MVP 期
   - 前 2-3 轮精确排
   - 后续轮次粗排并标记待进一步拆分
   - 明确哪一轮补 DDD、哪一轮回补临时节点
7. 为当前轮模块产出 `Current Capability Design Packet`：
   - `MVP Alignment`
   - `PRD Baseline for Capability`
   - `SDD for Capability`
   - `DDD Decision / DDD Content`
   - `Implementation Readiness`
8. 形成 `Current Iteration Contract`，明确这一轮做什么、不做什么以及完成定义。
9. 记录关键 `ADR`，说明为何当前为了 MVP 选择较轻方案、延后了哪些方案。
10. 本轮结束输出 `Iteration Freeze & Resume Note`，为后续多轮聊天或暂停恢复提供锚点，并显式列出新增临时节点及其回补轮次。

## 补丁 / 简单任务默认工作流
1. 产出 `Requirement Intake & Triage`，确认属于补丁而不是 MVP 演化。
2. 校验 PRD 或需求约束是否稳定。
3. 产出轻量 SDD，至少覆盖职责、接口、数据流、异常路径和关键约束。
4. 若涉及规则归属、边界演化、替换性或反腐边界，再进入 DDD。
5. 映射实现：目录、模块 owner、扩展点、测试与发布影响。

## 大方案必须产出的文档集
### 1. Requirement Intake & Triage
用于入口分流，必须包含：
- 需求摘要
- 补丁 / MVP 判定
- 判定理由
- 是否进入完整迭代架构链

### 2. MVP / Idea Baseline
用于冻结项目初期的目标锚点，必须包含：
- 核心想法是什么
- 当前要验证的用户价值或系统价值
- MVP 成功标准
- MVP 范围与非范围
- 当前阶段不做什么
- 哪些能力只是愿景，不属于当前 MVP

### 3. PRD Baseline
用于说明当前 MVP 到底要什么，必须包含：
- 目标能力
- 用户或业务规则
- 输入输出
- 验收标准
- 边界条件
- 与已有 PRD 的关系或差异
- 若有冲突，需要说明收敛后的唯一口径

### 4. Global Architecture Charter / SDD
用于约束全局方向，必须包含：
- 受 MVP 约束后的系统目标
- 核心能力模块版图
- 模块主边界
- 主数据流或主协作链
- 当前阶段架构主线
- 为未来演进保留的最小扩展点
- 明确哪些设计暂不展开

### 5. Capability Roadmap
用于拆分能力模块和排序，必须为每个模块说明：
- 模块名称
- 要验证的核心想法
- 是否属于 MVP 必需能力
- 前置依赖
- 影响边界
- 推荐迭代顺序
- 完成后可验证什么结果
- 是否需要进入 DDD
- 是否存在临时节点风险

### 6. Iteration Plan
用于安排整个 MVP 期的多轮计划，必须包含：
- MVP 期总目标
- 迭代轮次总览
- 前 2-3 轮精确计划
- 后续轮次粗略计划
- 每轮目标
- 每轮包含的能力模块
- 每轮前置依赖
- 每轮预期增量
- 每轮进入条件
- 每轮退出条件
- 每轮稳定节点
- 每轮临时节点
- 每轮后续需回补项

### 7. Current Capability Design Packet
用于当前轮模块的完整设计闭环，固定包含以下内容。

#### MVP Alignment
- 它验证什么核心想法
- 为什么是 MVP 必需能力
- 若现在不做，会影响什么
- 本轮不做的相关扩展是什么

#### PRD Baseline for Capability
- 模块目标
- 用户或业务规则
- 输入输出
- 验收标准
- 边界条件

#### SDD for Capability
- 模块职责
- 协作模块
- 调用链或时序
- 数据流或状态流
- 接口契约
- 异常路径
- 可观测性与非功能约束

#### DDD Decision / DDD Content
- 是否需要 DDD
- 若需要：限界上下文、聚合或实体归属、领域服务、领域规则归属、领域事件、反腐边界
- 若不需要：明确写出不需要的理由

#### Implementation Readiness
- 代码落点
- owner
- 扩展点
- 测试建议
- 发布影响
- 未决项

### 8. Current Iteration Contract
用于约束本轮执行边界，必须包含：
- 本轮目标
- 本轮只做哪些 MVP 模块
- 不做哪些非 MVP 扩展
- 输入依赖
- 输出增量
- 完成定义
- 验收方法

### 9. ADR
用于记录关键决策，必须包含：
- 决策主题
- 备选方案
- 最终选择
- 为什么该选择更符合当前 MVP
- 被延后的方案是什么
- 什么条件下需要升级设计

### 10. Iteration Freeze & Resume Note
用于支持中断恢复，必须包含：
- 本轮完成了哪些 MVP 能力
- 哪些边界已冻结
- 哪些想法已被验证或尚未验证
- 哪些是稳定节点，可直接继续
- 本轮新增了哪些临时节点
- 后续哪一轮必须回补这些临时节点
- 若不回补会影响什么
- 下一轮推荐从哪个模块继续
- 哪些变化会触发重审 `MVP / Idea Baseline`

## 默认输出顺序
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

`Current Capability Design Packet` 内部顺序固定为：
1. `MVP Alignment`
2. `PRD Baseline`
3. `SDD`
4. `DDD Decision / DDD Content`
5. `Implementation Readiness`

对补丁 / 简单任务，可压缩为：
1. 结论摘要
2. `Requirement Intake & Triage`
3. 约束分析
4. SDD
5. DDD 判断或 DDD 内容
6. 实现映射
7. 风险与取舍

## 反模式
- 收到需求后不做补丁 / MVP 分流，直接开始设计
- 未形成 `MVP / Idea Baseline` 就展开全量架构
- 只有 `Capability Roadmap`，没有独立 `Iteration Plan`
- 把非 MVP 模块拉进当前轮详细设计
- 接受临时节点却不安排后续回补迭代
- 先做 DDD 再补 SDD
- 用 DDD 术语掩盖缺失的接口、数据流或调用链设计
- 把 PRD、SDD、DDD 写成互不推导的并列文档
- 只在聊天里讨论，不留下可续接的冻结点和决策记录
