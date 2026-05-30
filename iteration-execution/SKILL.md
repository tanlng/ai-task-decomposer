---
name: iteration-execution
description: 迭代执行与续接。适用于判断当前项目做到哪里、当前 iteration 在做什么、哪些工作 freeze/resume、unfinished work 与 next step 是什么的请求；不负责重新做 MVP 规划或记录历史决策。
---

# iteration-execution

## What To Use It For
- 说明当前项目处于哪一轮
- 维护 freeze / resume 和 unfinished work
- 判断下一步该做什么
- 让不同 session 能接着同一轮往下做

## Core Heuristics
1. 先回答“当前做到哪里”，再回答“接下来做什么”。
2. 执行依据是 current iteration，而不是宽泛 roadmap。
3. stable 节点优先，temporary 节点必须带回补动作。
4. 任何可续接状态都要能让下一次 session 直接接手。
5. 本 skill 不重新定义 MVP 目标，也不承担历史解释。

## Workflow
1. 读取当前 iteration 边界和已完成内容。
2. 标记 stable 节点、temporary 节点和 unfinished work。
3. 判断当前是否处于 freeze、resume 或 active execution。
4. 给出 next step，只允许选择当前轮内、依赖满足的动作。
5. 若当前轮边界不清，退回 `mvp-evolution` 先补 iteration plan。

## Minimal Output
1. 当前 iteration
2. 当前状态
3. stable 节点
4. temporary 节点
5. unfinished work
6. next step
7. freeze / resume 信息

## Anti-Patterns
- 只看 roadmap 就安排当前工作
- 当前轮边界不清还继续推进
- 明知是 temporary 节点却不记录回补
- 用状态播报替代真正的可续接信息
