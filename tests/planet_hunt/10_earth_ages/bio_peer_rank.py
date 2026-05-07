"""
Rank all CMB-matched G-stars by biological recursion depth
closest to Earth's current depth. Assumes Earth-timeline biology
(life starts 0.77 Gyr after stellar formation).
"""
import json, math
import numpy as np

phi = (1 + 5**0.5) / 2
r   = 1 / (2 * phi)
eps = r**3

gen_per_yr_bact = 525960 / 20.0
gen_per_yr_euk  = 8760  / 8.0
gen_per_yr_meta = 1     / 3.0

LIFE_DELAY   = 0.77e9   # yr after stellar formation
EUK_DELAY    = 2.50e9
META_DELAY   = 3.97e9
EARTH_FORM   = 4.57e9

def depth(stellar_age_yr):
    t_bact = max(0, stellar_age_yr - LIFE_DELAY)
    t_euk  = max(0, stellar_age_yr - EUK_DELAY)
    t_meta = max(0, stellar_age_yr - META_DELAY)
    N = (t_bact * gen_per_yr_bact +
         t_euk  * gen_per_yr_euk  +
         t_meta * gen_per_yr_meta)
    return N * eps

D_earth = depth(EARTH_FORM)

def safe_age(r_dict):
    a = r_dict.get('age_flame')
    if a is None: return None
    try:
        f = float(a)
        return None if math.isnan(f) else f
    except: return None

# Load catalogue
with open("/home/joe/Desktop/PLANET_HUNT/09_age_match/age_matched_catalogue.json") as f:
    targets = json.load(f)

# Build ranked list
rows = []
for t in targets:
    age = safe_age(t)
    if age is None: continue
    age_yr = age * 1e9
    D = depth(age_yr)
    delta = abs(D - D_earth)
    frac  = D / D_earth * 100 if D_earth > 0 else 0
    bio_time = max(0, age - 0.77)
    rows.append({
        'source_id': t['source_id'],
        'dist_pc':   t['dist_pc'],
        'teff':      t['teff'],
        'stellar_age': age,
        'bio_time':  bio_time,
        'D':         D,
        'delta':     delta,
        'frac':      frac,
        'cmb_dT':    t['cmb_dT'],
        'mh':        t.get('mh_gspspec'),
    })

rows.sort(key=lambda x: x['delta'])

print(f"r={r:.6f}  r³={eps:.6f}")
print(f"Earth D_now = {D_earth:.4e}  (bio running {EARTH_FORM/1e9 - 0.77:.2f} Gyr)")
print()
print("=" * 90)
print("CMB-MATCHED G-STARS — RANKED BY BIOLOGICAL RECURSION DEPTH vs EARTH")
print("=" * 90)
print(f"  {'#':<4} {'Source ID':<22} {'Dist':>6} {'Teff':>6} {'Age':>7} "
      f"{'Bio':>6} {'D':>12} {'%Earth':>8} {'ΔT':>6}")
print("  " + "-"*88)

for i, row in enumerate(rows[:30]):
    mh_str = f"[M/H]={row['mh']:.2f}" if row['mh'] else ""
    marker = " ◀ EARTH" if i == 0 else ""
    print(f"  {i+1:<4} {str(row['source_id']):<22} "
          f"{row['dist_pc']:>5.0f}pc "
          f"{row['teff']:>6.0f}K "
          f"{row['stellar_age']:>6.2f}Gy "
          f"{row['bio_time']:>5.2f}Gy "
          f"{row['D']:>12.3e} "
          f"{row['frac']:>7.1f}% "
          f"{row['cmb_dT']:>5.2f}µK"
          f"{marker}")

print()
print("EARTH reference:")
print(f"  {'EARTH':<26} {'--':>6} {'5778':>6}K "
      f"{4.57:>6.2f}Gy {3.80:>5.2f}Gy "
      f"{D_earth:>12.3e} {'100.0%':>8} {'0.00':>6}µK")

print()
print("=" * 70)
print("TIER SUMMARY")
print("=" * 70)
# Group by how close to Earth
exact   = [r for r in rows if r['frac'] >= 90 and r['frac'] <= 110]
close   = [r for r in rows if r['frac'] >= 50 and r['frac'] < 90]
early   = [r for r in rows if r['frac'] > 0  and r['frac'] < 50]
ahead   = [r for r in rows if r['frac'] > 110]
no_life = [r for r in rows if r['D'] == 0]

print(f"  Biological twins (90–110% Earth depth):  {len(exact)}")
print(f"  Close (50–90% depth):                    {len(close)}")
print(f"  Early (1–50% depth):                     {len(early)}")
print(f"  Ahead (>110% depth):                     {len(ahead)}")
print(f"  No life yet (<0.77 Gyr stellar age):     {len(no_life)}")
print()

if exact:
    print("BIOLOGICAL TWINS — within 10% of Earth's recursion depth:")
    print(f"  {'Source ID':<22} {'Dist':>6} {'Teff':>6} {'Age':>7} {'D %Earth':>10} {'ΔT':>6}")
    for row in exact:
        print(f"  {str(row['source_id']):<22} "
              f"{row['dist_pc']:>5.0f}pc "
              f"{row['teff']:>6.0f}K "
              f"{row['stellar_age']:>6.2f}Gyr "
              f"{row['frac']:>9.1f}% "
              f"{row['cmb_dT']:>5.2f}µK")

# Save
with open("/home/joe/Desktop/PLANET_HUNT/10_earth_ages/bio_peer_ranked.json", "w") as f:
    json.dump(rows[:50], f, indent=2, default=str)
print(f"\nTop 50 saved → bio_peer_ranked.json")
