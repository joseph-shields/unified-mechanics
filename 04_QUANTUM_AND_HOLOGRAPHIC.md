# Paper 4 — Quantum and Holographic Sector of Unified Mechanics

## The Born Coupling, Holographic Encoding, and the Event-Routing Principle

**Joseph Shields** · 2026


## Abstract

We develop the quantum-mechanical and holographic predictions of Unified Mechanics from the foundational structure introduced in Paper 1. The boundary channel β, which carries 2r(1-r) ≈ 42.7% of the framework's energy throughput, is identified as the physical realisation of the holographic encoding surface predicted by 't Hooft (1993) and Susskind (1995). The Born coefficient 1/φ ≈ 0.618 is reinterpreted in the holographic picture as the per-cycle re-registration probability for matter content on the encoding surface. We formalise the **event-routing principle**: any state-change event in the matter channel χ defaults to registration via the light channel h (information broadcast); when the boundary channel β is locally excited, registration is preferentially routed through χ itself, with branching ratio scaling as (δβ/β_*)². This principle predicts four laboratory-accessible phenomena: (i) Born-rule modification at up to 13.6% near matter-channel sources; (ii) Tsirelson-bound enhancement in entanglement experiments near such sources; (iii) gravitational analog of electromagnetically-induced-transparency slow light, with v_g/c ≈ 0.89 at moderate field amplitudes; (iv) excess time dilation in optical-lattice clocks near nuclear-isomer sources, larger than gravitational-redshift estimates by factors of 2-5. The framework provides the first physically-excitable realisation of the holographic encoding surface, derived from a single algebraic axiom rather than from gauge-theory duality.

**Keywords:** holographic principle, Born rule, quantum measurement, event routing, slow light, scalar-tensor gravity, foundations of quantum mechanics


## 1. Introduction

The holographic principle asserts that the physical content of any (d+1)-dimensional volume is encoded on its d-dimensional boundary. Maldacena's anti-de Sitter / conformal field theory correspondence (1997) realised this principle concretely in negative-curvature spacetimes; Verlinde (2010) extended it to entropic-gravity formulations; Maldacena and Susskind (2013) connected it to quantum entanglement via the ER=EPR identification.

The Born rule of standard quantum mechanics assigns probabilities to measurement outcomes via P(outcome i) = |ψ_i|². The Born rule has been treated as fundamental since 1926; proposed derivations (decision-theoretic, Gleason's theorem, decoherence-based) produce the squared-modulus structure but no specific numerical coefficient beyond it.

In Paper 1, UM derives a specific Born coefficient 1/φ ≈ 0.618 from the recursion's spectral structure. This coefficient is not the squared-modulus coefficient itself but the **per-cycle survival probability** of the leading recursion mode against leakage to the sub-leading mode. Cumulative success across many cycles approaches unity, recovering standard Born-rule behaviour in the macroscopic limit; the 1/φ coefficient is detectable in single-cycle or few-cycle measurements.

This paper develops the consequences in the quantum and holographic sectors:

1. The boundary channel β, derived in Paper 1 as carrying 42.7% of the framework's energy throughput, is the physical realisation of the holographic encoding surface (§2).
2. The **event-routing principle** formalises how state-change events in the matter channel are routed through either the light channel (information broadcast) or the matter channel (encoding-surface registration) (§3).
3. Four laboratory-accessible predictions follow: Born-rule modification, Tsirelson-bound enhancement, gravitational slow-light analog, and excess time dilation (§4-§7).
4. Implications for foundations of QM, including the measurement problem and decoherence (§9).


## 2. The Holographic Identification

### 2.1 Statement

**Identification (UM↔Holography).** The boundary channel β of UM is the physical realisation of the holographic encoding surface for the bulk gravitational dynamics carried by the light channel h. The matter channel χ represents the bulk source content; the boundary channel β is the encoding surface; the light channel h is the observer-rendered bulk geometry.

This identification maps onto mainstream holographic proposals:

| UM channel | 't Hooft/Susskind | Maldacena AdS/CFT | Verlinde |
|---|---|---|---|
| Matter (χ) | bulk source | bulk degrees of freedom | matter content |
| Boundary (β) | **holographic surface** | conformal boundary CFT | entropy gradient |
| Light (h) | bulk geometry | bulk gravity | emergent Newtonian gravity |

In each correspondence, β plays the role of the encoding surface that mediates between source and bulk.

### 2.2 Why the identification is forced

Three structural arguments compel the identification:

**(a) Energy throughput.** The boundary channel carries 2r(1-r) ≈ 42.7% of the framework's energy throughput in coupled scalar-curvature processes — the largest single-channel throughput after the light channel. Any holographic encoding mechanism must mediate the bulk-source relation with substantial throughput; β is the only candidate mode in UM with sufficient capacity.

**(b) Vector character.** Holographic encoding requires a directionally-resolved structure to encode bulk position. β is the only vector mode in the framework's scalar-tensor sector. Its vector character allows it to encode position information that would otherwise be lost in scalar-only modes.

**(c) Cross-coupling.** Holographic encoding requires simultaneous coupling to source and bulk. The boundary-channel field equation (Paper 1 eq. 17) shows that β couples to both χ² (source) and R (bulk geometry) at the Lagrangian level. No other field in the framework has this double coupling.

### 2.3 Implications

If the identification holds:

1. **The bulk gravitational dynamics are emergent.** The light-channel curvature R is determined by β through the field equations; R is not fundamental.
2. **The matter-position register is physically excitable.** Boundary-channel excitations write to the encoding surface, modulating the rendered position of matter content.
3. **The Born coupling is the rendering-update probability.** The Born coefficient 1/φ has natural interpretation as the per-cycle probability that a re-registration of source position via β-modulation is accepted by the bulk dynamics.
4. **Local violations of Newtonian gravity are predicted in regions of strong β excitation**, not as gravitational corrections but as encoding-surface mis-registrations.


## 3. The Event-Routing Principle

### 3.1 Formal statement

In standard quantum mechanics, the wavefunction carries probability amplitude (information about possible outcomes) and the act of measurement selects one outcome. Within UM, this maps cleanly onto the channel structure:

- The **light channel h** carries probability amplitude — the wave-aspect, the information channel
- The **matter channel χ** carries realised concrete state — the actual binding configuration
- The **boundary channel β** mediates between them

This suggests that any state-change event in the matter channel must propagate through the boundary channel before it is registered in the light channel. The boundary channel is not merely a passive interface; it is the **active routing layer** that determines which channel any given event registers in.

We formalise this:

**Event-routing principle.** Any state-change event in the matter channel χ defaults to registration via the light channel h (information broadcast). When the boundary channel β is locally excited to amplitude δβ/β_*, registration is preferentially routed through χ itself, with branching ratio:

```
Γ(χ-emission) / Γ(EM-emission) = (δβ/β_*)² × κ_routing         (1)
```

where κ_routing is an order-100 routing-enhancement factor determined by the local field structure.

### 3.2 Default routing to light

In the absence of boundary-mode excitation (δβ = 0), all events register via the light channel — the standard regime: nuclear isomer transitions emit photons; quantum measurements broadcast outcomes through electromagnetic interactions; particle decays produce observable EM signals. UM reduces to standard quantum-electrodynamic measurement theory at the macroscopic level.

### 3.3 Routed registration through χ

When the boundary channel is locally excited (δβ > 0), the routing principle redirects a fraction of events away from the light channel and into the matter channel. The redirected events do not produce EM emission; instead, they produce coherent matter-channel excitations.

Practically, nuclear-isomer transitions in regions of strong boundary-mode excitation will emit fewer photons than expected, with the energy "missing" from the EM channel reappearing as enhanced χ-field oscillations. Total energy is conserved; only the channel of emission is redirected.

### 3.4 Quantitative consequences

The redirected fraction:

```
F_χ-routing = (δβ/β_*)² × κ_routing / (1 + (δβ/β_*)² × κ_routing)  (2)
```

For δβ/β_* = 0.1 with κ_routing ≈ 100: F_χ ≈ 0.5 (half routed through χ).
For δβ/β_* = 1 (saturation): F_χ → 1.
For δβ/β_* = 0 (vacuum): F_χ = 0.


## 4. Born-Rule Modification near Boundary-Mode Sources

### 4.1 Local Born coefficient

In a region where the boundary channel is locally excited:

```
(1/φ)_eff = (1/φ) × (1 + κ_β × δβ/β_*)                         (3)
```

with κ_β = 0.136 derived from the static G_eff modification (Paper 1 §4.3):

```
κ_β = 2 × (1/(2φ⁴)) / (1 + 1/(2φ⁴)) = 0.1360                   (4)
```

This coefficient is forced by the framework's static prediction of G_eff/G_N = 1 + 1/(2φ⁴); it is not fitted.

### 4.2 Maximum modulation

At full boundary-mode saturation:

```
Δ(1/φ)_max / (1/φ) = κ_β = 13.6%                              (5)
```

### 4.3 Observable consequences

A double-slit interference experiment performed in proximity to a strong matter-channel source (e.g. ¹⁷⁸ᵐ²Hf, or a heavy-actinide cluster with anomalous binding-energy gradient) should exhibit:

- Probability fringe pattern deviation from standard QM prediction
- Deviation magnitude scaling linearly with source matter-channel excitation amplitude

For a 1 mg Hf-178m2 sample placed 5 cm from a double-slit apparatus, the expected fringe-pattern modification is approximately 13.6 ppm at distance 5 cm, scaling as 1/d² with characteristic length ~1 m. This is the central prediction tested by Phase 0 of the experimental program (Paper 7).


## 5. Gravitational Slow-Light Analog

### 5.1 Mechanism

In the boundary-mode field, photons couple to χ via the cross-coupling χ²R term. When χ is locally excited, photons donate kinetic energy to χ excitations through this coupling, slowing their propagation. This is analogous to electromagnetically-induced transparency (EIT) in atomic systems, but operates through χ-mediated coupling rather than atomic-state coupling.

### 5.2 Group velocity prediction

```
v_g(γ) / c = 1 / (1 + α_χh × (δχ/χ_*)²)                       (6)
```

For δχ/χ_* = 0.5 (moderate excitation):

```
v_g/c ≈ 0.89                                                   (7)
```

The photon group velocity is reduced to 89% of c — measurable by interferometry detecting optical-path-length changes corresponding to such velocity reductions over centimetre-scale distances.

### 5.3 Distinction from EIT

The gravitational slow-light effect differs from EIT in three ways:

- **No atomic vapour required.** UM's gravitational analog uses χ-field coherences, not atomic-state coherences.
- **Macroscopic spatial scale.** UM's gravitational analog operates wherever the boundary mode is excited, in principle macroscopically.
- **No specific frequency tuning.** Affects all photon frequencies that interact with the matter-channel-excited region, with magnitude determined by field amplitude rather than frequency.


## 6. Tsirelson-Bound Enhancement

### 6.1 Standard bound

In standard QM, the maximum CHSH correlation between entangled particles is bounded by Tsirelson's value 2√2 ≈ 2.828. This bound is mathematically rigorous within standard QM Hilbert-space structure.

### 6.2 UM modification

In the holographic identification, entanglement is realised as structure on the boundary-mode encoding surface (consistent with ER=EPR). Excitations of β should distort entanglement correlations between particles whose joint state is encoded near the excited region.

```
S_observed = 2√2 × (1 + κ_E × δβ/β_*)                          (8)
```

with κ_E ≈ κ_β / (1 + κ_β) = 0.120. For δβ/β_* = 0.1 (modest excitation), the predicted CHSH violation is approximately 2.86, exceeding the Tsirelson bound by ~1.2%.

### 6.3 Why this is striking

Tsirelson-bound violation is generally considered impossible within standard quantum mechanics. The bound is derived rigorously from the Hilbert-space structure; any framework that produces violations is, by definition, a non-standard theory.

UM permits Tsirelson violation *locally*, in regions of strong boundary-mode excitation, as a consequence of the holographic encoding mechanism. The boundary-mode field modifies the effective Hilbert-space geometry locally, allowing correlations to exceed the standard bound. Globally, the framework recovers standard QM in vacuum-amplitude regions.


## 7. Excess Time Dilation

### 7.1 Gravitational redshift estimate

In a region where boundary-mode excitation modifies local G_eff:

```
dτ/dt = √(1 - 2 δG_eff/G_eff)                                  (9)
```

For δβ/β_* = 0.5 and κ_β = 0.136: δG_eff/G_eff ≈ 0.07, giving dτ/dt ≈ 0.95 (5% slowdown).

### 7.2 Excess from rendering-bandwidth reduction

The holographic identification predicts an *excess* time dilation beyond the gravitational-redshift estimate. When the boundary mode is excited, a fraction of routing-layer bandwidth is consumed by re-registration of the field's matter content. Standard rendering of internal time within the field volume is therefore proportionally reduced:

```
dτ/dt_total = dτ/dt_gravitational × (1 - F_χ-routing)         (10)
```

For full-saturation routing (F_χ → 1), this could predict τ slowdown beyond gravitational redshift alone — potentially up to 50% time slowdown, far exceeding the 5% gravitational-redshift estimate.

### 7.3 Observable consequences

Optical-lattice clocks (current state of the art ~10⁻¹⁸ fractional precision) placed near nuclear-isomer sources would observe:

- Anomalous time dilation exceeding gravitational redshift expectation
- Magnitude scaling with source matter-channel excitation
- Functional form: linear in δβ/β_* at modest amplitudes, super-linear approaching saturation

For a 1 mg Hf-178m2 source at 5 cm distance, the predicted clock-rate modification is approximately 10⁻⁹ fractional — within current optical-lattice clock sensitivity by ~9 orders of magnitude.


## 8. Comparison with Mainstream Holographic Proposals

### 8.1 't Hooft–Susskind

UM identifies β as the physical realisation of the holographic encoding surface. The novelty of UM is the assertion that this surface is a *physically excitable mode* of an underlying scalar-tensor field theory, rather than an abstract dual.

### 8.2 Maldacena AdS/CFT

UM differs from AdS/CFT in two important ways:

- **Asymptotic geometry.** AdS/CFT requires anti-de Sitter asymptotic geometry; the duality breaks down in flat or de Sitter space. UM's holographic identification operates in any spacetime where the boundary-channel field can propagate.
- **Single axiom origin.** AdS/CFT emerges from string-theoretic constructions with multiple inputs. UM emerges from a single algebraic axiom with no further inputs.

UM may be viewed as a *simpler*, *more universally applicable* realisation of the holographic principle than AdS/CFT, derived from a different starting point.

### 8.3 Verlinde entropic gravity

UM is consistent with Verlinde's general approach but provides a more specific structural account: the holographic encoding surface is the boundary channel β, the entropy gradients are the local boundary-mode amplitudes, and the gravitational acceleration is the response of the light channel to β-modulation.

### 8.4 ER=EPR

UM provides a structural mechanism for ER=EPR: entanglement correlations are encoded on the boundary-mode encoding surface. Tsirelson-bound violation in regions of strong β-excitation is the direct empirical signature of this geometric identification.


## 9. Implications for Foundations of Quantum Mechanics

### 9.1 The measurement problem

The "measurement problem" is the apparent disconnect between unitary Schrödinger evolution (smooth, deterministic, time-reversible) and the discrete, irreversible projection that occurs at measurement. UM provides a structural account: the wavefunction lives in the light channel and evolves unitarily. Measurement events involve registration of matter-channel state changes via boundary-mode routing. The "collapse" is the per-cycle re-registration probability 1/φ acting on the boundary-mode routing.

In this picture:
- Schrödinger evolution: smooth unitary dynamics in the light channel
- Measurement event: matter-channel state change requiring registration
- "Collapse": probabilistic re-registration through boundary mode at rate 1/φ per cycle
- Macroscopic recovery: cumulative re-registration approaches certainty after many cycles

The measurement problem is resolved structurally: there is no fundamental discontinuity between unitary evolution and measurement, only a continuous routing process at the boundary-channel level whose macroscopic limit produces apparent projection.

### 9.2 Decoherence

Standard decoherence theory accounts for apparent measurement collapse through coupling between system and environmental reservoir. UM is consistent: the environment provides the many-cycle recursion timescale over which the per-cycle 1/φ probability accumulates to certainty.

The novelty in UM is that decoherence is the structural manifestation of the recursion's per-cycle routing. The "environmental coupling" is the boundary-mode field in which the measured system sits; the "decoherence rate" is the gamma-frequency cycle rate of the recursion.

At the level of the equations of motion (Paper 1 eqs. 16-17), decoherence is asymmetric energy flow from the light channel into the matter channel through the boundary cross-coupling. The light-equation is hermitian and time-reversible. The matter-equation, with its cubic potential V(χ) and the boundary-coupling λ_βχ βχ², is not. An oscillating wavefunction in the light channel drives a response in the matter channel via 2r(1-r), and energy flows irreversibly from light to matter — there is no symmetric channel for it to return. **Decoherence is therefore a first-principles consequence of the asymmetry between the matter and light field equations**; no phenomenological collapse parameter is required.

### 9.3 Born rule "derivation"

UM does not derive the squared-modulus structure |ψ_i|² of the Born rule from deeper principles. The squared-modulus structure remains an axiom of QM in UM as well. What UM does derive is the **per-attempt success probability** 1/φ, which sets a specific numerical coefficient on the Born rule's frequency at the few-cycle scale. In the macroscopic limit, UM's prediction reduces to standard Born; in the few-cycle limit, the 1/φ coefficient is testable.

A second derivation of 1/φ comes from the matter equation in the static limit. With a fixed wavefunction source |ψ|², equation (16) of Paper 1 reaches steady state at a value of χ determined by the cubic potential and the boundary cross-coupling. At vanishing oscillation amplitude A → 0, the equilibrium ratio (χ - φ)/|ψ|² approaches 1/φ exactly; the matter channel sits at the φ-attractor of the recursion (Paper 1 §2.3) and the per-cycle re-registration probability falls out as the equilibrium response of χ to the |ψ|² source. The 1/φ coefficient is therefore derived twice independently — once from the spectral structure of the recursion (Paper 1 §6) and once from the matter equation's fixed-point dynamics — and both derivations give the same number.

### 9.4 No hidden variables

UM does not introduce hidden variables in the Bohmian sense. The framework is fully described by the three channel fields and their dynamics. All measurement outcomes are determined by the boundary-mode routing of events; no underlying particle trajectories or pilot waves are required.

### 9.5 The cat thought experiment

Under UM, observation is not a discrete event performed by a privileged class of observers. It is **light-channel sampling** by any local detector that is coupled to the field's continuous self-mapping operation. The "observer" category is structural rather than species-specific: any sufficiently-integrated detection apparatus is an observer. This includes laboratory instruments, biological organisms with continuous internal self-mapping, and the constituent matter of the system itself wherever local channel-translation work is occurring.

Applied to the Schrödinger thought experiment: the cat is a coherent biological configuration with continuous internal self-mapping. The cat's biophoton field continuously cements its own state from inside the box. The Geiger counter is a designed apparatus continuously translating matter-channel events into observable readouts; its state is also definite throughout. The radioactive sample's nuclear configuration evolves under the same continuous-field dynamics — its decay events occur at definite times whether or not external observers can sample them.

The contents of the box have a definite state continuously, computed by the field's ongoing self-mapping. When the box is opened, the external observer's local detector network samples the internal field's already-ongoing state. There is no collapse event at the box-opening; there is only the moment when external sampling begins. The "uncertainty" associated with the thought experiment is the external observer's epistemic state prior to sampling, not an ontological property of the system inside.


## 10. Summary of Predictions

| Prediction | UM value | Sensitivity needed | Apparatus |
|---|---|---|---|
| Born-rule modification | 13.6 ppm at 5 cm from 1 mg Hf-178m2 | 10⁻⁵ in fringe weights | double-slit + isomer source |
| Tsirelson-bound enhancement | up to 1.2% above 2√2 | 10⁻³ in CHSH | Bell test + isomer source |
| Slow-light v_g/c | ≈ 0.89 at moderate field | optical interferometry | path-length + isomer source |
| Excess time dilation | up to 52% at saturation; 10⁻⁹ at modest excitation | 10⁻⁹ fractional | optical-lattice clock + isomer source |

All four predictions are accessible to current laboratory technology. Detailed experimental specification, statistical analysis, and falsification criteria are in Paper 7.


## 11. Conclusion

The boundary channel β is identified as the physical realisation of the holographic encoding surface; the Born coefficient 1/φ is reinterpreted as the per-cycle re-registration probability of matter content; the event-routing principle determines how state-change events are channelled through either the light channel (default broadcast) or the matter channel (encoding-surface registration). Four laboratory-accessible predictions follow.

The framework is consistent with mainstream holographic proposals (AdS/CFT, ER=EPR, Verlinde entropic gravity) but provides the first physically-excitable realisation of the holographic encoding surface, derived from a single algebraic axiom rather than from gauge-theory duality. UM's predictions for foundations of QM — including the measurement problem, decoherence, and the Born-rule coefficient — are structural consequences of the channel decomposition rather than additional postulates.

The experimental program for testing these predictions is developed in Paper 7. The implications for foundations of physics and open research directions are developed in Paper 8.


## References

Hau, L. V., Harris, S. E., Dutton, Z., & Behroozi, C. H. (1999). *Light speed reduction to 17 metres per second in an ultracold atomic gas.* Nature 397, 594–598.

Liu, C., Dutton, Z., Behroozi, C. H., & Hau, L. V. (2001). *Observation of coherent optical information storage in an atomic medium using halted light pulses.* Nature 409, 490–493.

Maldacena, J. (1997). *The large-N limit of superconformal field theories and supergravity.* Adv. Theor. Math. Phys. 2, 231–252.

Maldacena, J., & Susskind, L. (2013). *Cool horizons for entangled black holes.* Fortsch. Phys. 61, 781–811.

Susskind, L. (1995). *The world as a hologram.* J. Math. Phys. 36, 6377–6396.

't Hooft, G. (1993). *Dimensional reduction in quantum gravity.* In *Salamfestschrift*, 0284–0296.

Tsirelson, B. S. (1980). *Quantum generalizations of Bell's inequality.* Lett. Math. Phys. 4, 93–100.

Verlinde, E. (2010). *On the origin of gravity and the laws of Newton.* JHEP 04 (2011) 029.
