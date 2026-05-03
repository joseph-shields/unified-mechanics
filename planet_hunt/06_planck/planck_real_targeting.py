"""
Real-sky CMB targeting using Planck SMICA alm directly.
No random seed — this is the actual CMB sky.
Finds the true Planck temperature at Earth's CMB patch and re-runs
seed matching on the real map to validate/compare our UM simulation results.
"""
import sys, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, "/home/joe/Desktop/UNIFIED_MECHANICS_v2")
sys.path.insert(0, "/mnt/Data/Science/OSIRIS")

import numpy as np
import healpy as hp
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json

PLANCK_FILE = "/mnt/Data/Science/data/planck/COM_CMB_IQU-smica_2048_R3.00_full.fits"
NSIDE_TARGET = 64

# ── Load Planck SMICA, rotate galactic → equatorial ───────────────────
print("Loading Planck SMICA...")
planck_gal = hp.read_map(PLANCK_FILE, field=0, dtype=np.float64) * 1e6  # K→µK
rot = hp.Rotator(coord=["G", "C"])
planck_equ = rot.rotate_map_pixel(planck_gal)
print(f"  NSIDE={hp.get_nside(planck_equ)}  std={planck_equ[planck_equ!=hp.UNSEEN].std():.2f} µK")

# Degrade to targeting resolution
planck_64 = hp.ud_grade(planck_equ, NSIDE_TARGET)
print(f"  Degraded to NSIDE={NSIDE_TARGET}")

# ── 5° disc average at every pixel ───────────────────────────────────
print("Computing 5° disc averages across full sky...")
npix = hp.nside2npix(NSIDE_TARGET)
disc_rad = np.radians(5.0)
T_avg = np.zeros(npix)

# Use smoothing as efficient proxy for disc averaging
planck_smooth = hp.smoothing(planck_64, fwhm=np.radians(5.0), verbose=False)
T_avg = planck_smooth

# ── Earth's actual Planck temperature ─────────────────────────────────
earth_ra, earth_dec = 242.56, -59.68
earth_vec = hp.ang2vec(np.pi/2 - np.radians(earth_dec), np.radians(earth_ra))
earth_pix = hp.vec2pix(NSIDE_TARGET, *earth_vec)
T_earth_planck = float(T_avg[earth_pix])

print(f"\nEarth CMB patch (Planck real data):")
print(f"  RA={earth_ra}°  Dec={earth_dec}°")
print(f"  Planck 5° avg T = {T_earth_planck:.2f} µK")
print(f"  UM simulation   = 23.2 µK")
print(f"  Difference      = {abs(T_earth_planck - 23.2):.2f} µK")

# ── Find matched patches in REAL Planck map ───────────────────────────
DELTA_T = 8.0  # µK threshold
theta_all, phi_all = hp.pix2ang(NSIDE_TARGET, np.arange(npix))
dec_all = 90 - np.degrees(theta_all)
ra_all  = np.degrees(phi_all)

# Galactic plane mask (avoid foreground contamination)
rot_inv = hp.Rotator(coord=["C", "G"])
theta_g, phi_g = rot_inv(theta_all, phi_all)
b_deg = 90 - np.degrees(theta_g)
gal_mask = np.abs(b_deg) > 15.0

dT = np.abs(T_avg - T_earth_planck)
matched = gal_mask & (dT < DELTA_T)
n_matched = matched.sum()

print(f"\nPlanck real-sky seed matching:")
print(f"  Earth T_Planck = {T_earth_planck:.2f} µK")
print(f"  Threshold ΔT < {DELTA_T} µK, |b| > 15°")
print(f"  Matched patches: {n_matched} ({100*n_matched/npix:.1f}% of sky)")

ras_planck  = ra_all[matched]
decs_planck = dec_all[matched]
dTs_planck  = dT[matched]

# Sort by ΔT
sort_idx = np.argsort(dTs_planck)
ras_planck  = ras_planck[sort_idx]
decs_planck = decs_planck[sort_idx]
dTs_planck  = dTs_planck[sort_idx]

print("\nTop 10 Planck real-sky seed positions:")
for i in range(min(10, n_matched)):
    print(f"  #{i+1:2d}  RA={ras_planck[i]:7.2f}°  Dec={decs_planck[i]:+7.2f}°  "
          f"ΔT={dTs_planck[i]:.3f} µK  T={T_avg[np.where(matched)[0][sort_idx[i]]]:.2f} µK")

# Save
np.save("/home/joe/Desktop/PLANET_HUNT/06_planck/planck_real_targets_ra.npy",  ras_planck[:50])
np.save("/home/joe/Desktop/PLANET_HUNT/06_planck/planck_real_targets_dec.npy", decs_planck[:50])
np.save("/home/joe/Desktop/PLANET_HUNT/06_planck/planck_real_targets_dT.npy",  dTs_planck[:50])
print("\nSaved top-50 Planck real-sky targets.")

# ── Compare UM sim targets vs Planck real targets ─────────────────────
um_ras  = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_ra.npy")
um_decs = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_dec.npy")

# For each UM target, find the nearest Planck real patch
print("\nUM simulation targets vs Planck real-sky temperature:")
print(f"  {'#':>3}  {'UM RA':>8}  {'UM Dec':>8}  {'UM ΔT':>8}  {'Planck T':>10}  {'Match':>6}")
for i in range(min(10, len(um_ras))):
    pix = hp.ang2pix(NSIDE_TARGET,
                     np.pi/2 - np.radians(um_decs[i]),
                     np.radians(um_ras[i]))
    T_p = float(T_avg[pix])
    dT_p = abs(T_p - T_earth_planck)
    match = "✓" if dT_p < DELTA_T else "✗"
    print(f"  {i+1:3d}  {um_ras[i]:8.2f}  {um_decs[i]:+8.2f}  "
          f"{float(np.load('/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_dT.npy')[i]):8.3f}  "
          f"{T_p:10.2f}  {match:>6}")

# ── Figure 1: Full-sky comparison UM sim vs Planck real ───────────────
print("\nRendering comparison map...")

# Load UM sim targets for overlay
um_dTs = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_dT.npy")

fig = plt.figure(figsize=(20, 16))
fig.patch.set_facecolor("#03030f")

# Panel 1: Planck real-sky (smoothed, equatorial)
hp.mollview(planck_smooth, fig=fig.number, sub=(2,1,1),
            title="", unit="µK", min=-150, max=150,
            cmap="RdBu_r", notext=True, coord=None)
ax1 = plt.gca()

# Mark Planck real matched patches
for ra, dec, dt in zip(ras_planck[:50], decs_planck[:50], dTs_planck[:50]):
    th = np.pi/2 - np.radians(dec)
    ph = np.radians(ra)
    hp.projscatter([th], [ph], lonlat=False,
                   marker="o", s=15, color="#44FF88", alpha=0.7, zorder=4)

# Earth marker
hp.projscatter([np.pi/2 - np.radians(earth_dec)], [np.radians(earth_ra)],
               lonlat=False, marker="*", s=250, color="yellow",
               edgecolors="white", linewidths=0.8, zorder=10)

ax1.set_title(
    f"Planck SMICA — Real CMB Sky (equatorial, 5° smoothed)\n"
    f"★ Earth T={T_earth_planck:.1f} µK   ● {n_matched} matched patches (ΔT<{DELTA_T}µK, |b|>15°)",
    color="white", fontsize=10, pad=6)

# Panel 2: UM simulation targets
planck_512 = hp.ud_grade(planck_equ, 512)
planck_512_smooth = hp.smoothing(planck_512, fwhm=np.radians(1.0), verbose=False)

hp.mollview(planck_512_smooth, fig=fig.number, sub=(2,1,2),
            title="", unit="µK", min=-300, max=300,
            cmap="RdBu_r", notext=True, coord=None)
ax2 = plt.gca()

for ra, dec in zip(um_ras[:50], um_decs[:50]):
    th = np.pi/2 - np.radians(dec)
    ph = np.radians(ra)
    hp.projscatter([th], [ph], lonlat=False,
                   marker="o", s=12, color="#FF8844", alpha=0.7, zorder=4)

hp.projscatter([np.pi/2 - np.radians(earth_dec)], [np.radians(earth_ra)],
               lonlat=False, marker="*", s=250, color="yellow",
               edgecolors="white", linewidths=0.8, zorder=10)

with open("/home/joe/Desktop/PLANET_HUNT/02_gaia_targets/cmb_ranked_targets.json") as f:
    gstars = json.load(f)
for s in gstars[:10]:
    th = np.pi/2 - np.radians(s["dec"])
    ph = np.radians(s["ra"])
    hp.projscatter([th], [ph], lonlat=False,
                   marker="*", s=80, color="white",
                   edgecolors="#88FFAA", linewidths=0.5, zorder=8)

ax2.set_title(
    "UM Simulation — Seed 271828 target patches overlaid on Planck\n"
    "● UM sim patches   ✦ Top Gaia G-star targets   ★ Earth",
    color="white", fontsize=10, pad=6)

fig.suptitle(
    "CMB Seed Targeting — Planck Real Sky vs UM Simulation\n"
    f"Earth Planck T = {T_earth_planck:.2f} µK  |  UM sim T = 23.2 µK  |  "
    f"Δ = {abs(T_earth_planck-23.2):.2f} µK",
    color="white", fontsize=12, fontweight="bold", y=1.01)

out1 = "/home/joe/Desktop/PLANET_HUNT/06_planck/planck_real_vs_um_targets.png"
fig.savefig(out1, dpi=130, bbox_inches="tight", facecolor="#03030f")
plt.close(fig)
print(f"Comparison map → {out1}")

# ── Figure 2: Earth patch zoom — Planck real ──────────────────────────
fig2, ax = plt.subplots(figsize=(10, 9))
fig2.patch.set_facecolor("#03030f")
ax.set_facecolor("#07071a")

PATCH = 15.0
vec = hp.ang2vec(np.pi/2 - np.radians(earth_dec), np.radians(earth_ra))
ipix = hp.query_disc(512, vec, np.radians(PATCH * 1.1))
th_p, ph_p = hp.pix2ang(512, ipix)
dec_p = 90 - np.degrees(th_p)
ra_p  = np.degrees(ph_p)
T_p   = planck_512_smooth[ipix]
mask  = T_p != hp.UNSEEN

sc = ax.scatter(ra_p[mask], dec_p[mask], c=T_p[mask], cmap="RdBu_r",
                vmin=-200, vmax=200, s=2.5, rasterized=True)
ax.scatter([earth_ra], [earth_dec], marker="*", s=400,
           color="yellow", edgecolors="white", linewidths=1.0, zorder=10,
           label=f"Earth  T={T_earth_planck:.1f} µK")

# Mark Ouroboros A
ouro_ra, ouro_dec = 298.874, -29.097
if abs(ouro_ra - earth_ra) < PATCH*1.5 and abs(ouro_dec - earth_dec) < PATCH*1.5:
    ax.scatter([ouro_ra], [ouro_dec], marker="*", s=200,
               color="#88FFAA", edgecolors="white", linewidths=0.8, zorder=9,
               label="Ouroboros A (Gaya)")

ax.set_xlim(earth_ra - PATCH, earth_ra + PATCH)
ax.set_ylim(earth_dec - PATCH, earth_dec + PATCH)
ax.set_xlabel("RA (°)", color="white"); ax.set_ylabel("Dec (°)", color="white")
ax.tick_params(colors="white")
for sp in ax.spines.values(): sp.set_color("#2a2a4a")
plt.setp(ax.get_xticklabels(), color="white")
plt.setp(ax.get_yticklabels(), color="white")
ax.legend(facecolor="#0a0a1a", labelcolor="white", fontsize=9)
plt.colorbar(sc, ax=ax, label="ΔT (µK)")
ax.set_title(
    f"Planck SMICA — Earth CMB Seed Patch (30°×30°)\n"
    f"Earth: Laniakea direction  T_Planck={T_earth_planck:.2f} µK  (UM pred: 23.2 µK)",
    color="white", fontsize=11)

out2 = "/home/joe/Desktop/PLANET_HUNT/06_planck/planck_earth_patch_real.png"
fig2.savefig(out2, dpi=150, bbox_inches="tight", facecolor="#03030f")
plt.close(fig2)
print(f"Earth patch → {out2}")
print("\nDone.")
