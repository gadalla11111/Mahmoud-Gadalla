from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Verdict(str, Enum):
    COMPLETE = "COMPLETE"
    INCOMPLETE = "INCOMPLETE"
    UNDECIDABLE = "UNDECIDABLE"


class CoverageKind(str, Enum):
    FULL_COUNT = "FULL_COUNT"
    CONTIGUOUS_IDS = "CONTIGUOUS_IDS"
    SORTED_TO_THRESHOLD = "SORTED_TO_THRESHOLD"  # not deletion-proof; gate refuses


@dataclass
class GateResult:
    verdict: Verdict
    missing: list[Any] = field(default_factory=list)
    reason: str = ""

    @property
    def ok(self) -> bool:
        return self.verdict == Verdict.COMPLETE


@dataclass
class CoverageClaim:
    kind: CoverageKind
    total: int | None = None


@dataclass
class SourceFacts:
    present_count: int
    keys: list[Any] = field(default_factory=list)
    sorted_desc: bool = False
    boundary_crossed: bool = False
    predicate_evaluable: bool = False
