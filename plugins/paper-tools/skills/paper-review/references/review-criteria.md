# Review Criteria

Use 1-5 ratings:

- `5`: Excellent
- `4`: Good
- `3`: Fair / Borderline
- `2`: Weak
- `1`: Poor

Every rating must include a brief rationale.

## Core Ratings

Include these ratings by default:

- `Technical Quality`
- `Novelty / Originality`
- `Experimental Validation`
- `Clarity / Presentation`
- `Significance / Impact`
- `Transparency`
- `Reviewer Confidence`
- `Overall Recommendation`

Use these recommendation choices:

- `Strong Accept`
- `Weak Accept`
- `Borderline Accept`
- `Borderline Reject`
- `Weak Reject`
- `Strong Reject`

`Overall Recommendation` is a rating/selection, not a sentence to include in the formal comments body.

## Dimension Guidance

### Technical Quality

Assess:

- Is the method technically sound?
- Are assumptions clear and reasonable?
- Does the method follow from the stated problem?
- Are there hidden weaknesses in the formulation, objective, or algorithm?

### Novelty / Originality

Assess:

- What is actually new?
- Is the contribution conceptual, technical, empirical, or mainly engineering?
- Is it more than a recombination of existing components?
- Are differences from prior work clearly established?

### Experimental Validation

Assess:

- Are datasets appropriate?
- Are metrics appropriate?
- Are baselines recent and fair?
- Does the `ablation study` support the key claims?
- Are qualitative results convincing?
- Are missing experiments important enough to affect the claim?

### Clarity / Presentation

Assess:

- Is the problem statement clear?
- Is the method understandable?
- Are figures and tables readable?
- Are claims stated precisely?
- Is related work positioned fairly?

### Significance / Impact

Assess:

- Would the work matter to the target community?
- Does it solve an important problem?
- Are the gains meaningful?
- Does it open useful research directions?

### Transparency

Assess whether the paper provides enough information to judge the work:

- implementation details
- training setup
- data preprocessing
- model settings
- code or project page if provided

Do not turn this into a full reproduction audit.

### Reviewer Confidence

Assess how confident the reviewer is in the evaluation, considering:

- extraction quality
- domain fit
- completeness of the paper text
- whether appendix, figures, or code are needed

## CV/ML/DL Specific Checks

Check:

- `baseline` fairness
- `ablation study` completeness
- `dataset` and metric suitability
- `claim-evidence alignment`
- `SOTA` claim strength
- `compute` fairness when efficiency is central
- `dataset leakage` risk
- `cherry-picking` risk
- robustness or out-of-domain evaluation when relevant
