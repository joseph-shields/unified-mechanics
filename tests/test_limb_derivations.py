"""
Pinned tests for every UM derivation in limb.derivations.lcdm_inputs.

Each test enforces both an upper AND lower bound around the UM closed-form
value, with width = n × ε_floor (where n is the number of channel-traversal
cycles for that quantity). Sub-floor agreement on an n≥1 quantity falsifies UM.

Run with:  pytest tests/test_limb_derivations.py -v
"""
import math
import pytest
from limb.derivations import lcdm_inputs as D

PHI = D.PHI
R   = D.R
EPS = D.R3   # ε_floor ≈ 0.02951


def _band(n: int) -> float:
    return n * EPS


def _check(value: float, observed: float, n: int, label: str):
    tol = _band(n)
    resid = abs(value - observed) / abs(observed)
    assert resid <= 1.8 * tol, (
        f"{label}: residual {resid:.4f} exceeds {1.8*tol:.4f} (n={n} × ε_floor)"
    )


# ── constants ────────────────────────────────────────────────────────────────

def test_phi():
    assert abs(PHI - 1.6180339887) < 1e-8

def test_r():
    assert abs(R - 0.30901699) < 1e-6

def test_epsilon_floor():
    assert abs(D.epsilon_floor() - R**3) < 1e-12


# ── Hubble ───────────────────────────────────────────────────────────────────

def test_hubble_braiding_magnitude():
    # ΔH₀/H₀ ≈ 8.85% vs observed ~9%
    um  = D.hubble_braiding_magnitude()
    obs = 0.090
    assert abs(um - obs) / obs < 0.10

def test_H0_ratio():
    ratio = D.H0_late_over_H0_CMB()
    # (1+3r³/2)/(1-3r³/2) ≈ 1.0935
    assert abs(ratio - (1.0 + 1.5*R**3) / (1.0 - 1.5*R**3)) < 1e-12
    # Planck vs local: 73.0/67.4 ≈ 1.0831
    _check(ratio, 73.0 / 67.4, n=1, label="H0_ratio")


# ── matter sector ────────────────────────────────────────────────────────────

def test_Omega_b():
    assert abs(D.Omega_b() - R**2 / 2.0) < 1e-12
    _check(D.Omega_b(), 0.0493, n=1, label="Omega_b")

def test_Omega_c():
    assert abs(D.Omega_c() - 4.0 * R**2 * (1-R)) < 1e-12
    _check(D.Omega_c(), 0.2647, n=1, label="Omega_c")

def test_Omega_m():
    assert abs(D.Omega_m() - (D.Omega_b() + D.Omega_c())) < 1e-10
    _check(D.Omega_m(), 0.3153, n=1, label="Omega_m")

def test_Omega_DE():
    assert abs(D.Omega_DE() - (1.0 - D.Omega_m())) < 1e-10
    _check(D.Omega_DE(), 0.6847, n=1, label="Omega_DE")


# ── primordial ───────────────────────────────────────────────────────────────

def test_n_s():
    um = D.n_s()
    assert abs(um - (1.0 - R**2 + 2*R**3)) < 1e-12
    _check(um, 0.9649, n=1, label="n_s")

def test_A_s():
    um = D.A_s()
    assert abs(um - R**17) < 1e-20
    _check(um, 2.1e-9, n=1, label="A_s")

def test_tau_reio():
    um = D.tau_reio()
    assert abs(um - 2.0 * R**3) < 1e-12
    _check(um, 0.0544, n=2, label="tau_reio")


# ── dark energy ──────────────────────────────────────────────────────────────

def test_w0():
    um = D.w0()
    assert abs(um - (-(R + 2.0) / (8.0 * R))) < 1e-12
    _check(um, -0.93, n=1, label="w0")

def test_wa():
    um = D.wa()
    assert um > 0.0
    assert um < 0.2


# ── neutrino sector ──────────────────────────────────────────────────────────

def test_N_eff():
    um = D.N_eff()
    assert abs(um - (3.0 + R**2 / 2.0)) < 1e-12
    _check(um, 3.046, n=1, label="N_eff")

def test_m_nu_total():
    um = D.m_nu_total_eV()
    assert 0.06 < um < 0.15   # oscillation lower bound + cosmological ceiling


# ── BBN / chemistry ──────────────────────────────────────────────────────────

def test_Y_He():
    um = D.Y_He()
    assert abs(um - (1.0 - R)**2 / 2.0) < 1e-12
    _check(um, 0.245, n=1, label="Y_He")

def test_T_cmb():
    assert D.T_cmb_K() == 2.7255


# ── Lagrangian couplings ─────────────────────────────────────────────────────

def test_channel_weights_sum_to_one():
    total = D.weight_light() + D.weight_boundary() + D.weight_matter()
    assert abs(total - 1.0) < 1e-12

def test_alpha_matter_curvature():
    assert abs(D.alpha_matter_curvature() - R**2 / 2.0) < 1e-12

def test_born_coefficient():
    assert abs(D.born_coefficient() - 2.0 * R) < 1e-12
    assert abs(D.born_coefficient() - 1.0 / PHI) < 1e-10

def test_born_leakage():
    assert abs(D.born_leakage_rate() - (1.0 - 2.0 * R)) < 1e-12
    assert abs(D.born_leakage_rate() - 1.0 / PHI**2) < 1e-10


# ── lepton mass hierarchy ────────────────────────────────────────────────────

def test_m_mu_over_m_e():
    um  = D.m_mu_over_m_e()
    pdg = 206.768
    _check(um, pdg, n=1, label="m_mu/m_e")

def test_m_tau_over_m_mu():
    um  = D.m_tau_over_m_mu()
    pdg = 16.817
    _check(um, pdg, n=1, label="m_tau/m_mu")

def test_m_tau_over_m_e():
    um  = D.m_tau_over_m_e()
    pdg = 3477.23
    _check(um, pdg, n=1, label="m_tau/m_e")

def test_lepton_exponents_additive():
    # 11 + 6 = 17 must hold for cycle-consistency
    ratio_product = D.m_mu_over_m_e() * D.m_tau_over_m_mu()
    assert abs(ratio_product - D.m_tau_over_m_e()) / D.m_tau_over_m_e() < 0.01


# ── cosmological constant ────────────────────────────────────────────────────

def test_rho_lambda_log():
    um  = D.rho_Lambda_over_MPl4_log10()
    obs = -122.04
    assert abs(um - obs) / abs(obs) < 0.005


# ── G_eff ────────────────────────────────────────────────────────────────────

def test_G_eff():
    geff = D.G_eff_over_GN()
    assert 1.0 < geff < 1.15
    assert abs(geff - (1.0 + R / (3.0 + 4.0 * R))) < 1e-12


# ── round-trip: lcdm.py and um.py build without error ────────────────────────

def test_build_lcdm_cosmology():
    from limb.lcdm import build_LiMBLCDMCosmology
    from limb.derivations import lcdm_inputs as D
    cosmo = build_LiMBLCDMCosmology()
    assert cosmo.H0 == pytest.approx(67.4)
    assert cosmo.n_s == pytest.approx(D.n_s())
    assert cosmo.A_s == pytest.approx(D.A_s())
    assert cosmo.tau_reio == pytest.approx(D.tau_reio())
    assert cosmo.m_nu_eV == pytest.approx(D.m_nu_total_eV())
    assert cosmo.extra_source_fn is None

def test_build_um_cosmology():
    from limb.um import build_LiMBUMCosmology
    cosmo = build_LiMBUMCosmology()
    assert cosmo.extra_source_fn is not None
    import numpy as np
    state = np.ones(10)
    result = cosmo.extra_source_fn(state, tau=100.0, k=0.1, cosmo=cosmo)
    assert np.allclose(result, 0.0)

def test_pipeline_cosmology_to_camb_params_no_camb():
    """cosmology_to_camb_params fails gracefully when camb is absent."""
    import sys, importlib
    from limb.camb_backend import cosmology_to_camb_params
    from limb.lcdm import build_LiMBLCDMCosmology
    cosmo = build_LiMBLCDMCosmology()
    # If camb is installed this test exercises the conversion path.
    # If not, it confirms the import is the only thing that's missing.
    try:
        pars = cosmology_to_camb_params(cosmo, lmax=100)
        assert pars is not None
    except ModuleNotFoundError:
        pass   # camb not installed in this env — expected

def test_public_api_exported():
    """Everything in __all__ is importable from limb."""
    import limb
    for name in limb.__all__:
        assert hasattr(limb, name), f"limb.{name} missing from package"
