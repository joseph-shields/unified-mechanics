# The Derivation of φ and r

**J. Shields · 2026**

---

## Origin

This framework began with a geometric observation, not with a Lagrangian.

The derivation of c² = c + 1 precedes the cosmological model. The model was built afterward, once it was recognised that the unique positive solution to this recursion — the golden ratio φ — appears as the braiding coupling fixed point of the nKGB Horndeski action under a stability condition. The two derivations, geometric and field-theoretic, return the same number.

---

## 1. The Geometric Derivation

Let W be the whole, S the shorter part, and cS the longer part, with c > 1 unknown:

$$W = cS + S$$

Impose the self-similarity condition — the whole is to the longer part as the longer part is to the shorter part:

$$\frac{W}{cS} = \frac{cS}{S}$$

Substitute W = cS + S:

$$\frac{cS + S}{cS} = \frac{cS}{S}$$

$$\frac{c + 1}{c} = c$$

$$c + 1 = c^2$$

$$c^2 - c - 1 = 0$$

### The Quadratic Formula

$$c = \frac{1 \pm \sqrt{(-1)^2 - 4(1)(-1)}}{2(1)} = \frac{1 \pm \sqrt{5}}{2}$$

Discriminant: Δ = 5. Two roots:

$$c_+ = \frac{1 + \sqrt{5}}{2} \approx 1.6180\ldots \qquad c_- = \frac{1 - \sqrt{5}}{2} \approx -0.6180\ldots$$

Since c = L/S is a ratio of positive lengths, c > 0. The negative root is rejected.

$$\boxed{\varphi = \frac{1 + \sqrt{5}}{2}}$$

---

## 2. The Field-Theory Identification

The same condition arises independently in the nKGB sector of the Horndeski action. For a scalar field threading the equilibrium between gravity and matter in a flat universe with zero total energy, the braiding coupling c must satisfy a stability condition at the KAM-irrational fixed point:

$$c^2 = c + 1$$

The unique stable real solution is c = φ. This is not a coincidence with §1 — it is the same fixed-point condition expressed in a different language. The KAM-irrational frequency φ = [1; 1, 1, 1, …] (continued-fraction expansion all ones) is the most irrational number, giving maximal stability against resonance at this fixed point.

The same eigenvalue appears in the Fibonacci-anyon sector of SU(2)₃ Chern-Simons theory on the AdS₃ boundary, where the braiding phase eigenvalue is exactly φ. Three derivations — geometric, scalar-tensor, topological — return the same number.

With c = φ fixed, the α-functions of the Horndeski action are determined uniquely:

```
G_eff(z = 0)   = 1.072
α_M(z = 0)     = 0.070
α_B(z = 0)     = 0.144
α_T            = 0.000     (speed of light preserved)
```

---

## 3. The Contraction Rate

$$r = \frac{1}{2\varphi} \approx 0.3090$$

Identities following directly from φ² = φ + 1:

$$\frac{1}{\varphi} = \varphi - 1 = 2r \qquad \text{(Born coupling — exact)}$$

$$r^3 \approx 0.02951 \qquad \text{(noise floor } \varepsilon_{\text{floor}} \text{ per channel-traversal cycle)}$$

The three-channel decomposition weights under the W(E₈) action:

| Channel | Weight |
|---|---|
| Light | (1−r)² ≈ 0.4775 |
| Boundary | 2r(1−r) ≈ 0.4271 |
| Matter | r² ≈ 0.0955 |

Sum = 1 exactly.

---

## 4. Everything from r

| Quantity | UM closed form | Observed | Residual |
|---|---|---|---|
| ρ_Λ / M_Pl⁴ | r²⁴⁰ | 10⁻¹²²·⁰⁴ | 0.4% in log |
| Ω_b | r²/2 | 0.0493 | 3.0% |
| Ω_DM | 4r²(1−r) | 0.2647 | 0.3% |
| Ω_DE | 1 − 9r²/2 + 4r³ | 0.685 | 0.5% |
| n_s | 1 − r²/φ² | 0.9649 | 0.15% |
| A_s | r¹⁷ | 2.1×10⁻⁹ | 1.7% |
| m_τ/m_e | φ¹⁷(1−r³) | 3477 | 0.33% |
| Born coupling | 1/φ = 2r | — | exact |
| ε_floor | r³ | 2.95% obs. band | structural |

Full derivations: `01_FOUNDATION.md`, `02_COSMOLOGY.md`, `05_PARTICLE_PHYSICS.md`.
The cosmological chain results and Bayesian evidence: `research/dgf/PROGRAMME_PAPER.md`.

---

## 5. The axiom

$$c^2 = c + 1$$

This equation was reached geometrically first. It was then found to be the stability condition of a scalar-tensor field theory, and the braiding eigenvalue of a topological quantum field theory. The unique positive root is φ. The contraction rate r = 1/(2φ) is the single dimensionless parameter of the theory. All cosmological quantities are closed-form functions of r. Nothing is fitted.
