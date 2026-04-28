# Output Templates

## Depth Selection

Use these output lengths as targets, not rigid limits:

- `brief`: about 1000-1800 Chinese characters. Use for quick reading or triage.
- `standard`: about 2500-4000 Chinese characters. Use by default.
- `deep`: about 5000-8000 Chinese characters. Use for group meetings, related work, or method-improvement analysis.

Do not ask the user to choose a depth every time. Infer from the request:

- `brief`: "快速读", "快速总结", "先判断值不值得读", "简单看一下".
- `standard`: default when no depth is specified.
- `deep`: "深度读", "精读", "组会汇报", "复现导向", "related work", "方法改进导向".

## Document Title

Use this title format for the first heading and for saved Markdown filenames:

```text
YYYY-VenueShort-ShortTitle
```

Rules:

- Use a 4-digit year.
- Use common venue abbreviations: `CVPR`, `ICCV`, `ECCV`, `NeurIPS`, `ICLR`, `AAAI`, `IJCAI`, `TPAMI`, `TIP`, `arXiv`.
- Use `UnknownYear` or `UnknownVenue` when unavailable.
- Prefer the official method/model/framework acronym or method name as `ShortTitle`.
- If no method name exists, derive a concise 4-8 word title with no spaces.
- Remove unsafe filename punctuation.
- Do not use spaces.
- Preserve known acronym capitalization, e.g. `SAM`, `CLIP`, `MAE`, `DINOv2`.

Examples:

```text
2024-CVPR-DepthAnything
2023-ICCV-SAM
2022-CVPR-MAE
2025-CVPR-HeterogeneousKDForDensePrediction
```

## Standard Structured Research Note

Use this fixed Markdown structure unless the user asks for a different format:

```markdown
# YYYY-VenueShort-ShortTitle

## 1. 基本信息

## 2. 一句话总结

## 3. 论文定位

## 4. 研究问题与动机

## 5. 方法拆解

## 6. 核心创新点

## 7. 实验设置

## 8. 实验结果分析

## 9. 可信度与证据强度

## 10. 局限与问题

## 11. 知识蒸馏相关性分析

## 12. 可复用设计与研究启发

## 13. 后续研究问题
```

## Style Requirements

For `standard` and `deep` notes:

- Use Chinese as the main language.
- Preserve important English technical terms.
- Start each major section with the core judgment.
- Then expand with evidence, technical detail, and research assessment.
- Avoid bullet-only reports for long notes.
- Do not invent missing details.
- Make extraction limitations visible.

Use this local pattern when appropriate:

```text
核心判断：...
Author claims：...
Evidence：...
Assessment：...
```

Do not force this substructure into every section when it makes the note harder to read.
