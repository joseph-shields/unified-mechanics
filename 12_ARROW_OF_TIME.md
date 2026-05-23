# Paper 12 — The Arrow of Time as a Theorem of the Axiom

**Joseph Shields** · 2026

---

## Abstract

The arrow of time is physics' most persistent unexplained asymmetry. Fundamental equations — Newton, Schrödinger, Einstein — are time-symmetric; the arrow is usually attributed to a special low-entropy initial condition (the "past hypothesis"), which is an assumption, not a derivation. We show that in Unified Mechanics the arrow of time is a theorem, not a postulate. It follows from a single algebraic fact: the axiom φ² = φ + 1 selects r = 1/(2φ) ≠ 1/2, which forces the expanding channel W_L to exceed the contracting channel W_M by a factor of exactly 5. The forward map x_{n+1} = 1/(4x_n + 2) is stable at r with eigenvalue −1/φ² ≈ −0.382. The backward map is unstable at r with eigenvalue −φ² ≈ −2.618. Forward and backward are not equivalent. The arrow of time points in the direction of W_L dominance, and that direction is fixed by the axiom before any boundary condition is specified.

---

## 1. The Standard Problem

Standard physics has no mechanism for the arrow of time. The laws are time-reversal symmetric (or CPT symmetric in the quantum case). The direction of time is smuggled in through the initial condition: the universe started in an improbably low-entropy state (the past hypothesis), and entropy has increased ever since. This is not an explanation — it moves the question from "why does time have a direction?" to "why did the universe start that way?"

UM does not need this move. The arrow of time is in the algebra.

---

## 2. The Channel Asymmetry

From the axiom φ² = φ + 1, with r = 1/(2φ) ≈ 0.30902:

```
W_L = (1 − r)²     ≈ 0.4775    (expanding / light)
W_B = 2r(1 − r)    ≈ 0.4271    (boundary)
W_M = r²           ≈ 0.0955    (contracting / matter)
```

The ratio of the expanding channel to the contracting channel:

```
W_L / W_M = (1 − r)² / r² = ((1 − r) / r)² = (1/r − 1)²       (1)
```

Since 1/r = 2φ, we have 1/r − 1 = 2φ − 1 = √5. Therefore:

```
W_L / W_M = (√5)² = 5    (exact)                                 (2)
```

The expanding channel carries exactly five times the weight of the contracting channel. This ratio is not a free parameter — it is forced by the axiom through φ = (1 + √5)/2.

---

## 3. Time Symmetry Would Require r = 1/2

A time-symmetric theory requires the forward and backward directions to be equivalent. In channel language, this means the expanding and contracting modes carry equal weight:

```
W_L = W_M  ⟺  (1 − r)² = r²  ⟺  r = 1/2                       (3)
```

Check: does r = 1/2 satisfy the axiom?

```
4(1/2)² + 2(1/2) − 1 = 1 + 1 − 1 = 1 ≠ 0                      (4)
```

r = 1/2 is not a root of 4x² + 2x − 1 = 0. The axiom φ² = φ + 1 does not permit r = 1/2. Time symmetry is algebraically excluded.

**Theorem:** Any system governed by the axiom φ² = φ + 1 is time-asymmetric. The asymmetry is not a consequence of initial conditions; it is a consequence of the axiom.

---

## 4. The Forward Map Is Stable; the Backward Map Is Not

From Paper 11, the UM map is:

```
x_{n+1} = 1/(4x_n + 2)    (forward)                             (5)
```

with stability eigenvalue at r:

```
λ_f = −4r² = −1/φ² ≈ −0.382,    |λ_f| < 1    (stable)          (6)
```

The inverse map — running time backward — is obtained by solving (5) for x_n:

```
x_n = (1 − 2x_{n+1}) / (4x_{n+1})    (backward)                 (7)
```

The backward map has the same fixed point r (since the fixed point equation 4r² + 2r − 1 = 0 is symmetric under this inversion). But the eigenvalue at r:

```
d/dx [(1 − 2x)/(4x)]|_{x=r} = −1/(4r²) = −φ² ≈ −2.618          (8)
```

The product of forward and backward eigenvalues is:

```
λ_f · λ_b = (−1/φ²)(−φ²) = 1    ✓                               (9)
```

as required for a map and its inverse.

The backward eigenvalue |λ_b| = φ² > 1: **the fixed point r is unstable under time reversal**. A perturbation of size ε grows to φ² ε after one backward step, then φ⁴ ε, then φ⁶ ε. Running backward from near r, the system rapidly escapes. Running forward from near r, the system contracts toward r at rate 1/φ² per step.

Forward and backward are not equivalent. The forward direction is the one in which r is the attractor. That direction is the arrow of time.

---

## 5. Divergence Under Time Reversal

Starting from r + δ with δ = 0.001, the backward map produces:

| Step | x | \|x − r\| |
|---|---|---|
| 0 | 0.31002 | 0.001000 |
| 1 | 0.30641 | 0.002610 |
| 2 | 0.31591 | 0.006890 |
| 3 | 0.29137 | 0.017645 |
| 4 | 0.35801 | 0.048994 |

Each step amplifies the deviation by approximately φ² ≈ 2.618. The system is gone from the neighborhood of r within a few steps. The forward map contracts the same perturbation by 1/φ² ≈ 0.382 per step.

There is no physical process corresponding to the backward map. Any real system beginning near r and evolving forward stays near r. A system hypothetically run backward diverges immediately. Time reversal is not a symmetry of the dynamics.

---

## 6. The Braiding Floor as a Clock

The braiding floor ε_floor = r³ ≈ 2.95% is dissipated irreversibly at each cycle. After N forward cycles:

```
Total dissipation = N · r³                                        (10)
```

This quantity is:
- Monotonically increasing in N (forward)
- Strictly decreasing to the past (backward)
- Cannot be negative

Total braiding floor accumulation is a clock. It ticks once per channel traversal, it ticks forward only, and its rate is fixed algebraically at r³ per cycle. This is not the thermodynamic entropy of a specific system — it is the irreducible information cost of existing in a channel-structured universe. It accumulates unconditionally, for every system, in every direction called forward.

---

## 7. Why There Is No Past Hypothesis

The standard account of the arrow of time requires specifying that the universe began in a low-entropy state. This is an external constraint — it does not follow from the dynamics.

In UM, no such constraint is needed. The arrow is in the map:

1. The axiom selects r ≠ 1/2.
2. r ≠ 1/2 forces W_L ≠ W_M (specifically W_L/W_M = 5).
3. W_L ≠ W_M means the forward and backward maps have different eigenvalues at r.
4. One direction (forward) has |λ| < 1: stable. The other (backward) has |λ| > 1: unstable.
5. Physical evolution is the stable direction. That is the arrow.

The past hypothesis is a statement about initial conditions. UM replaces it with a statement about algebra. The universe does not point forward because it started special. It points forward because the equation φ² = φ + 1 does not permit equal weights on expansion and contraction.

---

## 8. Connection to the Second Law

The second law of thermodynamics states that entropy does not decrease. In UM:

- **Local systems:** converge toward r along the forward map, contracting δ by 1/φ² per step. Local entropy (distance from fixed point) decreases. This is structure formation — the system becomes more ordered as it falls toward r.
- **The environment:** absorbs the exported entropy via the W_L channel. Each step exports (1 − r²) of the channel weight into the expanding mode. The total (local + environmental) braiding floor accumulation is N · r³, which increases.

The second law in UM is: total braiding floor accumulation is monotonically non-decreasing, at rate r³ per cycle per system, in the forward direction. Local ordering is permitted and expected; global dissipation is not.

---

## Summary

| Claim | Standard Physics | UM |
|---|---|---|
| Arrow of time | Imposed via past hypothesis (initial condition) | Derived from φ² = φ + 1 (algebraic theorem) |
| Time symmetry | Broken by boundary condition | Broken by r ≠ 1/2, forced by axiom |
| Forward direction | Direction of entropy increase | Direction in which r is stable (|λ_f| = 1/φ² < 1) |
| Backward direction | Entropy-decreasing (prohibited by hypothesis) | Unstable at r (|λ_b| = φ² > 1) |
| W_L / W_M | No analog | 5 exactly — from √5 in the golden ratio |
| Clock | External (thermodynamic entropy) | Braiding floor: N · r³, algebraically fixed |

The arrow of time is not an assumption in UM. It is what happens when an axiom selects a ratio that is not one-half.
