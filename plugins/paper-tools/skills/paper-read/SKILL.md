---
name: paper-read
description: Research-oriented reading of one local computer science paper, especially computer vision, AI, machine learning, deep learning, and knowledge distillation papers. Use when the user asks to read, understand, summarize, deep-read, analyze, or create structured notes for a single local PDF, TeX, Markdown, or text paper. Prioritize local file parsing; use web access only as optional metadata or project-page support when requested or when local metadata is incomplete.
---

# Paper Read

Use this skill to read one paper at a time and produce a structured research note for CV/ML/DL research. The default lens is doctoral research in knowledge distillation, especially heterogeneous knowledge distillation across logits, features, and relations.

## Workflow

1. Identify the input:
   - Prefer local `.pdf`, `.tex`, `.md`, or `.txt` files.
   - Process only one paper per invocation. If multiple papers are provided, ask the user which one to read first.
   - Do not use web content as a replacement for local paper text unless the user explicitly asks.

2. Parse the paper:
   - For local files, use `scripts/extract_paper_text.py` when available.
   - For PDFs, prefer column-aware extraction because most CV/ML papers are two-column.
   - If extraction is sparse, garbled, missing figures/tables/equations, or likely out of order, state the limitation before analysis.
   - See `references/pdf-extraction.md` for parser behavior and failure handling.

3. Choose output depth:
   - Use `standard` by default.
   - Use `brief` when the user asks for quick reading, quick summary, or whether the paper is worth reading.
   - Use `deep` when the user asks for deep reading, intensive reading, group-meeting notes, related-work support, or method-improvement analysis.
   - Ask the user to choose a depth only when the request is ambiguous and the difference would materially affect the work.

4. Read through the CV/ML/DL framework:
   - Focus on task definition, motivation, method, model architecture, objective/loss, experiments, evidence strength, limitations, and research use.
   - Keep `training strategy` under experiment setup, not method decomposition.
   - See `references/cv-ml-reading-framework.md`.

5. Apply the KD research lens:
   - Expand KD analysis for knowledge distillation, model compression, representation transfer, teacher-student, alignment, or heterogeneous architectures.
   - Keep the KD section short when the paper is not relevant.
   - See `references/kd-research-lens.md`.

6. Produce the note:
   - Main language: Chinese.
   - Preserve important English technical terms, e.g. `baseline`, `ablation study`, `loss function`, `SOTA`, `dataset leakage`, `feature alignment`.
   - Use the fixed Markdown structure from `references/output-templates.md`.
   - Do not save a Markdown file unless the user explicitly asks to save, write, or generate a document.

## Output Rules

Use the title format:

```text
YYYY-VenueShort-ShortTitle
```

`ShortTitle` should prefer the official method/model/framework acronym or method name. If none exists, use a concise title with no spaces. Preserve standard capitalization for known acronyms such as `SAM`, `CLIP`, `MAE`, and `DINOv2`.

For `standard` and `deep` outputs, use progressive explanation:

```text
core judgment -> supporting evidence -> technical detail -> research assessment
```

Start each major section with the key judgment before details. Avoid disconnected checklist dumps. Use bullets for dense technical points, but use explanatory paragraphs for long analysis.

Separate:

- `Author claims`: what the paper says
- `Evidence`: what the experiments or text support
- `Assessment`: your research judgment

Mark uncertainty explicitly:

- `未在论文中找到`
- `需要查看 appendix`
- `需要查看代码`
- `解析文本可能缺失`

## References

- `references/output-templates.md`: fixed Markdown structure, title rules, and depth targets.
- `references/cv-ml-reading-framework.md`: CV/ML/DL reading checklist.
- `references/kd-research-lens.md`: heterogeneous KD analysis lens.
- `references/pdf-extraction.md`: local parsing strategy, two-column handling, and parser warnings.
