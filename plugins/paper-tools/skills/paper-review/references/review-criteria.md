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
- Is the claimed mechanism plausible given the architecture, loss, optimization, or inference procedure?
- Are there mismatches between the motivation, method design, and what the method can actually guarantee?
- Are the key formulas, losses, constraints, or theoretical propositions correct and relevant to the claimed mechanism?
- Do derivations rely on hidden assumptions, unjustified approximations, or notation changes that alter the claim?
- Does the optimized objective actually encourage the behavior the paper claims?

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
- Do the experiments directly test the method's core mechanism or only report outcome gains?
- Do ablations isolate the proposed components from confounding implementation details?
- Do experiments test the consequences of important theoretical or formula-level claims?

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

- method mechanism and claim consistency
- formula/theory and claim consistency
- derivation gaps, hidden assumptions, unjustified relaxations, or objective-claim mismatch
- assumptions behind the architecture, objective, training strategy, or inference pipeline
- whether experiments validate the mechanism rather than only the final metric
- `baseline` fairness
- `ablation study` completeness
- `dataset` and metric suitability
- `claim-evidence alignment`
- `SOTA` claim strength
- `compute` fairness when efficiency is central
- `dataset leakage` risk
- `cherry-picking` risk
- robustness or out-of-domain evaluation when relevant

## Concern Selection Guidance

Prefer major concerns that expose a method-level or formula/theory-level weakness and then use experiments as supporting evidence. A strong major concern usually has this form:

```text
The method relies on assumption X or design choice Y. The paper does not justify why X/Y should hold in the target setting. The current experiments do not isolate or test this mechanism, so the main claim remains under-supported.
```

Formula/theory concerns are especially important when the paper uses equations, bounds, objectives, or derivations to justify novelty or validity. A strong formula-level concern usually has this form:

```text
The paper claims formula/objective X supports behavior Y, but the derivation assumes Z or optimizes a proxy that does not directly imply Y. Without clarifying this link or testing the predicted behavior empirically, the claimed mechanism remains unsupported.
```

Use pure experimental concerns as major concerns only when the missing evidence is necessary for the central claim, such as an omitted closest baseline, an ablation needed to validate the proposed mechanism, or an evaluation setting required by the paper's own motivation.
