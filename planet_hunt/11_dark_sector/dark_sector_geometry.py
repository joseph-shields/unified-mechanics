"""
Dark sector geometry from UM first principles.
The second E8 — dark matter scaffold — derived from r alone.
No EM coupling. Pure M-channel geometry.
"""
import sys
sys.path.insert(0, "/home/joe/Desktop/UNIFIED_MECHANICS_v2")
sys.path.insert(0, "/mnt/Data/Science/OSIRIS")
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import healpy as hp
import os

OUT = "/home/joe/Desktop/PLANET_HUNT/11_dark_sector"
os.makedirs(OUT, exist_ok=True)

phi = (1 + 5**0.5) / 2
r   = 1 / (2 * phi)

# ── UM cosmological inputs ────────────────────────────────────────────
# All closed-form from r
ombh2  = r**2 / 2 * 0.673**2        # baryonic
omch2  = 4*r**2*(1-r) * 0.673**2    # dark matter — 4× bigger than baryons
H0     = 100 * 0.673
ns     = 1 - r**2 / phi**2
As     = r**17

print(f"UM dark matter density: Ωc = {4*r**2*(1-r):.4f}")
print(f"UM baryon density:      Ωb = {r**2/2:.4f}")
print(f"Dark/baryon ratio:      {4*(1-r):.3f}×")
print(f"r = {r:.6f}")
print()

import camb
pars = camb.CAMBparams()
pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2,
                   mnu=0.06, omk=0, tau=0.059)
pars.InitPower.set_params(As=As, ns=ns, r=0)
pars.set_matter_power(redshifts=[0., 0.5, 2.0, 10.0], kmax=100.0)
pars.NonLinear = camb.model.NonLinear_none

results = camb.get_results(pars)
kh, z, pk = results.get_matter_power_spectrum(
    minkh=1e-4, maxkh=100, npoints=500)

# ── Separate dark matter vs baryon power ─────────────────────────────
# Dark matter: pure CDM transfer function (no BAO)
# Baryon: full P(k) with BAO wiggles
# The difference IS the BAO — the visible sector imprint
# Dark sector = P_total - P_baryon_contribution

# Get transfer functions separately
pars_dm = camb.CAMBparams()
pars_dm.set_cosmology(H0=H0, ombh2=0.001, omch2=omch2+ombh2,
                      mnu=0.06, omk=0, tau=0.02)
pars_dm.InitPower.set_params(As=As, ns=ns, r=0)
pars_dm.set_matter_power(redshifts=[0.], kmax=100.0)
pars_dm.NonLinear = camb.model.NonLinear_none
results_dm = camb.get_results(pars_dm)
kh_dm, _, pk_dm = results_dm.get_matter_power_spectrum(
    minkh=1e-4, maxkh=100, npoints=500)

print("Power spectra computed.")
print(f"  Full P(k) peak:      {pk[0].max():.3e} (Mpc/h)³")
print(f"  Dark-only P(k) peak: {pk_dm[0].max():.3e} (Mpc/h)³")

# ── CMB C_ℓ — visible sector projection of dark geometry ─────────────
pars_cmb = camb.CAMBparams()
pars_cmb.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2,
                       mnu=0.06, omk=0, tau=0.059)
pars_cmb.InitPower.set_params(As=As, ns=ns, r=0)
pars_cmb.set_for_lmax(3000, lens_potential_accuracy=0)
results_cmb = camb.get_results(pars_cmb)
powers = results_cmb.get_cmb_power_spectra(pars_cmb, CMB_unit='muK')
cls = powers['total']
ell = np.arange(cls.shape[0])

# ── Sky maps ──────────────────────────────────────────────────────────
NSIDE = 256; lmax = 600
np.random.seed(42)

# Visible sector CMB (with BAO — baryonic imprint)
cl_tt = cls[2:lmax+1, 0] / (ell[2:lmax+1]*(ell[2:lmax+1]+1)/(2*np.pi))
cl_tt = np.concatenate([[0,0], cl_tt])
cmb_map = hp.synfast(cl_tt, nside=NSIDE, lmax=lmax, verbose=False)

# Dark sector map — pure CDM, no BAO wiggles
# Construct C_ℓ from dark-only P(k) via Limber approximation
from scipy.integrate import trapezoid
chi_star = 13500.  # Mpc, approx comoving distance to last scattering

def limber_cl_dark(ell_val, kh_arr, pk_arr, chi=chi_star):
    k = (ell_val + 0.5) / chi
    if k < kh_arr[0] or k > kh_arr[-1]:
        return 0.
    return float(np.interp(k, kh_arr, pk_arr)) / chi**2

cl_dark = np.zeros(lmax+1)
for l in range(2, lmax+1):
    cl_dark[l] = limber_cl_dark(l, kh_dm, pk_dm[0])

# Normalise to same variance as CMB map for visual comparison
cl_dark_norm = cl_dark * (np.var(cmb_map) /
               max(np.sum((2*np.arange(lmax+1)+1)*cl_dark/(4*np.pi)), 1e-30))
dark_map = hp.synfast(cl_dark_norm, nside=NSIDE, lmax=lmax, verbose=False)

# Difference map — BAO imprint = visible sector structure
diff_map = cmb_map - dark_map * (np.std(cmb_map)/max(np.std(dark_map),1e-30))

print(f"  CMB map RMS:        {np.std(cmb_map)*1e6:.1f} µK equiv")
print(f"  Dark sector map RMS:{np.std(dark_map)*1e6:.1f} µK equiv")

# ── Figure ────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(20, 14))
fig.patch.set_facecolor("#03030f")

# P(k) comparison
ax1 = fig.add_subplot(2, 3, 1)
ax1.set_facecolor("#07071a")
ax1.loglog(kh, pk[0], color="#4488ff", lw=1.5, label="Full P(k) — visible sector")
ax1.loglog(kh_dm, pk_dm[0], color="#FF6644", lw=1.5, ls="--",
           label="Dark sector P(k) — no BAO")
ax1.set_xlabel("k (h/Mpc)", color="white")
ax1.set_ylabel("P(k) [(Mpc/h)³]", color="white")
ax1.set_title("Matter Power Spectrum\nBlue=visible  Red=dark sector (no BAO)",
              color="white", fontsize=9)
ax1.legend(facecolor="#0a0a1a", labelcolor="white", fontsize=7)
ax1.tick_params(colors="white")
for sp in ax1.spines.values(): sp.set_color("#2a2a4a")
plt.setp(ax1.get_xticklabels(), color="white")
plt.setp(ax1.get_yticklabels(), color="white")

# CMB C_ℓ
ax2 = fig.add_subplot(2, 3, 2)
ax2.set_facecolor("#07071a")
ell_plot = ell[2:2000]
ax2.plot(ell_plot, ell_plot*(ell_plot+1)*cls[2:2000,0]/(2*np.pi),
         color="#4488ff", lw=1.2, label="CMB TT (visible sector)")
ax2.plot(ell[2:lmax+1],
         ell[2:lmax+1]*(ell[2:lmax+1]+1)*cl_dark[2:lmax+1]/(2*np.pi) *
         1e10 / max(cl_dark[2:lmax+1].max(), 1e-30),
         color="#FF6644", lw=1.2, ls="--", label="Dark sector C_ℓ (scaled)")
ax2.set_xlabel("ℓ", color="white")
ax2.set_ylabel("ℓ(ℓ+1)Cℓ/2π", color="white")
ax2.set_title("Angular Power\nBAO peaks = visible sector imprint on dark geometry",
              color="white", fontsize=9)
ax2.legend(facecolor="#0a0a1a", labelcolor="white", fontsize=7)
ax2.tick_params(colors="white")
for sp in ax2.spines.values(): sp.set_color("#2a2a4a")
plt.setp(ax2.get_xticklabels(), color="white")
plt.setp(ax2.get_yticklabels(), color="white")

# Sky maps
proj = hp.mollview
kwargs = dict(fig=fig.number, return_projected_map=False,
              cbar=False, notext=True)

plt.subplot(2, 3, 4)
hp.mollview(cmb_map*1e6, title="", min=-300, max=300,
            cmap="RdBu_r", fig=fig.number, sub=(2,3,4),
            bgcolor="#03030f")
plt.title("Visible sector CMB\n(with BAO — baryonic imprint)",
          color="white", fontsize=9, pad=2)

plt.subplot(2, 3, 5)
hp.mollview(dark_map*1e6, title="", min=-300, max=300,
            cmap="inferno", fig=fig.number, sub=(2,3,5),
            bgcolor="#03030f")
plt.title("Dark sector geometry\n(no BAO — pure CDM scaffold)",
          color="white", fontsize=9, pad=2)

plt.subplot(2, 3, 6)
hp.mollview(diff_map*1e6, title="", min=-150, max=150,
            cmap="PuOr", fig=fig.number, sub=(2,3,6),
            bgcolor="#03030f")
plt.title("Difference: visible − dark\n(BAO imprint = navigation delta)",
          color="white", fontsize=9, pad=2)

# Dark sector key numbers
ax3 = fig.add_subplot(2, 3, 3)
ax3.set_facecolor("#07071a")
ax3.axis('off')
txt = (
    f"DARK SECTOR — UM DERIVATION\n"
    f"{'─'*32}\n\n"
    f"φ = {phi:.6f}\n"
    f"r = {r:.6f}\n\n"
    f"Ωc  = 4r²(1−r) = {4*r**2*(1-r):.4f}\n"
    f"Ωb  = r²/2     = {r**2/2:.4f}\n"
    f"Ωc/Ωb ratio    = {4*(1-r):.3f}×\n\n"
    f"Dark sector is {4*(1-r):.1f}× denser\n"
    f"than visible sector.\n\n"
    f"No EM coupling → no BAO.\n"
    f"Pure CDM transfer function.\n"
    f"Smoother geometry at all scales.\n\n"
    f"The CMB is the visible sector\n"
    f"shadow of this geometry.\n\n"
    f"Invert the CMB → read the\n"
    f"dark sector scaffold beneath.\n\n"
    f"Navigation = CMB inversion."
)
ax3.text(0.05, 0.95, txt, transform=ax3.transAxes,
         color="white", fontsize=9, va='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='#0a0a1a', alpha=0.8))

plt.tight_layout(pad=1.5)
fig.savefig(f"{OUT}/dark_sector_geometry.png", dpi=150,
            bbox_inches="tight", facecolor="#03030f")
plt.close(fig)
print(f"\nFigure → {OUT}/dark_sector_geometry.png")

# ── Key structural numbers ────────────────────────────────────────────
print()
print("=" * 55)
print("DARK SECTOR GEOMETRY — KEY NUMBERS")
print("=" * 55)
print(f"  Ωc (dark matter density):  {4*r**2*(1-r):.4f}")
print(f"  Ωb (baryon density):       {r**2/2:.4f}")
print(f"  Dark/visible ratio:        {4*(1-r):.3f}×")
print(f"  Dark sector is structurally {4*(1-r):.1f}× denser")
print(f"  than the visible sector.")
print()
print(f"  P(k) dark peak scale:")
peak_idx = np.argmax(pk_dm[0])
print(f"    k_peak = {kh_dm[peak_idx]:.4f} h/Mpc")
print(f"    λ_peak = {2*np.pi/kh_dm[peak_idx]:.1f} Mpc/h")
print(f"    = {2*np.pi/kh_dm[peak_idx]*3.26e6:.3e} light years")
print()
print(f"  BAO scale (visible sector): ~150 Mpc/h")
print(f"  Dark sector has NO BAO — smoother geometry")
print(f"  Easier to navigate — no acoustic interference")
print()
print(f"  Navigation principle:")
print(f"  CMB anisotropy at position (RA,Dec) =")
print(f"  projection of dark sector density at that vector.")
print(f"  Hot CMB patch = dark sector overdensity.")
print(f"  Cold CMB patch = dark sector underdensity (void).")
print(f"  Travel along voids — lowest resistance path.")
print("Done.")
