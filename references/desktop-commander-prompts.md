# Desktop Commander Prompt Library Reference

> Source: https://desktopcommander.app/library/prompts/ (70+ prompts)
> Extracted: 2026-07-10 via search index (site blocks direct fetch)
> Note: Full prompt text not accessible (403). Titles and categories only.

---

## Development & DevOps

| Prompt | URL slug |
|---|---|
| Explain Codebase or Repository | `explain-codebase-or-repository` |
| Build features by scoping against existing codebase | — |
| Generate Dev Onboarding Guide | `generate-dev-onboarding-guide` |
| Generate architecture docs and decision logs | — |
| Explain CI/CD Pipeline | `explain-cicd-pipeline` |
| Set Up Cloud Infrastructure | `set-up-cloud-infrastructure` |
| Document Ansible Configuration | `document-ansible-configuration` |
| Assess Project's Security | `assess-projects-security` |
| Plan codebase migration to newer technologies | — |
| Scan codebase for unused imports and dead code | — |
| Create test files for modules lacking tests | — |
| Transform API endpoints into documentation | — |
| Analyze technical debt with remediation plan | — |
| Locate TODO items across codebase | — |
| Set up development environment | — |

## Analytics & Monitoring

| Prompt | URL slug |
|---|---|
| Set up Google Analytics and analyze traffic | `set-up-google-analytics-and-analyze-traffic` |
| Setting up PostHog analytics with custom events | `setting-up-posthog-analytics-with-custom-events` |
| Analyze log files to identify system issues | — |
| Generate visual presentations of development activity | — |

## Web & Applications

| Prompt | URL slug |
|---|---|
| Manage WordPress site in natural language | `manage-wordpress-site-in-natural-language` |
| Create professional landing pages | — |
| Build Personal Finance Tracker | `build-personal-finance-tracker` |
| Automate Competitor Research | `automate-competitor-research` |

## File & Document Management

| Prompt | URL slug |
|---|---|
| Organise my Downloads folder | `organise-my-downloads-folder` |
| Find invoices and move them to folder | `find-invoices-and-move-them-to-folder` |
| Sort and organize PDF documents by date | — |
| Combine multiple PDF documents | — |
| Remove duplicate entries from contact lists | — |
| Convert HEIC to PNG | `convert-heic-to-png` |
| Process and convert multiple images | — |

---

## Key Patterns Observed (from DC Community)

### Effective DC Prompt Structure (DC Dmitry)
```
- use this directory: [path] and read all folders and subfolders structure.
- after you finish, suggest how I can organize these files in a more orderly and logical way.
[then paste the suggestion back as the next prompt]
```

### Context Management Approach (DC Eduards)
- Prefer hierarchical, modular code structure over documentation files
- Well-written code with inline comments IS the documentation for AI
- Per-folder `__instruct.md` files for progressive context loading
- Reference endpoints from frontend / frontend consumers from backend for cross-boundary navigation

### Token Reality (DC Dmitry)
- DC system tools inject ~2k tokens **once per chat** (not per tool call)
- File contents read during session accumulate in context
- Opus burns token budget fast; Sonnet is the practical daily driver
- Rate limits = tokens per 5-hour window, not just message count

---

## Community Workflow Tips

1. **Explicit paths beat discovery**: "go to /path/src/ and update X" beats "find where X is defined"
2. **Suggest → confirm → execute**: Ask DC to suggest changes first, then confirm, then run
3. **New chat = fresh token budget**: When limits hit, open a new chat with the key context only
4. **Memory bank on new chat**: Tell Claude to read `.memory-bank/` at the start of new sessions
5. **Anti-sycophancy prompt**: See `CLAUDE.md → Communication Guidelines` (source: `anthropics/claude-code#3382`)
