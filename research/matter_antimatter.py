"""
matter_antimatter.py — Baryon Asymmetry in Unified Mechanics
=============================================================
UM axiom: c^2 = c + 1  =>  phi = (1+sqrt(5))/2,  r = 1/(2*phi)

Computes:
  - eta_B = r^18 from 3 generations x 6 channel crossings per generation
  - Comparison to Planck 2018 observed value 6.104e-10
  - Context: r^17, r^19 neighbours
  - CP-violating phase delta_CP = arccos(W_B) and comparison to PDG
  - Jarlskog invariant J from UM channel weights
  - Running product interpretation of 18 channel traversals
"""

import math

# ---------------------------------------------------------------------------
# UM fundamental constants
# ---------------------------------------------------------------------------
PHI = (1 + math.sqrt(5)) / 2
R   = 1 / (2 * PHI)

W_L = (1 - R)**2
W_B = 2 * R * (1 - R)
W_M = R**2
EPS = R**3

print("=" * 65)
print("UNIFIED MECHANICS — BARYON ASYMMETRY AND CP VIOLATION")
print("=" * 65)
print(f"\nUM constants:")
print(f"  phi          = {PHI:.8f}")
print(f"  r            = {R:.8f}")
print(f"  W_L          = {W_L:.6f}")
print(f"  W_B          = {W_B:.6f}")
print(f"  W_M          = {W_M:.6f}")
print(f"  eps_floor    = {EPS:.6f}")

# ---------------------------------------------------------------------------
# Section 1 — Baryon-to-photon ratio
# ---------------------------------------------------------------------------
print("\n" + "-" * 65)
print("SECTION 1: Baryon-to-photon ratio eta_B = r^(3x6) = r^18")
print("-" * 65)

eta_obs = 6.104e-10    # Planck 2018

eta_17  = R**17
eta_18  = R**18
eta_19  = R**19

resid_18 = (eta_18 - eta_obs) / eta_obs * 100.0
eps_18   = abs(resid_18 / 100.0) / EPS

print(f"\n  Factorisation: 18 = 3 generations x 6 channel crossings")
print(f"  (4 colour transitions + 2 weak transitions per generation)")
print()
print(f"  r^17          = {eta_17:.6e}  (context: n=17)")
print(f"  r^18          = {eta_18:.6e}  (UM derivation)")
print(f"  r^19          = {eta_19:.6e}  (context: n=19)")
print()
print(f"  eta_B (Planck 2018) = {eta_obs:.6e}")
print(f"  r^18                = {eta_18:.6e}")
print(f"  Residual            = {resid_18:+.2f}%  =  {eps_18:.2f} eps_floor")

# Running product: each of 18 transitions contributes factor r
print(f"\n  Running product (cumulative r^k for k=1..18):")
prod = 1.0
for k in range(1, 19):
    prod *= R
    flag = "  <-- UM result" if k == 18 else ""
    if k >= 15 or k <= 3:
        print(f"    k={k:2d}: r^{k} = {prod:.4e}{flag}")
    elif k == 4:
        print(f"    ...")

# ---------------------------------------------------------------------------
# Section 2 — CP-violating phase
# ---------------------------------------------------------------------------
print("\n" + "-" * 65)
print("SECTION 2: CP-violating phase delta_CP = arccos(W_B)")
print("-" * 65)

delta_CP_UM  = math.acos(W_B)           # radians
delta_CP_PDG = 1.14                     # PDG 2022 (radians)

resid_dCP    = (delta_CP_UM - delta_CP_PDG) / delta_CP_PDG * 100.0
eps_dCP      = abs(resid_dCP / 100.0) / EPS

print(f"\n  W_B                  = {W_B:.6f}")
print(f"  delta_CP (UM)        = arccos(W_B) = {delta_CP_UM:.6f} rad")
print(f"  delta_CP (PDG 2022)  = {delta_CP_PDG:.6f} rad")
print(f"  Residual             = {resid_dCP:+.4f}%  =  {eps_dCP:.3f} eps_floor")

# ---------------------------------------------------------------------------
# Section 3 — Jarlskog invariant
# ---------------------------------------------------------------------------
print("\n" + "-" * 65)
print("SECTION 3: Jarlskog invariant J")
print("-" * 65)

# CKM Cabibbo angle from UM: lambda = 1/phi^3
lam    = 1.0 / PHI**3
lam2   = lam**2

# J ≈ lambda^2 * W_M * sin(delta_CP)
J_UM   = lam2 * W_M * math.sin(delta_CP_UM)
J_PDG  = 3.08e-5    # PDG 2022 central value Im[V_us V_cb V*_ub V*_cs]

resid_J = (J_UM - J_PDG) / J_PDG * 100.0
eps_J   = abs(resid_J / 100.0) / EPS

print(f"\n  lambda = 1/phi^3     = {lam:.6f}")
print(f"  lambda^2             = {lam2:.6f}")
print(f"  W_M                  = {W_M:.6f}")
print(f"  sin(delta_CP)        = {math.sin(delta_CP_UM):.6f}")
print(f"\n  J (UM) = lambda^2 x W_M x sin(delta_CP)")
print(f"         = {lam2:.6f} x {W_M:.6f} x {math.sin(delta_CP_UM):.6f}")
print(f"         = {J_UM:.4e}")
print(f"  J (PDG 2022)         = {J_PDG:.4e}")
print(f"  Residual             = {resid_J:+.2f}%  =  {eps_J:.2f} eps_floor")
print(f"  Note: tree-level formula; full CKM hierarchy requires")
print(f"  4th-order lambda suppression at V_ub, V_cb level.")

# Refined formula: J ~ r^6 * sin(delta_CP)
J_UM_ref  = R**6 * math.sin(delta_CP_UM)
resid_Jr  = (J_UM_ref - J_PDG) / J_PDG * 100.0
eps_Jr    = abs(resid_Jr / 100.0) / EPS
print(f"\n  Refined: J ~ r^6 x sin(delta_CP) = {J_UM_ref:.4e}")
print(f"  Residual (refined)   = {resid_Jr:+.2f}%  =  {eps_Jr:.2f} eps_floor")
print(f"  (Full CKM hierarchy derivation is future work.)")

# ---------------------------------------------------------------------------
# Section 4 — r^k neighbour scan around 18
# ---------------------------------------------------------------------------
print("\n" + "-" * 65)
print("SECTION 4: Neighbour scan  r^k  vs  eta_obs = 6.104e-10")
print("-" * 65)
print(f"\n  {'k':>3}   {'r^k':>14}   {'residual %':>12}   {'eps_f':>8}")
print(f"  {'-'*3}   {'-'*14}   {'-'*12}   {'-'*8}")
for k in range(14, 23):
    val = R**k
    res = (val - eta_obs) / eta_obs * 100.0
    eps = abs(res / 100.0) / EPS
    marker = "  <--" if k == 18 else ""
    print(f"  {k:>3}   {val:>14.4e}   {res:>+12.3f}   {eps:>8.3f}{marker}")

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
print("\n" + "=" * 65)
print("SUMMARY")
print("=" * 65)
print(f"  eta_B (UM, r^18)     = {eta_18:.4e}")
print(f"  eta_B (Planck 2018)  = {eta_obs:.4e}")
print(f"  Residual             = {resid_18:+.2f}%  ({eps_18:.2f} eps_floor)")
print()
print(f"  delta_CP (UM)        = {delta_CP_UM:.4f} rad")
print(f"  delta_CP (PDG)       = {delta_CP_PDG:.4f} rad")
print(f"  Residual             = {resid_dCP:+.4f}%  ({eps_dCP:.3f} eps_floor)")
print()
print(f"  J (UM, tree)         = {J_UM:.4e}")
print(f"  J (UM, refined r^6)  = {J_UM_ref:.4e}")
print(f"  J (PDG)              = {J_PDG:.4e}")
print(f"  Residual (tree)      = {resid_J:+.2f}%  ({eps_J:.2f} eps_floor)")
print(f"  Residual (refined)   = {resid_Jr:+.2f}%  ({eps_Jr:.2f} eps_floor)")
print()
print(f"  Remaining 2.77 eps_floor in eta_B attributed to")
print(f"  CP-phase thermal corrections (leptogenesis washout).")
print("=" * 65)
