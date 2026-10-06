# Review of *Introduction to Koszul Duality* (`2026_Koszul.tex`)

**Reviewer persona:** a beginning graduate student who knows basic ring and module theory (rings, ideals, modules, homomorphisms, quotients, direct sums, a little about semisimple modules) and linear algebra. I have little category theory, no homological algebra, and have never met quivers.

**How I read it:** I read the whole `.tex` source (1484 lines, which compiles to 18 pages) and worked through every example and most proofs by hand. Line numbers below refer to the `.tex` file; `\label` names are given where they exist so the author can find things quickly.

---

## 0. Overall impression

The notes are careful. They track left and right actions and the order of tensor factors much more honestly than most sources, they distinguish what is canonical from what depends on a choice of symmetrising form $\tau$, and they flag characteristic 2. Every example I checked by hand is correct (see §6).

The problems are mainly pedagogical. I list them in order of how much they slowed me down.

| # | Issue | Where | Priority |
|---|---|---|---|
| A1 | No motivation or roadmap: I never learn what Koszul duality *is* or why quadratic duals matter | start of document | High |
| A4 | Lecture 1 introduces about five kinds of duals and comparison maps, most of which are never used in Lectures 2–3 | lines 463–684, 746–777 | High |
| C1 | The key computational fact (tensor products over $\Bbbk^r$ decompose along matching idempotents, so composable words give a basis) is used constantly but never proved | 841–858, 1264–1297 | High |
| B2 | Basic properties of $\otimes_S$ (bimodule structure, associativity) are assumed silently | 720–737, 837 | High |
| C7 | The proof of the main theorem (biduality) is the most compressed proof in the notes | 1218–1224 | High |
| C10 | The "anticommuting square" example suggests the signs give a different algebra, but they don't in that example | 1435–1453 | Medium |
| B1 | Category-theoretic vocabulary is used without definition | 323, 506, 612 | Medium |

---

## A. Big picture and structure

### A1. No introduction, motivation or roadmap (High)
**Problem.** The document opens with "Convention" and then definitions. As a beginner I did not know what Koszul duality is, what problem it solves, or why I should care about $A^!$. By the end of Lecture 3 I can compute quadratic duals, but I still don't know what they are *for*.

**Suggestion.** Add a one-page introduction that does three things:
1. Gives a motivating example in plain terms, e.g. $\Bbbk[x]$ and $\Bbbk[x]/(x^2)$, or $\operatorname{Sym}(V)$ and $\bigwedge D(V)$. Point out that each "controls the homological algebra" of the other.
2. States the goal without proof. For example: for a Koszul algebra $A$, the Ext-algebra $\operatorname{Ext}^*_A(A_0,A_0)$ is isomorphic to the quadratic dual $A^!$ (up to the side and op conventions the course fixes). Also mention the derived equivalence of [BGS96].
3. Gives a roadmap: Lecture 1 covers grading and duals, Lecture 2 tensor and quadratic algebras, Lecture 3 the quadratic dual, and Lecture 4 onwards the Koszul complex and Koszul algebras (if planned).

### A2. Title vs. content (Medium)
**Problem.** The title is *Introduction to Koszul Duality*, but the notes stop at quadratic duality. The words "Koszul algebra", "Koszul complex" and "Ext" never appear.

**Suggestion.** If later lectures are coming, say so explicitly ("Lectures 4–… will define Koszul algebras"). If not, add at least a short closing section that states the definition of a Koszul algebra and the main theorem, with references.

### A3. Inconsistent lecture structure (Low)
**Problem.** Section 1 is titled "Rings and modules", but Sections 2 and 3 are "Lecture 2: …" and "Lecture 3: …". Section 1 also covers much more than rings and modules (graded duals, $S$-duals, symmetrising forms). The table of contents is commented out (line 185).

**Suggestion.** Rename it to something like "Lecture 1: Graded algebras, graded modules and duals" and restore `\tableofcontents`.

### A4. Too much unused machinery in Lecture 1 (High)
**Problem.** Lecture 1 defines the following, each with its own notation and comparison maps:
- $D(V)$ and $\mathbb D(V)$
- $M^*$ and ${}^*N$
- $M^{*_{\rm en}}$
- $M^{(*)}$, ${}^{(*)}M$ and $M^{(*_{\rm en})}$
- $\alpha_M$, $\beta_M$, $\gamma_M$
- $S^{\rm en}$, $\tau_{\rm en}$, and $\theta_D$, $\theta_r$, $\theta_\ell$, $\theta_{\rm en}$

Searching the source, the following are **never used** in Lectures 2–3, apart from two passing remarks at lines 1093 and 1166:
- $\mathbb D$ and Lemma `lem:linear-bidual`
- the graded $S$-duals (`def:graded-S-duals`, `cor:graded-dual-comparison`) and the transported $A$-action (676–684)
- the two-sided dual $M^{*_{\rm en}}$, $S^{\rm en}$, $\gamma_M$ and $\tau_{\rm en}$
- $\theta_D$ and $\theta_{\rm en}$
- $\operatorname{GrMod}$ and $\operatorname{grmod}$ (line 323)
- the term "positive degree ideal" and the augmentation map (432–440)

For a beginner this is about four pages of definitions with no payoff yet. I had to hold five different duals in my head while reading Lecture 3, which only needs $V^*$, ${}^*V$, $\tau$, $\alpha$ and $\beta$.

**Suggestion.** Keep in Lecture 1 only what Lectures 2–3 need: $D$, $M^*$, ${}^*N$, symmetrising forms, $\alpha$, $\beta$, and Lemma `lem:S-bidual`. Move the graded duals, the two-sided dual and $\theta_D$/$\theta_{\rm en}$ to the lecture where they are actually used (presumably the Koszul complex). Alternatively, keep them but add one sentence each saying *where* and *why* they will be needed.

### A5. Why $S$-duals rather than the $\Bbbk$-dual? (Medium)
**Problem.** Lines 519–520 say the different duals "can be identified after a choice of form". My immediate question was: then why not always use $D(V)$, which I already understand? The notes never answer this directly.

**Suggestion.** Add a short motivating remark before Definition `def:S-duals`. The $S$-dual $V^*$ is defined without any choices, so $A^!$ is canonical. It also satisfies $W^*\otimes_S V^* \cong (V\otimes_S W)^*$ ($\theta_r$) and the biduality $V\cong{}^*(V^*)$ without choices. The $\Bbbk$-dual only achieves this after picking $\tau$.

### A6. Forward references and ordering (Medium)
**Problem.** Several things are used before they are available:
- Line 323 defines $\operatorname{GrMod}A$ using "degree 0 homomorphisms", but homogeneous homomorphisms are only defined at lines 356–360.
- Line 717 ("The degree zero algebra acts on both sides of the degree 1 piece") refers to an algebra $A$ that has not yet been introduced in Lecture 2.
- Example `ex:cubic-quotient` (948–953) concludes "Hence $A$ is not quadratic". The justification that a quadratic presentation is forced to be $V=A_1$, $R=I_2$ only comes later (1043–1048 and 1167). As written, I could not rule out some other clever quadratic presentation.
- Lines 1086–1093 (Lecture 2) refer forward to Definition `def:quadratic-duals` (Lecture 3).

**Suggestion.** Move the definition of homogeneous maps before line 323. Start Lecture 2 with "Let $A$ be a graded algebra and $S=A_0$." In `ex:cubic-quotient`, either forward-reference the $qA$ criterion or move the example after it. Move lines 1086–1093 into Lecture 3.

### A7. References are never cited (Medium)
**Problem.** [BGS96] and [GI20] appear in the bibliography but are never `\cite`d. Several facts are used "without proof" with no pointer to where a proof can be found (lines 228, 587, 966).

**Suggestion.** Cite [BGS96] at the definitions of quadratic and Koszul duals, and say what [GI20] is used for. For a student audience, add standard textbook references:
- Polishchuk–Positselski, *Quadratic Algebras* (AMS University Lecture Series 37, 2005), for quadratic duality and Hilbert series.
- Assem–Simson–Skowroński, *Elements of the Representation Theory of Associative Algebras*, Vol. 1, for the radical, path algebras and Artin–Wedderburn.
- Loday–Vallette, *Algebraic Operads*, Ch. 3, for Koszul duality of associative algebras.
- Any standard algebra text for tensor products of modules.

---

## B. Prerequisites a beginning student may not have

### B1. Category-theoretic vocabulary (Medium)
**Problem.** The notes use "category", "full subcategory" (323), "duality … reverses arrows" (506), "natural" (600, 664, 743) and "commute with precomposition" (612) without definition. With "basic ring and module theory" I know none of these formally.

**Suggestion.** Either add a half-page glossary (category, functor, contravariant functor, natural transformation, equivalence and duality), or rephrase concretely. For example, Lemma `lem:linear-bidual` could say: "$\mathbb D$ sends degree-0 homomorphisms to degree-0 homomorphisms in the opposite direction, preserves composition, sends short exact sequences to short exact sequences, and $M\cong\mathbb D\mathbb D M$ via evaluation."

### B2. Tensor products: construction and basic properties (High)
**Problem.**
- Definition `def:vector-tensor` (445) is a universal property, not a construction. It does not say why such a space exists or why it is unique.
- After the definition of $M\otimes_S N$ (720–728), the "Equivalently, …" is really a theorem.
- The notes never state that if $M,N$ are $S$-bimodules then $M\otimes_S N$ is again an $S$-bimodule. Nor do they state associativity $(U\otimes_S V)\otimes_S W\cong U\otimes_S(V\otimes_S W)$ or $S\otimes_S V\cong V$. Without these, $V^{\otimes_S i}$ (733–737) is not even well defined as a bimodule, and the "multiplication given by concatenation" in $T_S(V)$ (837) is not obviously well defined.

**Suggestion.** Add a lemma "Basic properties of $\otimes_S$" listing existence, the bimodule structure, associativity, unit, and additivity in each variable. Mark the proofs as standard with a reference, or set them as exercises.

### B3. Facts about semisimple algebras used implicitly (Medium)
**Problem.** Three proofs use the fact that *every finite-dimensional $S$-module is a direct summand of some $S^{\oplus n}$*: Lemma `lem:S-bidual` (707), Proposition `prop:dual-low-degrees` (1183) and Lemma `lem:double-orthogonal` (1205). Theorem `thm:artin-wedderburn` only says "every submodule has a complement", and the step from there to "direct summand of a free module" is not spelled out. The parenthetical claim "(this does not depend on which side you work on)" (224) is also non-trivial.

**Suggestion.** Add a corollary right after Artin–Wedderburn: *every module over a semisimple algebra is projective; in particular every finite-dimensional module is a direct summand of $S^{\oplus n}$.* Cite it at each use.

### B4. The radical of $\Bbbk A_2$ is asserted, not computed (Low)
**Problem.** Example `ex:semisimple-algebras` (249–251) asserts $\operatorname{rad}(\Bbbk A_2)=\Bbbk e_{12}$. From the definition (intersection of maximal right ideals) I could not immediately check this. Also, despite its label, the example contains no semisimple algebra.

**Suggestion.** Show the computation. The maximal right ideals of $\Bbbk A_2$ are $\operatorname{span}(e_{11},e_{12})=e_{11}A$ and $\operatorname{span}(e_{12},e_{22})$, and their intersection is $\Bbbk e_{12}$. Also add a positive example, e.g. $\Bbbk^{\oplus n}$ and $\operatorname{Mat}_n(\Bbbk)$, and relabel.

### B5. "Every finite-dimensional semisimple algebra is symmetric" (Low)
**Problem.** This is quoted as "standard" (587) with no reference. Over a non-algebraically-closed field it needs reduced traces of division algebras, which a beginner has never seen. A commented-out passage about *split* semisimple algebras (245–247) suggests the author considered restricting.

**Suggestion.** Either give a reference, or restrict the course to *split* semisimple $S$ (products of $\operatorname{Mat}_n(\Bbbk)$). In that case the trace form of Example `ex:symmetrising-form` suffices and no unproved theorem is needed. This also makes the hypothesis "$S\otimes_\Bbbk T$ semisimple" in Proposition `prop:dual-tensor-products` automatic.

### B6. Bases of exterior and polynomial algebras (Low)
**Problem.** Line 966 and the Hilbert series at 1008–1013 state the monomial bases of $\operatorname{Sym}(V)$ and $\bigwedge V$ as known. Spanning is easy. *Linear independence* of the $x_{i_1}\cdots x_{i_d}$ in $\bigwedge V$ is not obvious from the presentation $T(V)/(v^2)$.

**Suggestion.** Mark this as a fact with a reference, or outline a proof as an exercise (e.g. via the diamond lemma, or by constructing the alternating multilinear forms).

### B7. Path algebra conventions (Low)
**Problem.** Line 218 says no knowledge of quivers is needed, which is good. But students who do look up path algebras will find opposite composition conventions in different books, so "$\Bbbk A_n$" may look like the opposite algebra to them.

**Suggestion.** One sentence: "With right modules, we compose arrows left to right, so $e_{ij}$ corresponds to the path $i\to j$."

---

## C. Mathematical gaps and subtle points

### C1. Missing lemma: tensor products over $\Bbbk^{\oplus r}$ (High)
**Problem.** Equation `eq:composable-tensors` (842–847) proves only that non-composable tensors *vanish*. Many later arguments use the converse, that composable words of basis elements form a *basis* of $V^{\otimes_S d}$:
- Example `ex:tensor-A3`, where $V\otimes_S V=\Bbbk(a\otimes b)$ needs $a\otimes b\neq 0$
- Example `ex:tensor-An`
- Example `ex:two-vertex-relations`
- the definition of "composable" (1266)
- Proposition `prop:monomial-dual`
- Example `ex:commuting-square-dual`

I could not see why $a\otimes_S b\neq 0$ from what is written.

**Suggestion.** Add a lemma: for $S=\bigoplus_{i=1}^r\Bbbk e_i$,
$$V\otimes_S W\;\cong\;\bigoplus_{i,j,\ell}\,e_iVe_j\otimes_\Bbbk e_jWe_\ell .$$
The proof constructs the inverse map using the universal property, since $S$-balanced bilinear maps are exactly those killing $e_iVe_j\otimes e_{j'}We_\ell$ for $j\neq j'$. Then state the corollary about composable words being a basis, and cite it everywhere it is used.

### C2. $\bigoplus_d\operatorname{Hom}^{\mathbb Z}_A(M,N(d))$ vs. $\operatorname{Hom}_A(M,N)$ (Medium)
**Problem.** Lines 371–375 claim the inclusion and equality for finitely generated $M$, with neither proof nor counterexample. They also don't say why the sum is direct.

**Suggestion.** Give a short proof. For $m\in M_j$ set $f_d(m)=f(m)_{j+d}$ and check $A$-linearity using that $A$ is graded. Only finitely many $f_d$ are nonzero on a finite homogeneous generating set. Then give a counterexample: $A=\Bbbk$, $M=\bigoplus_{i\ge0}\Bbbk(-i)$, $N=\Bbbk$, and $f$ the map sending every basis vector to $1$.

### C3. Existence step in Proposition `prop:dual-comparison` (Medium)
**Problem.** The proof (617) says non-degeneracy of $\tau$ "determines $f(m)$ uniquely". Non-degeneracy gives *uniqueness*. *Existence* needs $S\to D(S)$, $s\mapsto\tau(s\,\cdot)$, to be surjective, which uses $\dim S<\infty$ (injective plus equal dimensions). Linearity of $m\mapsto f(m)$ also needs a word. Separately, the statement calls $\gamma_M$ just "an isomorphism". It is in fact an isomorphism of $S$-bimodules (I checked), and that should be said. That $\tau_{\rm en}$ is symmetrising (631) is asserted without the one-line check.

**Suggestion.** Insert: "Since $\tau$ is non-degenerate and $\dim S<\infty$, the map $S\to D(S)$, $s\mapsto\tau(s\,\cdot)$, is bijective." Then state "$\gamma_M$ is an isomorphism of $S$-bimodules" in the proposition, and add the check for $\tau_{\rm en}$.

### C4. The $A$-action on $M^{(*)}$ depends on $\tau$ (Medium)
**Problem.** Lines 676–684 transport the $A$-action to $M^{(*)}$ via $\alpha_M$. When I computed an example, the resulting module structure turned out to depend on $\tau$, not just up to isomorphism. Take $A=\Bbbk A_2$, $M=e_{11}A$, and $\tau(e_1)=c_1$, $\tau(e_2)=c_2$. Let $\varphi_0(e_{11})=e_1$ and $\varphi_1(e_{12})=e_2$. Then
$$e_{12}\cdot\varphi_1=\tfrac{c_2}{c_1}\,\varphi_0.$$
Line 642 says the *identifications* depend on $\tau$, but a reader could easily think the $A$-module $M^{(*)}$ itself is canonical.

**Suggestion.** Add a remark with this example. Different $\tau$ give isomorphic but not equal $A$-module structures on $M^{(*)}$ (the isomorphism is multiplication by a central unit of $S$). Alternatively, only use the canonical $A$-module $\mathbb D(M)$ and drop the transported action (see A4).

### C5. What does "$A$ is quadratic" mean for an arbitrary graded algebra? (Medium)
**Problem.** Definition `def:quadratic` defines a quadratic algebra *as* a quotient $T_S(V)/(R)$. Later, "$A$ is quadratic" is used for arbitrary graded $A$ (952, 1047). The equivalence "$\pi_A$ iso $\iff$ $A$ quadratic" (1045–1047) silently uses the fact that any graded isomorphism $A\cong T_{S'}(V')/(R')$ forces $S'\cong A_0$ and $V'\cong A_1$. The grading is essential here. For example, $\Bbbk A_3$ with $\deg e_{ij}=2(j-i)$ is not quadratic as a graded algebra, although the underlying ungraded algebra is the quadratic algebra $\Bbbk A_3$.

**Suggestion.** Add: "A graded algebra $A$ is *quadratic* if $A\cong T_S(V)/(R)$ as graded algebras for some $S,V,R$ as in Definition `def:quadratic`. By Proposition `prop:quadratic-basic`, necessarily $S\cong A_0$ and $V\cong A_1$." Then mention the doubled grading as a warning example.

### C6. Overloaded notation $R^\perp$ (Medium)
**Problem.** $R^\perp$ denotes a subset of $(V\otimes_S V)^*$ in Definition `def:orthogonals`, and a subset of $V^*\otimes_S V^*$ in Definition `def:quadratic-duals` (1158). The identification via $\theta_r$ is mentioned once (1086) and then used silently. When reading the biduality proof I lost track of which space I was in.

**Suggestion.** Use a different symbol for the version inside $V^*\otimes_S V^*$ (e.g. $R^!$, or $\theta_r^{-1}(R^\perp)$), or state prominently once: "From now on we identify $V^*\otimes_S V^*$ with $(V\otimes_S V)^*$ via $\theta_r$."

### C7. Proof of Theorem `thm:quadratic-bidual` is too compressed (High)
**Problem.** This is the main theorem of Lecture 3, and the proof is five lines. The key sentence, "the tensor $v\otimes w$ then acts on $g\otimes f$ by $g(f(v)w)$" (1220), hides a computation. One applies $\theta_\ell$ *for the bimodule $V^*$* to $\mathrm{ev}_v\otimes\mathrm{ev}_w$, and uses the right $S$-action $(gs)(w)=g(sw)$ on $V^*$ from `eq:bimodule-dual-actions`. It took me a long time to reconstruct this.

**Suggestion.** Write out the chain of identifications as a commutative square:
$$V\otimes_S V\xrightarrow{\ \mathrm{ev}\otimes\mathrm{ev}\ }{}^*(V^*)\otimes_S{}^*(V^*)\xrightarrow{\ \theta_\ell\ }{}^*(V^*\otimes_S V^*)\xrightarrow{\ \theta_r^*\ }{}^*\big((V\otimes_S V)^*\big)$$
Show that the composite is the evaluation isomorphism of Lemma `lem:S-bidual` for $M=V\otimes_S V$, with the one-line calculation $\theta_\ell(\mathrm{ev}_v\otimes\mathrm{ev}_w)(g\otimes f)=\mathrm{ev}_w(g\,f(v))=g(f(v)w)$. Then apply Lemma `lem:double-orthogonal`.

### C8. Proof of Proposition `prop:monomial-dual`(2) (Low)
**Problem.** "The functional vanishes on every other basis tensor. Hence $c^*b^*\in R^\perp$ exactly when $bc\notin\mathcal R$" (1297) shows *which basis elements* lie in $R^\perp$. It does not show that $R^\perp$ is *spanned* by them, which is the actual claim. That step needs the composable $c^*\otimes b^*$ to form a basis of $V^*\otimes_S V^*$ (which needs C1) that pairs with $\{b\otimes c\}$ like a dual basis. The notation "$c^*b^*$" also means $c^*\otimes b^*$ in some places and a product in $A^!$ in others.

**Suggestion.** Add the sentence: "Since $\{c^*\otimes b^*\}$ and $\{b\otimes c\}$ are dual bases up to the idempotent factors, the annihilator of a span of basis vectors is the span of the remaining dual basis vectors." Clarify the notation as well.

### C9. Proof of Proposition `prop:dual-tensor-products` (Medium)
**Problem.** "These relations allow every $W$ letter to move past every $V$ letter … Thus they present $A\otimes_\Bbbk B$" (1416) shows only that the presented algebra $C$ *surjects* onto $A\otimes B$, and that $C$ is spanned by products (word in $V$)(word in $W$). It does not show the kernel is exactly generated by these relations. The proof also uses without comment that $(V')^{\otimes2}$ splits into four blocks ($VV$, $VW$, $WV$, $WW$) and that orthogonal complements split blockwise.

**Suggestion.** Add the standard argument. The relations give algebra maps $A\to C$ and $B\to C$ with commuting images. Hence there is a linear map $A\otimes B\to C$, $a\otimes b\mapsto\bar a\bar b$, which is surjective and inverse to $C\twoheadrightarrow A\otimes B$. Then state the block decomposition explicitly. The same argument with signs handles $\otimes^{\rm gr}$.

### C10. "Commuting square becomes anticommuting square" is misleading (Medium)
**Problem.** In Example `ex:commuting-square-dual` (1446), replacing the basis element $d^*$ by $-d^*$ turns $b^*a^*=-d^*c^*$ into $b^*a^*=d^*c^*$. So $A^!$ is isomorphic to a commuting square (with arrows reversed). Likewise $\Bbbk A_2\otimes^{\rm gr}\Bbbk A_2\cong\Bbbk A_2\otimes\Bbbk A_2$. A beginner, myself included, concludes that signs produce a genuinely different algebra here, but they don't. (Exercise 1467–1469 hints at this: for $\lambda\neq0$ all the algebras are isomorphic.)

**Suggestion.** Add a remark that in this example the sign can be removed by rescaling an arrow, so it records the *presentation*, not the isomorphism class. Then add an example where signs really matter. The natural one ties sections together nicely: $\operatorname{Sym}(V)\cong\Bbbk[x]\otimes\Bbbk[y]$, so by Proposition `prop:dual-tensor-products`,
$$\operatorname{Sym}(V)^!\cong\Bbbk[x]^!\otimes^{\rm gr}\Bbbk[y]^!=\Bbbk[x^*]/(x^{*2})\otimes^{\rm gr}\Bbbk[y^*]/(y^{*2})\cong\textstyle\bigwedge D(V),$$
consistent with Proposition `prop:symmetric-exterior-dual`. Here $x^*y^*=-y^*x^*$ cannot be rescaled away when $\operatorname{char}\Bbbk\neq2$.

### C11. Hilbert series: what is the point? (Medium)
**Problem.** Hilbert series are introduced (970–1026), and several examples have $h_A=h_{A^!}$ (e.g. `ex:alternating-quadratic-dual` and the commuting square). I started to suspect $h_A=h_{A^!}$ in general, which is false: $\operatorname{Sym}$ and $\bigwedge$ differ. No relation between $h_A$ and $h_{A^!}$ is ever stated. Moreover, when $S\neq\Bbbk$ the scalar Hilbert series is too coarse. For $\Bbbk A_2$, $h_A(t)\,h_{A^!}(-t)=(2+t)(2-t)\neq1$.

**Suggestion.** Add a "preview" remark. For $S=\Bbbk$ and $A$ Koszul, $h_A(t)\,h_{A^!}(-t)=1$; check this on $\operatorname{Sym}/\bigwedge$. For $S=\Bbbk^{\oplus r}$, introduce the matrix Hilbert series $H_A(t)_{ij}=\sum_d\dim(e_iA_de_j)\,t^d$, for which a matrix version of the identity holds. State it with the course's side and transpose conventions and give a reference. This gives Hilbert series a purpose.

### C12. Smaller precision issues (Low)
- **Lemma `lem:hilbert-operations`(2)** uses $L$, which is not in the hypotheses ("Let $M,N$ be …"). **Lemma `lem:hilbert-tensor`** contains a *definition* (the grading on $V\otimes W$) inside its statement. Move it to a definition.
- **Bimodules (330–335):** "The left and right scalar actions agree" reads like an extra axiom, but it follows from bilinearity. Say "Bilinearity forces …".
- **Non-homogeneous right ideal (421–425):** explain *why* the quotient grading fails. In $A/I$, $\bar e_{12}=-\bar e_{22}$, so the images of $A_0$ and $A_1$ intersect non-trivially.
- **"There are no signs in these actions" (489):** this is puzzling at that point, since I had no reason to expect signs. Either explain where signs will appear later (Koszul sign rule, graded tensor products in Lecture 3) or delete it.
- **Shift convention (341–349):** $M(d)_j=M_{j+d}$ moves $M$ *down* by $d$, which is a classic source of confusion. Add "if $M$ is concentrated in degree $0$, then $M(d)$ is concentrated in degree $-d$" and perhaps a small picture.
- **Enveloping algebra (546–551):** in $m\cdot(s\otimes t^{\rm op})=tms$ the *first* tensor factor acts on the *right*. This is consistent but counterintuitive, and many books use left $S^{e}$-modules with $(s\otimes t)m=smt$. A remark explaining the choice would help.
- **"as graded algebras over $S$" (1214, 1227):** define this, presumably an isomorphism restricting to the identity on degree $0$.
- **Right vs. left dual:** line 1166 says "we use $A^!$ unless a side is specified". Say briefly which one will match $\operatorname{Ext}$ later, and why.
- **Artin–Wedderburn (242):** "every finite-dimensional left or right $B$-module is semisimple". In fact *every* $B$-module is, and that stronger form is what C3/B3 need.

---

## D. Notation, naming and typesetting

- **206–207:** "Every row space" is confusing because there is only one space of row vectors. Suggest "The space $\Bbbk^{1\times n}$ of row vectors is a right $\operatorname{Mat}_n(\Bbbk)$-module via matrix multiplication."
- **211–216:** the matrix display mixes `\vdots` and `\cdots` inconsistently in the second row.
- **231:** the theorem has two labels (`thm:artin-wedderburn`, `prop:semisimple`) and is cited at 707 as "Theorem `prop:semisimple`". Use one label.
- **"Locally finite" vs. "locally finite-dimensional":** lines 299, 319, 323, 506, 664 and 909 use both. Pick one.
- **$\operatorname{grmod}$ (323):** in much of the literature $\operatorname{grmod}A$ means *finitely generated* graded modules. Warn the reader that here it means locally finite-dimensional.
- **$e_i$ vs. $e_{ii}$:** coordinate idempotents of $\Bbbk^{\oplus r}$ ($e_i$) and matrix units ($e_{ii}$) are used interchangeably (687, 694, 814, 841, 918, 1264). State the identification once.
- **$P_1=e_{11}A$ (352)** is named, but $e_{22}A$ (377) is not. Define $P_i:=e_{ii}A$ once and use it throughout.
- **"Positive degree ideal" (432)** is introduced as preferred terminology and never used again.
- **$\bigwedge^2V$ (1129)** is not defined. Say "$(\bigwedge V)_2$".
- **"$c^*b^*$"** sometimes means $c^*\otimes b^*$ in $T_S(V^*)$ and sometimes the product in $A^!$ (1286, 1302, 1445). Say once that juxtaposition denotes the product in $T_S(\cdot)$.
- **"Last update: `\today`" (183)** prints the compile date, not the revision date. Use a fixed date or a version number.
- **Preamble:** `\makeindex` without `\printindex` or any `\index`; `bbm` is loaded but unused; many macros are unused (`\soc`, `\top`, `\std`, `\costd`, `\Rej`, `\dimvec`, `\LL`, `\Ab`, …). The file failed to compile on a minimal TeX installation because `bbm.sty` was missing, even though it isn't used. Removing unused packages makes the notes easier for students to compile themselves.

---

## E. Exercises

- **Lecture 1 has no exercises.** Suggestions:
  1. Compute $\operatorname{rad}(\Bbbk A_3)$ from the definition.
  2. Verify that the grading on $\Bbbk A_n$ in `ex:triangular-grading` is multiplicative.
  3. Compute $\mathbb D(P_i)$ for $\Bbbk A_3$ and identify it with a column module $Ae_{jj}$.
  4. Prove the counterexample in C2.
  5. Redo Example `ex:dual-blocks` with a non-standard $\tau$, and observe the dependence noted in C4.
- **Existing exercises (Lectures 2–3)** are well chosen. For self-study, add difficulty markers, hints, and short answers (or a separate solutions sheet). For the $\lambda$-exercise (1467–1469), a hint that rescaling shows all $\lambda\neq0$ give isomorphic algebras would connect it to C10.
- **A non-monomial example with $S=\Bbbk$ beyond $\operatorname{Sym}/\bigwedge$:** the quantum plane $A=\Bbbk\langle x,y\rangle/(xy-q\,yx)$. Its dual has relations $x^{*2}=y^{*2}=0$ and $x^*y^*+q\,y^*x^*=0$, a "quantum exterior algebra". Setting $q=1$ recovers Proposition `prop:symmetric-exterior-dual`. It is a good exercise in tracking the order reversal in $\theta_r$.

---

## F. Things I checked and found correct

To be fair to the notes: I verified the following by hand and found no mathematical errors. My criticisms above are about exposition and missing justification, not wrong statements.

- Gradings and degrees in Examples `ex:triangular-grading`, `ex:shifted-row` and `ex:matrix-hom`, and the $\mathbb Z^2$-grading.
- The non-homogeneous right ideal in $\Bbbk A_2$, and $(e_{13})=\Bbbk e_{13}$, $(e_{14})=\Bbbk e_{14}$.
- All actions in Example `ex:row-linear-dual`, and the degree computation at 488.
- The bimodule structures in `eq:enveloping-action`, `eq:bimodule-dual-actions` and Definition `def:en-dual`.
- Well-definedness and balancedness of $\theta_D,\theta_r,\theta_\ell,\theta_{\rm en}$, and the identity $\gamma\circ\theta_{\rm en}=\theta_r\circ(\mathrm{id}\otimes\gamma)$.
- The computation in Proposition `prop:quadratic-dual-sides`.
- $R^\perp$ in Example `ex:symmetric-orthogonals` and Proposition `prop:symmetric-exterior-dual`, including characteristic 2.
- Examples `ex:An-quadratic-dual`, `ex:alternating-quadratic-dual` and `ex:commuting-square-dual`, including the Hilbert series $2+2t+t^2$ and $4+4t+t^2$.
- The answers implicit in the exercises: e.g. $h=4+3t$ for $\Bbbk A_4/(e_{13},e_{24})$, and $h_{T_S(V)}=2/(1-t)$.
