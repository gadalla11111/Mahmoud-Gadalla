---
name: codeql
description: Security vulnerability scanning with CodeQL — interprocedural data-flow and taint tracking. Builds a CodeQL database, generates custom data extensions (source/sink models), and runs explicit query suites. Use for deep taint analysis where pattern scanning isn't enough.
auto-trigger:
  - '"run codeql", "codeql scan", "find vulnerabilities with codeql", deep taint/data-flow analysis'
do-not-trigger:
  - fast multi-language pattern scanning (use semgrep)
  - API-misuse / footgun design review (use sharp-edges)
allowed-tools: Bash, Read, Grep, Glob
---

# codeql — interprocedural taint analysis

Two scan modes: **run all** (security-and-quality + security-experimental suites) or **important only** (high-precision findings).

## Three sequential workflows

1. **Build database** — create the CodeQL DB with correct build-method sequencing.
2. **Create data extensions** — generate custom source/sink models for project-specific patterns.
3. **Run analysis** — execute queries, process results into `$OUTPUT_DIR` (auto-increment `_1`, `_2`).

## Five non-negotiable principles

1. **Validate database quality** — a successful build ≠ good extraction; a cached build produces zero useful extraction. Check file counts and extraction errors.
2. **Data extensions are mandatory** — skipping means missing vulnerabilities in project-specific logic.
3. **Explicit suite references** — never pass pack names directly; generate custom `.qls` suite files to avoid hidden filtering/silent failures.
4. **Zero findings demand investigation** — may mean poor DB quality / missing models / wrong query packs, not clean code.
5. **Platform workarounds** — macOS Apple Silicon needs special handling; exit code 137 = architecture mismatch, not build failure.

## Done when

DB quality passes, data extensions evaluated, explicit suites executed, all query packs considered, and any zero-findings result investigated rather than assumed clean.
