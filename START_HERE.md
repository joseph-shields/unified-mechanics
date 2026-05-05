# Start Here

**What this is, in plain English.**

---

## Step 1: One question about a line

Take a line. Cut it into a longer piece and a shorter piece.

Now ask one question: *what ratio between the two pieces makes the whole line relate to the longer piece in exactly the same way the longer piece relates to the shorter piece?*

That's it. That's the whole question.

In other words — what cut makes the ratio repeat at every scale?

---

## Step 2: The algebra falls out

Call the ratio between longer and shorter `c`. Then the whole line is `cS + S` (longer plus shorter).

The self-repeating condition is:

```
whole / longer  =  longer / shorter
```

Substitute and simplify. You get:

```
c² = c + 1
```

One equation. No assumptions. No constants chosen in advance.

---

## Step 3: Solve it

That's a quadratic. Two solutions. One is negative (meaningless for a ratio of lengths). The positive one is:

```
φ = (1 + √5) / 2  ≈  1.618
```

The golden ratio. You've probably seen it before — in spiral shells, sunflowers, architecture. It shows up here because those things are all doing the same thing: repeating a ratio at every scale.

---

## Step 4: One number runs everything

From φ, define:

```
r  =  1 / (2φ)  ≈  0.309
```

This is the contraction rate — how much the recursion shrinks each step.

Now here's where it gets strange. That one number `r` — derived from nothing but the self-similarity question above — predicts the following, with no fitting, no free parameters, no adjustments:

| What | Formula | Measured value | How close |
|---|---|---|---|
| Dark energy fraction of the universe | 1 − 9r²/2 + 4r³ | 68.5% | 0.5% off |
| Dark matter fraction | 4r²(1−r) | 26.5% | 0.3% off |
| Ordinary matter fraction | r²/2 | 4.9% | 3% off |
| Cosmological constant | r²⁴⁰ | 10⁻¹²² | 0.4% in log |
| Spectral index of CMB fluctuations | 1 − r²/φ² | 0.9649 | 0.15% off |
| Tau/electron mass ratio | φ¹⁷(1−r³) | 3477 | 0.33% off |

These are not fits. The formulas were written before the numbers were checked.

---

## Step 5: Why this is different

Every cosmological model before this one has free parameters — numbers that get tuned until the model matches the data. ΛCDM (the standard model of cosmology) has six of them.

This framework has zero. Every number in the table above comes from one equation and one equation only:

```
c² = c + 1
```

The question was: what ratio repeats at every scale?
The answer was: φ.
The consequence was: everything else.

---

## Step 6: What about all the tensions?

Cosmologists have been arguing for years about the "Hubble tension" — different experiments measure the expansion rate of the universe and get different answers (~67 vs ~73 km/s/Mpc). Nobody can agree.

This framework says both measurements are correct. They're measuring different things — one measures how light propagates, the other measures how matter clusters. The framework predicts a specific gap between them and a boundary point at 69.47 km/s/Mpc. The arithmetic mean of every H₀ measurement ever published lands at ~69.5.

The tension isn't a problem. It's a signal.

---

## Where to go next

- The geometric derivation in full: `00_DERIVATION.md`
- Every cosmological quantity derived: `02_COSMOLOGY.md`
- The chain results and Bayesian evidence: `dgf/PROGRAMME_PAPER.md`
- The 98-observable test suite: `08_EMPIRICAL_VALIDATION.md`
