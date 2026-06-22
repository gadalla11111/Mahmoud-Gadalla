from typing import Any, Callable
from .models import GateResult, Verdict, CoverageClaim, CoverageKind, SourceFacts


def check_set(required: Any, present: Any) -> GateResult:
    """Deterministic set-completeness check. Never false-completes."""
    req = set(required)
    pre = set(present)
    missing = sorted(req - pre, key=str)
    if missing:
        return GateResult(
            verdict=Verdict.INCOMPLETE,
            missing=missing,
            reason=f"Missing {len(missing)} of {len(req)} required items: {missing}",
        )
    return GateResult(verdict=Verdict.COMPLETE, reason="All required items present.")


def verify_coverage(claim: CoverageClaim, facts: SourceFacts) -> GateResult:
    """Verify a predicate-coverage claim against source facts."""
    if claim.kind == CoverageKind.SORTED_TO_THRESHOLD:
        return GateResult(
            verdict=Verdict.UNDECIDABLE,
            reason="SORTED_TO_THRESHOLD is not deletion-proof; cannot certify COMPLETE.",
        )

    if claim.kind == CoverageKind.FULL_COUNT:
        if claim.total is None:
            return GateResult(verdict=Verdict.UNDECIDABLE, reason="FULL_COUNT requires total.")
        if facts.present_count < claim.total:
            missing_count = claim.total - facts.present_count
            return GateResult(
                verdict=Verdict.INCOMPLETE,
                reason=f"Source claimed {claim.total} rows; {facts.present_count} present ({missing_count} missing).",
            )
        if not facts.predicate_evaluable:
            return GateResult(verdict=Verdict.UNDECIDABLE, reason="Predicate not evaluable on present rows.")
        return GateResult(verdict=Verdict.COMPLETE, reason="Count matches claimed total; predicate evaluable.")

    if claim.kind == CoverageKind.CONTIGUOUS_IDS:
        keys = sorted(facts.keys)
        if len(keys) < 2:
            return GateResult(verdict=Verdict.UNDECIDABLE, reason="Too few keys to verify contiguity.")
        gaps = [keys[i + 1] - keys[i] for i in range(len(keys) - 1) if hasattr(keys[i], "__sub__")]
        if any(g != 1 for g in gaps):
            return GateResult(verdict=Verdict.INCOMPLETE, reason=f"ID gaps detected: {gaps}")
        return GateResult(verdict=Verdict.COMPLETE, reason="IDs are contiguous.")

    return GateResult(verdict=Verdict.UNDECIDABLE, reason=f"Unknown coverage kind: {claim.kind}")


def run_with_repair(
    declare_fn: Callable,
    facts: SourceFacts,
    source_total: int,
    max_retries: int = 3,
) -> tuple[GateResult, list[str]]:
    """Run coverage verification with an LLM-declaration repair loop."""
    trace: list[str] = []
    repair_msg = ""

    for attempt in range(max_retries):
        claim = declare_fn(facts, source_total, repair_msg)
        result = verify_coverage(claim, facts)
        trace.append(f"Attempt {attempt + 1}: {result.verdict} — {result.reason}")

        if result.verdict != Verdict.UNDECIDABLE:
            return result, trace

        repair_msg = (
            f"Previous declaration was undecidable: {result.reason}. "
            f"Use source_total={source_total} (never count visible rows). "
            f"Choose FULL_COUNT or CONTIGUOUS_IDS."
        )

    return GateResult(verdict=Verdict.UNDECIDABLE, reason="Max retries exceeded."), trace
