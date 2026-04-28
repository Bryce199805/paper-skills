# Output Templates

## Quick Mode Template

```markdown
# Review Analysis Note

## 1. 论文概述与审稿定位

## 2. 作者声称的贡献

## 3. 证据与实验支撑

## 4. 潜在优点

## 5. 主要问题判断

## 6. 次要问题判断

## 7. 私人 KD / 研究启发

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
# Review Analysis Note

## 1. 论文概述与审稿定位

## 2. 作者声称的贡献

## 3. 证据与实验支撑

## 4. 潜在优点

## 5. Candidate Major Concerns

## 6. Candidate Minor Concerns

## 7. 私人 KD / 研究启发

## 8. Preliminary Ratings

## 9. Missing Information / Uncertainty

## 10. Reviewer Decision Points
```

End by asking the user to confirm:

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
