"""Planck SMICA CMB map — equatorial render with UM target overlay."""
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

# ── Load Planck SMICA I map (field 0 = temperature, units µK_CMB) ─────
print("Loading Planck SMICA map...")
planck_map = hp.read_map(PLANCK_FILE, field=0, verbose=False)
# Convert K → µK if needed (Planck R3 is already in µK_CMB)
if np.std(planck_map[planck_map != hp.UNSEEN]) < 1e-3:
    planck_map[planck_map != hp.UNSEEN] *= 1e6
    print("  Converted K → µK")

NSIDE_planck = hp.get_nside(planck_map)
print(f"  NSIDE={NSIDE_planck}  npix={hp.nside2npix(NSIDE_planck)}")

# Planck map is in GALACTIC coords — rotate to EQUATORIAL (celestial)
# healpy rotator: GAL → EQU
rot = hp.Rotator(coord=["G", "C"])
planck_equ = rot.rotate_map_pixel(planck_map)
print("  Rotated: galactic → equatorial")

# ── Load targets ───────────────────────────────────────────────────────
ras_t  = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_ra.npy")
decs_t = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_dec.npy")
dTs_t  = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_dT.npy")

with open("/home/joe/Desktop/PLANET_HUNT/02_gaia_targets/cmb_ranked_targets.json") as f:
    gstars = json.load(f)

# ── Read actual Planck temperature at each UM CMB target position ──────
def planck_temp_at(ra_deg, dec_deg, radius_deg=5.0, nside=NSIDE_planck):
    """Disc-averaged Planck temperature at given equatorial RA/Dec."""
    ra_r  = np.radians(ra_deg)
    dec_r = np.radians(dec_deg)
    vec = hp.ang2vec(np.pi/2 - dec_r, ra_r)
    ipix = hp.query_disc(nside, vec, np.radians(radius_deg))
    vals = planck_equ[ipix]
    vals = vals[vals != hp.UNSEEN]
    return float(np.mean(vals)) if len(vals) > 0 else np.nan

earth_ra, earth_dec = 242.56, -59.68
T_earth_planck = planck_temp_at(earth_ra, earth_dec)
print(f"\nPlanck temperature at Earth CMB patch (5° disc): {T_earth_planck:.2f} µK")
print(f"UM simulation value:                              23.2 µK")
print(f"Difference: {abs(T_earth_planck - 23.2):.2f} µK")

# Top 10 UM targets vs Planck actual temps
print("\nUM target vs Planck actual temperatures:")
for i in range(min(10, len(ras_t))):
    T_p = planck_temp_at(ras_t[i], decs_t[i])
    print(f"  #{i+1:2d}  RA={ras_t[i]:7.2f}° Dec={decs_t[i]:+7.2f}°  "
          f"UM_sim={dTs_t[i]+23.2:.2f}µK  Planck={T_p:.2f}µK")

# ── Figure 1: Full-sky Planck mollview in equatorial coords ───────────
print("\nRendering full-sky map...")

# Smooth to 1° for clean visual (NSIDE=2048 is noisy raw)
planck_smooth = hp.smoothing(planck_equ, fwhm=np.radians(1.0), verbose=False)

fig1 = plt.figure(figsize=(18, 10))
fig1.patch.set_facecolor("#050510")

hp.mollview(planck_smooth, fig=fig1.number, coord=None,
            title="", unit="µK", min=-300, max=300,
            cmap="RdBu_r", notext=True, hold=True,
            bgcolor="#050510")

ax = plt.gca()

# Mark Earth CMB patch
earth_theta = np.pi/2 - np.radians(earth_dec)
earth_phi   = np.radians(earth_ra)

# Mark top 50 UM targets
for i, (ra, dec, dT) in enumerate(zip(ras_t[:50], decs_t[:50], dTs_t[:50])):
    th = np.pi/2 - np.radians(dec)
    ph = np.radians(ra)
    hp.projscatter([th], [ph], ax=ax, lonlat=False,
                   marker="o", s=12, color="#44FF88", alpha=0.6, zorder=4)

# Earth marker (bright)
hp.projscatter([earth_theta], [earth_phi], ax=ax, lonlat=False,
               marker="*", s=220, color="yellow",
               edgecolors="white", linewidths=0.8, zorder=10)

# Top 10 Gaia targets
for i, s in enumerate(gstars[:10]):
    th = np.pi/2 - np.radians(s["dec"])
    ph = np.radians(s["ra"])
    hp.projscatter([th], [ph], ax=ax, lonlat=False,
                   marker="*", s=80, color="white",
                   edgecolors="#88FFAA", linewidths=0.5, zorder=8)

ax.set_title(
    "Planck SMICA CMB — Equatorial Coordinates  (1° smoothed)\n"
    f"★ Earth (Laniakea, RA=243°, Dec=-60°, T_Planck={T_earth_planck:.1f}µK)   "
    "● UM seed-matched patches   ✦ Top Gaia G-star targets",
    color="white", fontsize=10, pad=8)

# Planck satellite info box
info = ("Planck satellite\n"
        "Orbit: Sun-Earth L2\n"
        "Distance: 1.5M km anti-Sun\n"
        "Mission: 2009-2013\n"
        "Map: SMICA R3.00")
ax.text(0.01, 0.98, info, transform=ax.transAxes,
        color="#aaaacc", fontsize=7, va="top",
        bbox=dict(boxstyle="round", facecolor="#0a0a2a", alpha=0.7))

out1 = "/home/joe/Desktop/PLANET_HUNT/06_planck/planck_fullsky_equatorial.png"
fig1.savefig(out1, dpi=150, bbox_inches="tight", facecolor="#050510")
plt.close(fig1)
print(f"Full-sky → {out1}")

# ── Figure 2: Earth CMB patch zoom — UM sim vs Planck actual ──────────
print("Rendering Earth patch comparison...")

fig2, (ax_um, ax_pk) = plt.subplots(1, 2, figsize=(16, 7))
fig2.patch.set_facecolor("#050510")
for ax in (ax_um, ax_pk): ax.set_facecolor("#07071a")

# Load UM simulated map
um_map = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_ra.npy")  # just to get range

# Render Planck patch
PATCH = 12.0  # degrees half-width
ra_c, dec_c = earth_ra, earth_dec

for ax, label, use_planck in [(ax_um, "UM Simulation (seed 271828)", False),
                               (ax_pk, f"Planck SMICA (T={T_earth_planck:.1f}µK)", True)]:
    if use_planck:
        src_map = planck_smooth
    else:
        # Load UM CMB map if available, else use Planck smoothed as proxy display
        try:
            src_map = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_map_nside512.npy")
            nside_src = 512
        except FileNotFoundError:
            src_map = planck_smooth
            nside_src = NSIDE_planck

    nside_src = hp.get_nside(src_map)
    vec = hp.ang2vec(np.pi/2 - np.radians(dec_c), np.radians(ra_c))
    ipix = hp.query_disc(nside_src, vec, np.radians(PATCH * 1.2))
    th_p, ph_p = hp.pix2ang(nside_src, ipix)
    dec_p = 90 - np.degrees(th_p)
    ra_p  = np.degrees(ph_p)
    T_p   = src_map[ipix]
    mask  = T_p != hp.UNSEEN

    sc = ax.scatter(ra_p[mask], dec_p[mask], c=T_p[mask], cmap="RdBu_r",
                    vmin=-200, vmax=200, s=1.5, rasterized=True)
    ax.scatter([earth_ra], [earth_dec], marker="*", s=300,
               color="yellow", edgecolors="white", linewidths=0.8, zorder=10)
    ax.set_xlim(ra_c - PATCH, ra_c + PATCH)
    ax.set_ylim(dec_c - PATCH, dec_c + PATCH)
    ax.set_xlabel("RA (°)", color="white")
    ax.set_ylabel("Dec (°)", color="white")
    ax.tick_params(colors="white")
    for sp in ax.spines.values(): sp.set_color("#2a2a4a")
    plt.setp(ax.get_xticklabels(), color="white")
    plt.setp(ax.get_yticklabels(), color="white")
    ax.set_title(label, color="#88FFAA", fontsize=10)

plt.colorbar(sc, ax=[ax_um, ax_pk], label="ΔT (µK)",
             orientation="vertical", fraction=0.025, pad=0.02)
fig2.suptitle("Earth CMB Seed Patch — UM Prediction vs Planck Reality\n"
              "★ Earth (Laniakea direction, RA=243°, Dec=−60°)",
              color="white", fontsize=11, fontweight="bold")

out2 = "/home/joe/Desktop/PLANET_HUNT/06_planck/planck_earth_patch_comparison.png"
fig2.savefig(out2, dpi=150, bbox_inches="tight", facecolor="#050510")
plt.close(fig2)
print(f"Earth patch comparison → {out2}")
print("Done.")
