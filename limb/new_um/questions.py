"""Strong observable questions for the CAMB-based LiMB solver."""
from __future__ import annotations

from typing import Any, Mapping

import numpy as np

from .types import FailureCondition, Scope, StrongQuestion


def _relative_rms(predicted: Any, observed: Any, floor: float = 1e-30) -> float:
    p = np.asarray(predicted, dtype=float)
    o = np.asarray(observed, dtype=float)
    if p.shape != o.shape:
        raise ValueError(f"shape mismatch: predicted {p.shape}, observed {o.shape}")
    denom = np.maximum(np.abs(o), floor)
    return float(np.sqrt(np.mean(((p - o) / denom) ** 2)))


def relative_rms_sufficient(predicted: Any, observed: Any, tolerance: float) -> bool:
    return _relative_rms(predicted, observed) <= tolerance


def _spectrum_readout(key: str, lmin: int, lmax: int):
    def readout(record: Mapping[str, Any]):
        values = np.asarray(record[key], dtype=float)
        if values.ndim != 1:
            raise ValueError(f"{key} must be one-dimensional")
        if lmax >= len(values):
            raise ValueError(
                f"{key} only contains ell <= {len(values)-1}; requested {lmax}"
            )
        return values[lmin : lmax + 1]
    return readout


def cmb_spectrum_questions(
    *,
    lmin: int = 2,
    lmax: int = 2500,
    tolerance: float = 0.03,
) -> tuple[StrongQuestion, ...]:
    """Return the canonical strong CMB questions.

    The default tolerance is a declared comparison tolerance only. It is not
    treated as an intrinsic law or a permission to force agreement.
    """

    if lmin < 0 or lmax < lmin:
        raise ValueError("require 0 <= lmin <= lmax")

    failures = (
        FailureCondition(
            code="registration",
            description="Observed spectrum/covariance is absent or miscalibrated.",
            repair="Repair the observation record before revising dynamics.",
        ),
        FailureCondition(
            code="inference",
            description="Legacy parameter compiler does not close the spectrum.",
            repair="Revise the parameter inference map.",
        ),
        FailureCondition(
            code="dynamics",
            description="No parameter-only repair closes all strong questions.",
            repair="Derive a physical perturbation realization and retest.",
        ),
        FailureCondition(
            code="scope",
            description="Requested ell range lies outside the validated solver scope.",
            repair="Restrict scope or validate the extended range.",
        ),
    )

    def make(name: str, key: str, carrier: str) -> StrongQuestion:
        return StrongQuestion(
            name=name,
            scope=Scope(
                system="CMB angular anisotropy",
                boundary=f"multipoles {lmin} <= ell <= {lmax}",
                horizon="last scattering to present observation",
                tolerance=tolerance,
                units="muK^2",
                assumptions=(
                    "CAMB forward equations",
                    "declared nuisance and calibration treatment",
                ),
            ),
            intervention="Run the CAMB forward model for the compiled cosmology.",
            response_carrier=carrier,
            answer_space=f"real spectrum vector of length {lmax-lmin+1}",
            readout=_spectrum_readout(key, lmin, lmax),
            sufficiency=relative_rms_sufficient,
            latency="one CAMB forward solve",
            cost="backend-dependent",
            failure_conditions=failures,
        )

    return (
        make("CMB_TT", "totCl_TT", "temperature angular power spectrum"),
        make("CMB_EE", "totCl_EE", "E-mode angular power spectrum"),
        make("CMB_TE", "totCl_TE", "temperature/E-mode cross spectrum"),
        make("CMB_BB", "totCl_BB", "B-mode angular power spectrum"),
    )


def relative_rms(predicted: Any, observed: Any) -> float:
    """Public residual used by the assessment layer."""
    return _relative_rms(predicted, observed)
