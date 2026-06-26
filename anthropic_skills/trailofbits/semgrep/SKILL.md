---
name: semgrep
description: Static code analysis with Semgrep — parallel, multi-language vulnerability scanning with automatic language detection, third-party rulesets (Trail of Bits, 0xdea, Decurity), and merged SARIF output. Use to scan a codebase for security vulnerabilities. Presents an approval plan before running any scan.
auto-trigger:
  - '"scan this codebase", "run semgrep", "find vulnerabilities", security audit of source'
  - static analysis pass before a security review or release
do-not-trigger:
  - deep interprocedural taint tracking specifically (use codeql)
  - API-misuse / footgun design review (use sharp-edges)
  - runtime production errors (use sentry-fix-issues / debug)
allowed-tools: Bash, Read, Grep, Glob
---

# semgrep — parallel static analysis

Scan codebases for vulnerabilities across languages with Semgrep. Detect languages, check Semgrep Pro (cross-file taint), then scan in parallel and merge to SARIF.

## Five-step workflow

1. **Initialize** — resolve output dir, detect languages, verify Pro status.
2. **Configure** — choose scan mode ("run all" vs "important only").
3. **Approval gate** — present exact target dirs, rulesets, and engine config; **wait for explicit approval**.
4. **Execute** — spawn all per-language scanner tasks together (one response) for parallelism.
5. **Consolidate** — merge outputs into a single SARIF + approved-rulesets log.

## Hard requirements

- **`--metrics=off` on every invocation** — no telemetry during security audits.
- **Step 3 is a hard gate** — "scan this codebase" is NOT approval. Present the plan, then wait.
- **Third-party rulesets are mandatory** — Trail of Bits, 0xdea, Decurity catch what the official registry misses.
- **All tasks spawn together** in a single response to maximize parallelization.

## Output

One directory (user-specified or auto-numbered): per-language raw outputs + merged SARIF + approved rulesets log.
