"""
UM quark mass analysis.

Two results:
  1. phi^4 colour-cycle pattern — quark masses in log_phi space,
     residuals normalised by accumulated braiding floor n*eps_floor.
  2. u-d isospin splitting from EW channel structure:
     m_d/m_u = sqrt(W_B/W_M) = 1/sin(theta_W) = sqrt(2*sqrt(5)).
"""

import numpy as np

PHI = (1 + np.sqrt(5)) / 2
R   = 1 / (2 * PHI)
WL  = (1 - R)**2
WB  = 2 * R * (1 - R)
WM  = R**2
EPS = R**3

ME = 0.511  # electron mass MeV

def pct(pred, obs):
    return (pred - obs) / obs * 100

def nfloor_units(pred, obs, n):
    return abs(pct(pred, obs)) / (n * EPS * 100)

print(f"""
╔══════════════════════════════════════════════════════════════════════╗
║  UM QUARK SECTOR                                                      ║
║  φ²=φ+1  φ={PHI:.6f}  r={R:.6f}  ε={EPS:.5f}             ║
╚══════════════════════════════════════════════════════════════════════╝
""")

# ── Strong coupling ────────────────────────────────────────────────────────────
as_um  = R**2 * (1 + R - R**2)
as_pdg = 0.1179
print(f"α_s(M_Z) = r²(1+r-r²) = {as_um:.4f}   PDG {as_pdg:.4f}   "
      f"{pct(as_um,as_pdg):+.2f}%  ({abs(pct(as_um,as_pdg))/(EPS*100):.2f} ε_floor)")
print()

# ── phi^4 pattern ──────────────────────────────────────────────────────────────
print("─── φ⁴ colour-cycle pattern ──────────────────────────────────────────")
print(f"{'Quark':<5} {'m_q (MeV)':>10} {'m/m_e':>9} {'log_φ':>6} "
      f"{'n':>3} {'φⁿ':>8} {'bare err':>9} {'n·ε_fl':>7} {'floors':>7}")
print("─" * 75)

# PDG 2022 MS-bar masses in MeV
quarks = [('u', 2.16), ('d', 4.67), ('s', 93.4),
          ('c', 1270.), ('b', 4180.), ('t', 172690.)]

for q, mq in quarks:
    ratio   = mq / ME
    log_phi = np.log(ratio) / np.log(PHI)
    n       = round(log_phi / 4) * 4
    bare    = PHI**n
    err     = pct(bare, ratio)
    nfl     = n * EPS * 100
    floors  = abs(err) / nfl
    flag    = '✓' if floors < 2 else ('~' if floors < 5 else '!')
    print(f"{q:<5} {mq:>10.2f} {ratio:>9.1f} {log_phi:>6.2f} "
          f"{n:>3} {bare:>8.0f} {err:>+8.1f}% {nfl:>6.1f}% {floors:>6.2f} {flag}")

print()

# ── u-d isospin splitting ──────────────────────────────────────────────────────
print("─── u–d isospin splitting from EW channel structure ──────────────────")
print()
print("  T3=+½ (u): couples via matter channel W_M → y_u ∝ W_M^½")
print("  T3=−½ (d): couples via boundary channel W_B → y_d ∝ W_B^½")
print("  m = y·v/√2  →  m_d/m_u = sqrt(W_B/W_M)")
print()

rho    = np.sqrt(WB / WM)          # = 1/sin(theta_W) = sqrt(2*sqrt(5))
sw2    = R / (2 * (1 - R))         # Weinberg angle from Paper 4
rho_sw = 1 / np.sqrt(sw2)
rho_exact = np.sqrt(2 * np.sqrt(5))

print(f"  sqrt(W_B/W_M)   = {rho:.5f}")
print(f"  1/sin(θ_W)      = {rho_sw:.5f}   (consistent ✓)")
print(f"  sqrt(2√5)       = {rho_exact:.5f}   (closed form ✓)")
print()

ratio_pdg = 4.67 / 2.16
print(f"  UM  m_d/m_u = {rho:.5f}")
print(f"  PDG m_d/m_u = {ratio_pdg:.5f}")
print(f"  Error: {pct(rho, ratio_pdg):+.2f}%  ({abs(pct(rho,ratio_pdg))/(EPS*100):.2f} ε_floor)")
print()

# isospin-symmetric bare mass
m0   = PHI**4 * ME
mean_pdg = (2.16 + 4.67) / 2
print(f"  Bare isospin average φ⁴·mₑ = {m0:.4f} MeV")
print(f"  PDG arithmetic mean (m_u+m_d)/2 = {mean_pdg:.4f} MeV")
print(f"  Error: {pct(m0,mean_pdg):+.2f}%  ({abs(pct(m0,mean_pdg))/(EPS*100):.2f} ε_floor)")
print()

m_u = 2 * m0 / (1 + rho)
m_d = 2 * m0 * rho / (1 + rho)
for label, um, obs, n in [('m_u', m_u, 2.16, 4), ('m_d', m_d, 4.67, 4)]:
    err  = pct(um, obs)
    fl   = nfloor_units(um, obs, n)
    print(f"  UM {label} = {um:.3f} MeV   PDG {obs:.2f} MeV   "
          f"{err:+.1f}%  ({fl:.2f} n·ε_floor) ✓")

print()

# ── Strange quark note ─────────────────────────────────────────────────────────
print("─── Strange quark ────────────────────────────────────────────────────")
s_bare = PHI**12 * ME
print(f"  φ¹²·mₑ = {s_bare:.1f} MeV   PDG 93.4 MeV")
print(f"  Error: {pct(s_bare, 93.4):+.1f}%  ({nfloor_units(s_bare,93.4,12):.2f} n·ε_floor, n=12)")
print(f"  PDG uncertainty ±11 MeV (~12%) — residual just outside n·ε_floor.")
print(f"  Closure requires QCD running from string scale. Next calculation.")
print()

# ── Summary ────────────────────────────────────────────────────────────────────
print("═" * 75)
print("  SUMMARY")
print("═" * 75)
rows = [
    ("m_d/m_u",  rho,   2.162,   1,  "sqrt(W_B/W_M)"),
    ("m_u",      m_u,   2.16,    4,  "2φ⁴mₑ/(1+ρ)"),
    ("m_d",      m_d,   4.67,    4,  "2φ⁴mₑρ/(1+ρ)"),
    ("m_s/mₑ",   s_bare/ME, 182.8, 12, "φ¹² (bare)"),
    ("m_c/mₑ",   PHI**16, 2485., 16, "φ¹⁶ (bare)"),
    ("m_b/mₑ",   PHI**20, 8180., 20, "φ²⁰ (bare)"),
    ("m_t/mₑ",   PHI**28, 337945., 28, "φ²⁸ (bare)"),
    ("α_s(M_Z)", as_um, 0.1179,  1,  "r²(1+r−r²)"),
]
print(f"  {'Observable':<12} {'Expression':<20} {'UM':>10} {'PDG':>10} "
      f"{'Error':>8} {'n·ε units':>10}")
print("  " + "─" * 73)
for label, um, obs, n, expr in rows:
    err = pct(um, obs)
    fl  = abs(err) / (n * EPS * 100)
    flag = '✓' if fl < 2 else ('~' if fl < 5 else '!')
    print(f"  {label:<12} {expr:<20} {um:>10.4g} {obs:>10.4g} "
          f"{err:>+7.1f}% {fl:>8.2f}  {flag}")
print()
print(f"  ε_floor = r³ = {EPS:.5f} ({EPS*100:.3f}%)")
print(f"  ρ = sqrt(W_B/W_M) = sqrt(2√5) = {rho:.5f}")
