"""
Render a 4K CMB sky map from UM-derived inputs via LiMB/CAMB.

Outputs: tests/figures/07_cmb_sky_4k.png  (3840 × 2160, Mollweide)
"""
from __future__ import annotations

import sys
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import healpy as hp

# ── path setup ────────────────────────────────────────────────────────────────
_HERE = os.path.dirname(os.path.abspath(__file__))
_V2   = os.path.dirname(_HERE)                            # UNIFIED_MECHANICS_v2/

if _V2 not in sys.path:
    sys.path.insert(0, _V2)

from limb.camb_backend import compute_limb_lcdm_cls
from limb.derivations import lcdm_inputs as D

# ── forward solve ─────────────────────────────────────────────────────────────
print("Running LiMB-CAMB forward solve …")
out   = compute_limb_lcdm_cls(lmax=6000, lens_potential_accuracy=1)
ells  = out["ells"]                    # shape (lmax+1,)
cl_TT = out["totCl_TT"]               # μK²,  shape (lmax+1,)

# healpy synfast wants C_ℓ in the standard dimensionless form (μK²).
lmax_hp = 6000
cl_pad  = np.zeros(lmax_hp + 1)
n_copy  = min(len(cl_TT), lmax_hp + 1)
cl_pad[:n_copy] = cl_TT[:n_copy]

# ── sky realization ───────────────────────────────────────────────────────────
print("Synthesising sky realization (nside=4096) …")
np.random.seed(42)                     # reproducible
nside = 4096                           # ~0.86 arcmin pixels, matches lmax 6000
sky   = hp.synfast(cl_pad, nside=nside, lmax=lmax_hp, verbose=False)

# ── render ────────────────────────────────────────────────────────────────────
print("Rendering 4K Mollweide projection …")
vmin, vmax = np.percentile(sky, [0.5, 99.5])

plt.close("all")

# healpy mollview always creates an (8.5 × 5.4) figure internally.
# Save at 451 DPI → 3834 × 2435 px (4K-class resolution).
DPI = 451

hp.mollview(
    sky,
    title="",
    unit=r"$\Delta T\ (\mu\mathrm{K})$",
    min=vmin, max=vmax,
    cmap="RdBu_r",
    cbar=True,
    bgcolor="black",
    notext=True,
)

fig = plt.gcf()
fig.set_facecolor("black")
for ax in fig.axes:
    ax.set_facecolor("black")

fig.text(
    0.98, 0.02,
    r"Unified Mechanics  ·  $c^2 = c + 1$  →  $\varphi$  →  LiMB / CAMB  ·  nside 4096  ·  lmax 6000",
    ha="right", va="bottom",
    color="white", fontsize=6, alpha=0.7,
    fontfamily="monospace",
)

out_path = os.path.join(_HERE, "figures", "07_cmb_sky_4k.png")
fig.savefig(out_path, dpi=DPI, bbox_inches="tight",
            facecolor="black", pad_inches=0.05)
plt.close(fig)
w = int(3834)   # approx at 451 dpi × 8.5 in
print(f"Saved → {out_path}  (~{w}px wide, 4K-class)")
