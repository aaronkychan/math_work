# Plan A (Balanced, classical Koszul theory)

👉 Goal: reach _definition + main properties + examples + Koszul duality (elementary form)_

### Lecture 1 — Motivation & graded algebras

- Why Koszul? (polynomial rings, exterior algebras, “linear resolutions”)
- Graded algebras, graded modules
- Examples: $k[x_1,…,x_n]$, exterior algebra

### Lecture 2 — Tensor algebra & quadratic algebras

- Tensor algebra $T(V)$
- Quadratic algebras $A=T(V)/(R)$
- Examples: symmetric vs exterior

### Lecture 3 — Free resolutions (hands-on)

- Projective/free resolutions
- Minimal resolutions (graded case)
- Compute resolution of $k$ over $k[x]$

### Lecture 4 — Tor and Ext (computational viewpoint)

- Define Tor, Ext via resolutions
- Compute small examples
- Yoneda intuition for Ext

### Lecture 5 — Definition of Koszul algebra

- Linear resolutions
- Definition: $A$ Koszul ⇔ $k$ has linear resolution
- First examples: polynomial ring, exterior algebra

### Lecture 6 — Koszul complex

- Construct Koszul complex for $k[x_1,…,x_n]$
- Exactness (sketch, not full proof)
- Interpretation

### Lecture 7 — Quadratic dual

- Define $A^!$
- Examples:
    - polynomial ↔ exterior
- Basic properties

### Lecture 8 — Koszul duality (elementary form)

- Statement: $\mathrm{Ext}_A(k,k) \cong A^!$
- Compute in examples
- Avoid derived categories; stay computational

### Lecture 9 — Hilbert series

- Hilbert series of graded algebras
- Relation:
    $$H_A(t) H_{A^!}(-t) = 1$$
- Check in examples

### Lecture 10 — More examples & non-examples

- Path algebras with relations (gentle intro)
- Monomial quadratic algebras
- When Koszul fails

### Lecture 11 — Applications / connections

Choose depending on taste:

- Gröbner bases (very light)
- PBW algebras
- Combinatorial examples

### Lecture 12 — Wrap-up & outlook

- Summary of equivalences
- What derived category viewpoint says (informally)
- Further directions (BGG, etc.)

# Plan B (More computational, less abstract)

👉 Better if students are weak in homological algebra

Shift emphasis to **examples + explicit computations**, delay Ext/Tor formalism.

### Key changes:

- Introduce resolutions via **examples first**
- Treat Tor/Ext as _derived from computation_, not abstract functors
- More time on:
    - Koszul complex
    - explicit duals
    - Hilbert series

This plan sacrifices some conceptual clarity but increases accessibility.

# Plan C (Representation-theoretic flavor, gentle path algebras)

👉 If you want a bridge to representation theory

### Add:

- Brief intro to quivers and path algebras (Lecture 2–3)
- Examples of quadratic algebras via quivers
- Koszul property in that context

### Remove/shorten:

- Some abstract Ext/Tor theory
- Replace with:
    - projectives over path algebras
    - combinatorial resolutions

---
