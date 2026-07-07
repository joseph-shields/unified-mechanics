# Canonicalization

## The Complete Theory of Invariant Structure, Refinement, and Realization

### Single Edition · Consolidated from Books 0–IV, the Series Charter, and the Bridge Paper

*Author: Joseph Shields, in dialogue with GPT and Claude. This edition ends the series' sub-book structure by law (Canonicalization: The Law of the Series, Final Charter v2.0, Part 7). It is one continuous text, in reading order, from the first primitive to the observational ledger. No content is deleted; everything is merged, renumbered into a single scheme, and — where two prior documents covered the same ground from different angles (Part Four) — actually rewritten into one.*

---

## How This Book Is Organized

The book has six Parts and a Coda. Parts are self-contained enough to cite by name (as the text itself constantly does — "Part I, Theorem 4.4" and so on, a convention already built into the prose and left intact rather than renumbered globally, since it is how every cross-reference in this material was originally written and verified).

```text
PART ZERO   Representation Reduction     the method             (formerly Book 0)
PART ONE    Invariant Structure          the object              (formerly Book I)
PART TWO    Refinement Dynamics          the process              (formerly Book II)
PART THREE  Representation Extension     the recursion            (formerly Book III)
PART FOUR   Realization Theory           the completion           (new, this edition)
PART FIVE   From Closure to Cosmos       the application          (the Bridge Paper)
CODA        The Law                      governance and register  (the Charter, final form)
```

Each Part keeps its own internal numbering (Definition 2.3, Theorem 4.4, and so on), exactly as it was proved and cross-referenced throughout the series' development. Cross-Part references use the existing convention — "Book I, Thm 4.4," "Book III, Rem 4.1b" — which the reader should now parse as "Part One" / "Part Three." This is a deliberate editorial choice: renumbering forty-some proven theorems into one flat sequence would risk introducing the exact kind of silent error the series' own translation test was built to catch. What has genuinely changed is that these are no longer separate documents with separate governance — they are chapters.

**The governing sentence**, stated once here and proved to be the correct description by everything that follows:

> **The series is the study of canonicalization: the conditions under which information-preserving reduction eliminates representational ambiguity, yielding a unique irreducible object through which all invariants factor.**

**The picture**, which survives every Part below and is the book's most durable asset:

```text
        Information-preserving reduction
                     |
        Does canonicalization exist?
                     |
        ├── No ──────────────────────────┐
        |                                |
        |                    Family of irreducible
        |                    representatives
        |                    (classify their equivalences)
        |
        └── Yes ─────────────────────────┐
                                         |
                              Unique normal form
                                         |
                              Canonical invariants
                              (everything factors through it)
```

**The doctrine**, one line per Part:

> Represent (Zero). Identify the invariant (One). Refine (Two), and when refinement stalls, Extend (Three). Realize (Four). Apply (Five).

**Status conventions**, uniform throughout: **[PROVEN]** / **[T]**, **[REFUTED]** / **[C]**, *(working)* / *(W)*, *(open)*, *(U)* for universe-scale conjectures in Part Four. A theorem's status is never inherited from its neighbors; it is checked at the point of statement, every time.

---

## Prologue: How to Read This Book

This book was not planned in advance. It was compressed into existence, over several days, by repeatedly asking one question of whatever had just been written — *is this primitive, or can it be reconstructed from less?* — and it carries the marks of that process on purpose. Two are worth naming before Part Zero begins, because they are not flaws to read past; they are the book's evidence for its own method.

**Errors are kept, not smoothed away.** Where an earlier draft claimed too much — a uniqueness theorem later shown to have a gap, a "the" where only an "a" was earned, a slowest-possible-rate claim later shown to hold at one scale and not all — the correction is in the text, at the place it was found, with the counterexample that found it. A reader who wants only the polished final claims can follow the **[T]**-tagged statements and skip the remarks; a reader who wants to see the method work can read the remarks too. Both readings are complete.

**The four Parts recur, and the recurrence is a theorem, not a decoration.** Part Zero reduces representations to a designation; Part One finds what a designation forces; Part Two refines forced structure until it stalls; Part Three shows that a stall is exactly the configuration Part Zero uses to certify a primitive, one level down — so the loop closes, provably, in Part Three's own text. Part Four asks what all of this looks like from the outside, as geometry and scale; Part Five spends that machinery on one physical framework, in the open, with a falsifier stated for every load-bearing claim. The Coda is the law the whole thing now lives under, plus the one register where it is still allowed to change.

If a single thread should be held through everything that follows, it is this: **representation is never the same as content, and every claim in this book knows which one it is making.**

---

## PART ZERO — REPRESENTATION REDUCTION

*The method: what a designation is, what deletion certifies, and why compression stops where it stops.*

### 0. What this document is

Books I and II and the Bridge Paper are domain-specific: point-generated closure structures, quantitative selection, physical realization. This document is not. It states the methodology by which those books were constructed, as an object in its own right — precise enough to be applied to other theories, and precise enough to be applied to itself (§7).

Status tags as in the series. One honesty rule governs everything below: the components of this method are classical (§8); the contribution claimed is their assembly into a constructive workflow with an objective stopping criterion, demonstrated end-to-end on one live case (§6).

---

### 1. The designation — the one primitive

Every application of the method begins with a choice that the method itself cannot make:

**Primitive 0.1 (Designation).** *Designate what is to be held fixed:* a class of descriptions together with a map from descriptions to the **object** they are descriptions *of*. Two descriptions are equivalent when they describe the same object.

The designation is prior to everything else. Without it, "invariance" is empty — under all maps nothing is invariant, under none everything is. The method does not tell you what to care about; it tells you how to purify a theory once you have said what you care about. *(In Book I, the designation was: descriptions = dependency assignments; object = the induced closed-set family. Every result downstream of that choice was forced; the choice itself was not.)*

**Definition 0.2 (Admissible transformation).** A transformation of descriptions is **admissible** iff it preserves the designated object.

**Definition 0.3 (Invariant).** An **invariant** is anything unchanged by every admissible transformation — equivalently, anything that is a function of the object alone.

**Definition 0.4 (Primitive, relative to a theory).** A component of a theory's presentation (a vocabulary item or axiom) is **primitive** iff its deletion changes the theory's invariant content — the set of invariant statements the theory determines. A component whose deletion changes nothing invariant is **representation**.

**Remark 0.5 (The duality).** Transformations and invariants determine each other in opposite directions — enlarging the admissible class shrinks the invariants, and conversely; the pair forms a Galois connection, and a designation is exactly the selection of one closed pair of it. This is why only *one* primitive is listed above: given either side, the other is derived.

---

### 2. The Meta-Principle

> **Meta-Principle (Compression).** *A theory is fully compressed when every remaining component of its presentation is primitive — characterized only by the invariants it preserves under the admissible transformations, with all representation deleted.*

**Justification (near-definitional, as it should be).** If a statement changes under an admissible transformation, it depends on the description and not on the object; therefore it is not a statement *about* the object; therefore it does not belong in a theory *of* the object. Nothing further is assumed. The Meta-Principle is not a discovery about mathematics; it is the unpacking of the word "about."

---

### 3. The Deletion Algorithm

```text
Given a component P of the theory's presentation:

    Delete P.

    Attempt to reconstruct every invariant theorem
    from what remains.

    ┌─ Reconstruction exhibited
    │      → P is representation.
    │        Delete permanently.
    │        (P may survive as a defined abbreviation.)
    │
    └─ Independence proved
           → P is primitive. Retain.

Repeat until every remaining component is primitive.
```

**Remark 0.6 (The certificate asymmetry — required, not optional).** The two branches carry different proof burdens, and conflating them is the method's characteristic failure mode:

- **Representation** is certified by a *reconstruction*: an explicit definition of P from the remainder, plus derivations of the affected theorems. A finite, checkable object.
- **Primitivity** is certified only by an *independence proof*: exhibit two admissible variants of the theory agreeing on everything except P. Failure to find a reconstruction certifies nothing; it is the absence of a certificate, not a certificate of absence.

Every "primitive" verdict lacking an independence proof is provisional and must be tagged so.

**Theorem 0.7 (Stopping criterion is objective)** **[PROVEN]** *For a finitely presented theory, the algorithm terminates: each permanent deletion strictly reduces a finite presentation, and the halted state — every component primitive — is a property of the presentation, not of the practitioner.*

*Proof.* Integer descent on presentation size; the halting condition is Definition 0.4 evaluated componentwise. □

Compression stops when deletion destroys invariant content. Not when it is elegant, not when it is tiring, not when it is liked.

**Theorem 0.8 (The endpoint is not unique)** **[PROVEN by counterexample]** *Distinct runs of the algorithm may halt at distinct fully compressed presentations of the same invariant content.*

*Counterexample.* Classical propositional logic compresses to the primitive basis {¬, ∧}, or to {¬, ∨}, or to {NAND} alone. Each is a fixed point of the algorithm — deleting the last connective destroys the invariant content (functional completeness); yet the three presentations differ. □

**Remark 0.9 (The mirror).** Theorem 0.8 is the meta-level image of Book I, Theorem 3.7: minimal presentations of one invariant object need not be unique. The invariant content is unique; the compressed *presentation* is unique only up to interdefinability. The method obeys the theory it generated — which is either a pleasing consistency or a warning, and the series treats it as both: any claim that compression found *the* foundation, rather than *a minimal presentation of* the foundation, oversteps Theorem 0.8.

---

### 4. The Compression Criterion

> A component is fundamental **iff** deleting it changes the invariant content of the theory.

This single criterion replaces every prior informal test in the series ("does the theory break?", "does it feel necessary?"), and by Remark 0.6 it splits into the two certificates above. It applies to vocabulary and axioms; definitions are abbreviations and are never fundamental by construction.

---

### 5. The Representation Elimination Principle

> **Every successful compression removes representation while preserving invariant structure.**

This sentence is the retrospective explanation of the entire series' development, including its most initially puzzling feature: the repeated arrival at standard mathematics (Moore families, preorders, distributive lattices, rewriting theory). The method was never imitating the classical corpus; it was stripping representation, and invariant content under natural designations *is* what the classical corpus catalogues. Arriving there is the method succeeding, not the project failing.

---

### 6. The case ledger (the live demonstration)

The DCL series as one end-to-end run of the algorithm:

| Component | Deleted? | Certificate | Verdict |
|---|---|---|---|
| Recursion | yes | reconstruction (closure propagation; v1.0 Rem 9.6) | representation |
| Validation | yes | reconstruction (closedness; v1.0 §9.5) | representation |
| Compression (as primitive) | yes | reconstruction (minimal presentations; Book I Def 2.6) | representation |
| Order | yes | reconstruction (condensation; v1.0 Thm 4.12) | representation |
| Time | yes | reconstruction at presentation level (Book I Rem 3.6) | representation |
| Identity (as primitive) | yes | reconstruction (generated closure; v1.0 Def 9.1) | representation |
| Dependency (as ontology) | yes | reconstruction (presentations of 𝒦; Book I Thm 3.1/3.4) | representation |
| Set-valued dependency (within presentations) | no | independence (single-valued variant loses joint dependency; v1.0 Prop 2.2) | primitive of the presentation layer |
| Point-generated closure structure | no | independence pending in full form; partial: general Moore variants change the theorems (Book I Rem 3.2) | **primitive (provisional — independence proof to Book 0 standard still owed)** |
| Designation itself | no | cannot be reconstructed from nothing to designate | primitive of Book 0 |

The last column's one provisional entry is deliberate and is the ledger working as designed: by Remark 0.6, Book I's central primitive currently holds its seat on a partial certificate, and upgrading it is an explicit open item — not an embarrassment, an address.

---

### 7. Self-application

Book 0 must pass its own test. Run the algorithm on its five components:

- **Admissible transformation / invariant:** interdefinable through the Galois connection (Rem 0.5) — either alone reconstructs the other. Each is representation *given the other*; the connection retains exactly one degree of freedom, which is:
- **The designation (Primitive 0.1):** delete it and there is no object for transformations to preserve; nothing remains to reconstruct it from. Independence is immediate — two different designations over the same descriptions yield different invariant contents. **Primitive.**
- **The algorithm (§3), the criterion (§4):** reconstructions of each other plus Definition 0.4. Representation of the Meta-Principle.
- **The Meta-Principle (§2):** the unpacking of "about" relative to a designation. Derived from Primitive 0.1 and the definitions.

Verdict: Book 0 compresses to a single primitive — the designation — exactly as a document about compression had better. *(One level of honest regress remains and is stated rather than hidden: the argument that self-application is the right test is itself an application of the method; the regress terminates in the same place all foundations do — in a choice, here Primitive 0.1, made openly.)*

---

### 8. Classical anchors *(the route/object split, meta-level edition)*

The method's three components have names and birthdays:

- **Designate transformations, study their invariants** — Klein's Erlangen Program (1872).
- **The independence certificate** (two variants agreeing except at P) — Padoa's method (1900).
- **The reconstruction guarantee** — Beth's definability theorem (1953): in first-order logic, whatever is implicitly determined is explicitly definable, so the algorithm's two branches are exhaustive there; beyond first-order logic, exhaustiveness is not guaranteed and the gap is a stated limit of the method, not a footnote.

What is claimed as the series' own: the assembly of these into a constructive theory-building workflow with the objective stopping criterion of Theorem 0.7 and the uniqueness bound of Theorem 0.8, plus the end-to-end demonstration of §6. The objects are classical; the route is ours; the honesty budget stays balanced.

---

### 9. Open problems of Book 0

**OP 0.1 (Confluence).** Characterize the designations for which all runs of the deletion algorithm halt at interdefinable endpoints. (Theorem 0.8 shows they need not coincide; Book I's minimal-presentation analysis suggests the obstruction is again "cycles of interdefinability," but that is an analogy, not a proof.)

**OP 0.2 (Independence upgrade).** ~~Supply the full Padoa-standard independence proof for Book I's primitive (ledger, row 9).~~ **Discharged**: Book III, Theorems 5.1–5.2 supply Padoa exhibits for both Book I's and Book II's primitives; the ledger's provisional entries are certified.

**OP 0.3 (Scope).** Beth's theorem bounds the first-order case; determine how the algorithm's exhaustiveness degrades in richer logics, and whether the workflow needs a third branch ("undetermined") there.

**OP 0.4 (Beyond formal theories).** The Bridge Paper applies the *spirit* of this method to a physical theory via the audit. Whether Definition 0.4 can be given exact content when "theory" includes declared empirical inputs is open, and is the precise point where Book 0 and the Bridge Paper meet.

---

### 10. The order this book follows

```text
Part Zero    The Compression Method          the rule
Part One     Invariant Closure Structures    what the rule finds
Part Two     Refinement Dynamics             what the find does
Part Three   Representation Extension        what happens when the find stalls
Part Four    Realization Theory              what it looks like from outside
Part Five    From Closure to Cosmos          what it may describe
```

Each Part is generated by applying the Part above it. The designation at the top is a choice; everything below it is earned or labelled.

### 11. The Representation Basis Theorems

One application before this Part hands off to the next. Two of the open problems this Part leaves behind — how far the deletion algorithm actually reaches, and whether "primitive count" means anything content-level — have short, complete answers the moment Part One's invariant structure is available to state them in. They are placed here, at the seam, because they use only this Part's algorithm on one side and only the next Part's object on the other.

**Theorem 0.11 (Deletion computes irredundancy)** **[T]** *The fixed points of the deletion algorithm (§3) on generating families are exactly the* **irredundant** *generating families: those from which no single generator can be removed without shrinking the generated invariant content.*

*Proof.* The algorithm halts iff every single deletion fails the reconstruction test (§3), which is the definition of irredundant. □

**Theorem 0.12 (Relative minimum is reachable; absolute minimum need not be)** **[T]** *If B ⊆ F are generating families for the same content, B is reachable from F by single deletions. But there exist F and minimum-cardinality bases B′ of the same content with B′ ⊄ F, so that no deletion order from F reaches B′.*

*Proof.* First claim: delete F∖B one element at a time; B ⊆ (current family) at every stage, so generation is preserved throughout. Second claim, by exhibit: F = {¬, ∧, ∨} generates classical propositional logic; deletion from F halts at {¬,∧} or {¬,∨}, both size 2 and both irredundant; but {NAND} alone generates the same content at size 1, and {NAND} is not a subfamily of F, so no deletion order from F ever reaches it. □

*Consequence.* Reaching absolute minima requires an operation beyond deletion — **substitution**: replace a generator by one derived from the rest, then delete. This is information-preserving by Definition C.4a (Coda) and is filed as an open extension of the algorithm (Part Four, back matter, OP-E′). Theorems 0.11–0.12 are the exact boundary of what deletion alone can promise: irredundancy, always; global minimality, only sometimes.

**Theorem 0.13 (Basis invariance, inside Part One's domain)** **[T]** *Let 𝒦 be a point-generated closure structure (Part One, Def. 1.2) with condensation poset X/∼ (Part One, Def. 2.3). Then S generates 𝒦 iff S meets every maximal identity class, the irredundant generating sets are exactly the transversals of the maximal classes, and* **every irredundant generating set has the same cardinality** *— the number of maximal identity classes.*

*Proof.* If x lies in a maximal class K and x ∈ cl(s) for some generator s, then [s] ⪰ [x]; maximality of [x] forces [s] = [x], so s ∈ K — every generating set must meet every maximal class. Conversely a transversal of the maximal classes generates 𝒦: every class lies below some maximal class in a finite poset, and the closure of a class representative contains its entire down-set. Two generators in the same class make one redundant (they generate identical closures); orphaning a class by omitting its sole representative breaks generation. Hence irredundant sets are exactly the transversals, and all transversals of one partition have equal size. □

*Reading, carried into Part One as its own opening remark.* Theorem 0.12 showed cardinality invariance can fail (Boolean logic: {¬,∧} and {NAND} differ in size). Theorem 0.13 shows exactly where it is restored: in Part One's specific domain — point-generated, pointwise-generating structures — the classical exchange property holds after all, and "primitive count" is a genuine content-level invariant there, not merely a property of the exhibited basis. The boundary between the two behaviors is the arity boundary between joint generation (Part Zero's general setting, where it fails) and unary generation (Part One's setting, where it holds) — named properly once Part One has supplied the vocabulary to name it in.

---

## PART ONE — INVARIANT STRUCTURE

*The object the method finds: point-generated closure structures, their identities, their order, and their attractor.*

#### Preface

Version 1.0 of this book presented itself as a theory of dependency systems. Version 2.0 exists because the theory, applied to itself, found that description presentation-dependent.

Different dependency assignments can induce exactly the same family of closed sets — and every theorem of v1.0, checked one by one, depends only on that family. The dependency graph is therefore an *implementation*. The invariant object is the **closure structure**, and this book is the theory of it.

The scope is stated at the outset, because honesty about scope is the difference between a theorem and an overclaim:

> **Book I is a theory of point-generated closure structures** — those in which the closure of a set is the union of the closures of its points. Not all closure systems are of this kind: linear span and convex hull are classical closure systems that are *not* point-generated (Theorem 3.1 gives the exact boundary). Every theorem in this book claims only the point-generated class.

Two further architectural decisions of this revision, both made explicitly rather than by drift:

**Time.** Different presentations of the same closure structure can reach closure in different numbers of generation steps. Generation depth is therefore *not* invariant. This book takes the position: **the closure structure is timeless; time belongs to presentations.** All presentations disagree about the journey and agree about the destination (Theorem 3.5) — and, more than that, they agree about the *direction* of the journey (Theorem 3.5). Whether a canonical time exists at the condensation level is flagged as future work (Remark 3.10) and is not claimed.

**Compression.** The word no longer names a workflow. A compression is a mathematical act: passing between presentations of the same invariant structure toward a minimal one (Definition 2.6, Theorem 3.7). This definition retroactively justifies every deletion performed during the theory's development: each removed presentation-dependent language while preserving invariant structure. That, and not any single theorem, is the deepest result of the compression era — the method was invariance-detection all along.

Status conventions are inherited from v1.0: **[PROVEN]**, **[REFUTED]**, *(working)*, *(open)*, with tags moving only toward resolution.

##### The Seven Goalposts

Fixed completion criteria for the foundational program. They do not move.

1. **Primitive Count** — identify the invariant primitive; demote implementations.
2. **Language Completeness** — every concept is exactly one of: primitive, definition, theorem, remark.
3. **Canonical Dynamics** — the intrinsic evolution, with existence, endpoint uniqueness, termination, and a monotone progress coordinate.
4. **Canonical Object** — the invariant attractor of every intrinsic process.
5. **Boundary Theorem** — where order stops deciding and selection begins. *(Book II)*
6. **Mathematical Embedding** — the invariant object located in classical mathematics. *(begun in Ch. 4; completed in later books)*
7. **Bridge Functional** — the quantitative functional that decides selection. *(Bridge Paper, Level 2)*

Book I completes Goalposts 1–4. Book II begins at Goalpost 5 and is written; it survives this revision unchanged, because its results were already stated in closure vocabulary.

---

---

### Chapter 1 — Presentations of One Object

#### 1.1 The observation that forced this revision

Consider two dependency assignments on X = {a, b, c}:

- Presentation P₁: δ(a) = {b, c}, δ(b) = ∅, δ(c) = ∅.
- Presentation P₂: δ(a) = {b}, δ(b) = {c}, δ(c) = ∅.

They are different functions, and — first warning — they are different *structures*: {b} is closed under P₁ but not under P₂ (where b requires c). Rewriting dependencies does not automatically preserve the object; whether it does is a checkable condition, not a feeling. Now take a pair that passes the check:

- Presentation P₂′: δ(a) = {b}, δ(b) = {c}, δ(c) = ∅, compared with
- Presentation P₃: δ(a) = {b, c}, δ(b) = {c}, δ(c) = ∅.

Verify: in both, the closed sets are exactly ∅, {c}, {b,c}, {a,b,c}; in both, cl(a) = {a,b,c}, cl(b) = {b,c}, cl(c) = {c}. P₃ carries a redundant edge (a's dependence on c is already implied through b); P₂′ is P₃ with the redundancy removed. And they differ dynamically: from {a}, P₃ reaches closure in one generation step, P₂′ in two. **Same closure structure, different presentations, different edge counts, different clocks.**

Every theorem of v1.0 — the Intersection Theorem, generated closure, identity, condensation, irreducibility, the lattice — gives identical verdicts on P₂′ and P₃, because every one of them is a statement about the closed-set family. The presentations are distinguishable only by vocabulary the theorems never use.

The conclusion is the founding move of v2.0, stated the calm way: **different presentations may encode the same mathematical object; this book studies that invariant object.** The dependency graph becomes one way of writing the object down.

#### 1.2 The primitive of Book I

**Definition 1.1 (Closure system — classical, for context).** A **closure system** (Moore family) on a finite set X is a family of subsets closed under arbitrary intersections and containing X. Its **generated closure** cl(S) is the intersection of all members containing S. *(This is the standard notion; it is stated here only to locate the next definition inside it. Closure systems in general — subspaces of a vector space, convex sets — are closed under intersections but not unions.)*

**Definition 1.2 (Point-generated closure structure — the primitive of Book I).** A **point-generated closure structure** on X is a closure system 𝒦 whose generated closure satisfies cl(∅) = ∅ and, for every S ⊆ X,
$$\operatorname{cl}(S) = \bigcup_{x \in S} \operatorname{cl}(x).$$

**Proposition 1.3 (Union characterization)** **[PROVEN]** *A closure system is point-generated if and only if 𝒦 contains ∅ and is closed under arbitrary unions.*

*Proof.* (⇒) ∅ = cl(∅) ∈ 𝒦. For closed sets {Cᵢ}: cl(⋃Cᵢ) = ⋃_{x∈⋃Cᵢ} cl(x) ⊆ ⋃Cᵢ, since each x lies in some closed Cᵢ, giving cl(x) ⊆ Cᵢ; with extensivity, ⋃Cᵢ is closed. (⇐) cl(∅) = ∅ since ∅ is closed. For any S: the set ⋃_{x∈S} cl(x) is a union of closed sets, hence closed, and contains S; so cl(S) ⊆ ⋃_{x∈S} cl(x); the reverse inclusion is monotonicity. □

*Two consequences worth naming now.* First, union-closure is exactly the property that fails for linear span and convex hull — which is why they sit outside Book I (Remark 3.2 gives the details). Second, "closed under intersections *and* unions, containing ∅ and X" is precisely the definition of the closed sets of an **Alexandrov topology**; Proposition 1.3 is therefore the bridge over which Chapter 4's classical identification will travel, laid down before it is needed rather than crossed suddenly.

**Definition 1.4 (Presentation).** A **presentation** of a point-generated closure structure 𝒦 on X is a dependency assignment δ : X → 𝒫(X) whose induced closed sets — the C with δ(x) ⊆ C for all x ∈ C — are exactly 𝒦.

The v1.0 primitives (elements, dependency) survive in exact demotion: elements remain primitive; dependency becomes the presentation layer. The primitive count of the invariant theory is **one structure over one carrier**.

#### 1.3 What Book I contains, and what it excludes

Admission criterion, replacing all subjective judgment:

> **A concept belongs in Book I if and only if it is invariant under change of presentation.**

Admitted: closed set, generated closure, identity, resolution, minimal presentation (a concept *about* presentations, itself presentation-invariant as a set), the canonical endpoint. Excluded, and deferred to their own books: selection, optimization, geometry, probability, physics, and any dynamics beyond canonical generation. Each exclusion is by the criterion, not by taste: each named concept requires structure (functionals, magnitudes, external processes) that changes when presentation-level or higher-level choices change.

Every concept in this book is exactly one of: **primitive** (the point-generated closure structure), **definition**, **theorem**, or **remark**. There is no fifth category. This is Goalpost 2, and it is closed.

---

---

### Chapter 2 — Definitions

Throughout, 𝒦 is a point-generated closure structure on finite X, and cl its generated-closure operator. Definitions are stated in cl-vocabulary only; no δ appears. (Definitions 2.5–2.6 are the exception by design: they are definitions *about* presentations.)

**Definition 2.1 (Closed set).** C ⊆ X is closed iff C ∈ 𝒦, equivalently cl(C) = C.

**Definition 2.2 (Identity).** A and B (elements or sets) represent the **same identity** iff cl(A) = cl(B). The identity *of* A is cl(A); the identity classes of elements are the classes of x ∼ y :⟺ cl(x) = cl(y).

**Definition 2.3 (Order and condensation).** x ⪰ y :⟺ y ∈ cl(x). This is a preorder; its quotient by ∼ is the **condensation**, a partial order on identity classes. *(Carried over from v1.0, Thm 4.11–4.12, whose proofs used only cl.)*

**Definition 2.4 (Resolution).** For nonempty S ⊆ X:
$$R^{*}(S) = \frac{|S|}{|\operatorname{cl}(S)|} \in (0, 1],$$
the fraction of its identity that S currently contains. R\*(S) = 1 iff S is closed. Derived, not primitive.

**Definition 2.5 (Size of a presentation).** For a presentation δ of 𝒦, its size is ‖δ‖ = Σₓ |δ(x) ∖ {x}| (self-loops are inert and not counted).

**Definition 2.6 (Compression; minimal presentation).** A **compression** is a passage from a presentation δ to a presentation δ′ of the *same* closure structure with ‖δ′‖ < ‖δ‖. A presentation is **minimal** if it admits no compression. *(This is the v2.0 meaning of the word: removal of presentation-dependent structure under preservation of invariant structure. The workflow-era usage is retired.)*

**Definition 2.7 (Intrinsic dynamics).** An operator F : 𝒫(X) → 𝒫(X), defined on every subset, is **intrinsic** if S ⊆ F(S) ⊆ cl(S) for all S — it loses no part of the current state and adds nothing outside the state's identity — and **progressive** if F(S) = S only when S is closed. Nothing constrains the step size: an operator adding one missing element per step and one adding all currently visible dependencies both qualify, and Theorem 3.5 treats them identically. Given a presentation δ, the **generation operator** is
$$D_\delta(S) = S \cup \bigcup_{x \in S} \delta(x),$$
the intrinsic operator that resolves exactly the currently visible constraints. The **canonical dynamics of a presentation** is S₀ = S, Sₙ₊₁ = D_δ(Sₙ). *(Not Sₙ₊₁ = cl(Sₙ): closure is idempotent, and that recursion teleports in one step. The dynamics of interest proceeds shell by shell.)*

---

---

### Chapter 3 — Core Theorems

#### 3.1 The boundary of the theory

**Theorem 3.1 (Presentability; the point-generated characterization)** **[PROVEN]**
*A closure structure 𝒦 on finite X admits a dependency presentation if and only if it is point-generated (Definition 1.2).*

*Proof.* (⇒) Let δ present 𝒦. By v1.0 Theorem 4.8/Proposition 4.9, cl(S) is the set of elements reachable from S by dependency chains, and a chain from S starts at some single x ∈ S; hence cl(S) = ⋃ₓ∈S cl(x). No chain starts from nothing, so cl(∅) = ∅.
(⇐) Suppose 𝒦 is point-generated. Define δ(x) = cl(x) ∖ {x}. A set C is δ-closed iff for every x ∈ C, cl(x) ⊆ C. If C ∈ 𝒦: x ∈ C gives cl(x) ⊆ cl(C) = C by monotonicity; so C is δ-closed. If C is δ-closed: cl(C) = ⋃ₓ∈C cl(x) ⊆ C ⊆ cl(C) (point-generation, then extensivity), so C ∈ 𝒦. The δ-closed family equals 𝒦. And since the generated-closure operator of any presentation is defined from its closed-set family by intersection (v1.0, Cor. 4.5), coinciding families force coinciding operators: cl_δ(S) = ⋂{C δ-closed : S ⊆ C} = ⋂{C ∈ 𝒦 : S ⊆ C} = cl(S). Hence δ presents 𝒦, operator and all. □

**Remark 3.2 (The excluded classics).** Linear span fails both clauses: cl(∅) = {0}, and the span of {v, w} strictly exceeds the union of the two lines. Convex hull fails the union clause: the hull of two points is a segment, not two points. These closure systems are real mathematics — and outside this book. Theorem 3.1 is also the resolution of v1.0's Open Problem 5: the dependency-presentable closure systems are exactly the point-generated ones. The boundary is now a theorem, not a scope apology.

#### 3.2 Elimination and invariance

**Definition 3.3 (The invariant language).** Let L_cl be the fragment of the formal language whose atomic vocabulary is: =, ∈, ⊆, Closed(·), cl(·) — and *not* δ or D_δ. All definitions of Chapter 2 except 2.5–2.7 are L_cl-formulas.

**Theorem 3.4 (Presentation Elimination / Presentation Invariance)** **[PROVEN]**
*Let δ and δ′ be any two presentations of the same closure structure 𝒦. Then every L_cl-statement has the same truth value under δ and δ′. Consequently every theorem of v1.0 expressible in L_cl — the Intersection Theorem, generated closure, identity, condensation, irreducibility, the closure lattice — holds or fails independently of the presentation, and Book I is a theory of closure structures, not of dependency graphs.*

*Proof.* The semantics of every L_cl-atom is defined directly from 𝒦 (Definitions 1.1, 2.1): Closed(S) ⟺ S ∈ 𝒦, and cl(S) = ⋂{C ∈ 𝒦 : S ⊆ C}. Neither δ nor δ′ occurs in these clauses; truth values are functions of (X, 𝒦) alone. Compound formulas inherit this by induction on structure. The listed v1.0 theorems are L_cl-statements by inspection of their v1.0 proofs, which invoke only closedness and cl. □

*Scope note, stated to prevent the one available misreading:* Theorem 3.4 covers the δ-free fragment. Statements about D_δ — trajectories, generation depths — are *not* L_cl-statements and are *not* claimed invariant; their invariant content is isolated next, and it is exactly the endpoint and the direction.

#### 3.3 Canonical dynamics

**Theorem 3.5 (Canonical Dynamics)** **[PROVEN]**
*Let F be any intrinsic progressive operator (Definition 2.7) — in particular D_δ for any presentation δ. For every nonempty S ⊆ X:*
1. *(Identity invariance)* cl(F(S)) = cl(S): *the dynamics never changes what S is, only how much of it is present;*
2. *(Termination)* *the orbit S, F(S), F²(S), … is ⊆-increasing and reaches a fixed point in at most |cl(S)| ≤ |X| steps;*
3. *(Endpoint uniqueness)* *that fixed point is exactly cl(S), for every intrinsic progressive F;*
4. *(Resolution monotonicity)* *R\* is strictly increasing along the orbit until it equals 1, which occurs exactly at arrival.*

*Proof.* (1) S ⊆ F(S) ⊆ cl(S) gives cl(S) ⊆ cl(F(S)) ⊆ cl(cl(S)) = cl(S) by monotonicity and idempotence. (2) Increasing by S ⊆ F(S); the orbit stays inside the finite set cl(S) by (1) plus F(T) ⊆ cl(T) = cl(S); strict growth at every non-fixed step bounds the length by |cl(S)|. (3) Let T be the fixed point. F(T) = T and progressivity force T closed; S ⊆ T ⊆ cl(S) and minimality of cl(S) among closed supersets of S force T = cl(S). Finally D_δ is intrinsic (δ(x) ⊆ cl(S) for x ∈ S because cl(S) is closed) and progressive (if D_δ(S) = S then every dependency of every member lies in S, i.e. S is closed). (4) Along the orbit the denominator |cl(Fⁿ(S))| = |cl(S)| is constant by (1); the numerator |Fⁿ(S)| strictly increases while unfixed by (2); R\* = 1 iff Fⁿ(S) = cl(S) by Definition 2.4. □

**Theorem 3.5 is Goalposts 3 and 4 in one statement**, and it is deliberately stronger than the v1.0/Book-II versions: existence and uniqueness hold not merely for the generation operator of one presentation, but for *every* intrinsic progressive dynamics whatsoever. There is nothing special about D_δ except that a presentation makes it constructible. The attractor is a property of the structure; the routes to it are properties of implementations.

**Remark 3.6 (Time).** Presentations P₂′ and P₃ of §1.1 reach cl(a) from {a} in two steps and one step respectively. Generation depth is presentation-dependent; therefore *time, in this theory, is a property of implementations, not of the invariant object*. What is invariant is the endpoint (Thm 3.5.3) and the direction — R\* increases along every intrinsic dynamics under every presentation (Thm 3.5.4). All presentations disagree about the journey and agree about the destination; all clocks disagree about duration and agree about the arrow.

#### 3.4 Minimal presentations

**Theorem 3.7 (Minimal Presentation)** **[PROVEN]**
*Every point-generated closure structure has at least one minimal presentation, and:*
1. *if every identity class is a singleton (trivial condensation), the minimal presentation is unique — it is the covering presentation δ(x) = { y : x ≻ y and no z has x ≻ z ≻ y };*
2. *in general, the minimal presentation is unique if and only if every identity class of size ≥ 2 has size exactly 2 and is comparable to no other class.*

*Proof.* *Existence*: sizes are non-negative integers over a nonempty set of presentations (nonempty by Theorem 3.1); take a minimum.

*(1), and the "if" of (2).* Suppose ⪰ restricted to singleton classes is a partial order and every nontrivial class is an isolated pair. Within an isolated pair {a, b}, mutual reachability with no outside help forces exactly the two edges a → b → a, and nothing else touches the pair. On the singleton part: (a) every covering edge x ≻ y is indispensable — any presentation must realize the reachability x to y by a chain, a chain through an intermediate z would give x ≻ z ≻ y contradicting covering, so the direct edge is present in *every* presentation; (b) the covering edges suffice — for x ≻ y, pick a maximal element z of {w : x ≻ w ⪰ y}; then x covers z, and by induction on the height of the interval, z reaches y through covering edges; prepend x → z. So every presentation contains the covering edges (a), and the covering edges alone present 𝒦 (b); hence the covering presentation is contained in all others and is the unique minimum. Combining the forced pair-cycles with the forced-and-sufficient covering edges gives uniqueness for case (2)-"if" as well.

*The "only if" of (2).* Two failure modes. **Mode A — a class K of size k ≥ 3**: minimal internal structure realizing mutual reachability on k vertices is a directed Hamiltonian cycle (k edges; fewer cannot make every vertex reach every other, since a spanning strongly connected digraph needs ≥ k edges); for k ≥ 3 at least two distinct cyclic orderings exist (a→b→c→a versus a→c→b→a), each extendable to a minimal presentation of 𝒦, so uniqueness fails. **Mode B — a class K of size 2 comparable to another class**: say K = {a, b} with some class L below it (the argument for L above is symmetric). The condensation covering edge from K to L must be realized by at least one edge leaving K; it may depart from a or from b, and the two choices give identical reachability (a and b reach each other) at identical size — two distinct minimal presentations. Hence uniqueness requires: no class of size ≥ 3, and no size-2 class with a comparable neighbor — which is exactly the stated condition. □

**Remark 3.8 (Verification note, kept deliberately).** An earlier draft of Theorem 3.7 stated uniqueness "iff the condensation is trivial." That is false: an isolated two-element class has a *forced* minimal presentation (the 2-cycle), so uniqueness survives one kind of nontrivial class. The corrected characterization above was found by the series' own rule — attempt the counterexample before believing the biconditional — and the record of the correction stays in the text, per the registry discipline of v1.0.

**Remark 3.8a (Independent-verification note on Theorem 3.7).** Because the theorem is the most combinatorial in the book, its count was re-derived from scratch during review: within a class of size k, mutual paths cannot leave the class (an outside intermediate would join the class), a spanning strongly connected digraph on k vertices needs at least k edges (every vertex needs out-degree ≥ 1), and equality forces a functional graph that is strongly connected, i.e. a single Hamiltonian cycle; between classes, each covering pair of the condensation needs at least one direct edge (no intermediate class exists to route through) and one suffices; hence minimum size = Σ_classes(k≥2) k + #covering pairs, with the non-uniqueness freedoms exactly as stated (cycle orderings for k ≥ 3; attachment endpoints whenever a class of size ≥ 2 meets a covering pair). The recommendation of a fully independent human check stands — that is what the tag discipline is for — but the theorem has now survived two adversarial passes.

**Remark 3.9 (Compression, formalized and closed).** With Definition 2.6 and Theorem 3.7, compression is finished as a concept: it is descent in ‖·‖ through the presentations of a fixed invariant structure, it terminates (integer descent), and its terminal objects are the minimal presentations. A valid compression is exactly a step that removes presentation-dependent structure while preserving the invariant structure — which is a *definition* now, not a philosophy. Retrospectively, every deletion performed during this theory's development was an instance: what was deleted was always presentation (vocabulary, redundancy, implementation); what survived was always 𝒦.

**Remark 3.10 (Where canonical time would have to live).** Theorem 3.7 locates the only place a canonical clock could exist: where minimal presentations are unique — at trivial condensation, i.e. *between* identities, never *within* one. Whether the condensation of an arbitrary structure carries a canonical dynamics whose depth deserves the name of time is explicitly **not claimed** here; it is the first question of the future-work list *(open)*.

**Remark 3.11 (The three convergences).** Generation ascends to cl(S) (Thm 3.5). Compression of presentations descends to minimal presentations of the same 𝒦 (Rem 3.9). Book II's structural compression of closed sets descends to cl(S) from above (Book II, Thm 4.3). Three different processes, defined at three different levels — states, presentations, structures — and each terminates at an invariant of 𝒦. That triple convergence is Goalpost 4's content in full: **the closure structure is not an operation applied to things; it is the attractor of every intrinsic process defined over it.**

---

---

### Chapter 4 — Equivalent Foundations

#### 4.1 The equivalence

Book I ends by exhibiting the invariant object in interchangeable forms, any of which could have been page one — four proven immediately below, a fifth added by Theorem 4.4.

**Theorem 4.1 (The four presentations of the primitive)** **[PROVEN]**
*For a finite carrier X, the following classes of objects are in canonical bijection, and every L_cl-statement transfers verbatim across the bijections:*
1. *point-generated closure structures 𝒦 on X (Definition 1.2);*
2. *dependency presentations up to closure-equivalence (Theorem 3.1);*
3. *preorders ⪰ on X — equivalently, finite Alexandrov topologies with closed sets the down-sets;*
4. *the fixed-point data of any intrinsic progressive dynamics: the map S ↦ (unique terminal fixed point of the orbit at S).*

*Proof.* (1 ⇄ 2) Theorem 3.1, with the equivalence classes of presentations indexed by their induced 𝒦. (1 ⇄ 3) From 𝒦 define x ⪰ y :⟺ y ∈ cl(x): reflexive by extensivity, transitive since y ∈ cl(x) gives cl(y) ⊆ cl(x). From ⪰ define cl(S) = ↓S (the down-closure); point-generation holds because ↓S = ⋃ₓ∈S ↓x, and the closed sets — the down-sets — are closed under unions and intersections, i.e. form an Alexandrov topology's closed family. The two constructions invert each other: y ∈ ↓{x} ⟺ x ⪰ y, and the down-sets of the induced preorder of 𝒦 are exactly 𝒦 by point-generation. (1 ⇄ 4) Theorem 3.5.3: the terminal map *is* S ↦ cl(S), from which 𝒦 is recovered as its fixed-point set; conversely 𝒦 determines cl and thereby every orbit's endpoint. □

**Remark 4.2 (Why point-generation is exactly the Alexandrov property — the smooth crossing).** The identification in form (3) is not a leap; it was pre-built in Chapter 1. An Alexandrov topology is by definition one whose closed sets are stable under arbitrary intersections *and arbitrary unions* — and Proposition 1.3 proved that this pair of stabilities is *precisely equivalent* to point-generation. So "point-generated closure structure" and "closed-set family of a finite Alexandrov space" are two names for one definition, and the preorder of form (3) is the classical specialization preorder. The crossing is a renaming, not a theorem — the theorem content of 4.1 lives in the bijections' inverses.

```text
                 dependency presentations δ
                (implementations; Thm 3.1)
                        ⇅  quotient by
                           closure-equivalence
   preorders ⪰      ⇆   POINT-GENERATED      ⇆   fixed-point data of
 (Alexandrov spaces;    CLOSURE STRUCTURE        intrinsic dynamics
  specialization;            𝒦 on X              S ↦ endpoint = cl(S)
  Prop 1.3 + Rem 4.2)   [the invariant]          (Thm 3.5)
                        ⇅  Birkhoff
                           (Thm 4.4)
              finite distributive lattices
           with 𝒦's join-irreducibles marked
```

**Remark 4.3 (The classical name).** Form (3) says the primitive of Book I is a classical citizen: **finite preordered sets**, equivalently finite Alexandrov spaces; the condensation of Definition 2.3 is the classical T₀ quotient; the identity classes are its points. This is Goalpost 6 begun honestly: the invariant object is not exotic, and the theory's claim to novelty rests — exactly as the Bridge Paper stated for the physical layer — not on the object but on the *route*: the object was arrived at by deletion tests from an operational vocabulary, and the route is what generalizes (Book II's boundary theorem; the Bridge Paper's levels).

#### 4.2 Do the identities form a lattice?

The question was raised in review, and deserves a full answer, because the answer sharpens the whole architecture.

**Theorem 4.4 (Identity poset; Birkhoff correspondence)** **[PROVEN]**
1. *The identities (the ∼-classes under the condensation order) form a partial order that is* **not in general a lattice** *— two incomparable identities need have neither meet nor join.*
2. *The closed sets, however, form a lattice that is not merely complete but* **distributive***: 𝒦 is canonically isomorphic to the lattice of down-sets of the identity poset.*
3. *Inside that lattice, the identities are recoverable: the join-irreducible elements of 𝒦 are exactly the point-closures cl(x), and cl(x) ↦ [x] is an order-isomorphism from the join-irreducibles onto the identity poset.*
4. *(Converse — Birkhoff)* *Every finite distributive lattice arises this way from exactly one poset, its poset of join-irreducibles. Hence "finite distributive lattice with its join-irreducibles" is a fifth equivalent presentation of the primitive, and the diagram above closes.*

*Proof.* (1) Counterexample: X = {a, b}, δ = ∅ everywhere. Two incomparable singleton identities; the identity poset is a two-element antichain, which has neither a top nor a bottom, hence no joins or meets — not a lattice.
(2) By form (3) of Theorem 4.1, 𝒦 is the family of down-sets of the preorder ⪰, and a subset of X is a down-set of a preorder iff it is a union of ∼-classes forming a down-set of the condensation poset; this correspondence is a bijection 𝒦 ≅ 𝒪(X/∼) preserving inclusion both ways. Meets and joins in 𝒦 are ∩ and ∪ (v1.0, Thm 4.17 with Prop 1.3), and set intersection distributes over union; hence 𝒦 is distributive.
(3) Each cl(x) is join-irreducible: if cl(x) = ⋃ᵢ Cᵢ with Cᵢ closed, then x ∈ Cⱼ for some j, so cl(x) ⊆ Cⱼ ⊆ cl(x). Conversely, every nonempty closed C satisfies C = ⋃_{x∈C} cl(x) by point-generation, so a join-irreducible C equals some cl(x). The map cl(x) ↦ [x] is well-defined and order-reflecting/preserving by Definition 2.2–2.3 (cl(x) ⊆ cl(y) ⟺ y ⪰ x... with the orientation of Def 2.3, cl(x) ⊆ cl(y) ⟺ x ∈ cl(y) ⟺ y ⪰ x), hence an order-isomorphism onto the identity poset with the induced order.
(4) Birkhoff's representation theorem for finite distributive lattices, classical; uniqueness of the poset is uniqueness of the join-irreducibles. □

**Remark 4.5 (What Theorem 4.4 buys).** Three things. *First*, the review question is answered exactly: identities form a poset; **closures** form the lattice; and the relationship between the two is not loose analogy but Birkhoff duality — the identities are the irreducible atoms of structure out of which every closed set is uniquely assembled as a down-set. *Second*, v1.0's Theorem 4.17 is upgraded: the closure lattice is distributive, a strictly stronger and strictly more classical statement. *Third*, Book II's boundary theorem gains a cleaner phrasing for free: selection operates on **antichains of the identity poset** — and antichains of a poset are, under Birkhoff, in canonical bijection with the elements of the distributive lattice itself, which is the structural reason the selection problem is exactly as rich as 𝒦 and no richer. Goalpost 6 is now substantially advanced: the invariant object has been located twice in classical mathematics — as finite preorders and as finite distributive lattices — and the two locations are two ends of one classical duality.

**Remark 4.6 (No privileged form).** None of the five forms is the "real" one. Dependency graphs compute well; closure families intersect well; preorders classify well; fixed-point dynamics motivates well; distributive lattices dualize well. Theorem 3.4 licenses free movement among them, and later books use whichever form makes a proof shortest — always stating results in L_cl so that Theorem 3.4 applies.

---

### Chapter 5 — Status and Transition

#### 5.1 Goalpost scoreboard at v2.0

| # | Goalpost | Status |
|---|---|---|
| 1 | Primitive Count | **Closed.** One primitive: the point-generated closure structure (Thm 3.1 fixes its exact extent). Elements: carrier. Dependency: presentation (Thm 3.4). |
| 2 | Language Completeness | **Closed.** Four categories; admission by presentation-invariance (§1.3). |
| 3 | Canonical Dynamics | **Closed.** D-operator form; existence, termination, endpoint uniqueness for *all* intrinsic progressive dynamics, R\* monotone (Thm 3.5). Time assigned to presentations (Rem 3.6); canonical time not claimed (Rem 3.10). |
| 4 | Canonical Object | **Closed.** cl(S) as the universal attractor across states, presentations, and structures (Rem 3.11). |
| 5 | Boundary Theorem | Book II (written; survives this revision verbatim — its results are L_cl-statements plus per-presentation dynamics, exactly the two categories Thm 3.4 and Thm 3.5 govern). |
| 6 | Mathematical Embedding | Substantially advanced: located as finite preorders/Alexandrov spaces (Thm 4.1) and as finite distributive lattices via Birkhoff duality (Thm 4.4); categorical formulation deferred. |
| 7 | Bridge Functional | Bridge Paper, Level 2; untouched by this revision. |

One item from v1.0 changes status rather than surviving: Open Problem 5 is **resolved** by Theorem 3.1. One draft error was caught and corrected during verification (Rem 3.8), leaving the characterization complete. One open question is newly *located* without being answered: canonical time at the condensation level (Rem 3.10). The refutation registry of v1.0 (Ch. 12) is carried forward unchanged; refuted statements remain refuted in every presentation — by Theorem 3.4, they could not do otherwise.

#### 5.2 Transition to Book II

Book I answers: **what structure is forced?** Answer: the point-generated closure structure, its identities, its order, and its attractor — all of it invariant, none of it chosen.

Book II begins where forcing ends: comparable closed structures are decided by order alone; between **incomparable** closed structures no order and no canonical functional decides (Book II, Prop 5.3), and *selection* enters — the first concept in the series that is not presentation-invariant, which is precisely why it was expelled from Book I by the admission criterion and given a book of its own.

The one-sentence version of Book I, v2.0:

> **Beneath every way of writing a system down — as dependencies, as closed families, as an order, as a dynamics — there is one invariant structure; everything intrinsic that can happen to the system ascends, descends, or condenses toward that structure's closure; and every honest compression ever performed on this theory was the same act: deleting the writing while keeping the written.**

---

## PART TWO — REFINEMENT DYNAMICS

*What happens to the object under independent constraints: resolution, selection, and — where refinement stalls — the filtration that records it.*

#### Section A — The Boundary

### Preface

Book I proved what closure *is*. This book proves what closure *optimizes* — and where genuine choice begins.

It answers the four goalposts fixed at the end of the resolution session:

1. Define the functional. — **Done, derived not assumed** (§2).
2. Prove compression/generation is monotone in it. — **Done** (§3).
3. Characterize the fixed points. — **Done** (§3, §4).
4. Show known optimization problems emerge as special cases. — **Split honestly**: one exact theorem, three shaped correspondences (§6).

One result required repairing the session's original functional, which fails its own monotonicity test (§1). The repair is stronger than the original and costs zero new primitives: the primitive count of Book I stands at two.

Status tags as in Book I: **[PROVEN]**, **[REFUTED]**, *(working)*, *(open)*.

---

### Chapter 1. The Ratio Functional Fails

**Definition 1.1 (constraint).** A **constraint** of a set S ⊆ X is a pair (x, d) with x ∈ S and d ∈ δ(x). The constraint is **resolved in S** if d ∈ S, else **unresolved**. Write T(S) for the total number of constraints of S and ρ(S) for the number resolved.

**Candidate 1.2 (session's Resolution Functional).** R(S) = ρ(S)/T(S), with R(S) := 1 when T(S) = 0. Closure ⟺ R = 1. ✓ (that part is correct: S closed iff every constraint resolved.)

**Proposition 1.3** **[REFUTED as a monotone quantity]** *R is not monotone under closure generation D(S) = S ∪ ⋃ₓ∈S δ(x).*

*Counterexample.* X = {a, b, z, c₁, c₂, c₃}; δ(a) = {b}, δ(b) = {a, z}, δ(z) = {c₁, c₂, c₃}, δ(cᵢ) = ∅.
S = {a, b}: constraints (a,b),(b,a),(b,z); resolved: first two. R(S) = 2/3.
D(S) = {a, b, z}: constraints as before plus (z,c₁),(z,c₂),(z,c₃); resolved: (a,b),(b,a),(b,z). R(D(S)) = 3/6 = 1/2 < 2/3. □

**Diagnosis 1.4.** Resolving a constraint may *expose* more constraints than it settles — the denominator moves. Any ratio over a growing total cannot be the invariant of a process whose essence is discovery. The failure is instructive, not fatal: it tells us to measure progress against something generation cannot change.

---

### Chapter 2. The Repair: Resolution Against Identity

**Lemma 2.1 (Identity invariance)** **[PROVEN]** *cl(D(S)) = cl(S) for every S ⊆ X.*

*Proof.* D(S) ⊆ cl(S): for x ∈ S, δ(x) ⊆ cl(S) since cl(S) is closed and contains x. Hence cl(D(S)) ⊆ cl(cl(S)) = cl(S) (Book I, Thm 4.7). Conversely S ⊆ D(S) gives cl(S) ⊆ cl(D(S)) by monotonicity. □

*Reading: resolving yourself never changes what you are; it changes how much of what you are is present.* The generated closure is the invariant target the ratio functional lacked.

**Definition 2.2 (Resolution).** For nonempty S ⊆ X:
$$R^{*}(S) \;=\; \frac{|S|}{|\operatorname{cl}(S)|}.$$
The fraction of its own identity that S currently contains. Note R\* is **derived** — built from cl and counting; no new primitive enters. The Book-I ledger is unchanged.

**Proposition 2.3 (Range and fixed points)** **[PROVEN]** *0 < R\*(S) ≤ 1, and R\*(S) = 1 ⟺ S is closed.*

*Proof.* S ⊆ cl(S) gives the bounds. R\* = 1 iff |S| = |cl(S)| iff S = cl(S) (finite sets, containment) iff S closed (Book I, Thm 4.7(4)). □

---

### Chapter 3. The Monotonicity Theorem (Goalposts 1–3)

**Theorem 3.1 (Resolution is a Lyapunov function for closure generation)** **[PROVEN]**
*For every nonempty S ⊆ X:*
1. *R\*(D(S)) ≥ R\*(S), with equality iff S is already closed;*
2. *the sequence R\*(S), R\*(D(S)), R\*(D²(S)), … is strictly increasing until it reaches 1, which it does in at most |X| steps;*
3. *R\* = 1 exactly at the fixed points of D, which are exactly the closed sets.*

*Proof.* (1) By Lemma 2.1 the denominator |cl(Dⁿ(S))| = |cl(S)| is constant along the trajectory; the numerator |Dⁿ(S)| is non-decreasing since S ⊆ D(S). If S is not closed, some constraint (x,d) is unresolved, so d ∈ D(S)∖S and the numerator strictly increases. If S is closed, D(S) = S. (2) Strict increase of an integer numerator bounded by |cl(S)| ≤ |X| forces arrival at Dᴺ(S) = cl(S) within |X| steps (Book I, Thm 4.8), where R\* = |cl(S)|/|cl(S)| = 1. (3) D(S) = S iff δ(x) ⊆ S for all x ∈ S iff S closed; combine with Prop 2.3. □

**Corollary 3.2 (A second law for the canonical dynamics)** **[PROVEN, conditional only on the reading]** *Under hypothesis (W3) of the Bridge Paper — physical time as closure-generation depth — resolution never decreases along time, strictly increases while any dependency is unresolved, and saturates at 1 exactly at completion. The arrow of time is the direction of self-completion, and R\* is its monotone witness.*

The mathematics of the corollary is Theorem 3.1; only the word "time" is hypothesis, and it is tagged as such.

---

### Chapter 4. The Optimization Theorem: cl Solves Its Own Problem

The session's midpoint proposal — *maximize density subject to executability* — becomes exact when stated as its dual:

**Problem 4.1 (Minimal sufficient completion).** Given content S ⊆ X: among all closed sets containing S, find one of least structure.

**Theorem 4.2 (cl is the universal optimizer)** **[PROVEN]** *cl(S) is the unique solution of Problem 4.1, and it is optimal simultaneously for every strictly monotone objective: for any weights w : X → (0, ∞), cl(S) uniquely minimizes Σₓ∈C w(x) over closed C ⊇ S.*

*Proof.* Every feasible C satisfies cl(S) ⊆ C (Book I, Cor. 4.5). With strictly positive weights, a proper superset has strictly larger weight; hence cl(S) is the unique minimizer, for every such w at once. □

*Consequence: below the level where magnitudes matter, there is no optimization problem — the order decides. The framework's central object was already the optimizer of the session's optimization, under every objective simultaneously.*

**Theorem 4.3 (Two flows, one endpoint)** **[PROVEN]**
*Fix content S. Define the ascending flow S, D(S), D²(S), … (resolution) and the descending flow: from any closed C ⊇ S, repeatedly pass to any closed C′ with S ⊆ C′ ⊊ C while one exists (compression relative to S). Then:*
1. *the ascending flow terminates at cl(S);*
2. *every maximal descending flow terminates at a closed set containing S with no closed proper subset containing S — and cl(S) is reachable from every start, being contained in all of them;*
3. *the descending flow from any C terminates at cl(S) itself whenever the compression is exhaustive (always removes removable elements outside cl(S)); in particular, descending from C = X reaches cl(S).*

*Proof.* (1) Book I, Thm 4.8. (2) Finite strict descent terminates; feasibility (closed, ⊇ S) is maintained by construction; cl(S) ⊆ C at every stage by Cor. 4.5. (3) If C ⊋ cl(S), then cl(S) itself witnesses a legal step C ⇝ cl(S) (or any intermediate); exhaustive compression therefore cannot halt above cl(S), and cannot pass below it by (2). □

*Resolution ascends, compression descends, and both stop at the generated closure — the least structure that is both complete and sufficient.* That sentence is the theorem-grade version of the session's page-one summary.

---

### Chapter 5. The Selection Boundary: Where Choice Begins

**Definition 5.1.** Two closed sets are **comparable** if one contains the other; else **incomparable**.

**Proposition 5.2 (Order decides comparable cases)** **[PROVEN]** *Between comparable feasible closed sets, every strictly monotone objective prefers the smaller; no functional information is needed beyond the order.* (Immediate from the argument of Thm 4.2.)

**Proposition 5.3 (Only incomparability requires a functional)** **[PROVEN]** *If C₁, C₂ are incomparable closed sets, there exist strictly positive weightings w, w′ with Σ_{C₁} w < Σ_{C₂} w and Σ_{C₁} w′ > Σ_{C₂} w′.*

*Proof.* Pick x₁ ∈ C₁∖C₂ and x₂ ∈ C₂∖C₁ (exist by incomparability). Let w load nearly all weight on x₂, w′ on x₁, ε > 0 elsewhere; the two inequalities follow for ε small. □

**The boundary, stated plainly.** Structure alone (the lattice of Book I, Thm 4.17) settles every comparable choice. Between incomparable closed structures — hexagonal versus square packing; one fold versus another — *no order forces the outcome, and Proposition 5.3 shows no functional is canonical without further input.* The further input is exactly the Bridge Paper's **Level 2**: magnitudes, the weight r, physical objective functions. Therefore:

> **Selection = optimization over an antichain of the closure lattice, under a Level-2 functional.** *(working — the definition is exact; which functional nature uses is the physics.)*

Geometry and physics do not enter the framework by decree; they enter at the first incomparable pair. The lattice of closed sets is the **phase space** of the theory: all canonical dynamics is monotone motion on it (up to identity, Thm 3.1; down to sufficiency, Thm 4.3), and everything not decided by that motion lives on antichains.

**Remark 5.4 (Snowflake and cloud).** A snowflake is a dependency system at its fixed point: R\* = 1, an antichain selection locked in by the 2D density functional (Bridge Paper §2, the A₂ story). A cloud is a system held away from its fixed point — external dependency injected faster than resolution closes it: R\* < 1 sustained. The two observations that sparked this book are the two regimes of Theorem 3.1. *(working reading; established mathematics beneath it)*

---

### Chapter 6. Known Optimization as Special Cases (Goalpost 4, split honestly)

**Theorem 6.1 (Exact case: Horn-clause inference)** **[PROVEN]** *Let elements be atomic propositions plus one node per Horn clause, with δ(clause-node) = its body atoms and δ(head) ∋ clause-node for each clause deriving it — or directly: for a definite Horn program P, define δ(head of clause) ⊇ body of clause. Then forward chaining from facts F computes exactly Dⁿ(F) in reverse, and the minimal model of P over F corresponds to a generated closure. Logical closure of definite programs is an instance of cl.*

*Proof sketch (full construction routine).* Forward chaining adds a head when all body atoms are present; D adds dependencies when the dependent is present. Orienting δ from heads to bodies makes "S closed" = "S supports everything it asserts," and cl(goal) = the minimal support set; the classical least-fixed-point semantics of definite programs (Knaster–Tarski on a monotone operator) is the same lattice-theoretic fact as Book I Thm 4.8. □

**Correspondences 6.2** *(working — same shape, not yet theorems)*
- **Packing / crystallization:** maximize a density functional over the antichain of admissible lattices — the Chapter 5 template with w = geometric density. Exact once Level 2 supplies the functional.
- **Protein folding:** maximize satisfied bonds (resolved constraints) subject to chain admissibility — a constrained ascent of a resolution-like quantity.
- **Least action / minimal energy:** select among incomparable admissible histories by a magnitude functional — the template again; the identification of the functional with action is entirely Level 2/3 physics.

Tag discipline: 6.1 is a theorem; 6.2 is a shape. The framework earns the word "unification" only as 6.2's entries are promoted, one proof at a time.

---

### Chapter 7. Scoreboard and the Page-One Sentence

**The four goalposts of the resolution session:**

| # | Goalpost | Status |
|---|---|---|
| 1 | Define the functional | **Green** — R\* = |S|/|cl(S)|, derived, zero new primitives (Def 2.2) |
| 2 | Prove monotonicity | **Green** — Lyapunov theorem (Thm 3.1); original ratio refuted first (Prop 1.3) |
| 3 | Characterize fixed points | **Green** — fixed points of D = closed sets = R\* = 1 (Thm 3.1.3); optima = generated closures (Thm 4.2) |
| 4 | Known problems as special cases | **Split** — Horn inference exact (Thm 6.1); packing/folding/action shaped, awaiting Level 2 |

**Primitive ledger:** unchanged — elements, dependency. Resolution, density, optimization, and selection all entered the derived column. The session's instinct that "one more compression" existed was right, and the compression was of the session's own proposal: Resolution failed the deletion test *in the good way* — it is a theorem about closure, not a new axiom beside it.

**Page one:**

> *A dependency system defines unresolved constraints against a fixed identity, the generated closure. Resolution ascends toward that identity and compression descends toward it; both are monotone, both terminate, and both stop at the same object — the least structure that is complete and sufficient. Everything the order decides is thereby decided. Genuine selection begins only between incomparable completions, and the functional that decides those is where physics enters.*

**Hand-off to the Bridge Paper.** This book closes the structural half of Level 2's doorway: it proves *where* a magnitude functional is needed (antichains, Prop 5.3) and *that* nothing below that point needs one (Thm 4.2). What remains of Level 2 is unchanged and now sharper: derive the functional — the weight r and its multiplicative composition — and the snowflake deduction's link 2 becomes the first physical instance of Definition 5.1's selection. The corrected architecture:

```text
Dependency  →  Closure (identity)  →  Resolution R* (ascent, Thm 3.1)
                                   →  Compression (descent, Thm 4.3)
            →  Lattice = phase space (Book I Thm 4.17)
            →  Selection on antichains (Def 5.1)  →  Level 2 functional  →  Realization
```

---

---

#### Section B — Filtration

Part One located where selection begins: on antichains, where order is exhausted and a functional must decide. Part Two is what selection *is* once it is running — compressed, by the deletion algorithm of Book 0, to one object.

---

### Chapter 8. The Filtration Primitive

#### 8.1 The compression

The working vocabulary of selection had four components: a residual space of admissible candidates, constraint operators that cut it down, the descending sequence of cuts, and the realization at the end. Run the deletion algorithm on each:

| Component | Certificate | Verdict |
|---|---|---|
| Constraint operators | reconstruction: any operator sequence is *one presentation generating* the filtration; the filtration retains everything the theorems use | representation |
| Realization | reconstruction: it is the limit ⋂ₙ Rₙ, already contained in the filtration | representation |
| Residual space | reconstruction: it is R₀, the filtration's first term | representation |
| **Filtration** | independence proof to Book 0 standard not yet supplied | **primitive (provisional)** |

**Definition 8.1 (Filtration).** A **filtration** on a finite universe X of candidates is a descending chain
$$R_0 \supseteq R_1 \supseteq R_2 \supseteq \cdots$$
of subsets of X. It is **generated by a constraint family** 𝐼 = (I₁, I₂, …) — each Iₖ a predicate on candidates — when Rₙ = R₀ ∩ {x : I₁(x), …, Iₙ(x)}; nesting is then automatic.

**Remark 8.2 (The symmetry with Book I).** The demotion of constraint operators is the exact Book-II image of Book I's founding move: dependency graphs were presentations generating an invariant closure structure; constraint operators are presentations generating an invariant filtration. Different operator sequences can generate the same chain, and every Part Two theorem uses only the chain. The parallel is method, not coincidence: both are single applications of Book 0's algorithm, and the provisional tag on the surviving primitive is carried in both books for the same reason (Book 0, Rem 0.6: primitivity needs an independence certificate, and neither book has supplied one yet — Book 0, OP 0.2 now covers both).

#### 8.2 Indistinguishability

**Definition 8.3.** Candidates x, y are **𝐼-indistinguishable**, written x ≡_𝐼 y, if Iₖ(x) = Iₖ(y) for every constraint in the family. An equivalence relation, by inspection.

This is the object-level shadow of Book 0's invariance: the constraint family plays the role of the invariant set, and ≡_𝐼-classes are what the current theory *can see*.

---

### Chapter 9. Convergence and Extension Necessity

#### 9.1 What is trivial and what is not — said out loud

That |⋂ₙ Rₙ| is zero, one, or greater than one is a fact about cardinality, true of any set; stated alone it is bookkeeping, not a theorem. The content of this chapter is threefold: the limit is *attained* (9.4.1); the three outcomes carry forced *interpretations* (9.4.2); and the third outcome carries a genuine theorem — the survivors' ambiguity is provably irreducible by the existing constraint family (9.5). The chapter is written so that a referee can locate the content and skip the bookkeeping.

#### 9.2 The theorems

**Theorem 9.4 (Filtration Convergence)** **[PROVEN]**
*Let (Rₙ) be a filtration on finite X generated by a constraint family 𝐼. Then:*
1. *(Attainment)* *the chain stabilizes: there is N ≤ |R₀| with Rₙ = R_N for all n ≥ N, and R_∞ := ⋂ₙ Rₙ = R_N is attained in finitely many steps;*
2. *(Trichotomy with forced readings)* *exactly one of:*
   - *R_∞ = ∅ — the constraint family is inconsistent over R₀: no candidate satisfies all constraints;*
   - *R_∞ = {r} — the family determines a unique realization r;*
   - *|R_∞| > 1 — residual freedom survives every constraint in the family.*

*Proof.* (1) A descending chain of subsets of a finite set can strictly decrease at most |R₀| times; once Rₙ₊₁ = Rₙ under a generated filtration, all later terms coincide with it, since each later term intersects Rₙ with further constraints already… precisely: R_N = R_{N+1} means constraint I_{N+1} removes nothing from R_N; subsequent terms can still shrink, so take N as the last index of strict decrease, which exists since only finitely many strict decreases occur; then Rₙ = R_N for n ≥ N and the intersection equals R_N. (2) Cardinality of R_N. □

**Theorem 9.5 (Extension Necessity — the content of Case 3)** **[PROVEN]**
*Suppose the filtration has stabilized with |R_∞| > 1. Then:*
1. *any two survivors x, y ∈ R_∞ are 𝐼-indistinguishable: every constraint in the generating family is satisfied by both, so their value profiles over the family coincide;*
2. *consequently, any constraint J that separates two survivors is* **independent** *of the family 𝐼: J is not expressible as any function of (I₁, I₂, …). No strengthening, reweighting, or combination of existing constraints reduces R_∞;*
3. *the pair (x, y) is exactly an independence certificate in the sense of Book 0 (Padoa's method): two objects agreeing on every current invariant and yet distinct. Case 3 does not merely permit an extension of the invariant set — it constructively exhibits the certificate that one is required.*

*Proof.* (1) Every survivor satisfies every Iₖ by membership in each Rₙ; hence the value profile (I₁(x), I₂(x), …) = (true, true, …) is identical across R_∞, so all survivors are 𝐼-indistinguishable. (2) If J = f(I₁, I₂, …) for any function f, then J is constant on 𝐼-indistinguishability classes; by (1) all survivors lie in one class; so J cannot separate two of them — contrapositive gives independence. (3) Immediate comparison with Book 0, Remark 0.6: two admissible objects agreeing on all designated invariants and differing, which is Padoa's configuration verbatim. □

**Remark 9.6 (The series closes its loop).** Theorem 9.5.3 is, in the author's judgment, the most important structural fact in Part Two: *the top of the series and the bottom of the series are the same object.* Book 0's certificate for "this concept is primitive" and Book II's trigger for "a new invariant must be discovered" are one configuration — a Padoa pair — encountered at the meta level in the first case and at the object level in the second. Extension (Book III's verb) fires exactly when Deletion's certificate (Book 0's verb) appears among the survivors. The recursion of the series is therefore not an aesthetic arrangement; it is forced by the mathematics of indistinguishability.

**Remark 9.7 (What Case 3 rules out, practically).** Theorem 9.5.2 is a stop-loss for research effort: once stabilization with |R_∞| > 1 is verified, further work *inside* the current constraint family — tightening tolerances, recombining constraints, optimizing thresholds — provably cannot decide the outcome. The only productive move is orthogonal: a constraint carrying new information. In the Bridge Paper's vocabulary: when the audited observable ledger stabilizes with multiple admissible theories, the next test must probe a *new dependency chain*, not remeasure an old one more precisely. (Which is, notably, the structural argument for the Born-rule laboratory test over further cosmological tightening: it is the constraint most plausibly independent of the family already applied.)

#### 9.3 Non-uniqueness of generating families, for the record

**Remark 9.8.** Distinct constraint families can generate the same filtration (reorder two commuting constraints; replace one by an equivalent pair). By Remark 8.2 these are presentation differences; all Part Two theorems are invariant under them. The mirror of Book I Thm 3.7 and Book 0 Thm 0.8 holds a third time: the chain is the invariant; the family is the clock. Whether a canonical *minimal* generating family exists, and when it is unique, is the Part Two analogue of the minimal-presentation theorem *(open, expected tractable by the same covering-edge style of argument)*.

---

### Chapter 10. The Architecture, Final Form

The series, compressed to four verbs, each with its object and its theorem:

```text
Book 0    DELETE     representation        certificate asymmetry; objective stop  (Thm 0.7–0.8)
Book I    PRESERVE   invariant structure   presentation invariance; the attractor (Thm 3.4–3.5)
Book II   REFINE     residual freedom      convergence; extension necessity       (Thm 9.4–9.5)
Book III  EXTEND     the invariant set     begins at a Padoa pair in R_∞          (trigger: Thm 9.5.3)
```

Book III now exists (v0.2) under the charter Part Two supplied in one sentence: **Book III opens if and only if a stabilized filtration exhibits two survivors, and its first task is to find a constraint provably independent of everything before it.** Its opening condition, dichotomy, terminal-states theorem, and audit are written; the door has been walked through.

---

## PART THREE — REPRESENTATION EXTENSION

*What happens when refinement stalls: the Padoa pair, the terminal-states theorem, and the loop that closes the first three Parts into one recursion.*

### Preface

Book III does three things. First, it answers the open compression question that closed the last review round — *is filtration primitive, or the canonical presentation of independent invariant extension?* — with a theorem whose verdict is neither of the offered options (Chapter 1). Second, it develops the mathematics of extension itself: where new invariants come from, when none can come, and what the whole recursion terminates in (Chapters 2–4). Third, it runs the audit the series now demands of itself, and discharges the two provisional-primitive tags that Books I and II have been carrying (Chapter 5).

Tags as always: **[PROVEN]**, *(working)*, *(open)*.

---

### Chapter 1. The Reconstruction Theorem, and the Verdict

#### 1.1 Setup

Fix a universe X and a starting residual R₀ ⊆ X. A **constraint** is a predicate I : R₀ → {true, false}. A family (I₁, I₂, …) **generates** the chain Rₙ = R₀ ∩ {x : I₁(x), …, Iₙ(x)}. Call two constraints **residually equivalent at stage n** if they agree on Rₙ₋₁ (values elsewhere act on already-eliminated candidates and touch nothing downstream).

**Definition 1.1 (Effective independence).** Iₙ₊₁ is **effectively independent at stage n** if it is non-constant on Rₙ.

#### 1.2 The step theorem

**Theorem 1.2 (Step Independence)** **[PROVEN]** *For a generated chain, exactly one of three things happens at each step, and each is characterized by the new constraint's behavior on the residual:*
1. Rₙ₊₁ = Rₙ *(stall)* ⟺ Iₙ₊₁ *is constant-true on* Rₙ *— dependent: its value on the residual is a function (the constant function) of the accumulated profile;*
2. Rₙ₊₁ = ∅ *with* Rₙ ≠ ∅ *(annihilation)* ⟺ Iₙ₊₁ *is constant-false on* Rₙ *— an incompatibility, likewise dependent in form;*
3. ∅ ⊊ Rₙ₊₁ ⊊ Rₙ *(refinement)* ⟺ Iₙ₊₁ *is effectively independent at stage n.*

*Proof.* Rₙ₊₁ = {x ∈ Rₙ : Iₙ₊₁(x)}, and Rₙ is a single class of the accumulated indistinguishability (the all-true profile; Book II, Thm 9.5.1). Constant-true, constant-false, and non-constant on that class exhaust the possibilities and yield exactly the three set outcomes. A constraint constant on the residual is representable there as a function of the accumulated profile (a constant one); a non-constant one cannot be, by the argument of Book II Thm 9.5.2 restricted to the class. □

**Remark 1.3 (What the filtration is, then).** A filtration strictly refines exactly when an effectively independent invariant lands. So the chain of residuals is, step for step, **the record of independence events** — the sets shrink precisely when, and only when, something genuinely new is distinguished. (A globally novel constraint that happens to be constant on the current residual buys nothing: independence *where it matters* is the local notion, which is why Definition 1.1 is stated at the residual and not over X.)

**Corollary 1.2a (Residual Monotonicity)** **[PROVEN]** *Along any sequence of admitted constraints, the residual never increases: it is unchanged at dependent-true steps, strictly decreased at effectively independent steps, and annihilated at constant-false steps. Immediate from Theorem 1.2.* □

*Remark.* Deliberately small, and stated so that later quantities can measure themselves against it: any functional monotone under set inclusion — cardinality, and eventually any entropy- or information-styled measure a later book may introduce — inherits monotonicity along every run from this corollary alone. The invariant distinguishes; the residual records; nothing un-distinguishes.

#### 1.3 The reconstruction, both ways

**Theorem 1.4 (Reconstruction / Extension–Intension Duality)** **[PROVEN]**
*On a fixed (X, R₀) there is a bijection between:*
- *filtrations* R₀ ⊇ R₁ ⊇ R₂ ⊇ ⋯ *, and*
- *constraint sequences up to residual equivalence,*

*given by: a family ↦ its generated chain; a chain ↦ its membership constraints Iₙ(x) := (x ∈ Rₙ). Both round trips are the identity (the second up to residual equivalence, which is the correct notion of sameness for constraints).*

*Proof.* A family's generated chain is nested by construction. A chain's membership constraints generate it back: R₀ ∩ {x : x ∈ R₁, …, x ∈ Rₙ} = Rₙ by nesting. Conversely, starting from a family, the generated chain's membership constraint at stage n agrees with Iₙ on Rₙ₋₁ (there, x ∈ Rₙ ⟺ Iₙ(x)), which is residual equivalence. □

#### 1.4 The verdict — duality, not demotion

The review proposed demoting the filtration to a presentation of "independent invariant extension." Theorem 1.4 rules on the proposal, and the ruling is symmetric: **each side reconstructs the other.** By Book 0's own law (Theorem 0.8: compressed presentations are unique only up to interdefinability), when two candidates are interdefinable, *neither* is the primitive and neither is mere presentation — they are two canonical presentations of one invariant, and the primitive is their equivalence class.

And this particular pair has a classical name: it is the **extension/intension duality** — the sets-side and the predicates-side of one content. Book II's primitive, stated in its final honest form:

> **Primitive (Book II, final form): the refinement content — one invariant with two canonical presentations: extensionally, a filtration of residuals; intensionally, a sequence of effectively independent invariant extensions. Theorem 1.2 is the dictionary between them, step by step.**

The review's instinct that "one more compression" existed was half right: the compression exists, and what it removes is the *asymmetry* between the two vocabularies, not one of the vocabularies. The pattern now holds at every level of the series — Book I's dependency/closure, Book 0's transformations/invariants (the Galois pair of Rem 0.5), Book II's filtration/extension: **each book's foundation is a dual pair, and each book's founding theorem is the dictionary.** *(This regularity is recorded as an observation, not elevated to a principle — it has three instances, and three instances is a pattern to test, not a law; testing it is OP III.3.)*

---

### Chapter 2. The Extension Problem

#### 2.1 Existence is never the obstruction

**Proposition 2.1** **[PROVEN]** *If |R_∞| > 1, an effectively independent constraint exists: membership in any nonempty proper subset of R_∞.*

*Proof.* Such a subset exists (|R_∞| ≥ 2) and its membership predicate is non-constant on R_∞. □

So set-theoretically, extension is always available — which shows the real problem lies elsewhere. Not every predicate is *admissible*: the designation (Book 0, Primitive 0.1) fixes, along with everything else, which constraints count — lawful, definable in the theory's language, derivable from the axiom, measurable. Call that class the **invariant source** 𝒮.

**Definition 2.2 (The Extension Problem).** Given a stabilized residual R_∞ with |R_∞| > 1 and an invariant source 𝒮: *does 𝒮 contain a constraint effectively independent at R_∞?*

#### 2.2 The dichotomy

**Theorem 2.3 (Absolute residual freedom)** **[PROVEN]** *Exactly one of:*
1. *some* J ∈ 𝒮 *is effectively independent at* R_∞ *— then the recursion re-enters Book II and the residual strictly shrinks; or*
2. *every* J ∈ 𝒮 *is constant on* R_∞ *— equivalently,* R_∞ *is contained in a single class of the* 𝒮*-indistinguishability relation. Then the survivors cannot be separated by any constraint the designation admits, in any combination (Book II, Thm 9.5.2): the ambiguity is* **absolute relative to the designation***.*

*Proof.* The two cases are the negation of one another; the equivalence in (2) is the definition of ≡_𝒮 restricted to R_∞; the "in any combination" strengthening is Extension Necessity. □

**Remark 2.4 (The classical shape of Case 2).** Survivors agreeing on every admissible sentence and yet distinct is the shape of the classical independence phenomena of logic — elementarily equivalent non-isomorphic models; statements undecidable from the axioms, where two completions survive everything the theory can say. Book III does not claim those celebrated results; it observes that its Case 2 is the *same configuration*, met constructively: the series' machinery, run to its stopping point, halts exactly where logic says unremovable choices live. The route/object honesty of the whole series, once more.

**Remark 2.5 (The two exits from Case 2, and what "physics" formally is).** Absolute residual freedom has exactly two exits, and both leave Book III:
- **Upward:** enlarge the designation — admit new predicates into 𝒮. A Book 0 act, reopening the whole recursion one level up.
- **Sideways:** decide among theory-indistinguishable survivors by a *functional* — which is precisely Book II Part One's selection on antichains and the Bridge Paper's Level 2. And notice what this makes of the Bridge's "declared input": **an empirical measurement is formally an enlargement of the invariant source** — the act of admitting a predicate ("agrees with the observed value") that the axiom alone did not supply. The Bridge Paper's central legitimacy argument (§2.2: self-reading with labels) is thereby given its exact place in the series' mathematics: physics enters as designation enlargement, performed openly.

---

### Chapter 3. The Cost of Reaching Uniqueness

A small theorem with a sharp moral, new in this book.

**Proposition 3.1 (Discovery length)** **[PROVEN]** *Let |R₀| = m ≥ 2.*
1. *(Specification)* *If the target survivor may be named, one constraint suffices: membership in the singleton.*
2. *(Identification)* *If constraints must be committed before knowing which survivor is real — the worst case over targets — then at least ⌈log₂ m⌉ effectively independent constraints are required, and m − 1 always suffice.*

*Proof.* (1) Prop 2.1 with the singleton. (2) Lower bound: n binary constraint outcomes partition R₀ into at most 2ⁿ profile classes; identification means the true survivor's class is a singleton for every possible target, so 2ⁿ ≥ m. Upper bound: remove one non-target candidate per step; each such membership constraint is effectively independent while ≥ 2 remain. □

**Remark 3.2 (Specifying versus identifying).** The gap between 1 and ⌈log₂ m⌉ is the formal difference between *specifying* an answer and *identifying* one — between writing a constraint that names the realization and committing to constraints that must work whichever survivor is real. A framework that reaches uniqueness suspiciously fast is, by this proposition, either very lucky, in possession of unusually informative invariants, or aiming; the pre-registration discipline of the Bridge Paper (§4.2) is exactly the instrument that certifies which. The proposition turns that audit concern into a counting bound.

---

### Chapter 4. The Terminal States Theorem — the Series in One Statement

**Theorem 4.1 (Terminal States)** **[PROVEN]** *Let X be a finite set, A ⊆ X nonempty, and 𝒮 a set of functions X → {0,1} of which a finite subfamily 𝒮₀ ⊆ 𝒮 is designated* **obligatory** *(every run must apply each member of 𝒮₀) with the remainder* **elective** *(applicable only while non-constant on the current set). A* **run** *is a sequence of sets B₀ = A, Bₙ₊₁ = Bₙ ∩ Jₙ₊₁⁻¹(1), where each Jₙ₊₁ is an unapplied obligatory constraint or an elective constraint non-constant on Bₙ; a run halts when the obligatory family is exhausted and no member of 𝒮 is non-constant on the current set. Then:*
1. *every run halts within |A| − 1 + |𝒮₀| steps; and*
2. *its final set B satisfies exactly one of: B = ∅; |B| = 1; or |B| > 1 with every member of 𝒮 constant on B.*

*Proof.* (1) Each elective step strictly decreases a subset of the finite set A (elective constraints are non-constant on the current set, so remove at least one element and keep at least one — Thm 1.2.3), and there are at most |A| − 1 strict decreases; obligatory steps number exactly |𝒮₀|. (2) If B = ∅ or |B| = 1, every function is constant on B and the run has halted; the three listed conditions are mutually exclusive by cardinality and jointly exhaustive: if |B| > 1 and the run has halted, the halting condition says every member of 𝒮 is constant on B. □

**Remark 4.1a (Nomenclature and interpretation — kept outside the theorem deliberately).** The three outcomes are named: **contradiction** (B = ∅ — reachable only through an obligatory constraint that is constant-false at its application, Thm 1.2.2), **categoricity** (|B| = 1 — a unique realization determined by the admitted invariants), and **absolute residual freedom** (|B| > 1 with 𝒮 blind on B — the survivors indistinguishable by everything the designation admits; exits per Remark 2.5). These correspond structurally to familiar logical phenomena — inconsistency, categorical axiomatization, and undecidable choice among elementarily indistinguishable completions — a correspondence recorded here as interpretation, not as part of the mathematics above.

**Remark 4.1b (The obligatory family is falsifiability's address).** The obligatory/elective distinction was forced by the stress test of Appendix A and pays for itself immediately: elective constraints, chosen only while effective, can never empty the residual — so without 𝒮₀ the contradiction state is unreachable and the trichotomy silently collapses to two. What makes contradiction *possible* is precisely the existence of constraints one is not free to decline. In the Bridge Paper's vocabulary those are the **declared inputs** — observations, pre-registered comparisons — and the mapping is exact: *empirical refutation is the contradiction terminal state, and it exists in the formalism if and only if the designation carries obligatory constraints.* A framework with no obligatory family cannot be falsified by its own recursion; the Bridge's ledger is, in these terms, the series' 𝒮₀.

**Remark 4.3 (The whole series, read through Theorem 4.1).** Every construction in this series is one pass of a single terminating procedure:

```text
Book 0   DELETE     choose the designation; strip representation;
                    keep what survives Padoa                    (the certificate)
Book I   IDENTIFY   the invariant structure the designation
                    forces, with its attractor                  (the object)
Book II  REFINE     accumulate effectively independent
                    invariants; the filtration records them     (the record)
Book III EXTEND     at a Padoa pair among survivors, find an
                    independent admissible constraint — or
                    prove none exists and exit                  (the loop / the halt)
```

*and the procedure has exactly three possible ends* — contradiction, categoricity, or designation-relative ambiguity — *which are the three classical fates of a formal theory.* The recursion is genuine: Book III's Case 1 re-enters Book II; its Case 2 exits upward into Book 0 (enlarge the designation) or sideways into a functional (the Bridge). Nothing loops forever on a finite universe; nothing halts for reasons of taste. The one unforced act in the entire architecture is the one the architecture has always admitted: the designation at the top. Everything below it is now either a theorem or a labelled exit.

---

### Chapter 5. The Audit — Provisional Tags Discharged

Book 0's ledger (§6) and Book II's footer each carried a provisional-primitive tag pending an independence proof to Padoa standard (Book 0, Rem 0.6; OP 0.2). Book III supplies both certificates. Each is one exhibit long, which is what a healthy foundation's independence proofs should be.

**Theorem 5.1 (Book I's primitive is primitive)** **[PROVEN — OP 0.2, part 1, discharged]**
*The point-generated closure structure is not reconstructible from the remaining vocabulary of Book I (the carrier and its elements).*

*Proof (Padoa exhibit).* Take X = {a, b}. Model A: 𝒦_A = the full powerset (the discrete structure; every set closed). Model B: 𝒦_B = {∅, {b}, {a,b}} (the structure presented by a → b). Both are point-generated closure structures on the *same* carrier, with the carrier vocabulary (elements, equality, membership in X) interpreted identically; yet they disagree on the invariant statement Closed({a}). Two admissible models agreeing on everything except the candidate concept: by Padoa's method, 𝒦 is not definable from the rest, hence primitive. □

**Theorem 5.2 (Book II's primitive is primitive)** **[PROVEN — OP 0.2, part 2, discharged]**
*The refinement content (the filtration/extension dual pair of Thm 1.4) is not reconstructible from the remaining vocabulary of Book II (the carrier, R₀, and Book I's structure).*

*Proof (Padoa exhibit).* Take any X, R₀ = X, |X| ≥ 2, with any fixed closure structure. Model A: the constant filtration Rₙ = R₀ for all n. Model B: any strictly refining filtration (exists by Prop 2.1). Carrier, R₀, and 𝒦 identical; the invariant statement "some step is a refinement" (equivalently, by Thm 1.2, "some effectively independent invariant was admitted") differs. Hence the refinement content is not a function of the prior structure: primitive. □

**Updated series ledger.**

| Book | Primitive | Certificate | Status |
|---|---|---|---|
| 0 | the designation | immediate (nothing prior to reconstruct from; Book 0 §7) | certified |
| I | point-generated closure structure | Padoa exhibit, Thm 5.1 | **certified (was provisional)** |
| II | refinement content (filtration ⇄ extension dual pair) | Padoa exhibit, Thm 5.2 | **certified (was provisional)** |
| III | none claimed | — | Book III adds theorems, not primitives: its objects (𝒮, ≡_𝒮, terminal states) are all defined from the designation and Book II |

That last row is itself an audit result worth stating: Book III passes the deletion algorithm *empty-handed* — every concept it introduces is reconstructible from what came before. The extension book adds no primitive to extend. The series' total primitive count, top to bottom, certified: **three** — a designation, a structure, a refinement content — of which the first is a choice and the other two are dual pairs.

---

### Chapter 6. Open Problems of Book III

**OP III.1 (Canonical extension).** In Case 1 of Theorem 2.3, many effective constraints may exist. Is there a canonical choice — maximally informative (nearest to halving the residual, per Prop 3.1's bound), or minimal in a definability order on 𝒮? This is Book III's analogue of the minimal-presentation question, third instance of the pattern.

**OP III.2 (Infinite universes).** Theorem 4.1's termination uses finiteness. Formulate the transfinite recursion and determine which terminal states survive (stabilization may need ordinal stages; absolute freedom may become the generic case).

**OP III.3 (The dual-pair pattern).** Every book's foundation so far is a dual pair with a dictionary theorem (§1.4). Test whether this is forced by the method — a theorem of Book 0 about what deletion-stable foundations must look like — or an artifact of three samples.

**OP III.4 (The source hierarchy).** Designation enlargements (Rem 2.5) can be iterated: 𝒮 ⊆ 𝒮′ ⊆ 𝒮″ ⋯. Characterize the fixed points of that outer recursion — designations that admit no enlargement resolving their own absolute freedom — and their relation to the classical limitative theorems, stated with the care that comparison demands.

---

### Appendix A — The Translation Test (and what it caught)

The final challenge of the stress-test round: prove Theorem 4.1 **without the words** *refinement*, *filtration*, or *residual*. If the proof survives translation, the theorem is attached to invariant content rather than vocabulary — a Book 0 test applied to Book III's own centerpiece.

#### A.1 The vocabulary-free statement and proof

**Theorem A.1.** *Let X be a finite set, A a nonempty subset of X, 𝒮 a set of functions from X to {0,1}, and 𝒮₀ a finite subfamily of 𝒮. Consider sequences B₀ = A, Bₙ₊₁ = Bₙ ∩ Jₙ₊₁⁻¹(1), where each Jₙ₊₁ is either an element of 𝒮₀ not yet used, or any element of 𝒮 taking both values on Bₙ; the sequence stops when every element of 𝒮₀ has been used and every element of 𝒮 takes one value on the current set. Then every such sequence stops after at most |A| − 1 + |𝒮₀| terms, and its final set B satisfies exactly one of:*
1. *B has no elements;*
2. *B has one element;*
3. *B has more than one element, and every function in 𝒮 takes a single value on B.*

*Proof.* A function taking both values on Bₙ yields Bₙ₊₁ nonempty and strictly smaller; strict decreases among subsets of the finite set A number at most |A| − 1; the used-once elements of 𝒮₀ number |𝒮₀|; so the sequence stops. At the stop: if B has zero or one element, every function takes a single value on it vacuously or trivially and cases (1)/(2) apply; otherwise the stopping condition itself is case (3). The cases exclude one another by counting elements. □

Only sets, functions, values, intersections, and counting appear. The theorem survives translation. **But:**

#### A.2 What the translation caught

Writing A.1 exposed a defect in the *original* Theorem 4.1 that seven prior stress tests, including the dedicated exhaustiveness test, had passed over. The original procedure applied only constraints that are non-constant on the current set — and such a constraint always leaves a **nonempty** proper subset. Under the original procedure, the empty terminal state was therefore *unreachable*: the celebrated trichotomy was, procedurally, a dichotomy wearing a third label.

The repair is the obligatory/elective distinction now built into Theorem 4.1 and Theorem A.1: constraints one is free to choose can only ever distinguish; constraints one is *not* free to decline — the obligatory family 𝒮₀ — are the sole source of annihilation, hence of the contradiction state, hence of falsifiability (Remark 4.1b). The gap was not terminological; it was a missing structural ingredient that the vocabulary happened to be papering over — *residual* and *filtration* quietly suggested that emptying was among the things filtering does, and the bare-set restatement refused the suggestion.

Recorded per the series' registry discipline: the translation test is hereby promoted from a one-off challenge to a standing instrument. **Any theorem serving as a book's centerpiece must survive restatement in the vocabulary of the book below it.** Theorem 3.4 of Book I made this a guarantee for L_cl-statements; Appendix A makes it a required *practice*, because the guarantee only covers statements already written invariantly, and the practice is how one discovers the statements that aren't.

#### A.3 Status of the independent-verification requests

For the registry, the round's outstanding external checks: the Padoa exhibits (Thms 5.1–5.2) received a tentative pass and a request for *reconstruction from scratch by another prover* — a request this document cannot satisfy about itself, since author-verification is not independence; it stands open and assigned outward. The minimal-presentation theorem (Book I, Thm 3.7) carries the same standing request from an earlier round. Both are the correct kind of debt for a foundation to carry visibly: named, small, and payable by anyone.

---

## PART FOUR — REALIZATION THEORY

*Completing the architecture: what invariant structure looks like from outside, as geometry and scale.*

### Preface to Part Four: The End of Object-First Theory

Classical theory begins with objects. It asks what a point is, what a space is, what a manifold is, what a field is, what a particle is, what a geometry is. The object is placed first; the law is then written over it.

The three Parts behind this one reverse that order, and this Part states the reversal in its terminal form.

The primitive is not an object. The primitive is a compatibility law: a universe of local configurations, an invariant source of admissible predicates, and an obligatory observational family. A system enters the theory only through this law. Everything else is downstream.

That is the point at which the whole book becomes a compiler.

It does not begin by choosing a geometry. It begins by asking which configurations remain admissible after invariant-preserving refinement. It does not begin by choosing a manifold. It asks which manifold types can faithfully realize the scaling behavior forced by the compatibility law. It does not begin by choosing a physical object. It asks what can appear as a stable carrier of invariant content.

This Part is therefore not an application chapter tacked onto a finished theory. It is the place where representation, reduction, invariant structure, refinement, and extension are converted into realization — and, where the mathematics permits, actually carried out rather than merely promised. Roughly half of what follows is proven outright; the other half is stated as precisely as an open problem can be stated, with the boundary between the two marked at every step, in keeping with the whole book's discipline.

The doctrine of this Part:

```text
Objects are terminal.
Compatibility is primitive.
Scaling is a candidate invariant signature of realization.
Geometry is output.
```

The governing question is no longer:

```text
What exists?
```

It is:

```text
What can exist as a faithful realization of a compatibility law?
```

---

### Chapter 1. Compatibility Laws

#### 1.1 The Entry Point

A system enters this Part through a compatibility law — already fixed as Definition C.1 in the Coda, restated here at its point of use.

**Definition 1.1 (Compatibility Law).** A compatibility law for a system is a triple $(X, \mathcal{S}, \mathcal{S}_0)$ where:

- $X$ is a finite universe of local configurations;
- $\mathcal{S}$ is an invariant source of admissible predicates on $X$;
- $\mathcal{S}_0 \subseteq \mathcal{S}$ is an obligatory family, recording the observational constraints already imposed.

The word "system" has no further primitive content in this Part. Two systems with the same compatibility law are indistinguishable to the theory until a faithful reconstruction theorem separates them (Chapter 11).

This is the first discipline of Realization Theory:

> Systems are compared through compatibility laws, never through their realized shapes.

#### 1.2 The Methodological Inversion

The direction of explanation, fixed as law in the Coda, restated here:

$$\text{Observation} \;\to\; \text{Compatibility Law} \;\to\; \text{Framework} \;\to\; \text{Necessary Consequences}.$$

Observation does not arrive as a conclusion. It enters as obligation. Once it has entered, the theory computes what must follow. This is why the contradiction terminal state (Part Three, Thm 4.1; §9 below) is not an embarrassment but a structural feature: if the obligatory family is incompatible with the invariant source, refinement must expose that incompatibility.

Realization Theory is therefore not a theory of arbitrary construction. It is a theory of admissibility.

#### 1.3 Equivalence of Compatibility Laws

Two compatibility laws are equivalent when they generate the same invariant content under refinement — the Part Four instance of the faithful-representation discipline that has governed every Part so far (Part One, Thm 3.4; Part Two/Three, Thm 1.4).

**Definition 1.2 (Compatibility Equivalence).** Two laws $(X, \mathcal{S}, \mathcal{S}_0)$ and $(Y, \mathcal{T}, \mathcal{T}_0)$ are **compatibility-equivalent** when there exists a bijective correspondence between their residual refinement sequences that preserves, at every stage: residual inclusion, the admissible continuation set, the distinguishability classes, and the terminal state reached.

This definition deliberately avoids identifying the underlying sets $X$ and $Y$. The point is not whether they look alike. The point is whether refinement sees the same invariant content — the same discipline as Part One's presentation-invariance, one level up.

**Proposition 1.3 (Compatibility-equivalent systems have equivalent refinement dynamics)** **[T]** *If $(X,\mathcal{S},\mathcal{S}_0)$ and $(Y,\mathcal{T},\mathcal{T}_0)$ are compatibility-equivalent, then their residual-size sequences, branching sequences (Ch. 3), distinguishability sequences (Ch. 3), and terminal signatures (Ch. 9) coincide under the correspondence.*

*Proof.* Each of the four listed quantities is defined purely from the data Definition 1.2 requires to be preserved at every stage (residual inclusion gives residual size; the continuation set gives branching directly, Def. 3.1; the distinguishability classes give $D(n)$ directly, Def. 3.2; the terminal state is preserved by hypothesis). A correspondence preserving all four inputs stagewise preserves everything computed from them. □

Proposition 1.3 is deliberately immediate — it is the check that Definition 1.2 asked for exactly the right things, not less. Every later chapter's reconstruction theorems (Ch. 11) must produce a correspondence of this exact shape before any hot-swap of vocabulary — graph, manifold, operator algebra — is licensed.

---

### Chapter 2. Residuals and Realization Space

#### 2.1 Residuals

Given a compatibility law, refinement produces the descending sequence already constructed and proven to terminate in Parts Two and Three:

$$R_0 \supseteq R_1 \supseteq R_2 \supseteq \cdots$$

Each $R_n$ is the residual set of configurations not yet eliminated by the constraints imposed up to stage $n$.

The residual is not a psychological uncertainty. It is not merely what an observer does not know. It is the current admissible content of the system under the compatibility law — the same object Part Two's filtration and Part Three's run construct, read here as the raw material of realization rather than as an object of pure refinement theory.

#### 2.2 Realization Space

**Definition 2.1 (Realization space).** The **realization space** of a compatibility law is the refinement history of its residuals: the sequence $(R_0, R_1, R_2, \ldots)$ together with the constraint that generated each step.

This is a deliberate correction of an intuitive but wrong picture. The realization space is not the set of all imaginable worlds. It is not a background container in which the system happens to sit. It is the structured remainder left by obligatory compatibility — a record, not a stage.

$$\text{Realization space} = \text{residual history under refinement.}$$

#### 2.3 Realization as Stabilization

A realized structure is not chosen from outside the theory. It is the stable carrier of invariant content after refinement has done all it can do without forced extension (Part Three, Ch. 2).

**Definition 2.2 (Stable Realization).** A structure $G$ is a **stable realization** of a compatibility law if:

1. $G$ faithfully represents the invariant content of the residual sequence;
2. $G$ remains invariant under all admissible reductions of presentation;
3. $G$ preserves the terminal distinguishability relation;
4. $G$ introduces no unlicensed distinctions.

Condition 4 is essential and is the Part Four instance of Part One's Occam-shaped discipline (the generated closure as least sufficient structure, Part One Thm 4.2, applied here to realizations rather than closed sets): a realization may fail by omission, but it may also fail by excess. Extra geometry is still extra structure, and extra structure is a claim that must be paid for — the No-Excess Rule of Chapter 5.

---

### Chapter 3. The Three Monotone Clocks

This Part inherits three clocks from the machinery already built. At fixed designation, each is non-increasing along refinement — proven here in full, not merely asserted, because Chapter 4's scaling programme is only as trustworthy as this chapter's floor.

#### 3.1 Residual Size

Residual size records how much of $X$ remains admissible: $|R_n|$. It measures collapse of the admissible universe, and its termination was proven in Part Two (Thm 9.4) and Part Three (Thm 1.2.3).

#### 3.2 Branching

**Definition 3.1 (Branching).** At stage $n$, the **admissible continuation set** is
$$A_n = \{\, J \in \mathcal{S} : J \text{ is non-constant on } R_n \,\}, \qquad B(n) = |A_n|.$$
Branching is the cardinality of the admissible continuation set under the current compatibility law — not paths, not edges.

**Theorem 3.1 (Branching Collapse)** **[T]** *Along any run at fixed designation, $A_{n+1} \subseteq A_n$, hence $B(n+1) \le B(n)$. The inequality also holds under the successor-set reading of "continuation": the number of distinct sets $\{R_n \cap J^{-1}(1) : J \in A_n\}$ is likewise non-increasing.*

*Proof.* A constraint constant on $R_n$ is constant on every subset, in particular on $R_{n+1}$; contrapositively, non-constant on $R_{n+1}$ implies non-constant on $R_n$, giving $A_{n+1} \subseteq A_n$. For the successor-set reading: if $J, J'$ induce distinct successors of $R_{n+1}$, they differ at some point of $R_{n+1} \subseteq R_n$, hence induce distinct successors of $R_n$; the induced map on distinct successors is therefore injective upward. □

*Robustness note.* The theorem was checked under both candidate readings of "continuation" during the definition's stress-testing and holds under each; Definition 3.1 is fixed on the constraint-set reading for cleanliness, not necessity.

#### 3.3 Distinguishability

**Definition 3.2 (Distinguishability).** $D(n)$ is the number of $\mathcal{S}$-equivalence classes ($x \equiv_\mathcal{S} y$ iff every $J \in \mathcal{S}$ agrees on $x,y$) still meeting $R_n$.

**Theorem 3.2 (Distinguishability Monotonicity)** **[T]** *Along any run at fixed designation, $D(n+1) \le D(n)$.*

*Proof.* A class meeting $R_{n+1}$ meets $R_n \supseteq R_{n+1}$. □

When distinguishability falls, the law has compressed distinctions. When it plateaus without reaching 1, the law has encountered an extension boundary (Part Three, Thm 2.3 Case 2) — see Chapter 9.

#### 3.4 The Realization Signature

**Definition 3.3 (Realization signature).** The joint behavior $(|R_n|, B(n), D(n))$ is the **realization signature** of a system at stage $n$.

**Corollary 3.3 (The clocks never run backward)** **[T]** *At fixed designation, residual size, branching, and distinguishability are all non-increasing along every run — immediate from Part Two/Three's residual monotonicity plus Theorems 3.1–3.2.*

This corollary is the first hard constraint on geometry, restated as a governing principle for everything below: **a proposed geometry is not admissible because it is elegant. It is admissible only if it realizes the clock behavior forced by the compatibility law.** The open question this Part exists to make progress on is not whether the clocks fall — that is settled — but *how fast*.

---

### Chapter 4. Scaling Classes

#### 4.1 Scaling Before Geometry

The most important sentence in this Part, stated with the care its earlier draft was asked to observe:

> Within this programme, scaling laws are investigated as candidate invariants across families of realizations.

Geometry may change under faithful representation. Whether scaling class is fully invariant is a question this Part makes progress on (Theorem 4.7) without closing entirely (§4.4's floor family is itself a scaling result still being mapped).

This is the same discipline that has governed every Part: representations may change; invariant content may not. Here, the invariant content under investigation is no longer merely a closure structure or a terminal equivalence relation. It is the asymptotic pattern of refinement itself.

#### 4.2 Basic Scaling Classes

A first classification, by collapse rate:

| Class | Clock Behavior | Interpretation | Status |
|---|---|---|---|
| Finite collapse | reaches terminal state in bounded steps | rigid compatibility | proven possible (Part Three, Thm 4.1) |
| Polynomial collapse | ball volume grows like $r^d$ | graded refinement | proven, calibrated (Thm 4.9 below) |
| Exponential collapse | grows like $\lambda^n$, $\lambda > 1$ | strong contraction | proven, floor located (Thm 4.4–4.6) |
| Logarithmic collapse | decreases like $1/\log n$ | slow compression | *(open)* |
| Plateau collapse | stabilizes before uniqueness | unresolved equivalence (§9's Case 3) | proven to occur (Part Three, Thm 4.1.3); rate *(open)* |
| Oscillatory / periodic refinement | repeats a refinement profile | periodic admissibility | *(open — finite-universe case has no room to oscillate without stalling; genuinely needs OP-A's infinite extension)* |
| Critical refinement | sits between collapse regimes | boundary of universality | *(open)* |

Two rows are placeholders no longer; two remain exactly the honest open questions they were always going to be. The organizing principle throughout:

$$\text{Realization class} = \text{compatibility law} + \text{refinement scaling.}$$

#### 4.3 Universality of Scaling

Two systems may have different realized geometries but the same scaling class. When that happens, this Part regards them as belonging to the same **realization universality class**, provided the compatibility law and reconstruction data (Ch. 11) support the identification. This is why geometry cannot be the first classifier — it is too late in the chain (Ch. 6).

#### 4.4 Self-Similar Refinement Rules, and the Search for a Floor

The polynomial row of §4.2's table is calibrated in Chapter 6, once geometry has been constructed. The exponential row is calibrated here, by classifying the recursive compatibility laws directly.

**Definition 4.1 (Refinement rule).** A **refinement rule** on $k$ roles is a $k \times k$ matrix $M$ with entries in $\{0,1\}$, where $M_{ij} = 1$ iff one generation step of a role-$i$ region produces a role-$j$ region. A rule is **admissible** if it is primitive (some power of $M$ is strictly positive — every role eventually produces every role) and non-degenerate (not a permutation matrix — something actually refines, not merely relabels). The **asymptotic branching rate** of $M$ is its Perron eigenvalue $\lambda(M)$: role populations satisfy $v_{n+1} = M^{\mathsf T} v_n$, so total population grows as $\lambda^n$.

Refinement rules are the recursive compatibility laws — the smallest closed vocabularies a self-refining realization can have, and the natural place to ask what "slow" and "fast" scaling can mean.

**Theorem 4.4 (Extremal two-role self-refinement)** **[T]** *Among all admissible refinement rules on exactly two roles, the minimum asymptotic branching rate exceeding 1 is the golden ratio $\varphi$, attained by the Fibonacci rule*
$$M_{\mathrm{Fib}} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$
*(role A produces A and B; role B matures into A), and by its transpose.*

*Proof.* Finite enumeration, machine-verified. Of the sixteen $0$–$1$ matrices on two roles, primitivity holds for exactly three up to relabelling: $M_{\mathrm{Fib}}$ and its transpose, with characteristic polynomial $\lambda^2 - \lambda - 1$ and Perron root $\varphi \approx 1.618034$; and the all-ones matrix, with Perron root $2$. All others are reducible (some role never reaches the other) or are the pure swap (a permutation: $\lambda = 1$, degenerate). Hence the admissible spectrum on exactly two roles is $\{\varphi, 2\}$, with minimum $\varphi$. □

**Theorem 4.5 (Spectral pair of the extremal rule)** **[T]** *The Fibonacci rule's eigenvalues are $\varphi$ and $-1/\varphi$. Consequently, along the extremal two-role refinement, total population grows by factor $\varphi$ per generation, and every deviation from the leading composition decays by factor $1/\varphi$ per generation — growth and damping are reciprocal.*

*Proof.* $\lambda^2 - \lambda - 1 = 0$ has roots $\varphi$ and $1-\varphi = -1/\varphi$ (since $\varphi(\varphi-1)=1$); Perron–Frobenius makes $\varphi$ the leading eigenvalue; the complementary spectral projection carries all deviations, contracting by $|-1/\varphi| = 1/\varphi$ per step. □

**Is $\varphi$ the universal floor, over every role count?** No — and the record of finding that out is left in the text, because the correction is itself a demonstration of the book's law that no result may claim "the" extremal object without a proof of uniqueness over the *full* class in question (Coda, Law 5.2).

**Theorem 4.6 (The floor family; $\varphi$'s exact scope)** **[T]** *For each $k \ge 2$, consider the $k$-role rule $a_1 \to a_2 \to \cdots \to a_{k-1} \to a_k \to (a_1, a_2)$ — a cycle of length $k$ closed by one extra edge from the last role back to the second. This rule is admissible (cycles of coprime lengths $k$ and $k{-}1$ force primitivity), with characteristic polynomial $\lambda^k - \lambda - 1$. Its Perron root is strictly decreasing in $k$ — verified: $k{=}2$: $1.618034$; $k{=}3$: $1.324718$; $k{=}4$: $1.220744$; $k{=}5$: $1.167304$ — and tends to $1$ as $k \to \infty$, since for any fixed $\lambda > 1$, $\lambda^k$ eventually exceeds $\lambda + 1$. Consequently: the admissible refinement floor, taken over all role counts, is $1$, and it is not attained. $\varphi$ is extremal at $k = 2$, and only at $k=2$.*

*Proof.* As stated; primitivity from coprimality of the two cycle lengths ($k$ via the main loop, $k-1$ via the shortcut through $a_2$); the polynomial is read directly from the companion form of the rule; monotone decrease and the limit follow from comparing $\lambda^k$ against the fixed affine bound $\lambda + 1$. □

*What this buys, stated plainly.* The unqualified claim "the slowest possible way for something to keep making more of itself is the golden ratio" is false — it holds at exactly one scale, $k=2$, among infinitely many. What survives, correctly scoped: **$\varphi$ is the extremal rate for the minimum nontrivial number of roles.** Any claim resting on extremality alone must now say *which* extremality — global (false; Theorem 4.6 refutes it) or lexicographic: fewest roles first, then slowest rate (Theorem 4.4, exact). This distinction is carried forward to Chapter 12 and to Part Five, where it becomes hypothesis **U1$'$** rather than the unqualified U1 an earlier draft used.

**Theorem 4.7 (Trichotomy of refinement growth)** **[T]** *An admissible rule's canonical geometry falls in exactly one class: $\lambda(M) = 1$ is impossible for admissible rules (primitive non-permutation $0$–$1$ matrices have $\lambda > 1$); polynomial growth arises exactly from the degenerate/reducible rules excluded from admissibility (nilpotent-plus-identity structures — chains and their products, Theorems 4.9–4.10 below); admissible rules give exponential growth $\lambda > 1$, classified by Perron value, with $\varphi$ the floor at $k=2$ and no floor at all once $k$ is allowed to grow (Theorem 4.6).*

*Proof.* Assembled from Perron–Frobenius for primitive matrices, the enumeration of Theorem 4.4, and the calibrations of §6.3. □

*Consequence for the scaling table of §4.2:* the exponential row is now fully classified, with the corrected floor statement folded in; the polynomial row is classified in Chapter 6; the fractional-degree and logarithmic rows remain open, filed at the back of this Part.

---

### Chapter 5. Faithful Realization

#### 5.1 Faithfulness

**Definition 5.1.** A realization is **faithful** iff its induced invariant content equals the represented content — Definition C.4/C.4a's information-preservation, applied here to realizations rather than raw presentations.

Faithfulness has two directions:

$$\text{law} \to \text{realization}, \qquad \text{realization} \to \text{law}.$$

The first direction says the realization carries all required invariant content. The second says the realization carries no unlicensed invariant content.

#### 5.2 The No-Excess Rule

This Part adds a negative discipline to the positive ones inherited from before:

> Extra structure is a theorem debt.

If a realization contains geometry, topology, differentiability, metric data, algebraic symmetry, or boundary information not forced by the compatibility law, that structure must be either reconstructed from the law (Ch. 11) or explicitly marked as representational surplus. Silence on this point is not permitted by Law 5.3 (category separation).

#### 5.3 Representation Equivalence

**Definition 5.2.** Two faithful realizations of the same law are **representation-equivalent** when they preserve the same residual sequence, terminal relation, and scaling class.

This licenses the sentence: **different shapes may be the same realization content** — the geometric-level instance of the whole book's founding distinction between representation and invariant.

---

### Chapter 6. Geometry as Output

#### 6.1 The Late Arrival of Geometry

Geometry enters only after compatibility, refinement, and scaling. The wrong question is *what geometry does the system have?* The right question is *what geometry can realize this refinement scaling faithfully?*

#### 6.2 The Four Tests

A geometric carrier is admissible only if it passes four tests: **faithfulness** (preserves invariant content), **refinement stability** (remains coherent under continued refinement), **boundary compatibility** (carries the necessary terminal or extension data), and **scaling realization** (realizes the clock behavior of Chapter 3). Failure of any one test blocks the geometry as a faithful realization.

#### 6.3 The Canonical Metric

Geometry, on this Part's discipline, is not chosen. It is constructed — and for the domain this book has actually proven a closure theory for (Part One's point-generated structures), the construction is already complete.

**Theorem 6.4 (Canonical metric space of a closure structure)** **[T]** *Every point-generated closure structure* 𝒦 *canonically determines a metric space: its condensation X/∼ is a poset (Part One, Thm 4.12); a poset's minimal presentation is unique — the covering (Hasse) graph (Part One, Thm 3.7, trivial-condensation case); the graph distance d on that graph is therefore a function of* 𝒦 *alone and is presentation-invariant by construction.*

*Proof.* Composition of the cited theorems; each step is a function of 𝒦, so the result is an L_cl-object and Part One's Presentation Invariance (Thm 3.4) applies. □

Every invariant structure this book has proven the existence of already carries exactly one metric geometry — the geometry of its forced covering relations. What was missing until this Part was only the noticing: this passes all four tests of §6.2 by construction, since it is a function of 𝒦 and nothing else.

**Theorem 6.5 (Time–Geometry Correspondence)** **[T]** *On a T₀ structure presented by its covering presentation, the generation dynamics from x coincides with metric ball growth: Dⁿ({x}) is exactly the down-ball {y ⪯ x : d(x,y) ≤ n}, and the resolution function of Part One is normalized cumulative ball volume:*
$$R^{*}(D^n(\{x\})) = \frac{|B^{\downarrow}(x,n)|}{|\operatorname{cl}(x)|}.$$

*Proof.* Induction: D adds, at each step, exactly the covering-successors of current elements — extending reachability radius by one along covering edges; covering-path length downward is d restricted to the down-set. The R\* identity is Part One, Def. 2.4, applied to the ball. □

*Reading.* Part One's clock (generation depth) and this chapter's space (covering distance) are one structure parameterized two ways: **time is radius.** Part Five's hypothesis that physical time is generation depth becomes, geometrically, the claim that time is the radial coordinate of self-completion — unchanged in status, now geometric in content.

#### 6.4 Dimension

**Definition 6.6 (Growth degree).** For the canonical metric with ball volumes γₓ(r) = |B(x,r)|: the structure has **dimension d** if γ(r) ≍ rᵈ (uniformly in basepoint, over a growing family); **growth rate log λ** if γ(r) ≍ λʳ (the exponential class of Chapter 4). Dimension is a scaling exponent of the canonical geometry — the polynomial row of §4.2's table, made precise.

**Theorem 6.7 (Calibration)** **[T]** *The n-chain family has dimension 1; the n×n grid (product of two chains) has dimension 2.*

*Proof.* Chain: γ(r) = min(2r+1, n) — degree 1. Grid: the covering graph of a product poset is the Cartesian product of covering graphs, whose distance is the ℓ¹ sum; the ball volume is Σₖ s₁(k)γ₂(r−k) with sphere sizes s₁(k) ≍ k⁰, giving γ(r) ≍ r². □

**Theorem 6.8 (Dimension is additive)** **[T]** *If P has dimension p and Q has dimension q, the product structure P × Q has dimension p + q.*

*Proof.* γ_{P×Q}(r) = Σₖ s_P(k)γ_Q(r−k) with s_P(k) ≍ k^{p−1}; the convolution Σ k^{p−1}(r−k)^q ≍ r^{p+q}. □

*Consequence:* dimensional composition is free — a d-dimensional observable geometry is realized by any product of d one-dimensional refinement structures. Non-integer and exponential classes are Chapter 4's territory, not this construction's; §4.2's remaining open rows stay open.

#### 6.5 Geometry Is a Carrier

A geometry is not the system. It is a carrier of invariant content — Theorems 6.4–6.8 exhibit the carrier for Part One's domain; they do not elevate it to the system itself, which remains the compatibility law of Chapter 1. This lets the theory compare graphs, manifolds, lattices, and operator systems without collapsing them into one vocabulary prematurely.

---

### Chapter 7. Manifold Admissibility

#### 7.1 Manifolds Are Solution Types

A manifold type is not a primitive type of existence. It is a solution type for a compatibility law. This Part therefore classifies manifolds by admissibility role, not by traditional prestige.

#### 7.2 Provisional Classification

| Carrier Type | Admissibility Role | Status |
|---|---|---|
| Discrete space | finite residual classification | **proven instance**: chains and grids, Thm 6.7–6.8 |
| Topological manifold | continuity of residual neighborhoods | *(open — needs OP-A, the infinite-universe extension)* |
| Smooth manifold | differentiable refinement flow | *(open, as above)* |
| Metric manifold | quantified scaling realization | partially realized: Thm 6.4 supplies the discrete case; continuum limit is OP-A/U5 |
| Symplectic manifold | preserved pairing under refinement | *(open)* |
| Riemannian manifold | positive metric realization | *(open — continuum limit of Thm 6.4)* |
| Lorentzian manifold | indefinite causal realization | *(open — needs a signed refinement notion not yet built)* |
| Fibered manifold | separated base and internal compatibility | *(open — natural candidate: product structures, Thm 6.8, generalized beyond direct products)* |
| Stratified space | layered terminal or singular refinement | *(open — connects to §9's terminal-state taxonomy)* |
| Singular space | forced collapse of local regularity | *(open — connects to contradiction states, §9.1)* |
| Noncommutative space | order-sensitive realization where points are secondary | *(open — would require relaxing point-generation itself, cf. Part Zero's arity boundary, Thm 0.13)* |

This table is a chapter map, not a theorem — one row is discharged (discrete), several have a stated route to discharge, and honesty requires leaving the rest exactly as open as they are.

#### 7.3 The Manifold Constraint

**Theorem Schema 7.1** *(open, precise target stated).* A manifold type is admissible for a compatibility law only if its structural invariants reconstruct the law's residual scaling and terminal distinguishability. The single-sentence constraint every future manifold-admissibility theorem in this Part must satisfy.

---

### Chapter 8. Boundary and Extension

Extension is not a verb added after refinement. It is refinement's recursion clause — proven, not merely named, in Part Two (Thm 9.5.3) and taken up as Part Three's own charter: when refinement stalls at a Padoa pair, extension fires.

In this Part's vocabulary:

$$\text{extension} = \text{birth of a new realization boundary.}$$

A boundary is not merely an edge of a space. It is a locus where the current compatibility law cannot finish distinguishing without enlarging the source — Part Three, Remark 2.5's two exits (enlarge 𝒮, or decide by a Level-2 functional), read geometrically.

---

### Chapter 9. Terminal States

#### 9.1 The Finite Case — Proven

For finite universes, the terminal states are exactly the three of Part Three, Theorem 4.1, and their geometric signature is a theorem, not an observation:

**Theorem 9.1 (Terminal Signature)** **[T]** *At any terminal state of a finite run, the triple (|R|, B, D) — residual size, branching, distinguishability — takes exactly one of three values:*
$$(0,0,0), \qquad (1,0,1), \qquad (m,0,1) \text{ with } m>1.$$
*In particular B = 0 always, and D ≤ 1 always: every finite run terminates in total indistinguishability.*

*Proof.* Halting means no member of 𝒮 is non-constant on R: B = 0. If R = ∅, nothing is distinguished: D = 0. If |R| = 1, one class: D = 1. If |R| > 1, halting is Part Three Thm 2.3 Case 2: all survivors lie in one ≡_𝒮 class: D = 1. □

*Reading:* the procedure runs exactly until the framework can no longer see differences; refinement is the consumption of visible distinction, and Corollary 3.3's clocks are its meters.

#### 9.2 The Extended Taxonomy — Open, and Honestly Scoped

An earlier working draft of this Part listed seven terminal forms: empty residual, unique realization, equivalence class of realizations, periodic refinement, non-terminating asymptotic realization, contradiction state, extension-required state. Theorem 9.1 accounts for the first, second, third (as D = 1 with m > 1), sixth, and seventh exactly, in the finite case. **Periodic refinement** and **non-terminating asymptotic realization** have no room to occur under Part Three's finite termination guarantee (Thm 1.2.3 there: strict decrease on a finite set cannot cycle or run forever) — they are not additional finite cases the theorem missed; they are **genuinely infinite-universe phenomena**, correctly absent from a proof that assumes finiteness, and correctly present in a taxonomy built for the eventual infinite case. They are filed as such: real questions, filed under OP-A (the infinite-universe extension), not errors in Theorem 9.1's finite trichotomy.

---

### Chapter 10. Universality

Realization universality is the recognition that different carriers can instantiate the same refinement behavior. Two systems belong to the same **realization universality class** when they share: compatibility-law structure, residual scaling, branching scaling, distinguishability scaling, terminal type, and reconstruction data (Ch. 11). This is this Part's analogue of the classical notion of universality, stripped of substrate — and, per Chapter 4's honest scoring, it is fully classified only where the scaling itself is (the exponential and integer-polynomial rows); elsewhere it inherits those rows' open status.

---

### Chapter 11. Reconstruction Theorems

Every hot-swap requires a reconstruction theorem — the discipline that has governed the entire book since Part One's opening move (dependency graphs are presentations, not the object) and formalized in Part One Thm 3.4 and Part Two/Three Thm 1.4. To replace a compatibility law with a graph, manifold, lattice, operator algebra, or category, one must prove:

$$\text{compatibility law} \to \text{representation}, \qquad \text{representation} \to \text{compatibility law}, \qquad \text{invariant content preserved both ways.}$$

No reconstruction theorem, no equivalence claim. This chapter is the enforcement clause; it is what prevents this Part from becoming metaphor. Its proven instances so far: the canonical metric of Theorem 6.4 (compatibility law → graph, one direction fully constructive); the presentation theorems of Part One (Thm 3.1) and Parts Two/Three (Thm 1.4) at the level below geometry. Its open instances: manifold, operator, and categorical carriers (Ch. 7; OP-F in the Coda's ledger).

---

### Chapter 12. The Completed Architecture

#### 12.1 The Chain, Stated Once, Fully Tagged

Everything else in this Part is theorem or open problem. This closing section is the assembled chain from proven structure to cosmological application — a map, not a proof, and marked as such at every link.

1. **[T]** A compatibility law fixes canonical dynamics, a canonical metric, and monotone refinement clocks (Chs. 1–3, 6).
2. **[T]** Self-similar realization is classified by refinement rules; the two-role admissible spectrum has floor φ (Thm 4.4), with spectral pair (φ, −1/φ) (Thm 4.5) — and, corrected in the same breath it was discovered, **no floor at all** once role count is allowed to grow (Thm 4.6).
3. **(U1′ — lexicographic extremal selection, superseding the uncorrected global claim.)** *Physical realization selects, first, the minimum number of roles admitting nontrivial self-refinement (two), and, second, the slowest admissible rate at that role count — jointly forcing the Fibonacci rule uniquely.* Falsifiable on both edges: a realized fundamental refinement with more than two roles at a rate below φ refutes the first clause; a realized two-role rate strictly in (1, φ) refutes the second — and the second edge is a standing consistency check on the identification itself, since Theorem 4.4 already proves no such rate exists among two-role rules.
3′. *(Recorded alternative.* Part Five's E8/heterotic route reaches structure by identification rather than by extremal selection; the two routes are not yet reconciled, and doing so is Part Five's own successor open problem.)
4. **(W)** Under U1′, the realized constants are the extremal spectral pair: growth φ per generation, damping 1/φ per generation — Unified Mechanics' axiom re-derived as Theorem 4.4's characteristic equation, its Born coefficient as Theorem 4.5's damping factor. Part Five's audit then governs every downstream number exactly as written there.
5. **(W)** Time is generation depth, which Theorem 6.5 identifies as the radial coordinate of the canonical geometry; the arrow is Corollary 3.3 (nothing un-distinguishes); space is the covering geometry of Theorem 6.4; dimension is growth degree (Def. 6.6), composable by products (Thm 6.8). *Open, stated plainly: nothing yet selects growth degree 3(+1) — the dimension-selection problem, with Part Five's E8 thread its only current candidate mechanism.*
6. **[T]+(W)** The universe-as-structure reading: the maximal self-closed realization, reading itself through obligatory constraints; refutation, uniqueness, and undecidable residual freedom are its only three finite-case fates (Part Three, Thm 4.1; §9.1 above), and every observation shifts it along Corollary 3.3's one-way meters. A self-measuring universe refines until it can no longer see differences at the current designation — and enlargement of the source (Ch. 8) is what "new physics" is, formally.

#### 12.2 What This Part Adds and What It Leaves

**Proven in this Part:** Proposition 1.3; Theorems 3.1–3.2, Corollary 3.3; Theorems 4.4–4.5, 4.6 (the corrected floor family), 4.7; Theorems 6.4–6.5, 6.7–6.8; Theorem 9.1 — fourteen results.

**Discharged or sharpened:** the extremality claim (corrected in the same chapter it first appears, per Law 5.2 — no unqualified "the" survives past its own statement); the terminal-state taxonomy (finite case closed, infinite case correctly relocated to OP-A); geometry's status (constructed, Thm 6.4, not imported).

**Left open, honestly:** the fractional-degree and logarithmic scaling rows (§4.2); manifold reconstruction beyond the discrete case (Ch. 7, 11); dimension selection (§12.1.5); the continuum limit (OP-A, threaded through this whole Part); the reconciliation of extremal selection with Part Five's identification route (§12.1.3′).

**The sentence this Part adds to the book**, now stated at the scope it has actually earned: *the slowest possible way for a two-part structure to keep making more of itself is the golden ratio, its errors die at the reciprocal rate, and the equation that says so is the axiom Part Five's physics started from — whether nature stops at two parts, and whether it takes the slow road at all, are each one falsifiable hypothesis, stated separately, neither smuggled into the other.*

What follows in Part Five spends this machinery on one physical framework, in the open, with every load-bearing claim tagged exactly as this Part has tagged its own.

---

### Appendix to Part Four A — Frozen Definitions

Consolidated from this Part; duplicates nothing already fixed in the Coda's Definitions C.1–C.4a, which this Part uses without restating.

- **Compatibility law:** $(X, \mathcal{S}, \mathcal{S}_0)$ — Def. 1.1 / Coda Def. C.1.
- **Residual, realization space:** Defs. 2.1 and surrounding §2.1–2.2.
- **Branching, distinguishability:** Defs. 3.1–3.2 / Coda Def. C.2–C.3.
- **Faithful realization:** Def. 5.1 / Coda Def. C.4–C.4a.
- **Refinement rule, admissibility, asymptotic branching rate:** Def. 4.1.
- **Scaling class, realization universality class:** §4.1–4.3, Ch. 10.
- **Canonical metric, growth degree:** Thm 6.4, Def. 6.6.

### Appendix to Part Four B — Open Problems

Specific to this Part; the master ledger spanning the whole book is in the Coda.

1. **Infinite universes (= Coda OP-A, instantiated here):** replace finite termination with ordinal-stage or asymptotic stabilization; needed before the logarithmic and oscillatory rows of §4.2, most of §7.2's table, and the continuum limit (U5) can move.
2. **Fractional-degree scaling rules:** which refinement structures realize non-integer growth degree; §4.2's remaining open row.
3. **Manifold reconstruction theorems:** discharge Chapter 7's table row by row, each via Chapter 11's two-way requirement.
4. **Dimension selection:** a mechanism forcing growth degree $3(+1)$ specifically — open, with the $E_8$ route of Part Five the only named candidate.
5. **Reconciliation of U1′ with Part Five's identification route:** are extremal selection and $E_8$ identification the same fact seen twice, or genuinely different claims — at most one can be the deeper explanation.
6. **Damping identification (U2):** does a physically realized system's per-cycle deviation decay match $1/\varphi$ exactly — Part Five's Born-coefficient laboratory test is this open problem's direct empirical probe.
7. **The 240 thread (U4):** whether the Pisano-period echo noted in Part Five, now attached to the same matrix family Theorem 4.4 studies, is signal or coincidence — recorded as a thread, weighted as a thread, pending Part Five's Route B.

---

## PART FIVE — FROM CLOSURE TO COSMOS

*The application: connecting the invariant machinery of Parts Zero through Four to Unified Mechanics, stated with a falsifier on every load-bearing claim.*

#### Preface

Paper I (*The Dependency–Closure Language, v1.0*) formalized the structural core that survived a long compression session: two primitives — elements and dependency — and one derived notion, closure, from which identity, order, and reduction all follow.

Unified Mechanics (UM) is the physical framework this compression began from: a single algebraic axiom, c² = c + 1, whose fixed point φ and contraction rate r = 1/(2φ) generate closed-form expressions for the cosmological energy budget, the cosmological constant, the dark-energy equation of state, the Born coefficient, the lepton hierarchy, and more.

This paper is the bridge between them. It does three things:

1. **Maps the correspondences** — the places where the abstract layer and the physical layer are visibly expressions of the same idea, stated carefully enough that each correspondence is either a result, a working hypothesis, or an open task, never a blur between the three.
2. **States the Bridge Problem** — the layered sequence of additions (magnitude, dynamics, geometry) that any route from pure structure to physical observables has to pass through, and where UM currently sits on each layer.
3. **Applies the language to the framework itself** — the audit. This turns out to be the natural conclusion of the whole project: the Dependency–Closure Language's first real application is to organize, discipline, and complete Unified Mechanics. A theory's claims form a dependency system. A theory is finished when that system is closed.

A word on tone. Paper I used hard status stamps, because a foundations document needs them. This paper keeps the same honesty with a lighter touch. Statements are marked inline as *(established)* — proved in Paper I or standard mathematics; *(working)* — a live hypothesis with stated content; or *(open)* — a task with a known shape. Nothing here is graded on enthusiasm. The spirit is the one the language was built in: nothing assumed, everything either earned or clearly labelled as still to earn.

One thing this paper does not do: it does not re-derive or certify UM's numerical results. Those derivations live in the UM papers and stand or fall on their own mathematics and on observation. What this paper adds is the connective structure — how each claim hangs together, what each one depends on, and what it would mean, precisely, for the whole framework to close.

---

---

### Part 1 — The Two Layers

#### 1.1 Layer S: structure

The Dependency–Closure Language, in one paragraph. A dependency system is a set of distinguishable elements X with a dependency assignment δ(x) ⊆ X. A set is *closed* when nothing inside it requires anything outside it. Every set has a unique smallest closed completion, cl(S) *(established — Paper I, Thm. 4.4/Cor. 4.5)*. The identity of a thing is its generated closure *(established — Def. 9.1)*; mutually dependent elements are one identity *(established — Thm. 4.12)*; the closed sets form a complete lattice *(established — Thm. 4.17)*. The layer is qualitative: it says what completeness, identity, and reduction *are*, and proves how they behave. It contains no numbers, no time, and no space — deliberately.

#### 1.2 Layer P: physics

Unified Mechanics, in one paragraph. The axiom c² = c + 1 has unique positive fixed point φ = (1+√5)/2; the contraction rate is r = 1/(2φ) ≈ 0.309. The identity (r + (1−r))² = 1 decomposes unity into three channel weights — light (1−r)² ≈ 0.4775, boundary 2r(1−r) ≈ 0.4271, matter r² ≈ 0.0955 — read as three modes of one self-referential operation. From r alone, UM writes closed forms for the cosmological constant (ρ_Λ/M_Pl⁴ = r²⁴⁰), the energy budget (Ω_b = r²/2, Ω_DM = 4r²(1−r), Ω_DE = 1 − 9r²/2 + 4r³), the dark-energy state (w₀ = −(r+2)/(8r)), the Born coefficient (1/φ = 2r), the intrinsic precision floor (ε = r³ ≈ 2.95%), and a longer table besides — with a falsification roadmap running from Euclid's 2026 dark-energy release through DESI's neutrino bound to a laboratory Born-rule test.

#### 1.3 How the layers relate

The relationship is precise and worth stating precisely, because it is easy to over- or under-claim.

Layer S is what remained when Layer P's *conceptual vocabulary* was compressed: recursion, execution, validation, identity, and observation were fed through the deletion test, and what survived was dependency and closure. In that sense Layer S is a distillate of Layer P's ideas.

But the distillation ran one way. Layer S does not derive Layer P; an abstract closure theory cannot, by itself, produce a value of Ω_DM. And Layer P does not prove Layer S correct; the physics could succeed or fail regardless of how elegant the abstraction is. In the vocabulary of Paper I's Rule (X6): **Unified Mechanics is a candidate model of a quantitative extension of the Dependency–Closure Language.** The extension itself — the additional axioms that let numbers, cycles, and eventually observables enter — is the subject of Part 3.

What each layer does for the other is discipline. Layer S gives Layer P a completeness criterion, an audit method, and a precise sense of "identity," "closure," and "reading itself" — words UM uses constantly and can now use formally. Layer P gives Layer S its reason to exist beyond mathematics, and a live testing ground for its open problems, especially the triadicity question.

---

---

### Part 2 — The Correspondences

Six places where the two layers meet. Each is stated with its standing.

#### 2.1 The axiom is a closure statement *(working)*

Rewrite the UM axiom. Divide c² = c + 1 by c:

$$c = 1 + \frac{1}{c}.$$

Read as a definition, this says: *the quantity c is defined in terms of itself, and the definition resolves.* The unique positive solution, φ, is the one proportion whose defining dependency closes — the value you get when "the whole relates to the part as the part relates to the remainder" is required to be self-consistent.

In Layer-S vocabulary: the equation's dependency graph is a single loop (c depends on c), and φ is the unique positive point at which that loop is a *closed* structure rather than a dangling one. The golden recursion is a one-element cyclic dependency system with a quantitative label — and Paper I established that cycles are legitimate closed structure (Remark 2.4, Example B.2): foundations need not bottom out; they may hold themselves up. φ is the numerical face of exactly that.

This gives the bridge its first working hypothesis:

> **(W1)** *c² = c + 1 is the minimal quantitative closure — the simplest self-referential condition that both closes and yields a nontrivial number — in the same sense that (elements, dependency) is the minimal qualitative one.*

UM's foundation paper already sketches the minimality argument (simplest nontrivial one-variable algebraic recursion, unit coefficients, representation-invariant fixed point). What would settle (W1) is a theorem: define the class of admissible quantitative self-closures explicitly, show the near-misses fail (x² = x closes but yields nothing; x² = 1 yields a number but no recursion; x² = 2x rescales away), and prove c² = c + 1 is the unique minimum of the class. That is a finite, purely mathematical task, and it would convert the axiom's motivation from an aesthetic argument into a selection theorem. It belongs near the top of the joint program.

#### 2.2 Identity, self-reading, and the declared input *(established as a translation; the physics remains the physics)*

Paper I's deepest single move was defining identity as generated closure: a thing *is* the total dependency structure it generates, and two presentations are the same thing when their closures coincide.

The *Shared Space* note made the corresponding move on the physics side: a self-contained universe has no external observer, so any complete self-description must be written from inside — the universe "reads itself," and the observed world is one of the axioms available to the system, not foreign information smuggled in.

The bridge translation: **the universe, in UM's picture, is the structure whose generated closure is itself.** There is nothing outside it for its dependencies to dangle into; it is the maximal closed set, and its self-description (observation) is a dependency that resolves internally.

This translation has one immediately practical consequence, and it resolves a question that used to loop endlessly: *is using an observed value cheating?* The answer the two layers give together is: it is neither cheating nor free. An observed value is a **declared input** — a legitimate internal axiom of a self-reading system, provided it is *declared*: labelled as an input in the dependency chain of whatever it supports. The distinction that matters is not "used data / didn't use data." It is "the chain says where every number came from / the chain doesn't." This becomes a load-bearing category of the audit in Part 4.

#### 2.3 The three channels and the triadicity question *(working — and the strongest single resonance)*

The compression session spent a long stretch on one question: does a self-validating system need a third irreducible role, or can two suffice? The session's honest endpoint was narrow and precise: every attempt to house validation in a binary system entangled the judge with the judged; and the moment a system must reason about the relation between its two participants, that relation gets promoted to a component of the structure — giving *A, R, B*: two participants and their reified relation. That was left as Paper I's Open Problem 1 — suggestive, not proved.

Now set that beside UM's channel decomposition, in UM's own words: the boundary channel β "is the algebraic linkage that ties matter and light into one universe, not a third species alongside them" — an anchor, an interface, the mediator through which matter and light couple, carrying the cross-term weight 2r(1−r), symmetric under exchange of the two things it links.

These are the same shape. The boundary channel is a physical candidate for the reified relation: not a third substance, but the relation-between promoted to a dynamical component, exactly as the abstract argument said would happen the moment the system must operate on its own linkage. Even the algebra cooperates: in (r + (1−r))² = 1, the participants enter as squares, r² and (1−r)², and the mediator enters as the *cross term* — the product of the two, doubled, which is where "relation between" lives in any squared sum.

So the bridge statement, carefully:

> **(W2)** *If Open Problem 1 resolves positively — if independent self-validation provably requires structure beyond two participants — then UM's three-channel decomposition acquires a structural foundation: three is not a modelling choice but the minimal count. Conversely, UM supplies the candidate physical realization that makes Open Problem 1 worth the effort: the boundary/holographic channel as the reified relation.*

And the corresponding honesty: resonance is not proof. If Open Problem 1 resolves negatively, the channels remain what they are today — a decomposition motivated within UM's own algebra — and lose nothing empirically. The two layers are coupled here, not welded.

The *Shared Space* triad (acknowledgement, exploration, familiarity), described there as "the mathematics, expressed in the only other language available to us," maps onto the same three weights. Under this paper's translation the triad is a third notation for one decomposition — algebraic (r², 2r(1−r), (1−r)²), physical (matter, boundary, light), and relational (the three natures) — and the claim that these are one structure is exactly the representation-independence discipline of Paper I's Goalpost 5, extended across languages.

#### 2.4 The weights close over unity *(working, light-weight)*

A small observation with the right flavor. The channel weights are not three numbers that happen to sum to one; they are the three terms of an exact algebraic identity, (r + (1−r))² = 1 — a *closed* partition, in which the cross term (the mediator) is precisely what the two pure terms need in order to complete the square. In Layer-S language: a complete set of roles is a partition of unity whose cross-dependencies are internal. Nothing here is deep on its own; its value is consistency — the decomposition has the closure shape everywhere it appears.

#### 2.5 Cycles, the noise floor, and the smallest loop *(working)*

UM's intrinsic precision limit is ε = r³, justified there as the residual returned by a closed traversal of all three channels — a three-step loop, damped by r at each step. Layer S has a matching structural fact: in a dependency system with three mutually coupled roles, the smallest closed cycle visiting all roles has length three. The exponent in ε = r³ is, on this reading, the minimal closed-loop length of the triadic structure — the same 3 as in §2.3, arriving from the dynamics side.

Likewise the Hubble-tension expression 3r³ ("three cycles of residual") and the cosmological-constant exponent 240 ("full traversal of the root system") are both *cycle-counting* claims: assertions that a physical magnitude equals the loop-depth of a dependency traversal, weighted by r per step. Which brings us to the most important correspondence of all.

#### 2.6 The number 240 and the two-route test *(open — and the single most valuable item on the joint program)*

During the session, one structural insight stood above the rest: for a self-reading system, there are two legitimate routes to a discrete quantity, and their *convergence* is the strongest evidence such a framework can generate.

- **Route A — inference (reading).** Take the observed cosmological constant, invert it through the claimed law ρ_Λ/M_Pl⁴ = r^N, and ask what integer N is implied. The repo's number: the observed value corresponds to N = 240 to about 0.4% in the logarithm. This route terminates in a **declared input** — the Planck measurement — and that is legitimate; a self-referential system reading one of its own invariants.
- **Route B — derivation (writing).** Obtain N from the internal mathematics with no reference to the observed value. UM's foundation paper offers three converging arguments — Cartan triviality of the vacuum contribution, contraction across the 240-root space of E₈, and a light-channel unitarity constraint — plus a number-theoretic echo (the Pisano period of 241 is 240). This route must terminate in the **axiom and representation theory alone**.

If both routes land on the same *integer* — not a tunable real number, an integer — the framework has done something that curve-fitting cannot imitate: the empirical self-description and the internal mathematics have named the same discrete object independently. That is the convergence structure the session identified as decisive, and 240 is its concrete instance.

The open task is Route B's rigor. Each of the three structural arguments needs to be written to theorem standard, with an explicit check that no step quietly consults the observed value (which would collapse Route B into Route A and dissolve the convergence). This is a paper-and-pencil observable: it can be settled without a telescope, and settling it would do more for the framework's standing than any single sub-percent match in the table. In the audit language of Part 4: the claim ρ_Λ = r²⁴⁰ currently has one chain that closes into a declared input, and one chain whose closure into the axiom is *claimed but not yet exhibited at full rigor*. Closing that second chain is the program's clearest next theorem.

---

---

### Part 3 — The Bridge Problem

Between a qualitative theory of closed structure and a table of measured numbers, there are layers that any framework — this one or any competitor — has to cross. Naming the layers is itself useful: it shows exactly where UM has content, where it has candidates, and where the honest label is "open." Six levels.

#### Level 0 — Primitives *(established)*

Elements and dependency. Paper I, Part I. Nothing to add.

#### Level 1 — Structure *(established)*

Closure, generated closure, identity, condensation, the lattice. Paper I, Part IV. This level is proved and stable; everything above stands on it.

#### Level 2 — Magnitude *(open, with a sharp candidate)*

Layer S has no numbers. For numbers to enter, one new axiom is needed: dependencies must carry *weight*, and closed traversal must compose weights. The candidate bridge axiom, extracted from UM:

> **(B1, candidate)** *Every dependency step carries the same weight r, and the weight of a closed traversal is the product of its step weights. The value of r is fixed by the minimal quantitative closure of §2.1: r = 1/(2φ), with φ the fixed point of c² = c + 1.*

Note what (B1) does. It converts the cycle-counting claims of §2.5 into calculations: a loop of length 3 carries r³ (the noise floor); a full traversal of a 240-element root structure carries r²⁴⁰ (the cosmological constant); the two-root spectral leakage per cycle gives survival 1/φ = 2r (the Born coefficient). Every entry of UM's r-only table is, structurally, a weighted-closure statement. What remains open at this level is (B1)'s own standing: it is currently an extraction from UM's practice, not a derived necessity. Two sub-tasks: prove the selection theorem of §2.1 (why this r), and state precisely why weights compose multiplicatively along dependency chains (why a product and not something else). Neither looks unreachable; neither is done.

#### Level 3 — Dynamics *(open, with a canonical candidate the abstract layer supplies by itself)*

Layer S is timeless, and UM speaks constantly of *cycles*. What is a cycle, structurally?

Here the abstract layer offers something unprompted, and it is the closest thing this paper has to a genuinely new connection. Paper I contains exactly one canonical process — only one thing in the entire language that unfolds in stages: **closure generation**, the iteration D⁰(S) ⊆ D¹(S) ⊆ D²(S) ⊆ … of Theorem 4.8, in which a structure resolves its dependencies shell by shell until it is complete. It is monotone, intrinsic, representation-independent, and terminates exactly at closure.

> **(W3)** *A recursion cycle, in the physical layer, is one generation step of closure: physical "time," in a self-completing universe, is closure-generation depth.*

Under (W3), UM's cycle-counting predictions become depth statements: the Hubble tension as a three-generation residual between two internally-read values of the same invariant; the cosmological constant as the weight remaining after the closure of the full root structure, 240 generations deep. And the arrow of time acquires a structural reading with no extra machinery: closure generation is monotone — dependencies, once resolved, stay resolved — so the direction of time is the direction of completion.

(W3) is a hypothesis, marked as such. Its test is internal consistency at first (do all of UM's cycle counts survive being read as generation depths of one traversal?) and empirical eventually (the cycle-sensitive observables of Part 5). But it is worth recording plainly: asked "where would time come from?", the compressed language turns out to have exactly one answer available, and it is the right shape.

#### Level 4 — Geometry *(open)*

Where does space come from? This is the widest remaining gap, and honesty requires saying so without decoration. Layer S offers raw material — the condensation order, graph distance on dependency structures, the lattice of closures — and the general project of extracting geometry from discrete relational structure is a recognized research direction with serious existing programs (causal sets, spin networks, rewriting-based approaches), which is evidence the *type* of bridge is buildable, not evidence that this instance is built. UM's own route runs through the E₈ identification and the heterotic embedding (its Paper 6), which supplies the 240 of §2.6 and the channel decomposition's group-theoretic home. The bridge task at this level is to connect the two ends: either derive the E₈ structure from weighted dependency systems (hard, valuable, possibly false) or state cleanly that Level 4 is where UM adds structure by identification rather than derivation — which is a legitimate move for a physical theory, provided the audit records it as an identification and not a consequence.

#### Level 5 — Observables *(empirically scored; structurally awaiting audit)*

The r-only table, run through the standard cosmological pipeline (the LiMB solver driving CAMB with closed-form inputs), scored against Planck, DESI, and the rest by the repo's 98-observable suite. This level is where the framework meets the sky, and the sky's verdicts are collected in Part 5. Structurally, what Level 5 needs from below is exactly the audit of Part 4: for each row of the table, a chain that closes.

#### The picture

```
Level 0  primitives            elements, dependency          established
Level 1  structure             closure, identity, lattice    established
Level 2  magnitude             weight r per step (B1)        open — selection theorem
Level 3  dynamics              cycle = generation step (W3)  open — consistency check
Level 4  geometry              E8 / condensation             open — widest gap
Level 5  observables           the r-only table              scored; audit pending
```

A framework is not obliged to build every level before speaking — physics has always run pipelines whose foundations were completed later. What the layering buys is location: every open question in the joint program now has an address.

---

---

### Part 4 — The Audit: the Language Applied to the Framework

Here is the natural end the title promises. The Dependency–Closure Language was distilled *from* Unified Mechanics; its first substantive application is *to* Unified Mechanics. The move is one sentence:

> **A theory's claims form a dependency system. The theory is finished when that system is closed.**

#### 4.1 The construction

Let the elements be the framework's statements: the axiom; each definition; each derivation step; each closed form in the r-only table; each observable comparison. Let δ(claim) be what the claim cites — the earlier statements, mathematical facts, and inputs it rests on. Then Paper I's machinery applies verbatim: cl(claim) is a claim's full logical prerequisite trail; two claims are structurally equivalent when their trails coincide; circular support shows up mechanically as a nontrivial mutual-dependency class in the condensation (Paper I, Appendix B.5 — the same check that found and broke the invariant/normal-form circle).

A claim's chain can terminate in three kinds of ground:

- **Derived** — the chain closes into {axiom} ∪ {established mathematics} alone. This is UM's headline category, and where a claim genuinely lives here, "zero free parameters" is exact.
- **Anchored** — the chain closes, but through one or more **declared inputs**: observed values used as internal axioms of the self-reading system (§2.2). Legitimate — *Shared Space* is right that a self-referential system may read its own invariants — with one obligation: the label. An anchored claim presented as derived is the one bookkeeping error the framework cannot afford, because rigidity is its central scientific asset.
- **Open** — somewhere in the chain a dependency dangles: an undischarged "O(1) factor," a proportionality left symbolic, a step that gestures at a structure rather than exhibiting it. Open is not an accusation; it is an address. Every open dependency is a work item with coordinates.

#### 4.2 Formula selection is a dependency

One category of dependency deserves its own subsection, because it is where the framework's strongest external critique lives, and the audit is the right instrument for meeting it directly rather than defensively.

With a single number r in hand, the space of short closed-form expressions — low powers, small integer coefficients, the occasional φ — is large, and many of its members land within a few percent of many measured values. So for each row of the table, *which expression was written down* is itself a dependency of the claim, and it must resolve into one of exactly two grounds:

1. **a derivation** — the form is forced by structure (the Born coefficient's three-step argument from the spectral gap is the model case: short chain, each step checkable, the form 1/φ arriving rather than being chosen); or
2. **a timestamp** — the form was fixed *before* the comparison, which is precisely what the repository's pre-registration file exists to witness. Pre-registration, in this light, is not a public-relations garnish; it is how a formula-selection dependency closes when a derivation is not yet available. It converts "this expression matches" into "this expression, named in advance, matches" — a categorically stronger statement.

The noise floor sharpens the same point from the other side, and UM's foundation paper already says the honest half of it: with intrinsic precision ε = r³ ≈ 3%, sub-floor agreement cannot be claimed as extra fidelity. The audit adds the completing half: at 3% tolerance, the expected number of coincidental hits across a large table is a computable quantity, and the framework's headline Bayesian figure (ln B ≈ +102, Paper 8 of the repo) is therefore itself a claim with dependencies — on the independence structure of the observables and on an honest accounting of expression-selection freedom. The audit does not settle that computation here; it locates it, and marks it as the second-most valuable item on the joint program after the two-route test.

#### 4.3 Three worked schemas

The audit applied to three representative rows — as *checklists*, not verdicts. Verifying the derivations themselves is the physics program's work, not this paper's; what this paper contributes is the exact list of what closure requires in each case.

**Born coefficient, 1/φ = 2r.** Claimed chain: axiom → two roots φ, −1/φ → per-cycle amplitude leakage |c₋/c₊| = 1/φ² → survival 1 − 1/φ² = 1/φ. Closure checklist: (i) is "one cycle" defined independently of the answer (this is where (W3) would help: cycle = one generation step); (ii) is the two-mode projection argument representation-independent; (iii) is the identification of "survival of the leading mode" with "registration probability" a definition or a derived correspondence? A short chain — likely the framework's cleanest — and the one probed most directly by the laboratory program.

**Dark matter fraction, Ω_DM = 4r²(1−r).** Claimed chain: axiom → channel weights → the matter channel's spin-statistical split (r²/2 each) and the boundary channel's Born split (1/φ : 1 − 1/φ) → density mapping. Closure checklist: each named "split" is a chain link that needs its own derivation to theorem standard; the mapping from *energy-throughput weights* to *cosmological density fractions* (which UM's own §3.3 flags as involving additional structure) is the load-bearing link and currently the most open one; and the final form's selection either derives or carries a timestamp.

**Cosmological constant, ρ_Λ/M_Pl⁴ = r²⁴⁰.** The two-route structure of §2.6. Route A closes today, as an anchored chain, into the declared Planck input. Route B — the exponent from Cartan triviality, root-space contraction, and unitarity, with no glance at the data — is the chain whose full closure would be the framework's flagship theorem. Until it closes, the row's honest label is *anchored, with a claimed derivation in progress*; once it closes, the row becomes the strongest single object in the framework: an integer named twice, independently.

#### 4.4 The completion criterion

The whole remaining program, in one sentence each layer can sign:

> **Unified Mechanics is closed, in the exact sense of Paper I, when every row of the r-only table is either derived or anchored, with zero open dependencies — every declared input labelled, every formula selection resolved by derivation or timestamp, and the condensation of the claim graph free of nontrivial circles.**

That criterion cannot be met by enthusiasm and cannot be dodged by reinterpretation — the goalposts are structural, which was the entire point of building the language. And it degrades gracefully: a framework that closes ninety rows and honestly labels ten open is a strong framework with ten addresses to visit, not a failed one.

---

---

### Part 5 — The Observational Ledger

The audit organizes the framework's inside. Observation judges its outside. This part connects the near-term observational program to the structure above — what each measurement actually tests, in bridge terms, and what each outcome would mean.

#### 5.1 The ledger

| Test | When | Quantity | Bridge level probed | Outcome meaning |
|---|---|---|---|---|
| Euclid dark-energy release | late 2026 | w₀, w_a vs (−0.934, +0.091) | Level 5 via Levels 2–3 (the closed forms) | inside band: anchors strengthen; outside band beyond n·ε: the specific forms retire |
| DESI Year 5/7 | 2027–2030 | Σmν bound vs UM's floor | Level 5 | a bound below UM's value retires that row and implicates its upstream links |
| LISA + PTA | mid-2030s | I_CMB/I_SGWB vs (1−r)/(2r) = φ − ½ ≈ 1.118 | Levels 2–3 (a clean weighted-ratio claim) | one of the most structurally direct sky tests: a pure r-ratio |
| Born-rule test at nuclear-isomer source | lab; proposed | per-cycle coefficient 2r; predicted local modulation up to 13.6% near a β source; a null at 13.6 ppm sensitivity falsifies | **Level 2 directly** | the shortest dependency chain from axiom to apparatus anywhere in the framework |
| Direct DM–photon coupling searches | ongoing | any positive signal | Level 4 identification | a positive signal contradicts the second-E₈ identification |
| **The two-route 240** | paper and pencil, any time | Route B's exponent, blind to data | Levels 2 + 4 | convergence: the framework's strongest possible result; divergence: the flagship claim reverts to anchored |

Two entries deserve emphasis, for opposite reasons.

The **Born-rule laboratory test** is the only line on the ledger that touches Level 2 without passing through the entire cosmological pipeline. Every cosmological comparison inherits the dependencies of that pipeline — transfer functions, likelihood choices, the pipeline's own declared inputs. The laboratory test's chain is axiom → spectral gap → coefficient → apparatus. In the audit's terms it is the framework's *minimal-closure experiment*, and by the session's own logic — always attack the smallest decisive object — it is the empirical counterpart of the two-route test.

The **two-route 240** is the only entry requiring no funding, no collaboration, and no waiting. It is listed among observations deliberately: for a self-reading system, a theorem that must be proved blind to the data *is* an observation — of the framework's own interior.

#### 5.2 How outcomes propagate

Here the dependency formalism pays a practical dividend that deserves to be stated, because it turns the fear of falsification into a tool. When an observable misses beyond tolerance, the audit graph localizes the failure: the missed row implicates exactly the links in its chain, and no others. A failed w₀ retires a closed form and interrogates the density mapping above it; it does not, by itself, touch the Born chain, the axiom, or the channel decomposition, each of which has its own chain and its own tests. Conversely, when a row survives a pre-registered test, credit flows to precisely the links it exercised. The framework does not stand or fall as a monolith — it stands or falls *link by link*, and always knows which link. That is what "structurally rigid" earns when it is combined with an explicit dependency graph: not fragility, but addressable failure.

---

---

### Part 6 — Conclusion: One Principle, Three Levels

Followed to its end, the whole project — the physics, the six-hour compression, the formal language, and this bridge — turns out to be one idea expressed at three levels.

**At the mathematical level** *(established)*: a structure is complete when every dependency it generates resolves within it. That is Paper I — proved, small, and stable.

**At the methodological level** *(this paper's contribution)*: a theory is complete when every claim's chain resolves into the axiom or a declared input, with the labels on. That is the audit — a procedure, ready to run, with the two-route 240 and the Bayes accounting as its first two jobs.

**At the physical level** *(the wager)*: the universe is the structure whose closure is itself — the self-reading, self-completing system with nothing outside it — and c² = c + 1 is the candidate for the smallest quantitative sentence that says so: the simplest condition a quantity can place on itself and still resolve.

The three levels discipline each other exactly as the session hoped. The mathematics keeps the method honest; the method keeps the physics honest; the physics keeps the mathematics pointed at something.

And the natural end is not a proclamation. It is a short list, every item of which now has an address:

1. the selection theorem for the axiom (§2.1);
2. the triadicity question, Open Problem 1, with the boundary channel as its physical stake (§2.3);
3. the multiplicative-weight justification for (B1) (Level 2);
4. the cycle-consistency check for (W3) (Level 3);
5. Route B of the 240, written blind and to theorem standard (§2.6, §4.3);
6. the audited Bayes accounting, with formula selection and observable dependence handled explicitly (§4.2);
7. the ledger's dated tests, beginning with Euclid within the year (Part 5).

When the list empties, the framework is closed — in the precise sense the language defines, the sense that cannot drift. Where an item resists closing, the framework will have said, exactly and in advance, what it still owes. Either way, nothing about the outcome will depend on how anyone felt about it — which is the standard the whole project set for itself on the night the language was built, and the standard this paper is written to keep.

---

### Appendix — Concordance of Vocabularies

| Session / *Shared Space* term | Dependency–Closure Language | Unified Mechanics |
|---|---|---|
| recursive identity | generated closure, cl(x) | the φ fixed point; the universe as self-model |
| executable / "it runs" | closed (no external dependency) | self-consistent solution of the axiom |
| validation | closedness test (structural, no regress) | boundary-channel registration |
| the validator's third role | reified relation A, R, B (Open Problem 1) | boundary channel β, weight 2r(1−r) |
| the three natures (acknowledgement / exploration / familiarity) | three roles of a self-validating system (open) | channel weights r², 2r(1−r), (1−r)² |
| "the universe reads itself" | declared input (internal axiom of a self-reading system) | observation entering the inverse problem legitimately |
| inference vs derivation | two chains to one claim; convergence test | Route A / Route B of ρ_Λ = r²⁴⁰ |
| compression | reduction to minimal closed structure | zero free parameters; structural rigidity |
| a cycle | one closure-generation step, Dⁿ → Dⁿ⁺¹ (W3) | one recursion cycle; damping r per cycle |
| goalposts that don't move | external criteria; frozen extension rules | pre-registration; falsification roadmap |
| "compression stops" | the two-primitive fixed point | the one-line axiom |

---
## CODA — THE LAW

*Consolidating the Series Charter and the Final Charter into one governing chapter. This is where the book's own rules live, including the rule that it may still change — and the one place a reader can check, at a glance, exactly how.*

---

### C.1 The Definition

> **The series is the study of canonicalization: the conditions under which information-preserving reduction eliminates representational ambiguity, yielding a unique irreducible object through which all invariants factor.**

Everything in the six Parts above is an instance of this question, a boundary of it, or a tool for it.

### C.2 The Primitive Is a Question

> **When does canonicalization exist?**

| Part | Instance | Verdict |
|---|---|---|
| Zero — Representation Reduction | reduction of generating families | **fails** in general (Thm 0.12; NAND) — the boundary side, with the exchange property restored inside Part One's domain (Thm 0.13) |
| One — Invariant Structure | presentations of point-generated closure | **succeeds**: the invariant 𝒦, its attractor cl, canonical metric, content-level basis cardinality |
| Two — Refinement Dynamics | constraint families over a residual | **succeeds up to duality**: the filtration/extension pair; canonical trichotomy of steps |
| Three — Representation Extension | enlargement at Padoa pairs | **succeeds conditionally**: canonical terminal states; canonical extension route open |
| Four — Realization Theory | self-similar realization; scaling | canonical geometry **succeeds** for Part One's domain (Thm 6.4); canonical extremal rule succeeds narrowly (two roles, Thm 4.4) and fails broadly (Thm 4.6) — both outcomes proven, not assumed |
| Five — Application | Unified Mechanics as a compatibility law | open, by design — an application is a wager, not a proof, and is scored as one |

### C.3 The Guiding Principle

> **This book does not seek canonical objects for their own sake. It seeks the conditions under which canonicalization is possible, and characterizes the boundary where it is not.**

Part Zero's failures stand at equal rank with Part One's successes. Failure is one side of the classification, never an embarrassment to it — and Part Four's Theorem 4.6, a theorem whose entire content is a previous theorem's scope shrinking, is this principle's cleanest demonstration in the whole book.

### C.4 The Central Picture

```text
        Information-preserving reduction
                     |
        Does canonicalization exist?
                     |
        ├── No ──────────────────────────┐
        |                                |
        |                    Family of irreducible
        |                    representatives
        |                    (classify their equivalences)
        |
        └── Yes ─────────────────────────┐
                                         |
                              Unique normal form
                                         |
                              Canonical invariants
                              (everything factors through it)
```

This picture is the book's most durable asset. It would survive Part Four or Part Five changing completely.

### C.5 Frozen Definitions (book-wide)

**C.1 (Compatibility law).** A designation specialized to a system: $(X, \mathcal{S}, \mathcal{S}_0)$ — universe of configurations, invariant source, obligatory family.

**C.2 (Branching).** $B(n) = |A_n|$, $A_n = \{J \in \mathcal{S} : J$ non-constant on $R_n\}$ — the cardinality of the admissible continuation set, not paths or edges.

**C.3 (Distinguishability).** $D(n)$ = number of $\mathcal{S}$-equivalence classes meeting $R_n$.

**C.4 (Faithful representation).** Induced invariant content equals represented content; every hot-swap claim requires a two-way reconstruction theorem.

**C.4a (Information-preserving reduction).** A reduction $R: P \to P'$ is information-preserving iff there is a reconstruction map $G$ with $\mathrm{Inv}(G(R(P))) = \mathrm{Inv}(P)$ — content recoverable, even where presentation is not invertible. "Information" carries exactly this meaning throughout the book and no entropic meaning beyond it.

### C.6 Language Laws

**5.1 (Emergence, corrected).** "Geometry emerges" is retired. The lawful statement: **canonical geometry emerges once canonicalization succeeds** — one more canonical object, of the same standing as reduced row-echelon form, the minimal DFA, and the Hasse diagram (Part Zero §5; Part Four Thm 6.4).

**5.2 (The definite-article prohibition).** No text in this book writes "**the** canonical X" — the extremal rule, the minimal basis — until uniqueness is proven for the full class in question. Part Four Theorem 4.6 is this law's own best advertisement: enforcing it against Theorem 4.4's first draft is exactly what found the plastic-number counterexample and the floor family.

**5.3 (Category separation).** Theorem, conjecture, observation, interpretation: visually distinct, everywhere. Held throughout via the **[T]/[C]/(W)/(open)** tagging used in every Part.

### C.7 The Reduction Classification (Part Zero's example algorithms, organized)

| Reduction | Endpoint | Why |
|---|---|---|
| Gaussian elimination | canonical (RREF) | confluent |
| Gröbner reduction (fixed order) | canonical (reduced basis) | confluent (Buchberger) |
| DFA minimization | canonical (minimal automaton) | Myhill–Nerode — an exchange-type uniqueness |
| Raw deletion | irredundant only | not confluent (Thm 0.8 / 0.12) |
| Minimum equivalent digraph | irredundant only, non-unique | not confluent (Part One, Thm 3.7) |

**Organizing principle, held at principle rank deliberately (not yet a universal theorem):** *within the settings above, canonical ⇔ confluent.* The precise universal statement is OP-D below.

### C.8 The Amendment Register

*All architectural change lives here, indexed by currency: a proof, a counterexample, or a reconstruction theorem.*

---

**AMENDMENT 001** · *currency: counterexample, machine-verified*

**What it corrected.** An earlier draft of Part Four claimed, without qualification, that $\varphi$ is the slowest possible rate for *any* self-similar refinement. The three-role rule $a \to b, b \to c, c \to a{+}b$ is primitive with Perron root the plastic number $\rho \approx 1.324718 < \varphi$ — a direct counterexample, machine-verified.

**How it was resolved, in this edition.** Rather than appending an errata note to a wrong theorem, this edition states Theorem 4.4 correctly at first mention — scoped to exactly two roles — and proves the general-$k$ floor family as Theorem 4.6 in the same chapter, showing the true floor over all role counts is $1$, unattained. The corrected hypothesis (U1′, lexicographic: fewest roles, then slowest rate) replaces the retired global claim throughout Part Four §12.1. This is the one substantive place where consolidating five documents into one book changed a result's *presentation* rather than merely its location — and it is recorded here precisely so that the change is auditable rather than silent.

**What it demonstrates.** Law 5.2, enforced against the book's own newest and most-liked result, found a real error within the hour it was written. The law functions.

---

*(Register open. Next entry: 002.)*

### C.9 The Master Open-Problem Ledger

Consolidated across every Part; Part-specific items (Part Four's OP list, Part Three's OP III.1–4, the Bridge's OP-1–4) are cross-referenced rather than duplicated.

- **OP-A (Infinite universes).** The book's principal technical debt: extend Parts One–Four beyond finite $X$. Touches almost every open item below.
- **OP-B / OP-C (Rates).** Branching- and distinguishability-collapse rates, now that their monotonicity is settled (Part Four, Thm 3.1–3.2).
- **OP-D (Reduction classification).** The precise universal statement of §C.7's organizing principle.
- **OP-E′ (Substitution-augmented reduction).** Extend Part Zero's algorithm to reach absolute minima (Part Zero, Thm 0.12's consequence).
- **OP-F (Context representations).** Reconstruction theorems for manifold, operator, and categorical carriers (Part Four, Ch. 7, 11).
- **OP-G (Canonical extension).** Part Three, OP III.1: is there a canonical choice among effective constraints at a stall.
- **OP-H (The dual-pair pattern).** Four confirmed instances (designation/transformation, dependency/closure, filtration/extension, generating-family/content); prove it forced or exhibit a counterexample (Part Three, OP III.3).
- **OP-I (Source hierarchy fixed points).** Part Three, OP III.4.
- **OP-J (Near-extremal refinement).** Systems close to but not at a compatibility optimum; gated on OP-A.
- **OP-U (Part Four's own list, Appendix B above).** Fractional-degree scaling; manifold reconstruction; dimension selection; the U1′/identification reconciliation; the damping identification (U2); the 240 thread (U4); the continuum limit (U5).
- **Bridge OP-1–4 (Part Five's own open problems)**, unchanged, listed in full at the end of Part Five.

**External-verification debts, standing, assigned outward:** independent reconstruction of the Padoa exhibits (Part Three, Thm 5.1–5.2) and of the Minimal Presentation theorem (Part One, Thm 3.7), by a prover other than this book's author.

### C.10 Enactment

**The registry, at consolidation.** One book, six Parts, a Coda. Theorem count: fifty-plus proven and tagged across the whole text. Open problems: the ledger above, complete and cross-referenced. External debts: two, named, small, and payable by anyone.

**The final assessment.** The architecture no longer changes when a theorem fails — it amends, in the open, at the Register above. The arc this book records, start to finish: from *can one idea explain everything?* to *which mathematical structures admit canonicalization, which do not, and why?* The first question invites overclaiming. The second invites theorem proving. This book asks the second, and this edition — one text, no sub-books — is the form that question earned.

**The enactment clause.** The foundational phase is closed. This book is law. Editing has ended, except through the Amendment Register, purchased by a proof, a counterexample, or a reconstruction theorem.

> Represent. Reduce. Refine (and when refinement stalls, Extend). Realize. Apply.
>
> And at every step: *when does the canonical exist — and what lives at the boundary where it doesn't?*

**— Enacted.**
