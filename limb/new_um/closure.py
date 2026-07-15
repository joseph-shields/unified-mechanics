"""Question geometry, answerability, and dynamic closure tools."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

import numpy as np

from .questions import relative_rms
from .types import (
    DeterminationStatus,
    DynamicStatus,
    GroundingStatus,
    InquiryStatus,
    QuestionAssessment,
    StrongQuestion,
)


def total_variation(p: Any, q: Any) -> float:
    """Total-variation distance after non-negative normalization."""

    p_arr = np.asarray(p, dtype=float)
    q_arr = np.asarray(q, dtype=float)
    if p_arr.shape != q_arr.shape:
        raise ValueError("response arrays must have equal shape")
    if np.any(p_arr < 0) or np.any(q_arr < 0):
        raise ValueError("total_variation requires non-negative responses")
    p_sum = float(p_arr.sum())
    q_sum = float(q_arr.sum())
    if p_sum <= 0 or q_sum <= 0:
        raise ValueError("response arrays must carry positive total weight")
    p_norm = p_arr / p_sum
    q_norm = q_arr / q_sum
    return float(0.5 * np.abs(p_norm - q_norm).sum())


def answer_profile_distance(
    left_record: Mapping[str, Any],
    right_record: Mapping[str, Any],
    questions: Sequence[StrongQuestion],
    *,
    weights: Mapping[str, float] | None = None,
) -> float:
    """Weighted distance induced by grounded strong-question answers.

    Spectra may contain signed cross-correlations, so this function uses
    bounded relative RMS rather than total variation for generic readouts.
    """

    total = 0.0
    for question in questions:
        weight = 1.0 if weights is None else float(weights.get(question.name, 1.0))
        if weight < 0:
            raise ValueError("question weights must be non-negative")
        left = question.answer(left_record)
        right = question.answer(right_record)
        residual = relative_rms(left, right)
        total += weight * min(residual, 1.0)
    return float(total)


def assess_questions(
    predicted_record: Mapping[str, Any],
    observed_record: Mapping[str, Any] | None,
    questions: Sequence[StrongQuestion],
) -> tuple[QuestionAssessment, ...]:
    """Compute terminal status vectors for the supplied questions."""

    assessments: list[QuestionAssessment] = []
    for question in questions:
        predicted = question.answer(predicted_record)
        if observed_record is None:
            assessments.append(
                QuestionAssessment(
                    question=question.name,
                    determination=DeterminationStatus.PARTIAL,
                    inquiry=InquiryStatus.ANSWERABLE,
                    dynamic=DynamicStatus.NOT_TESTED,
                    grounding=GroundingStatus.CONDITIONAL,
                    residual=None,
                    tolerance=question.scope.tolerance,
                    passed=None,
                    notes=(
                        "Forward answer exists, but no external observation "
                        "record was supplied for closure."
                    ),
                )
            )
            continue

        observed = question.answer(observed_record)
        residual = relative_rms(predicted, observed)
        passed = question.sufficiency(predicted, observed, question.scope.tolerance)
        assessments.append(
            QuestionAssessment(
                question=question.name,
                determination=DeterminationStatus.DETERMINED,
                inquiry=InquiryStatus.ANSWERED,
                dynamic=DynamicStatus.NOT_TESTED,
                grounding=GroundingStatus.REGISTERED,
                residual=residual,
                tolerance=question.scope.tolerance,
                passed=bool(passed),
                notes=(
                    "Closed against supplied record."
                    if passed
                    else "Mismatch requires typed diagnosis; it does not by "
                    "itself identify parameter, dynamics, or observation failure."
                ),
            )
        )
    return tuple(assessments)


def closure_defect(projection: Any, full_rhs: Any, reduced_rhs: Any) -> np.ndarray:
    """Return Delta = f_bar(P y) - P f(y) for a linear readout projection."""

    p = np.asarray(projection, dtype=float)
    f = np.asarray(full_rhs, dtype=float)
    f_bar = np.asarray(reduced_rhs, dtype=float)
    if p.ndim != 2:
        raise ValueError("projection must be a matrix")
    if f.ndim != 1 or f_bar.ndim != 1:
        raise ValueError("rhs arrays must be vectors")
    if p.shape[1] != f.shape[0] or p.shape[0] != f_bar.shape[0]:
        raise ValueError("incompatible projection/RHS shapes")
    return f_bar - p @ f


def minimal_norm_source(
    projection: Any,
    defect: Any,
    *,
    regularization: float = 0.0,
) -> np.ndarray:
    r"""Minimum-norm additive source that repairs a declared closure defect.

    Solves min_s ||s||_2 subject to P s = Delta in the full-row-rank,
    zero-regularization case. With lambda > 0 it returns the stabilized
    correction

        s* = P^T (P P^T + lambda I)^-1 Delta.

    This is a construction rule, not a physical derivation. A source is
    physically admissible only after conservation, gauge, stability, and
    independent-observable tests are supplied.
    """

    p = np.asarray(projection, dtype=float)
    delta = np.asarray(defect, dtype=float)
    if p.ndim != 2 or delta.ndim != 1:
        raise ValueError("projection must be 2-D and defect must be 1-D")
    if p.shape[0] != delta.shape[0]:
        raise ValueError("defect dimension must equal projection row count")
    if regularization < 0:
        raise ValueError("regularization must be non-negative")

    gram = p @ p.T
    if regularization:
        gram = gram + regularization * np.eye(gram.shape[0])
    try:
        dual = np.linalg.solve(gram, delta)
    except np.linalg.LinAlgError:
        dual = np.linalg.pinv(gram) @ delta
    return p.T @ dual


def source_repair_residual(projection: Any, source: Any, defect: Any) -> float:
    p = np.asarray(projection, dtype=float)
    s = np.asarray(source, dtype=float)
    delta = np.asarray(defect, dtype=float)
    return float(np.linalg.norm(p @ s - delta))
