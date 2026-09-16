# A Deformation-Theoretic Study of the Principal 2-Block of \(\mathrm{Sz}(8)\)

## 1. Central question

Let

\[
G=\mathrm{Sz}(8),\qquad p=2,\qquad P\in \operatorname{Syl}_2(G),\qquad N=N_G(P).
\]

Let

\[
A=B_0(kG),\qquad B=B_0(kN),
\]

or, more precisely, their basic algebras over an algebraically closed field \(k\) of characteristic \(2\).

The known situation is that \(A\) and \(B\) are stably equivalent of Morita type but not derived equivalent. For this example \(N\cong 2^{3+3}:7\), and the relevant quiver-and-relations data are accessible computationally. [Koshita’s quiver-and-relations paper](https://www.researchgate.net/publication/220160889_An_example_of_relations_on_the_Ext-quiver_for_the_Suzuki_group_Sz8_in_characteristic_2)

The first objective is:

> Determine whether a meaningful deformation \(A_\lambda\) of the basic algebra \(A\), preferably preserving its quiver, has a parameter value for which \(A_\lambda\) is derived equivalent to \(B\).

The second objective is:

> Identify which features of the \(\mathrm{Sz}(8)\) obstruction generalize to other blocks with nonabelian TI defect groups.

A crucial preliminary distinction concerns coefficients. Over a characteristic-zero \(2\)-modular ring \(\mathcal O\), the centers of the corresponding blocks are already non-isomorphic. Over \(k\) of characteristic \(2\), the ordinary centers are isomorphic, so subtler derived invariants are required. [Marcus’s survey](https://www.researchgate.net/publication/228384698_Derived_equivalences_and_the_abelian_defect_group_conjecture), [the detailed center calculation](https://pure.manchester.ac.uk/ws/portalfiles/portal/54585068/FULL_TEXT.PDF)

---

## 2. Main research questions

### Q1. What are the genuine relation parameters?

Given a presentation

\[
A\cong kQ/I,
\]

which scalar coefficients in \(I\) are genuine moduli, and which disappear after rescaling arrows, changing bases, or applying automorphisms of \(Q\)?

This should be settled before any derived-equivalence search.

### Q2. Which deformations remain finite-dimensional and symmetric?

For a parameterized ideal \(I_\lambda\), determine for which \(\lambda\)

\[
A_\lambda=kQ/I_\lambda
\]

is:

- finite-dimensional;
- basic;
- symmetric or self-injective;
- of the same dimension and Cartan type as \(A\);
- equipped with the same number of simple modules.

### Q3. Do derived invariants eliminate all fixed-quiver deformations?

For each surviving \(A_\lambda\), compare with \(B\):

\[
Z(A_\lambda),\quad HH^\ast(A_\lambda),\quad HH_\ast(A_\lambda),
\]

Külshammer ideals, stable centers, Loewy structures, periodicity, and the integral Euler form.

Derived equivalence preserves the center and Hochschild cohomology, and for symmetric algebras it also preserves Külshammer-type structures. [Summary of derived invariants](https://www.researchgate.net/publication/228384698_Derived_equivalences_and_the_abelian_defect_group_conjecture)

### Q4. If invariants agree, is there a tilting complex?

Search for a two-sided tilting complex \(T\) such that

\[
\operatorname{End}_{D^b(A_\lambda)}(T)\cong B.
\]

The most natural candidates should come from Okuyama–Rickard or mutation-type constructions, rather than from arbitrary complexes.

### Q5. Is the obstruction attached to the algebra or to the stable equivalence?

The canonical stable equivalence in this example is known as a model of a non-liftable stable equivalence. A successful deformation might therefore need to deform the stable bimodule as well as the algebra.

---

## 3. Phase I: Fix the mathematical input

Before computation, fix the following choices.

### 3.1 Coefficient field

Begin with

\[
k=\mathbb F_2
\]

and then test over

\[
\mathbb F_4,\ \mathbb F_8,\ \mathbb F_{16}.
\]

The final formulation should be over an algebraically closed field of characteristic \(2\), but finite-field calculations are useful for discovering parameter values and detecting Galois phenomena.

If integral lifting is included, separately use a \(2\)-modular system

\[
(K,\mathcal O,k),
\]

where \(\mathcal O\) is a complete discrete valuation ring.

### 3.2 Exact presentations

Collect:

1. the quiver \(Q_A\) and relations for the principal block of \(kG\);
2. the quiver \(Q_B\) and relations for the principal block of \(kN\);
3. the identification of vertices with simple modules;
4. the symmetrizing form, if available;
5. the stable-equence bimodule or the images of simple modules.

The principal-block part of the published quiver data must be isolated carefully if the source presentation describes the whole group algebra.

### 3.3 Reproducibility files

Create a small repository containing:

```text
sz8-deformation/
├── data/
│   ├── principal_quiver.g
│   ├── local_quiver.g
│   ├── relations_A.g
│   └── relations_B.g
├── scripts/
│   ├── verify_dimensions.g
│   ├── radical_layers.g
│   ├── centers.g
│   ├── parameter_scan.g
│   └── tilting_search.g
├── results/
├── README.md
└── CITATIONS.md
```

Every computation should record the field, parameter value, presentation, package versions, and output.

---

## 4. Phase II: Reconstruct and verify \(A\) and \(B\)

For both algebras:

1. construct \(kQ/I\);
2. compute a Gröbner basis for the relations;
3. verify finite-dimensionality;
4. compute a canonical path basis;
5. calculate \(\dim_k A\) and \(\dim_k B\);
6. compute the radical filtration;
7. calculate the Loewy layers of all projective indecomposable modules;
8. compute the Cartan matrices;
9. verify symmetry/self-injectivity;
10. compute the centers and their radical filtrations.

This phase is essential: an incorrect relation convention, path multiplication convention, or vertex orientation can invalidate all later results.

For the \(\mathrm{Sz}(8)\) case, reproduce the known center calculation as a baseline. In characteristic \(2\), the centers of the block and its local correspondent have the same Loewy length and are isomorphic, whereas the integral centers behave differently. [Detailed discussion](https://pure.manchester.ac.uk/ws/portalfiles/portal/54585068/FULL_TEXT.PDF)

---

## 5. Phase III: Construct the deformation space

Start with relation deformations of the form

\[
I_\lambda=\langle r_1(\lambda),\ldots,r_m(\lambda)\rangle,
\]

where the \(r_i(\lambda)\) are linear combinations of paths of length at least \(2\).

### 5.1 Gauge reduction

Apply:

- independent rescaling of arrows;
- changes of bases between parallel arrows;
- automorphisms of the quiver;
- changes of representatives for relations.

Determine the quotient of the apparent parameter space by these transformations.

A coefficient that can be removed by arrow rescaling is not a genuine deformation parameter.

### 5.2 Flatness

For a formal family

\[
A_t=k[[t]]Q/I_t,
\]

check that \(A_t\) is flat over \(k[[t]]\). Computationally, this means verifying that the dimensions of the fibers remain constant and that the chosen path basis does not acquire unexpected torsion.

The special values \(\lambda=0\), \(\lambda=1\), and \(\lambda\in k^\times\setminus\{1\}\) should be treated separately.

### 5.3 Hochschild-theoretic interpretation

Compute

\[
HH^2(A)\cong \operatorname{Ext}^2_{A^e}(A,A).
\]

Then determine which relation changes represent:

- trivial deformations;
- nontrivial first-order deformations;
- obstructed deformations;
- deformations preserving symmetry or self-injectivity.

This prevents the project from confusing a change of presentation with a genuine deformation of the algebra.

---

## 6. Phase IV: Filter deformations by invariants

For each genuine parameter value, calculate:

### Algebra structure

- dimension;
- center;
- center Loewy length;
- radical powers;
- socle;
- Nakayama automorphism;
- symmetric bilinear form.

### Module-theoretic data

- simple modules;
- projective indecomposable modules;
- Cartan form;
- Ext\(^1\)-quiver;
- higher Ext groups;
- periodicity of simples;
- stable Auslander–Reiten information.

### Derived invariants

- \(HH^0\), \(HH^1\), \(HH^2\);
- Hochschild homology;
- Külshammer ideals \(T_n(A)^\perp\);
- generalized Reynolds ideals;
- the integral Euler form on \(K_0\);
- stable center and stable Hochschild invariants.

A deformation that fails one of these comparisons can be discarded without attempting to construct a tilting complex.

A negative result would still be valuable if it proves, for example:

> No flat deformation preserving the quiver and symmetry can be derived equivalent to the local correspondent.

---

## 7. Phase V: Search for derived equivalences

If a parameter value survives all invariant tests, search for a Rickard equivalence.

### 7.1 Tilting complexes

Construct complexes of projective \(A_\lambda\)-modules

\[
T^\bullet=\bigoplus_i T_i^\bullet
\]

and test:

\[
\operatorname{Hom}_{D^b(A_\lambda)}(T^\bullet,T^\bullet[n])=0
\quad(n\neq 0),
\]

together with generation of \(D^b(A_\lambda)\).

Then calculate

\[
\operatorname{End}_{D^b(A_\lambda)}(T^\bullet).
\]

### 7.2 Mutation strategy

Begin with the simple modules and apply:

- Okuyama–Rickard mutations;
- two-term tilting mutations;
- approximations by projective summands;
- mutations suggested by the stable equivalence.

The resulting endomorphism algebras may have different quivers. Therefore fixed-quiver deformation should not be the only search space.

### 7.3 Stable-equivalence compatibility

Compare the induced stable functor with the known Morita-type stable equivalence. If the canonical stable equivalence sends simple modules to a simple-minded system that cannot be lifted, then a successful derived equivalence must use a different identification of the stable categories.

The \(\mathrm{Sz}(8)\) example has already appeared in the literature as a non-liftable stable equivalence, making this compatibility question particularly important. [Chan–Koenig–Liu](https://math0.bnu.edu.cn/~liuym/paper/Chan-Koenig-Liu.pdf)

---

## 8. Phase VI: Enlarge beyond fixed-quiver deformations

If no fixed-quiver deformation succeeds, study the following broader classes.

### 8.1 Quiver-changing derived partners

Take endomorphism algebras of tilting complexes over \(A\). Their quivers need not equal \(Q_A\), but they may still be derived equivalent to \(A\).

### 8.2 Deformations of source algebras

Instead of deforming the basic algebra directly, deform a source algebra or a symmetric algebra with the same defect-group data.

### 8.3 Deformation of the stable bimodule

Let \(M\) be the stable-equivalence bimodule. Study whether \(M\) admits a compatible deformation to an \(A_t\)-\(B\)-bimodule.

The relevant obstruction should be expressed through Hochschild or bimodule Ext groups, schematically

\[
\operatorname{Ext}^2_{A\otimes B^{\mathrm{op}}}(M,M).
\]

This may reveal whether the failure is caused by the algebras themselves or by the particular stable equivalence.

---

## 9. Phase VII: Generalization

The general theory should begin with blocks having nonabelian trivial-intersection defect groups.

Candidate examples include:

- Suzuki groups \({}^2B_2(q)\) in characteristic \(2\);
- small Ree groups \({}^2G_2(q)\) in characteristic \(3\);
- sporadic examples such as \(M_{11}\), \(McL\), and \(J_4\) at their relevant primes.

The comparison should ask:

1. Does a stable equivalence of Morita type exist for structural TI reasons?
2. Are the ordinary centers equal over \(k\)?
3. Is there an integral center obstruction?
4. Do Külshammer ideals distinguish the blocks?
5. Are fixed-quiver deformation spaces nontrivial?
6. Does the obstruction persist throughout the family?
7. Can one characterize the obstruction using fusion systems, source algebras, or higher Hochschild structure?

The ultimate goal would be a statement of the form:

> For a class of nonabelian TI blocks, stable equivalence is controlled by local structure, whereas derived equivalence additionally detects a higher or integral deformation invariant.

---

## 10. Computational equipment

### Required

Install:

- GAP 4.x;
- QPA, the Quivers and Path Algebras package.

QPA supports finite-dimensional quotients of path algebras, Gröbner-basis calculations, modules, and projective resolutions. [Official QPA documentation](https://gap-packages.github.io/qpa/doc/chap0.html)

On macOS, the simplest route is usually:

```bash
brew install gap
```

Then test:

```bash
gap -q
```

Inside GAP:

```gap
LoadPackage("qpa");
GAPInfo.Version;
```

### Recommended additions

For reconstructing the group-theoretic side:

```gap
LoadPackage("atlasrep");
```

GAP already contains MeatAxe functionality for modular representations. MeatAxe64 is optional for larger matrix calculations.

For a basic package test, create `toolcheck.g`:

```gap
Print("GAP version: ", GAPInfo.Version, "\n");

for p in ["qpa", "atlasrep", "meataxe64"] do
    Print(p, ": ", LoadPackage(p), "\n");
od;
```

### Optional

Install Magma or SageMath if:

- integral \(2\)-adic computations are required;
- symbolic parameter elimination becomes difficult in GAP;
- an independent verification of the QPA calculations is desired.

### Files to provide

The most important inputs are:

1. the exact principal-block quiver;
2. the complete relations;
3. the field convention;
4. the correspondence between vertices and simples;
5. any available presentation of the local correspondent;
6. the intended stable-equivalence bimodule or simple-module correspondence.

The first computational milestone should be a script that reconstructs \(A\) and \(B\), verifies their dimensions and projective structures, and reproduces the known center calculations before any deformation is attempted.

---

## 11. Expected outcomes

There are three equally valuable possible outcomes.

### Positive

A nontrivial deformation \(A_\lambda\) is found that is derived equivalent to \(B\).

### Structural negative

All fixed-quiver symmetric deformations fail a derived invariant, proving that the proposed deformation direction is too narrow.

### Conceptual negative

The stable equivalence bimodule itself has a deformation obstruction, showing that the failure of derived equivalence is not repairable by changing relations alone.

Any of these would provide a useful foundation for generalization.