# AGENTS.md — rulebook-ai

## What this is
Python package manifest and lockfile for `rulebook-ai`. This directory contains `pyproject.toml` and `uv.lock` — source code is not vendored here.

## Build / Test
```bash
# Install dependencies from lockfile
uv sync

# Run any configured scripts
uv run rulebook-ai
```

## Conventions
- Dependencies managed via `uv` (not pip)
- Lockfile (`uv.lock`) must be committed and kept up to date
- Prefer minor/patch dependency updates; discuss major bumps first

## AI Assistant Notes
- Do not add source code here — this is a manifest-only directory
- When updating dependencies, run `uv lock` to regenerate the lockfile
- Verify the lockfile is valid with `uv sync` after changes
