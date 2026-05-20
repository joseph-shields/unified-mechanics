# Unified Mechanics — For Everyone

**Joseph Shields · 2026**

No science background needed. Start here.

---

## Step 1 — One question

You've got a piece of string. Cut it into a longer piece and a shorter piece.

Ask this: *what ratio between them makes the whole string relate to the longer piece in exactly the same way the longer piece relates to the shorter?*

That's it. One question. No physics. No assumptions.

It gives you one equation. That equation has exactly one answer. That answer is called the golden ratio — **φ ≈ 1.618**. You've probably seen it in sunflower seeds, shells, and architecture. It shows up there for the same reason: things that repeat the same pattern at every scale all land on the same number.

From φ, we get one more number:

```
r = 1 / (2φ) ≈ 0.309
```

Everything else in the universe follows from r. No tuning. No guessing.

---

## Step 2 — Three channels

The equation φ² = φ + 1 splits space into exactly three parts. Think of them like three modes the universe operates in simultaneously:

| Channel | Share of space | What it is |
|---|---|---|
| **Light** | 47.75% | Everything that moves and propagates |
| **Boundary** | 42.71% | The interface — where things meet and interact |
| **Matter** | 9.55% | Everything that accumulates and stays put |

These three add up to exactly 100%. Not approximately. Exactly. They're not chosen — they fall out of the algebra automatically.

In plain English:
- Light is **exploration** — it goes everywhere, carries information, doesn't stay
- Boundary is **acknowledgement** — the moment two things meet
- Matter is **familiarity** — structure that repeats, things that settle

> *For the deeper version of this in plain English: [`papers/shared_space.pdf`](papers/shared_space.pdf)*

---

## Step 3 — What it gets right

From those three channels and the single number r — no fitting, nothing added — the framework derives:

| What | How close |
|---|---|
| How much of the universe is dark energy | 0.5% off |
| How much is dark matter | 0.3% off |
| The cosmological constant (hardest problem in physics) | 0.4% off in log |
| How fast the universe is expanding | derives the exact tension between measurements |
| The fine structure constant (governs all of chemistry) | 0.034% off |
| The proton-to-electron mass ratio | 0.11% off |
| 20 constants of nature total | all within the structural noise floor |

None of these were fitted. The formulas were written before the numbers were checked.

---

## Step 4 — The noise floor

Every result has a precision limit — a minimum gap between the framework's answer and the observed value. That limit is:

```
ε_floor = r³ ≈ 2.95% per channel crossing
```

This isn't a fudge. It's a structural cost — like how any physical process has overhead. The important thing is it cuts **both ways**: a result that agrees *too* closely also breaks the framework. It's a two-sided test, not a tolerance band.

---

## Step 5 — What the universe looks like

These images were produced entirely from r — the CMB (the oldest light in the universe) simulated from scratch, no real sky data used:

<p align="center">
  <img src="research/figures/08a_cmb_sphere_1.png" width="46%"/>
  &nbsp;&nbsp;
  <img src="research/figures/08c_cmb_sphere_3.png" width="46%"/>
</p>

*Two independent simulations of the CMB sky from the same UM-derived power spectrum. The dark blue patch in the first image is the Eridanus supervoid — a real feature of the universe that appears here without being put in.*

<p align="center">
  <img src="research/figures/07b_cmb_sky_4k_seed_e.png" width="96%"/>
</p>

*Full sky map. Every pixel derived from one number.*

---

## Step 6 — The Hubble tension (in plain English)

Cosmologists have been arguing for years because two different methods of measuring how fast the universe is expanding give different answers — about 67 vs 73 km/s/Mpc. Nobody could agree on why.

This framework says: both are right. They're measuring different things. One measures how light travels. The other measures how matter clusters. The framework predicts an exact gap between them of 3r³ ≈ 8.85% and a midpoint of 69.47 km/s/Mpc.

The arithmetic mean of every H₀ measurement ever published: **~69.5**.

The tension isn't a problem. It's a signal.

---

## Step 7 — Finding planets

The same framework was used to search for Earth-like planets. The CMB temperature at any point in the sky is the fossil record of conditions when the universe first became transparent. Regions with the same CMB temperature as Earth's neighbourhood formed under the same initial conditions.

<p align="center">
  <img src="research/planet_hunt/00_earth_reference/cmb_fullsky.png" width="96%"/>
</p>

**1,287 unstudied G-type stars** identified across 575 matched sky patches. Top target: a G5V star 51 light-years away, bright enough for existing telescopes, never studied for planets.

> *Full pipeline: [`research/planet_hunt/README.md`](research/planet_hunt/README.md)*

---

## Step 8 — How to break it

To disagree with the framework you have to break the axiom. Breaking the axiom means arguing that nothing can be self-similar at every scale. The universe already answered that one.

There are also five specific upcoming experiments that could falsify it — Euclid (2026), DESI (2027-2030), LISA + PTA (2030s). Each one either confirms or kills it on a precise number. That's what a real framework looks like.

> *Falsification roadmap: [`07_EXPERIMENTAL_PROGRAM.md`](07_EXPERIMENTAL_PROGRAM.md)*

---

## Where to go next

| If you want... | Go here |
|---|---|
| The philosophical argument | [`THE_QUESTION.md`](THE_QUESTION.md) |
| Plain English walkthrough | [`START_HERE.md`](START_HERE.md) |
| Common objections answered | [`FAQ.md`](FAQ.md) |
| The full mathematical derivation | [`00_DERIVATION.md`](00_DERIVATION.md) |
| All 8 papers | [`00_MASTER_HANDOVER.md`](00_MASTER_HANDOVER.md) |
| The solver (run it yourself) | [`README.md`](README.md) |
