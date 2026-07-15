"""New Unified Mechanics layer for LiMB.

This package keeps the old formula suite as an observation/inference ledger,
uses CAMB as the forward record generator, and adds explicit strong-question,
answerability, geometry, closure, and revision mathematics.
"""
from .closure import (
    answer_profile_distance,
    assess_questions,
    closure_defect,
    minimal_norm_source,
    source_repair_residual,
    total_variation,
)
from .legacy_observations import (
    build_observation_inference_cosmology,
    evidence_as_dicts,
    legacy_evidence,
)
from .questions import cmb_spectrum_questions, relative_rms
from .solver import compute_forward_record, solve
from .types import (
    ClaimStatus,
    DeterminationStatus,
    DynamicStatus,
    EvidenceRecord,
    FailureCondition,
    GroundingStatus,
    InquiryStatus,
    QuestionAssessment,
    Scope,
    SolverResult,
    StrongQuestion,
)

__all__ = [
    "ClaimStatus",
    "DeterminationStatus",
    "DynamicStatus",
    "EvidenceRecord",
    "FailureCondition",
    "GroundingStatus",
    "InquiryStatus",
    "QuestionAssessment",
    "Scope",
    "SolverResult",
    "StrongQuestion",
    "answer_profile_distance",
    "assess_questions",
    "build_observation_inference_cosmology",
    "closure_defect",
    "cmb_spectrum_questions",
    "compute_forward_record",
    "evidence_as_dicts",
    "legacy_evidence",
    "minimal_norm_source",
    "relative_rms",
    "solve",
    "source_repair_residual",
    "total_variation",
]
