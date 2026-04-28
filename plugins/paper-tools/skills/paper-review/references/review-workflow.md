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

1. `Review Analysis Note` in Chinese.
2. `Reviewer Comments` in English.

The analysis note should be concise but judgment-oriented. It should identify the likely review stance, strongest concerns, and evidence quality.

The formal comments should be submission-ready but should not include an explicit recommendation sentence in the body.

## Collaborative Mode

Use collaborative mode by default.

Stage 1 output:

1. Paper summary for review
2. Claimed contributions
3. Evidence check
4. Potential strengths
5. Candidate major concerns
6. Candidate minor concerns
7. Private KD/research relevance when useful
8. Preliminary ratings
9. Reviewer decision points

Stop after Stage 1 and ask the user to confirm the major concerns, rating direction, and whether to draft final comments.

Stage 2 output, after user confirmation:

1. Updated ratings if needed
2. English reviewer comments
3. Optional revision of tone or strength if the user requests it

## Review Judgment Rules

Prioritize issues that affect:

- validity of the main claim
- novelty or originality
- technical soundness
- experimental sufficiency
- baseline fairness
- clarity of the contribution
- suitability of datasets and metrics
- claim-evidence alignment

Do not over-weight issues that are merely preferences, alternative design choices, or private research interests.

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
