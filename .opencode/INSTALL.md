# Installing Paper Tools for OpenCode

Add Paper Tools to the `plugin` array in your `opencode.json`:

```json
{
  "plugin": ["paper-tools@git+https://github.com/<owner>/<repo>.git"]
}
```

For local development, point OpenCode at this repository:

```json
{
  "plugin": ["paper-tools@file:///absolute/path/to/paper-tools"]
}
```

Restart OpenCode after changing the config.

## Usage

Use OpenCode's native `skill` tool to list and load skills:

```text
use skill tool to list skills
use skill tool to load paper-read
use skill tool to load paper-review
```

The plugin registers this repository's `skills/` directory automatically. No symlinks or copied skill folders are required.
