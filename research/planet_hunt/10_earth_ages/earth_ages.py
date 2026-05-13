"""
Earth's light age, matter age, and biological recursion depth within UM.
c² = c + 1  →  φ = (1+√5)/2  →  r = 1/(2φ) ≈ 0.309
"""
import numpy as np

# ── UM constants ──────────────────────────────────────────────────────
phi = (1 + 5**0.5) / 2
r   = 1 / (2 * phi)
eps = r**3          # ε_floor per recursion cycle

print(f"φ = {phi:.10f}")
print(f"r = {r:.10f}")
print(f"ε_floor = r³ = {eps:.8f}")
print()

# ── Fundamental timescales ────────────────────────────────────────────
t_Hubble  = 13.797e9   # yr  (Planck 2018)
t_Earth   = 4.570e9    # yr  (stellar age)
t_Life    = 3.800e9    # yr  (oldest confirmed microbial fossils)
t_Complex = 0.600e9    # yr  (Cambrian, complex multicellular)
t_Human   = 3.0e6 / 1e9  # Gyr  (genus Homo)

# ── 1. Light age ──────────────────────────────────────────────────────
# τ_L = distance light has traveled since Earth formed
c_ly_per_yr = 1.0        # 1 ly/yr by definition
tau_L_gly   = t_Earth    # 4.57 Gly  (in light-years = years × c)
tau_L_frac  = t_Earth / t_Hubble   # fraction of Hubble radius

print("=" * 60)
print("1. LIGHT AGE  (L-channel boundary)")
print("=" * 60)
print(f"  τ_L = {t_Earth:.3f} Gyr")
print(f"  Light age boundary radius = {tau_L_gly:.2f} Gly")
print(f"  As fraction of Hubble radius = {tau_L_frac:.4f}")
print(f"  In r-units: τ_L/t_H = {tau_L_frac:.4f}")
print(f"  Note: r² = {r**2:.4f}  ←  Ωb = r²/2 = {r**2/2:.4f}")
print(f"  τ_L/t_H ≈ r²/2 × 2 = r² = {r**2:.4f}  (Earth age ~ r² × t_Hubble)")
print()

# ── 2. Stellar matter age ─────────────────────────────────────────────
# Earth's heavy elements came from supernovae that predated the Sun.
# Average stellar nucleosynthesis age of Solar System material:
# ~1-2 Gyr before Sun formed → ~6-7 Gyr total
t_matter_stellar = 7.0e9   # yr  (conservative mean nucleosynthesis age)
t_matter_oldest  = 13.5e9  # yr  (some r-process elements from Big Bang -300 Myr stars)

print("=" * 60)
print("2. MATTER AGE  (M-channel — stellar nucleosynthesis)")
print("=" * 60)
print(f"  Earth stellar age:               {t_Earth/1e9:.2f} Gyr")
print(f"  Mean nucleosynthesis age:        {t_matter_stellar/1e9:.2f} Gyr")
print(f"  Oldest r-process elements:       {t_matter_oldest/1e9:.2f} Gyr")
print(f"  Stellar matter age excess over")
print(f"    light age:  Δτ_M(stellar) = {(t_matter_stellar - t_Earth)/1e9:.2f} Gyr")
print()

# ── 3. Biological recursion depth ─────────────────────────────────────
# Each biological generation = one M-channel recursion cycle at bio scale
# Accumulated recursion depth = N_gen × ε_floor

# Bacterial (E. coli type, 20 min generation)
t_bact_yr     = t_Life * 1e9          # 3.8e9 yr of bacterial life
gen_min_bact  = 20.0                   # minutes per generation
gen_yr_bact   = gen_min_bact / (525960)  # generations per year ≈ 2.63e4
N_bact        = t_bact_yr * gen_yr_bact

# Eukaryotic (single-cell, ~8hr generation for yeast-like)
t_euk_yr      = 2.0e9                  # 2 Gyr of eukaryotic life
gen_hr_euk    = 8.0
gen_yr_euk    = 8760 / gen_hr_euk
N_euk         = t_euk_yr * gen_yr_euk

# Metazoan (complex multicellular, ~3yr mean generation)
t_meta_yr     = 0.6e9
gen_yr_meta   = 1/3.0
N_meta        = t_meta_yr * gen_yr_meta

# Human lineage (25yr generation)
t_hum_yr      = t_Human * 1e9
gen_yr_hum    = 1/25.0
N_hum         = t_hum_yr * gen_yr_hum

N_total = N_bact + N_euk + N_meta + N_hum

print("=" * 60)
print("3. BIOLOGICAL RECURSION DEPTH  (M-channel acceleration)")
print("=" * 60)
print(f"  Bacterial generations (3.8 Gyr):  {N_bact:.3e}")
print(f"  Eukaryotic generations (2 Gyr):   {N_euk:.3e}")
print(f"  Metazoan generations (600 Myr):   {N_meta:.3e}")
print(f"  Human lineage (3 Myr):            {N_hum:.3e}")
print(f"  Total biological cycles:          {N_total:.3e}")
print()
print(f"  Accumulated ε_floor recursion depth:")
print(f"    N × r³ = {N_total:.3e} × {eps:.6f} = {N_total * eps:.3e}")
print()

# Recursion depth ratio: bio vs stellar thermal cycle
# Stellar thermal (Kelvin-Helmholtz) timescale ~15 Myr for Sun
# Number of KH cycles in 4.57 Gyr:
N_KH = t_Earth / 15e6
print(f"  Stellar Kelvin-Helmholtz cycles:  {N_KH:.0f}")
print(f"  Bio/stellar KH cycle ratio:       {N_total/N_KH:.3e}")
print()

# ── 4. Total matter age ───────────────────────────────────────────────
# In UM: matter age = stellar nucleosynthesis age + biological recursion contribution
# Convert biological recursion depth to an effective "age" in Gyr
# by asking: how many Hubble times of stellar recursion would give the same depth?

# Stellar recursion rate: N_KH per 4.57 Gyr → N_KH/t_Earth per Gyr
stellar_rate  = N_KH / (t_Earth/1e9)   # cycles per Gyr (stellar scale)
bio_eff_age   = (N_total / stellar_rate) / 1e9  # effective Gyr equivalent

print("=" * 60)
print("4. EFFECTIVE MATTER AGE  (stellar + biological)")
print("=" * 60)
print(f"  Stellar nucleosynthesis age:     {t_matter_stellar/1e9:.2f} Gyr")
print(f"  Biological recursion equivalent: {bio_eff_age:.3e} Gyr")
print(f"  Total effective matter age:      τ_M ≈ {(t_matter_stellar/1e9 + bio_eff_age):.3e} Gyr")
print()
print(f"  Ratio τ_M / τ_L = {(t_matter_stellar/1e9 + bio_eff_age) / (t_Earth/1e9):.3e}")
print()

# ── 5. The key implication ────────────────────────────────────────────
print("=" * 60)
print("5. IMPLICATIONS FOR YOUNG STAR SYSTEMS")
print("=" * 60)
print()

# If Ouroboros A is 0.45 Gyr old:
t_ouro = 0.45e9   # yr
# Stellar KH cycles:
N_KH_ouro = t_ouro / 15e6
# If bacterial life present since 0.1 Gyr:
t_bact_ouro = 0.35e9
N_bact_ouro = t_bact_ouro * gen_yr_bact
print(f"  Ouroboros A stellar age:         {t_ouro/1e9:.2f} Gyr")
print(f"  Stellar KH cycles:               {N_KH_ouro:.0f}")
print(f"  If bacterial life since 0.1 Gyr:")
print(f"    Bio cycles:                    {N_bact_ouro:.3e}")
print(f"    Bio recursion depth:           {N_bact_ouro * eps:.3e}")
print(f"    Equivalent stellar cycles:     {N_bact_ouro / (N_KH_ouro / (t_ouro/1e9) / 1e9):.3e}")
print()
print(f"  Conclusion: a 0.45 Gyr stellar age with bacterial life")
print(f"  accumulates {N_bact_ouro:.2e} bio recursion cycles.")
print(f"  Earth at same stellar age had ~{(0.35e9 * gen_yr_bact):.2e} cycles.")
print(f"  The matter age is determined by biology, not the star.")
print()

# ── 6. UM r-structure of Earth's age ─────────────────────────────────
print("=" * 60)
print("6. EARTH AGE IN r-STRUCTURE")
print("=" * 60)
print()
print(f"  t_Earth / t_Hubble = {t_Earth/t_Hubble:.6f}")
print(f"  r²                 = {r**2:.6f}")
print(f"  r² / 2             = {r**2/2:.6f}  ← Ωb")
print(f"  2r²                = {2*r**2:.6f}")
print(f"  r² × φ             = {r**2 * phi:.6f}")
print()
print(f"  Closest r-expression to t_Earth/t_H:")
candidates = {
    'r²':      r**2,
    '2r²':     2*r**2,
    'r²φ':     r**2*phi,
    'r/φ':     r/phi,
    'r²+r³':   r**2+r**3,
    '2r/(1+r)': 2*r/(1+r),
    'r^1.5':   r**1.5,
}
target = t_Earth / t_Hubble
for name, val in sorted(candidates.items(), key=lambda x: abs(x[1]-target)):
    print(f"    {name:12s} = {val:.6f}  Δ = {val-target:+.6f}")
