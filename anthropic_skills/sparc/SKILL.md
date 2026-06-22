---
name: sparc
description: >
  SPARC development methodology: Specification → Pseudocode → Architecture →
  Refinement → Completion. Use for new features, complex implementations, or
  architectural changes where structured phases prevent rework. Skip for simple
  fixes, docs, or config-only changes. Trigger phrases: "sparc spec", "sparc
  implement", "sparc refine", "sparc complete", "use sparc for".
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob]
argument-hint: "<feature-description> [--phase spec|implement|refine|complete]"
---

# SPARC Methodology

Five phases from fuzzy idea to production-ready feature. Each phase gates the next — no skipping ahead.

| Phase | Trigger | Output |
|---|---|---|
| 1 — Specification | "sparc spec" / "use sparc for" | Requirements, acceptance criteria, constraints, edge cases |
| 2 — Pseudocode | "sparc pseudocode" | Language-agnostic algorithms, data structures, complexity |
| 3 — Architecture | "sparc arch" / "sparc implement" | Module boundaries, API contracts, DDD aggregates |
| 4 — Refinement | "sparc refine" | Code review, test coverage ≥ 80%, performance validation |
| 5 — Completion | "sparc complete" | Traceability matrix, docs, deployment checklist |

---

## Phase 1 — Specification

**When**: starting a new feature; before any code.

**Steps**:
1. Analyze the feature description and codebase to extract:
   - **Functional requirements** — what the feature must do (user-facing behaviors)
   - **Non-functional requirements** — performance targets, security constraints
   - **Integration points** — existing systems or APIs affected
   - **Data requirements** — what is created, read, updated, deleted
2. Write ≥ 3 acceptance criteria in Given/When/Then format:
   ```
   AC-1: Given [precondition], when [action], then [expected result]
   ```
3. List constraints: performance, security, compatibility, infrastructure.
4. Map ≥ 3 edge cases: invalid input, concurrent access, external dependency failures.

**Output**:
```markdown
# Specification: {Feature Name}

## Requirements
### Functional
- FR-1: ...
### Non-Functional
- NFR-1: ...

## Acceptance Criteria
- AC-1: Given ..., when ..., then ...
- AC-2: ...
- AC-3: ...

## Constraints
- Performance: ...
- Security: ...

## Edge Cases
- EC-1: ...
- EC-2: ...
- EC-3: ...

## Integration Points
- IP-1: ...

---
Phase 1 complete → proceed to Pseudocode phase.
```

---

## Phase 2 — Pseudocode

**When**: Specification phase complete.

**Steps**:
1. For each acceptance criterion, write language-agnostic pseudocode that satisfies it.
2. Define core data structures with type annotations.
3. Map control flow: happy path + error paths for each edge case + concurrent access handling.
4. Annotate algorithmic complexity (time and space) for critical paths.

**Output**:
```markdown
# Pseudocode: {Feature Name}

## Core Algorithms
### Algorithm: {name}
```pseudocode
FUNCTION processRequest(input):
    VALIDATE input against schema
    IF invalid THEN THROW ValidationError
    result <- TRANSFORM input
    STORE result
    RETURN result
```
Complexity: O(n) time, O(1) space

## Data Structures
- {StructName}: { field1: type, field2: type }
```

---

## Phase 3 — Architecture

**When**: Pseudocode phase complete.

**Steps**:
1. Define bounded contexts and aggregates (DDD):
   - Entity boundaries and value objects
   - Aggregate invariants
   - Domain events
2. Design API contracts: request/response schemas, error codes, versioning.
3. Plan module boundaries: directory structure, dependency direction rules (no cycles), public vs internal interfaces.
4. Specify infrastructure: persistence, caching, messaging, config.

**Output**:
```markdown
# Architecture: {Feature Name}

## Bounded Contexts
- {ContextName}: {description}
  - Aggregates: {list}
  - Events: {list}

## API Contracts
### POST /api/{resource}
- Request: { field1: string }
- Response: { id: string }
- Errors: 400 (validation), 409 (conflict)

## Module Structure
```
src/{feature}/
  {feature}.types.ts
  {feature}.service.ts
  {feature}.controller.ts
  {feature}.repository.ts
  {feature}.test.ts
```

## Infrastructure
- Persistence: ...
- Caching: ...
```

---

## Phase 4 — Refinement

**When**: Architecture phase complete, code implemented.

**Steps**:
1. **Code review** — check against: spec compliance, architecture adherence, pseudocode fidelity, code quality (naming, SRP, error handling, no dead code).
2. **Test coverage** — run tests, measure coverage, write missing tests targeting ≥ 80% on new code. Cover every AC and every edge case.
3. **Performance validation** — profile critical paths; compare against NFR thresholds; optimize if needed.
4. Iterate steps 1–3 until: all ACs have passing tests, no critical review issues, coverage met, performance constraints satisfied.

**Output**:
```markdown
# Refinement: {Feature Name}

## Code Review Summary
- Critical issues: 0 (must be 0 to advance)
- High: N, Medium: N, Resolved: N/total

## Test Coverage
- Overall: N%  New code: N%  ACs covered: N/total

## Performance
| Constraint | Target | Measured | Status |
|---|---|---|---|
| Response time | <200ms | 145ms | Pass |
```

---

## Phase 5 — Completion

**When**: Refinement phase complete.

**Steps**:
1. Run full regression suite; all tests must pass.
2. Build traceability matrix: each AC → test(s) that verify it → code file(s) that implement it.
3. Generate/update documentation: API docs, usage examples, affected existing docs.
4. Complete deployment readiness checklist.

**Deployment checklist**:
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Database migrations prepared (if applicable)
- [ ] Configuration changes documented
- [ ] Rollback plan defined
- [ ] Security review complete (no secrets committed, inputs validated)

**Output**:
```markdown
# Completion: {Feature Name}

## Traceability Matrix
| AC | Test | Code | Status |
|---|---|---|---|
| AC-1 | test_xxx | service.ts:42 | Pass |
| AC-2 | test_yyy | controller.ts:18 | Pass |

## Deployment Checklist
- [x] All tests passing
- [x] Documentation complete
- [x] Rollback plan defined
- [x] Security reviewed

---
SPARC workflow complete.
```

---

## Rules

- **No phase skipping** — if the Specification is missing, start there even if the user wants to jump to code.
- **ACs are the contract** — every line of implementation must trace back to an AC.
- **Gate on critical issues** — Phase 4 does not complete while critical review issues remain open.
- **Traceability matrix must close** — every AC must have a corresponding passing test before Phase 5 completes.
