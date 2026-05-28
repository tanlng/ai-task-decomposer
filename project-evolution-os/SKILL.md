---
name: project-evolution-os
description: 项目推进总控。根据 architecture-design 产出的分流结论、Iteration Plan、当前轮契约、稳定节点与临时节点，推进开发记录、状态流转、提测、发布、日报与下一步工作选择。复杂 Bug 优先进入定位阶段。
---

# project-evolution-os

## 何时使用
- 推进项目
- 记录进度
- 判断下一步做什么
- 汇总当前开发状态
- 基于迭代计划选择当前轮工作
- 提测、发布、日报

## 依赖输入
### 补丁
- `Requirement Intake & Triage`
- 轻量 `PRD / SDD / 按需 DDD`（若存在）

### MVP 演化
- `Requirement Intake & Triage`
- `MVP / Idea Baseline`
- `PRD Baseline`
- `Global Architecture Charter / SDD`
- `Capability Roadmap`
- `Iteration Plan`
- `Current Iteration Contract`
- `Iteration Freeze & Resume Note`

## 推进规则
1. 先看需求分流，再判断状态；不要跳过 `补丁 / MVP 演化` 分流。
2. 对 MVP 大方案，未完成 `Triage`、`Baseline`、当前轮契约前，不标记为可开发。
3. `Capability Roadmap` 只说明模块拆分；真正的推进依据是 `Iteration Plan` 和 `Current Iteration Contract`。
4. 默认优先从当前轮、依赖满足的 `稳定节点` 开工。
5. `临时节点` 可以推进，但必须同时指出后续回补轮次与风险。
6. 若 `Iteration Plan` 或当前能力包标记需要 DDD，则对应轮次必须补齐。

## 默认动作
### 补丁
1. 确认属于补丁
2. 判断是否需要轻量 PRD / SDD / DDD
3. 标记状态、下一步动作
4. 推进开发、提测、发布

### MVP 演化
1. 确认已进入 MVP 演化链路
2. 检查 `MVP / Idea Baseline`、`PRD Baseline`、`Global Architecture Charter / SDD`
3. 根据 `Iteration Plan` 判断当前轮次
4. 根据 `Current Iteration Contract` 锁定本轮边界
5. 优先选择稳定节点
6. 完成后更新对 `Iteration Freeze & Resume Note` 的状态理解

## “开始工作”默认规则
- 若当前轮存在依赖已满足的稳定节点，优先推荐它。
- 若没有可直接推进的稳定节点，先说明阻塞，再判断是否需要补 PRD / SDD / DDD / 节点回补。
- 若只能推进临时节点，必须明确这属于临时推进，并说明后续回补轮次。

## 最小输出
1. 当前阶段
2. 当前状态
3. 当前需求分流
4. 当前迭代 / 当前轮次
5. 当前稳定节点
6. 当前临时节点与回补轮次
7. 下一步动作
8. 本轮成果物
9. 风险提醒
10. 状态更新建议

## 反模式
- 不做补丁 / MVP 分流，直接推进状态
- 只看 `Capability Roadmap`，忽略 `Iteration Plan`
- 没有当前轮契约就判断“开始做哪个模块”
- 明知道是临时节点，却不记录回补轮次
- 有稳定节点不做，跳去做未排入当前轮的工作
