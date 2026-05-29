# AI 项目长期演化治理体系（当前认知总结）

## 一、我真正想解决的问题

我并不是单纯想“让 AI 写代码”。

我真正想解决的是：

> 在长期、多轮、动态演化的软件项目中，如何让多个“会失忆的 AI 执行者”，仍然能够维持项目的连续性、一致性与可演化性。

核心问题不是代码生成，而是：

* 决策连续性
* 项目历史连续性
* 多轮迭代连续性
* AI 能力边界控制
* 长任务的可续接性
* 演化过程中的组织稳定性

这本质上已经不是“prompt engineering”。

而是：

> AI 时代的软件组织治理问题。

---

# 二、为什么会自然走向 architecture-design

因为 AI 天生存在几个问题：

## 1. AI 不是连续的人

每一次聊天：

* 都像一个新成员加入项目
* 会重新理解系统
* 会重新推断边界
* 会重新做决策

所以必须有人维护：

* 长期原则
* 项目历史
* 当前进度
* 已验证与未验证能力
* 为什么当时这么设计

否则 AI 会不断：

* 重复试错
* 重复推翻
* 重复重构
* 用通用模式覆盖项目特殊历史

---

## 2. AI 默认会“统计蒸馏”

大模型倾向于：

* 泛化
* 平均正确
* 回归通用模式

但真实项目中：

很多关键决策恰恰是：

* 阶段性的
* 市场驱动的
* 特殊 trade-off
* 非通用的

因此必须有人保护：

> “项目自己的局部真理”。

---

## 3. 长期项目真正难的不是架构，而是历史

小项目：

* 重写成本低
* token 多一点问题不大

大项目真正困难的是：

> “为什么系统会演化成现在这样”。

包括：

* 哪些是长期稳定原则
* 哪些是 MVP 妥协
* 哪些是实验
* 哪些已经失败
* 哪些不应该被静默推翻

因此：

真正需要沉淀的不是代码，
而是：

> 高于代码的决策层。

---

# 三、我现在重新定义 architecture-design

architecture-design 不再是：

* DDD skill
* SDD skill
* 架构设计模板
* 全流程项目管理器

它真正的定位是：

> AI Project Governance Layer（AI 项目治理层）

或者：

> Project Decision Continuity Layer（项目决策连续性层）

它的目标不是：

* 指导 AI 如何写代码

而是：

> 维护项目长期组织意识。

---

# 四、architecture-design 真正需要解决的四个问题

## 1. 决策连续性

让未来 AI 理解：

* 为什么系统会变成现在这样
* 哪些是长期原则
* 哪些是临时妥协
* 哪些已经验证
* 哪些不能轻易推翻

对应内容：

* MVP
* ADR
* 架构原则
* 历史决策
* rejected options

---

## 2. 当前状态连续性

让未来 AI 知道：

* 当前做到哪里
* 哪些 iteration 已完成
* 哪些 temporary node 未回补
* 下一步是什么
* 哪些工作被冻结

对应内容：

* freeze
* resume
* iteration
* next step
* unfinished work

---

## 3. AI 能力边界控制

当任务明显超出 AI 当前稳定能力时：

不允许：

* 乱写
* 失控重构
* 一次性设计完整系统

而是自动降级为：

* capability split
* staged delivery
* partial implementation
* temporary node
* iterative evolution

本质是：

> 复杂任务降级协议。

---

## 4. 多 session 长任务续接

不同对话中的 AI：

必须能够继续：

* 之前的 iteration
* 已冻结能力
* 未完成设计
* staged implementation

而不是重新设计整个系统。

---

# 五、为什么不能只有一个 architecture-design

因为之前的问题是：

一个 skill 同时承担了：

* PM
* 架构
* DDD
* SDD
* 演化
* 项目管理
* 实施 gate
* freeze 管理
* ADR
* iteration

导致：

* token 爆炸
* 使用复杂
* 心智负担极高

因此必须拆分。

---

# 六、最终结构（当前最佳实践）

## 1. architecture-design

只保留：

> 长期治理规则。

负责：

* stable vs temporary
* 什么时候必须进入迭代
* 什么时候必须降级
* 如何 freeze/resume
* 如何保持长期连续性

它不再负责：

* 完整架构设计
* DDD 细节
* SDD 模板
* iteration 全流程

---

## 2. mvp-evolution

负责：

* MVP baseline
* capability roadmap
* iteration planning
* 当前验证目标

解决：

> “现在到底在验证什么”。

---

## 3. project-memory

负责：

* ADR
* 历史原因
* rejected options
* 为什么这样设计
* 已失败路线

解决：

> “为什么系统会变成现在这样”。

---

## 4. iteration-execution

负责：

* 当前 iteration
* freeze/resume
* unfinished work
* next step
* temporary node

解决：

> “当前项目做到哪里”。

---

## 5. complexity-degradation

负责：

当 AI 无法稳定完成复杂任务时：

* capability split
* staged implementation
* partial delivery
* local evolution
* temporary node

解决：

> “AI 不会时不要乱写”。

---

# 七、核心思想

我不是在设计：

* prompt
* workflow
* 架构模板

而是在设计：

> AI 长期协作的软件组织治理系统。

它的目标不是：

* 绝对正确
* 完美架构

而是：

> 在长期动态演化中，保持项目意识不丢失。

---

# 八、最终原则

## 1. 代码不是最重要的

真正重要的是：

* 决策
* 边界
* 取舍
* 历史
* 当前阶段目标

代码只是某一阶段的实现结果。

---

## 2. 已验证核心保持稳定

对：

* 世界观
* 核心交互
* 已验证能力

保持保守。

---

## 3. 未验证能力允许临时实现

允许：

* MVP shortcut
* temporary node
* staged evolution

因为很多东西：

* 只有市场知道
* 只有用户反馈知道

不能提前过度设计。

---

## 4. AI 不负责最终决策

AI：

* 可以执行
* 可以分析
* 可以建议

但：

* 最终 trade-off
* 长期方向
* 阶段性取舍

仍然属于项目 owner。

---

# 九、当前最终认知

我现在已经不再把：

* architecture-design
* DDD
* SDD
* MVP
* iteration

看成：

> “工程流程”。

而是：

> AI 时代的软件组织记忆系统。

它存在的目的不是：

* 让 AI 更聪明

而是：

> 让项目在长期演化中，不会失去自己。
