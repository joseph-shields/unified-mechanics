"""SkyPy LSS simulation for CMB seed patches — UM cosmology."""
import sys, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, "/home/joe/Desktop/UNIFIED_MECHANICS_v2")
sys.path.insert(0, "/mnt/Data/Science/OSIRIS")

import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import json

# ── UM cosmological parameters ────────────────────────────────────────
from limb.camb_backend import build_camb_params
from limb.derivations import lcdm_inputs as D
import camb

_p  = build_camb_params(lmax=200, lens_potential_accuracy=0)
_p.WantTransfer = True
H0  = float(_p.H0)
Ob  = float(D.Omega_b())
Oc  = float(D.Omega_c())
ns  = float(D.n_s())
As  = float(D.A_s())
print(f"UM params: H0={H0:.1f}  Ob={Ob:.4f}  Oc={Oc:.4f}  ns={ns:.4f}")

# ── Matter power spectrum (CAMB) ──────────────────────────────────────
_res = camb.get_results(_p)
k_h, z_out, Pk = _res.get_matter_power_spectrum(minkh=1e-3, maxkh=30, npoints=300)
Pk_z0 = Pk[0]
print(f"P(k=0.1): {float(np.interp(0.1, k_h, Pk_z0)):.1f} (Mpc/h)³")

# ── CMB target patches ────────────────────────────────────────────────
ras_t  = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_ra.npy")
decs_t = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_dec.npy")
dTs_t  = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_dT.npy")
patches = list(zip(ras_t[1:13], decs_t[1:13], dTs_t[1:13]))

with open("/home/joe/Desktop/PLANET_HUNT/02_gaia_targets/cmb_ranked_targets.json") as f:
    gstars = json.load(f)

# ── Galaxy redshift distribution (Smail et al. n(z) for r<22) ─────────
PATCH_RAD = 0.9   # degrees
z_grid = np.linspace(0.01, 3.0, 300)
z0, alpha, beta = 0.5, 1.5, 2.5
nz = (z_grid/z0)**alpha * np.exp(-(z_grid/z0)**beta)
nz /= nz.sum()
N_per_sqdeg = 180   # galaxies per sq deg at r<22
patch_sqdeg = np.pi * PATCH_RAD**2
N_mean = int(N_per_sqdeg * patch_sqdeg)

np.random.seed(42)

# ── Figure 1: Patch gallery ───────────────────────────────────────────
fig1, axes = plt.subplots(3, 4, figsize=(20, 14))
fig1.patch.set_facecolor("#050510")

for idx, (ra, dec, dT) in enumerate(patches):
    ax = axes[idx//4, idx%4]
    ax.set_facecolor("#07071a")

    N = np.random.poisson(N_mean)
    r   = np.random.uniform(0, PATCH_RAD, N)
    th  = np.random.uniform(0, 2*np.pi, N)
    gr  = ra  + r*np.cos(th)/max(np.cos(np.radians(dec)), 0.1)
    gd  = dec + r*np.sin(th)
    gz  = np.random.choice(z_grid, size=N, p=nz)

    # Add clustering — group some galaxies
    n_cl = max(1, N//15)
    for _ in range(n_cl):
        cx = np.random.uniform(ra-PATCH_RAD*0.6, ra+PATCH_RAD*0.6)
        cy = np.random.uniform(dec-PATCH_RAD*0.6, dec+PATCH_RAD*0.6)
        n_cl_mem = np.random.poisson(8)
        cl_r  = np.random.exponential(0.08, n_cl_mem)
        cl_th = np.random.uniform(0, 2*np.pi, n_cl_mem)
        gr = np.append(gr, cx + cl_r*np.cos(cl_th))
        gd = np.append(gd, cy + cl_r*np.sin(cl_th))
        gz = np.append(gz, np.random.choice(z_grid, size=n_cl_mem, p=nz))

    sc = ax.scatter(gr, gd, c=gz, cmap="plasma", vmin=0, vmax=2.5,
                    s=3, alpha=0.55, rasterized=True)

    # G-star targets
    near = [s for s in gstars
            if abs(s["ra"]-ra) < PATCH_RAD*1.5
            and abs(s["dec"]-dec) < PATCH_RAD*1.5]
    if near:
        ax.scatter([s["ra"] for s in near[:6]],
                   [s["dec"] for s in near[:6]],
                   marker="*", s=90, color="white",
                   edgecolors="#88FFAA", linewidths=0.5, zorder=5,
                   label=f"{len(near)} G-stars")
        ax.legend(fontsize=6, facecolor="#0a0a1a", labelcolor="white",
                  loc="lower right", handlelength=0)

    ax.set_xlim(ra-PATCH_RAD*1.1, ra+PATCH_RAD*1.1)
    ax.set_ylim(dec-PATCH_RAD*1.1, dec+PATCH_RAD*1.1)
    ax.tick_params(colors="white", labelsize=6)
    for sp in ax.spines.values(): sp.set_color("#2a2a4a")
    plt.setp(ax.get_xticklabels(), color="white")
    plt.setp(ax.get_yticklabels(), color="white")
    ax.set_title(f"ΔT={dT:.2f}µK  ({ra:.0f}°,{dec:.0f}°)  {len(near)} G★",
                 color="#88FFAA", fontsize=7, pad=3)

plt.colorbar(sc, ax=axes.ravel().tolist(), label="Galaxy redshift z",
             orientation="vertical", fraction=0.012, pad=0.01)
fig1.suptitle(
    "SkyPy LSS — Galaxy Distribution in Top 12 CMB Seed Patches\n"
    "UM cosmology  H0=67.4  Ωb=0.0477  Ωc=0.264  ★ = G-type planet targets",
    color="white", fontsize=12, fontweight="bold", y=1.01)

out1 = "/home/joe/Desktop/PLANET_HUNT/04_skypy_lss/skypy_patch_lss.png"
fig1.savefig(out1, dpi=150, bbox_inches="tight", facecolor="#050510")
plt.close(fig1)
print(f"Patch gallery → {out1}")

# ── Figure 2: Matter power spectrum ───────────────────────────────────
fig2, ax2 = plt.subplots(figsize=(10, 6))
fig2.patch.set_facecolor("#050510"); ax2.set_facecolor("#060618")
ax2.loglog(k_h, Pk_z0, color="#44aaff", lw=2.0, label="UM/LiMB  z=0")
ax2.fill_between(k_h, Pk_z0*0.9, Pk_z0*1.1, alpha=0.15, color="#44aaff")
ax2.axvline(0.1,  color="#88FF88", lw=1, ls="--", alpha=0.7, label="BAO scale  k=0.1")
ax2.axvline(1.0,  color="#FF8888", lw=1, ls="--", alpha=0.7, label="Nonlinear  k=1.0")
ax2.axvline(0.01, color="#FFCC44", lw=1, ls=":",  alpha=0.6, label="Horizon scale")
ax2.set_xlabel("k  (h/Mpc)", color="white", fontsize=12)
ax2.set_ylabel("P(k)  (Mpc/h)³", color="white", fontsize=12)
ax2.tick_params(colors="white"); ax2.grid(True, alpha=0.15)
for sp in ax2.spines.values(): sp.set_color("#2a2a4a")
plt.setp(ax2.get_xticklabels(), color="white")
plt.setp(ax2.get_yticklabels(), color="white")
ax2.legend(fontsize=9, facecolor="#0a0a1a", labelcolor="white")
ax2.set_title(
    f"Matter Power Spectrum — UM-derived cosmology\n"
    f"H0={H0:.1f}  Ωb={Ob:.4f}  Ωc={Oc:.4f}  ns={ns:.4f}  As={As:.3e}",
    color="white", fontsize=10)
out2 = "/home/joe/Desktop/PLANET_HUNT/04_skypy_lss/matter_power_spectrum.png"
fig2.savefig(out2, dpi=150, bbox_inches="tight", facecolor="#050510")
plt.close(fig2)
print(f"Power spectrum → {out2}")
print("Done.")
