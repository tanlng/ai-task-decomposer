---
name: project-evolution-os
description: 项目推进总控。负责把需求按补丁或 MVP 演化分流，消费 architecture-design 产出的 PRD、SDD、Iteration Plan、稳定节点与临时节点，推进开发记录、状态流转、提测、发布、日报与下一步工作选择。复杂 Bug 优先进入定位阶段。
---

# project-evolution-os

## 何时使用
- 推进项目
- 记录进度
- 下一步做什么
- 梳理当前阶段
- 汇总当前开发状态
- 基于迭代计划选择下一步工作
- 提测
- 发布
- 日报

## 与 architecture-design 的衔接
- 对 `补丁` 需求：
  - 默认消费 `Requirement Intake & Triage`
  - 若需要设计，则消费轻量 `PRD / SDD / 按需 DDD`
  - 不强制要求完整 `Iteration Plan`
- 对 `MVP 演化`：
  - 默认消费 `Requirement Intake & Triage`
  - `MVP / Idea Baseline`
  - `PRD Baseline`
  - `Global Architecture Charter / SDD`
  - `Capability Roadmap`
  - `Iteration Plan`
  - `Current Iteration Contract`
  - `Iteration Freeze & Resume Note`

## 阶段约束
- 收到新需求后，先按 `补丁 / MVP 演化` 分流，不要直接进入开发状态判断。
- 对 MVP 大方案，未完成 `Requirement Intake & Triage` 和 `MVP / Idea Baseline` 前，不应标记为可开发。
- 对 MVP 大方案，未完成全局 `PRD Baseline` 与 `Global Architecture Charter / SDD` 前，不应进入模块级开发推进。
- `Capability Roadmap` 只回答模块拆分与依赖，不替代 `Iteration Plan`。
- `Iteration Plan` 是多轮推进依据；`Current Iteration Contract` 只约束当前轮执行边界。
- 未完成当前轮所需 SDD 的任务，不应标记为可开发，除非明确判断为无需系统设计的简单补丁。
- DDD 不是所有任务必经步骤，但只要 `Iteration Plan` 或当前轮设计包标记需要 DDD，就必须在对应轮次补齐。
- `稳定节点` 可作为默认开工点；`临时节点` 必须挂入后续迭代或回补任务，不能只记录不推进。

## 默认推进顺序
### 补丁
1. 读取 `Requirement Intake & Triage`，确认属于补丁。
2. 确认是否需要轻量 PRD / SDD / DDD。
3. 标记当前状态与下一步动作。
4. 推进开发、提测、发布。

### MVP 演化
1. 读取 `Requirement Intake & Triage`，确认进入 MVP 演化链路。
2. 确认 `MVP / Idea Baseline` 是否已冻结。
3. 确认 `PRD Baseline` 与 `Global Architecture Charter / SDD` 是否已完成。
4. 读取 `Capability Roadmap` 和 `Iteration Plan`，判断当前所在轮次。
5. 读取 `Current Iteration Contract`，确认本轮边界与完成定义。
6. 优先从 `稳定节点` 中选择下一步工作。
7. 若只能推进 `临时节点`，必须同时指出它所属的回补轮次和风险。
8. 本轮完成后更新 `Iteration Freeze & Resume Note` 对应的状态理解，并给出下一轮建议。

## “开始工作”默认规则
- 若当前处于 MVP 迭代中，优先选择：
  - 当前轮 `Current Iteration Contract` 内
  - 且标记为 `稳定节点`
  - 且依赖已满足
  的工作作为下一步。
- 若当前没有可直接推进的稳定节点：
  - 明确指出阻塞原因
  - 判断是否需要先补 SDD / DDD / PRD / 节点回补
  - 不要凭感觉跳到未计划的模块
- 若当前只有临时节点可做：
  - 明确这属于临时推进
  - 指出后续必须在哪一轮回补

## 默认输出
1. 当前阶段
2. 当前子阶段
3. 当前状态
4. 当前需求分流
5. 当前迭代 / 当前轮次
6. 当前稳定节点
7. 当前临时节点与回补轮次
8. 下一步动作
9. 本轮成果物
10. 风险提醒
11. 状态更新建议

## 输出要求
- `当前需求分流`：
  - 明确是补丁还是 MVP 演化
- `当前迭代 / 当前轮次`：
  - 对 MVP 大方案，说明来自 `Iteration Plan` 的第几轮
  - 若只有粗排而无精排，明确标记需要先补当前轮细化
- `当前稳定节点`：
  - 列出可直接开工的节点或模块
- `当前临时节点与回补轮次`：
  - 列出尚未回补的临时节点
  - 说明计划在哪一轮处理
- `下一步动作`：
  - 默认优先推荐稳定节点上的工作
  - 若推荐的不是稳定节点，要说明原因

## 反模式
- 不做补丁 / MVP 分流，直接推进状态
- 只看 `Capability Roadmap`，忽略 `Iteration Plan`
- 没有当前轮契约就直接判断“开始做哪个模块”
- 明知道是临时节点，却不记录回补轮次
- 有稳定节点不做，跳去做未排入当前轮的工作
- 把 architecture-design 的设计阶段和项目推进阶段混成一层，导致当前状态不可判断
