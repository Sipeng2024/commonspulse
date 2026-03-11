# [Hackathon Submission] CommonsPulse

## 项目名称
CommonsPulse

## 参赛赛道
影响力评估（Impact Evaluation）

## 项目简介（TL;DR）
CommonsPulse 是一个面向 GCC / DAO / grant program 的 **上游 portfolio watcher / evidence pipeline**。它持续抓取项目的公开进展信号（如 GitHub 提交、release、issue 负载等），生成可审计的 markdown + JSON snapshots，帮助资助方低成本地维护持续更新的 portfolio evidence layer，而不是依赖季度人工整理。它不尝试替代 reviewer，也不做黑箱打分，而是把分散的公开证据整理成可复用、可下游消费的结构化输入。这样既能提升运营效率，也能为后续 review workflow、dashboard 或人工评审提供稳定上游。

## 要解决的真实问题
随着 GCC Portfolio 扩大，项目跟踪会越来越依赖高频、重复、但价值密度不高的人工劳动：运营人员需要在 GitHub、官网、博客、社媒和文档之间来回切换，判断一个项目是否仍在推进、是否交付了有意义的里程碑、是否出现停滞或偏航风险。这样的流程有三个问题：

1. **信息分散**：公开信号分布在多个平台，难以形成统一视图。
2. **跟踪滞后**：很多状态只能等到季度汇总时才暴露出来，问题发现过晚。
3. **不可复用**：不同项目、不同 grant round 都在重复相似的手工整理工作。

在 GCC/DAO 场景里，这不只是内部效率问题，也会影响社区透明度：外部成员很难持续、低成本地了解一个被资助项目是否真的在推进。

## 方案与技术实现
CommonsPulse 的设计目标不是“自动决定项目好坏”，也不是 reviewer workbench，而是构建一个 **evidence-based upstream monitoring agent**，负责收集公开证据、提炼进展信号，并输出可供下游系统复用的 portfolio snapshots。

当前 MVP 包含以下工作流：

1. **Source ingestion**
   - 从 YAML 配置读取待跟踪项目列表。
   - 当前优先接入 GitHub 公开 API，抓取 repo 元数据、最近提交、最近 release。

2. **Evidence extraction**
   - 抽取项目的 stars / forks / open issues / latest commit / latest release / repo description 等基础证据。
   - 所有结论都保留原始 evidence 字段，避免黑箱化。

3. **Signal classification**
   - 基于最近提交时间、最近 release 时间、issue 负载等指标，将项目在 development / release cadence / maintainability 维度上分类为 weak / medium / strong / unknown。
   - 输出的是上游监控信号，不是最终资助结论，也不是 reviewer 决策界面。

4. **Snapshot generation**
   - 生成 markdown 报告，方便运营快速巡检。
   - 同时生成 JSON snapshot，方便进一步接到 dashboard、review workbench、GitHub comment 或其他 agent 流程。

5. **Composable upstream layer**
   - CommonsPulse 明确把最终判断交给下游 review workflow 或人工 reviewer。
   - 后续重点是扩展数据源、统一 evidence schema、提高上游监控覆盖面。

仓库中已经提供：
- 可运行的 Python MVP
- 示例项目配置
- 示例输出报告
- demo 视频

## 代码仓库链接
https://github.com/Sipeng2024/commonspulse

## Demo 视频链接
https://github.com/Sipeng2024/commonspulse/blob/main/demo.mp4

## 公共物品属性
CommonsPulse 作为一个 grant evidence pipeline / portfolio watcher，天然具有公共物品属性：

1. **开源可复用**：代码以 MIT 协议开放，任何基金会、DAO、公共物品资助计划都可以直接复用。
2. **非 GCC 专属**：虽然问题来自 GCC 的 impact evaluation 场景，但方案本身适用于所有需要持续跟踪 portfolio 进展的资助组织。
3. **可审计**：输出是 markdown + JSON，保留公开证据字段，便于社区复核，不是封闭评分模型。
4. **可持续扩展**：后续可以接更多公开数据源（RSS、blog、X、docs、GitHub Issues/PR、release notes），逐步形成通用的 grant evidence infrastructure，供不同 review workbench 复用。

## 风险与依赖
当前版本识别到的主要风险包括：

1. **公开活动不等于真实进展**
   - 项目可能在私有仓库或线下推进，公共信号偏弱不一定意味着停滞。
   - 应对方式：CommonsPulse 只做 evidence aggregation + signal emission，不做自动裁决。

2. **不同项目的“健康信号”差异很大**
   - 有的项目 release 很少但推进稳定，有的项目 issue 很多但维护质量仍然很高。
   - 应对方式：后续加入项目类型感知和可配置阈值，而不是固定规则一刀切。

3. **LLM 或启发式规则可能误判上下文**
   - 应对方式：所有信号都附带 evidence，并把最终解释交给下游 review workflow 或人工 reviewer。

4. **当前数据源仍偏少**
   - MVP 先证明最小工作流可行，后续扩展到更多公开信号源，避免一开始过度工程。

## 联系邮箱
victor@bbd.sh

## 收款地址
0x0000000000000000000000000000000000000000 （temporary placeholder; can be updated before payout if needed）

## 提交确认
- [x] 我确认本提交信息真实有效，并愿意在 Issue 中进行公开讨论
- [x] 我理解四赛道独立评审，获奖结果与奖金发放以官方公告为准
