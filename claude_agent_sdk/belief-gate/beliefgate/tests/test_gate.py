import pytest
from beliefgate import check_set, verify_coverage, CoverageClaim, CoverageKind, SourceFacts, Verdict


# Leak-proof: never false-completes
def test_complete():
    r = check_set(required={"a", "b", "c"}, present={"a", "b", "c", "d"})
    assert r.ok
    assert r.verdict == Verdict.COMPLETE

def test_incomplete():
    r = check_set(required={"a", "b", "c"}, present={"a", "c"})
    assert not r.ok
    assert "b" in r.missing

def test_empty_required():
    r = check_set(required=[], present=["x"])
    assert r.ok

def test_empty_present():
    r = check_set(required=["x"], present=[])
    assert not r.ok
    assert "x" in r.missing

def test_range_required():
    r = check_set(required=range(200, 251), present=list(range(200, 251)))
    assert r.ok

def test_range_with_gap():
    present = list(range(200, 251))
    present.remove(225)
    r = check_set(required=range(200, 251), present=present)
    assert not r.ok
    assert 225 in r.missing

def test_sorted_threshold_undecidable():
    facts = SourceFacts(present_count=10, keys=list(range(10)), sorted_desc=True, boundary_crossed=True)
    r = verify_coverage(CoverageClaim(CoverageKind.SORTED_TO_THRESHOLD), facts)
    assert r.verdict == Verdict.UNDECIDABLE

def test_full_count_complete():
    facts = SourceFacts(present_count=5, predicate_evaluable=True)
    r = verify_coverage(CoverageClaim(CoverageKind.FULL_COUNT, total=5), facts)
    assert r.ok

def test_full_count_incomplete():
    facts = SourceFacts(present_count=4, predicate_evaluable=True)
    r = verify_coverage(CoverageClaim(CoverageKind.FULL_COUNT, total=5), facts)
    assert not r.ok

def test_contiguous_ids_complete():
    facts = SourceFacts(present_count=5, keys=[1, 2, 3, 4, 5])
    r = verify_coverage(CoverageClaim(CoverageKind.CONTIGUOUS_IDS), facts)
    assert r.ok

def test_contiguous_ids_gap():
    facts = SourceFacts(present_count=4, keys=[1, 2, 4, 5])
    r = verify_coverage(CoverageClaim(CoverageKind.CONTIGUOUS_IDS), facts)
    assert not r.ok
