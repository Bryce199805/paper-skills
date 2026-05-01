# Review Workflow

## Input Handling

Review one paper at a time. Prefer local files:

- `.pdf`
- `.tex`
- `.md`
- `.txt`

Use `scripts/extract_paper_text.py` when available. For PDFs, account for two-column extraction risk. If the extraction is unreliable, state the limitation before making strong judgments.

## Quick Mode

Use quick mode when the user wants direct output.

Output order:

1. `Paper Understanding Report` in Chinese.
2. `Initial Review Report` in Chinese.
3. `Reviewer Comments` in English.

The paper understanding report should help the reviewer catch up with an unfamiliar manuscript. It should explain the task, motivation, method mechanism, key formulas or derivations, architecture or objective design, assumptions, claimed contributions, and how the experiments are supposed to support the claims.

The initial review report should be judgment-oriented. It should identify the likely review stance, strongest method-level concerns, and how experiments support or weaken those concerns.

The formal comments should be submission-ready but should not include an explicit recommendation sentence in the body.

## Collaborative Mode

Use collaborative mode by default.

Stage 1 output:

1. `Paper Understanding Report`
2. `Initial Review Report`

The paper understanding report comes first. It should be a precision reading document, not a review verdict. It should make the method legible enough that the user can discuss the manuscript without rereading from scratch.

The initial review report comes second. It should use the understanding report as its basis and distinguish:

- method-level vulnerabilities
- formula/theory-level vulnerabilities
- experiment-supported evidence for those vulnerabilities
- pure experimental gaps that are not yet method-level concerns
- uncertainties caused by missing appendix, figures, equations, or code

Stop after Stage 1 and ask the user to confirm the paper understanding, major concerns, rating direction, and whether to draft final comments.

Stage 2 output, after user confirmation:

1. Updated ratings if needed
2. English reviewer comments
3. Optional revision of tone or strength if the user requests it

## Review Judgment Rules

Use this reasoning order:

1. Understand the method's intended mechanism.
2. Trace the key formulas, objectives, losses, constraints, or theoretical propositions that define the method.
3. Identify the assumptions or design choices the method depends on.
4. Check whether those assumptions are justified theoretically, mathematically, architecturally, or empirically.
5. Use experiments to test the method-level or formula-level concern, not as a standalone checklist of missing results.
6. Convert only claim-relevant weaknesses into major concerns.

Prioritize issues that affect:

- validity of the main claim
- novelty or originality
- technical soundness
- method mechanism and design justification
- correctness and relevance of formulas, derivations, objectives, and theoretical claims
- consistency between problem formulation, method design, and objective
- experimental sufficiency
- baseline fairness
- clarity of the contribution
- suitability of datasets and metrics
- claim-evidence alignment

Do not over-weight issues that are merely preferences, alternative design choices, private research interests, or isolated missing experiments without a clear connection to the paper's claims.

When discussing experiments, prefer this structure:

```text
Method/formula concern -> why existing experiments do or do not test it -> what evidence would resolve it
```

Avoid treating every absent baseline, dataset, ablation, or metric as a major flaw. Missing experiments matter most when they are needed to validate a central mechanism, compare against the most relevant alternative, or support a strong claim.

When discussing formulas or theory, prefer this structure:

```text
Formula/theory claim -> hidden assumption or derivation gap -> effect on the method claim -> theoretical clarification or empirical test that would resolve it
```

Do not ignore equations as presentation details. A flawed loss, unjustified relaxation, unsupported bound, inconsistent notation, or mismatch between the optimized objective and claimed behavior can be a major concern when it affects the paper's central contribution.

## Formal Tone

Write formal comments as:

- professional
- polite
- direct
- evidence-based
- concise

For each major concern, prefer:

```text
Issue -> Impact -> Requested evidence or revision
```

Avoid:

- hostile wording
- vague hedging
- unsupported accusations
- turning private research inspiration into author-facing criticism
