# Local Paper Extraction

Prioritize local file parsing. Use web access only for optional metadata or project-page support when local information is incomplete or the user asks for it.

## Supported Inputs

- `.pdf`
- `.tex`
- `.md`
- `.txt`

## Tool Priority

Required for the lightweight path:

- `python3`
- `pdftotext`
- `pdfinfo`
- `detex` for `.tex` when available

Optional enhancement:

- `PyMuPDF` imported as `fitz`

Do not require OCR by default. If extracted text is very sparse, report that the PDF may be scanned or image-heavy.

## PDF Strategy

Most CV/ML papers are two-column. Use column-aware extraction:

1. If `PyMuPDF` is available, use block coordinates.
2. Otherwise, use `pdftotext -layout`.
3. Detect stable mid-page whitespace for two-column text.
4. Reconstruct each page as left column followed by right column.
5. Preserve page numbers and parser warnings.
6. If two-column detection is unstable, fall back to raw layout text and warn the user.

Expected limitations:

- figure text can be missing or out of order
- table content can be incomplete
- equations can be simplified
- algorithm boxes can be fragmented
- appendix content may need separate attention

Never invent missing figure, table, equation, or appendix details.

## TeX Strategy

Use `detex` when available to strip LaTeX commands. If unavailable, read the raw `.tex` file and warn that LaTeX markup remains.

## Markdown / Text Strategy

Read directly as UTF-8, falling back to replacement decoding if needed.

## Extraction Warning Policy

Before analysis, surface major limitations such as:

- `PDF 文本解析过短，可能是扫描版或图片型 PDF`
- `双栏顺序可能混乱`
- `图表/公式/algorithm 信息可能缺失`
- `appendix 未包含或未解析`
