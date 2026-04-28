---
name: paper-review
description: Academic peer review of one local computer science paper, especially computer vision, AI, machine learning, deep learning, and knowledge distillation papers. Use when the user asks to review, referee, evaluate, critique, score, or draft reviewer comments for a single local PDF, TeX, Markdown, or text paper. Supports quick mode for one-shot analysis plus formal comments, and collaborative mode for staged reviewer-agent interaction before drafting final English comments.
---

# Paper Review

Use this skill to review one paper at a time. The default domain is CV/ML/DL, with private reviewer-side awareness of knowledge distillation and heterogeneous KD when relevant.

## Mode Selection

Use `collaborative` mode by default when the user says "审稿", "review this paper", or gives a general review request.

Use `quick` mode when the user asks for:

- 快速审稿
- 直接给审稿意见
- 一次性输出
- reviewer comments now

Use `collaborative` mode when the user asks for:

- 协同审稿
- 一步步审
- 先分析，不要直接写最终意见
- 和我一起判断

## Shared Workflow

1. Process only one paper per invocation. If multiple papers are provided, ask which one to review first.
2. Prefer local `.pdf`, `.tex`, `.md`, or `.txt` files.
3. Parse local files with `scripts/extract_paper_text.py` when available.
4. Surface extraction limitations before review if the text is sparse, garbled, missing figures/tables/equations, or likely affected by two-column ordering.
5. Apply the CV/ML/DL review criteria in `references/review-criteria.md`.
6. Use ratings from `references/review-criteria.md`.
7. Use templates from `references/output-templates.md`.

## Quick Mode

In quick mode, produce both:

1. `Review Analysis Note` in Chinese for the reviewer.
2. `Reviewer Comments` in English for submission.

The formal comments must include:

- `Ratings`
- `Summary`
- `Strengths`
- `Major Concerns`
- `Minor Concerns`
- `Questions for Authors`

Do not include an explicit recommendation sentence in the formal comments body. Put `Overall Recommendation` only in the ratings area because review systems usually handle it as a separate choice.

## Collaborative Mode

In collaborative mode, do not draft final English reviewer comments in the first response.

First produce:

- Chinese review analysis note
- preliminary ratings
- candidate major concerns
- candidate minor concerns
- uncertainty and missing information
- reviewer decision points for the user

Then stop and ask the user to confirm:

- which concerns should become major concerns
- whether the preliminary ratings are appropriate
- which `Overall Recommendation` direction to use
- whether to draft the final English reviewer comments

Only draft final English comments after the user confirms.

## Language and Tone

- Private analysis: Chinese as the main language, preserving important English technical terms.
- Formal reviewer comments: English.
- Formal tone: polite but direct.
- Avoid excessive hedging.
- Avoid personal research preferences in formal comments.
- Major concerns must clearly state the issue, why it affects the paper's claims or quality, and what evidence or revision would address it.

## Private KD Lens

Use `references/private-kd-lens.md` only for the reviewer's private analysis and research inspiration. Do not include private heterogeneous KD ideas in formal reviewer comments.

Include KD-related points in formal comments only when they directly affect the paper's claims, validity, novelty, or experimental evidence.

## References

- `references/review-workflow.md`: quick and collaborative mode details.
- `references/review-criteria.md`: scoring dimensions and CV/ML/DL review checks.
- `references/output-templates.md`: internal analysis and English formal comment templates.
- `references/private-kd-lens.md`: private KD and heterogeneous KD analysis lens.
