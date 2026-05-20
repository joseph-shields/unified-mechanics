# Unified Mechanics

**Joseph Shields** · 2026

---

**Start here: [`THE_QUESTION.md`](THE_QUESTION.md)**

---

You've got a piece of string. Cut it into a longer piece and a shorter piece. Ask: *what ratio between the two pieces makes the whole string relate to the longer piece the same way the longer piece relates to the shorter piece?*

That gives you one equation — `φ² = φ + 1` — with one positive solution: `φ = (1+√5)/2 ≈ 1.618`. Define `r = 1/(2φ) ≈ 0.309`. From `r` alone, with no fitting:

- Dark energy: `1 − 9r²/2 + 4r³ = 68.8%` (observed 68.5%)
- Hubble tension: `3r³ = 8.85%` (observed ~9%)
- CMB spectral index: `1 − r²/φ² = 0.9635` (observed 0.9649)
- Cosmological constant: `r²⁴¹ ≈ 10⁻¹²²·⁴` (observed `10⁻¹²²·⁰⁴`)

**Full derivation table: [`00_WHAT_THIS_IS.md`](00_WHAT_THIS_IS.md)** · **Plain English: [`START_HERE.md`](START_HERE.md)** · **Common objections: [`FAQ.md`](FAQ.md)**

---

## Three natures

The equation `φ² = φ + 1` has exactly three terms. They correspond to three channels — three modes of recursive propagation that tile all of space without overlap:

| Channel | Weight | Nature |
|---|---|---|
| Light `(1−r)²` | 47.75% | **Exploration** — open propagation, carries information forward |
| Boundary `2r(1−r)` | 42.71% | **Acknowledgement** — the interface between the other two |
| Matter `r²` | 9.55% | **Familiarity** — accumulation, structure that repeats |

These sum to exactly 1. The boundary channel is the cross-term — it cannot be seeded directly. It appears at the interface whenever both other channels are present.

> *"The three natures are not metaphors laid over the mathematics. They are the mathematics, expressed in the only other language available to us."*

What this means in plain language: **[`papers/shared_space.pdf`](papers/shared_space.pdf)**

---

## 20 SM constants — zero free parameters

Every result below is derived from `r = 1/(2φ)`. The noise floor is `ε_floor = r³ ≈ 2.95%` per channel-traversal cycle — a structural cost, not a tolerance. A quantity crossing `n` channels accumulates `n × ε_floor`. **All 20 are within floor.**

| Observable | Formula | UM value | Observed | Error | n×ε |
|---|---|---|---|---|---|
| **Fine structure** `1/α` | `φ¹⁰+φ⁵+φ²+φ⁻²` | 137.082 | 137.036 | +0.034% | 0.01 |
| **sin²θ_W** | `r / [2(1−r)]` | 0.2250 | 0.2229 | +0.32% | 0.11 |
| **m_p / m_e** | `φ¹⁵(1+r)(1+r³)` | 1838.0 | 1836.2 | +0.11% | 0.04 |
| **α_s(M_Z)** | `r²(1+r−r²)` | 0.1159 | 0.1179 | −1.71% | 0.58 |
| **m_d / m_u** | `√(W_B / W_M)` | 2.115 | 2.162 | −2.2% | 0.74 |
| **δ_CP** | `arccos(W_B)` | 1.1296 rad | 1.14±0.13 | −0.92% | 0.31 |
| **λ = \|V_us\|** | `1 / φ³` | 0.23607 | 0.22452 | +5.15% | 1.75 |
| **\|V_cb\|** | `W_B × W_M` | 0.04078 | 0.04113 | −0.85% | 0.14 |
| **m_ν3** | `m_e(1+r) / φ³⁴` | 52.5 meV | ~50 meV | +4.9% | 1.66 |
| **m_ν2** | `m_e(1+r) / φ³⁸` | 7.65 meV | ~8.6 meV | −11.0% | 3.73 |
| **Σm_ν** | sum | 60 meV | ≤120 meV | — | within bound |
| **η_B** | `r¹⁸` | 6.60×10⁻¹⁰ | 6.10×10⁻¹⁰ | +8.2% | 2.77 |
| **Λ / M_Pl⁴** | `r²⁴¹` | 1.22×10⁻¹²³ | 1.16×10⁻¹²³ | +5.5% | 1.86 |
| **M_GUT** | `M_Pl · φ⁻¹⁴` | 1.45×10¹⁶ GeV | ~2×10¹⁶ GeV | — | within band |
| **Δa_μ (HVP)** | `ε_floor × a_μ^HVP` | 2.05×10⁻⁹ | 2.51×10⁻⁹ | — | — |
| **Immirzi γ** | `1 / φ³` | 0.2361 | 0.2375 | −0.6% | 0.20 |
| **Ω_DM** | `4r²(1−r)` | 0.2639 | 0.2647 | −0.3% | 0.10 |
| **w₀** | derived | −0.934 | −0.93 | −0.43% | 0.15 |
| **Hubble tension** | `3r³`, n=3 | 8.85% | ~9% | +6.5% | 0.74 |
| **Strange quark** | `φ¹²mₑ√W_B` | 107.5 MeV | ~93 MeV | +15.1% | 0.43 |

`W_B = 2r(1−r)` · `W_M = r²`

**Full addendum: [`papers/extended/addendum_closed_results.pdf`](papers/extended/addendum_closed_results.pdf)**

---

## 101 observables — cosmological validation

Paper 8 runs UM against 101 observables across Planck, DESI DR2, BOSS, KiDS, DES, Pantheon+, BBN, and cosmic chronometers. 92/101 PASS. The 9 fails are concentrated in the Pantheon+ low-z distance moduli — a known H₀-anchor tension that is itself a target of Paper 2's braiding derivation.

**Paper 8: [`08_EMPIRICAL_VALIDATION.md`](08_EMPIRICAL_VALIDATION.md)**

The noise floor makes UM falsifiable in a precise sense: any n≥1 quantity agreeing with observation *below* n×ε_floor would falsify the framework, not confirm it.

---

## LiMB — the solver

`limb/` contains **LiMB** *(Light instigating Matter Barrier)*, the UM-derived CAMB-backend solver.
Every cosmological input to CAMB is a closed-form function of `r`; nothing is fitted.

**Install:**

```bash
pip install camb numpy
git clone https://github.com/joseph-shields/unified-mechanics.git
cd unified-mechanics
pip install -e .
```

**Quickstart:**

```python
from limb import compute_limb_lcdm_cls, planck_lcdm_reference_cls
import numpy as np

um     = compute_limb_lcdm_cls(lmax=2500)
planck = planck_lcdm_reference_cls(lmax=2500)

ell      = um["ells"]
residual = (um["totCl_TT"] - planck["totCl_TT"]) / planck["totCl_TT"]
print(f"Peak residual vs Planck best-fit: {np.abs(residual[2:]).max()*100:.2f}%")
```

Or from the command line:

```bash
limb-run          # lmax=2500
limb-run 100000   # push to ℓ=100000
```

**Pipeline:** `derivations` → `Cosmology` → `CAMBparams` → C_ℓ

```
limb/
├── camb_backend.py      # forward solver — cosmology_to_camb_params(), compute_limb_lcdm_cls()
├── cosmology.py         # frozen parameter container — one object, all CAMB inputs
├── lcdm.py              # build_LiMBLCDMCosmology() — every field derived from r
├── um.py                # LiMB-UM — L+M+B source extension (trivial-channel limit for now)
├── channels/            # L (light), M (matter), B (barrier) source-function stubs
├── derivations/
│   └── lcdm_inputs.py   # every closed-form derivation, source-cited to the papers
├── pyproject.toml       # pip install — camb + numpy only
└── LICENSE              # LGPL v3+
```

> **Note on `channels/`:** source terms return zero by design — this is the trivial-channel limit (UM → GR). UM's derivations here come entirely from the r-only closed-form inputs to CAMB, not from modified perturbation terms. A Planck ΛCDM reference run is included in `camb_backend.py` for direct comparison. Full three-channel perturbation solver (JAX) is next.

**Tests:** `pytest tests/test_limb_derivations.py` — 32 pinned derivation tests.

---

## Demo chain

50,016-step emcee chain — LiMB C_ℓ vs Planck 2018 TT bandpowers, run from a fresh clone:

| | |
|---|---|
| Free parameters | 1 (A_planck — overall calibration nuisance) |
| Fixed cosmological parameters | 10 (all UM-derived) |
| A_planck posterior | 1.0067 ± 0.0012 (0.67% from unity — within ε_floor) |
| χ²/dof | 1.343 (2471 bins, ℓ ∈ [30, 2500]) |
| N_eff | 1,688 independent samples |
| Wall time | 0.6 s |

Chain: `tests/data/demo_chain/` · Script: `tests/demo_chain.py`

---

## CMB power spectrum

<p align="center">
  <img src="research/figures/08a_cmb_sphere_1.png" width="46%" alt="UM-derived CMB sphere — Eridanus supervoid realization"/>
  &nbsp;&nbsp;
  <img src="research/figures/08c_cmb_sphere_3.png" width="46%" alt="UM-derived CMB sphere — independent realization"/>
</p>

*Orthographic sphere renders at lmax 20000. The dark blue region in the first sphere is the simulated **Eridanus supervoid** — a ~−150 µK cold patch at RA 150°, Dec −57°. Both are independent realizations drawn from the same UM-derived power spectrum.*

<p align="center">
  <img src="research/figures/07b_cmb_sky_4k_seed_e.png" width="96%" alt="UM-derived CMB full sky — Mollweide projection"/>
</p>

*Full-sky Mollweide projection (nside 4096, lmax 8000). Produced by `research/render_cmb_4k.py` — reproducible, ~60 s on a consumer CPU.*

---

## Falsification roadmap

| Test | Timing | What falsifies UM |
|---|---|---|
| **Phase 0 — Born rule** at Hf-178m2 | $2.5M / 18 months | Null at 13.6 ppm sensitivity |
| **Euclid 2026** dark-energy | Late 2026 | w₀, wₐ outside (−0.934, +0.091) ± floor |
| **DESI Year 5/7** neutrino bound | 2027–2030 | Σmν < 0.05 eV |
| **LISA + PTA** SGWB ratio | Mid-2030s | I_CMB/I_SGWB outside 1.118 ± 10% |
| **Direct DM-photon coupling** | Ongoing | Any positive signal |

---

## Papers

### Main series

| Paper | Topic |
|---|---|
| [`01_FOUNDATION.md`](01_FOUNDATION.md) | The axiom, three channels, empirical origin of the 70/25/5 composition |
| [`02_COSMOLOGY.md`](02_COSMOLOGY.md) | H₀, dark energy, Hubble tension, CMB C_ℓ — all from r |
| [`03_GRAVITY_AND_BLACK_HOLES.md`](03_GRAVITY_AND_BLACK_HOLES.md) | WEP derivation, Page curve, black hole information, ER=EPR |
| [`04_QUANTUM_AND_HOLOGRAPHIC.md`](04_QUANTUM_AND_HOLOGRAPHIC.md) | Born rule, holography, entanglement as boundary channel |
| [`05_PARTICLE_PHYSICS.md`](05_PARTICLE_PHYSICS.md) | Lepton ratios, quark masses, gauge coupling running, Strong CP |
| [`06_HETEROTIC_IDENTIFICATION.md`](06_HETEROTIC_IDENTIFICATION.md) | G₂ holonomy, heterotic E₈×E₈, (G₂)₁ ⊂ (E₈)₁ embedding |
| [`07_EXPERIMENTAL_PROGRAM.md`](07_EXPERIMENTAL_PROGRAM.md) | Testable predictions, pre-registration, experimental roadmap |
| [`08_EMPIRICAL_VALIDATION.md`](08_EMPIRICAL_VALIDATION.md) | 101 observables — 92 PASS across Planck, DESI, BOSS, KiDS, DES |

### Focused derivations (`papers/`)

| Paper | Key result |
|---|---|
| [`alpha_em_g2`](papers/alpha_em_g2.pdf) | `1/α = φ¹⁰+φ⁵+φ²+φ⁻² = 137.082` — most precise UM result (+0.034%) |
| [`electroweak_baryon`](papers/electroweak_baryon.pdf) | `sin²θ_W = r/[2(1−r)]` · `m_p/m_e = φ¹⁵(1+r)(1+r³)` |
| [`qcd_running`](papers/qcd_running.pdf) | `α_s(M_Z) = r²(1+r−r²)` · quark mass ratios via φ⁴ colour cycle |
| [`ckm_mixing`](papers/ckm_mixing.pdf) | `δ_CP = arccos(W_B)` — CP violation IS the boundary channel weight |
| [`neutrino_masses`](papers/neutrino_masses.pdf) | `m_ν3 = m_e(1+r)/φ³⁴` · `m_ν2 = m_e(1+r)/φ³⁸` |
| [`matter_antimatter`](papers/matter_antimatter.pdf) | `η_B = r¹⁸` — three Sakharov conditions = three channel crossings |
| [`cosm_constant`](papers/cosm_constant.pdf) | `Λ/M_Pl⁴ = r²⁴¹` — the 10¹²³ problem in one line |
| [`gauge_unification`](papers/gauge_unification.pdf) | All three SM gauge couplings from one axiom · M_GUT = M_Pl·φ⁻¹⁴ |
| [`muon_g2`](papers/muon_g2.pdf) | HVP anomaly bounded by ε_floor — Δa_μ ≈ 2.05×10⁻⁹ |
| [`shared_space`](papers/shared_space.pdf) | The three natures in plain English — no equations except the final table |
| [`addendum_closed_results`](papers/extended/addendum_closed_results.pdf) | 20 observables · 20/20 within floor · zero free parameters |

---

## MCMC chains

All cosmological parameters fixed by derivation — sampler runs on nuisance only. Full cobaya runs with hi_class/EFTCAMB backend across Planck + DESI DR2 + BOSS fσ8:

| Run | Data | Steps to R-1 < 0.01 | Wall time |
|---|---|---|---|
| A | Planck TTTEEE + lowl | 520 | 3.4 s |
| B | Planck + DESI DR2 BAO | 560 | 9.0 s |
| C | Planck + BAO + BOSS fσ8 | 1000 | 8.3 s |
| H | Planck + BAO + BOSS fσ8 (alt seed) | 1040 | 7.9 s |
| I | Planck + BAO + fσ8 + H_tension | 2400 | 6.6 s |

Runs C and H — same likelihoods, independent seeds — produce identical best-fit χ². Chain files: `tests/data/chains/`.

---

## Reproducibility

| | |
|---|---|
| `tests/data/` | 98-observable test suite, Bayes analysis, chain summaries |
| `tests/data/chains/` | Full cobaya MCMC outputs — Planck, DESI, BOSS, hi_class |
| `research/planet_hunt/` | CMB temperature hunt through Planck SMICA → 1,287 Gaia targets |
| `research/recursion_floor/` | MCMC R-1 clustering at exact powers of R = 1/(2φ) |
| `research/dgf/PROGRAMME_PAPER.md` | Full empirical programme with chain configs |
| `PRE_REGISTRATION.md` | Derivations locked before observations |

---

## CMB-Guided Planet Hunt

`research/planet_hunt/` applies UM's cosmological framework to exoplanet targeting. CMB temperature at any sky position is the fossil record of the primordial density perturbation that seeded structure formation there — regions with the same temperature as Earth's neighbourhood formed under the same initial conditions.

**Results:** 575 matched CMB patches · **1,287 unstudied Gaia G-stars** · Top target at 51 pc, G=8.3, ESPRESSO-accessible now.

<p align="center">
  <img src="research/planet_hunt/00_earth_reference/cmb_fullsky.png" width="96%" alt="Full-sky CMB — Earth seed patches marked"/>
</p>

<p align="center">
  <img src="research/planet_hunt/04_skypy_lss/skypy_highl_patches.png" width="96%" alt="Matter overdensity in top-12 CMB seed patches"/>
</p>

Full pipeline and Gaia catalogue: `research/planet_hunt/README.md`

---

## Citation

```
Shields, J. (2026). Unified Mechanics: A Single-Axiom Framework
for Cosmology, Gravity, and Quantum Mechanics.
```
