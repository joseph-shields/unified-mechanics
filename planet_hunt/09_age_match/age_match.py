"""
Age-match the 1,287 CMB-selected G-stars against Gaia DR3 astrophysical
parameters (FLAME ages) + isochrone/gyro proxies.

Tiers:
  Peer     — 3.5–5.5 Gyr  (Earth's stage right now)
  Ahead    — 5.5–8.0 Gyr  (same seed, further along)
  Elder    — > 8.0 Gyr    (structurally older lineage)
  Young    — < 3.5 Gyr    (still developing)
"""
import warnings; warnings.filterwarnings("ignore")
import json, os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "/home/joe/Desktop/PLANET_HUNT/09_age_match"
os.makedirs(OUT, exist_ok=True)

# Load full 1,287-star catalogue
with open("/home/joe/Desktop/PLANET_HUNT/02_gaia_targets/cmb_gstar_targets.json") as f:
    targets = json.load(f)

source_ids = [str(t['source_id']) for t in targets]
target_map = {str(t['source_id']): t for t in targets}
print(f"Total targets: {len(targets)}")

# ── Query Gaia DR3 astrophysical_parameters for FLAME ages ────────────
print("Querying Gaia DR3 astrophysical_parameters (FLAME ages)...")
ages = {}
try:
    from astroquery.gaia import Gaia
    Gaia.MAIN_GAIA_TABLE = "gaiadr3.gaia_source"

    # Batch in chunks of 200
    chunk_size = 200
    for i in range(0, len(source_ids), chunk_size):
        chunk = source_ids[i:i+chunk_size]
        id_list = ",".join(chunk)
        try:
            job = Gaia.launch_job(f"""
                SELECT ap.source_id,
                       ap.age_flame, ap.age_flame_lower, ap.age_flame_upper,
                       ap.mass_flame, ap.lum_flame,
                       ap.teff_gspspec, ap.logg_gspspec, ap.mh_gspspec,
                       ap.alphafe_gspspec,
                       gs.teff_gspphot, gs.logg_gspphot
                FROM gaiadr3.astrophysical_parameters AS ap
                JOIN gaiadr3.gaia_source AS gs ON ap.source_id = gs.source_id
                WHERE ap.source_id IN ({id_list})
            """, verbose=False)
            r = job.get_results()
            for row in r:
                sid = str(row['source_id'])
                ages[sid] = {
                    'age_flame':       float(row['age_flame'])       if row['age_flame'] is not None else None,
                    'age_flame_lower': float(row['age_flame_lower']) if row['age_flame_lower'] is not None else None,
                    'age_flame_upper': float(row['age_flame_upper']) if row['age_flame_upper'] is not None else None,
                    'mass_flame':      float(row['mass_flame'])      if row['mass_flame'] is not None else None,
                    'teff_gspspec':    float(row['teff_gspspec'])    if row['teff_gspspec'] is not None else None,
                    'logg_gspspec':    float(row['logg_gspspec'])    if row['logg_gspspec'] is not None else None,
                    'mh_gspspec':      float(row['mh_gspspec'])      if row['mh_gspspec'] is not None else None,
                }
            print(f"  Chunk {i//chunk_size+1}: {len(r)} matches")
        except Exception as e:
            print(f"  Chunk {i//chunk_size+1} failed: {e}")

except Exception as e:
    print(f"Gaia query failed: {e}")

print(f"Total stars with Gaia age data: {len(ages)}")

# ── Merge age data into targets ────────────────────────────────────────
results = []
for t in targets:
    sid = str(t['source_id'])
    entry = dict(t)
    age_data = ages.get(sid, {})
    entry.update(age_data)
    results.append(entry)

# ── Tier classification ────────────────────────────────────────────────
def classify(age):
    if age is None: return 'unknown'
    if age < 3.5:   return 'young'
    if age < 5.5:   return 'peer'
    if age < 8.0:   return 'ahead'
    return 'elder'

TIER_COLOR = {
    'peer':    '#44FF88',
    'ahead':   '#FFD700',
    'elder':   '#FF6644',
    'young':   '#4488FF',
    'unknown': '#888888',
}

for r in results:
    r['tier'] = classify(r.get('age_flame'))

# Count tiers
from collections import Counter
tier_counts = Counter(r['tier'] for r in results)
print("\nTier breakdown:")
for tier, n in sorted(tier_counts.items()):
    print(f"  {tier:8s}: {n}")

# ── Ranked lists ───────────────────────────────────────────────────────
peers  = sorted([r for r in results if r['tier'] == 'peer'],
                key=lambda x: abs(x.get('age_flame', 99) - 4.5))
ahead  = sorted([r for r in results if r['tier'] == 'ahead'],
                key=lambda x: x.get('age_flame', 0), reverse=True)
elders = sorted([r for r in results if r['tier'] == 'elder'],
                key=lambda x: x.get('age_flame', 0), reverse=True)
known  = [r for r in results if r['tier'] != 'unknown']

print(f"\nTop peers (closest to 4.5 Gyr):")
for r in peers[:10]:
    age = r.get('age_flame')
    lo  = r.get('age_flame_lower')
    hi  = r.get('age_flame_upper')
    print(f"  {r['source_id']}  dist={r['dist_pc']:.1f}pc  "
          f"Teff={r['teff']:.0f}K  age={age:.2f} [{lo:.2f},{hi:.2f}] Gyr  "
          f"ΔT={r['cmb_dT']:.2f}µK")

print(f"\nTop elders (oldest first):")
for r in (elders+ahead)[:10]:
    age = r.get('age_flame')
    print(f"  {r['source_id']}  dist={r['dist_pc']:.1f}pc  "
          f"Teff={r['teff']:.0f}K  age={age:.2f} Gyr  "
          f"ΔT={r['cmb_dT']:.2f}µK  tier={r['tier']}")

# ── Figure ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(18, 8))
fig.patch.set_facecolor("#03030f")
for ax in axes: ax.set_facecolor("#07071a")

# Left: age distribution
ages_known = [r['age_flame'] for r in known if r.get('age_flame')]
if ages_known:
    axes[0].hist(ages_known, bins=30, color="#4488ff", alpha=0.7,
                 edgecolor="#2255aa")
    axes[0].axvspan(3.5, 5.5, color="#44FF88", alpha=0.15, label="Peer window (3.5–5.5 Gyr)")
    axes[0].axvline(4.57, color="#44FF88", lw=2, ls="--", label="Earth age (4.57 Gyr)")
    axes[0].axvspan(5.5, 8.0, color="#FFD700", alpha=0.10, label="Ahead (5.5–8 Gyr)")
    axes[0].axvspan(8.0, 14, color="#FF6644", alpha=0.10, label="Elder (>8 Gyr)")
    axes[0].set_xlabel("Stellar age (Gyr)", color="white")
    axes[0].set_ylabel("Count", color="white")
    axes[0].set_title(
        f"Age distribution — {len(ages_known)} CMB-matched G-stars with Gaia FLAME ages\n"
        f"Peers: {tier_counts['peer']}  Ahead: {tier_counts['ahead']}  "
        f"Elder: {tier_counts['elder']}  Young: {tier_counts['young']}",
        color="white", fontsize=10)
    axes[0].legend(facecolor="#0a0a1a", labelcolor="white", fontsize=8)
    axes[0].tick_params(colors="white")
    for sp in axes[0].spines.values(): sp.set_color("#2a2a4a")
    plt.setp(axes[0].get_xticklabels(), color="white")
    plt.setp(axes[0].get_yticklabels(), color="white")

# Right: sky scatter coloured by tier
for tier, color in TIER_COLOR.items():
    pts = [r for r in results if r['tier'] == tier]
    if not pts:
        continue
    ras  = [r['ra'] for r in pts]
    decs = [r['dec'] for r in pts]
    ages_t = [r.get('age_flame') or 0 for r in pts]
    sizes  = [20 if tier == 'unknown' else 40 for _ in pts]
    axes[1].scatter(ras, decs, s=sizes, c=color, alpha=0.7,
                    label=f"{tier} ({len(pts)})", zorder=3)

# Mark Earth direction
axes[1].scatter([242.56], [-59.68], s=200, c="white", marker="*",
                zorder=5, label="Earth seed")
axes[1].set_xlabel("RA (deg)", color="white")
axes[1].set_ylabel("Dec (deg)", color="white")
axes[1].set_title(
    "CMB-matched G-stars — age tiers\n"
    "★ = Earth CMB seed direction",
    color="white", fontsize=10)
axes[1].legend(facecolor="#0a0a1a", labelcolor="white", fontsize=8,
               ncol=2)
axes[1].tick_params(colors="white")
for sp in axes[1].spines.values(): sp.set_color("#2a2a4a")
plt.setp(axes[1].get_xticklabels(), color="white")
plt.setp(axes[1].get_yticklabels(), color="white")

plt.tight_layout(pad=2.0)
fig.savefig(f"{OUT}/age_tiers.png", dpi=150,
            bbox_inches="tight", facecolor="#03030f")
plt.close(fig)
print(f"\nFigure → {OUT}/age_tiers.png")

# ── Save catalogue ─────────────────────────────────────────────────────
with open(f"{OUT}/age_matched_catalogue.json", "w") as f:
    json.dump(results, f, indent=2, default=str)

# ── Top-10 ops list ────────────────────────────────────────────────────
ops = sorted(known, key=lambda x: (
    # Sort: peers first (closest to 4.5), then ahead, then elder
    0 if x['tier']=='peer' else 1 if x['tier']=='ahead' else 2,
    abs(x.get('age_flame',99) - 4.5)
))[:20]

print("\n" + "="*70)
print("TOP OPS TARGETS — CMB-matched, age-ranked")
print("="*70)
print(f"{'Rank':<5} {'Source ID':<22} {'Dist':>6} {'Teff':>6} {'Age':>8} {'Tier':<8} {'ΔT':>6}")
print("-"*70)
for i, r in enumerate(ops):
    print(f"{i+1:<5} {str(r['source_id']):<22} "
          f"{r['dist_pc']:>5.1f}pc "
          f"{r['teff']:>6.0f}K "
          f"{r.get('age_flame',0):>7.2f}Gyr "
          f"{r['tier']:<8} "
          f"{r['cmb_dT']:>5.2f}µK")

with open(f"{OUT}/ops_targets.json", "w") as f:
    json.dump(ops, f, indent=2, default=str)
print(f"\nSaved {len(ops)} ops targets → {OUT}/ops_targets.json")
print("Done.")
