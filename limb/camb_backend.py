# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
LiMB-LCDM forward solve via CAMB.

CAMB is the community-standard CMB Boltzmann reference solver
(Lewis & Challinor, 20+ years of validation). Using CAMB as the
LiMB-LCDM kernel removes any "the solver is buggy" excuse — if
LiMB-LCDM matches Planck via this path, the conclusion is about
**UM**, not about the code.

This backend only handles the trivial-channel limit (LCDM with all
inputs UM-derived). The full LiMB-UM mode requires a modified-gravity
backend (EFTCAMB, hi_class) — that lands later.
"""
from __future__ import annotations

from osiris.limb.derivations import lcdm_inputs as D


# Dimensional anchor — UM derives the SHAPE of H_0 (the Hubble braiding
# 3r³ tension) but not the absolute scale (recursion is dimensionless).
H0_DIMENSIONAL_ANCHOR_KM_S_MPC: float = 67.4   # CMB-anchored Friedmann closure


def build_camb_params(lmax: int = 2500,
                       lens_potential_accuracy: int = 1):
    """Construct a ``camb.CAMBparams`` populated entirely from UM
    derivations. Returns the configured params object — caller then
    runs ``camb.get_results(pars)``.
    """
    import camb   # imported lazily so the module is import-cheap

    h = H0_DIMENSIONAL_ANCHOR_KM_S_MPC / 100.0
    ombh2 = D.Omega_b() * h**2          # UM r²/2 · h²
    omch2 = D.Omega_c() * h**2          # UM 4r²(1-r) · h²

    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0      = H0_DIMENSIONAL_ANCHOR_KM_S_MPC,
        ombh2   = ombh2,
        omch2   = omch2,
        omk     = 0.0,                  # UM forces flatness (∑Ω = 1)
        tau     = D.tau_reio(),         # UM 2r³ ≈ 0.0590
        mnu     = D.m_nu_total_eV(),    # UM m_τ · r²⁰ ≈ 0.115 eV
        nnu     = D.N_eff(),            # UM 3 + r²/2
        YHe     = D.Y_He(),             # UM (1-r)²/2
        TCMB    = D.T_cmb_K(),          # FIRAS anchor
    )
    pars.InitPower.set_params(
        ns      = D.n_s(),              # UM 1 - r²/φ²
        As      = D.A_s(),              # UM r¹⁷
        r       = 0.0,                  # no tensor mode in trivial limit
    )
    pars.set_dark_energy(
        w       = D.w0(),               # UM -(r+2)/(8r)
        wa      = D.wa(),               # UM 32r⁵(1-r)/Ω_DE
        dark_energy_model = "ppf",      # smooth Parameterized Post-Friedmann
    )
    pars.set_for_lmax(lmax, lens_potential_accuracy=lens_potential_accuracy)
    return pars


def compute_limb_lcdm_cls(lmax: int = 2500,
                           lens_potential_accuracy: int = 1) -> dict:
    """Run CAMB end-to-end with UM-derived inputs and return C_ℓ.

    Returns
    -------
    dict with keys:
        ``ells``           — ℓ array, shape (lmax+1,)
        ``totCl_TT``       — total (lensed) TT in μK², shape (lmax+1,)
        ``totCl_EE``       — total (lensed) EE in μK²
        ``totCl_BB``       — total (lensed) BB in μK²
        ``totCl_TE``       — total (lensed) TE in μK²
        ``unlensed_TT``    — unlensed scalar TT
        ``derived_params`` — CAMB's derived-param dict (sigma8, etc.)
        ``camb_pars``      — the CAMBparams object used
    """
    import camb
    import numpy as np

    pars = build_camb_params(lmax=lmax,
                              lens_potential_accuracy=lens_potential_accuracy)
    results = camb.get_results(pars)
    powers = results.get_cmb_power_spectra(pars, lmax=lmax, CMB_unit="muK")

    total = np.asarray(powers["total"])              # (lmax+1, 4) cols TT,EE,BB,TE
    unlensed = np.asarray(powers["unlensed_scalar"]) # (lmax+1, 4)
    ells = np.arange(total.shape[0])

    return {
        "ells":           ells,
        "totCl_TT":       total[:, 0],
        "totCl_EE":       total[:, 1],
        "totCl_BB":       total[:, 2],
        "totCl_TE":       total[:, 3],
        "unlensed_TT":    unlensed[:, 0],
        "derived_params": results.get_derived_params(),
        "camb_pars":      pars,
    }


def planck_lcdm_reference_cls(lmax: int = 2500,
                                lens_potential_accuracy: int = 1) -> dict:
    """Reference CAMB run with **Planck 2018 best-fit** LCDM inputs.

    Same code path as ``compute_limb_lcdm_cls`` but with the Planck
    parameters dropped in directly instead of UM derivations. Used as
    the side-by-side baseline so ANY LiMB-vs-Planck residual is
    isolated to the difference between UM-derived and Planck-fitted
    parameter values, NOT solver settings.
    """
    import camb
    import numpy as np

    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=67.36, ombh2=0.02237, omch2=0.1200, omk=0.0,
        tau=0.0544, mnu=0.06, nnu=3.046, YHe=0.245, TCMB=2.7255,
    )
    pars.InitPower.set_params(ns=0.9649, As=2.1e-9, r=0.0)
    pars.set_dark_energy(w=-1.0, wa=0.0, dark_energy_model="ppf")
    pars.set_for_lmax(lmax, lens_potential_accuracy=lens_potential_accuracy)

    results = camb.get_results(pars)
    powers = results.get_cmb_power_spectra(pars, lmax=lmax, CMB_unit="muK")
    total = np.asarray(powers["total"])
    return {
        "ells":     np.arange(total.shape[0]),
        "totCl_TT": total[:, 0],
        "totCl_EE": total[:, 1],
        "totCl_BB": total[:, 2],
        "totCl_TE": total[:, 3],
    }
