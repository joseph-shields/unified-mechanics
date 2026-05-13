"""Find the seed that matches Planck SMICA using chain best-fit UM params."""
import sys, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, "/home/joe/Desktop/UNIFIED_MECHANICS_v2")
sys.path.insert(0, "/mnt/Data/Science/OSIRIS")

import numpy as np
import healpy as hp
import multiprocessing as mp
import time, os
import camb

# ── Chain best-fit parameters (min -loglike from planck_um_chain.txt) ──
H0_bf       = 68.1589
ombh2_bf    = 0.022181
omch2_bf    = 0.122613
tau_bf      = 0.059017
ln10As_bf   = 3.052107
ns_bf       = 0.963526
TCMB_bf     = 2.724948

As_bf = np.exp(ln10As_bf) * 1e-10

print("Chain best-fit parameters:")
print(f"  H0={H0_bf}  ombh2={ombh2_bf}  omch2={omch2_bf}")
print(f"  tau={tau_bf}  As={As_bf:.4e}  ns={ns_bf}")

# ── Build C_l with best-fit params ─────────────────────────────────────
LMAX_SCAN = 48    # NSIDE=16 scan
LMAX_FULL = 3000  # full render

def make_cls(lmax):
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0_bf, ombh2=ombh2_bf, omch2=omch2_bf,
                       tau=tau_bf, TCMB=TCMB_bf)
    pars.InitPower.set_params(As=As_bf, ns=ns_bf)
    pars.set_for_lmax(lmax, lens_potential_accuracy=0)
    res = camb.get_results(pars)
    cls = res.get_cmb_power_spectra(pars, CMB_unit="muK")["total"][:, 0]
    cls[0] = 0.0; cls[1] = 0.0
    return cls[:lmax+1]

Cl_scan = make_cls(LMAX_SCAN)
print(f"C_l built to lmax={LMAX_SCAN}")

# ── Prepare Planck reference at NSIDE=16 ───────────────────────────────
NSIDE_SCAN = 16
print("Loading Planck SMICA…")
planck_raw = hp.read_map(
    "/mnt/Data/Science/data/planck/COM_CMB_IQU-smica_2048_R3.00_full.fits",
    field=0, dtype=np.float64)
planck_raw *= 1e6   # K → µK

rot = hp.Rotator(coord=["G", "C"])
planck_equ = rot.rotate_map_pixel(planck_raw)
planck_16  = hp.ud_grade(planck_equ, NSIDE_SCAN)
planck_16  = hp.remove_dipole(planck_16, verbose=False)

# Galactic plane mask
npix = hp.nside2npix(NSIDE_SCAN)
theta_all, phi_all = hp.pix2ang(NSIDE_SCAN, np.arange(npix))
rot_inv = hp.Rotator(coord=["C", "G"])
theta_g, phi_g = rot_inv(theta_all, phi_all)
b_deg = 90 - np.degrees(theta_g)
mask  = np.abs(b_deg) > 20.0

planck_ref = planck_16[mask].astype(np.float64)
planck_ref -= planck_ref.mean()
print(f"  Planck ref pixels: {mask.sum()}  std={planck_ref.std():.2f} µK")

# ── Shared memory for workers ──────────────────────────────────────────
def _init_worker(cl_arr, ref_arr, mask_arr):
    global _Cl, _ref, _mask
    _Cl   = cl_arr
    _ref  = ref_arr
    _mask = mask_arr

def scan_chunk(args):
    seed_start, seed_end = args
    Cl   = _Cl
    ref  = _ref
    mask = _mask
    nside = NSIDE_SCAN

    best_r    = -2.0
    best_seed = seed_start
    ref_std   = ref.std()

    for seed in range(seed_start, seed_end):
        np.random.seed(seed)
        m = hp.synfast(Cl, nside=nside, lmax=len(Cl)-1, verbose=False)
        m = hp.remove_dipole(m, verbose=False)
        v = m[mask]; v -= v.mean()
        s = v.std()
        if s < 1e-12:
            continue
        r = float(np.dot(v, ref) / (len(ref) * s * ref_std))
        if r > best_r:
            best_r    = r
            best_seed = seed

    return best_seed, best_r


def run_scan(seed_lo, seed_hi, n_workers=8, label=""):
    chunk = (seed_hi - seed_lo) // n_workers
    chunks = [(seed_lo + i*chunk, seed_lo + (i+1)*chunk) for i in range(n_workers)]
    print(f"  Scanning {seed_lo:,}–{seed_hi:,} ({label})…")
    t0 = time.time()
    with mp.Pool(n_workers,
                 initializer=_init_worker,
                 initargs=(Cl_scan, planck_ref, mask)) as pool:
        res = pool.map(scan_chunk, chunks)
    dt = time.time() - t0
    best = max(res, key=lambda x: x[1])
    print(f"    best seed={best[0]}  r={best[1]:.4f}  ({dt:.1f}s)")
    return best


if __name__ == "__main__":
    # ── Stage 1: coarse scan 0–10M ────────────────────────────────────
    best_seed, best_r = run_scan(0, 10_000_000, label="coarse")

    # ── Stage 2: fine scan ±100k around best ─────────────────────────
    lo = max(0, best_seed - 100_000)
    hi = best_seed + 100_000
    fine_seed, fine_r = run_scan(lo, hi, label="fine")
    if fine_r > best_r:
        best_seed, best_r = fine_seed, fine_r

    print(f"\n══ PLANCK SEED: {best_seed}   r = {best_r:.5f} ══")
    np.save("/home/joe/Desktop/PLANET_HUNT/06_planck/planck_best_seed.npy",
            np.array([best_seed, best_r]))

    # ── Render ────────────────────────────────────────────────────────
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("Building full-res render…")
    Cl_full = make_cls(LMAX_FULL)

    NSIDE_RENDER = 512
    np.random.seed(best_seed)
    um_map = hp.synfast(Cl_full, nside=NSIDE_RENDER, lmax=LMAX_FULL, verbose=False)
    um_map = hp.smoothing(um_map, fwhm=np.radians(1.0), verbose=False)
    um_map_gal = hp.Rotator(coord=["C","G"]).rotate_map_pixel(um_map)

    planck_512 = hp.ud_grade(planck_raw, NSIDE_RENDER)
    planck_512 = hp.smoothing(planck_512, fwhm=np.radians(1.0), verbose=False)

    fig = plt.figure(figsize=(20, 8))
    fig.patch.set_facecolor("#050510")

    hp.mollview(planck_512, fig=fig.number, sub=(1,2,1),
                title="", unit="µK", min=-300, max=300,
                cmap="RdBu_r", notext=True)
    plt.gca().set_title("Planck SMICA  (real universe, galactic)",
                        color="#88FFAA", fontsize=11, pad=6)

    hp.mollview(um_map_gal, fig=fig.number, sub=(1,2,2),
                title="", unit="µK", min=-300, max=300,
                cmap="RdBu_r", notext=True)
    plt.gca().set_title(f"UM derivation — seed {best_seed}  r={best_r:.4f}",
                        color="#88FFAA", fontsize=11, pad=6)

    fig.suptitle(
        f"CMB Sky — Planck vs UM (chain best-fit params)\n"
        f"H0={H0_bf:.2f}  ombh2={ombh2_bf:.5f}  omch2={omch2_bf:.5f}  "
        f"ns={ns_bf:.5f}  As={As_bf:.3e}",
        color="white", fontsize=10, y=1.01)

    out = "/home/joe/Desktop/PLANET_HUNT/06_planck/planck_vs_um_seed.png"
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="#050510")
    plt.close(fig)
    print(f"Render → {out}")
    print("Done.")
