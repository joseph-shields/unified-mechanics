"""CAMB-backed LiMB solver wrapped in new Unified Mechanics semantics.

CAMB is used only as the external forward-execution engine. The new UM layer
supplies typed questions, provenance, answerability, closure assessment, and
revision targets. No IRIS dependency or code path is used.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from limb.camb_backend import cosmology_to_camb_params

from .closure import assess_questions
from .legacy_observations import build_observation_inference_cosmology
from .questions import cmb_spectrum_questions
from .types import SolverResult, StrongQuestion


def compute_forward_record(
    *,
    lmax: int = 2500,
    lens_potential_accuracy: int = 1,
) -> tuple[Any, dict[str, Any], tuple]:
    """Execute the legacy observation/inference cosmology through CAMB."""

    import camb
    import numpy as np

    cosmology, evidence = build_observation_inference_cosmology()
    params = cosmology_to_camb_params(
        cosmology,
        lmax=lmax,
        lens_potential_accuracy=lens_potential_accuracy,
    )
    results = camb.get_results(params)
    powers = results.get_cmb_power_spectra(params, lmax=lmax, CMB_unit="muK")
    total = np.asarray(powers["total"])
    unlensed = np.asarray(powers["unlensed_scalar"])
    record = {
        "ells": np.arange(total.shape[0]),
        "totCl_TT": total[:, 0],
        "totCl_EE": total[:, 1],
        "totCl_BB": total[:, 2],
        "totCl_TE": total[:, 3],
        "unlensed_TT": unlensed[:, 0],
        "derived_params": results.get_derived_params(),
    }
    return cosmology, record, evidence


def solve(
    *,
    lmax: int = 2500,
    questions: Sequence[StrongQuestion] | None = None,
    observed_record: Mapping[str, Any] | None = None,
    tolerance: float = 0.03,
    lens_potential_accuracy: int = 1,
) -> SolverResult:
    """Run LiMB and return a typed new-UM result.

    When ``observed_record`` is absent, the questions remain answerable but not
    externally closed. Supplying a record with the same spectrum keys performs
    the declared closure test.
    """

    cosmology, record, evidence = compute_forward_record(
        lmax=lmax,
        lens_potential_accuracy=lens_potential_accuracy,
    )
    if questions is None:
        questions = cmb_spectrum_questions(lmax=lmax, tolerance=tolerance)
    assessments = assess_questions(record, observed_record, questions)
    return SolverResult(
        cosmology=cosmology,
        forward_record=record,
        evidence=evidence,
        assessments=assessments,
        backend="CAMB",
        metadata={
            "new_um_layer": "strong-question closure architecture",
            "legacy_role": "observation-inference evidence ledger",
            "dynamics_status": (
                "CAMB baseline dynamics; no claimed three-channel physical "
                "realization until conservation/stability/gauge proofs exist"
            ),
            "iris_used": False,
        },
    )
