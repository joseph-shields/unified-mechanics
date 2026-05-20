"""
gauge_unification.py
Unified Mechanics — Gauge Coupling Unification
=============================================
Derives all three SM gauge couplings at M_Z from the single axiom φ² = φ + 1,
runs them with SM 1-loop beta functions, locates pairwise intersections, and
compares the UM-natural GUT scale M_Pl * phi^{-14} to the intersection band.

Zero free parameters are adjusted; every number follows from r = 1/(2*phi).
"""

import math

# ── Axiom and fundamental constants ──────────────────────────────────────────
phi   = (1 + math.sqrt(5)) / 2          # golden ratio
r     = 1 / (2 * phi)                   # contraction rate  ≈ 0.30902
r2    = r**2
r3    = r**3

W_L   = (1 - r)**2                      # longitudinal channel weight
W_B   = 2 * r * (1 - r)                # boundary channel weight
W_M   = r**2                            # matter channel weight
eps   = r**3                            # braiding floor

M_Z   = 91.1876                         # GeV
M_Pl  = 1.220910e19                     # GeV  (reduced Planck mass × sqrt(8pi))

print("=" * 65)
print("  Unified Mechanics — Gauge Coupling Unification")
print("=" * 65)
print(f"\n  phi   = {phi:.8f}")
print(f"  r     = {r:.8f}   (= 1/(2*phi))")
print(f"  W_L   = {W_L:.6f}")
print(f"  W_B   = {W_B:.6f}")
print(f"  W_M   = {W_M:.6f}")
print(f"  eps   = {eps:.6f}   (braiding floor = r^3)")

# ── UM-derived couplings at M_Z ───────────────────────────────────────────────
# Fine structure constant
inv_alpha_fib = phi**10 + phi**5 + phi**2 + phi**(-2)
alpha_em = 1.0 / inv_alpha_fib

# Weinberg angle
sin2_theta_W = r / (2 * (1 - r))

# SU(2) coupling
alpha_2 = alpha_em / sin2_theta_W

# U(1)_Y coupling (before GUT normalisation)
alpha_Y = alpha_em / (1 - sin2_theta_W)

# GUT-normalised U(1): alpha_1 = (5/3) * alpha_Y
alpha_1 = (5.0 / 3.0) * alpha_Y

# Strong coupling
alpha_3 = r2 * (1 + r - r2)

# Inverse couplings at M_Z
inv1 = 1.0 / alpha_1
inv2 = 1.0 / alpha_2
inv3 = 1.0 / alpha_3

print("\n── Couplings at M_Z = {:.4f} GeV ──────────────────────────────".format(M_Z))
print(f"\n  1/alpha_em  = phi^10+phi^5+phi^2+phi^-2 = {inv_alpha_fib:.4f}")
print(f"               observed: 137.036   residual: {100*(inv_alpha_fib/137.036 - 1):+.3f}%")
print(f"  sin^2(th_W) = r/(2(1-r))                 = {sin2_theta_W:.6f}")
print(f"               observed: 0.22290   residual: {100*(sin2_theta_W/0.22290 - 1):+.3f}%")
print(f"  alpha_2     = alpha_em / sin^2(th_W)      = {alpha_2:.6f}")
print(f"  alpha_Y     = alpha_em / (1-sin^2(th_W))  = {alpha_Y:.6f}")
print(f"  alpha_1     = (5/3)*alpha_Y               = {alpha_1:.6f}  (GUT-normalised)")
print(f"  alpha_3     = r^2*(1+r-r^2)               = {alpha_3:.6f}")
print(f"               observed: 0.11790   residual: {100*(alpha_3/0.11790 - 1):+.3f}%")
print(f"\n  Inverse couplings at M_Z:")
print(f"  1/alpha_1 = {inv1:.4f}   (GUT-normalised U(1))")
print(f"  1/alpha_2 = {inv2:.4f}   (SU(2)_L)")
print(f"  1/alpha_3 = {inv3:.4f}   (SU(3)_c)")

# ── SM 1-loop beta coefficients ───────────────────────────────────────────────
# 1/alpha_i(mu) = 1/alpha_i(M_Z) - (b_i / 2pi) * ln(mu / M_Z)
b1 = 41.0 / 10.0    # +4.1   U(1) — grows with energy
b2 = -19.0 / 6.0    # -3.167 SU(2)_L
b3 = -7.0           # SU(3)_c

two_pi = 2 * math.pi

def inv_alpha_run(inv_alpha_MZ, b, log_ratio):
    """1-loop running: 1/alpha(mu) = 1/alpha(M_Z) - (b/2pi)*log(mu/M_Z)."""
    return inv_alpha_MZ - (b / two_pi) * log_ratio

# ── Pairwise intersections ────────────────────────────────────────────────────
# Set inv_alpha_i = inv_alpha_j, solve for log(mu/M_Z):
# inv1 - (b1/2pi)*x = inv2 - (b2/2pi)*x
# (b2-b1)/2pi * x = inv2 - inv1
# x = 2pi*(inv2-inv1) / (b2-b1)

def intersection(inv_i, b_i, inv_j, b_j):
    """Return (log_ratio, mu_GeV, inv_alpha_at_intersection)."""
    denom = b_j - b_i
    if abs(denom) < 1e-12:
        return None, None, None
    log_ratio = two_pi * (inv_j - inv_i) / denom
    mu = M_Z * math.exp(log_ratio)
    inv_at = inv_i - (b_i / two_pi) * log_ratio
    return log_ratio, mu, inv_at

print("\n── 1-loop Running — Pairwise Intersections ─────────────────────")

pairs = [
    ("alpha_1", inv1, b1, "alpha_2", inv2, b2),
    ("alpha_1", inv1, b1, "alpha_3", inv3, b3),
    ("alpha_2", inv2, b2, "alpha_3", inv3, b3),
]

intersection_results = {}
for (name_i, invi, bi, name_j, invj, bj) in pairs:
    lr, mu, inv_x = intersection(invi, bi, invj, bj)
    # Also evaluate the third coupling there
    names_all = {"alpha_1": (inv1, b1), "alpha_2": (inv2, b2), "alpha_3": (inv3, b3)}
    key = f"{name_i}∩{name_j}"
    intersection_results[key] = (mu, inv_x, lr)
    third_name = [n for n in ["alpha_1", "alpha_2", "alpha_3"] if n not in [name_i, name_j]][0]
    inv3rd_val, b3rd = names_all[third_name]
    inv_third_at_mu = inv_alpha_run(inv3rd_val, b3rd, lr)
    print(f"\n  {name_i} ∩ {name_j}:")
    print(f"    mu      = {mu:.4e} GeV")
    print(f"    1/alpha = {inv_x:.3f}")
    print(f"    {third_name} there: 1/alpha = {inv_third_at_mu:.3f}  "
          f"(separation = {abs(inv_x - inv_third_at_mu):.2f})")

# ── UM-predicted GUT scale ────────────────────────────────────────────────────
print("\n── UM GUT Scale ─────────────────────────────────────────────────")

phi14 = phi**14
phi13 = phi**13
M_GUT_14 = M_Pl / phi14
M_GUT_13 = M_Pl / phi13

print(f"\n  phi^14         = {phi14:.2f}")
print(f"  M_Pl*phi^-14   = {M_GUT_14:.4e} GeV  (primary)")
print(f"  phi^13         = {phi13:.2f}")
print(f"  M_Pl*phi^-13   = {M_GUT_13:.4e} GeV  (secondary)")
print(f"\n  MSSM/GUT scale ~ 2e16 GeV")

# Evaluate all three couplings at M_GUT_14
log_gut14 = math.log(M_GUT_14 / M_Z)
inv1_gut = inv_alpha_run(inv1, b1, log_gut14)
inv2_gut = inv_alpha_run(inv2, b2, log_gut14)
inv3_gut = inv_alpha_run(inv3, b3, log_gut14)

print(f"\n  At M_GUT = M_Pl*phi^-14 = {M_GUT_14:.3e} GeV:")
print(f"    1/alpha_1 = {inv1_gut:.3f}")
print(f"    1/alpha_2 = {inv2_gut:.3f}")
print(f"    1/alpha_3 = {inv3_gut:.3f}")
print(f"    Spread (max-min) = {max(inv1_gut,inv2_gut,inv3_gut)-min(inv1_gut,inv2_gut,inv3_gut):.3f}")

# ── Running table ─────────────────────────────────────────────────────────────
print("\n── Running Table: 1/alpha_i vs log10(mu/GeV) ───────────────────")
print(f"\n  {'log10(mu)':>10}  {'mu [GeV]':>12}  {'1/a1':>8}  {'1/a2':>8}  {'1/a3':>8}")
print("  " + "-"*56)

scales_log10 = [2, 4, 6, 8, 10, 12, 14, 15, 16, 17, 18, 19]
for l10 in scales_log10:
    mu_val = 10**l10
    lr_val = math.log(mu_val / M_Z)
    i1 = inv_alpha_run(inv1, b1, lr_val)
    i2 = inv_alpha_run(inv2, b2, lr_val)
    i3 = inv_alpha_run(inv3, b3, lr_val)
    marker = ""
    if abs(l10 - math.log10(M_GUT_14)) < 0.6:
        marker = "  <-- UM GUT"
    print(f"  {l10:>10}  {mu_val:>12.2e}  {i1:>8.3f}  {i2:>8.3f}  {i3:>8.3f}{marker}")

# ── Summary ───────────────────────────────────────────────────────────────────
print("\n── Summary ──────────────────────────────────────────────────────")
print("""
  UM derives all three SM gauge couplings at M_Z from r = 1/(2*phi):
    alpha_em  via phi Fibonacci cycle sums
    sin^2(W)  via W_M/W_B = r/(2(1-r))
    alpha_3   via r^2*(1+r-r^2)

  SM 1-loop running does NOT produce perfect unification (known).
  The three pairwise intersections span 10^14 -- 10^17 GeV.
  The UM-natural scale M_Pl * phi^{-14} = 1.45e16 GeV sits within
  this band, consistent with MSSM unification at ~2e16 GeV.

  Full unification requires SUSY threshold corrections or the
  second E_8 sector of the heterotic companion paper.
""")
