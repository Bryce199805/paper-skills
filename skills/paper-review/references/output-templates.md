# Output Templates

## Quick Mode Template

```markdown
# Paper Understanding Report

## 1. 论文基本问题与目标

## 2. 方法核心机制

## 3. 关键公式 / 理论依据 / 目标函数

## 4. 关键设计与假设

## 5. 作者声称的贡献

## 6. 实验如何支撑论文主张

## 7. 当前理解的不确定点

# Initial Review Report

## 1. 初步审稿定位

## 2. 方法层面的主要优点

## 3. 方法层面的主要漏洞

## 4. 公式 / 理论层面的主要漏洞

## 5. 实验对上述漏洞的支持或不足

## 6. 次要问题

## 7. 私人 KD / 研究启发（仅在相关时保留）

## 8. 初步评分与审稿倾向

# Reviewer Comments

## Ratings

- Technical Quality: X/5  
  Rationale: ...
- Novelty / Originality: X/5  
  Rationale: ...
- Experimental Validation: X/5  
  Rationale: ...
- Clarity / Presentation: X/5  
  Rationale: ...
- Significance / Impact: X/5  
  Rationale: ...
- Transparency: X/5  
  Rationale: ...
- Reviewer Confidence: X/5  
  Rationale: ...
- Overall Recommendation: ...

## Summary

## Strengths

## Major Concerns

## Minor Concerns

## Questions for Authors
```

Do not include an explicit recommendation sentence in `Summary`, `Major Concerns`, or the final paragraph.

## Collaborative Mode Stage 1 Template

```markdown
# Paper Understanding Report

## 1. 论文基本问题与目标

## 2. 方法核心机制

## 3. 关键公式 / 理论依据 / 目标函数

## 4. 关键设计与假设

## 5. 作者声称的贡献

## 6. 实验如何支撑论文主张

## 7. 当前理解的不确定点

# Initial Review Report

## 1. 初步审稿定位

## 2. 方法层面的主要优点

## 3. Candidate Method-Level Major Concerns

## 4. Candidate Formula / Theory-Level Major Concerns

## 5. Experiment Evidence for the Above Concerns

## 6. Pure Experimental Gaps Not Yet Major Concerns

## 7. Candidate Minor Concerns

## 8. 私人 KD / 研究启发（仅在相关时保留）

## 9. Preliminary Ratings

## 10. Missing Information / Uncertainty

## 11. Reviewer Decision Points
```

End by asking the user to confirm:

- Is the `Paper Understanding Report` accurate enough?
- Which candidate concerns should be used as `Major Concerns`?
- Are the preliminary ratings appropriate?
- What `Overall Recommendation` direction should be selected?
- Should final English reviewer comments be drafted now?

## Formal English Comment Rules

Formal comments must be:

- English
- polite but direct
- evidence-based
- specific enough for authors to respond

Each `Major Concern` should include:

- the issue
- why it affects the paper
- what evidence, analysis, or revision would address it

Major concerns should usually be method-centered or formula/theory-centered and evidence-supported. Use experiments to show why the method or formula/theory concern is unresolved, rather than listing missing experiments without explaining the affected claim.

Avoid:

- "I recommend rejection" or similar body-text recommendation statements
- private research inspiration
- unsupported claims about author intent
- overly soft language that obscures the criticism

Prefer:

```text
The current baseline comparison is insufficient to support the claimed advantage over prior work. In particular, ...
```

Avoid:

```text
It might be nice if the authors could maybe consider adding more baselines.
```
