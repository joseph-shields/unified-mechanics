# Paper 11 — The UM Equation of Motion

**Joseph Shields** · 2026

---

## Abstract

Unified Mechanics has a fixed point r = 1/(2φ) and a three-channel partition W_L, W_B, W_M. What it has not yet stated is how a system moves. This paper derives the UM equation of motion directly from the axiom φ² = φ + 1 via the Fibonacci recursion. The result is a discrete map x_{n+1} = 1/(4x_n + 2) whose unique physical fixed point is r, whose stability eigenvalue is λ = −4r² = −4W_M, and whose continuous limit gives the equation of motion dx/dN = −(4x² + 2x − 1)/(4x + 2). The polynomial 4x² + 2x − 1 = 0 is the axiom φ² = φ + 1 rewritten in terms of r. The system does not flow toward r because of boundary conditions or initial data — it flows because the equation of motion is the axiom acting as a restoring force. Every recursive system obeys this equation.

---

## 1. The Problem

UM has three channels summing to 1 and a fixed point r ≈ 0.30902 toward which systems converge. It has a noise floor ε_floor = r³ ≈ 2.95% per cycle. What it does not have is an explicit equation of motion — a rule that says how x evolves from cycle to cycle and why.

This paper derives that rule from the axiom alone.

---

## 2. The UM Dynamical Variable

Let x(t) be the effective contraction ratio of a system at cycle t. At equilibrium x = r. The three channel weights at any instant are:

```
W_L(x) = (1 − x)²        expanding mode
W_B(x) = 2x(1 − x)       boundary mode
W_M(x) = x²              contracting mode
```

W_L + W_B + W_M = 1 identically. The system's state is fully specified by x ∈ [0, 1].

---

## 3. Deriving the Map from the Axiom

The axiom φ² = φ + 1 generates the Fibonacci recursion:

```
φ_{n+1} = 1 + 1/φ_n                                              (1)
```

This converges to φ from any starting value φ_0 > 0. It is the simplest self-referential recursion consistent with the axiom.

Converting to x = 1/(2φ), so φ = 1/(2x):

```
1/(2x_{n+1}) = 1 + 2x_n
x_{n+1} = 1/(2 + 4x_n) = 1/(4x_n + 2)                          (2)
```

Equation (2) is the **UM map**. It follows from the axiom by change of variable. No additional assumptions.

**Verification of fixed point:**

```
x* = 1/(4x* + 2)
4x*² + 2x* = 1
4x*² + 2x* − 1 = 0
x* = (−2 + √(4 + 16))/8 = (−1 + √5)/4 = 1/(2φ) = r    ✓      (3)
```

The polynomial 4x² + 2x − 1 = 0 is the axiom φ² = φ + 1 rewritten in terms of x = 1/(2φ). The fixed point condition and the axiom are the same statement.

---

## 4. Stability

The stability eigenvalue of the map at x = r is:

```
λ = d/dx [1/(4x + 2)]|_{x=r} = −4/(4r + 2)²                    (4)
```

Since 4r + 2 = 2(2r + 1) = 2φ (because 2r = 1/φ, so 2r + 1 = 1/φ + 1 = φ):

```
λ = −4/(2φ)² = −4/(4φ²) = −1/φ² = −(2 − φ) = −4r²            (5)
```

The stability eigenvalue is exactly **λ = −4r² = −4W_M**.

Numerically: λ ≈ −0.382. The negative sign means convergence is oscillatory — the system approaches r from alternating sides. The magnitude 4r² ≈ 0.382 < 1 means it contracts at each step.

The matter channel governs convergence. This is not a postulate — it is a consequence of the map's algebraic structure. The channel that represents self-referential contraction (W_M = r²) is exactly the channel whose weight determines how fast systems collapse toward the fixed point.

---

## 5. The Continuous Equation of Motion

The change per step from the map:

```
Δx = x_{n+1} − x_n = 1/(4x + 2) − x = (1 − x(4x + 2))/(4x + 2)
   = (1 − 4x² − 2x)/(4x + 2)
   = −(4x² + 2x − 1)/(4x + 2)                                   (6)
```

In the continuous limit (treating N as a real variable):

```
dx/dN = −(4x² + 2x − 1)/(4x + 2)                                (7)
```

This is the **UM equation of motion**.

Properties:
- Vanishes at x = r (the fixed point, 4r² + 2r − 1 = 0)
- Positive for x < r (drives upward toward r)
- Negative for x > r (drives downward toward r)
- The driving polynomial is the axiom φ² = φ + 1

The system flows toward r because 4x² + 2x − 1 = 0 is the condition that selects r. Any deviation from r produces a nonzero restoring gradient proportional to how far the system is from satisfying the axiom.

---

## 6. With the Braiding Floor

The map (2) is deterministic. Physical systems carry irreducible noise ε_floor = r³ per cycle. The full stochastic equation of motion is:

```
x_{n+1} = 1/(4x_n + 2) + r³ · ξ_n                              (8)
```

where ξ_n ∈ [−1, +1] is the braiding noise at cycle n.

Near the fixed point r, the deviation δ_n = x_n − r obeys:

```
δ_{n+1} = −4r² · δ_n + r³ · ξ_n                                 (9)
```

The stationary variance of δ is:

```
Var(δ) = (r³)² / (1 − (4r²)²) = r⁶ / (1 − 16r⁴)              (10)
```

Numerically: Var(δ) ≈ (0.02951)² / (1 − 16 × 0.00912) ≈ 8.71 × 10⁻⁴ / 0.854 ≈ 1.02 × 10⁻³.

The RMS fluctuation around r is √Var(δ) ≈ 0.032 ≈ r³ · (1 + small correction). The floor sets the irreducible spread around the attractor.

---

## 7. Convergence Rate

Starting from an arbitrary x_0, the number of cycles N to reach within ε_floor = r³ of r:

Near r, each cycle contracts the deviation by factor 4r² ≈ 0.382. Starting from |δ_0|:

```
N* = log(|δ_0| / r³) / log(1/(4r²)) = log(|δ_0| / r³) / log(φ²)   (11)
```

Since log(1/(4r²)) = log(φ²) = 2 log φ, convergence accelerates at the golden ratio squared per order of magnitude. From x_0 = 0.5 (the maximally uncertain initial condition, distance |δ_0| ≈ 0.19 from r): N* ≈ 2 cycles (verified numerically).

---

## 8. Physical Interpretation

Equation (7) says: every system with recursive structure flows toward the configuration that satisfies φ² = φ + 1, and does so at a rate governed by the matter channel weight W_M = r². The boundary channel W_B = 2r(1−r) mediates this flow — without it (W_B = 0 ↔ x = 0 or x = 1) there is no crossing between the expanding and contracting modes and the system is frozen.

This unifies what several independent frameworks have called different things:
- Freeman's thermodynamic equilibrium: the state that maximizes information channel capacity is x = r
- Frank's single coherence scale: the scale at which J(k²L²) peaks is k* = 1/L = 1/(r · r_s), the inverse of the UM boundary scale
- Schepis's attractor: the "resonant bias" that selects stable configurations is exactly the fixed point of equation (2)

All three are the same equation viewed from different directions.

---

## 9. What the Equation of Motion Is Not

Equation (7) is not a phenomenological fit. It is not a free-parameter differential equation with coefficients chosen to match data. The coefficients 4 and 2 in 4x² + 2x − 1 are fixed by the axiom φ² = φ + 1 — they are the coefficients of the minimal polynomial of r over ℚ. The denominator 4x + 2 is 2(4r + 1)/1, fixed by the map (2). There is nothing adjustable.

The equation of motion is the axiom itself — restated as a flow in x-space.

---

## Summary

| Object | Expression | Origin |
|---|---|---|
| UM map | x_{n+1} = 1/(4x_n + 2) | φ_{n+1} = 1 + 1/φ_n, change of variable |
| Fixed point | x* = r = 1/(2φ) | 4r² + 2r − 1 = 0, i.e. φ² = φ + 1 |
| Stability eigenvalue | λ = −4r² = −4W_M | −4/(4r+2)² = −1/φ² |
| Equation of motion | dx/dN = −(4x²+2x−1)/(4x+2) | Δx per step, continuous limit |
| Stochastic form | δ_{n+1} = −4r²·δ_n + r³·ξ_n | Map + braiding floor |
| Driving force | 4x² + 2x − 1 = 0 | The axiom in x-coordinates |

The system flows because the equation of motion is the axiom acting as a restoring force. The convergence rate is set by the matter channel. The irreducible spread is set by the braiding floor. Nothing is free.
