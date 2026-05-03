"""High-lmax (8000) matter overdensity + C_l pipeline — UM cosmology."""
import sys, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, "/home/joe/Desktop/UNIFIED_MECHANICS_v2")
sys.path.insert(0, "/mnt/Data/Science/OSIRIS")

import numpy as np
import healpy as hp
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json
from scipy.integrate import trapezoid as sci_trapz

from limb.camb_backend import build_camb_params
from limb.derivations import lcdm_inputs as D
import camb

# ── Cosmology ─────────────────────────────────────────────────────────
LMAX  = 8000
NSIDE = 2048

pars = build_camb_params(lmax=LMAX, lens_potential_accuracy=0)
pars.WantTransfer = True
H0   = float(pars.H0)
h    = H0 / 100.0
Ob   = float(D.Omega_b())
Oc   = float(D.Omega_c())
ns   = float(D.n_s())
As   = float(D.A_s())
Om   = Ob + Oc
print(f"UM: H0={H0:.2f}  h={h:.4f}  Ob={Ob:.4f}  Oc={Oc:.4f}  ns={ns:.4f}")

results = camb.get_results(pars)

# ── Matter P(k) ────────────────────────────────────────────────────────
k_h, _, Pk2d = results.get_matter_power_spectrum(minkh=1e-4, maxkh=100, npoints=600)
Pk_z0 = Pk2d[0]
print(f"P(k=0.1) = {float(np.interp(0.1, k_h, Pk_z0)):.1f} (Mpc/h)³")

# ── CMB C_l (TT) ──────────────────────────────────────────────────────
cls_cmb = results.get_cmb_power_spectra(pars, CMB_unit="muK")["total"][:, 0]
ells_cmb = np.arange(len(cls_cmb))

# ── Limber C_l for projected matter ───────────────────────────────────
# n(z) Smail distribution (photometric z~0.1-3)
z_arr = np.linspace(0.01, 3.0, 400)
z0, alpha, beta = 0.5, 1.5, 2.5
nz = (z_arr / z0)**alpha * np.exp(-(z_arr / z0)**beta)
nz /= sci_trapz(nz, z_arr)

# Comoving distance χ(z)  [Mpc/h]
E_z = np.sqrt(Om * (1 + z_arr)**3 + (1 - Om))
dchi_dz = (3e5 / H0) / E_z * h      # (Mpc/h) per unit z
chi_arr = np.cumsum(dchi_dz * np.gradient(z_arr))
chi_arr -= chi_arr[0]

# Window function W(z) = n(z)/χ² × (dχ/dz)⁻¹  → normalise
W_z = nz * dchi_dz
W_z /= sci_trapz(W_z, z_arr)

# Limber integral: C_l = ∫ W(z)² P(k_l, z=0) / χ² dχ
ells_mat = np.arange(2, min(LMAX + 1, 3001))
Cl_mat   = np.zeros(len(ells_mat))

Pk_k  = k_h        # k in h/Mpc
Pk_pz = Pk_z0      # P(k) at z=0

dchi = dchi_dz * np.gradient(z_arr)
chi_safe = np.maximum(chi_arr, 1.0)

for i, ell in enumerate(ells_mat):
    k_l    = (ell + 0.5) / chi_safe          # h/Mpc
    Pk_l   = np.interp(k_l, Pk_k, Pk_pz, left=0, right=0)
    Cl_mat[i] = sci_trapz(W_z**2 * Pk_l / chi_safe**2 * dchi, z_arr)

print(f"C_l matter computed for ells 2–{ells_mat[-1]}")

# ── Matter overdensity HEALPix map (NSIDE=2048) ───────────────────────
# Pad C_l array to LMAX
Cl_full = np.zeros(LMAX + 1)
Cl_full[2:len(ells_mat)+2] = np.maximum(Cl_mat, 0)

np.random.seed(42)
matter_map = hp.synfast(Cl_full, nside=NSIDE, lmax=LMAX, verbose=False)
print(f"Matter map synthesised: NSIDE={NSIDE}  npix={hp.nside2npix(NSIDE)}")

# ── Load CMB targets + Gaia stars ─────────────────────────────────────
ras_t  = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_ra.npy")
decs_t = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_dec.npy")
dTs_t  = np.load("/home/joe/Desktop/PLANET_HUNT/01_cmb_pipeline/cmb_targets_dT.npy")
patches = list(zip(ras_t[1:13], decs_t[1:13], dTs_t[1:13]))

with open("/home/joe/Desktop/PLANET_HUNT/02_gaia_targets/cmb_ranked_targets.json") as f:
    gstars = json.load(f)

PATCH_RAD = 0.9   # degrees

# ── Figure 1: 12-patch gallery (matter overdensity from map) ──────────
fig1, axes = plt.subplots(3, 4, figsize=(22, 15))
fig1.patch.set_facecolor("#050510")

for idx, (ra, dec, dT) in enumerate(patches):
    ax = axes[idx // 4, idx % 4]
    ax.set_facecolor("#07071a")

    # Extract pixels in patch from matter map
    ra_rad  = np.radians(ra)
    dec_rad = np.radians(dec)
    vec = hp.ang2vec(np.pi/2 - dec_rad, ra_rad)
    ipix = hp.query_disc(NSIDE, vec, np.radians(PATCH_RAD * 1.1))

    theta_p, phi_p = hp.pix2ang(NSIDE, ipix)
    dec_p = 90 - np.degrees(theta_p)
    ra_p  = np.degrees(phi_p)

    delta = matter_map[ipix]
    sc = ax.scatter(ra_p, dec_p, c=delta, cmap="inferno",
                    vmin=np.percentile(delta, 5), vmax=np.percentile(delta, 95),
                    s=0.3, alpha=0.7, rasterized=True)

    # G-star targets
    near = [s for s in gstars
            if abs(s["ra"] - ra) < PATCH_RAD * 1.5
            and abs(s["dec"] - dec) < PATCH_RAD * 1.5]
    if near:
        ax.scatter([s["ra"] for s in near[:6]],
                   [s["dec"] for s in near[:6]],
                   marker="*", s=100, color="white",
                   edgecolors="#88FFAA", linewidths=0.5, zorder=5)

    ax.set_xlim(ra - PATCH_RAD * 1.1, ra + PATCH_RAD * 1.1)
    ax.set_ylim(dec - PATCH_RAD * 1.1, dec + PATCH_RAD * 1.1)
    ax.tick_params(colors="white", labelsize=5)
    for sp in ax.spines.values():
        sp.set_color("#2a2a4a")
    plt.setp(ax.get_xticklabels(), color="white")
    plt.setp(ax.get_yticklabels(), color="white")
    ax.set_title(f"ΔT={dT:.2f}µK  ({ra:.0f}°,{dec:+.0f}°)  {len(near)}G★",
                 color="#88FFAA", fontsize=7, pad=3)

plt.colorbar(sc, ax=axes.ravel().tolist(), label="Matter overdensity δ",
             orientation="vertical", fraction=0.012, pad=0.01)
fig1.suptitle(
    f"Matter Overdensity — NSIDE={NSIDE}  lmax={LMAX}  UM cosmology\n"
    "Top 12 CMB seed patches  ★ = G-type planet targets",
    color="white", fontsize=11, fontweight="bold", y=1.01)

out1 = "/home/joe/Desktop/PLANET_HUNT/04_skypy_lss/skypy_highl_patches.png"
fig1.savefig(out1, dpi=120, bbox_inches="tight", facecolor="#050510")
plt.close(fig1)
print(f"Patch gallery → {out1}")

# ── Figure 2: Full-dynamic-range P(k) ─────────────────────────────────
fig2, ax2 = plt.subplots(figsize=(10, 6))
fig2.patch.set_facecolor("#050510")
ax2.set_facecolor("#060618")
ax2.loglog(k_h, Pk_z0, color="#44aaff", lw=2.0, label=f"UM/LiMB  z=0  lmax={LMAX}")
ax2.fill_between(k_h, Pk_z0 * 0.9, Pk_z0 * 1.1, alpha=0.15, color="#44aaff")
ax2.axvline(0.01,  color="#FFCC44", lw=1, ls=":", alpha=0.6, label="Horizon scale k=0.01")
ax2.axvline(0.1,   color="#88FF88", lw=1, ls="--", alpha=0.7, label="BAO scale k=0.1")
ax2.axvline(1.0,   color="#FF8888", lw=1, ls="--", alpha=0.7, label="Nonlinear k=1.0")
ax2.axvline(10.0,  color="#FF44AA", lw=1, ls=":", alpha=0.5, label="Small scale k=10")
ax2.set_xlabel("k  (h/Mpc)", color="white", fontsize=12)
ax2.set_ylabel("P(k)  (Mpc/h)³", color="white", fontsize=12)
ax2.tick_params(colors="white")
ax2.grid(True, alpha=0.15)
for sp in ax2.spines.values():
    sp.set_color("#2a2a4a")
plt.setp(ax2.get_xticklabels(), color="white")
plt.setp(ax2.get_yticklabels(), color="white")
ax2.legend(fontsize=9, facecolor="#0a0a1a", labelcolor="white")
ax2.set_title(
    f"Matter Power Spectrum — UM lmax={LMAX}\n"
    f"H0={H0:.1f}  Ωb={Ob:.4f}  Ωc={Oc:.4f}  ns={ns:.4f}  As={As:.3e}",
    color="white", fontsize=10)

out2 = "/home/joe/Desktop/PLANET_HUNT/04_skypy_lss/matter_power_spectrum_highl.png"
fig2.savefig(out2, dpi=150, bbox_inches="tight", facecolor="#050510")
plt.close(fig2)
print(f"P(k) high-lmax → {out2}")

# ── Figure 3: C_l comparison — CMB TT vs matter ───────────────────────
fig3, ax3 = plt.subplots(figsize=(12, 6))
fig3.patch.set_facecolor("#050510")
ax3.set_facecolor("#060618")

ell_cmb_plot = ells_cmb[2:min(LMAX+1, len(ells_cmb))]
dl_cmb = ell_cmb_plot * (ell_cmb_plot + 1) / (2 * np.pi) * cls_cmb[2:len(ell_cmb_plot)+2]
ax3.semilogy(ell_cmb_plot, np.maximum(dl_cmb, 1e-6),
             color="#44aaff", lw=1.5, alpha=0.9, label="CMB TT  D_ℓ = ℓ(ℓ+1)Cℓ/2π  (µK²)")

dl_mat = ells_mat * (ells_mat + 1) / (2 * np.pi) * np.maximum(Cl_mat, 1e-20)
# Normalise matter D_l to CMB peak for visual comparison
cmb_peak = np.max(dl_cmb[:300]) if len(dl_cmb) > 300 else np.max(dl_cmb)
mat_peak  = np.max(dl_mat)
scale = cmb_peak / mat_peak if mat_peak > 0 else 1.0
ax3.semilogy(ells_mat, dl_mat * scale,
             color="#FF8844", lw=1.5, alpha=0.9,
             label=f"Matter (Limber)  ×{scale:.1e}  (scaled)")

ax3.axvline(200,  color="#88FF88", lw=1, ls="--", alpha=0.6, label="ℓ=200 (first CMB peak)")
ax3.axvline(2000, color="#FF8888", lw=1, ls="--", alpha=0.6, label="ℓ=2000")
ax3.set_xlabel("Multipole ℓ", color="white", fontsize=12)
ax3.set_ylabel("D_ℓ  (µK² or arbitrary)", color="white", fontsize=12)
ax3.set_xlim(2, LMAX)
ax3.tick_params(colors="white")
ax3.grid(True, alpha=0.15)
for sp in ax3.spines.values():
    sp.set_color("#2a2a4a")
plt.setp(ax3.get_xticklabels(), color="white")
plt.setp(ax3.get_yticklabels(), color="white")
ax3.legend(fontsize=9, facecolor="#0a0a1a", labelcolor="white")
ax3.set_title(
    f"Angular Power Spectra — CMB TT vs Projected Matter  (lmax={LMAX})\nUM cosmology",
    color="white", fontsize=11)

out3 = "/home/joe/Desktop/PLANET_HUNT/04_skypy_lss/cl_cmb_vs_matter.png"
fig3.savefig(out3, dpi=150, bbox_inches="tight", facecolor="#050510")
plt.close(fig3)
print(f"C_l comparison → {out3}")
print("Done.")
