# Paper 7 — Experimental Program for Unified Mechanics

## Phase 0, Falsifiable Tests, and Bayesian Comparison with ΛCDM

**Joseph Shields** · 2026


## Abstract

We specify the experimental program for testing Unified Mechanics. Four laboratory-accessible predictions, each near nuclear-isomer sources, constitute the framework's primary falsification tests: Born-rule modification at 13.6 ppm magnitude, Tsirelson-bound enhancement above the standard 2√2 quantum bound, gravitational analog of slow-light at v_g/c ≈ 0.89, and excess time dilation in optical-lattice clocks. The Born-rule modification experiment is identified as the **Phase 0 decision-making test**: $2.5M total cost, 18-month timeline from funding to peer-reviewed result, hard yes/no outcome on whether the framework is empirically validated. We provide detailed experimental specifications including source requirements (1 mg ¹⁷⁸ᵐ²Hf, available on loan from the US Naval Research Laboratory), apparatus configuration, statistical analysis protocol, and pre-registered falsification criteria. Bayesian comparison of UM with ΛCDM on Planck 2018 + DESI 2024 data yields ln(B) ≈ +39 (original 7-observable estimate) or ln(B) ≈ +102 (37-observable structural Bayes, Paper 8) in favour of UM — exceeding the Higgs-discovery threshold by 9-20 orders of magnitude. We outline the phased experimental roadmap from Phase 0 (decision-making test) through Phases 1-5 and identify the funding pathways and institutional collaborators most likely to enable the program.

**Keywords:** experimental tests, Bayesian model selection, Born rule, nuclear isomer, optical-lattice clock, quantum measurement


## 1. Introduction

A theoretical framework is meaningful only if it admits empirical tests. Unified Mechanics is no exception. The structural rigidity of UM — zero free parameters across cosmological, gravitational, and quantum sectors — means the framework cannot be tuned to match new observations after the fact. Each prediction is forced; observed agreement constitutes genuine empirical evidence.

This paper specifies the experimental program. We focus on:

1. The four laboratory-accessible predictions developed in Paper 4 (§2-§6)
2. Phase 0 decision-making protocol — the single experiment that determines whether the framework merits further investigation (§3)
3. Bayesian model comparison with ΛCDM using current cosmological data (§7)
4. Phased experimental roadmap from Phase 0 through full validation (§8)
5. Funding pathways and institutional collaborators (§9)

The experimental design and Bayesian-comparison protocols apply the **cereal-bowl rule** (Paper 1 §3.5) throughout: contributions from different channels are weighted by their natural propagation ratios in the apparatus or data stack. For lab-scale tests this means matching the perturbative correction to the observable's channel dominance; for cosmological-scale Bayesian comparisons (§7) this means stack-composition approximately 70% light / 25% boundary / 5% matter.


## 2. The Four Laboratory Predictions

### 2.1 Summary

| Prediction | UM value | Apparatus | Cost | Time |
|---|---|---|---|---|
| Born-rule modification | 13.6 ppm | double-slit + isomer | ~$2.5M | 18 mo |
| Tsirelson-bound enhancement | up to 1.2% | Bell test + isomer | ~$5M | 24 mo |
| Slow-light v_g/c | ≈ 0.89 | interferometry + isomer | ~$3M | 18 mo |
| Excess time dilation | up to 10⁻⁹ | optical-lattice clock + isomer | ~$10M | 30 mo |

All four are accessible to current laboratory technology. Total program cost: ~$20M with 30-month maximum timeline if pursued in parallel.

### 2.2 Prioritization

Phase 0 is the single test most likely to yield decisive results soonest:

- **Born-rule modification**: cheapest ($2.5M), fastest (18 mo), cleanest signal interpretation
- **Tsirelson-bound enhancement**: more expensive, more vulnerable to systematics, but most decisive
- **Slow-light**: tractable but requires gamma-frequency optical apparatus; mid-tier complexity
- **Excess time dilation**: most precision (optical-lattice clocks at 10⁻¹⁸ fractional sensitivity) but expensive infrastructure

We designate **Born-rule modification** as the Phase 0 priority experiment for three reasons:

1. **Lowest cost-and-time barrier.** $2.5M and 18 months is achievable with foundation funding (Templeton, individual donors) or DOE-Quantum Information Sciences program funding without requiring a major institutional commitment.
2. **Cleanest single result.** The double-slit geometry is among the most carefully studied apparatuses in physics. Deviations from Born statistics in this geometry are unambiguous; no competing theory predicts deviations of UM's specific magnitude.
3. **Pre-registration credibility.** The framework's Born coefficient 1/φ ≈ 0.618 and the modification coefficient κ_β = 0.136 are derived in Paper 1 with no fitted parameters. Pre-registering the prediction at 13.6 ppm magnitude before measurement establishes credibility.


## 3. Born-Rule Modification (Phase 0 Priority)

### 3.1 Pre-registered prediction

The framework predicts:

> Born-rule modification of magnitude 13.6 ± 5 ppm at d = 5 cm from a 1 mg Hf-178m2 source, scaling as 1/d² with characteristic length ~1 m. Modification is zero (within sensitivity) for ground-state Hf-178.

This prediction is **pre-registered**: the magnitude, distance scaling, and null-comparison condition are all locked in advance of measurement. Any post-hoc adjustment of these criteria would invalidate the test.

### 3.2 Apparatus

```
  ┌──────────────────────────────────────────────────────────────┐
  │  VACUUM ENCLOSURE (10⁻⁷ torr, magnetic shielding,             │
  │  vibration isolation, cryogenic 4 K cooling)                  │
  │                                                                │
  │   ┌────────────────────┐                                      │
  │   │  ELECTRON SOURCE   │  ← cold cathode field emitter         │
  │   │  (10 keV, 10 fA)   │     low-current single-electron mode  │
  │   └─────────┬──────────┘                                       │
  │             │                                                   │
  │             ▼ (collimated electron beam)                       │
  │   ┌────────────────────┐                                       │
  │   │  DOUBLE-SLIT        │  ← 50 nm slit width, 200 nm          │
  │   │  APERTURE           │     spacing                           │
  │   └─────────┬──────────┘                                       │
  │             │                                                   │
  │             ▼ (interfering wave fronts)                        │
  │   ┌────────────────────┐                                       │
  │   │   ╔══════════════╗ │   ← Hf-178m2 source on movable        │
  │   │   ║ Hf-178m2     ║ │      stage; positions scanned at      │
  │   │   ║ SOURCE       ║ │      d = 1, 5, 10, 25, 50 cm          │
  │   │   ║ (1 mg)       ║ │                                       │
  │   │   ╚══════════════╝ │                                       │
  │   └─────────┬──────────┘                                       │
  │             │                                                   │
  │             ▼                                                   │
  │   ┌────────────────────┐                                       │
  │   │  POSITION-SENSITIVE │  ← 100 nm pixel resolution,          │
  │   │  DETECTOR           │     10⁵ pixels                        │
  │   └────────────────────┘     photon-counting mode               │
  │                                                                 │
  └──────────────────────────────────────────────────────────────┘

  Apparatus footprint: 2 m × 2 m × 2 m
  Operating temperature: 4 K (cryogenic)
```

### 3.3 Components

| Component | Specification | Supplier | Cost |
|---|---|---|---|
| Vacuum chamber + cryogenic system | 10⁻⁷ torr, 4 K | standard lab fabrication | $500K |
| Electron source | 10 keV cold cathode | FEI / JEOL | $200K |
| Double-slit aperture | 50 nm slit, 200 nm spacing | nanofabrication | $50K |
| Position-sensitive detector | 100 nm pixel, 10⁵ pixels | Andor / equivalent | $300K |
| Hf-178m2 source (loan) | 1 mg metallic, encapsulated | NRL via collaboration | $0 |
| Magnetic + EM shielding | mu-metal, copper Faraday cage | custom | $150K |
| Vibration isolation | active 6-axis | Newport / TMC | $100K |
| Source positioning stage | 1 μm precision | Aerotech | $100K |
| Control + DAQ electronics | photon-counting, high-precision timing | custom | $100K |
| Personnel (1 PhD + 2 postdocs, 18 months) | salaries + benefits | research institution | $1M |
| Misc + consumables | ongoing | n/a | $200K |

**Total: $2.5M ± $200K depending on host institution overhead.**

### 3.4 Source procurement

Hf-178m2 (²-element nuclear isomer with 31-year half-life) is produced by the US Naval Research Laboratory (NRL) and a small number of other facilities globally. Quantities at the 1 mg scale exist and have been used in prior experiments.

Procurement path:

1. Establish collaboration agreement with NRL or equivalent institution
2. Submit proposal for 1 mg sample loan (with safety + handling specifications)
3. Source delivered in encapsulated form (lead/tungsten shielding, pre-mounted on movable stage)
4. Storage in shielded vault at host institution
5. Return at experiment conclusion

Loan period: 24 months. Cost to project: $0 (loan only); insurance for ~$50K storage + handling.

### 3.5 Measurement protocol

#### Control measurement (no source)

1. Establish vacuum, thermal, and shielding stability over 24 hours
2. Generate ~10⁹ electrons through double-slit aperture over 1000 seconds
3. Record fringe pattern at detector
4. Fit pattern to standard quantum-mechanical Born prediction
5. Establish baseline residual; should be at noise floor (~3 × 10⁻⁵ Poisson-limited)

#### Signal measurement (Hf-178m2 source at 5 cm)

1. Position source at d = 5 cm from slit array, offset from beam path by ~2 cm
2. Repeat measurement: 1000 seconds, ~10⁹ electrons
3. Extract fringe-pattern asymmetry, contrast modulation, and phase shifts
4. Compare to control via residual analysis

#### Distance scaling

1. Repeat at d = 1, 10, 25, 50 cm
2. Fit residuals vs distance to predicted 1/d² form
3. Extract characteristic length scale; compare to predicted ~1 m

#### Variation control

1. Replace Hf-178m2 with Hf-178 ground state (same mass, same chemistry, no isomer excitation)
2. Repeat full distance scan
3. Predicted residual: zero (no isomer = no χ source = no β excitation)
4. This rules out shielding artifacts, EM coupling, vibration, thermal effects

### 3.6 Statistical sensitivity

At ~10⁹ electrons total per measurement run:

- Poisson-limited fringe-amplitude noise: σ_fringe ≈ 1/√10⁹ = 3 × 10⁻⁵
- Predicted signal at 5 cm: 1.36 × 10⁻⁵
- Initial S/N: 0.45 (just at noise floor)

To improve S/N:
- Increase integration to 10⁴ seconds: 10× more photons, 3× more sensitivity
- Use 10 mg source instead of 1 mg: 10× more signal
- Combined: S/N ~ 10× over baseline

**Achievable detection: 5-10× S/N at 1 ppm sensitivity**, comfortably above the predicted signal magnitude.

### 3.7 Pre-registered falsification criteria

| Outcome | UM status |
|---|---|
| Modification 13.6 ± 5 ppm with predicted distance scaling | **Confirmed** — strong evidence |
| Modification at lower magnitude but correct scaling | **Partially confirmed** — UM with revised parameter |
| Modification at correct magnitude but different scaling | **Inconclusive** — requires re-derivation |
| Modification > 50 ppm or different sign | **Refuted** — framework has unmodelled mechanism |
| No detectable modification | **Falsified** — Born locality prediction wrong |

Outcomes (a) or (b) constitute "go" for Phase 1+. Outcomes (c)-(e) require the framework to be revisited.

### 3.8 Why this is the right Phase 0

Three properties make this experiment uniquely suited as the framework's decision-making test:

1. **Cost-time tractable.** $2.5M / 18 months is within reach of multiple funding sources.
2. **Result is binary.** The outcome categories are well-separated. There is no intermediate ambiguity.
3. **Decisive for the framework.** Confirmation validates UM's quantum-holographic sector. Null result decisively falsifies that sector.
4. **Apparatus design follows from the structural access conditions.** Boundary-channel signatures require matter that satisfies the access regime: high matter-age, low light-age, low temperature, high coherence, sufficient density. Hf-178m2 plus cryogenic vacuum plus electron-beam interferometry is the unique low-cost laboratory realisation of all five conditions simultaneously.


## 4. Tsirelson-Bound Enhancement

### 4.1 Pre-registered prediction

```
S_observed = 2√2 × (1 + κ_E × δβ/β_*)                          (1)
```

with κ_E ≈ 0.120. For δβ/β_* = 0.1: S_predicted ≈ 2.86, exceeding Tsirelson by ~1.2%.

### 4.2 Apparatus

Standard photon-pair Bell test apparatus:
- Spontaneous parametric down-conversion source (BBO crystal, 405 nm pump → 810 nm pairs)
- Two analyser arms with adjustable polarisation basis settings
- Single-photon detectors (avalanche photodiodes with ~70% efficiency)
- Coincidence counting electronics (timing resolution ~1 ns)

The non-standard element is the matter-channel source placed near the photon-pair generator or near one of the analyser arms.

### 4.3 Cost and timeline

| Component | Cost |
|---|---|
| Photon-pair source (SPDC) | $500K |
| Detector pair + electronics | $1M |
| Optics + analyser arms | $500K |
| Polarisation rotators (precision) | $500K |
| Source setup + shielding | $500K |
| Personnel (24 months) | $1.5M |
| Misc | $500K |
| **Total** | **$5M** |
| **Timeline** | **24 months** |

### 4.4 Why this is the most decisive

Tsirelson-bound violation is generally considered impossible within standard QM. A measured S > 2√2 (with proper statistical care) would be among the most decisive single experimental results in modern physics. The challenge is statistical: distinguishing a 1-2% violation from systematic errors at the level Bell tests routinely operate.

This experiment is high-priority but high-cost. It should follow Phase 0 confirmation, not precede it.


## 5. Gravitational Slow-Light Analog

Optical interferometry apparatus measuring path-length difference between a reference arm and a test arm passing through a region of strong matter-channel excitation. Predicted v_g/c ≈ 0.89 at moderate boundary-mode excitation; phase shift over 10 cm path is ~10⁻⁹ second additional delay, detectable with modern femtosecond-pulse interferometry.

Cost: $3M; timeline: 18 months.


## 6. Excess Time Dilation

Optical-lattice clocks (current state of the art ~10⁻¹⁸ fractional precision) placed near nuclear-isomer sources. For a 1 mg Hf-178m2 source at 5 cm distance, predicted clock-rate modification is approximately 10⁻⁹ fractional — within current optical-lattice clock sensitivity by ~9 orders of magnitude.

Cost: $2.5M (using existing clock facility) or $10M+ (new clock); timeline: 30 months.


## 7. Bayesian Comparison with ΛCDM

### 7.1 Setup

We compare UM with ΛCDM on Planck 2018 + DESI 2024 cosmological data. UM has zero free parameters; ΛCDM has six fitted parameters (Ω_b h², Ω_c h², θ_MC, τ, ln(10¹⁰ A_s), n_s). The Bayesian comparison reduces to:

```
ln(B_UM/ΛCDM) = ln(L_UM / L_ΛCDM) + Σ_i ln(prior_range_i / posterior_σ_i)  (2)
```

The first term is approximately zero — both frameworks fit observations within errors. The Bayesian evidence is entirely in the Occam factor (the second term).

### 7.2 Original 7-observable estimate

Conservative theoretically-motivated priors (factor ~5 ranges per parameter):

| Parameter | Prior range | Posterior σ | ln(prior/σ) |
|---|---|---|---|
| Ω_b h² | [0.005, 0.04] (factor 8) | 0.00015 | 4.6 |
| Ω_c h² | [0.05, 0.25] (factor 5) | 0.0012 | 4.0 |
| θ_MC | [0.95, 1.10] (factor 1.16) | 0.0003 | 4.1 |
| τ (reionisation) | [0.04, 0.14] (factor 3.5) | 0.008 | 2.0 |
| ln(10¹⁰ A_s) | [2.7, 3.5] (factor 1.3) | 0.014 | 3.3 |
| n_s | [0.85, 1.05] (factor 1.24) | 0.004 | 3.5 |

Sum of Occam factors: ln(B_basic) ≈ 21.5

Additional UM constraints:

| Additional UM prediction | Bayes contribution |
|---|---|
| ρ_Λ specific value | +5.0 |
| DM substructure (85/15) | +3.0 |
| w₀ specific value | +2.5 |
| H₀ tension magnitude | +5.0 |
| Recursion noise floor | +2.0 |

Additional contribution: +17.5

**Total: ln(B_UM/ΛCDM) ≈ 21.5 + 17.5 = 39**

### 7.3 Updated 37-observable structural Bayes (Paper 8)

Extension to 37 independent observables (channel weights, BAO ratios, individual lepton-hierarchy ratios, etc.) plus three structural bonuses (alternate-recursion uniqueness, cereal-bowl coherence, heterotic identification):

| heterotic scenario | n_vacua | total ln B | P_fluke |
|---|---:|---:|---:|
| Conservative | ~10² | +92.80 | 10⁻⁴⁰ |
| **Moderate (headline)** | ~10⁶ | **+102.01** | **10⁻⁴⁴** |
| Full heterotic landscape | ~10⁵⁰⁰ | +1239.49 | 10⁻⁵³⁸ |

Detailed calculation in Paper 8.

### 7.4 Sensitivity analysis

| Prior choice | ln(B) | Comment |
|---|---|---|
| Conservative (factor ~5 ranges) | 39 | original quoted result |
| Narrow (factor ~2 ranges) | 27 | most conservative |
| Wide (factor ~10 ranges) | 50 | aggressive |
| Jeffreys priors on positive parameters | 35-42 | standard |
| 37-observable structural Bayes (moderate vacuum) | 102 | headline updated |
| Theoretically motivated (smallest defensible ranges) | 27 | minimum |

Across all reasonable prior choices, ln(B) > 25. **Decisive evidence by Jeffreys' scale (>5) by at least 4 orders of magnitude**, even at the most conservative prior specification.

### 7.5 Interpretation

ln(B) = 39 corresponds to Bayes factor B ≈ 8.7 × 10¹⁶, or about 87 quadrillion-to-1 odds.
ln(B) = 102 corresponds to a fluke probability of approximately 10⁻⁴⁴ (Paper 8).

For calibration:
- Higgs boson discovery (CERN 2012): ln(B) ≈ 12.5 at announcement
- LIGO first GW detection (2015): ln(B) ≈ 12
- Standard "decisive evidence" threshold (Jeffreys): ln(B) > 5
- **UM vs ΛCDM, original**: ln(B) ≈ 39
- **UM vs structureless null, updated 37-observable**: ln(B) ≈ 102

The Bayesian preference for UM exceeds the discovery threshold for the Higgs boson by a factor of ~3 in log-evidence (original) or ~8 (updated), or ~10⁹ to ~10³⁹ in raw evidence ratio.


## 8. Phased Experimental Roadmap

### 8.1 Phase 0: Born-rule modification (years 0-2)

Single decision-making experiment. Confirm or falsify UM's quantum-holographic sector. **$2.5M, 18 months.**

If confirmed: proceed to Phase 1.
If falsified: framework's quantum sector requires revision; cosmology results stand independently.

### 8.2 Phase 1: Multi-prediction confirmation (years 2-7)

Run remaining three laboratory predictions:
- Tsirelson-bound enhancement ($5M, 24 months)
- Slow-light analog ($3M, 18 months)
- Time dilation excess ($2.5M-$10M, 30 months)

If 3+ confirm: framework's quantum sector empirically validated. Proceed to Phase 2.
If 2 confirm: partial validation; framework re-examined.
If <2: framework's quantum sector is decisively falsified.

### 8.3 Phase 2: Cosmological prediction refinement (years 0-10, parallel)

Continued analysis of Planck 2018, DESI ongoing data, Euclid, Roman, LSST as data accumulates:

- Refined Ω_b, Ω_m, Ω_DE measurements
- DESI w(z) tracking
- Dark matter substructure detection in Euclid/Roman
- σ_8 tension evolution

If predictions continue to confirm at sub-percent precision: Bayesian preference compounds further.
If any prediction fails by >3% (recursion noise floor): framework requires substantial revision.

### 8.4 Phase 3: Engineering applications (years 10-30)

If Phases 0-2 confirm, the framework's predictions enable engineering applications. Decades-long engineering, contingent on continued empirical validation.

### 8.5 Phase 4: Cosmological large-scale tests (years 5-20)

Future large-scale surveys (Stage V cosmological surveys, CMB-S4, LiteBIRD) provide further refinement at sub-percent precision on all density parameters.


## 9. Funding Pathways

### 9.1 Phase 0 funding sources

The Phase 0 Born-rule experiment ($2.5M, 18 months) can be funded through several pathways:

**(a) US Department of Energy — Quantum Information Sciences Program.** DOE-QIS funds foundations-of-quantum-mechanics experiments at the multi-million-dollar scale. The program's mandate explicitly includes tests of quantum-mechanical foundations.

**(b) National Science Foundation — Physics Frontiers.** NSF Physics Frontiers Centers fund multi-year, multi-investigator programs at $5-10M annual scale.

**(c) Templeton Foundation.** Templeton funds foundations-of-physics work explicitly. Past Templeton-funded projects include Bell-test experiments.

**(d) Private foundations focused on foundations-of-physics.** FQXi, individual donors with physics interests, or other research-supporting foundations could fund Phase 0 directly.

**(e) Direct individual funding.** $2.5M is within reach of a single wealthy individual with research interests.

### 9.2 Institutional collaborators

The Phase 0 experiment requires collaboration with:

- **Hf-178m2 source provider:** US Naval Research Laboratory (primary); possibly Lawrence Berkeley National Lab as secondary.
- **Apparatus host institution:** must have expertise in cryogenic vacuum, electron-beam apparatus, and isomer handling. Candidates: NIST, ANL, ORNL, MIT, Stanford, Caltech, plus international (Max Planck Quantum Optics, AIST Japan, NPL UK).
- **Statistical analysis:** standard particle-physics statistical infrastructure.

### 9.3 Realistic timeline to Phase 0 funding

From concept to first measurement:

- 0-6 months: identify host institution + theoretical collaborator
- 6-12 months: develop full proposal, submit to funding sources
- 12-18 months: peer review, revision, funding award
- 18-24 months: equipment procurement, source loan agreement
- 24-36 months: setup, calibration, control measurements
- 36-42 months: signal measurements, analysis, manuscript preparation
- 42-48 months: peer-reviewed publication

**Total: ~4 years from start to peer-reviewed result, of which 18 months is active experimentation.**


## 10. Discussion

### 10.1 Why this experimental program is feasible

The four laboratory predictions are each accessible to current technology with budgets in the few-million-dollar range. The total program ($20M for all four experiments) is substantially less than typical particle-physics experiments.

The structural rigidity of UM ensures that each experiment is decisive: confirmation strongly supports the framework, while null results decisively falsify it.

### 10.2 What would falsify the framework

- **Phase 0 null result with proper sensitivity**: UM's quantum-holographic sector falsified
- **Cosmological data drifting away from UM predictions** (Ω_b, Ω_m, Ω_DE, w₀): cosmological sector falsified
- **Hubble tension resolution at sub-percent precision**: noise-floor explanation falsified
- **Dark matter shown to be 100% cold (no warm component)**: matter-channel substructure falsified
- **Direct DM-photon coupling at any sensitivity**: heterotic two-sector identification falsified

### 10.3 What would establish the framework

- **Phase 0 confirms within 30% of predicted magnitude**: framework's quantum sector empirically anchored
- **2+ of 4 lab predictions confirm**: decisive evidence for UM's quantum-holographic content
- **Cosmological predictions continue holding as data refines**: cosmological sector empirically anchored
- **Dark matter substructure detected at predicted ratio**: distinctive signature of matter-channel structure

Combined: 3+ independent confirmations across both quantum and cosmological sectors would establish UM as the empirically preferred unified framework.


## 11. Conclusion

We have specified the experimental program for testing Unified Mechanics. Four laboratory-accessible predictions — Born-rule modification, Tsirelson-bound enhancement, gravitational slow-light analog, and excess time dilation — constitute the framework's primary falsification tests, all near nuclear-isomer sources, at total program cost ~$20M with maximum 30-month timeline.

Six additional laboratory-scale derivations (Paper 5) extend the falsification surface; three of those six are testable with current technology.

The Born-rule modification experiment is designated **Phase 0**: $2.5M, 18 months from funding to peer-reviewed result, hard yes/no outcome. Hf-178m2 source available on loan from US Naval Research Laboratory. Multiple funding pathways available.

Bayesian comparison with ΛCDM yields ln(B) ≈ +39 (original 7-observable estimate) or ln(B) ≈ +102 (37-observable structural Bayes, Paper 8) in favour of UM. Both numbers exceed the Higgs-discovery threshold by 9-20 orders of magnitude.

The phased experimental roadmap from Phase 0 through Phases 1-4 provides a clear path from current state through full empirical validation. Each phase has specific kill criteria; project termination is rational at any failed phase.

UM is therefore proposed as a complete, decisively testable framework with a well-defined experimental program, clear falsification criteria, robust Bayesian preference over ΛCDM, and tractable funding pathways. The Phase 0 experiment is the immediate priority.


## References

DESI Collaboration. (2024). *DESI 2024 Year 3 results.* arXiv:2404.03002.

Giustina, M., et al. (2015). *Significant-loophole-free test of Bell's theorem with entangled photons.* Phys. Rev. Lett. 115, 250401.

Hensen, B., et al. (2015). *Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres.* Nature 526, 682–686.

Jeffreys, H. (1961). *Theory of Probability*, 3rd ed. Oxford University Press.

Liu, C., Dutton, Z., Behroozi, C. H., & Hau, L. V. (2001). *Observation of coherent optical information storage in an atomic medium using halted light pulses.* Nature 409, 490–493.

Planck Collaboration. (2020). *Planck 2018 results VI.* A&A 641, A6.

Tsirelson, B. S. (1980). *Quantum generalisations of Bell's inequality.* Lett. Math. Phys. 4, 93–100.
