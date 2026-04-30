# UM everything-at-once test suite — results

- framework: c² = c + 1
- ε_floor = r³ ≈ 2.9508% per channel-traversal cycle
- total tests: 98 | PASS: 77 | FAIL: 9 | SUB-FLOOR: 12

| observable | UM | observed | Δ | n | status |
| --- | ---: | ---: | ---: | :-: | :-: |
| Born coefficient  1/φ | 0.618034 | 0.618034 | 8.1e-11 | 0 | EXACT |
| Born leakage      1/φ² | 0.381966 | 0.381966 | 1.3e-10 | 0 | EXACT |
| ε_floor = r³ | 0.0295085 | 0.0295085 | 4.2e-10 | 0 | EXACT |
| Hubble braiding 3r³ | 0.0885255 | 0.0885255 | 7.1e-10 | 0 | EXACT |
| channel weight light  (1-r)² | 0.477458 | 0.477458 | 7.8e-11 | 0 | EXACT |
| channel weight bound. 2r(1-r) | 0.427051 | 0.427051 | 5.8e-11 | 0 | EXACT |
| channel weight matter r² | 0.0954915 | 0.0954915 | 1.3e-10 | 0 | EXACT |
| Σ channels = 1 | 1 | 1 | 0.0e+00 | 0 | EXACT |
| E₈ root count | 240 | 240 | 0.0e+00 | 0 | EXACT |
| Pisano period of 241 | 240 | 240 | 0.0e+00 | 0 | EXACT |
| cosmic-web fractal D | 2.22361 | 2.224 | 1.8e-04 | 0 | MISMATCH |
| SGWB-CMB info ratio φ-1/2 | 1.11803 | 1.118 | 3.0e-05 | 0 | MISMATCH |
| lepton ratio  m_μ / m_e | 204.88 | 206.77 | -0.91% | 0 | PASS |
| lepton ratio  m_τ / m_μ | 16.916 | 16.817 | +0.59% | 0 | PASS |
| lepton ratio  m_τ / m_e | 3465.6 | 3477.2 | -0.33% | 0 | PASS |
| Higgs/Planck (log10) | -16.991 | -16.99 | -0.01% | 0 | PASS |
| Ω_b | 0.047746 | 0.0493 | -3.15% | 0 | PASS |
| Ω_c (DM) | 0.26393 | 0.265 | -0.40% | 0 | PASS |
| Ω_m | 0.31168 | 0.315 | -1.05% | 0 | PASS |
| Ω_DE | 0.68832 | 0.685 | +0.48% | 0 | PASS |
| Σ Ω (closure) | 1 | 1 | 0.0e+00 | 0 | EXACT |
| Ω_k (curvature, UM forces flat) | 0 | 0 | 0.0e+00 | 0 | EXACT |
| w_0 | -0.93402 | -0.93 | -0.43% | 0 | PASS |
| w_a | 0.090519 | 0.091 | -0.53% | 0 | PASS |
| ρ_Λ/M_Pl⁴ (log10) | -122.4 | -122.04 | -0.30% | 0 | PASS |
| H₀_late / H₀_CMB | 1.0926 | 1.0843 | +0.77% | 0 | PASS |
| braiding magnitude (3r³) | 0.088525 | 0.084323 | +4.98% | 1 | PASS |
| G_eff / G_N | 1.0729 | 1.073 | -0.00% | 0 | PASS |
| n_s | 0.96353 | 0.9649 | -0.14% | 0 | PASS |
| A_s | 2.1365e-09 | 2.1e-09 | +1.74% | 0 | PASS |
| running α_s = dn/dlnk | 0 | 0 | 0.0e+00 | 0 | EXACT |
| tensor-to-scalar r | 0 | 0 | 0.0e+00 | 0 | EXACT |
| τ_reio | 0.059017 | 0.054 | +9.29% | 2 | PASS |
| Y_He | 0.23873 | 0.245 | -2.56% | 0 | PASS |
| N_eff | 3.0477 | 3.046 | +0.06% | 0 | PASS |
| z_reio (derived from τ) | 8.5 | [7, 9.5] | — | 0 | WITHIN BOUND |
| D/H × 10⁵ (BBN, Cooke+ 2018) | 2.718 | 2.527 | +7.56% | 2 | PASS |
| Σm_ν within Planck 95% upper | 0.112 | [0.058, 0.12] | — | 0 | WITHIN BOUND |
| Σm_ν within DESI 95% upper | 0.112 | [0.058, 0.072] | — | 0 | VIOLATES BOUND |
| 100·θ_* | 105.34 | 104.11 | +1.18% | 0 | PASS |
| z_* | 1090.5 | 1089.9 | +0.06% | 0 | PASS |
| r_*  (Mpc) | 144.98 | 144.43 | +0.38% | 0 | PASS |
| z_drag | 1058.1 | 1059.9 | -0.17% | 0 | PASS |
| r_drag (Mpc) | 147.88 | 147.09 | +0.53% | 0 | PASS |
| z_eq | 3382.5 | 3402 | -0.57% | 0 | PASS |
| k_eq (Mpc⁻¹) | 0.010326 | 0.010384 | -0.55% | 0 | PASS |
| θ_d (damping scale) | 0.16332 | 0.16075 | +1.60% | 0 | PASS |
| CMB TT median residual | 0.0315 | ≤0.0531 | 3.15% | 1 | PASS  (≤5.3%) |
| CMB EE median residual | 0.0704 | ≤0.1062 | 7.04% | 2 | PASS  (≤10.6%) |
| CMB TT  ℓ=220 (1st peak) [μK²] | 5731.8 | 5732.9 | -0.02% | 1 | SUB-FLOOR |
| CMB TT  ℓ=540 (2nd peak) [μK²] | 2630.8 | 2592.5 | +1.48% | 1 | PASS |
| CMB TT  ℓ=810 (3rd peak) [μK²] | 2561.1 | 2539.6 | +0.84% | 1 | SUB-FLOOR |
| CMB TT  ℓ=2000 (damping) [μK²] | 231.44 | 231.08 | +0.15% | 2 | SUB-FLOOR |
| CMB TE ℓ=400 (zero-crossing-aware) | -11.6 | -0.44 | 63.42% | 1 | FAIL |
| CMB φφ  ℓ=50 | 1.307e-07 | 1.3417e-07 | -2.58% | 2 | PASS |
| CMB φφ  ℓ=100 | 9.8796e-08 | 1.0167e-07 | -2.83% | 2 | PASS |
| CMB φφ  ℓ=500 | 1.8601e-08 | 1.9284e-08 | -3.54% | 2 | PASS |
| CMB φφ  ℓ=1000 | 6.4402e-09 | 6.7101e-09 | -4.02% | 2 | PASS |
| lensing amplitude A_L  (UM = 1 by construction) | 1 | 1 | 0.0e+00 | 0 | EXACT |
| σ8(z=0) | 0.78923 | 0.811 | -2.68% | 0 | PASS |
| σ8(z=0.5) | 0.61018 | 0.628 | -2.84% | 1 | PASS |
| S₈ vs KiDS-1000 | 0.80445 | 0.766 | +5.02% | 1 | PASS |
| S₈ vs DES-Y3 | 0.80445 | 0.776 | +3.67% | 1 | PASS |
| fσ8(z=0.5)  BOSS RSD | 0.45424 | 0.47 | -3.35% | 1 | PASS |
| fσ8(z=1.0)  eBOSS QSO | 0.41559 | 0.408 | +1.86% | 1 | PASS |
| DESI BGS D_V/r_d at z=0.295 | 7.9281 | 7.93 | -0.02% | 2 | SUB-FLOOR |
| DESI LRG1 D_M/r_d at z=0.51 | 13.266 | 13.62 | -2.60% | 2 | PASS |
| DESI LRG1 D_H/r_d at z=0.51 | 22.164 | 20.98 | +5.65% | 2 | PASS |
| DESI LRG2 D_M/r_d at z=0.706 | 17.355 | 16.85 | +3.00% | 2 | PASS |
| DESI LRG2 D_H/r_d at z=0.706 | 19.627 | 20.08 | -2.26% | 2 | SUB-FLOOR |
| DESI LRG3 D_M/r_d at z=0.93 | 21.465 | 21.71 | -1.13% | 2 | SUB-FLOOR |
| DESI LRG3 D_H/r_d at z=0.93 | 17.139 | 17.88 | -4.14% | 2 | PASS |
| DESI ELG2 D_M/r_d at z=1.317 | 27.409 | 27.79 | -1.37% | 2 | SUB-FLOOR |
| DESI ELG2 D_H/r_d at z=1.317 | 13.752 | 13.82 | -0.49% | 2 | SUB-FLOOR |
| DESI Lyα D_M/r_d at z=2.33 | 38.334 | 39.71 | -3.47% | 2 | PASS |
| DESI Lyα D_H/r_d at z=2.33 | 8.4691 | 8.52 | -0.60% | 2 | SUB-FLOOR |
| H(z=0.07) chronometer [km/s/Mpc] | 70.06 | 69±20 | +0.1σ | 0 | PASS (0.1σ) |
| H(z=0.12) chronometer [km/s/Mpc] | 72.09 | 68.6±26 | +0.1σ | 0 | PASS (0.1σ) |
| H(z=0.2) chronometer [km/s/Mpc] | 75.57 | 72.9±30 | +0.1σ | 0 | PASS (0.1σ) |
| H(z=0.4) chronometer [km/s/Mpc] | 85.41 | 95±17 | -0.6σ | 0 | PASS (0.6σ) |
| H(z=0.48) chronometer [km/s/Mpc] | 89.77 | 97±62 | -0.1σ | 0 | PASS (0.1σ) |
| H(z=0.88) chronometer [km/s/Mpc] | 114.8 | 90±40 | +0.6σ | 0 | PASS (0.6σ) |
| H(z=1.43) chronometer [km/s/Mpc] | 156.6 | 177±18 | -1.1σ | 0 | PASS (1.1σ) |
| H(z=1.75) chronometer [km/s/Mpc] | 184.2 | 202±40 | -0.4σ | 0 | PASS (0.4σ) |
| μ(z=0.05) Pantheon+ | 36.81 | 36.6±0.05 | +4.2σ | 0 | FAIL (4.2σ) |
| μ(z=0.1) Pantheon+ | 38.39 | 38.3±0.04 | +2.2σ | 0 | FAIL (2.2σ) |
| μ(z=0.2) Pantheon+ | 40.02 | 39.9±0.04 | +3.0σ | 0 | FAIL (3.0σ) |
| μ(z=0.4) Pantheon+ | 41.74 | 41.6±0.04 | +3.4σ | 0 | FAIL (3.4σ) |
| μ(z=0.8) Pantheon+ | 43.54 | 43.4±0.06 | +2.3σ | 0 | FAIL (2.3σ) |
| μ(z=1.2) Pantheon+ | 44.62 | 44.5±0.1 | +1.2σ | 0 | PASS (1.2σ) |
| μ(z=1.6) Pantheon+ | 45.38 | 45.2±0.15 | +1.2σ | 0 | PASS (1.2σ) |
| H(z=10.0) ratio LiMB/Planck-bf | 1.0004 | 1 | +0.04% | 1 | SUB-FLOOR |
| H(z=100.0) ratio LiMB/Planck-bf | 0.99894 | 1 | -0.11% | 1 | SUB-FLOOR |
| H(z=1000.0) ratio LiMB/Planck-bf | 0.99823 | 1 | -0.18% | 1 | SUB-FLOOR |
| comoving D to LSS (z=1090) [Mpc] | 13762 | 13873 | -0.79% | 0 | PASS |
| age of universe [Gyr] | 13.612 | 13.797 | -1.34% | 0 | PASS |
| r_drag [Mpc] | 147.88 | 147.05 | +0.56% | 0 | PASS |
| r_*  (sound horizon @ recomb) [Mpc] | 144.98 | 144.43 | +0.38% | 0 | PASS |
