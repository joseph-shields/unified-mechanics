# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
LiMB-LCDM forward solve via CAMB.

CAMB is the community-standard CMB Boltzmann reference solver
(Lewis & Challinor, 20+ years of validation). Using CAMB as the
LiMB-LCDM kernel removes any "the solver is buggy" excuse — if
LiMB-LCDM matches Planck via this path, the conclusion is about
**UM**, not about the code.

Pipeline
--------
1. ``build_LiMBLCDMCosmology()`` — assemble all UM-derived parameters
   into a :class:`~limb.cosmology.Cosmology` object (zero calls to CAMB).
2. ``cosmology_to_camb_params(cosmo)`` — translate that object into a
   ``camb.CAMBparams`` instance. This is a pure structural conversion;
   no fitting, no tuning.
3. ``compute_limb_lcdm_cls()`` — run CAMB end-to-end and return C_ℓ.

This separation means any change to a UM derivation automatically
propagates through to the solver — there is no second place to update.

This backend handles the trivial-channel limit (LCDM with all inputs
UM-derived). Full LiMB-UM mode (non-zero channel source terms) requires
a modified-gravity backend (EFTCAMB, hi_class) — that lands later.
"""
from __future__ import annotations

from limb.cosmology import Cosmology
from limb.lcdm import build_LiMBLCDMCosmology


def cosmology_to_camb_params(cosmo: Cosmology,
                              lmax: int = 2500,
                              lens_potential_accuracy: int = 1):
    """Translate a :class:`~limb.cosmology.Cosmology` into a ``camb.CAMBparams``.

    This is a pure structural conversion — every field on ``cosmo`` maps
    directly to a CAMB input. No derivations happen here.

    Parameters
    ----------
    cosmo : Cosmology
        Parameter container, typically from ``build_LiMBLCDMCosmology()``.
    lmax : int
        Maximum multipole. CAMB is validated to ℓ ≈ 2500 against Planck;
        LiMB has been run to ℓ = 100 000 without numerical instability.
    lens_potential_accuracy : int
        Passed to ``camb.set_for_lmax``. 1 is sufficient for C_ℓ comparison.

    Returns
    -------
    camb.CAMBparams
        Configured params object. Call ``camb.get_results(pars)`` to solve.
    """
    import camb

    h = cosmo.H0 / 100.0
    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0    = cosmo.H0,
        ombh2 = cosmo.Omega_b * h**2,
        omch2 = cosmo.Omega_c * h**2,
        omk   = cosmo.Omega_k,
        tau   = cosmo.tau_reio,
        mnu   = cosmo.m_nu_eV,
        nnu   = cosmo.N_eff,
        YHe   = cosmo.Y_He,
        TCMB  = cosmo.T_cmb,
    )
    pars.InitPower.set_params(
        ns = cosmo.n_s,
        As = cosmo.A_s,
        r  = 0.0,           # no tensor mode in trivial-channel limit
    )
    pars.set_dark_energy(
        w                 = cosmo.w0,
        wa                = cosmo.wa,
        dark_energy_model = "ppf",   # smooth Parameterized Post-Friedmann
    )
    pars.set_for_lmax(lmax, lens_potential_accuracy=lens_potential_accuracy)
    return pars


def build_camb_params(lmax: int = 2500, lens_potential_accuracy: int = 1):
    """Convenience: UM default cosmology → ``camb.CAMBparams``.

    Equivalent to::

        cosmology_to_camb_params(build_LiMBLCDMCosmology(), lmax=lmax)

    Use :func:`cosmology_to_camb_params` directly if you want to pass a
    custom or modified :class:`~limb.cosmology.Cosmology`.
    """
    return cosmology_to_camb_params(
        build_LiMBLCDMCosmology(),
        lmax=lmax,
        lens_potential_accuracy=lens_potential_accuracy,
    )


def compute_limb_lcdm_cls(lmax: int = 2500,
                           lens_potential_accuracy: int = 1) -> dict:
    """Run CAMB end-to-end with UM-derived inputs and return C_ℓ.

    Returns
    -------
    dict with keys:

    ``ells``
        ℓ array, shape ``(lmax+1,)``.
    ``totCl_TT``, ``totCl_EE``, ``totCl_BB``, ``totCl_TE``
        Total (lensed) power spectra in μK².
    ``unlensed_TT``
        Unlensed scalar TT.
    ``derived_params``
        CAMB's derived-parameter dict (``sigma8``, ``rdrag``, etc.).
    ``cosmo``
        The :class:`~limb.cosmology.Cosmology` object used.
    ``camb_pars``
        The ``camb.CAMBparams`` object used.
    """
    import camb
    import numpy as np

    cosmo = build_LiMBLCDMCosmology()
    pars  = cosmology_to_camb_params(cosmo, lmax=lmax,
                                     lens_potential_accuracy=lens_potential_accuracy)
    results = camb.get_results(pars)
    powers  = results.get_cmb_power_spectra(pars, lmax=lmax, CMB_unit="muK")

    total    = np.asarray(powers["total"])           # (lmax+1, 4): TT EE BB TE
    unlensed = np.asarray(powers["unlensed_scalar"]) # (lmax+1, 4)
    ells     = np.arange(total.shape[0])

    return {
        "ells":           ells,
        "totCl_TT":       total[:, 0],
        "totCl_EE":       total[:, 1],
        "totCl_BB":       total[:, 2],
        "totCl_TE":       total[:, 3],
        "unlensed_TT":    unlensed[:, 0],
        "derived_params": results.get_derived_params(),
        "cosmo":          cosmo,
        "camb_pars":      pars,
    }


def planck_lcdm_reference_cls(lmax: int = 2500,
                               lens_potential_accuracy: int = 1) -> dict:
    """Reference CAMB run with Planck 2018 best-fit LCDM inputs.

    Same code path as :func:`compute_limb_lcdm_cls` but with Planck
    parameters instead of UM derivations. Use this as the side-by-side
    baseline: any LiMB-vs-Planck residual is then purely from the
    difference between UM-derived and Planck-fitted parameter values,
    not from solver settings.
    """
    import camb
    import numpy as np

    planck = Cosmology(
        H0=67.36, Omega_b=0.02237/0.6736**2, Omega_c=0.1200/0.6736**2,
        Omega_k=0.0, T_cmb=2.7255, tau_reio=0.0544,
        N_eff=3.046, m_nu_eV=0.06, Y_He=0.245,
        n_s=0.9649, A_s=2.1e-9, k_pivot=0.05,
        w0=-1.0, wa=0.0,
    )
    pars    = cosmology_to_camb_params(planck, lmax=lmax,
                                       lens_potential_accuracy=lens_potential_accuracy)
    results = camb.get_results(pars)
    powers  = results.get_cmb_power_spectra(pars, lmax=lmax, CMB_unit="muK")
    total   = np.asarray(powers["total"])

    return {
        "ells":      np.arange(total.shape[0]),
        "totCl_TT":  total[:, 0],
        "totCl_EE":  total[:, 1],
        "totCl_BB":  total[:, 2],
        "totCl_TE":  total[:, 3],
        "cosmo":     planck,
        "camb_pars": pars,
    }


def main() -> None:
    """CLI entry point: run the LiMB-LCDM solver and print a summary."""
    import sys

    lmax = int(sys.argv[1]) if len(sys.argv) > 1 else 2500
    print(f"LiMB-LCDM forward solve  (lmax={lmax})")
    print("Deriving UM parameters...")

    out   = compute_limb_lcdm_cls(lmax=lmax)
    cosmo = out["cosmo"]
    dp    = out["derived_params"]

    print(f"\nUM-derived inputs:")
    print(f"  H0        = {cosmo.H0:.4f} km/s/Mpc  (dimensional anchor)")
    print(f"  Omega_b   = {cosmo.Omega_b:.6f}  (r²/2)")
    print(f"  Omega_c   = {cosmo.Omega_c:.6f}  (4r²(1-r))")
    print(f"  n_s       = {cosmo.n_s:.6f}  (1 - r²/φ²)")
    print(f"  A_s       = {cosmo.A_s:.4e}  (r¹⁷)")
    print(f"  tau_reio  = {cosmo.tau_reio:.6f}  (2r³)")
    print(f"  w0        = {cosmo.w0:.6f}  (-(r+2)/(8r))")
    print(f"  wa        = {cosmo.wa:.6f}  (32r⁵(1-r)/Ω_DE)")

    print(f"\nCAMB derived parameters:")
    for key in ("sigma8", "rdrag", "thetastar", "YHe"):
        if key in dp:
            print(f"  {key:12s} = {dp[key]:.6f}")

    tt  = out["totCl_TT"]
    ell = out["ells"]
    peak_ell = int(ell[tt.argmax()])
    print(f"\nCMB TT spectrum:")
    print(f"  First peak ℓ ≈ {peak_ell}")
    print(f"  Peak power  = {tt.max():.1f} μK²")
    print(f"\nC_ℓ computed to ℓ = {lmax}. Done.")
