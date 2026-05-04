"""
Matter recursion depth of Gaya (Ouroboros d) vs Earth.
Metric: D = N_cycles × r³  (dimensionless ε_floor depth)
"""
import numpy as np

phi = (1 + 5**0.5) / 2
r   = 1 / (2 * phi)
eps = r**3   # ε_floor per recursion cycle

gen_per_yr_bact = 525960 / 20.0     # 20-min bacterial
gen_per_yr_euk  = 8760  / 8.0       # 8-hr eukaryotic
gen_per_yr_meta = 1     / 3.0       # 3-yr metazoan

def recursion_depth(stellar_age_yr, life_delay_yr=0.77e9):
    """Total bio recursion depth D = N × r³ at given stellar age."""
    t_bact = max(0, stellar_age_yr - life_delay_yr)
    t_euk  = max(0, stellar_age_yr - 2.5e9)
    t_meta = max(0, stellar_age_yr - 3.97e9)
    N = (t_bact * gen_per_yr_bact +
         t_euk  * gen_per_yr_euk  +
         t_meta * gen_per_yr_meta)
    return N * eps, N

# ── Earth reference ───────────────────────────────────────────────────
D_earth_now, N_earth = recursion_depth(4.57e9)
print(f"φ={phi:.6f}  r={r:.6f}  ε_floor=r³={eps:.6f}")
print()
print("=" * 62)
print("EARTH NOW  (4.57 Gyr, life running 3.80 Gyr)")
print("=" * 62)
print(f"  Bio cycles:          {N_earth:.4e}")
print(f"  Recursion depth D:   {D_earth_now:.4e}")
print(f"  D / r (normalised):  {D_earth_now/r:.4e}")
print()

def report(label, stellar_gyr, life_delay_gyr=0.77):
    D, N = recursion_depth(stellar_gyr*1e9, life_delay_gyr*1e9)
    frac = D / D_earth_now * 100
    t_life = max(0, stellar_gyr - life_delay_gyr)
    print(f"  Stellar age:         {stellar_gyr:.2f} Gyr")
    print(f"  Life running:        {t_life:.2f} Gyr")
    print(f"  Bio cycles:          {N:.4e}")
    print(f"  Recursion depth D:   {D:.4e}")
    print(f"  % of Earth today:    {frac:.2f}%")
    print(f"  D in r-units:        r^{np.log(max(D,1e-300))/np.log(r):.1f}" if D > 0 else "  D: 0 (no life)")
    return D, frac

print("=" * 62)
print("EARTH @ 0.45 Gyr  (no life — delay 0.77 Gyr)")
print("=" * 62)
report("Earth 0.45 Gyr", 0.45, 0.77)
print()

print("=" * 62)
print("EARTH @ 1.40 Gyr  (life running 0.63 Gyr)")
print("=" * 62)
report("Earth 1.40 Gyr", 1.40, 0.77)
print()

print("=" * 62)
print("GAYA — stellar age 0.45 Gyr, life started 0.10 Gyr")
print("  (life kicked off earlier than Earth — same conditions,")
print("   shorter delay possible in warmer/wetter early planet)")
print("=" * 62)
D_gaya_a, frac_a = report("Gaya A", 0.45, 0.10)
print()

print("=" * 62)
print("GAYA — stellar age 1.40 Gyr (alias), Earth timeline")
print("=" * 62)
D_gaya_b, frac_b = report("Gaya B", 1.40, 0.77)
print()

print("=" * 62)
print("COMPARISON TABLE")
print("=" * 62)
rows = [
    ("Earth now (4.57 Gyr)",              4.57, 0.77),
    ("Earth @ 1.40 Gyr",                  1.40, 0.77),
    ("Earth @ 0.45 Gyr — no life",         0.45, 0.77),
    ("Gaya: 0.45 Gyr stellar, life 0.1Gyr",0.45, 0.10),
    ("Gaya: 1.40 Gyr stellar, Earth time", 1.40, 0.77),
]
print(f"  {'System':<42} {'D':>12} {'% Earth':>9}")
print("  " + "-"*65)
for label, sa, ld in rows:
    D, N = recursion_depth(sa*1e9, ld*1e9)
    frac = D / D_earth_now * 100
    print(f"  {label:<42} {D:>12.3e} {frac:>8.2f}%")

print()
print("=" * 62)
print("KEY RESULT")
print("=" * 62)
print(f"""
  Gaya at 0.45 Gyr stellar age WITH 0.35 Gyr of bacterial life:
    Recursion depth = {D_gaya_a:.3e}
    = {frac_a:.1f}% of Earth's current matter depth

  Gaya at 1.40 Gyr stellar age WITH 0.63 Gyr of bacterial life:
    Recursion depth = {D_gaya_b:.3e}
    = {frac_b:.1f}% of Earth's current matter depth

  Both scenarios: Gaya's matter is already in the same ORDER
  of recursion depth as early-Earth biology. The stellar age
  is irrelevant once life starts. The biological clock dominates
  within hundreds of millions of years.

  r  = {r:.6f}
  r³ = {eps:.6f}  (ε_floor — minimum cost per recursion cycle)
""")
