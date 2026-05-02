# Unified Mechanics

**Joseph Shields** · 2026

---

## The axiom

```
c² = c + 1
```

Unique positive fixed point: `φ = (1+√5)/2`. Contraction rate: `r = 1/(2φ) ≈ 0.309`.
From `r` alone, with **zero free parameters**:

| Quantity | UM closed form | Observed | Residual |
|---|---|---|---|
| ρ_Λ / M_Pl⁴ | r²⁴⁰ | 10⁻¹²²·⁰⁴ | 0.4% in log |
| Ω_b | r²/2 | 0.0493 | 3.0% (at floor) |
| Ω_DM | 4r²(1-r) | 0.2647 | 0.3% |
| Ω_DE | 1 − 9r²/2 + 4r³ | 0.685 | 0.5% |
| w₀ | −(r+2)/(8r) | −0.93 (DESI) | within band |
| ΔH₀/H₀ | 3r³ | ~9% | within band |
| G_eff/G_N | 1 + r/(3+4r) | 1.073 (lab G) | structural |
| n_s | 1 − r²/φ² | 0.9649 | 0.15% |
| A_s | r¹⁷ | 2.1×10⁻⁹ | 1.7% |
| Born coupling | 1/φ = 2r | — | exact |
| ε_floor | r³ | 2.95% obs. band | structural |
| m_τ/m_e | φ¹⁷(1−r³) | 3477 (PDG) | 0.33% |

**98-observable test suite:** 88 PASS within n×ε_floor. Structural Bayes ln B = +102 vs ΛCDM, fluke probability ~10⁻⁴⁴.


## Corpus

| paper | content |
|---|---|
| `00_WHAT_THIS_IS.md` | one-page entry point |
| `00_MASTER_HANDOVER.md` | high-level overview, key results table |
| `01_FOUNDATION.md` | axiom, recursion, three-channel decomposition, Lagrangian, noise floor, Born coefficient, E₈ closure, cereal-bowl rule |
| `02_COSMOLOGY.md` | every r-only LCDM closed form: Ω_b, Ω_c, w₀, wₐ, n_s, A_s, τ_reio, Y_He, N_eff, Σmν, ρ_Λ, Hubble braiding |
| `03_GRAVITY_AND_BLACK_HOLES.md` | Bekenstein-Hawking 1/4 derivation, Hawking radiation, ER=EPR consistency, deep planetary cores |
| `04_QUANTUM_AND_HOLOGRAPHIC.md` | Born coupling, holographic encoding, event-routing principle, decoherence, three-channel completion of QM |
| `05_PARTICLE_PHYSICS.md` | lepton hierarchy, Higgs/Planck ratio, lab-scale κ-couplings, SGWB-CMB ratio |
| `06_HETEROTIC_IDENTIFICATION.md` | (G₂)₁ ⊂ (E₈)₁ in heterotic E₈×E₈, dark matter as second E₈, SM emergence, landscape resolved |
| `07_EXPERIMENTAL_PROGRAM.md` | Phase 0 (Born rule, $2.5M, 18 months), four lab predictions, falsification surface, funding pathways |
| `08_EMPIRICAL_VALIDATION.md` | 98-observable test suite, alternate-recursion uniqueness, cereal-bowl weighting, structural Bayes |
| `PRE_REGISTRATION.md` | locked predictions before observations, falsification thresholds |

### DGF derivation record

| file | content |
|---|---|
| `dgf/PROGRAMME_PAPER.md` | *How The Universe Works* — synthesis paper covering the c²=c+1 derivation and full empirical programme |
| `dgf/chain_yamls/` | cobaya chain configs (B, L0, L1, LF, LFP, M, R5v8, T, T2) — the derivation chains behind the cosmological observables |

### LiMB — the solver

`limb/` contains **LiMB** *(Light instigating Matter Barrier)*, the UM-derived CAMB-backend solver.
Every cosmological input to CAMB is a closed-form function of `r`; nothing is fitted.

```
limb/
├── camb_backend.py      # CAMB forward solve with UM-derived inputs
├── lcdm.py              # LiMBLCDMCosmology — trivial-channel limit
├── um.py                # LiMBUMCosmology   — full L+M+B source extension
├── channels/            # L (light), M (matter), B (barrier) source terms
├── derivations/
│   └── lcdm_inputs.py   # every closed-form derivation (r-only)
└── LICENSE              # LGPL v3+
```

The CMB image above was produced by `tests/render_cmb_4k.py` — fully reproducible, ~60 s on CPU.

### Tests and figures

```
tests/
├── data/chains/         # MCMC chain outputs (Planck, DESI, DES Y3, KiDS, joint)
├── figures/             # CMB sky map (4K), power spectra, Hubble braiding, ...
└── render_cmb_4k.py     # reproduce the 4K CMB image
```


## Falsification roadmap

| test | timing | what falsifies UM |
|---|---|---|
| **Phase 0 — Born rule** at Hf-178m2 | $2.5M / 18 months | null at 13.6 ppm sensitivity |
| **Euclid 2026** dark-energy | late 2026 | w₀, wₐ outside (−0.934, +0.091) ± floor |
| **DESI Year 5/7** neutrino bound | 2027–2030 | Σmν < 0.05 eV |
| **LISA + PTA** SGWB ratio | mid-2030s | I_CMB/I_SGWB outside 1.118 ± 10% |
| **Direct DM-photon coupling** | ongoing | any positive signal |


## Citation

```
Shields, J. (2026). Unified Mechanics: A Single-Axiom Framework
for Cosmology, Gravity, and Quantum Mechanics.
```
