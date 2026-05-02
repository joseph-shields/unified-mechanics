"""
Render a 4K CMB sky map from UM-derived inputs via LiMB/CAMB.
Output: tests/figures/07_cmb_sky_4k.png  (3840×2160)
"""
from __future__ import annotations

import sys, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import healpy as hp

_HERE   = os.path.dirname(os.path.abspath(__file__))
_V2     = os.path.dirname(_HERE)
_OSIRIS = "/mnt/Data/Science/OSIRIS"
for p in (_V2, _OSIRIS):
    if p not in sys.path:
        sys.path.insert(0, p)

from limb.camb_backend import build_camb_params

# ── Planck-style colormap with boosted luminance/saturation ──────────────────
def _planck_cmap():
    from matplotlib.colors import LinearSegmentedColormap
    import colorsys

    raw = [
        (0.000, "#0A0A6E"),
        (0.120, "#1244A8"),
        (0.230, "#1E7FD8"),
        (0.340, "#50BBEE"),
        (0.440, "#AAE0F8"),
        (0.500, "#FAFAF8"),   # zero — bright white
        (0.560, "#FDEEA0"),
        (0.670, "#FBAA20"),
        (0.780, "#E84800"),
        (0.900, "#9A1000"),
        (1.000, "#3A0000"),
    ]

    def boost(hex_col, sat_scale=1.25, val_scale=1.08):
        r, g, b = matplotlib.colors.to_rgb(hex_col)
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        s = min(1.0, s * sat_scale)
        v = min(1.0, v * val_scale)
        return colorsys.hsv_to_rgb(h, s, v)

    positions = [c[0] for c in raw]
    colours   = [boost(c[1]) for c in raw]
    return LinearSegmentedColormap.from_list(
        "planck_vivid", list(zip(positions, colours)), N=1024
    )

PLANCK_CMAP = _planck_cmap()

# ── forward solve ─────────────────────────────────────────────────────────────
LMAX = 8000
print(f"LiMB/CAMB forward solve (lmax={LMAX}) …")
import camb
pars    = build_camb_params(lmax=LMAX, lens_potential_accuracy=1)
results = camb.get_results(pars)
powers  = results.get_cmb_power_spectra(pars, lmax=LMAX, CMB_unit="muK")
total   = np.asarray(powers["total"])
ells    = np.arange(total.shape[0])

# D_ℓ → C_ℓ
factor          = np.zeros_like(ells, dtype=float)
factor[ells>=2] = 2*np.pi / (ells[ells>=2] * (ells[ells>=2]+1))
cl_TT = total[:,0] * factor
cl_EE = total[:,1] * factor
cl_BB = total[:,2] * factor
cl_TE = total[:,3] * factor

# ── sky realization ───────────────────────────────────────────────────────────
NSIDE = 4096
print(f"Synthesising sky (nside={NSIDE}, lmax={LMAX}) …")
np.random.seed(20260430)
cmb_map = hp.synfast([cl_TT, cl_EE, cl_BB, cl_TE],
                      nside=NSIDE, lmax=LMAX, new=True, pol=True)
T_map = cmb_map[0]

# ── render via healpy mollview at 4K DPI ─────────────────────────────────────
# healpy creates an (8.5 × 5.4) inch figure; 451 DPI → ~3834px wide
print("Rendering 4K …")
DPI = 451
plt.close("all")

hp.mollview(T_map,
            title=r"UM-derived CMB sky  —  simulated realization from $c^2 = c + 1$  (not the Planck sky)",
            unit=r"$\delta T$ ($\mu$K)",
            cmap=PLANCK_CMAP, min=-500, max=500,
            cbar=True)
hp.graticule(dpar=30, dmer=60, color="white", alpha=0.15, linewidth=0.4)

fig = plt.gcf()
fig.set_facecolor("white")
fig.text(0.98, 0.01,
         fr"Joseph Shields · Unified Mechanics · LiMB/CAMB · nside {NSIDE} · lmax {LMAX}",
         ha="right", va="bottom", fontsize=6, alpha=0.45)

out = os.path.join(_HERE, "figures", "07_cmb_sky_4k.png")
fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
plt.close(fig)

from PIL import Image
sz = Image.open(out).size
print(f"Saved → {out}  {sz[0]}×{sz[1]}")
