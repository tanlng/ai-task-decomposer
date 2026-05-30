---
name: architecture-design
description: AI 项目治理层。适用于需要判定 stable vs temporary、是否进入迭代、何时 freeze/resume、如何保持多 session 决策连续性的请求；MVP 规划用 mvp-evolution，历史决策用 project-memory，当前推进用 iteration-execution，复杂任务降级用 complexity-degradation。
---

# architecture-design

## What To Use It For
- 判断一个请求是否已经进入“项目治理问题”，而不是单点实现问题
- 规定哪些原则必须长期稳定，哪些内容允许临时存在
- 决定什么时候必须进入迭代，什么时候可以先 freeze 或 resume
- 为后续 skill 指定正确入口，避免让多个 skill 竞争同一个问题

## Core Heuristics
1. 先保护项目连续性，再讨论局部最优实现。
2. 默认把代码看成阶段性结果，把决策、边界、历史和阶段目标看成核心资产。
3. stable 原则一旦确认，不允许被静默推翻。
4. temporary 节点可以存在，但必须带着回看条件和退出条件。
5. 本 skill 只负责治理规则，不代替 MVP 规划、项目记忆、当前迭代执行或复杂度降级。

## Workflow
1. 先判断当前问题是不是以下四类之一：
   - “现在验证什么” -> `mvp-evolution`
   - “为什么现在这样” -> `project-memory`
   - “当前做到哪里” -> `iteration-execution`
   - “任务太复杂要降级” -> `complexity-degradation`
2. 如果不是以上四类，而是需要先定义长期规则，再由本 skill 接管。
3. 明确当前请求里的 stable 原则、temporary 允许项、freeze/resume 条件。
4. 指定后续 owner skill，避免继续在治理层展开执行细节。

## Minimal Output
1. 问题是否属于治理层
2. stable 原则
3. temporary 允许项
4. freeze / resume 规则
5. 后续应切换到的 skill

## Anti-Patterns
- 把本 skill 当成 SDD / DDD / 全流程方案模板
- 直接在治理层展开 capability 拆分、ADR 记录或当前轮推进
- 允许 temporary 节点存在，却不给回看条件
- 用“继续做代码”绕过是否需要进入迭代的判断
