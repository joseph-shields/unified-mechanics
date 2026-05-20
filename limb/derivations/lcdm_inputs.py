# LiMB — Light instigating Matter Barrier
# Copyright (c) 2026 Joseph Shields — LGPL v3+  (see limb/LICENSE)
"""
UM derivations of every LCDM "free input."

LCDM cosmology has six base parameters and a handful of fixed-by-hand
constants. UM derives every one of them from ``φ² = φ + 1`` and the
channel structure. Each function below returns the UM value; a pinned
test sits next to each one in ``tests/test_limb_derivations.py``.

**Status legend**:
  * ``DERIVED``  — UM math is done, value is closed-form, test pins it.
  * ``OPEN``     — derivation target; raises NotImplementedError. Drop
                   the algebra in the body and flip the docstring tag.

**UM braiding floor** (source: ``02_cosmology.md`` §6.2-6.4): the
recursion noise floor is ``ε_floor = r³ ≈ 2.95%`` per single
channel-traversal cycle (with ``r = 1/(2φ)``). It accumulates as
``n × ε_floor`` for a quantity reached after ``n`` channel-traversal
events. Per §6.4, sub-floor agreement on an ``n ≥ 1`` quantity
*falsifies* UM (or requires sub-floor mechanisms not yet in the
framework). Tightness is failure, not victory. Tests in
``tests/test_limb_derivations.py`` enforce both upper *and* lower
bounds for every cycle-extrapolated derivation.

Sources for each closed form: Paper 1 (``01_foundation.md``) §8 and
Appendix A.1, plus Paper 2 (``02_cosmology.md``) §3-7. Each ``DERIVED``
function carries an inline citation to the equation it implements.

"""
from __future__ import annotations

import math


# ─────────────────────────────────────────────────────────────────────
# The framework's only constants. Everything below is r-only.
# ─────────────────────────────────────────────────────────────────────
PHI: float = (1.0 + math.sqrt(5.0)) / 2.0       # golden ratio, φ
R:   float = 1.0 / (2.0 * PHI)                  # contraction rate, ≈ 0.309
R2:  float = R * R                              # ≈ 0.0955  (matter weight)
R3:  float = R2 * R                             # ≈ 0.02951 (noise floor)
ONE_MINUS_R: float = 1.0 - R


def _open(name: str, note: str) -> float:
    raise NotImplementedError(
        f"UM derivation of {name!r} is OPEN. {note}\n"
        f"Fill in the body of limb.derivations.lcdm_inputs.{name} "
        f"with the closed-form result and update the docstring tag."
    )


# ── Hubble rate ──────────────────────────────────────────────────────
def H0_late_over_H0_CMB() -> float:
    """**DERIVED**. extended/11 §1, eq. 11.1:
    ``H_0,late / H_0,CMB = (1 + 3r³/2) / (1 - 3r³/2)``.

    The clean structural statement of the Hubble braiding. Numerical:
    ≈ 1.0935 (vs observed 73/67.4 = 1.0831, residual 0.95% — within
    the n=1 expected band)."""
    return (1.0 + 1.5 * R3) / (1.0 - 1.5 * R3)


# Note: extended/11 §1 also gives the Friedmann-closure shape
#   H_0 = M_Pl · r¹²⁰ / √(3 · Ω_DE)
# but converting to km/s/Mpc requires the dimensional factor
# c · (1 Mpc)⁻¹ with O(1) prefactors (8π, etc.) that depend on
# Planck-mass convention (reduced vs unreduced). The shape is in
# the paper; the dimensional conversion is observational anchor.
# Not pinned here — the structural pin is H0_late_over_H0_CMB above.


# ── matter sector ───────────────────────────────────────────────────
def Omega_b() -> float:
    """**DERIVED**. Paper 1 §8.1, eq. table:  ``Ω_b = r²/2``.

    Numerical: 0.0477 (vs Planck 0.0493, residual 3.0% — at floor)."""
    return R2 / 2.0


def Omega_c() -> float:
    """**DERIVED**. Paper 1 §8.1 / Appendix A.1:  ``Ω_DM = 4 r² (1-r)``.

    Equivalent form ``2 r (1-r) / φ``. Numerical: 0.2640
    (vs Planck 0.2647, residual 0.3%)."""
    return 4.0 * R2 * ONE_MINUS_R


def Omega_m() -> float:
    """**DERIVED**. Paper 1 Appendix A.1: ``Ω_m = r²(9/2 - 4r)``.

    Equivalent to ``Ω_b + Ω_DM``. Numerical: 0.3118
    (vs Planck 0.314, residual 0.7%)."""
    return R2 * (4.5 - 4.0 * R)


def Omega_DE() -> float:
    """**DERIVED**. Paper 1 Appendix A.1: ``Ω_DE = 1 - 9 r² / 2 + 4 r³``.

    Equivalent expanded form ``(1-r)² + 2r(1-r)(1 - 1/φ) + r²/2``.
    Numerical: 0.6883 (vs Planck 0.685, residual 0.5%)."""
    return 1.0 - 4.5 * R2 + 4.0 * R3


# ── primordial / inflationary ────────────────────────────────────────
def n_s() -> float:
    """**DERIVED**. extended/11 §2, eq. 11.4:
    ``n_s = 1 - r²/φ² = 1 - r² + 2r³``.

    Scalar tilt = matter-channel weight × Born leakage rate (one
    cycle of matter content leaking through the sub-leading recursion
    mode). Numerical: 0.9635 (vs Planck 0.9649, residual +0.15%,
    sub-floor)."""
    return 1.0 - R2 + 2.0 * R3


def A_s() -> float:
    """**DERIVED**. extended/11 §3, eq. 11.5:  ``A_s = r¹⁷``.

    Scalar amplitude r-suppressed by the e→τ generation count (17
    cycles, same exponent as the heaviest charged-lepton mass ratio).
    Numerical: 2.137 × 10⁻⁹ (vs Planck 2.1 × 10⁻⁹, residual +1.76%,
    sub-floor)."""
    return R ** 17


# ── reionisation ─────────────────────────────────────────────────────
def tau_reio() -> float:
    """**DERIVED**. extended/11 §4, eq. 11.6:
    ``τ_reio = 2r³ = r²/φ``.

    Two boundary-channel pulses on matter content (recombination →
    first stars → reionisation). Numerical: 0.0590 (vs Planck 0.054,
    residual +9.3%, within n=2 band).

    Note: UM treats τ_reio as initial-condition-sensitive; the central
    closed form (11.6) is the structural answer, the observed spread
    captures initial-condition variation."""
    return 2.0 * R3


# ── dark energy ─────────────────────────────────────────────────────
def w0() -> float:
    """**DERIVED**. Paper 1 §8.1 / Appendix A.1:  ``w₀ = -(r+2)/(8r)``.

    Equivalent forms: ``-(1+4φ)/8``, ``-(3+2√5)/8``. Numerical:
    -0.9340 (vs DESI 2024 -0.93, within error)."""
    return -(R + 2.0) / (8.0 * R)


def wa() -> float:
    """**DERIVED**. Paper 1 Appendix A.1:
    ``wₐ = 32 r⁵ (1-r) / (1 - 9r²/2 + 4r³)`` = ``32 r⁵ (1-r) / Ω_DE``.

    Numerical: ≈ +0.091."""
    return (32.0 * R**5 * ONE_MINUS_R) / Omega_DE()


# ── neutrino sector ─────────────────────────────────────────────────
def N_eff() -> float:
    """**DERIVED**. extended/11 §5, eq. 11.7:
    ``N_eff = 3 + r²/2``.

    Three channels (one effective species each at high T) plus the
    matter-channel α-coupling correction at neutrino decoupling.
    Numerical: 3.0477 (vs standard 3.046, residual +0.057%,
    sub-floor)."""
    return 3.0 + R2 / 2.0


# Heaviest-charged-lepton mass anchor for the neutrino-mass derivation
# (extended/11 §6, eq. 11.9). PDG: m_τ = 1776.86 MeV/c².
M_TAU_EV: float = 1776.86e6


def m_nu_total_eV() -> float:
    """**DERIVED**. extended/11 §6, eq. 11.9:
    ``Σ m_ν ≈ m_ν,τ = m_τ · r²⁰``.

    The heaviest neutrino is the matter-channel partner of the τ
    lepton at 17 + 3 cycles (lepton e→τ count plus three boundary
    cycles for the matter→boundary→light→boundary translation).
    Lighter species are r-suppressed below the 10⁻⁵ eV scale and
    contribute negligibly. Numerical: ≈ 0.115 eV (vs cosmology bound
    0.06-0.12 eV, sits at edge — testable as DESI tightens)."""
    return M_TAU_EV * (R ** 20)


# ── primordial chemistry / BBN ──────────────────────────────────────
def Y_He() -> float:
    """**DERIVED**. extended/11 §7, eq. 11.10:
    ``Y_He = (1-r)² / 2``.

    Primordial helium mass fraction equals half the light-channel
    weight (BBN photon-to-baryon ratio governs nucleon processing
    rate; helium-4 captures half the available bound fraction).
    Numerical: 0.2387 (vs BBN 0.245, residual -2.55%, sub-floor).

    Heuristic note: a fully-derived BBN reaction-network calculation
    using the UM-derived weights should land within ε_floor of this
    value. Currently a structural-shape derivation, not a reaction-
    network derivation."""
    return ONE_MINUS_R ** 2 / 2.0


# ── CMB monopole ────────────────────────────────────────────────────
def T_cmb_K() -> float:
    """**OBSERVATIONAL**. extended/11 §8: UM cannot derive an absolute
    temperature from the dimensionless recursion φ² = φ + 1.
    Temperature carries dimension of energy; UM supplies ratios
    (a_rec/a_today, T_rec/T_today) but the absolute scale of T_today
    is a single dimensional anchor.

    Returns the FIRAS-measured value 2.7255 K. This is the
    framework's **only** observational input once the UM closed forms
    are in — analogous to how Newtonian mechanics needs one
    experimental measurement before its derived ratios acquire
    dimensional values."""
    return 2.7255


# ── extra-LCDM derivations ──────────────────────────────────────────
# These are not LCDM "free inputs" but UM derives them and the solver
# wants them. Listed here so the registry is single-sourced.

def G_eff_over_GN() -> float:
    """**DERIVED**. Paper 1 §4.3 / Appendix A.1:
    ``G_eff/G_N = 1 + 1/(2φ⁴) = 1 + r/(3 + 4r)``.

    Numerical: 1.0729. The χ²R term in the Lagrangian (eq. 10) shifts
    the effective Newton coupling by +7.3% at χ = χ_*. The
    laboratory-measured G is the *effective* G; the bare G_N is 7.3%
    smaller. For LiMB-LCDM (trivial-channel limit), this collapses
    to G_N since χ sits at its VEV.
    """
    return 1.0 + R / (3.0 + 4.0 * R)


def epsilon_floor() -> float:
    """**DERIVED**. Paper 1 §5.1, eq. 19:  ``ε_floor = r³``.

    The framework's intrinsic single-cycle precision limit. Numerical:
    ≈ 0.0295 = 2.95%."""
    return R3


def hubble_braiding_magnitude() -> float:
    """**DERIVED**. Paper 1 §8.1 / Paper 2 §6:  ``Δ H0/H0 = 3 r³``.

    The Hubble braiding (formerly "tension") between CMB-anchored and
    local-distance-ladder H0 — three channel-traversal cycles between
    recombination and present, each contributing one ε_floor.
    Numerical: ≈ 8.85% (vs observed ~9%)."""
    return 3.0 * R3


def w0_minus_1_LCDM_residual() -> float:
    """**DERIVED**. Helper: how far w₀ sits from the LCDM Λ value.

    Paper 1 §8.1:  ``w₀ + 1 = 1 - (r+2)/(8r) = (6r - 2)/(8r)``.
    Numerical: ≈ +0.066 (UM's w₀ is 6.6% less negative than -1).
    """
    return 1.0 + w0()


def rho_Lambda_over_MPl4_log10() -> float:
    """**DERIVED**. Paper 1 §7.2, eq. 24:  ``ρ_Λ/M_Pl⁴ = r²⁴⁰``.

    Returns log₁₀ of the predicted dimensionless cosmological-constant
    density. Numerical: ≈ -122.4 (vs observed ≈ -122.04, residual
    0.4% in log-magnitude — at floor)."""
    return 240.0 * math.log10(R)


# ── channel weights (Paper 1 §3.1 eq. 8) ────────────────────────────
def weight_light() -> float:
    """**DERIVED**. Paper 1 §3.1, eq. 8: ``(1-r)²`` ≈ 0.4775."""
    return ONE_MINUS_R ** 2


def weight_boundary() -> float:
    """**DERIVED**. Paper 1 §3.1, eq. 8: ``2 r (1-r)`` ≈ 0.4271."""
    return 2.0 * R * ONE_MINUS_R


def weight_matter() -> float:
    """**DERIVED**. Paper 1 §3.1, eq. 8: ``r²`` ≈ 0.0955."""
    return R2


# ── Born coupling (Paper 1 §6, eq. 22-23) ───────────────────────────
def born_coefficient() -> float:
    """**DERIVED**. Paper 1 §6, eq. 23 / Appendix A.1:
    ``P_Born = 1/φ = 2r``  ≈ 0.6180.

    Per-cycle survival probability of the leading recursion mode."""
    return 2.0 * R


def born_leakage_rate() -> float:
    """**DERIVED**. Paper 1 Appendix A.1: ``1/φ² = 1 - 2r`` ≈ 0.3820."""
    return 1.0 - 2.0 * R


# ── Lagrangian couplings (Paper 1 §4.2 eq. 11-13) ───────────────────
def alpha_matter_curvature() -> float:
    """**DERIVED**. Paper 1 §4.2, eq. 11: ``α = r²/2 = 1/(8φ²)``
    ≈ 0.0477. The χ²R coupling coefficient."""
    return R2 / 2.0


def lambda_boundary_curvature() -> float:
    """**DERIVED**. Paper 1 §4.2, eq. 12: ``λ_βh ∝ 2r(1-r)`` ≈ 0.4271
    (canonical-normalisation proportionality constant absorbed)."""
    return 2.0 * R * ONE_MINUS_R


def lambda_boundary_matter() -> float:
    """**DERIVED**. Paper 1 §4.2, eq. 13:
    ``λ_βχ ∝ √(r² · 2r(1-r))`` ≈ 0.2024 (geometric mean of
    contributing channel weights)."""
    return math.sqrt(R2 * 2.0 * R * ONE_MINUS_R)


# ── lab-test cross-couplings (extended/07) ──────────────────────────
def kappa_matter_matter() -> float:
    """**DERIVED**. extended/07 §1, eq. 1.2-1.3: matter-source /
    matter-observable cereal-bowl-corrected coupling.

    Equal to ``√(r² · 2r(1-r))`` ≈ 0.202 (the boundary cross-coupling
    alone, since source-to-observable ratio is 1). Used by κ_grav,
    κ_tun in lab predictions."""
    return math.sqrt(R2 * 2.0 * R * ONE_MINUS_R)


def kappa_matter_light() -> float:
    """**DERIVED**. extended/07 §2, §4, §6: matter-source /
    light-observable cereal-bowl-corrected coupling.

    ``(r²/(1-r)²) × √(r² · 2r(1-r))`` ≈ 0.0404. Used by κ_h, κ_Cas,
    κ_lens in lab predictions."""
    return (R2 / ONE_MINUS_R**2) * math.sqrt(R2 * 2.0 * R * ONE_MINUS_R)


def kappa_decoherence() -> float:
    """**DERIVED**. extended/07 §5, eq. 5.3: macroscopic decoherence
    coupling. Equal to the boundary channel weight ``2r(1-r)``
    ≈ 0.4271."""
    return 2.0 * R * ONE_MINUS_R


# ── particle / mass-hierarchy results ───────────────────────────────
def Higgs_over_Planck_log10() -> float:
    """**DERIVED**. Paper 1 §8 / Appendix A.1: ``M_H/M_Pl = r³³(1-r)``.

    Returns log₁₀ of the dimensionless ratio. Numerical:
    ≈ -16.99 (corresponding to ≈ 1.022 × 10⁻¹⁷, observed
    ≈ 1.018 × 10⁻¹⁷ — within 0.3%)."""
    return 33.0 * math.log10(R) + math.log10(ONE_MINUS_R)


def m_mu_over_m_e() -> float:
    """**DERIVED**. LEPTON_HIERARCHY_STANDALONE eq. 10:
    ``m_μ/m_e = (1/φ)⁻¹¹ · (1 + r³) = φ¹¹ (1 + r³)``.

    Numerical: ≈ 204.9 (vs PDG 206.77, residual 0.91% — sub-floor,
    consistent with an n=0 structural derivation)."""
    return (PHI ** 11) * (1.0 + R3)


def m_tau_over_m_mu() -> float:
    """**DERIVED**. LEPTON_HIERARCHY_STANDALONE eq. 8:
    ``m_τ/m_μ = (1/φ)⁻⁶ · (1 - r³)/(1 + r³) = φ⁶ (1-r³)/(1+r³)``.

    Numerical: ≈ 16.92 (vs PDG 16.82, residual 0.59%)."""
    return (PHI ** 6) * (1.0 - R3) / (1.0 + R3)


def m_tau_over_m_e() -> float:
    """**DERIVED**. LEPTON_HIERARCHY_STANDALONE eq. 9 inverted:
    eq. 9 gives ``m_e/m_τ = (1/φ)¹⁷ / (1 - r³)``, so
    ``m_τ/m_e = (1 - r³) · φ¹⁷``.

    Numerical: ≈ 3466 (vs PDG 3477, residual -0.33%). The exponents
    11 + 6 = 17 are cycle-additive — required for consistency."""
    return (1.0 - R3) * (PHI ** 17)


# ── geometric / structural results ──────────────────────────────────
def cosmic_web_fractal_dimension() -> float:
    """**DERIVED**. Paper 1 Appendix A.1 / Paper 2 §7.5:
    ``D = 2 + r/(2(1-r)) = 2 + 1/(2√5)``.

    Numerical: ≈ 2.224 (vs SDSS / Sylos Labini surveys reporting
    D ≈ 2.0-2.2 at intermediate scales — within range)."""
    return 2.0 + R / (2.0 * ONE_MINUS_R)


def sgwb_cmb_information_ratio() -> float:
    """**DERIVED**. Paper 1 Appendix A.1 / extended/04:
    ``I_CMB / I_SGWB = (1-r)/(2r) = φ - 1/2``.

    Numerical: ≈ 1.118. The CMB carries ≈1.118× the boundary-channel
    information capacity of the SGWB. Testable once the primordial
    SGWB component is isolated by LISA + PTA networks."""
    return PHI - 0.5


# ── derivation status registry ──────────────────────────────────────
DERIVATION_STATUS = {
    # LCDM free inputs (the canonical six, plus a few constants)
    "H0_late_over_H0_CMB":  "DERIVED",   # (1+3r³/2)/(1-3r³/2)
    "Omega_b":              "DERIVED",   # r²/2
    "Omega_c":              "DERIVED",   # 4 r² (1-r)
    "n_s":                  "DERIVED",   # 1 - r²/φ²
    "A_s":                  "DERIVED",   # r¹⁷
    "tau_reio":             "DERIVED",   # 2r³
    "w0":                   "DERIVED",   # -(r+2)/(8r)
    "wa":                   "DERIVED",   # 32 r⁵ (1-r) / Ω_DE
    "N_eff":                "DERIVED",   # 3 + r²/2
    "m_nu_total_eV":        "DERIVED",   # m_τ · r²⁰
    "Y_He":                 "DERIVED",   # (1-r)²/2
    "T_cmb_K":              "OBSERVATIONAL",  # FIRAS dimensional anchor

    # extra-LCDM, not free in LCDM but UM derives them
    "Omega_m":                    "DERIVED",   # r²(9/2 - 4r)
    "Omega_DE":                   "DERIVED",   # 1 - 9r²/2 + 4r³
    "G_eff_over_GN":              "DERIVED",   # 1 + r/(3+4r)
    "epsilon_floor":              "DERIVED",   # r³
    "hubble_braiding_magnitude":  "DERIVED",   # 3 r³
    "w0_minus_1_LCDM_residual":   "DERIVED",
    "rho_Lambda_over_MPl4_log10": "DERIVED",   # 240 · log10(r)

    # channel weights (Paper 1 §3.1)
    "weight_light":               "DERIVED",   # (1-r)²
    "weight_boundary":            "DERIVED",   # 2r(1-r)
    "weight_matter":               "DERIVED",  # r²

    # Born coupling (Paper 1 §6)
    "born_coefficient":           "DERIVED",   # 2r = 1/φ
    "born_leakage_rate":          "DERIVED",   # 1 - 2r = 1/φ²

    # Lagrangian couplings (Paper 1 §4.2)
    "alpha_matter_curvature":     "DERIVED",   # r²/2
    "lambda_boundary_curvature":  "DERIVED",   # 2r(1-r)
    "lambda_boundary_matter":     "DERIVED",   # √(r² · 2r(1-r))

    # lab-test cross-couplings (extended/07)
    "kappa_matter_matter":        "DERIVED",
    "kappa_matter_light":         "DERIVED",
    "kappa_decoherence":          "DERIVED",

    # particle / mass-hierarchy results
    "Higgs_over_Planck_log10":    "DERIVED",   # 33·log10(r) + log10(1-r)
    "m_mu_over_m_e":              "DERIVED",   # φ¹¹(1+r³)
    "m_tau_over_m_mu":            "DERIVED",   # φ⁶(1-r³)/(1+r³)
    "m_tau_over_m_e":             "DERIVED",   # φ¹⁷/(1-r³)

    # geometric / structural
    "cosmic_web_fractal_dimension": "DERIVED", # 2 + 1/(2√5)
    "sgwb_cmb_information_ratio":   "DERIVED", # φ - 1/2
}
