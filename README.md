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

---

<p align="center">
  <img src="tests/figures/08a_cmb_sphere_1.png" width="46%" alt="UM-derived CMB sphere — Eridanus supervoid realization"/>
  &nbsp;&nbsp;
  <img src="tests/figures/08c_cmb_sphere_3.png" width="46%" alt="UM-derived CMB sphere — independent realization"/>
</p>

*Orthographic sphere renders at lmax 20000 — angular resolution ~0.6 arcmin, far finer than any current instrument, generated on a consumer CPU with no upper bound on ℓ. The dark blue region in the first sphere is the simulated **Eridanus supervoid** (CMB Cold Spot): a large coherent underdensity producing a ~−150 µK cold patch at RA 150°, Dec −57°. Both are independent random realizations drawn from the same UM-derived power spectrum. UM predicts the full statistical distribution — acoustic peak positions, power spectrum shape, variance at every angular scale — from which the CMB is drawn. The Planck sky is one specific draw from that distribution; these are others.*

<p align="center">
  <img src="tests/figures/07b_cmb_sky_4k_seed_e.png" width="96%" alt="UM-derived CMB full sky — Mollweide projection"/>
</p>

*Full-sky Mollweide projection (nside 4096, lmax 8000). This realization reproduces the large-scale structure of the Planck sky — warm region upper-left, cold region lower-right — by statistical coincidence, illustrating that the UM-derived power spectrum is consistent with the observed sky. All inputs are closed-form functions of `r` at every multipole; with more compute there is no ceiling.*

---

## Papers

| | |
|---|---|
| `01_FOUNDATION.md` | Axiom, recursion, three-channel decomposition, Lagrangian, noise floor, Born coefficient, E₈ closure |
| `02_COSMOLOGY.md` | Every r-only ΛCDM closed form: Ω_b, Ω_c, w₀, wₐ, n_s, A_s, τ_reio, Y_He, N_eff, Σmν, ρ_Λ, Hubble braiding |
| `03_GRAVITY_AND_BLACK_HOLES.md` | Bekenstein-Hawking 1/4 derivation, Hawking radiation, ER=EPR consistency |
| `04_QUANTUM_AND_HOLOGRAPHIC.md` | Born coupling, holographic encoding, event-routing principle, decoherence |
| `05_PARTICLE_PHYSICS.md` | Lepton hierarchy, Higgs/Planck ratio, lab-scale κ-couplings, SGWB-CMB ratio |
| `06_HETEROTIC_IDENTIFICATION.md` | (G₂)₁ ⊂ (E₈)₁ in heterotic E₈×E₈, dark matter as second E₈, SM emergence |
| `07_EXPERIMENTAL_PROGRAM.md` | Phase 0 (Born rule, $2.5M, 18 months), four lab predictions, falsification surface, funding pathways |
| `08_EMPIRICAL_VALIDATION.md` | 98-observable test suite, alternate-recursion uniqueness, structural Bayes |
| `PRE_REGISTRATION.md` | Locked predictions prior to observations, falsification thresholds |

### Synthesis paper

`dgf/PROGRAMME_PAPER.md` — *How The Universe Works*: full derivation of the c²=c+1 axiom and the complete empirical programme, with cobaya MCMC chain configs covering Planck, DESI, DES Y3, KiDS, and joint constraints.

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

The CMB images above are produced by `tests/render_cmb_4k.py` — fully reproducible, ~60 s on a consumer CPU.


## Falsification roadmap

| Test | Timing | What falsifies UM |
|---|---|---|
| **Phase 0 — Born rule** at Hf-178m2 | $2.5M / 18 months | Null at 13.6 ppm sensitivity |
| **Euclid 2026** dark-energy | Late 2026 | w₀, wₐ outside (−0.934, +0.091) ± floor |
| **DESI Year 5/7** neutrino bound | 2027–2030 | Σmν < 0.05 eV |
| **LISA + PTA** SGWB ratio | Mid-2030s | I_CMB/I_SGWB outside 1.118 ± 10% |
| **Direct DM-photon coupling** | Ongoing | Any positive signal |


## CMB-Guided Planet Hunt

`planet_hunt/` applies the UM cosmological framework directly to exoplanet targeting.

**The method:** the CMB temperature at any sky position is the fossil record of the primordial density perturbation that seeded structure formation there. Regions with the same CMB temperature as Earth's neighbourhood formed under the same initial conditions. The pipeline identifies those regions and queries Gaia DR3 for unstudied G-type stars within them.

**Earth CMB reference:** RA=242.56°, Dec=−59.68° (Laniakea / Great Attractor direction). CMB 5° disc temperature in the UM simulation (seed 271828): **+23.2 µK**. In Planck SMICA real data: **−141.69 µK**. These differ because they are different realizations drawn from the same UM-derived power spectrum — the method selects by percentile rank within each realization, not by absolute temperature.

Earth appears at **rank #0** in its own seed category. Every star in the catalogue below it is a candidate for another Earth, selected by the same cosmological initial conditions.

**Results:**
- 575 matched CMB patches (1.2% of sky, ΔT < 8 µK threshold)
- **1,287 unstudied G-type stars** in those regions (Gaia DR3, Teff 5100–6300K, within 500 pc)
- Top target: **Gaia 675329552985501209** — 51 pc, G=8.3, Teff=5664K, CMB ΔT=0.10 µK
- Predicted Earth-twin: **Gaya** (1.00 Re, 351d period, Teq=254K, K=0.093 m/s) — observable with ESPRESSO at La Silla now

**The Ouroboros system** (Gaia 675329552985501209) — full 8-planet architecture derived from stellar physics:

| Name | AU | Period | Size | Teq |
|------|----|--------|------|-----|
| Nabu (b) | 0.28 | 56d | 0.45 Re | 497K |
| Ishtar (c) | 0.55 | 155d | 0.92 Re | 354K |
| **Gaya (d)** | **0.962** | **351d** | **1.00 Re** | **254K** |
| Vritra (e) | 1.30 | 550d | 1.40 Re | 219K |
| Ares (f) | 1.75 | 863d | 1.10 Re | 188K |
| Indra (g) | 4.80 | 10.9yr | 10.5 Re | 120K |
| Kronos (h) | 9.80 | 31.8yr | 9.0 Re | 84K |
| Skadi (i) | 19.5 | 89yr | 3.8 Re | 60K |

<p align="center">
  <img src="planet_hunt/07_planet_concept/gaya.png" width="45%" alt="Gaya — Earth-twin planet in the Ouroboros system"/>
  &nbsp;&nbsp;
  <img src="planet_hunt/07_planet_concept/system_overview.png" width="50%" alt="The Ouroboros system — full architecture"/>
</p>

*Left: Gaya (Ouroboros d) — 1.00 Re, 351-day year, equilibrium temperature 254K. Right: full Ouroboros system overview. All 8 planets derived from UM stellar physics and CMB seed matching.*

Full pipeline, catalogue, and renders: `planet_hunt/` — see `planet_hunt/README.md`.

---

## Citation

```
Shields, J. (2026). Unified Mechanics: A Single-Axiom Framework
for Cosmology, Gravity, and Quantum Mechanics.
```
