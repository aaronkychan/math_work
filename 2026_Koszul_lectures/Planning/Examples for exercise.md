# 1. A non-Koszul commutative quadratic algebra

$A = k[x,y]/(x^2,\; xy,\; y^2)$

### Why this is good

- Looks very simple but **fails Koszulity**
- Forces students to _test_ linearity, not assume it

### Students can compute:

- Basis: $\{1,x,y\}$
- Hilbert series: $1 + 2t$
- Quadratic dual    $A^! = k\langle \xi,\eta\rangle$:
     - relations space is all degree 2 ⇒ dual has **no relations**
- Compare Hilbert series → fails Koszul identity

### Teaches:

- “quadratic” ≠ “Koszul”
- dual can be _much bigger_
- Hilbert series test is meaningful

---

# 2. Quantum plane

$A = k\langle x,y\rangle / (xy - q\,yx), \quad q \neq 0$

### Why:

- First **noncommutative Koszul algebra**
- Still very structured

### Students can compute:

- PBW basis: $x^a y^b$
- Hilbert series: same as commutative case
- Quadratic dual: $A^! = k\langle \xi,\eta\rangle / (\xi\eta + q\,\eta\xi)$
- Check Koszulity (either via known result or guided argument)

### Teaches:

- Koszulity beyond commutative world
- deformation idea (same Hilbert series, different relations)
- duality respects deformation

---

# 3. Path algebra of a quiver with quadratic relations

Take quiver: $1 \xrightarrow{a} 2 \xrightarrow{b} 3$

with relation: $ba = 0$

### Why:

- Introduces **quiver perspective** (very useful later)
- Still very concrete

### Students can compute:

- Basis of paths modulo relations
- Projective modules (explicit!)
- Resolution of simples (in small cases)
- Quadratic dual:
    - reverse arrows
    - orthogonal relations

### Teaches:

- Koszul theory in representation-theoretic language
- how relations affect Ext
- concrete resolutions beyond polynomial case

---

# 4. Monomial quadratic algebra with mixed behavior

$A = k\langle x,y\rangle / (x^2,\; xy)$

### Why:

- Simple relations but **asymmetric**
- Computations are doable but not obvious

### Students can compute:

- Basis: words avoiding $x^2, xy$
- Hilbert series (nontrivial counting!)
- Quadratic dual: $A^! = k\langle \xi,\eta\rangle / (\xi\eta,\; \xi^2)$
- Try to detect Koszulity (it actually _is_ Koszul)

### Teaches:

- combinatorics of monomial algebras
- asymmetry in relations
- practice with dual construction