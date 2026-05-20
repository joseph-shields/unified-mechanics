# FAQ

---

## "You're just fitting φ to the data."

No parameter was fitted. φ falls out of one question — what ratio makes a line self-similar at every scale? — before any physics enters. The formula `φ² = φ + 1` has one positive solution and that solution is forced. Once you have φ, you have r. Once you have r, every number in the framework follows algebraically. There's nothing to fit because there's nothing free.

If it were a fit, you'd expect it to work in some places and fail in others. It works across cosmology, particle physics, and quantum mechanics simultaneously, with residuals that cluster at exactly the structural noise floor. That's not what fitting looks like.

---

## "The golden ratio shows up everywhere. This is numerology."

The golden ratio shows up in sunflowers and shells because they're doing the same thing — repeating a ratio at every scale. The question here is whether the universe does that too. The answer is apparently yes, and the agreement with observation is quantitative and falsifiable. Numerology doesn't have a noise floor. Numerology doesn't predict the fine structure constant to 0.034%. Numerology doesn't make testable predictions about Euclid 2026 data that doesn't exist yet.

---

## "Why φ? Why not some other number?"

Because no other number works. The alternate-recursion sweep ran every small-integer self-referential algebra of the same form. The nearest competitor gives residuals 68 times worse. φ isn't chosen because it's aesthetically pleasing — it's the unique stable fixed point of the simplest possible recursion. Every other choice either diverges or produces a universe nothing like ours.

---

## "Where's the peer review?"

The universe is the peer reviewer. It's also the only reviewer with access to the actual data. Every number in this framework was derived before it was checked against observation, and the pre-registration is in the repo. 92 of 101 independent observables pass. The 9 that don't are concentrated in the Pantheon+ low-z distance moduli — a known tension that existing models also struggle with.

No journal reviewer has ever looked at the CMB. The CMB has.

---

## "What about the results that failed?"

They're in the paper. All of them. The framework doesn't bury its failures — they're in `08_EMPIRICAL_VALIDATION.md` with the exact residuals. The Pantheon+ low-z failures are a real issue and they're documented as such. A framework with zero free parameters that hits 92/101 across Planck, DESI, BOSS, KiDS, DES, BBN, and cosmic chronometers simultaneously is not a framework that's hiding anything.

---

## "Where do the channel weights come from?"

From the recursion itself. Once you have r, you have two complementary quantities: r and (1-r). The only way to tile all of space with those two rates without overlap or gap is the binomial expansion of unity:

```
(r + (1-r))² = r² + 2r(1-r) + (1-r)²
             = 0.0955 + 0.4271 + 0.4775
             = 1
```

Those three terms are the channel weights. They're not a choice. They're what you get when you ask how a recursion with rate r distributes itself completely. Matter, boundary, and light are the three ways that can happen.

---

## "What does it predict that ΛCDM doesn't?"

Several things ΛCDM either can't address or leaves as free parameters:

- **The Hubble tension** — ΛCDM treats it as a problem. UM says both measurements are correct and predicts the exact gap (`3r³ ≈ 9%`) and the boundary point where they meet (69.47 km/s/Mpc). The arithmetic mean of every H₀ measurement ever published lands at ~69.5.
- **The cosmological constant** — ΛCDM has no explanation for why it takes the value it does. UM derives it: `r²⁴¹ ≈ 10⁻¹²²·⁴`.
- **Dark matter** — ΛCDM requires a particle. UM identifies it as the second E₈ of heterotic string theory — gravitationally coupled, electromagnetically decoupled by structure. All non-gravitational DM searches return null indefinitely. That's a prediction.
- **The Born rule coefficient** — testable at 13.6 ppm in a $2.5M lab experiment. ΛCDM doesn't touch quantum mechanics at all.

---

## "The Hubble tension — aren't you just picking the midpoint?"

No. The boundary point 69.47 km/s/Mpc is derived from r before any H₀ data is looked at. The fact that the arithmetic mean of published measurements lands at 69.5 is a consequence, not an input. The tension isn't a problem to be solved by choosing a value — it's a structural signal that the two measurement methods are sensitive to different channels. Light propagation and matter clustering give different answers because they are different things.

---

## "The cosmological constant derivation feels post-hoc. You chose 241."

241 isn't chosen. 240 is the number of roots of E₈ — a fixed mathematical fact. The +1 is the single braiding correction from the recursion overhead. The derivation is in `papers/cosm_constant.pdf`. The cosmological constant problem has been called the worst fine-tuning problem in physics. The UM answer isn't fine-tuning — it's the algebraic completion of the recursion over the E₈ root system.

---

## "Why should the universe care about φ at all? What's the mechanism?"

That question has the burden of proof backwards. φ is what falls out of the only stable fixed point of the simplest self-referential recursion. Three independent formalisms — geometric, scalar-tensor field theory, and topological quantum field theory — all land on it independently. The question isn't why the universe picks φ. It's what would have to be true for anything recursing stably to avoid it.

The answer is: nothing could avoid it.

---

## "This needs more data / more experiments before it can be taken seriously."

The pre-registration is already in the repo. The falsification surfaces are specific and near-term: Euclid late-2026, DESI Year 5/7, LISA + PTA in the 2030s. Each one either confirms or kills the framework on a precise number, not a vague trend. That's more than most models offer.

Also worth noting: if the string question had returned any other number, you wouldn't be reading this. There would be nothing to read. The reason this exists is precisely because the answer was φ and φ alone turns out to run everything. That's not something you get to dismiss as coincidence after the fact.

And under the framework's own Born rule conditions — the structural Bayes gives a fluke probability of around 10⁻⁴⁴. The possibility that this is wrong doesn't pass the framework's own noise floor threshold. The universe has already voted.

In the meantime — 92/101 observables, zero free parameters, $150 in electricity. Make of that what you will.
