# CV/ML/DL Reading Framework

Use this framework for computer vision, AI, machine learning, and deep learning papers.

## 1. 基本信息

Extract:

- Title
- Authors
- Venue / Year
- Local file path
- Code / project page if the paper text provides it
- Research area
- Paper type: `method`, `dataset`, `benchmark`, `survey`, `application`, `theory`

## 2. 一句话总结

Write 1-2 sentences. Do not restate the abstract. State:

- task
- core idea
- claimed benefit

## 3. 论文定位

Clarify:

- What task does the paper solve?
- Which research line does it belong to?
- What type of methods does it improve, replace, or complement?
- What is its position among related methods?

## 4. 研究问题与动机

Assess:

- What limitation of prior work motivates the paper?
- Is the limitation real and important?
- Is the problem about performance, efficiency, robustness, generalization, data efficiency, annotation cost, interpretability, or deployment?
- Is the problem definition clear?
- Does the paper exaggerate a weakness or construct a strawman?

## 5. 方法拆解

Keep this section about algorithmic design, not training logistics.

Analyze:

- input and output
- overall pipeline
- key modules
- model architecture
- objective / loss function
- feature transformation
- alignment mechanism
- inference procedure
- algorithmic novelty

Explain why the key design might work. For long outputs, begin with the core mechanism before listing modules.

## 6. 核心创新点

Separate claimed and actual contributions:

- Author-claimed contributions
- Actual technical contribution
- Conceptual contribution
- Engineering contribution
- Whether it is mainly a recombination of existing ideas
- The most reusable idea

## 7. 实验设置

Put training and implementation conditions here:

- datasets
- evaluation metrics
- baselines
- teacher / student setup when relevant
- optimizer
- learning rate schedule
- batch size
- epochs
- augmentation
- pretrained model
- temperature
- loss weights
- compute budget if central to the claim
- implementation details needed to understand the evidence

The goal is to understand experimental conditions, not to perform a full reproduction audit.

## 8. 实验结果分析

Assess:

- What does the main result table show?
- Where does the method improve over baselines?
- Is the improvement meaningful?
- Does `ablation study` support each key claim?
- Do qualitative results support the argument?
- Are failure cases shown?
- Is there possible `cherry-picking`?
- Are variance, multiple runs, or statistical significance needed but missing?

## 9. 可信度与证据强度

Focus on whether the evidence supports the claims:

- Are baselines reasonable?
- Are comparisons fair?
- Are metrics appropriate?
- Does the evidence support the main claim?
- Is there possible `dataset leakage`?
- Is there an `unfair comparison` risk?
- Are important experiments missing?
- Does the paper overclaim beyond its evidence?
- Is code availability mentioned, as auxiliary context only?

Do not turn this section into a detailed reproduction checklist.

## 10. 局限与问题

Separate:

- limitations acknowledged by the authors
- limitations inferred from the paper
- likely failure cases
- sensitivity to assumptions
- scalability concerns
- unverified claims

## 11-13. Research Use

Use the KD lens when relevant, then summarize:

- reusable ideas
- reusable modules
- reusable losses
- reusable experiment designs
- related-work statements
- follow-up research questions
