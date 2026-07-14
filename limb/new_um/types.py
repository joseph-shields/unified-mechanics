"""Typed structures for the new Unified Mechanics LiMB layer.

This module deliberately separates:
- physical observations,
- inference maps,
- algebraic identities,
- candidate realizations,
- and open dynamical claims.

Nothing becomes a derivation merely because its numerical value agrees
with an observation.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Mapping


class ClaimStatus(str, Enum):
    """Epistemic status of a value used by the solver."""

    OBSERVATION = "observation"
    ALGEBRAIC_IDENTITY = "algebraic_identity"
    INFERENCE_CANDIDATE = "inference_candidate"
    DERIVED_REALIZATION = "derived_realization"
    OPEN = "open"


class DeterminationStatus(str, Enum):
    DETERMINED = "determined"
    PARTIAL = "partial"
    UNDETERMINED = "undetermined"


class InquiryStatus(str, Enum):
    ANSWERED = "answered"
    ANSWERABLE = "answerable"
    RESOURCE_LIMITED = "resource_limited"
    UNDERDETERMINED = "underdetermined"


class DynamicStatus(str, Enum):
    CLOSED = "closed"
    CLOSABLE = "closable"
    UNSTABLE = "unstable"
    NOT_TESTED = "not_tested"


class GroundingStatus(str, Enum):
    REGISTERED = "registered"
    DERIVED_FROM_REGISTERED = "derived_from_registered"
    CONDITIONAL = "conditional"
    UNGROUNDED = "ungrounded"


@dataclass(frozen=True)
class Scope:
    """Boundary and resolution declaration for a strong question."""

    system: str
    boundary: str
    horizon: str
    tolerance: float
    units: str = ""
    assumptions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.tolerance < 0:
            raise ValueError("tolerance must be non-negative")


@dataclass(frozen=True)
class FailureCondition:
    code: str
    description: str
    repair: str


Readout = Callable[[Mapping[str, Any]], Any]


@dataclass(frozen=True)
class StrongQuestion:
    """Executable physical question.

    ``readout`` maps a solver/observation record to the answer-bearing
    quantity. ``sufficiency`` decides whether the comparison closes.
    """

    name: str
    scope: Scope
    intervention: str
    response_carrier: str
    answer_space: str
    readout: Readout = field(compare=False, repr=False)
    sufficiency: Callable[[Any, Any, float], bool] = field(compare=False, repr=False)
    latency: str = "solver-dependent"
    cost: str = "solver-dependent"
    failure_conditions: tuple[FailureCondition, ...] = ()

    def answer(self, record: Mapping[str, Any]) -> Any:
        return self.readout(record)


@dataclass(frozen=True)
class EvidenceRecord:
    """Provenance-bearing value used by the observation/inference layer."""

    name: str
    value: float
    status: ClaimStatus
    expression: str
    source: str
    units: str = ""
    assumptions: tuple[str, ...] = ()
    notes: str = ""

    @property
    def is_foundational_derivation(self) -> bool:
        return self.status is ClaimStatus.DERIVED_REALIZATION


@dataclass(frozen=True)
class QuestionAssessment:
    question: str
    determination: DeterminationStatus
    inquiry: InquiryStatus
    dynamic: DynamicStatus
    grounding: GroundingStatus
    residual: float | None
    tolerance: float
    passed: bool | None
    notes: str = ""


@dataclass(frozen=True)
class SolverResult:
    """New-UM wrapper around an external forward record."""

    cosmology: Any
    forward_record: Mapping[str, Any]
    evidence: tuple[EvidenceRecord, ...]
    assessments: tuple[QuestionAssessment, ...]
    backend: str
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def assessment_by_name(self, name: str) -> QuestionAssessment:
        for assessment in self.assessments:
            if assessment.question == name:
                return assessment
        raise KeyError(name)
