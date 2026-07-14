"""Legacy UM formula catalogue retyped as observation/inference evidence.

The old ``limb.derivations.lcdm_inputs`` functions are preserved for
reproducibility. This adapter changes their logical role:

- dimensional anchors remain observations;
- exact algebraic identities remain algebraic identities;
- numerical parameter dictionaries remain inference candidates until a
  physical realization derives them from action/dynamics.

This is the requested use of the old framework as the observation-inference
layer, rather than silently treating every closed form as foundational physics.
"""
from __future__ import annotations

from dataclasses import asdict

from limb.cosmology import Cosmology
from limb.derivations import lcdm_inputs as old

from .types import ClaimStatus, EvidenceRecord


H0_ANCHOR_KM_S_MPC = 67.4


def _candidate(
    name: str,
    value: float,
    expression: str,
    source: str,
    *,
    units: str = "",
    assumptions: tuple[str, ...] = (),
    notes: str = "",
) -> EvidenceRecord:
    return EvidenceRecord(
        name=name,
        value=float(value),
        status=ClaimStatus.INFERENCE_CANDIDATE,
        expression=expression,
        source=source,
        units=units,
        assumptions=assumptions,
        notes=notes,
    )


def legacy_evidence() -> tuple[EvidenceRecord, ...]:
    """Return a complete provenance ledger for LiMB's CAMB inputs."""

    common = (
        "Legacy golden-recursion dictionary is treated as a candidate "
        "observation-to-parameter inference map, not as a completed "
        "microphysical derivation."
    )
    return (
        EvidenceRecord(
            name="H0",
            value=H0_ANCHOR_KM_S_MPC,
            status=ClaimStatus.OBSERVATION,
            expression="H0 = 67.4 km/s/Mpc",
            source="CMB-anchored Friedmann-scale input",
            units="km/s/Mpc",
            notes="Dimensional anchor.",
        ),
        _candidate("Omega_b", old.Omega_b(), "r^2 / 2", "legacy UM", notes=common),
        _candidate(
            "Omega_c", old.Omega_c(), "4 r^2 (1-r)", "legacy UM", notes=common
        ),
        EvidenceRecord(
            name="Omega_k",
            value=0.0,
            status=ClaimStatus.INFERENCE_CANDIDATE,
            expression="Omega_k = 0",
            source="legacy channel-sum closure",
            assumptions=("flat effective CAMB background",),
            notes=(
                "Algebraic channel-sum closure is not by itself a derivation "
                "of spatial flatness from field equations."
            ),
        ),
        EvidenceRecord(
            name="T_cmb",
            value=old.T_cmb_K(),
            status=ClaimStatus.OBSERVATION,
            expression="T_cmb = 2.7255 K",
            source="FIRAS anchor",
            units="K",
        ),
        _candidate(
            "tau_reio",
            old.tau_reio(),
            "2 r^3",
            "legacy UM",
            assumptions=("effective reionisation history",),
            notes=common,
        ),
        _candidate("N_eff", old.N_eff(), "3 + r^2/2", "legacy UM", notes=common),
        _candidate(
            "m_nu_eV",
            old.m_nu_total_eV(),
            "m_tau r^20",
            "legacy UM",
            units="eV",
            assumptions=("single effective massive species",),
            notes=common,
        ),
        _candidate(
            "Y_He",
            old.Y_He(),
            "(1-r)^2 / 2",
            "legacy UM",
            assumptions=("effective BBN mapping",),
            notes=common,
        ),
        _candidate(
            "n_s", old.n_s(), "1 - r^2 + 2 r^3", "legacy UM", notes=common
        ),
        _candidate("A_s", old.A_s(), "r^17", "legacy UM", notes=common),
        EvidenceRecord(
            name="k_pivot",
            value=0.05,
            status=ClaimStatus.OBSERVATION,
            expression="k_pivot = 0.05 Mpc^-1",
            source="conventional primordial-spectrum pivot",
            units="1/Mpc",
        ),
        _candidate(
            "w0",
            old.w0(),
            "-(r+2)/(8r)",
            "legacy UM",
            assumptions=("CPL effective dark-energy representation",),
            notes=common,
        ),
        _candidate(
            "wa",
            old.wa(),
            "32 r^5(1-r)/Omega_DE",
            "legacy UM",
            assumptions=("CPL effective dark-energy representation",),
            notes=common,
        ),
    )


def build_observation_inference_cosmology() -> tuple[Cosmology, tuple[EvidenceRecord, ...]]:
    """Compile the legacy evidence ledger into a CAMB-facing cosmology."""

    evidence = legacy_evidence()
    values = {record.name: record.value for record in evidence}
    cosmo = Cosmology(
        H0=values["H0"],
        Omega_b=values["Omega_b"],
        Omega_c=values["Omega_c"],
        Omega_k=values["Omega_k"],
        T_cmb=values["T_cmb"],
        tau_reio=values["tau_reio"],
        N_eff=values["N_eff"],
        m_nu_eV=values["m_nu_eV"],
        Y_He=values["Y_He"],
        n_s=values["n_s"],
        A_s=values["A_s"],
        k_pivot=values["k_pivot"],
        w0=values["w0"],
        wa=values["wa"],
    )
    return cosmo, evidence


def evidence_as_dicts() -> list[dict]:
    return [asdict(item) for item in legacy_evidence()]
