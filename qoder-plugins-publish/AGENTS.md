# AGENTS.md — qoder-plugins-publish

## What this is
Publishing automation and source for 16 authored Qoder AI IDE plugins. Plugins cover cloud infrastructure (Alibaba Cloud), architecture analysis, development workflows, debugging, and more.

## Structure
- Each plugin is a directory with a `SKILL.md` (or equivalent) defining its behavior
- Python scripts handle packaging and publishing to the Qoder plugin registry
- `pyproject.toml` manages Python dependencies for the publishing toolchain

## Build / Test
```bash
# Install Python dependencies
uv sync

# Run publishing scripts (check individual plugin directories for specifics)
python -m publish
```

## Conventions
- Plugin names use kebab-case (e.g., `alibabacloud-planning`)
- Each plugin should be self-contained with its own documentation
- SKILL.md files follow the Qoder skill format
- Test plugins locally before publishing

## AI Assistant Notes
- Do not modify published plugin content without updating version numbers
- The publishing pipeline is idempotent — re-publishing the same version is safe
- Check if a plugin already exists before creating a new one
