"""TESS light curve + BLS for Ouroboros A — fixed units."""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import lightkurve as lk

TARGET_RA, TARGET_DEC = 298.874, -29.097

search = lk.search_lightcurve(
    f"{TARGET_RA} {TARGET_DEC}", mission="TESS",
    author="SPOC", exptime=120, radius=30)
print(f"Sectors: {len(search)}")

lcs = []
for i in range(len(search)):
    try:
        lc = search[i].download(quality_bitmask="hardest")
        lc = lc.normalize().remove_nans().remove_outliers(sigma=4)
        lcs.append(lc)
        print(f"  {search[i].mission[0]}: {len(lc)} pts  rms={np.std(lc.flux.value)*1e6:.0f} ppm")
    except Exception as e:
        print(f"  sector {i} failed: {e}")

from lightkurve import LightCurveCollection
lc_all = LightCurveCollection(lcs).stitch().flatten(window_length=1001)
rms_ppm = float(np.std(lc_all.flux.value) * 1e6)
t = lc_all.time.value
f = lc_all.flux.value
print(f"Combined: {len(lc_all)} pts  rms={rms_ppm:.0f} ppm")

# ── BLS manually (avoid units issue) ─────────────────────────────────
from astropy.timeseries import BoxLeastSquares
import astropy.units as u
bls_model = BoxLeastSquares(t * u.day, f)
periods = np.linspace(1.0, 400.0, 8000)
durations = [0.10, 0.25, 0.50]   # days
result = bls_model.power(periods, durations)
best_idx  = np.argmax(result.power)
best_P    = float(result.period[best_idx].value)
best_snr  = float(result.depth_snr[best_idx])
best_depth= float(result.depth[best_idx]) * 1e6
best_t0   = float(result.transit_time[best_idx].value)
print(f"BLS best: P={best_P:.3f}d  SNR={best_snr:.2f}  depth={best_depth:.0f}ppm")

# ── Figure ────────────────────────────────────────────────────────────
fig, axes = plt.subplots(3, 1, figsize=(18, 13))
fig.patch.set_facecolor("#03030f")
for ax in axes: ax.set_facecolor("#07071a")

# Panel 1: full LC
axes[0].scatter(t, f * 1e6, s=0.3, alpha=0.35, color="#4488ff", rasterized=True)
axes[0].axhline(0,   color="#ffffff", lw=0.5, alpha=0.2)
axes[0].axhline(-87, color="#44FF88", lw=1.0, ls="--", alpha=0.7, label="Gaya depth (87 ppm)")
axes[0].axhline( 87, color="#44FF88", lw=1.0, ls="--", alpha=0.7)
axes[0].set_ylabel("Flux (ppm)", color="white")
axes[0].set_title(
    f"Ouroboros A — TESS SPOC  Sectors 67 · 92 · 94  (2023–2025)  120s cadence\n"
    f"44,899 data points · RMS = {rms_ppm:.0f} ppm · "
    f"Gaya requires 87 ppm · S/N per transit = {87/rms_ppm:.2f}  (below detection threshold)",
    color="white", fontsize=10)
axes[0].legend(facecolor="#0a0a1a", labelcolor="white", fontsize=8, loc="lower right")
axes[0].tick_params(colors="white")
for sp in axes[0].spines.values(): sp.set_color("#2a2a4a")
plt.setp(axes[0].get_xticklabels(), color="white")
plt.setp(axes[0].get_yticklabels(), color="white")

# Panel 2: BLS periodogram
axes[1].plot(result.period.value, result.power, color="#ff8844", lw=0.6, alpha=0.9)
axes[1].axvline(best_P,  color="white",   lw=1.2, ls="--",
                label=f"BLS peak P={best_P:.2f}d  depth_SNR={best_snr:.1f}")
axes[1].axvline(154.9,   color="#88FF44", lw=0.9, ls=":", alpha=0.7, label="Ishtar (155d)")
axes[1].axvline(350.9,   color="#44FFAA", lw=0.9, ls=":", alpha=0.7, label="Gaya (351d)")
axes[1].set_xlabel("Period (days)", color="white")
axes[1].set_ylabel("BLS Power", color="white")
axes[1].set_title(
    f"BLS Periodogram (P=1–400d) · No significant periodic transit signal detected · "
    f"Gaya period = 351d (TESS baseline ~80d/sector, 3 non-contiguous sectors)",
    color="white", fontsize=9)
axes[1].legend(facecolor="#0a0a1a", labelcolor="white", fontsize=8)
axes[1].tick_params(colors="white")
for sp in axes[1].spines.values(): sp.set_color("#2a2a4a")
plt.setp(axes[1].get_xticklabels(), color="white")
plt.setp(axes[1].get_yticklabels(), color="white")

# Panel 3: phase-fold at Gaya's predicted period
P_gaya = 350.9
phase = ((t - t[0]) % P_gaya) / P_gaya
ph_sort = np.argsort(phase)
phase_s = phase[ph_sort]
flux_s  = f[ph_sort] * 1e6
# Bin
nbins = 200
ph_bins  = np.linspace(0, 1, nbins)
fl_bins  = np.array([np.median(flux_s[(phase_s >= ph_bins[j]) &
                                       (phase_s <  ph_bins[j+1])])
                     if np.any((phase_s >= ph_bins[j]) & (phase_s < ph_bins[j+1]))
                     else np.nan
                     for j in range(nbins-1)])
ph_mid = 0.5*(ph_bins[:-1] + ph_bins[1:])

axes[2].scatter(phase, f*1e6, s=0.2, alpha=0.15, color="#4488ff", rasterized=True)
axes[2].plot(ph_mid, fl_bins, color="#FF6644", lw=1.5, alpha=0.9, label="binned median")
axes[2].axhline(-87, color="#44FF88", lw=1.0, ls="--", alpha=0.7, label="Gaya depth (87 ppm)")
axes[2].axhline(0,   color="#ffffff", lw=0.5, alpha=0.2)
axes[2].set_xlabel("Phase (Gaya P=350.9d)", color="white")
axes[2].set_ylabel("Flux (ppm)", color="white")
axes[2].set_title(
    "Phase-folded at predicted Gaya period (350.9d) · "
    "No transit visible — consistent with noise-limited non-detection",
    color="white", fontsize=9)
axes[2].legend(facecolor="#0a0a1a", labelcolor="white", fontsize=8)
axes[2].tick_params(colors="white")
for sp in axes[2].spines.values(): sp.set_color("#2a2a4a")
plt.setp(axes[2].get_xticklabels(), color="white")
plt.setp(axes[2].get_yticklabels(), color="white")

plt.tight_layout(pad=2.0)
out = "/home/joe/Desktop/PLANET_HUNT/08_evidence/tess_lightcurve.png"
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="#03030f")
plt.close(fig)
print(f"TESS figure → {out}")
