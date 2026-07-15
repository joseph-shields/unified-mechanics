"""Tests for the new Unified Mechanics LiMB layer.

These tests do not require CAMB unless the integration test is selected.
"""
from __future__ import annotations

import numpy as np
import pytest

from limb.new_um import (
    ClaimStatus,
    DynamicStatus,
    GroundingStatus,
    answer_profile_distance,
    assess_questions,
    build_observation_inference_cosmology,
    closure_defect,
    cmb_spectrum_questions,
    legacy_evidence,
    minimal_norm_source,
    source_repair_residual,
)


def _record(n: int = 32, shift: float = 0.0):
    x = np.linspace(1.0, 2.0, n) + shift
    return {
        "totCl_TT": x,
        "totCl_EE": 0.5 * x,
        "totCl_TE": 0.2 * x,
        "totCl_BB": 0.01 * x,
    }


def test_legacy_values_are_retyped_not_erased():
    evidence = legacy_evidence()
    names = {item.name for item in evidence}
    assert {"H0", "Omega_b", "Omega_c", "T_cmb", "n_s", "A_s"} <= names
    by_name = {item.name: item for item in evidence}
    assert by_name["H0"].status is ClaimStatus.OBSERVATION
    assert by_name["T_cmb"].status is ClaimStatus.OBSERVATION
    assert by_name["Omega_b"].status is ClaimStatus.INFERENCE_CANDIDATE
    assert not by_name["Omega_b"].is_foundational_derivation


def test_observation_inference_compiler_matches_evidence():
    cosmo, evidence = build_observation_inference_cosmology()
    by_name = {item.name: item.value for item in evidence}
    assert cosmo.H0 == pytest.approx(by_name["H0"])
    assert cosmo.Omega_b == pytest.approx(by_name["Omega_b"])
    assert cosmo.Omega_c == pytest.approx(by_name["Omega_c"])
    assert cosmo.n_s == pytest.approx(by_name["n_s"])


def test_strong_questions_are_executable():
    record = _record()
    questions = cmb_spectrum_questions(lmax=20, tolerance=0.05)
    for question in questions:
        answer = question.answer(record)
        assert answer.shape == (19,)
        assert question.scope.tolerance == pytest.approx(0.05)
        assert question.failure_conditions


def test_assessment_without_observation_is_answerable_not_closed():
    questions = cmb_spectrum_questions(lmax=20)
    assessments = assess_questions(_record(), None, questions)
    assert all(item.passed is None for item in assessments)
    assert all(item.dynamic is DynamicStatus.NOT_TESTED for item in assessments)
    assert all(item.grounding is GroundingStatus.CONDITIONAL for item in assessments)


def test_assessment_closes_identical_record():
    record = _record()
    questions = cmb_spectrum_questions(lmax=20, tolerance=1e-12)
    assessments = assess_questions(record, record, questions)
    assert all(item.passed for item in assessments)
    assert all(item.residual == pytest.approx(0.0) for item in assessments)


def test_answer_profile_distance_is_zero_on_identical_records():
    questions = cmb_spectrum_questions(lmax=20)
    record = _record()
    assert answer_profile_distance(record, record, questions) == pytest.approx(0.0)
    assert answer_profile_distance(record, _record(shift=0.1), questions) > 0.0


def test_minimum_norm_source_repairs_full_row_rank_defect():
    projection = np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 1.0]])
    full_rhs = np.array([1.0, 2.0, 3.0])
    reduced_rhs = np.array([5.0, 8.0])
    defect = closure_defect(projection, full_rhs, reduced_rhs)
    source = minimal_norm_source(projection, defect)
    assert source_repair_residual(projection, source, defect) < 1e-10


def test_regularized_source_is_finite_for_rank_deficiency():
    projection = np.array([[1.0, 1.0], [2.0, 2.0]])
    defect = np.array([1.0, 2.0])
    source = minimal_norm_source(projection, defect, regularization=1e-6)
    assert np.all(np.isfinite(source))


@pytest.mark.integration
def test_camb_solver_metadata_excludes_iris():
    camb = pytest.importorskip("camb")
    from limb.new_um import solve

    result = solve(lmax=30)
    assert result.backend == "CAMB"
    assert result.metadata["iris_used"] is False
    assert len(result.forward_record["totCl_TT"]) == 31
