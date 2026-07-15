# LiMB Recast in New Unified Mechanics

## Status

This document records the mathematical conversion of LiMB from the older
single-dictionary presentation into the newer strong-question and descriptive
closure framework.

The numerical forward engine is **CAMB**. IRIS is not used.

The older golden-recursion formula catalogue is retained as an
**observation–inference ledger**. Its values are not deleted, but their logical
status is made explicit.

---

## 1. Layer separation

The converted solver has four layers.

### Layer R — registered observation

An observation record is a physically retained response, for example a
calibrated CMB angular power spectrum with covariance and declared multipole
scope.

### Layer I — observation-to-parameter inference

The legacy functions in `limb.derivations.lcdm_inputs` define a candidate
compiler

\[
I_{\rm old}: r \longmapsto
(H_0,\Omega_b,\Omega_c,n_s,A_s,\tau_{\rm reio},\ldots).
\]

The converted code does not call every entry of this dictionary a physical
derivation. It assigns one of:

- observation;
- algebraic identity;
- inference candidate;
- derived realization;
- open.

At present, the dimensional values of \(H_0\) and \(T_{\rm CMB}\) are
observational anchors. Most dimensionless formulae are inference candidates
until an action or microscopic dynamics derives them.

### Layer F — forward execution

CAMB executes the candidate cosmology:

\[
F_{\rm CAMB}: \theta \longmapsto
(C_\ell^{TT},C_\ell^{EE},C_\ell^{TE},C_\ell^{BB},\ldots).
\]

This tests the consequences of the supplied parameter record. It does not
back-derive that parameter record from first principles.

### Layer Q — strong-question closure

A strong physical question is represented by

\[
\Theta=(\Sigma,a_\Theta,Y_\Theta,K_\Theta,c_\Theta,
\tau_\Theta,\kappa_\Theta,\mathcal F_\Theta),
\]

with explicit scope, intervention, response carrier, answer space, cost,
latency, sufficiency rule, and typed failure conditions.

For the CMB questions in this package, the intervention is a CAMB forward run
and the response is a declared slice of one angular spectrum.

---

## 2. Strong CMB questions

The default question family contains:

\[
\mathfrak Q_{\rm CMB}
=\{\Theta_{TT},\Theta_{EE},\Theta_{TE},\Theta_{BB}\}.
\]

Each question declares:

- the multipole interval \([\ell_{\min},\ell_{\max}]\);
- the comparison tolerance;
- the response units;
- the solver intervention;
- and failure modes.

Given predicted record \(R_p\) and observed record \(R_o\), define the relative
RMS answer discrepancy

\[
d_\Theta(R_p,R_o)
=
\sqrt{\frac1N\sum_j
\left(
\frac{a_\Theta(R_p)_j-a_\Theta(R_o)_j}
{\max(|a_\Theta(R_o)_j|,\epsilon)}
\right)^2}.
\]

The question closes when

\[
d_\Theta(R_p,R_o)\leq \varepsilon_\Theta.
\]

This comparison rule is declared, not smuggled in as an intrinsic law.

---

## 3. Answer-profile geometry

For question family \(\mathfrak Q\), define

\[
d_{\mathfrak Q}(R_1,R_2)
=
\sum_{\Theta\in\mathfrak Q}
 w_\Theta\min\{d_\Theta(R_1,R_2),1\}.
\]

This gives a bounded operational distance between solver records relative to
the chosen strong questions.

Adding grounded questions refines the geometry. Removing questions contracts
it.

---

## 4. Dynamic closure defect

Let the full state satisfy

\[
\dot y=f(y).
\]

Let a linear answer readout be

\[
z=Py.
\]

Suppose the declared reduced answer dynamics is

\[
\dot z=\bar f(z).
\]

The closure defect is

\[
\Delta(y)=\bar f(Py)-Pf(y).
\]

The quotient is dynamically closed exactly when

\[
\Delta(y)=0
\]

through the declared domain.

This is the correct new-UM diagnostic for deciding whether a compressed
observable state has autonomous dynamics.

---

## 5. Minimum-norm closure repair

If an additive full-state source \(s\) is introduced,

\[
\dot y=f(y)+s,
\]

then exact closure requires

\[
Ps=\Delta.
\]

Among all algebraic repairs, the minimum Euclidean norm solution is

\[
\boxed{
 s^*=P^\top(PP^\top)^+\Delta
}
\]

where \((\cdot)^+\) is the Moore–Penrose pseudoinverse.

For numerical stability, the implementation can use

\[
s^*_{\lambda}
=P^\top(PP^\top+\lambda I)^{-1}\Delta.
\]

### What this result means

It is the smallest additive source that repairs the declared answer-level
closure defect.

### What it does not mean

It does **not** establish a physical three-channel law. A candidate source
must still satisfy:

1. dimensional consistency;
2. gauge consistency;
3. constraint preservation;
4. stress-energy conservation or an explicit exchange law;
5. absence of ghost and gradient instabilities;
6. causal and locality requirements;
7. closure across independent question families;
8. held-out observational tests.

Therefore the minimum-norm source is a disciplined construction and diagnostic
tool, not a licence to fit residuals and call them mechanics.

---

## 6. Typed revision order

When a strong CMB question fails, revision proceeds in this order:

\[
\text{type}
\to\text{scope}
\to\text{registration}
\to\text{retention}
\to\text{decoding}
\to\text{inference map}
\to\text{quotient}
\to\text{dynamics}
\to\text{mechanism}
\to\text{ontology}.
\]

A spectral mismatch does not automatically prove new dynamics. Calibration,
scope, covariance, nuisance treatment, or the old parameter compiler may fail
first.

---

## 7. What has been converted

The new package now supplies:

- typed scopes and strong questions;
- provenance-bearing evidence records;
- an explicit observation–inference compiler;
- a CAMB-only forward solver;
- terminal question assessments;
- answer-profile geometry;
- dynamic closure defects;
- minimum-norm closure repair;
- tests separating algebraic correctness from physical status.

---

## 8. What remains to derive

The next physical stage is not to guess values for the old `light`, `matter`,
and `barrier` source stubs.

It is to define a candidate realization

\[
\mathcal R_{\rm phys}
=(X,\mathcal A,\Gamma,M,\mathfrak Q)
\]

and derive a perturbation law whose induced answer dynamics closes the strong
question family while satisfying the admissibility conditions above.

Only then should a nonzero channel source enter the forward equations.

---

## 9. Governing statement

> The old LiMB catalogue supplies candidate observational inferences. CAMB
> executes their consequences. New Unified Mechanics governs which questions
> are being answered, how the answers are grounded, where the description
> closes, and exactly what must be revised when it fails.
