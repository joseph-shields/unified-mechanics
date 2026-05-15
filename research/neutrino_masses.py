"""
neutrino_masses.py
Unified Mechanics — Neutrino Mass Hierarchy
Joseph Shields, 2026

Derives the atmospheric and solar neutrino mass scales from the UM axiom
c^2 = c + 1, using only r = 1/(2*phi) and m_e = 0.511 MeV.
No free parameters.
"""

import math

# ── Fundamental UM constants ──────────────────────────────────────────────────
PHI = (1 + math.sqrt(5)) / 2        # golden ratio
R   = 1 / (2 * PHI)                 # contraction rate r ≈ 0.30902
EPS = R**3                           # braiding floor ε_floor ≈ 0.02951

W_L = (1 - R)**2                    # longitudinal weight ≈ 0.4775
W_B = 2 * R * (1 - R)              # boundary weight    ≈ 0.4271
W_M = R**2                          # matter weight      ≈ 0.0955

print("=" * 65)
print("  Unified Mechanics — Neutrino Mass Hierarchy")
print("=" * 65)
print(f"  phi           = {PHI:.6f}")
print(f"  r             = {R:.6f}")
print(f"  eps_floor     = {EPS:.5f}")
print(f"  W_L           = {W_L:.5f}")
print(f"  W_B           = {W_B:.5f}")
print(f"  W_M           = {W_M:.5f}")
print()

# ── Reference: electron mass ──────────────────────────────────────────────────
m_e_eV = 0.511e6   # electron mass in eV

# Weak-force boundary correction (neutrinos couple to W_B weakly)
boundary_corr = 1 + R           # = 1.30902

print(f"  m_e           = {m_e_eV:.3e} eV")
print(f"  (1 + r)       = {boundary_corr:.5f}   [weak vertex correction]")
print()

# ── phi powers ───────────────────────────────────────────────────────────────
phi34 = PHI**34
phi38 = PHI**38
phi4  = PHI**4

print(f"  phi^4         = {phi4:.4f}")
print(f"  phi^34        = {phi34:.3e}")
print(f"  phi^38        = {phi38:.3e}")
print()

# ── m_nu3 : atmospheric mass scale ───────────────────────────────────────────
# Cycle depth n=34 because 34 = 2 × 17 (17 = 11 + 6, total charged-lepton depth)
m_nu3_eV = m_e_eV * boundary_corr / phi34

obs_atm_eV = 50e-3   # sqrt(Delta m^2_atm) ≈ 50 meV (normal hierarchy, PDG)
resid_nu3  = (m_nu3_eV - obs_atm_eV) / obs_atm_eV * 100
eps_units_nu3 = resid_nu3 / 100 / EPS

print("-" * 65)
print("  m_nu3  (atmospheric scale)  n = 34")
print(f"    UM:   m_nu3 = m_e * (1+r) / phi^34")
print(f"         = {m_e_eV:.3e} * {boundary_corr:.5f} / {phi34:.3e}")
print(f"         = {m_nu3_eV*1e3:.4f} meV")
print(f"    Obs:  sqrt(Delta m^2_atm) ~ {obs_atm_eV*1e3:.1f} meV  (PDG 2022)")
print(f"    Residual: {resid_nu3:+.2f}%  =  {eps_units_nu3:+.2f} eps_floor")
print()

# ── m_nu2 : solar mass scale ──────────────────────────────────────────────────
# Cycle depth n=38; generation step is phi^4 => 38 = 34 + 4
m_nu2_eV = m_e_eV * boundary_corr / phi38

obs_sol_eV = 8.6e-3   # sqrt(Delta m^2_sol) ≈ 8.6 meV (PDG 2022)
resid_nu2  = (m_nu2_eV - obs_sol_eV) / obs_sol_eV * 100
eps_units_nu2 = resid_nu2 / 100 / EPS

print("-" * 65)
print("  m_nu2  (solar scale)  n = 38")
print(f"    UM:   m_nu2 = m_e * (1+r) / phi^38")
print(f"         = {m_e_eV:.3e} * {boundary_corr:.5f} / {phi38:.3e}")
print(f"         = {m_nu2_eV*1e3:.4f} meV")
print(f"    Obs:  sqrt(Delta m^2_sol) ~ {obs_sol_eV*1e3:.1f} meV  (PDG 2022)")
print(f"    Residual: {resid_nu2:+.2f}%  =  {eps_units_nu2:+.2f} eps_floor")
print()

# ── Mass ratio m_nu3 / m_nu2 ──────────────────────────────────────────────────
ratio_um  = m_nu3_eV / m_nu2_eV        # = phi^4 exactly
ratio_obs = obs_atm_eV / obs_sol_eV    # proxy (mass eigenstate proxy)
resid_ratio = (ratio_um - ratio_obs) / ratio_obs * 100

print("-" * 65)
print("  Mass ratio  m_nu3 / m_nu2 = phi^4  (EXACT in UM)")
print(f"    UM:    phi^4 = {phi4:.4f}")
print(f"    Proxy: sqrt(dm2_atm)/sqrt(dm2_sol) = {ratio_obs:.4f}")
print(f"    Residual: {resid_ratio:+.1f}%   [proxy depends on m_nu1 assumption]")
print()

# ── Normal hierarchy: m_nu1 ≈ 0 ──────────────────────────────────────────────
# In normal hierarchy m_nu1 << m_nu2 << m_nu3
m_nu1_eV = 0.0   # lightest state ~ 0 in UM normal hierarchy

# Check consistency with oscillation parameters
dm2_atm_um = m_nu3_eV**2 - m_nu1_eV**2
dm2_sol_um = m_nu2_eV**2 - m_nu1_eV**2

print("-" * 65)
print("  Oscillation parameters from UM masses")
print(f"    Delta m^2_atm (UM) = m_nu3^2 - m_nu1^2")
print(f"                       = {dm2_atm_um:.4e} eV^2")
print(f"    Observed:            ~2.5e-3 eV^2  (PDG 2022)")
print()
print(f"    Delta m^2_sol (UM) = m_nu2^2 - m_nu1^2")
print(f"                       = {dm2_sol_um:.4e} eV^2")
print(f"    Observed:            ~7.4e-5 eV^2  (PDG 2022)")
print()

# ── Sum of masses / cosmological bound ───────────────────────────────────────
sum_mv = m_nu1_eV + m_nu2_eV + m_nu3_eV
planck_bound = 120e-3   # Planck 2018: Sigma m_nu < 120 meV

print("-" * 65)
print("  Cosmological sum")
print(f"    Sigma m_nu (UM) = m_nu1 + m_nu2 + m_nu3")
print(f"                    = {m_nu1_eV*1e3:.2f} + {m_nu2_eV*1e3:.3f} + {m_nu3_eV*1e3:.3f}  meV")
print(f"                    = {sum_mv*1e3:.2f} meV")
print(f"    Planck 2018 bound: < {planck_bound*1e3:.0f} meV")
print(f"    Status: {'WITHIN BOUND' if sum_mv < planck_bound else 'EXCEEDS BOUND'}")
print()

# ── Summary table ─────────────────────────────────────────────────────────────
print("=" * 65)
print("  SUMMARY TABLE")
print("=" * 65)
print(f"  {'Observable':<22} {'UM':>12} {'Observed':>12} {'Residual':>10}")
print("-" * 65)
print(f"  {'m_nu3 (meV)':<22} {m_nu3_eV*1e3:>12.3f} {obs_atm_eV*1e3:>12.1f} {resid_nu3:>+9.1f}%")
print(f"  {'m_nu2 (meV)':<22} {m_nu2_eV*1e3:>12.4f} {obs_sol_eV*1e3:>12.1f} {resid_nu2:>+9.1f}%")
print(f"  {'m_nu3/m_nu2':<22} {ratio_um:>12.4f} {ratio_obs:>12.4f} {resid_ratio:>+9.1f}%")
print(f"  {'Sigma m_nu (meV)':<22} {sum_mv*1e3:>12.2f} {'<120':>12} {'within':>10}")
print("=" * 65)
print()
print("  All results from c^2 = c + 1.  Zero free parameters.")
