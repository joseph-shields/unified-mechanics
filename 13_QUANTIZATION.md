# Paper 13 — Quantization as a Consequence of the Braiding Floor

**Joseph Shields** · 2026

---

## Abstract

Standard quantum mechanics imposes quantization by promoting classical variables to operators and postulating commutation relations [x, p] = iℏ. Planck's constant ℏ is a measured input, not derived. In Unified Mechanics, quantization is not imposed — it follows from the braiding floor ε_floor = r³, the irreducible cost of one channel traversal. Because physical processes consist of integer numbers of traversals, all action comes in multiples of r³. This gives an equally-spaced energy spectrum E_n = n · r³ · 2 ln φ, a zero-point energy of r³ · ln φ, a binary spin structure from the two-state W_M channel, and an uncertainty relation Δx · ΔN ≥ r³/2. The quantum of action r³ plays the role of ℏ in UM natural units. The classical limit is recovered as n → ∞ when adjacent levels become indistinguishable.

---

## 1. The Problem

Standard quantization is a procedure: take a classical system, promote observables to operators, impose [x, p] = iℏ. This works extraordinarily well but does not explain why ℏ has the value it does, why observables must be operators, or why discrete spectra appear at all. The procedure is borrowed from data, not derived from a prior principle.

UM does not borrow the procedure. Discreteness is already in the structure.

---

## 2. Why Processes Are Discrete

The UM map (Paper 11) is:

```
x_{n+1} = 1/(4x_n + 2)                                          (1)
```

The variable N counting map iterations is an integer. You cannot apply the map half a time. Physical processes in UM are sequences of complete channel traversals — each traversal moves the system one step along the map. There is no continuous interpolation between steps.

This discreteness is the origin of quantization. The cycle count N ∈ ℤ₊ is the UM quantum number.

---

## 3. The Quantum of Action

Each channel traversal costs exactly ε_floor = r³ of irreversible information exchange (the braiding floor, Paper 01). The action of a process involving n traversals is:

```
A = n · r³,    n = 0, 1, 2, ...                                  (2)
```

Action is quantized in units of r³. Sub-r³ processes do not exist — they would fall below the braiding floor and are unphysical by the falsification criterion of UM.

In standard quantum mechanics, the quantum of action is ℏ. In UM natural units, r³ plays this role:

```
r³ ↔ ℏ    (in UM units)                                          (3)
```

The dimensional connection between r³ and the SI value of ℏ requires matching UM's unit system to SI — this is an open derivation. What is settled: discreteness of action, the minimum unit, and the spectrum structure.

---

## 4. The Energy Spectrum Near the Fixed Point

Near r, the deviation δ_n = x_n − r evolves as (Paper 11):

```
δ_{n+1} = −4r² · δ_n                                            (4)
```

The natural oscillation rate of the UM system is set by the eigenvalue magnitude:

```
ω = −ln(4r²) = ln(φ²) = 2 ln φ ≈ 0.9624 per cycle              (5)
```

A system completing n W_B channel crossings accumulates action A = n · r³. The energy associated with n crossings at oscillation rate ω:

```
E_n = n · r³ · ω = n · r³ · 2 ln φ                              (6)
```

Numerically: E_n ≈ n × 0.02840 (in UM units). The spectrum is **equally spaced**, with uniform gap:

```
ΔE = r³ · 2 ln φ ≈ 0.02840                                      (7)
```

This is the UM harmonic oscillator spectrum. The form E_n = n · r³ · ω mirrors standard QM's E_n = nℏω, with r³ replacing ℏ and 2 ln φ as the natural UM frequency.

---

## 5. Zero-Point Energy

The braiding floor produces irreducible fluctuations even at n = 0. From the stationary variance of δ (Paper 11, equation 10):

```
⟨δ²⟩_stat = r⁶ / (1 − 16r⁴)                                    (8)
```

The zero-point fluctuation amplitude is √⟨δ²⟩_stat ≈ 0.032. The associated zero-point energy:

```
E_0 = r³ · ln φ ≈ 0.01420                                       (9)
```

A system cannot be at rest at x = r. The braiding floor guarantees irreducible motion around the fixed point. This is the UM analog of vacuum energy — ground state fluctuation that cannot be removed. It is not a free parameter; it is r³ × ln φ.

---

## 6. Spin from the W_M Binary Structure

The matter channel W_M = r² has exactly two configurations:

```
+r²    matter      (winding +1, converging toward r)
−r²    antimatter  (winding −1, diverging from r)
```

This two-state structure is the UM origin of spin-1/2. No spinors need to be introduced — the binary nature of the W_M channel is the algebraic content of what spinors represent geometrically. A system in the W_M channel either reinforces the fixed point (+) or opposes it (−). These are the two spin states.

The ratio of the matter state to the total channel weight:

```
W_M / (W_L + W_B + W_M) = r² ≈ 0.0955                          (10)
```

This is fixed by the axiom. Spin is not a degree of freedom added to UM — it is the W_M channel read as a two-state system.

---

## 7. The Uncertainty Relation

The minimum action r³ sets a lower bound on joint uncertainty. Let Δx be the uncertainty in channel position and ΔN be the uncertainty in cycle count. Then:

```
Δx · ΔN ≥ r³/2                                                  (11)
```

This is the UM uncertainty relation. It says: you cannot simultaneously know the channel position to precision Δx and the number of traversals to precision ΔN if their product would fall below r³/2. The factor of 1/2 matches the standard QM convention Δx · Δp ≥ ℏ/2.

The uncertainty relation is not imposed. It follows from the braiding floor: a channel position measurement with precision better than r³ would require a sub-floor process, which is unphysical.

---

## 8. The Classical Limit

The relative spacing between adjacent energy levels:

```
(E_{n+1} − E_n) / E_n = ΔE / (n · ΔE) = 1/n                   (12)
```

| n | Relative spacing |
|---|---|
| 1 | 100% |
| 10 | 10% |
| 100 | 1% |
| 1000 | 0.1% |
| n → ∞ | 0 |

At large n the discrete spectrum becomes indistinguishable from a continuum. The classical limit is n → ∞ — many traversals, fine-grained energy levels, continuous dynamics recovered. This is Bohr's correspondence principle, derived rather than postulated.

---

## 9. What UM Does Not Yet Have

The dimensional connection between r³ and the SI value of ℏ is an open derivation. UM works in a natural unit system where r is dimensionless. Connecting to SI requires:

1. Identifying the UM unit of length (likely l_Planck via L_micro = 2√(ln 2) l_P, Paper 10)
2. Identifying the UM unit of time (one channel traversal in seconds)
3. Computing r³ in SI action units (J·s) and comparing to ℏ = 1.055 × 10⁻³⁴ J·s

This is a prediction, not a parameter — if the UM unit system is self-consistent, r³ in SI units must equal ℏ. That check is deferred to the experimental programme (Paper 07).

---

## Summary

| Quantum concept | Standard QM | UM derivation |
|---|---|---|
| Quantum of action | ℏ (measured) | r³ (derived from axiom) |
| Quantization condition | [x,p] = iℏ (postulated) | Integer channel traversals (map discreteness) |
| Energy spectrum | E_n = nℏω (imposed) | E_n = n · r³ · 2 ln φ (derived) |
| Level spacing | ℏω (arbitrary) | r³ · 2 ln φ ≈ 0.02840 (fixed) |
| Zero-point energy | ℏω/2 (from commutators) | r³ · ln φ (from braiding floor) |
| Spin-1/2 | Spinors (postulated) | W_M binary structure (±r²) |
| Uncertainty | Δx · Δp ≥ ℏ/2 (postulated) | Δx · ΔN ≥ r³/2 (braiding floor) |
| Classical limit | n → ∞ (Bohr, postulated) | 1/n → 0 (derived from spectrum) |

Quantization is not imposed in UM. It is what happens when physical processes cannot cost less than r³ and can only come in whole units.
