"""
LiMB demo chain — UM-derived C_ℓ vs Planck 2018 TT bandpowers.

Theory:  LiMB forward solver (zero free cosmological parameters).
Data:    Planck 2018 TT power spectrum  (COM_PowerSpect_CMB-TT-full_R3.01.txt).
Sampler: emcee, 50 000 steps (32 walkers × 1563 steps).
Free:    A_planck — overall calibration/beam nuisance.
         Prior: Gaussian(1.0, σ=0.0025)  [Planck collaboration convention].

If the UM-derived spectrum is correct, the posterior should peak at
A_planck ≈ 1.0 with no adjustment to any cosmological parameter.

Usage:
    python tests/demo_chain.py /path/to/COM_PowerSpect_CMB-TT-full_R3.01.txt

Output written to tests/data/demo_chain/
"""
from __future__ import annotations
import sys, os, json, time
import numpy as np

# ── make the cloned repo importable ──────────────────────────────────────────
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from limb import compute_limb_lcdm_cls

# ── load Planck TT bandpowers ─────────────────────────────────────────────────
PLANCK_FILE = sys.argv[1] if len(sys.argv) > 1 else \
    "/mnt/Data/Science/DGF/research/data/COM_PowerSpect_CMB-TT-full_R3.01.txt"

data = np.loadtxt(PLANCK_FILE, comments="#")
ell_d  = data[:, 0].astype(int)
Dl_d   = data[:, 1]          # D_ℓ = ℓ(ℓ+1)Cℓ/2π  in μK²
err_lo = data[:, 2]
err_hi = data[:, 3]
sigma  = 0.5 * (err_lo + err_hi)   # symmetric approximation

# Trim to ℓ ∈ [30, 2500] — the well-calibrated regime
mask  = (ell_d >= 30) & (ell_d <= 2500)
ell_d = ell_d[mask]
Dl_d  = Dl_d[mask]
sigma = sigma[mask]

print(f"Planck TT bandpowers loaded: {len(ell_d)} bins  ℓ ∈ [{ell_d[0]}, {ell_d[-1]}]")

# ── run LiMB forward solver once ─────────────────────────────────────────────
print("Running LiMB forward solver...")
t0  = time.time()
out = compute_limb_lcdm_cls(lmax=2500)
print(f"  Done in {time.time()-t0:.2f} s")

cosmo     = out["cosmo"]
ell_th    = out["ells"]
Dl_th_all = out["totCl_TT"]          # D_ℓ from LiMB, full ℓ range

# Interpolate theory onto Planck bin centres
Dl_th = np.interp(ell_d, ell_th, Dl_th_all)

# Sanity: chi-squared at A_planck = 1.0 before any sampling
chi2_raw = np.sum(((Dl_th - Dl_d) / sigma) ** 2)
ndof     = len(Dl_d) - 1       # 1 free parameter (A_planck)
print(f"\nPre-chain chi² / dof = {chi2_raw:.1f} / {ndof}  = {chi2_raw/ndof:.3f}")

# ── likelihood + prior ───────────────────────────────────────────────────────
A_PLANCK_MU    = 1.0
A_PLANCK_SIGMA = 0.0025

def log_prior(A):
    # Gaussian prior on calibration nuisance
    return -0.5 * ((A - A_PLANCK_MU) / A_PLANCK_SIGMA) ** 2

def log_likelihood(A):
    residuals = (A * Dl_th - Dl_d) / sigma
    return -0.5 * np.dot(residuals, residuals)

def log_posterior(theta):
    A = theta[0]
    if not (0.9 < A < 1.1):
        return -np.inf
    return log_prior(A) + log_likelihood(A)

# ── emcee chain ──────────────────────────────────────────────────────────────
import emcee

N_WALKERS = 32
N_STEPS   = 1563        # 32 × 1563 = 49 996 ≈ 50 000 total samples
N_DIM     = 1

rng     = np.random.default_rng(271828)
p0      = A_PLANCK_MU + 1e-4 * rng.standard_normal((N_WALKERS, N_DIM))
sampler = emcee.EnsembleSampler(N_WALKERS, N_DIM, log_posterior)

print(f"\nRunning emcee: {N_WALKERS} walkers × {N_STEPS} steps "
      f"= {N_WALKERS * N_STEPS:,} total samples")
t0 = time.time()
sampler.run_mcmc(p0, N_STEPS, progress=True)
wall = time.time() - t0
print(f"  Done in {wall:.1f} s")

# ── analysis ─────────────────────────────────────────────────────────────────
BURN_IN  = 200
flat     = sampler.get_chain(discard=BURN_IN, flat=True)   # (N_eff, 1)
A_chain  = flat[:, 0]

A_mean   = float(np.mean(A_chain))
A_std    = float(np.std(A_chain))
A_med    = float(np.median(A_chain))

try:
    tau_ac   = float(sampler.get_autocorr_time(quiet=True)[0])
except Exception:
    tau_ac   = float("nan")

N_eff    = int(len(A_chain) / max(tau_ac, 1)) if not np.isnan(tau_ac) else len(A_chain)
chi2_bf  = float(-2 * log_likelihood(A_mean))

deviation_sigma = abs(A_mean - A_PLANCK_MU) / A_std

print(f"\n── Results ─────────────────────────────────────────────────────")
print(f"  A_planck  = {A_mean:.6f} ± {A_std:.6f}")
print(f"  Median    = {A_med:.6f}")
print(f"  Deviation from 1.0: {deviation_sigma:.2f}σ")
print(f"  χ²(best-fit) / dof = {chi2_bf:.1f} / {ndof} = {chi2_bf/ndof:.3f}")
print(f"  Autocorr time τ    = {tau_ac:.1f} steps")
print(f"  N_eff              = {N_eff:,}")
print(f"  Wall time          = {wall:.1f} s")
print(f"────────────────────────────────────────────────────────────────")

# ── save ─────────────────────────────────────────────────────────────────────
OUT_DIR = os.path.join(_ROOT, "tests", "data", "demo_chain")
os.makedirs(OUT_DIR, exist_ok=True)

np.save(os.path.join(OUT_DIR, "chain.npy"), flat)

um_params = {
    "H0":       cosmo.H0,
    "Omega_b":  cosmo.Omega_b,
    "Omega_c":  cosmo.Omega_c,
    "n_s":      cosmo.n_s,
    "A_s":      cosmo.A_s,
    "tau_reio": cosmo.tau_reio,
    "w0":       cosmo.w0,
    "wa":       cosmo.wa,
    "N_eff":    cosmo.N_eff,
    "m_nu_eV":  cosmo.m_nu_eV,
    "Y_He":     cosmo.Y_He,
}
summary = {
    "description": (
        "emcee chain: LiMB UM-derived C_l vs Planck 2018 TT bandpowers. "
        "Zero free cosmological parameters. Only A_planck (calibration nuisance) sampled."
    ),
    "planck_data":   os.path.basename(PLANCK_FILE),
    "ell_range":     [int(ell_d[0]), int(ell_d[-1])],
    "n_bins":        int(len(ell_d)),
    "n_walkers":     N_WALKERS,
    "n_steps":       N_STEPS,
    "total_samples": N_WALKERS * N_STEPS,
    "burn_in":       BURN_IN,
    "n_eff":         N_eff,
    "autocorr_tau":  round(tau_ac, 2),
    "wall_time_s":   round(wall, 2),
    "A_planck": {
        "mean":    round(A_mean, 8),
        "std":     round(A_std, 8),
        "median":  round(A_med, 8),
        "prior_mu":    A_PLANCK_MU,
        "prior_sigma": A_PLANCK_SIGMA,
        "deviation_from_unity_sigma": round(deviation_sigma, 4),
    },
    "chi2_at_A_mean":     round(chi2_bf, 4),
    "ndof":               ndof,
    "chi2_per_dof":       round(chi2_bf / ndof, 6),
    "chi2_raw_A1":        round(chi2_raw, 4),
    "chi2_raw_A1_per_dof": round(chi2_raw / ndof, 6),
    "um_derived_params":  {k: round(v, 10) for k, v in um_params.items()},
    "limb_version":       "v0.1.0",
    "camb_version":       __import__("camb").__version__,
}

summary_path = os.path.join(OUT_DIR, "demo_chain_summary.json")
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2)

print(f"\nSaved:")
print(f"  {OUT_DIR}/chain.npy")
print(f"  {summary_path}")
