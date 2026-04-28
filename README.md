# Paper Tools

Paper Tools is a plugin-style skill bundle for academic paper workflows, focused on computer vision, machine learning, deep learning, and knowledge distillation research.

It is organized around portable `SKILL.md` skills, with small adapter manifests for different AI CLIs.

## Skills

- `paper-read`: read one local paper and produce a structured research note.
- `paper-review`: review one local paper with quick or collaborative peer-review workflows.

## Repository Layout

```text
paper-tools/
├── skills/
│   ├── paper-read/
│   └── paper-review/
├── .codex-plugin/
│   └── plugin.json
├── .claude-plugin/
│   └── plugin.json
├── .opencode/
│   ├── INSTALL.md
│   └── plugins/
│       └── paper-tools.js
├── gemini-extension.json
├── GEMINI.md
├── AGENTS.md
└── package.json
```

The portable core is `skills/*/SKILL.md`. Tool-specific files are adapters.

## Installation

Replace `<owner>/<repo>` with the published GitHub repository.

### Codex

Use the Codex plugin flow and install this repository as a plugin. The Codex manifest is:

```text
.codex-plugin/plugin.json
```

It declares:

```json
"skills": "./skills/"
```

After installation, Codex should expose:

```text
paper-read
paper-review
```

### Claude Code

Install as a Claude plugin from the repository. The Claude manifest is:

```text
.claude-plugin/plugin.json
```

The skills are in:

```text
skills/
```

### Gemini CLI

Install as a Gemini extension:

```bash
gemini extensions install https://github.com/<owner>/<repo>
```

Gemini uses:

```text
gemini-extension.json
GEMINI.md
```

### OpenCode

Add Paper Tools to the `plugin` array in `opencode.json`:

```json
{
  "plugin": ["paper-tools@git+https://github.com/<owner>/<repo>.git"]
}
```

For local development:

```json
{
  "plugin": ["paper-tools@file:///absolute/path/to/paper-tools"]
}
```

Restart OpenCode after changing the config.

The OpenCode plugin entry is:

```text
.opencode/plugins/paper-tools.js
```

It registers this repository's `skills/` directory automatically. No copied skill folders or symlinks are required.

### Generic Agents

Agents that understand `AGENTS.md` can use:

```text
AGENTS.md
```

Agents that directly load `SKILL.md` directories can point to:

```text
skills/paper-read
skills/paper-review
```

## Local Parsing Dependencies

The paper skills prioritize local file parsing.

Required lightweight tools:

- `python3`
- `pdftotext`
- `pdfinfo`
- `detex` for `.tex` files

Optional enhancement:

- `PyMuPDF` (`pymupdf`, imported as `fitz`) for coordinate-aware PDF extraction.

PDF parsing is designed for two-column CV/ML papers, but extraction quality still depends on the source PDF.

## Development Notes

When adding a new paper-related skill:

1. Add it under `skills/<skill-name>/`.
2. Include a valid `SKILL.md`.
3. Keep CLI-specific metadata in adapter files, not in the core skill unless the target CLI requires it.
4. Update this README's skill list.
