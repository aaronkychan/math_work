# Change Proposal 9: Lecture 1

> **Applied on 14 October 2026.** All 17 approved replacements are in the source. The notes compile successfully, and the PDF has been updated. The exact passages and diffs below are retained as the approval record.

**Prepared:** 14 October 2026  
**Revised:** 14 October 2026, retaining the same proposal and replacement numbers.  
**Source:** [2026_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:258)  
**Scope:** Section 1 only, including its exercises.  
**Total:** 17 replacements; `+387` added lines, `-320` removed lines.

## Application Record

- Applied all 17 replacements after confirming that every quoted original passage matched the source exactly.
- Made only minor consistency corrections in later lectures: updated two references to the vector-space tensor construction and renamed the forward bidual maps from `coev` to `ev`, with the corresponding word changed to “evaluation”. No later mathematical argument was revised.
- Made layout-only adjustments: kept a short supplementary block together, allowed looser line breaking in three paragraphs, and removed trailing whitespace. The approved mathematical wording is unchanged.
- Preserved the preamble, the hidden-content setting, and the existing hidden solution. The homework was already synchronised and was not changed again during application.
- The built-in and local compilers both succeeded. The final local compilation has no warnings, overfull boxes, or unresolved references. `2026_Koszul.pdf` is saved beside the source.

## Editorial Decisions

- **Evaluation:** the canonical map is $V\to D(D(V))$. Name it evaluation; give its inverse explicitly when finite dimensional. Do not call the inverse coevaluation.
- **Two directions:** display both linear dual functors and both graded linear dual functors. All are exact. Biduality requires finite dimension for $D$, or local finiteness for $\mathbb D$.
- **General degree-zero algebra:** retain finite-dimensional semisimple $S$, not a one-simple assumption. Explain idempotents through direct summands and $\operatorname{Hom}_A(eA,M)\cong Me$.
- **Organisation of duals:** canonical linear duals handle $A$-modules. The one-sided $S$-duals handle $S$-modules and bimodules, including generators and relations. Compare them in one theorem after introducing the graded constructions. Transported $A$-actions are advanced and depend on a chosen symmetrising form.
- **Level of detail:** basis-first tensor products; their universal-property proof is supplementary. Two-sided duals, division-algebra forms, and limitations of duality remain advanced. Relocate worked homework solutions into hidden blocks after the exercise statements, without discarding the solutions.

## Homework and Notation Audit

- **Confirmed:** the homogeneous-map example is [Homework 1, Exercise 1(3)](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Homework1.tex). Replacements 5 and 16 have moved its solution to a hidden block after the lecture exercise.
- **Confirmed:** the form-comparison questions are Homework 1, Exercise 2. The assignment has been synchronised with Replacements 16 and 17: the supplied answer is hidden, the problem is retained, and only $\operatorname{char}\Bbbk\neq2$ is required for the advanced transported-action parts. Exercise 1(3) also has a hidden solution immediately after its statement. The assignment uses the native `solution` environment with `\noprintanswers`.
- **Notation audit:** no occurrence of $A_{>0}$ remains anywhere in the notes. Later lectures were already consistent; Replacement 7 changed the three occurrences in Lecture 1 to $A_+$.
- **Universal property:** a specified bilinear map induces the displayed linear map. Replacement 9 gives both the bilinear map and its domain and codomain.

**Dependencies:** The full set was applied together. Replacements 4 and 6 are linked; Replacements 5, 15, and 16 relocate the worked examples; Replacements 10--15 and 17 organise the duals. Replacement 9 uses the tensor universal-property label introduced in Replacement 8.

## Contents

| Replacement | Change | Lines |
| --- | --- | --- |
| [1](#replacement-1-introduce-exact-functors-before-the-contravariant-case) | Introduce Exact Functors Before the Contravariant Case | `+11` / `-14` |
| [2](#replacement-2-name-the-canonical-bidual-map-evaluation) | Name the Canonical Bidual Map Evaluation | `+18` / `-19` |
| [3](#replacement-3-explain-idempotents-and-their-direct-summands) | Explain Idempotents and Their Direct Summands | `+41` / `-16` |
| [4](#replacement-4-use-idempotents-to-describe-module-homomorphisms) | Use Idempotents to Describe Module Homomorphisms | `+19` / `-14` |
| [5](#replacement-5-relocate-the-confirmed-homework-solution-to-a-hidden-block) | Relocate the Confirmed Homework Solution to a Hidden Block | `+0` / `-21` |
| [6](#replacement-6-introduce-the-left-graded-module-category-at-the-right-place) | Introduce the Left Graded Module Category at the Right Place | `+1` / `-0` |
| [7](#replacement-7-use-the-positive-degree-ideal-notation-a) | Use the Positive Degree Ideal Notation A+ | `+6` / `-6` |
| [8](#replacement-8-construct-vector-space-tensor-products-from-bases) | Construct Vector-Space Tensor Products from Bases | `+27` / `-18` |
| [9](#replacement-9-make-indexing-explicit-and-add-polynomial-examples) | Make Indexing Explicit and Add Polynomial Examples | `+32` / `-16` |
| [10](#replacement-10-display-both-directions-of-linear-duality-and-their-precise-scope) | Display Both Directions of Linear Duality and Their Precise Scope | `+70` / `-60` |
| [11](#replacement-11-keep-s-module-and-bimodule-duals-as-the-basic-s-dual-constructions) | Keep S-Module and Bimodule Duals as the Basic S-Dual Constructions | `+33` / `-39` |
| [12](#replacement-12-supply-symmetrising-forms-for-general-semisimple-algebras) | Supply Symmetrising Forms for General Semisimple Algebras | `+19` / `-4` |
| [13](#replacement-13-make-the-comparison-theorem-the-common-summary) | Make the Comparison Theorem the Common Summary | `+13` / `-3` |
| [14](#replacement-14-concentrate-the-comparison-proof-on-right-modules) | Concentrate the Comparison Proof on Right Modules | `+22` / `-26` |
| [15](#replacement-15-remove-the-duplicate-worked-example-and-separate-transported-actions) | Remove the Duplicate Worked Example and Separate Transported Actions | `+22` / `-56` |
| [16](#replacement-16-make-the-exercises-self-contained-and-retain-hidden-solutions) | Make the Exercises Self-Contained and Retain Hidden Solutions | `+48` / `-6` |
| [17](#replacement-17-use-only-the-needed-characteristic-assumption) | Use Only the Needed Characteristic Assumption | `+5` / `-2` |

**Diff legend:** `-` removes a line; `+` adds a line; a leading space retains context. Old line numbers refer to the source inspected on 14 October. New line numbers include the preceding proposed replacements. The full passages below each diff are exact, without ellipses standing for omitted source.

## Later-Lecture Follow-Ups

Outside Lecture 1, only non-printing reminders and the minor notation, reference, and line-breaking corrections listed above were made. Substantive later-lecture revisions remain deferred.

| Location | Reminder |
| --- | --- |
| Lecture 2, tensor products | The vector-space universal-property and basis-construction references have been updated. The broader revision to arbitrary algebras, explicit defining identities, and supplementary proofs remains deferred. |
| Lecture 2, idempotent tensors and tensor duality | Keep the idempotent-matching calculation central. For the general $(A,B,C)$ version, state the finite-projectivity hypothesis on the appropriate tensor factor; finite vector-space dimension alone is insufficient over a general algebra. |
| Lecture 2, tensor algebras | Retain the universal-property statement and formula in the main text; shorten or move routine proof details to supplementary material. Address remaining local editorial comments when Lecture 2 is revised. |
| Lecture 3, biduals | Completed the immediate notation correction: forward bidual maps are named evaluation and written `ev`, retaining the existing left/right conventions and arguments. |
| Lecture 4 and planned Lectures 6--7 | Reuse $A_+$ from Lecture 1. Explain later that $\operatorname{Hom}_A(M,S)\cong\operatorname{Hom}_S(M/MA_+,S)$, and that $\operatorname{Ext}_A^i(M,S)$ dualises the generator data in a minimal resolution. This is not a derived functor of $\operatorname{Hom}_S(-,S)$, which is exact. Audit graded shifts and the Yoneda algebra action when writing the precise statement. |
| Before the bibliography | The requested linked notation table is deferred by the Lecture 1-only scope; add the page break and table in a separately authorised global update. |

## Writing Conventions Updated in the Skill

- Retain **degree-preserving**, **orientation-preserving**, and **orientation-reversing**; leave phrases such as “degree $i$ component” unhyphenated.
- Use compact basis notation, for example $\{u_i\mid i\in I\}$ and $\{u_i\otimes v_j\mid i\in I,\ j\in J\}$.
- Say **arbitrary family** when any set-indexed family is allowed; otherwise state the restriction. Give full index ranges on sums and products.
- Call $u\otimes v$ an **element**, or a **vector** when appropriate, rather than “a tensor”.
- Distinguish an **induced** linear map from the bilinear formula that specifies it. Preserve the object type and existing parts of a definition when adding notation.

## Checks

- Every active Lecture 1 `\comm` is accounted for by a replacement or by the settled discussion reflected above.
- Commented-out source and the hidden solution are preserved verbatim; the hidden setting is unchanged.
- Replacement intervals do not overlap, proposed labels are unique, and Lecture 1 references resolve in the assembled proposal.
- No substantive mathematical replacement extends beyond Section 1; the later-lecture consistency corrections are recorded above.
- The updated `Homework1.tex` compiled successfully with the built-in and local compilers; `Homework1.pdf` is saved beside it. Only the current solution-visibility setting was used.
- The approved text has been applied and compiled with both compilers. The final local log has no warnings or unresolved references, and `2026_Koszul.pdf` is saved in the course folder.

---

## Replacement 1: Introduce Exact Functors Before the Contravariant Case

**Source:** [Lecture 1, line 371](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:371)  
**Added:** `+11` lines | **Removed:** `-14` lines

Define ordinary exactness first. Arrow reversal belongs to contravariance; exchanging injections and surjections also requires exactness. Retain the existing label for cross-references.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -371,19 +371,16 @@
-\begin{definition}\label{def:exact-contravariant}
+\begin{definition}\label{def:exact-functor}\label{def:exact-contravariant}
 Let $A,B$ be $\Bbbk$-algebras.
-\comm{the obvious natural thing to do is to introduce exact (covariant) functor first, the whole purpose of introducing opposite category is so that we can talk about duality as if they are covairant; why suddenly do exact contravar duality.  introduce usual exact functor, then remark they preserves injection/surjection, and so contravariant exact functors, which are those that starts in opposite category, will swaps injection/surjection. }
-A contravariant functor $F:(\Mod A)^\op\to\Mod B$ is \defn{exact} if $F(0)=0$ and it sends every short exact sequence \eqref{eq:short-exact-sequence} to a short exact sequence
+A functor $F:\Mod A\to\Mod B$ is \defn{exact} if $F(0)=0$ and every short exact sequence \eqref{eq:short-exact-sequence} gives a short exact sequence
+\[
+0\longrightarrow F(L)\xrightarrow{F(i)}F(M)\xrightarrow{F(p)}F(N)\longrightarrow0.
+\]
+\end{definition}
+
+An exact functor preserves injective and surjective maps: apply it to
+$0\to L\xrightarrow{i}M\to M/i(L)\to0$ and $0\to\Ker p\to M\xrightarrow{p}N\to0$, respectively.
+For a functor $F:(\Mod A)^\op\to\Mod B$, exactness instead means that \eqref{eq:short-exact-sequence} gives
 \[
 0\longrightarrow F(N)\xrightarrow{F(p)}F(M)\xrightarrow{F(i)}F(L)\longrightarrow0.
 \]
-\end{definition}
+Thus an exact contravariant functor exchanges injective and surjective maps.
 
-An exact contravariant functor exchanges injective and surjective maps:
-\[
-f\text{ injective}\ \Longrightarrow\ F(f)\text{ surjective},
-\qquad
-f\text{ surjective}\ \Longrightarrow\ F(f)\text{ injective}
-\quad(f:M\to N).
-\]
-Indeed, apply $F$ to $0\to M\xrightarrow{f}N\to N/f(M)\to0$ in the first case, and to $0\to\Ker f\to M\xrightarrow{f}N\to0$ in the second.
-Contravariance alone reverses arrows; without exactness, the two implications need not hold.
-
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{definition}\label{def:exact-contravariant}
Let $A,B$ be $\Bbbk$-algebras.
\comm{the obvious natural thing to do is to introduce exact (covariant) functor first, the whole purpose of introducing opposite category is so that we can talk about duality as if they are covairant; why suddenly do exact contravar duality.  introduce usual exact functor, then remark they preserves injection/surjection, and so contravariant exact functors, which are those that starts in opposite category, will swaps injection/surjection. }
A contravariant functor $F:(\Mod A)^\op\to\Mod B$ is \defn{exact} if $F(0)=0$ and it sends every short exact sequence \eqref{eq:short-exact-sequence} to a short exact sequence
\[
0\longrightarrow F(N)\xrightarrow{F(p)}F(M)\xrightarrow{F(i)}F(L)\longrightarrow0.
\]
\end{definition}

An exact contravariant functor exchanges injective and surjective maps:
\[
f\text{ injective}\ \Longrightarrow\ F(f)\text{ surjective},
\qquad
f\text{ surjective}\ \Longrightarrow\ F(f)\text{ injective}
\quad(f:M\to N).
\]
Indeed, apply $F$ to $0\to M\xrightarrow{f}N\to N/f(M)\to0$ in the first case, and to $0\to\Ker f\to M\xrightarrow{f}N\to0$ in the second.
Contravariance alone reverses arrows; without exactness, the two implications need not hold.

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{definition}\label{def:exact-functor}\label{def:exact-contravariant}
Let $A,B$ be $\Bbbk$-algebras.
A functor $F:\Mod A\to\Mod B$ is \defn{exact} if $F(0)=0$ and every short exact sequence \eqref{eq:short-exact-sequence} gives a short exact sequence
\[
0\longrightarrow F(L)\xrightarrow{F(i)}F(M)\xrightarrow{F(p)}F(N)\longrightarrow0.
\]
\end{definition}

An exact functor preserves injective and surjective maps: apply it to
$0\to L\xrightarrow{i}M\to M/i(L)\to0$ and $0\to\Ker p\to M\xrightarrow{p}N\to0$, respectively.
For a functor $F:(\Mod A)^\op\to\Mod B$, exactness instead means that \eqref{eq:short-exact-sequence} gives
\[
0\longrightarrow F(N)\xrightarrow{F(p)}F(M)\xrightarrow{F(i)}F(L)\longrightarrow0.
\]
Thus an exact contravariant functor exchanges injective and surjective maps.

```

</details>

---

## Replacement 2: Name the Canonical Bidual Map Evaluation

**Source:** [Lecture 1, line 409](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:409)  
**Added:** `+18` lines | **Removed:** `-19` lines

Use the accepted convention: evaluation is the always-defined forward map. Give an explicit inverse only in finite dimension, and keep verification supplementary. The inverse is not renamed coevaluation.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -409,27 +406,26 @@
-On finite-dimensional spaces, the canonical map to the bidual gives a natural isomorphism, which we denote by $\mathrm{coev}$:
+For every vector space $V$, evaluation defines a natural injective map
+\begin{equation}\label{eq:vector-bidual-evaluation}
+\mathrm{ev}_V:V\longrightarrow D(D(V)),\qquad
+v\longmapsto(\lambda\mapsto\lambda(v)).
+\end{equation}
+If $V$ is finite-dimensional, choose a basis $v_1,\ldots,v_n$ and its \defn{dual basis} $v_1^*,\ldots,v_n^*$, defined by $v_i^*(v_j)=\delta_{ij}$.
+Then
 \[
-\mathrm{coev}:\id_{\mod\Bbbk}\xrightarrow{\sim}D\circ D,
-\qquad
-\mathrm{coev}_V:V\longrightarrow D(D(V)),\quad
-x\longmapsto(\lambda\mapsto\lambda(x)).
+\mathrm{ev}_V^{-1}:D(D(V))\longrightarrow V,\qquad
+\Phi\longmapsto\sum_{i=1}^n\Phi(v_i^*)v_i.
 \]
+Consequently, $D:(\mod\Bbbk)^\op\to\mod\Bbbk$ is a duality.
 \begin{supplementary}
-Indeed, if $x\neq0$, some $\lambda\in D(V)$ satisfies $\lambda(x)\neq0$, so $\mathrm{coev}_V$ is injective; equal finite dimensions give surjectivity.
-Naturality follows from
+If $v\neq0$, choose $\lambda\in D(V)$ with $\lambda(v)\neq0$; hence $\mathrm{ev}_V$ is injective.
+For $u:V\to W$, $v\in V$, and $\lambda\in D(W)$,
 \[
-D(D(u))(\mathrm{coev}_V(x))(\lambda)
-=\lambda(u(x))
-=\mathrm{coev}_W(u(x))(\lambda)
-\quad(x\in V,\ \lambda\in D(W)).
+D(D(u))(\mathrm{ev}_V(v))(\lambda)=\lambda(u(v))
+=\mathrm{ev}_W(u(v))(\lambda),
 \]
+which proves naturality.
+In finite dimension, writing $\lambda=\sum_{i=1}^n\lambda(v_i)v_i^*$ gives
+$\Phi(\lambda)=\lambda(\sum_{i=1}^n\Phi(v_i^*)v_i)$.
+Thus the displayed formula is the inverse of \eqref{eq:vector-bidual-evaluation}, and is independent of the chosen basis.
 \end{supplementary}
-\old{
-We write $\mathrm{ev}_V:=\mathrm{coev}_V^{-1}:D(D(V))\to V$ for the inverse: $\mathrm{ev}_V(\Phi)$ is the unique $x\in V$ such that $\Phi(\lambda)=\lambda(x)$ for every $\lambda\in D(V)$.
-}
-\comm{defining evaluation as inverse of coevaluation is a big no no.  evaluation has its own proper definition, and it is also the more natural map than coevaluation.  define it and say that coev and ev are invese to each other at what situation instead.  This applies to subsec 1.11 too.
-
-Genuine question (but really is comes from Lem 1.46): why is coevaluation more superior than evaluation?  if it is natural isom, then the inverse must be evaluation anyway??  Isn't evaluation the map (nat. transf) that always exists??
-}
-Consequently, $D:(\mod\Bbbk)^\op\to\mod\Bbbk$ is a duality.
 \end{example}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
On finite-dimensional spaces, the canonical map to the bidual gives a natural isomorphism, which we denote by $\mathrm{coev}$:
\[
\mathrm{coev}:\id_{\mod\Bbbk}\xrightarrow{\sim}D\circ D,
\qquad
\mathrm{coev}_V:V\longrightarrow D(D(V)),\quad
x\longmapsto(\lambda\mapsto\lambda(x)).
\]
\begin{supplementary}
Indeed, if $x\neq0$, some $\lambda\in D(V)$ satisfies $\lambda(x)\neq0$, so $\mathrm{coev}_V$ is injective; equal finite dimensions give surjectivity.
Naturality follows from
\[
D(D(u))(\mathrm{coev}_V(x))(\lambda)
=\lambda(u(x))
=\mathrm{coev}_W(u(x))(\lambda)
\quad(x\in V,\ \lambda\in D(W)).
\]
\end{supplementary}
\old{
We write $\mathrm{ev}_V:=\mathrm{coev}_V^{-1}:D(D(V))\to V$ for the inverse: $\mathrm{ev}_V(\Phi)$ is the unique $x\in V$ such that $\Phi(\lambda)=\lambda(x)$ for every $\lambda\in D(V)$.
}
\comm{defining evaluation as inverse of coevaluation is a big no no.  evaluation has its own proper definition, and it is also the more natural map than coevaluation.  define it and say that coev and ev are invese to each other at what situation instead.  This applies to subsec 1.11 too.

Genuine question (but really is comes from Lem 1.46): why is coevaluation more superior than evaluation?  if it is natural isom, then the inverse must be evaluation anyway??  Isn't evaluation the map (nat. transf) that always exists??
}
Consequently, $D:(\mod\Bbbk)^\op\to\mod\Bbbk$ is a duality.
\end{example}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
For every vector space $V$, evaluation defines a natural injective map
\begin{equation}\label{eq:vector-bidual-evaluation}
\mathrm{ev}_V:V\longrightarrow D(D(V)),\qquad
v\longmapsto(\lambda\mapsto\lambda(v)).
\end{equation}
If $V$ is finite-dimensional, choose a basis $v_1,\ldots,v_n$ and its \defn{dual basis} $v_1^*,\ldots,v_n^*$, defined by $v_i^*(v_j)=\delta_{ij}$.
Then
\[
\mathrm{ev}_V^{-1}:D(D(V))\longrightarrow V,\qquad
\Phi\longmapsto\sum_{i=1}^n\Phi(v_i^*)v_i.
\]
Consequently, $D:(\mod\Bbbk)^\op\to\mod\Bbbk$ is a duality.
\begin{supplementary}
If $v\neq0$, choose $\lambda\in D(V)$ with $\lambda(v)\neq0$; hence $\mathrm{ev}_V$ is injective.
For $u:V\to W$, $v\in V$, and $\lambda\in D(W)$,
\[
D(D(u))(\mathrm{ev}_V(v))(\lambda)=\lambda(u(v))
=\mathrm{ev}_W(u(v))(\lambda),
\]
which proves naturality.
In finite dimension, writing $\lambda=\sum_{i=1}^n\lambda(v_i)v_i^*$ gives
$\Phi(\lambda)=\lambda(\sum_{i=1}^n\Phi(v_i^*)v_i)$.
Thus the displayed formula is the inverse of \eqref{eq:vector-bidual-evaluation}, and is independent of the chosen basis.
\end{supplementary}
\end{example}

```

</details>

---

## Replacement 3: Explain Idempotents and Their Direct Summands

**Source:** [Lecture 1, line 470](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:470)  
**Added:** `+41` lines | **Removed:** `-16` lines

State the point of the triangular example, shorten its main calculation, define orthogonal and primitive idempotents, and show the projection/inclusion factorisation without introducing an auxiliary module symbol.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -470,25 +466,50 @@
 \begin{example}\label{ex:semisimple-algebras}
 The algebras $\Bbbk^{\oplus r}$ and $\Mat_n(\Bbbk)$ are semisimple by Theorem~\ref{thm:artin-wedderburn}.
-For $A=\Bbbk A_2$, the ideal $J=\Bbbk e_{12}$ satisfies $J^2=0$ (see also Homework question).
-If $L$ is simple, then $LJ$ is either $0$ or $L$; the latter would give $L=LJ^2=0$. Hence every maximal right ideal contains $J$.
-Since $A/J\cong\Bbbk\oplus\Bbbk$, those ideals are $\Bbbk e_{11}\oplus\Bbbk e_{12}$ and $\Bbbk e_{12}\oplus\Bbbk e_{22}$. Their intersection is $J$, so $\rad A=\Bbbk e_{12}\neq0$.
-\comm{this example is somewhat unnecssarily verbal and yet obscure the crucial logic.  Again, what is the purpose of the example.  Write the purpose first, and then show it.  If you claim something, then clarify why you are doing each step you do.  Use more symbols instead of words.  }
+Upper triangular matrices need not form a semisimple algebra: for $A=\Bbbk A_2$,
+\[
+\rad A=\Bbbk e_{12}\neq0,\qquad
+A/\rad A\cong\Bbbk^{\oplus2}.
+\]
+\begin{supplementary}
+Put $J=\Bbbk e_{12}$, so $J^2=0$.
+For a simple right module $L$, simplicity gives $LJ=0$ or $LJ=L$; the second alternative implies $L=LJ^2=0$, a contradiction.
+Hence $J$ is contained in every maximal right ideal.
+The quotient $A/J\cong\Bbbk^{\oplus2}$ has exactly two maximal right ideals, whose inverse images have intersection
+\[
+(\Bbbk e_{11}\oplus\Bbbk e_{12})\cap
+(\Bbbk e_{12}\oplus\Bbbk e_{22})=J.
+\]
+\end{supplementary}
 \end{example}
 
-\begin{definition}
-An element $e$ of an algebra $A$ is \defn{idempotent} if $e^2=e$.
-\comm{introduce primitive idempotent and othogonal idempotent and talk about sum to one here.}
+\begin{definition}\label{def:idempotents}
+An element $e\in A$ is \defn{idempotent} if $e^2=e$.
+Idempotents $e,f$ are \defn{orthogonal} if $ef=fe=0$.
+A non-zero idempotent is \defn{primitive} if it is not the sum of two non-zero orthogonal idempotents.
+A finite family $e_1,\ldots,e_r$ of pairwise orthogonal idempotents is \defn{complete} if $\sum_{i=1}^r e_i=1_A$.
 \end{definition}
 
-
 \begin{remark}\label{rem:idempotent-units}
-\comm{chect the use of remark is really relevant to the updated content.}
-An idempotent $e$ is a local unit at a direct summand: 
-\comm{add commutative diagram $A \xrightarrow{e} A$ factors through a direct summand $P$ via canonical projection and inclusion}
-$e$ is the identity of the \defn{idempotent truncation} (or \defn{corner subalgebra}) $eAe=\{eae\mid a\in A\}$
-
-It will be convenient to talk about \defn{coordinate idempotent} $e_i=(0,\ldots,1_{A_i},\ldots,0)$
-for a finite product $A=\prod_{i=1}^r A_i$.
-They sum to $1_A$ and are \defn{pairwise orthogonal}, meaning $e_ie_j=0$ for $i\neq j$.
+For orthogonal idempotents $e,f\in A$,
+\[
+(e+f)A=eA\oplus fA.
+\]
+An idempotent acts as a local identity: left multiplication by $e$ is a projection onto the right module $eA$,
+\[
+A=eA\oplus(1-e)A,\qquad
+\xymatrix@C=42pt@R=18pt{
+A \ar[rr]^{a\mapsto ea} \ar[dr]_{a\mapsto ea} && A\\
+& eA \ar[ur]_{\text{inclusion}} &
+}
+\]
+and $e(ea)=ea$.
+The \defn{corner subalgebra} $eAe=\{eae\mid a\in A\}$ has identity $e$.
+For $A=\prod_{i=1}^r A_i$, the \defn{coordinate idempotents} $e_i=(0,\ldots,1_{A_i},\ldots,0)$ are a complete orthogonal family and are the identities of the individual factors.
+In $A=\Bbbk A_n$, the diagonal matrix units $e_{11},\ldots,e_{nn}$ are primitive, since $e_{ii}Ae_{ii}=\Bbbk e_{ii}$.
+For $n\geq2$, the sum $e=e_{11}+\cdots+e_{n-1,n-1}$ gives the corner
+\[
+eAe=\left\{\begin{pmatrix}B&0\\0&0\end{pmatrix}\;\middle|\;B\in\Bbbk A_{n-1}\right\}
+\cong\Bbbk A_{n-1}.
+\]
 \end{remark}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:semisimple-algebras}
The algebras $\Bbbk^{\oplus r}$ and $\Mat_n(\Bbbk)$ are semisimple by Theorem~\ref{thm:artin-wedderburn}.
For $A=\Bbbk A_2$, the ideal $J=\Bbbk e_{12}$ satisfies $J^2=0$ (see also Homework question).
If $L$ is simple, then $LJ$ is either $0$ or $L$; the latter would give $L=LJ^2=0$. Hence every maximal right ideal contains $J$.
Since $A/J\cong\Bbbk\oplus\Bbbk$, those ideals are $\Bbbk e_{11}\oplus\Bbbk e_{12}$ and $\Bbbk e_{12}\oplus\Bbbk e_{22}$. Their intersection is $J$, so $\rad A=\Bbbk e_{12}\neq0$.
\comm{this example is somewhat unnecssarily verbal and yet obscure the crucial logic.  Again, what is the purpose of the example.  Write the purpose first, and then show it.  If you claim something, then clarify why you are doing each step you do.  Use more symbols instead of words.  }
\end{example}

\begin{definition}
An element $e$ of an algebra $A$ is \defn{idempotent} if $e^2=e$.
\comm{introduce primitive idempotent and othogonal idempotent and talk about sum to one here.}
\end{definition}


\begin{remark}\label{rem:idempotent-units}
\comm{chect the use of remark is really relevant to the updated content.}
An idempotent $e$ is a local unit at a direct summand: 
\comm{add commutative diagram $A \xrightarrow{e} A$ factors through a direct summand $P$ via canonical projection and inclusion}
$e$ is the identity of the \defn{idempotent truncation} (or \defn{corner subalgebra}) $eAe=\{eae\mid a\in A\}$

It will be convenient to talk about \defn{coordinate idempotent} $e_i=(0,\ldots,1_{A_i},\ldots,0)$
for a finite product $A=\prod_{i=1}^r A_i$.
They sum to $1_A$ and are \defn{pairwise orthogonal}, meaning $e_ie_j=0$ for $i\neq j$.
\end{remark}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:semisimple-algebras}
The algebras $\Bbbk^{\oplus r}$ and $\Mat_n(\Bbbk)$ are semisimple by Theorem~\ref{thm:artin-wedderburn}.
Upper triangular matrices need not form a semisimple algebra: for $A=\Bbbk A_2$,
\[
\rad A=\Bbbk e_{12}\neq0,\qquad
A/\rad A\cong\Bbbk^{\oplus2}.
\]
\begin{supplementary}
Put $J=\Bbbk e_{12}$, so $J^2=0$.
For a simple right module $L$, simplicity gives $LJ=0$ or $LJ=L$; the second alternative implies $L=LJ^2=0$, a contradiction.
Hence $J$ is contained in every maximal right ideal.
The quotient $A/J\cong\Bbbk^{\oplus2}$ has exactly two maximal right ideals, whose inverse images have intersection
\[
(\Bbbk e_{11}\oplus\Bbbk e_{12})\cap
(\Bbbk e_{12}\oplus\Bbbk e_{22})=J.
\]
\end{supplementary}
\end{example}

\begin{definition}\label{def:idempotents}
An element $e\in A$ is \defn{idempotent} if $e^2=e$.
Idempotents $e,f$ are \defn{orthogonal} if $ef=fe=0$.
A non-zero idempotent is \defn{primitive} if it is not the sum of two non-zero orthogonal idempotents.
A finite family $e_1,\ldots,e_r$ of pairwise orthogonal idempotents is \defn{complete} if $\sum_{i=1}^r e_i=1_A$.
\end{definition}

\begin{remark}\label{rem:idempotent-units}
For orthogonal idempotents $e,f\in A$,
\[
(e+f)A=eA\oplus fA.
\]
An idempotent acts as a local identity: left multiplication by $e$ is a projection onto the right module $eA$,
\[
A=eA\oplus(1-e)A,\qquad
\xymatrix@C=42pt@R=18pt{
A \ar[rr]^{a\mapsto ea} \ar[dr]_{a\mapsto ea} && A\\
& eA \ar[ur]_{\text{inclusion}} &
}
\]
and $e(ea)=ea$.
The \defn{corner subalgebra} $eAe=\{eae\mid a\in A\}$ has identity $e$.
For $A=\prod_{i=1}^r A_i$, the \defn{coordinate idempotents} $e_i=(0,\ldots,1_{A_i},\ldots,0)$ are a complete orthogonal family and are the identities of the individual factors.
In $A=\Bbbk A_n$, the diagonal matrix units $e_{11},\ldots,e_{nn}$ are primitive, since $e_{ii}Ae_{ii}=\Bbbk e_{ii}$.
For $n\geq2$, the sum $e=e_{11}+\cdots+e_{n-1,n-1}$ gives the corner
\[
eAe=\left\{\begin{pmatrix}B&0\\0&0\end{pmatrix}\;\middle|\;B\in\Bbbk A_{n-1}\right\}
\cong\Bbbk A_{n-1}.
\]
\end{remark}

```

</details>

---

## Replacement 4: Use Idempotents to Describe Module Homomorphisms

**Source:** [Lecture 1, line 572](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:572)  
**Added:** `+19` lines | **Removed:** `-14` lines

Combine the regular-module examples and the scalar convention. Name the evaluation result Yoneda lemma and give its explicit inverse. Define bimodules with different acting algebras before using the corner example.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -572,22 +593,27 @@
-Similarly, $\Grmod(A^\op)$ is the category of graded left $A$-modules.
-
 \begin{definition}\label{def:bimodule}
-For an algebra $A$, an \defn{$A$-bimodule} is a vector space $M$ with $\Bbbk$-bilinear left and right $A$-module actions satisfying $(am)b=a(mb)$ for all $a,b\in A$ and $m\in M$.
-It is graded if $M=\bigoplus_{j\in\Z}M_j$ and $A_iM_jA_k\subset M_{i+j+k}$ for all $i,j,k\in\Z$.
+For $\Bbbk$-algebras $B,C$, a \defn{$(B,C)$-bimodule} is a vector space $M$ with bilinear left $B$- and right $C$-module actions satisfying $(bm)c=b(mc)$ for all $b\in B$, $c\in C$, and $m\in M$.
+When $B=C=A$, we call $M$ an \defn{$A$-bimodule}.
+For graded $B,C$, a grading on $M$ satisfies $B_iM_jC_k\subset M_{i+j+k}$ for all $i,j,k\in\Z$.
 \end{definition}
 
-More precisely, we should have call the bimodules in Definition \ref{def:bimodule} as `$\Bbbk$-central $A$-bimodule' instead; but we will always work over a field $\Bbbk$ and so will not make such distinction from now on.
+Bilinearity implies $(c1_B)m=cm=m(c1_C)$ for $c\in\Bbbk$; we always use this scalar convention.
+Multiplication makes $A_A$ a graded right module and ${}_AA_A$ a graded bimodule; each $A_i$ is an $A_0$-bimodule.
 
-The algebra $A$ is a graded $A$-bimodule by multiplication, and each $A_i$ is an $A_0$-bimodule.
-Bilinearity forces the left and right scalar actions to agree: $(c1_A)m=cm=m(c1_A)$ for $c\in\Bbbk$.
-
-For an $A$-bimodule $M$ and idempotents $e,f\in A$, the local-unit interpretation in Remark~\ref{rem:idempotent-units} becomes $em=m=mf$ for $m\in eMf=\{enf\mid n\in M\}$.
-\comm{add Yoneda lemma here: $\Hom_A(eA,M)\cong Me$ as vector spaces.  then after lemma, write $eMf$ as bimodule example}
-
-\old{The left and right local units may differ: $e_{11}e_{12}=e_{12}=e_{12}e_{22}$ in $\Bbbk A_2$.}\comm{this sentence just confuses people}
+Idempotents also describe maps out of the summands of $A_A$.
+\begin{lemma}[Yoneda lemma]\label{lem:idempotent-hom}
+For an idempotent $e\in A$ and a right $A$-module $M$, evaluation at $e$ gives a natural vector space isomorphism
+\[
+\Hom_A(eA,M)\xrightarrow{\sim}Me,\qquad f\longmapsto f(e),
+\quad\text{with inverse}\quad m\longmapsto(ea\mapsto ma).
+\]
+\end{lemma}
+\begin{proof}
+We have $f(e)=f(e)e$ and $f(ea)=f(e)a$.
+If $m=me$, the map $ea\mapsto ma$ is well-defined because $ea=ea'$ implies $ma=mea=mea'=ma'$.
+These formulas prove that the maps are inverse; postcomposition by a module map $M\to N$ proves naturality.
+\end{proof}
 
 \begin{example}
-\comm{should this combine with 2nd para below definition of bimodule??}
-The decomposition $A=\bigoplus_{i\in\Z}A_i$ makes the right regular module $A_A$ a graded module, and ${}_AA_A$ a graded bimodule.
+For an $A$-bimodule $M$ and idempotents $e,f\in A$, the space $eMf:=\{enf\mid n\in M\}$ is an $(eAe,fAf)$-bimodule, with local identities $em=m=mf$ for $m\in eMf$.
 \end{example}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
Similarly, $\Grmod(A^\op)$ is the category of graded left $A$-modules.

\begin{definition}\label{def:bimodule}
For an algebra $A$, an \defn{$A$-bimodule} is a vector space $M$ with $\Bbbk$-bilinear left and right $A$-module actions satisfying $(am)b=a(mb)$ for all $a,b\in A$ and $m\in M$.
It is graded if $M=\bigoplus_{j\in\Z}M_j$ and $A_iM_jA_k\subset M_{i+j+k}$ for all $i,j,k\in\Z$.
\end{definition}

More precisely, we should have call the bimodules in Definition \ref{def:bimodule} as `$\Bbbk$-central $A$-bimodule' instead; but we will always work over a field $\Bbbk$ and so will not make such distinction from now on.

The algebra $A$ is a graded $A$-bimodule by multiplication, and each $A_i$ is an $A_0$-bimodule.
Bilinearity forces the left and right scalar actions to agree: $(c1_A)m=cm=m(c1_A)$ for $c\in\Bbbk$.

For an $A$-bimodule $M$ and idempotents $e,f\in A$, the local-unit interpretation in Remark~\ref{rem:idempotent-units} becomes $em=m=mf$ for $m\in eMf=\{enf\mid n\in M\}$.
\comm{add Yoneda lemma here: $\Hom_A(eA,M)\cong Me$ as vector spaces.  then after lemma, write $eMf$ as bimodule example}

\old{The left and right local units may differ: $e_{11}e_{12}=e_{12}=e_{12}e_{22}$ in $\Bbbk A_2$.}\comm{this sentence just confuses people}

\begin{example}
\comm{should this combine with 2nd para below definition of bimodule??}
The decomposition $A=\bigoplus_{i\in\Z}A_i$ makes the right regular module $A_A$ a graded module, and ${}_AA_A$ a graded bimodule.
\end{example}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{definition}\label{def:bimodule}
For $\Bbbk$-algebras $B,C$, a \defn{$(B,C)$-bimodule} is a vector space $M$ with bilinear left $B$- and right $C$-module actions satisfying $(bm)c=b(mc)$ for all $b\in B$, $c\in C$, and $m\in M$.
When $B=C=A$, we call $M$ an \defn{$A$-bimodule}.
For graded $B,C$, a grading on $M$ satisfies $B_iM_jC_k\subset M_{i+j+k}$ for all $i,j,k\in\Z$.
\end{definition}

Bilinearity implies $(c1_B)m=cm=m(c1_C)$ for $c\in\Bbbk$; we always use this scalar convention.
Multiplication makes $A_A$ a graded right module and ${}_AA_A$ a graded bimodule; each $A_i$ is an $A_0$-bimodule.

Idempotents also describe maps out of the summands of $A_A$.
\begin{lemma}[Yoneda lemma]\label{lem:idempotent-hom}
For an idempotent $e\in A$ and a right $A$-module $M$, evaluation at $e$ gives a natural vector space isomorphism
\[
\Hom_A(eA,M)\xrightarrow{\sim}Me,\qquad f\longmapsto f(e),
\quad\text{with inverse}\quad m\longmapsto(ea\mapsto ma).
\]
\end{lemma}
\begin{proof}
We have $f(e)=f(e)e$ and $f(ea)=f(e)a$.
If $m=me$, the map $ea\mapsto ma$ is well-defined because $ea=ea'$ implies $ma=mea=mea'=ma'$.
These formulas prove that the maps are inverse; postcomposition by a module map $M\to N$ proves naturality.
\end{proof}

\begin{example}
For an $A$-bimodule $M$ and idempotents $e,f\in A$, the space $eMf:=\{enf\mid n\in M\}$ is an $(eAe,fAf)$-bimodule, with local identities $em=m=mf$ for $m\in eMf$.
\end{example}

```

</details>

---

## Replacement 5: Relocate the Confirmed Homework Solution to a Hidden Block

**Source:** [Lecture 1, line 616](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:616)  
**Added:** `+0` lines | **Removed:** `-21` lines

Confirmed against Homework1.tex: this is Exercise 1(3), not merely a similar example. Replacement 5 removes the solution from the main exposition; Replacement 16 retains it in a hidden solution immediately after the exercise statement. Apply both replacements together. The lecture source is unchanged pending approval.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -616,21 +641,0 @@
-\begin{example}\label{ex:infinite-hom}
-\comm{This is Homework exercise???  This is writing out solution of homework???? don't do this}
-Let $S=\Bbbk e_1\oplus\Bbbk e_2$ with componentwise multiplication, concentrated in degree $0$.
-Write
-\[
-M=\bigoplus_{i\geq0}(e_1S)(-i)=\bigoplus_{i\geq0}\Bbbk m_i,
-\qquad
-\deg m_i=i,\quad m_ie_1=m_i,\quad m_ie_2=0,
-\]
-and let $N=e_1S$ be concentrated in degree $0$.
-Define the $S$-linear map $f:M\to N$ by
-\[
-f\Bigl(\sum_{i\geq0}c_i m_i\Bigr)=\sum_{c_i\neq0}c_i e_1
-\quad\text{for finitely supported }(c_i)_{i\geq0}
-\]
-so that $f(m_i)=e_1\neq0$ for every $i\geq0$.
-On the summand $(e_1S)(-i)$, the restriction $f|_{(e_1S)(-i)}:(e_1S)(-i)\to e_1S$ is the underlying identity map, of degree $-i$.
-A homogeneous map $M\to N$ of degree $d$ vanishes on $m_i$ unless $d=-i$.
-Hence $f$ is not a finite sum of homogeneous maps.
-\end{example}
-
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:infinite-hom}
\comm{This is Homework exercise???  This is writing out solution of homework???? don't do this}
Let $S=\Bbbk e_1\oplus\Bbbk e_2$ with componentwise multiplication, concentrated in degree $0$.
Write
\[
M=\bigoplus_{i\geq0}(e_1S)(-i)=\bigoplus_{i\geq0}\Bbbk m_i,
\qquad
\deg m_i=i,\quad m_ie_1=m_i,\quad m_ie_2=0,
\]
and let $N=e_1S$ be concentrated in degree $0$.
Define the $S$-linear map $f:M\to N$ by
\[
f\Bigl(\sum_{i\geq0}c_i m_i\Bigr)=\sum_{c_i\neq0}c_i e_1
\quad\text{for finitely supported }(c_i)_{i\geq0}
\]
so that $f(m_i)=e_1\neq0$ for every $i\geq0$.
On the summand $(e_1S)(-i)$, the restriction $f|_{(e_1S)(-i)}:(e_1S)(-i)\to e_1S$ is the underlying identity map, of degree $-i$.
A homogeneous map $M\to N$ of degree $d$ vanishes on $m_i$ unless $d=-i$.
Hence $f$ is not a finite sum of homogeneous maps.
\end{example}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
```

</details>

---

## Replacement 6: Introduce the Left Graded Module Category at the Right Place

**Source:** [Lecture 1, line 665](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:665)  
**Added:** `+1` lines | **Removed:** `-0` lines

Move the notation removed in Replacement 4 to immediately after the definition of the graded module categories.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -665 +670,2 @@
+Thus $\Grmod(A^\op)$ is the category of graded left $A$-modules and degree-preserving maps.
 Forgetting the grading gives a functor $\Grmod A\to\Mod A$.
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
Forgetting the grading gives a functor $\Grmod A\to\Mod A$.
```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
Thus $\Grmod(A^\op)$ is the category of graded left $A$-modules and degree-preserving maps.
Forgetting the grading gives a functor $\Grmod A\to\Mod A$.
```

</details>

---

## Replacement 7: Use the Positive Degree Ideal Notation A+

**Source:** [Lecture 1, line 751](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:751)  
**Added:** `+6` lines | **Removed:** `-6` lines

Use $A_+$, already used in Lectures 4 and 5, and add stable references for the definition and projection. Audit completed: Lectures 2--5 contain no $A_{>0}$; all three existing occurrences are in Lecture 1, covered by this replacement. No immediate later-lecture edit was needed.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -751,11 +757,11 @@
-\begin{definition}
-The \defn{positive degree ideal} of a graded algebra $A$ is \comm{in later lecture, the notes use $A_+$, decide which one to use and keep it throughout.   always keep notation consistent.} $A_{>0}:=\bigoplus_{i>0}A_i$.\footnote{It is also called the augmentation ideal; we avoid that terminology.}
+\begin{definition}\label{def:positive-ideal}
+The \defn{positive degree ideal} of a graded algebra $A$ is $A_+:=\bigoplus_{i>0}A_i$.\footnote{It is also called the augmentation ideal; we avoid that terminology.}
 \end{definition}
 
-The subspace $A_{>0}$ is a homogeneous two-sided ideal. The quotient map
-\[
-\pi:A\longrightarrow A/A_{>0}\cong A_0,\qquad
+The subspace $A_+$ is a homogeneous two-sided ideal. The quotient map
+\begin{equation}\label{eq:degree-zero-projection}
+\pi:A\longrightarrow A/A_+\cong A_0,\qquad
 \sum_{i\in\Z}a_i\mapsto a_0,
-\]
+\end{equation}
 makes $A_0$ a graded $A$-bimodule concentrated in degree $0$, with $a\cdot s\cdot b=\pi(a)s\pi(b)$ for $a,b\in A$ and $s\in A_0$.
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{definition}
The \defn{positive degree ideal} of a graded algebra $A$ is \comm{in later lecture, the notes use $A_+$, decide which one to use and keep it throughout.   always keep notation consistent.} $A_{>0}:=\bigoplus_{i>0}A_i$.\footnote{It is also called the augmentation ideal; we avoid that terminology.}
\end{definition}

The subspace $A_{>0}$ is a homogeneous two-sided ideal. The quotient map
\[
\pi:A\longrightarrow A/A_{>0}\cong A_0,\qquad
\sum_{i\in\Z}a_i\mapsto a_0,
\]
makes $A_0$ a graded $A$-bimodule concentrated in degree $0$, with $a\cdot s\cdot b=\pi(a)s\pi(b)$ for $a,b\in A$ and $s\in A_0$.

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{definition}\label{def:positive-ideal}
The \defn{positive degree ideal} of a graded algebra $A$ is $A_+:=\bigoplus_{i>0}A_i$.\footnote{It is also called the augmentation ideal; we avoid that terminology.}
\end{definition}

The subspace $A_+$ is a homogeneous two-sided ideal. The quotient map
\begin{equation}\label{eq:degree-zero-projection}
\pi:A\longrightarrow A/A_+\cong A_0,\qquad
\sum_{i\in\Z}a_i\mapsto a_0,
\end{equation}
makes $A_0$ a graded $A$-bimodule concentrated in degree $0$, with $a\cdot s\cdot b=\pi(a)s\pi(b)$ for $a,b\in A$ and $s\in A_0$.

```

</details>

---

## Replacement 8: Construct Vector-Space Tensor Products from Bases

**Source:** [Lecture 1, line 764](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:764)  
**Added:** `+27` lines | **Removed:** `-18` lines

Start with the concrete basis construction, then state the universal property as a proposition. Its proof and the full uniqueness argument are supplementary. Arbitrary bases are allowed so that the later direct-sum identities remain valid.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -764,6 +770,18 @@
-\comm{i question if this is really a good definition for beginner.  especially when in the context of the course, the most important part is about tensor product algebra $T_S(V)$, but the generating space $V$ is f.d. by assumption since we work only with locally finite things, so we are always dealing with tensor product of f.d. v.sp, then the practical definition should be just pick a basis for the factors and define the tensor product, then show the universal property holds, and thus the uniqueness argument.  This is actually similar to the approach when you introduce tensor product over an algebra, so we should use this.   the proof of universal property, and the consequential uniquness, should be supplementary material.}
 \begin{definition}\label{def:vector-tensor}
-For vector spaces $U,V$, the \defn{tensor product} $U\otimes_\Bbbk V$ is equipped with a bilinear map $(u,v)\mapsto u\otimes v$ such that every bilinear map $b:U\times V\to W$ has a unique linear factorisation:
+Choose a basis $\{u_i\mid i\in I\}$ of $U$ and a basis $\{v_j\mid j\in J\}$ of $V$.
+The \defn{tensor product} $U\otimes_\Bbbk V$ is the vector space with basis $\{u_i\otimes v_j\mid i\in I,\ j\in J\}$, equipped with the bilinear map
+\[
+\Bigl(\sum_{i\in I}a_i u_i,\sum_{j\in J}b_j v_j\Bigr)
+\longmapsto\sum_{(i,j)\in I\times J}a_i b_j(u_i\otimes v_j)
+\quad\text{for finitely supported families }(a_i)_{i\in I},(b_j)_{j\in J}.
+\]
+We denote its value at $(u,v)$ by $u\otimes v$.
+\end{definition}
+
+% An element of the form $u\otimes v$ is called a \defn{pure tensor}.
+% \comm{do not introduce useless terminology!}
+\begin{proposition}[Universal property]\label{prop:vector-tensor-universal}
+Every bilinear map $b:U\times V\to W$ has a unique linear factorisation
 \[
 \xymatrix@C=60pt@R=22pt{
 U\times V \ar[r]^{(u,v)\mapsto u\otimes v} \ar[dr]_{b}
@@ -771,27 +789,24 @@
 & W.
 }
 \]
-\end{definition}
+Consequently, $U\otimes_\Bbbk V$ is independent of the chosen bases up to a unique isomorphism preserving the bilinear map.
+\end{proposition}
 
-% An element of the form $u\otimes v$ is called a \defn{pure tensor}.
-% \comm{do not introduce useless terminology!}
-Choose bases $(u_i)_{i\in I}$ of $U$ and $(v_j)_{j\in J}$ of $V$.
-Construct $U\otimes_\Bbbk V$ as the vector space with basis $\{u_i\otimes v_j\mid i\in I,\ j\in J\}$, and extend $(u_i,v_j)\mapsto u_i\otimes v_j$ bilinearly.
-For $b:U\times V\to W$ bilinear, the unique required map is
-\[
-\widetilde b:U\otimes_\Bbbk V\longrightarrow W,
-\qquad u_i\otimes v_j\longmapsto b(u_i,v_j).
-\]
-Let $T,T'$ be vector spaces with bilinear maps $t:U\times V\to T$ and $t':U\times V\to T'$ satisfying the universal property in Definition~\ref{def:vector-tensor}.
-The universal properties give unique linear maps $a:T\to T'$ and $b:T'\to T$ with $a\circ t=t'$ and $b\circ t'=t$.
-The universal property of $(T,t)$, applied to the bilinear map $t:U\times V\to T$, gives a unique linear map $h:T\to T$ with $h\circ t=t$.
-Both $b\circ a$ and $\id_T$ have this property, since
+\begin{supplementary}
+\begin{proof}
+The formula $\widetilde b(u_i\otimes v_j)=b(u_i,v_j)$ determines a unique linear map $\widetilde b:U\otimes_\Bbbk V\to W$.
+Bilinearity gives $\widetilde b(u\otimes v)=b(u,v)$ for all $u\in U$ and $v\in V$.
+
+Suppose $t:U\times V\to T$ and $t':U\times V\to T'$ both satisfy the universal property.
+They give unique linear maps $a:T\to T'$ and $b:T'\to T$ with $a\circ t=t'$ and $b\circ t'=t$.
+Both $b\circ a:T\to T$ and $\id_T:T\to T$ factor $t$ through itself, since
 \[
 (b\circ a)\circ t=b\circ t'=t=\id_T\circ t.
 \]
-Hence $b\circ a=\id_T$.
+Uniqueness for $(T,t)$ gives $b\circ a=\id_T$.
 Likewise, $(a\circ b)\circ t'=a\circ t=t'=\id_{T'}\circ t'$, so uniqueness for $(T',t')$ gives $a\circ b=\id_{T'}$.
-Thus the tensor product is independent of the chosen bases up to the unique isomorphism carrying $t(u,v)$ to $t'(u,v)$.
+\end{proof}
+\end{supplementary}
 
 For finite bases with $|I|=r$ and $|J|=s$, we obtain $\dim_\Bbbk(U\otimes_\Bbbk V)=rs$.
 We use the canonical identifications
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\comm{i question if this is really a good definition for beginner.  especially when in the context of the course, the most important part is about tensor product algebra $T_S(V)$, but the generating space $V$ is f.d. by assumption since we work only with locally finite things, so we are always dealing with tensor product of f.d. v.sp, then the practical definition should be just pick a basis for the factors and define the tensor product, then show the universal property holds, and thus the uniqueness argument.  This is actually similar to the approach when you introduce tensor product over an algebra, so we should use this.   the proof of universal property, and the consequential uniquness, should be supplementary material.}
\begin{definition}\label{def:vector-tensor}
For vector spaces $U,V$, the \defn{tensor product} $U\otimes_\Bbbk V$ is equipped with a bilinear map $(u,v)\mapsto u\otimes v$ such that every bilinear map $b:U\times V\to W$ has a unique linear factorisation:
\[
\xymatrix@C=60pt@R=22pt{
U\times V \ar[r]^{(u,v)\mapsto u\otimes v} \ar[dr]_{b}
& U\otimes_\Bbbk V \ar@{-->}[d]^{\exists!\,\widetilde b}\\
& W.
}
\]
\end{definition}

% An element of the form $u\otimes v$ is called a \defn{pure tensor}.
% \comm{do not introduce useless terminology!}
Choose bases $(u_i)_{i\in I}$ of $U$ and $(v_j)_{j\in J}$ of $V$.
Construct $U\otimes_\Bbbk V$ as the vector space with basis $\{u_i\otimes v_j\mid i\in I,\ j\in J\}$, and extend $(u_i,v_j)\mapsto u_i\otimes v_j$ bilinearly.
For $b:U\times V\to W$ bilinear, the unique required map is
\[
\widetilde b:U\otimes_\Bbbk V\longrightarrow W,
\qquad u_i\otimes v_j\longmapsto b(u_i,v_j).
\]
Let $T,T'$ be vector spaces with bilinear maps $t:U\times V\to T$ and $t':U\times V\to T'$ satisfying the universal property in Definition~\ref{def:vector-tensor}.
The universal properties give unique linear maps $a:T\to T'$ and $b:T'\to T$ with $a\circ t=t'$ and $b\circ t'=t$.
The universal property of $(T,t)$, applied to the bilinear map $t:U\times V\to T$, gives a unique linear map $h:T\to T$ with $h\circ t=t$.
Both $b\circ a$ and $\id_T$ have this property, since
\[
(b\circ a)\circ t=b\circ t'=t=\id_T\circ t.
\]
Hence $b\circ a=\id_T$.
Likewise, $(a\circ b)\circ t'=a\circ t=t'=\id_{T'}\circ t'$, so uniqueness for $(T',t')$ gives $a\circ b=\id_{T'}$.
Thus the tensor product is independent of the chosen bases up to the unique isomorphism carrying $t(u,v)$ to $t'(u,v)$.

For finite bases with $|I|=r$ and $|J|=s$, we obtain $\dim_\Bbbk(U\otimes_\Bbbk V)=rs$.
We use the canonical identifications
\[
\begin{aligned}
(U\otimes_\Bbbk V)\otimes_\Bbbk W&\xrightarrow{\sim}U\otimes_\Bbbk(V\otimes_\Bbbk W),
& (u\otimes v)\otimes w&\longmapsto u\otimes(v\otimes w),\\
\Bbbk\otimes_\Bbbk U&\xrightarrow{\sim}U,
& c\otimes u&\longmapsto cu,
\end{aligned}
\]
and set $U^{\otimes_\Bbbk 0}:=\Bbbk$.

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{definition}\label{def:vector-tensor}
Choose a basis $\{u_i\mid i\in I\}$ of $U$ and a basis $\{v_j\mid j\in J\}$ of $V$.
The \defn{tensor product} $U\otimes_\Bbbk V$ is the vector space with basis $\{u_i\otimes v_j\mid i\in I,\ j\in J\}$, equipped with the bilinear map
\[
\Bigl(\sum_{i\in I}a_i u_i,\sum_{j\in J}b_j v_j\Bigr)
\longmapsto\sum_{(i,j)\in I\times J}a_i b_j(u_i\otimes v_j)
\quad\text{for finitely supported families }(a_i)_{i\in I},(b_j)_{j\in J}.
\]
We denote its value at $(u,v)$ by $u\otimes v$.
\end{definition}

% An element of the form $u\otimes v$ is called a \defn{pure tensor}.
% \comm{do not introduce useless terminology!}
\begin{proposition}[Universal property]\label{prop:vector-tensor-universal}
Every bilinear map $b:U\times V\to W$ has a unique linear factorisation
\[
\xymatrix@C=60pt@R=22pt{
U\times V \ar[r]^{(u,v)\mapsto u\otimes v} \ar[dr]_{b}
& U\otimes_\Bbbk V \ar@{-->}[d]^{\exists!\,\widetilde b}\\
& W.
}
\]
Consequently, $U\otimes_\Bbbk V$ is independent of the chosen bases up to a unique isomorphism preserving the bilinear map.
\end{proposition}

\begin{supplementary}
\begin{proof}
The formula $\widetilde b(u_i\otimes v_j)=b(u_i,v_j)$ determines a unique linear map $\widetilde b:U\otimes_\Bbbk V\to W$.
Bilinearity gives $\widetilde b(u\otimes v)=b(u,v)$ for all $u\in U$ and $v\in V$.

Suppose $t:U\times V\to T$ and $t':U\times V\to T'$ both satisfy the universal property.
They give unique linear maps $a:T\to T'$ and $b:T'\to T$ with $a\circ t=t'$ and $b\circ t'=t$.
Both $b\circ a:T\to T$ and $\id_T:T\to T$ factor $t$ through itself, since
\[
(b\circ a)\circ t=b\circ t'=t=\id_T\circ t.
\]
Uniqueness for $(T,t)$ gives $b\circ a=\id_T$.
Likewise, $(a\circ b)\circ t'=a\circ t=t'=\id_{T'}\circ t'$, so uniqueness for $(T',t')$ gives $a\circ b=\id_{T'}$.
\end{proof}
\end{supplementary}

For finite bases with $|I|=r$ and $|J|=s$, we obtain $\dim_\Bbbk(U\otimes_\Bbbk V)=rs$.
We use the canonical identifications
\[
\begin{aligned}
(U\otimes_\Bbbk V)\otimes_\Bbbk W&\xrightarrow{\sim}U\otimes_\Bbbk(V\otimes_\Bbbk W),
& (u\otimes v)\otimes w&\longmapsto u\otimes(v\otimes w),\\
\Bbbk\otimes_\Bbbk U&\xrightarrow{\sim}U,
& c\otimes u&\longmapsto cu,
\end{aligned}
\]
and set $U^{\otimes_\Bbbk 0}:=\Bbbk$.

```

</details>

---

## Replacement 9: Make Indexing Explicit and Add Polynomial Examples

**Source:** [Lecture 1, line 810](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:810)  
**Added:** `+32` lines | **Removed:** `-16` lines

Allow arbitrary set-indexed families explicitly. Add formal power series as the direct-product counterpart of polynomials, distinguishing the vector-space product from ring multiplication. The displayed linear maps are induced by the specified bilinear maps. Keep the tensor/direct-product comparison lemma advanced.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -810,4 +825,4 @@
-For a family $(M_i)_{i\in I}$ of right $A$-modules, the \defn{direct product} and \defn{direct sum} are
+For an arbitrary family $(M_i)_{i\in I}$ of right $A$-modules, indexed by a set $I$, the \defn{direct product} and \defn{direct sum} are
 \[
 \begin{aligned}
 \prod_{i\in I}M_i&=\{(m_i)_{i\in I}\mid m_i\in M_i\text{ for all }i\in I\},\\
@@ -815,30 +830,46 @@
 \end{aligned}
 \]
 Addition and the $A$-action are componentwise; the same definitions apply to vector spaces by taking $A=\Bbbk$.
-Thus $\bigoplus_i M_i\subset\prod_i M_i$, with equality for finite $I$.
+Thus $\bigoplus_{i\in I} M_i\subset\prod_{i\in I} M_i$, with equality for finite $I$.
 For example, $(1,1,\ldots)\in\prod_{i\geq0}\Bbbk$ does not belong to $\bigoplus_{i\geq0}\Bbbk$.
 In a direct sum, an element is a finite sum of its components; no notion of convergence is involved.
-\comm{also reference about Laurent polynomial ring and ordinary polynomial ring}
+For instance, ordinary polynomials use non-negative powers, whereas Laurent polynomials allow integer powers, but both are finite sums:
+\[
+\Bbbk[x]=\bigoplus_{n\geq0}\Bbbk x^n,\qquad
+\Bbbk[x,x^{-1}]=\bigoplus_{n\in\Z}\Bbbk x^n.
+\]
+The \defn{formal power series ring} allows arbitrary coefficients:
+\[
+\Bbbk[[x]]=\left\{\sum_{n\geq0}a_nx^n\;\middle|\;a_n\in\Bbbk\text{ for every }n\geq0\right\}
+\cong\prod_{n\geq0}\Bbbk x^n
+\quad\text{as vector spaces}.
+\]
+Addition is coefficientwise, and multiplication is
+\[
+\Bigl(\sum_{n\geq0}a_nx^n\Bigr)\Bigl(\sum_{n\geq0}b_nx^n\Bigr)
+=\sum_{n\geq0}\Bigl(\sum_{j=0}^n a_jb_{n-j}\Bigr)x^n.
+\]
 
-Tensor products distribute over direct sums: for vector spaces $U_i$ ($i\in I$) \comm{add to math discussion rule, generally, I highly dislike this type of exposition -- bracket an indexing set straight after a notation, use approach that can be read aloud naturally; in casual math discussion, this is fine; but when writing any exposition note, lecture notes, paper, this is forbidden in my standard} and $V$, there is a canonical linear isomorphism
-\[
+
+Tensor products distribute over direct sums: for an arbitrary family $(U_i)_{i\in I}$ of vector spaces, indexed by a set $I$, and a vector space $V$, there is a canonical linear isomorphism
+\begin{equation}\label{eq:vector-tensor-sums}
 \Bigl(\bigoplus_{i\in I}U_i\Bigr)\otimes_\Bbbk V
 \xrightarrow{\sim}\bigoplus_{i\in I}(U_i\otimes_\Bbbk V),
 \qquad (u_i)_i\otimes v\longmapsto(u_i\otimes v)_i.
-\]
-\comm{always check bigoplus bigotimes this type of things has indexing writen properly (previous generated just take $i$, instead of $i\in I$ corrected here)}
-The map is defined by the universal property in Definition~\ref{def:vector-tensor}.
-If $\iota_i:U_i\to\bigoplus_jU_j$ is the inclusion, the inverse sends $u\otimes v$ in the summand corresponding to $i\in I$ to $\iota_i(u)\otimes v$.
+\end{equation}
+
+The bilinear map $\bigl(\bigoplus_{i\in I}U_i\bigr)\times V\to\bigoplus_{i\in I}(U_i\otimes_\Bbbk V)$, $((u_i)_i,v)\mapsto(u_i\otimes v)_i$, induces \eqref{eq:vector-tensor-sums} by Proposition~\ref{prop:vector-tensor-universal}.
+If $\iota_i:U_i\to\bigoplus_{j\in I}U_j$ is the inclusion, the inverse sends $u\otimes v$ in the summand corresponding to $i\in I$ to $\iota_i(u)\otimes v$.
 The same construction applies in the other tensor variable.
 
 \begin{advanced}
 For direct products, the corresponding map need not be an isomorphism.
 
 \begin{lemma}\label{lem:vector-tensor-products}
-For vector spaces $U_i$ ($i\in I$) and $V$, the coordinate projections define a linear map
+For an arbitrary family $(U_i)_{i\in I}$ of vector spaces, indexed by a set $I$, and a vector space $V$, the coordinate projections define a linear map
 \begin{equation}\label{eq:vector-tensor-products}
-\Bigl(\prod_iU_i\Bigr)\otimes_\Bbbk V
-\longrightarrow\prod_i(U_i\otimes_\Bbbk V),
+\Bigl(\prod_{i\in I}U_i\Bigr)\otimes_\Bbbk V
+\longrightarrow\prod_{i\in I}(U_i\otimes_\Bbbk V),
 \qquad (u_i)_i\otimes v\longmapsto(u_i\otimes v)_i.
 \end{equation}
 This map is injective, and is an isomorphism if $I$ is finite or $V$ is finite-dimensional.
@@ -846,14 +877,14 @@
 \end{lemma}
 
 \begin{proof}
-The map is defined by the universal property in Definition~\ref{def:vector-tensor}.
-Every tensor can be written $\sum_{\ell=1}^r u^{(\ell)}\otimes v_\ell$ with the $v_\ell$ linearly independent: choose a basis of the span of its finitely many second factors.
+The bilinear map $\bigl(\prod_{i\in I}U_i\bigr)\times V\to\prod_{i\in I}(U_i\otimes_\Bbbk V)$, $((u_i)_i,v)\mapsto(u_i\otimes v)_i$, induces \eqref{eq:vector-tensor-products} by Proposition~\ref{prop:vector-tensor-universal}.
+Every element can be written $\sum_{\ell=1}^r u^{(\ell)}\otimes v_\ell$ with the $v_\ell$ linearly independent: choose a basis of the span of its finitely many second factors.
 If its image is zero, then $\sum_{\ell=1}^r u_i^{(\ell)}\otimes v_\ell=0$ for every $i$.
 The tensor-product basis construction gives $u_i^{(\ell)}=0$ for all $i,\ell$, proving injectivity.
 If $v_1,\ldots,v_r$ is a basis of $V$, the inverse is
 \[
-\prod_i(U_i\otimes_\Bbbk V)\longrightarrow
-\Bigl(\prod_iU_i\Bigr)\otimes_\Bbbk V,\qquad
+\prod_{i\in I}(U_i\otimes_\Bbbk V)\longrightarrow
+\Bigl(\prod_{i\in I}U_i\Bigr)\otimes_\Bbbk V,\qquad
 \Bigl(\sum_{\ell=1}^r u_i^{(\ell)}\otimes v_\ell\Bigr)_i
 \longmapsto\sum_{\ell=1}^r(u_i^{(\ell)})_i\otimes v_\ell.
 \]
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
For a family $(M_i)_{i\in I}$ of right $A$-modules, the \defn{direct product} and \defn{direct sum} are
\[
\begin{aligned}
\prod_{i\in I}M_i&=\{(m_i)_{i\in I}\mid m_i\in M_i\text{ for all }i\in I\},\\
\bigoplus_{i\in I}M_i&=\{(m_i)_{i\in I}\in\prod_{i\in I}M_i\mid m_i=0\text{ for all but finitely many }i\}.
\end{aligned}
\]
Addition and the $A$-action are componentwise; the same definitions apply to vector spaces by taking $A=\Bbbk$.
Thus $\bigoplus_i M_i\subset\prod_i M_i$, with equality for finite $I$.
For example, $(1,1,\ldots)\in\prod_{i\geq0}\Bbbk$ does not belong to $\bigoplus_{i\geq0}\Bbbk$.
In a direct sum, an element is a finite sum of its components; no notion of convergence is involved.
\comm{also reference about Laurent polynomial ring and ordinary polynomial ring}

Tensor products distribute over direct sums: for vector spaces $U_i$ ($i\in I$) \comm{add to math discussion rule, generally, I highly dislike this type of exposition -- bracket an indexing set straight after a notation, use approach that can be read aloud naturally; in casual math discussion, this is fine; but when writing any exposition note, lecture notes, paper, this is forbidden in my standard} and $V$, there is a canonical linear isomorphism
\[
\Bigl(\bigoplus_{i\in I}U_i\Bigr)\otimes_\Bbbk V
\xrightarrow{\sim}\bigoplus_{i\in I}(U_i\otimes_\Bbbk V),
\qquad (u_i)_i\otimes v\longmapsto(u_i\otimes v)_i.
\]
\comm{always check bigoplus bigotimes this type of things has indexing writen properly (previous generated just take $i$, instead of $i\in I$ corrected here)}
The map is defined by the universal property in Definition~\ref{def:vector-tensor}.
If $\iota_i:U_i\to\bigoplus_jU_j$ is the inclusion, the inverse sends $u\otimes v$ in the summand corresponding to $i\in I$ to $\iota_i(u)\otimes v$.
The same construction applies in the other tensor variable.

\begin{advanced}
For direct products, the corresponding map need not be an isomorphism.

\begin{lemma}\label{lem:vector-tensor-products}
For vector spaces $U_i$ ($i\in I$) and $V$, the coordinate projections define a linear map
\begin{equation}\label{eq:vector-tensor-products}
\Bigl(\prod_iU_i\Bigr)\otimes_\Bbbk V
\longrightarrow\prod_i(U_i\otimes_\Bbbk V),
\qquad (u_i)_i\otimes v\longmapsto(u_i\otimes v)_i.
\end{equation}
This map is injective, and is an isomorphism if $I$ is finite or $V$ is finite-dimensional.
The same statements hold with the two tensor factors reversed.
\end{lemma}

\begin{proof}
The map is defined by the universal property in Definition~\ref{def:vector-tensor}.
Every tensor can be written $\sum_{\ell=1}^r u^{(\ell)}\otimes v_\ell$ with the $v_\ell$ linearly independent: choose a basis of the span of its finitely many second factors.
If its image is zero, then $\sum_{\ell=1}^r u_i^{(\ell)}\otimes v_\ell=0$ for every $i$.
The tensor-product basis construction gives $u_i^{(\ell)}=0$ for all $i,\ell$, proving injectivity.
If $v_1,\ldots,v_r$ is a basis of $V$, the inverse is
\[
\prod_i(U_i\otimes_\Bbbk V)\longrightarrow
\Bigl(\prod_iU_i\Bigr)\otimes_\Bbbk V,\qquad
\Bigl(\sum_{\ell=1}^r u_i^{(\ell)}\otimes v_\ell\Bigr)_i
\longmapsto\sum_{\ell=1}^r(u_i^{(\ell)})_i\otimes v_\ell.
\]
For finite $I$, products equal sums.
Reversing the tensor factors gives the other statements, since $U\otimes_\Bbbk V\to V\otimes_\Bbbk U$, $u\otimes v\mapsto v\otimes u$, is an isomorphism.
\end{proof}

\begin{example}\label{ex:tensor-product-product-failure}
The comparison in \eqref{eq:vector-tensor-products} need not be surjective when $V$ is infinite-dimensional.
Take $U_i=\Bbbk$ for $i\geq1$ and $V=\bigoplus_{j\geq1}\Bbbk v_j$.
Under $\Bbbk\otimes_\Bbbk V\cong V$, the image of the product comparison in \eqref{eq:vector-tensor-products} is
\[
\left\{(w_i)_i\in\prod_{i\geq1}V\;\middle|\;
\dim_\Bbbk\operatorname{span}_\Bbbk\{w_i\mid i\geq1\}<\infty\right\}.
\]
Indeed, the image of $\sum_{\ell=1}^r(c_i^{(\ell)})_i\otimes w_\ell$ has every entry in $\operatorname{span}_\Bbbk\{w_1,\ldots,w_r\}$.
Conversely, expand all entries in a basis of their common finite-dimensional span.
Since the $v_i$ are linearly independent, $(v_i)_i$ is not in the image.
\end{example}
\end{advanced}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
For an arbitrary family $(M_i)_{i\in I}$ of right $A$-modules, indexed by a set $I$, the \defn{direct product} and \defn{direct sum} are
\[
\begin{aligned}
\prod_{i\in I}M_i&=\{(m_i)_{i\in I}\mid m_i\in M_i\text{ for all }i\in I\},\\
\bigoplus_{i\in I}M_i&=\{(m_i)_{i\in I}\in\prod_{i\in I}M_i\mid m_i=0\text{ for all but finitely many }i\}.
\end{aligned}
\]
Addition and the $A$-action are componentwise; the same definitions apply to vector spaces by taking $A=\Bbbk$.
Thus $\bigoplus_{i\in I} M_i\subset\prod_{i\in I} M_i$, with equality for finite $I$.
For example, $(1,1,\ldots)\in\prod_{i\geq0}\Bbbk$ does not belong to $\bigoplus_{i\geq0}\Bbbk$.
In a direct sum, an element is a finite sum of its components; no notion of convergence is involved.
For instance, ordinary polynomials use non-negative powers, whereas Laurent polynomials allow integer powers, but both are finite sums:
\[
\Bbbk[x]=\bigoplus_{n\geq0}\Bbbk x^n,\qquad
\Bbbk[x,x^{-1}]=\bigoplus_{n\in\Z}\Bbbk x^n.
\]
The \defn{formal power series ring} allows arbitrary coefficients:
\[
\Bbbk[[x]]=\left\{\sum_{n\geq0}a_nx^n\;\middle|\;a_n\in\Bbbk\text{ for every }n\geq0\right\}
\cong\prod_{n\geq0}\Bbbk x^n
\quad\text{as vector spaces}.
\]
Addition is coefficientwise, and multiplication is
\[
\Bigl(\sum_{n\geq0}a_nx^n\Bigr)\Bigl(\sum_{n\geq0}b_nx^n\Bigr)
=\sum_{n\geq0}\Bigl(\sum_{j=0}^n a_jb_{n-j}\Bigr)x^n.
\]


Tensor products distribute over direct sums: for an arbitrary family $(U_i)_{i\in I}$ of vector spaces, indexed by a set $I$, and a vector space $V$, there is a canonical linear isomorphism
\begin{equation}\label{eq:vector-tensor-sums}
\Bigl(\bigoplus_{i\in I}U_i\Bigr)\otimes_\Bbbk V
\xrightarrow{\sim}\bigoplus_{i\in I}(U_i\otimes_\Bbbk V),
\qquad (u_i)_i\otimes v\longmapsto(u_i\otimes v)_i.
\end{equation}

The bilinear map $\bigl(\bigoplus_{i\in I}U_i\bigr)\times V\to\bigoplus_{i\in I}(U_i\otimes_\Bbbk V)$, $((u_i)_i,v)\mapsto(u_i\otimes v)_i$, induces \eqref{eq:vector-tensor-sums} by Proposition~\ref{prop:vector-tensor-universal}.
If $\iota_i:U_i\to\bigoplus_{j\in I}U_j$ is the inclusion, the inverse sends $u\otimes v$ in the summand corresponding to $i\in I$ to $\iota_i(u)\otimes v$.
The same construction applies in the other tensor variable.

\begin{advanced}
For direct products, the corresponding map need not be an isomorphism.

\begin{lemma}\label{lem:vector-tensor-products}
For an arbitrary family $(U_i)_{i\in I}$ of vector spaces, indexed by a set $I$, and a vector space $V$, the coordinate projections define a linear map
\begin{equation}\label{eq:vector-tensor-products}
\Bigl(\prod_{i\in I}U_i\Bigr)\otimes_\Bbbk V
\longrightarrow\prod_{i\in I}(U_i\otimes_\Bbbk V),
\qquad (u_i)_i\otimes v\longmapsto(u_i\otimes v)_i.
\end{equation}
This map is injective, and is an isomorphism if $I$ is finite or $V$ is finite-dimensional.
The same statements hold with the two tensor factors reversed.
\end{lemma}

\begin{proof}
The bilinear map $\bigl(\prod_{i\in I}U_i\bigr)\times V\to\prod_{i\in I}(U_i\otimes_\Bbbk V)$, $((u_i)_i,v)\mapsto(u_i\otimes v)_i$, induces \eqref{eq:vector-tensor-products} by Proposition~\ref{prop:vector-tensor-universal}.
Every element can be written $\sum_{\ell=1}^r u^{(\ell)}\otimes v_\ell$ with the $v_\ell$ linearly independent: choose a basis of the span of its finitely many second factors.
If its image is zero, then $\sum_{\ell=1}^r u_i^{(\ell)}\otimes v_\ell=0$ for every $i$.
The tensor-product basis construction gives $u_i^{(\ell)}=0$ for all $i,\ell$, proving injectivity.
If $v_1,\ldots,v_r$ is a basis of $V$, the inverse is
\[
\prod_{i\in I}(U_i\otimes_\Bbbk V)\longrightarrow
\Bigl(\prod_{i\in I}U_i\Bigr)\otimes_\Bbbk V,\qquad
\Bigl(\sum_{\ell=1}^r u_i^{(\ell)}\otimes v_\ell\Bigr)_i
\longmapsto\sum_{\ell=1}^r(u_i^{(\ell)})_i\otimes v_\ell.
\]
For finite $I$, products equal sums.
Reversing the tensor factors gives the other statements, since $U\otimes_\Bbbk V\to V\otimes_\Bbbk U$, $u\otimes v\mapsto v\otimes u$, is an isomorphism.
\end{proof}

\begin{example}\label{ex:tensor-product-product-failure}
The comparison in \eqref{eq:vector-tensor-products} need not be surjective when $V$ is infinite-dimensional.
Take $U_i=\Bbbk$ for $i\geq1$ and $V=\bigoplus_{j\geq1}\Bbbk v_j$.
Under $\Bbbk\otimes_\Bbbk V\cong V$, the image of the product comparison in \eqref{eq:vector-tensor-products} is
\[
\left\{(w_i)_i\in\prod_{i\geq1}V\;\middle|\;
\dim_\Bbbk\operatorname{span}_\Bbbk\{w_i\mid i\geq1\}<\infty\right\}.
\]
Indeed, the image of $\sum_{\ell=1}^r(c_i^{(\ell)})_i\otimes w_\ell$ has every entry in $\operatorname{span}_\Bbbk\{w_1,\ldots,w_r\}$.
Conversely, expand all entries in a basis of their common finite-dimensional span.
Since the $v_i$ are linearly independent, $(v_i)_i$ is not in the image.
\end{example}
\end{advanced}

```

</details>

---

## Replacement 10: Display Both Directions of Linear Duality and Their Precise Scope

**Source:** [Lecture 1, line 958](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:958)  
**Added:** `+70` lines | **Removed:** `-60` lines

Complete the Hom formula with the correct shift $+i$, display all four functors, separate exactness from biduality, and state what works for finite-dimensional algebras and locally finite graded algebras. Keep failures advanced. Preserve the row-module example and its commented-out lines.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -958,44 +989,37 @@
 \subsection{\texorpdfstring{Graded $\Bbbk$-linear duals}{Graded k-linear duals}}
 
-A linear functional on a graded vector space need not have a degree: it may be non-zero on infinitely many homogeneous components.
-To obtain a graded vector space, we retain only finite sums of homogeneous functionals.
+A linear functional on a graded vector space can be non-zero on infinitely many degrees.
+To obtain a graded space, retain only finite sums of homogeneous functionals.
 
 \begin{definition}\label{def:linear-duals}
-For a graded vector space $V=\bigoplus_{i\in\Z}V_i$, its \defn{graded $\Bbbk$-linear dual} is
-the graded vector space defined using the linear dual $D$ of Example~\ref{ex:linear-duality} by
+For a graded vector space $V=\bigoplus_{i\in\Z}V_i$, the \defn{graded $\Bbbk$-linear dual} is the graded vector space
 \[
-\bbD(V)=\bigoplus_{i\in \Z} \bbD(V)_i
-\qquad\text{with} = \bigoplus_{i\in \Z}\Hom_\Bbbk^\Z(.....)\comm{write in Hom notation}\qquad
-\bbD(V)_i=D(V_{-i}).
+\bbD(V)=\bigoplus_{i\in\Z}\bbD(V)_i
+=\bigoplus_{i\in\Z}\Hom_\Bbbk^\Z(V,\Bbbk(i)),
+\qquad \bbD(V)_i=D(V_{-i}).
 \]
+Here $\Bbbk$ is concentrated in degree $0$, and the summand $\Hom_\Bbbk^\Z(V,\Bbbk(i))$ is placed in degree $i$.
 \end{definition}
 
-\begin{advanced}
-For general infinite-dimensional $V$, we have $\bbD(V)\subset D(V)$, whereas restriction to the homogeneous components gives $D(V)\cong\prod_{i\in\Z}D(V_i)$.
-An arbitrary family of functionals on the $V_i$ defines a functional on $V$, since each vector has only finitely many non-zero components.
-These spaces coincide when $V$ is finite-dimensional.
-\end{advanced}
-
 Linear duality reverses the side of a module action.
-For a right $A$-module $M$ and a left $A$-module $N$, define
+For a right $A$-module $M$ and a left $A$-module $N$, set
 \begin{equation}\label{eq:linear-dual-actions}
-(a f)(m):=f(ma),\qquad (g a)(n):=g(an)
-\quad(a\in A,\ f\in D(M),\ g\in D(N)).
+(af)(m)=f(ma),\qquad (ga)(n)=g(an)
+\quad\text{for }a\in A,\ f\in D(M),\ g\in D(N),\ m\in M,\ n\in N.
 \end{equation}
-Here $m\in M$ and $n\in N$; the first formula makes $D(M)$ a left module and the second makes $D(N)$ a right module.
-For graded modules, the same formulas preserve the graded $\Bbbk$-linear dual: if $a\in A_p$ and $f\in\bbD(M)_q$, then $af$ vanishes outside $M_{-p-q}$ and hence has degree $p+q$.
-
-For a module homomorphism $u:M\to N$, precomposition defines $D(u):D(N)\to D(M)$ by $D(u)(f)=f\circ u$.
-If $u$ preserves degrees, this restricts to $\bbD(u):\bbD(N)\to\bbD(M)$, also of degree $0$.
-Thus we obtain functors
+For graded modules these actions restrict to the graded linear duals: if $a\in A_p$ and $f\in\bbD(M)_q$, then $af$ vanishes outside $M_{-p-q}$.
+Precomposition, $f\mapsto f\circ u$ for a module map $u:M\to N$, gives four exact functors:
 \begin{equation}\label{eq:linear-dual-functors}
-D:(\Mod A)^\op\longrightarrow\Mod(A^\op),
-\qquad
-\bbD:(\Grmod A)^\op\longrightarrow\Grmod(A^\op).
+\begin{aligned}
+D:(\Mod A)^\op&\longrightarrow\Mod(A^\op),
+&D:(\Mod(A^\op))^\op&\longrightarrow\Mod A,\\
+\bbD:(\Grmod A)^\op&\longrightarrow\Grmod(A^\op),
+&\bbD:(\Grmod(A^\op))^\op&\longrightarrow\Grmod A.
+\end{aligned}
 \end{equation}
-Indeed, $D(\id_M)=\id_{D(M)}$ and $D(v\circ u)=D(u)\circ D(v)$ for composable $u,v$, and the same identities hold for $\bbD$.
-Replacing $A$ by $A^\op$ gives the corresponding functors from left modules to right modules.
-\comm{Perhaps it makes sense to stress that this duality is one reason why we like to work with algebra over a field? What do you think (tell me before doing any edit)}
+No finiteness assumption is needed for these functors or their exactness.
+Exactness follows from Example~\ref{ex:linear-duality}, degree by degree for $\bbD$.
+Thus working over a field supplies exact dual functors; recovering a module from its bidual requires the finiteness conditions below.
 
 \begin{example}\label{ex:row-linear-dual}
 Let $A=\Bbbk A_3$ and $P_1=e_{11}A$ as in Example~\ref{ex:shifted-row}.
@@ -1012,43 +1036,60 @@
 \end{example}
 
 \begin{lemma}\label{lem:linear-bidual}
-The functor $\bbD$ in \eqref{eq:linear-dual-functors} restricts to a duality $(\grmod A)^\op\to\grmod(A^\op)$.
-The coevaluation map and its inverse are natural isomorphisms
+The functors $D$ give inverse dualities between finite-dimensional right and left $A$-modules.
+The functors $\bbD$ give inverse dualities between locally finite graded right and left $A$-modules:
+\[
+\bbD:(\grmod A)^\op\xrightarrow{\sim}\grmod(A^\op),\qquad
+\bbD:(\grmod(A^\op))^\op\xrightarrow{\sim}\grmod A.
+\]
+For locally finite $M$, evaluation is a natural graded module isomorphism
 \begin{equation}\label{eq:linear-bidual-evaluation}
-\begin{aligned}
-\mathrm{coev}_M:M&\xrightarrow{\sim}\bbD(\bbD(M)),
-&m&\longmapsto(f\mapsto f(m)),\\
-\mathrm{ev}_M:=\mathrm{coev}_M^{-1}:\bbD(\bbD(M))&\xrightarrow{\sim}M
-&& (M\in\grmod A).
-\end{aligned}
+\mathrm{ev}_M:M\xrightarrow{\sim}\bbD(\bbD(M)),\qquad
+m\longmapsto(f\mapsto f(m)).
 \end{equation}
-\comm{as commented earlier, should not define evaluation as inverse of coev...}
-Thus $\mathrm{ev}_M(\Phi)$ is the unique $m\in M$ such that $\Phi(f)=f(m)$ for every $f\in\bbD(M)$.
-Moreover, $\bbD$ takes every short exact sequence $0\to L\to M\to N\to0$ to a short exact sequence $0\to\bbD(N)\to\bbD(M)\to\bbD(L)\to0$.
 \end{lemma}
 
 \begin{proof}
-The map $\mathrm{coev}_M$ in \eqref{eq:linear-bidual-evaluation} is an isomorphism in each degree by Example~\ref{ex:linear-duality}, and \eqref{eq:linear-dual-actions} makes it $A$-linear.
-For $u:M\to N$ of degree $0$, $m\in M$, and $f\in\bbD(N)$,
-\[
-\bigl(\bbD(\bbD(u))(\mathrm{coev}_M(m))\bigr)(f)
-=\mathrm{coev}_M(m)(f\circ u)=f(u(m))
-=\mathrm{coev}_N(u(m))(f).
-\]
-Hence $\bbD(\bbD(u))\circ\mathrm{coev}_M=\mathrm{coev}_N\circ u$, which is naturality as in \eqref{eq:naturality-square}.
-Taking inverses of the coevaluation maps gives $\mathrm{ev}_N\circ\bbD(\bbD(u))=u\circ\mathrm{ev}_M$.
-Replacing $A$ by $A^\op$ gives the other natural isomorphism required for a duality.
-For a short exact sequence $0\to L\xrightarrow{i}M\xrightarrow{p}N\to0$ in $\Grmod A$, apply the exactness of $D$ from Example~\ref{ex:linear-duality} in each degree.
-The resulting sequences are
-\[
-0\longrightarrow D(N_{-d})\xrightarrow{D(p|_{M_{-d}})}D(M_{-d})
-\xrightarrow{D(i|_{L_{-d}})}D(L_{-d})\longrightarrow0
-\quad(d\in\Z).
-\]
-By Remark~\ref{rem:graded-exactness}, these give the short exact sequence $0\to\bbD(N)\xrightarrow{\bbD(p)}\bbD(M)\xrightarrow{\bbD(i)}\bbD(L)\to0$.
+Evaluation is a vector space isomorphism by \eqref{eq:vector-bidual-evaluation}, degree by degree in the graded case.
+For a right module, $\mathrm{ev}_M(ma)(f)=f(ma)=\mathrm{ev}_M(m)(af)$, proving $A$-linearity.
+Naturality follows from \eqref{eq:vector-bidual-evaluation}; applying the same argument to $A^\op$ gives the other bidual isomorphism.
 \end{proof}
 
-The same argument without grading gives a duality between finite-dimensional right and left $A$-modules.  \comm{genuine wonder if these are really ok (ungraded module $\Bbbk$-linear duality for ungraded algebras) for finitely generated modules over possibly infinite-dimensional algebra (at least `finitely generated' algebra?)  what is the assumption needed on the algebra for this to work; note that current convention for $\mod A$ is f.g. mod, not f.d. mod.  correct this paragraph, plus answer my question if possible.   for lecture notes, just note that f.d. algebra is fine and maybe more general things like quotients of polynomial ring, but rigour assumption needed should be put in advanced material}
-If $A$ is finite-dimensional, these are precisely the finitely generated modules, so $D:(\mod A)^\op\to\mod(A^\op)$ is a duality.
-Without finite dimensionality for $D$, or local finiteness for $\bbD$, coevaluation need not be surjective, so its inverse $\mathrm{ev}$ need not exist. \comm{again, evaluation map should be naturally existing, whether they are inverse to coevaluation is another matter.  rephrase what you want to say.}
+\begin{corollary}[Finiteness and duality]\label{cor:dual-finiteness}
+\begin{enumerate}
+\item If $A$ is finite-dimensional, its finitely generated modules are finite-dimensional, and
+\[
+D:(\mod A)^\op\xrightarrow{\sim}\mod(A^\op)
+\]
+is a duality.
+\item If $A$ is locally finite, every finitely generated graded $A$-module $M$ is locally finite. Thus
+\[
+M\xrightarrow[\mathrm{ev}_M]{\sim}\bbD(\bbD(M)),
+\]
+and $\bbD(M)$ is locally finite, though it need not be finitely generated.
+\end{enumerate}
+\end{corollary}
+\begin{proof}
+For (1), apply Example~\ref{ex:module-categories} and Lemma~\ref{lem:linear-bidual}.
+For (2), a finite homogeneous generating set gives a surjection from a finite direct sum of shifts of $A$ to $M$; hence every $M_i$ is finite-dimensional. Apply Lemma~\ref{lem:linear-bidual}.
+\end{proof}
+Part (2) applies to polynomial rings with their usual grading and to their homogeneous quotients.
 
+\begin{advanced}
+For a locally finite graded vector space $V$, restriction gives
+\[
+\bbD(V)=\bigoplus_{i\in\Z}D(V_{-i})\subset
+D(V)\cong\prod_{i\in\Z}D(V_i).
+\]
+The inclusion is equality exactly when only finitely many $V_i$ are non-zero.
+For an arbitrary vector space, evaluation $V\to D(D(V))$ is injective but need not be surjective; hence the functors in \eqref{eq:linear-dual-functors} are not dualities on all modules.
+
+\begin{example}
+Graded linear duality need not preserve finite generation, even for a polynomial ring.
+Let $A=\Bbbk[x]$ with $\deg x=1$ and let $\varepsilon_n(x^m)=\delta_{nm}$ for $n,m\geq0$.
+Then $\deg\varepsilon_n=-n$, $x\varepsilon_0=0$, and $x\varepsilon_n=\varepsilon_{n-1}$ for $n\geq1$.
+Any finite set of elements of $\bbD(A)$ lies in the span of $\varepsilon_0,\ldots,\varepsilon_N$ for some $N$, and multiplication by $x$ preserves that span.
+Thus $\bbD(A)$ is locally finite but not finitely generated.
+\end{example}
+\end{advanced}
+
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\subsection{\texorpdfstring{Graded $\Bbbk$-linear duals}{Graded k-linear duals}}

A linear functional on a graded vector space need not have a degree: it may be non-zero on infinitely many homogeneous components.
To obtain a graded vector space, we retain only finite sums of homogeneous functionals.

\begin{definition}\label{def:linear-duals}
For a graded vector space $V=\bigoplus_{i\in\Z}V_i$, its \defn{graded $\Bbbk$-linear dual} is
the graded vector space defined using the linear dual $D$ of Example~\ref{ex:linear-duality} by
\[
\bbD(V)=\bigoplus_{i\in \Z} \bbD(V)_i
\qquad\text{with} = \bigoplus_{i\in \Z}\Hom_\Bbbk^\Z(.....)\comm{write in Hom notation}\qquad
\bbD(V)_i=D(V_{-i}).
\]
\end{definition}

\begin{advanced}
For general infinite-dimensional $V$, we have $\bbD(V)\subset D(V)$, whereas restriction to the homogeneous components gives $D(V)\cong\prod_{i\in\Z}D(V_i)$.
An arbitrary family of functionals on the $V_i$ defines a functional on $V$, since each vector has only finitely many non-zero components.
These spaces coincide when $V$ is finite-dimensional.
\end{advanced}

Linear duality reverses the side of a module action.
For a right $A$-module $M$ and a left $A$-module $N$, define
\begin{equation}\label{eq:linear-dual-actions}
(a f)(m):=f(ma),\qquad (g a)(n):=g(an)
\quad(a\in A,\ f\in D(M),\ g\in D(N)).
\end{equation}
Here $m\in M$ and $n\in N$; the first formula makes $D(M)$ a left module and the second makes $D(N)$ a right module.
For graded modules, the same formulas preserve the graded $\Bbbk$-linear dual: if $a\in A_p$ and $f\in\bbD(M)_q$, then $af$ vanishes outside $M_{-p-q}$ and hence has degree $p+q$.

For a module homomorphism $u:M\to N$, precomposition defines $D(u):D(N)\to D(M)$ by $D(u)(f)=f\circ u$.
If $u$ preserves degrees, this restricts to $\bbD(u):\bbD(N)\to\bbD(M)$, also of degree $0$.
Thus we obtain functors
\begin{equation}\label{eq:linear-dual-functors}
D:(\Mod A)^\op\longrightarrow\Mod(A^\op),
\qquad
\bbD:(\Grmod A)^\op\longrightarrow\Grmod(A^\op).
\end{equation}
Indeed, $D(\id_M)=\id_{D(M)}$ and $D(v\circ u)=D(u)\circ D(v)$ for composable $u,v$, and the same identities hold for $\bbD$.
Replacing $A$ by $A^\op$ gives the corresponding functors from left modules to right modules.
\comm{Perhaps it makes sense to stress that this duality is one reason why we like to work with algebra over a field? What do you think (tell me before doing any edit)}

\begin{example}\label{ex:row-linear-dual}
Let $A=\Bbbk A_3$ and $P_1=e_{11}A$ as in Example~\ref{ex:shifted-row}.
The functionals $\varepsilon_{1j}(e_{1\ell})=\delta_{j\ell}$ for $1\leq j,\ell\leq 3$ form a basis of $\bbD(P_1)$, with
\[
\deg\varepsilon_{1j}=1-j,\qquad
e_{12}\varepsilon_{12}=\varepsilon_{11},\qquad
e_{23}\varepsilon_{13}=\varepsilon_{12},\qquad
e_{jj}\varepsilon_{1j}=\varepsilon_{1j}.
\]
The actions follow from \eqref{eq:linear-dual-actions}.
%For comparison with an infinite-dimensional space, take $V=\bigoplus_{i\geq 0}\Bbbk v_i$ with $\deg v_i=i$.
%The functional $\lambda(v_i)=1$ for every $i$ belongs to $D(V)$ but not to $\bbD(V)$.
\end{example}

\begin{lemma}\label{lem:linear-bidual}
The functor $\bbD$ in \eqref{eq:linear-dual-functors} restricts to a duality $(\grmod A)^\op\to\grmod(A^\op)$.
The coevaluation map and its inverse are natural isomorphisms
\begin{equation}\label{eq:linear-bidual-evaluation}
\begin{aligned}
\mathrm{coev}_M:M&\xrightarrow{\sim}\bbD(\bbD(M)),
&m&\longmapsto(f\mapsto f(m)),\\
\mathrm{ev}_M:=\mathrm{coev}_M^{-1}:\bbD(\bbD(M))&\xrightarrow{\sim}M
&& (M\in\grmod A).
\end{aligned}
\end{equation}
\comm{as commented earlier, should not define evaluation as inverse of coev...}
Thus $\mathrm{ev}_M(\Phi)$ is the unique $m\in M$ such that $\Phi(f)=f(m)$ for every $f\in\bbD(M)$.
Moreover, $\bbD$ takes every short exact sequence $0\to L\to M\to N\to0$ to a short exact sequence $0\to\bbD(N)\to\bbD(M)\to\bbD(L)\to0$.
\end{lemma}

\begin{proof}
The map $\mathrm{coev}_M$ in \eqref{eq:linear-bidual-evaluation} is an isomorphism in each degree by Example~\ref{ex:linear-duality}, and \eqref{eq:linear-dual-actions} makes it $A$-linear.
For $u:M\to N$ of degree $0$, $m\in M$, and $f\in\bbD(N)$,
\[
\bigl(\bbD(\bbD(u))(\mathrm{coev}_M(m))\bigr)(f)
=\mathrm{coev}_M(m)(f\circ u)=f(u(m))
=\mathrm{coev}_N(u(m))(f).
\]
Hence $\bbD(\bbD(u))\circ\mathrm{coev}_M=\mathrm{coev}_N\circ u$, which is naturality as in \eqref{eq:naturality-square}.
Taking inverses of the coevaluation maps gives $\mathrm{ev}_N\circ\bbD(\bbD(u))=u\circ\mathrm{ev}_M$.
Replacing $A$ by $A^\op$ gives the other natural isomorphism required for a duality.
For a short exact sequence $0\to L\xrightarrow{i}M\xrightarrow{p}N\to0$ in $\Grmod A$, apply the exactness of $D$ from Example~\ref{ex:linear-duality} in each degree.
The resulting sequences are
\[
0\longrightarrow D(N_{-d})\xrightarrow{D(p|_{M_{-d}})}D(M_{-d})
\xrightarrow{D(i|_{L_{-d}})}D(L_{-d})\longrightarrow0
\quad(d\in\Z).
\]
By Remark~\ref{rem:graded-exactness}, these give the short exact sequence $0\to\bbD(N)\xrightarrow{\bbD(p)}\bbD(M)\xrightarrow{\bbD(i)}\bbD(L)\to0$.
\end{proof}

The same argument without grading gives a duality between finite-dimensional right and left $A$-modules.  \comm{genuine wonder if these are really ok (ungraded module $\Bbbk$-linear duality for ungraded algebras) for finitely generated modules over possibly infinite-dimensional algebra (at least `finitely generated' algebra?)  what is the assumption needed on the algebra for this to work; note that current convention for $\mod A$ is f.g. mod, not f.d. mod.  correct this paragraph, plus answer my question if possible.   for lecture notes, just note that f.d. algebra is fine and maybe more general things like quotients of polynomial ring, but rigour assumption needed should be put in advanced material}
If $A$ is finite-dimensional, these are precisely the finitely generated modules, so $D:(\mod A)^\op\to\mod(A^\op)$ is a duality.
Without finite dimensionality for $D$, or local finiteness for $\bbD$, coevaluation need not be surjective, so its inverse $\mathrm{ev}$ need not exist. \comm{again, evaluation map should be naturally existing, whether they are inverse to coevaluation is another matter.  rephrase what you want to say.}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\subsection{\texorpdfstring{Graded $\Bbbk$-linear duals}{Graded k-linear duals}}

A linear functional on a graded vector space can be non-zero on infinitely many degrees.
To obtain a graded space, retain only finite sums of homogeneous functionals.

\begin{definition}\label{def:linear-duals}
For a graded vector space $V=\bigoplus_{i\in\Z}V_i$, the \defn{graded $\Bbbk$-linear dual} is the graded vector space
\[
\bbD(V)=\bigoplus_{i\in\Z}\bbD(V)_i
=\bigoplus_{i\in\Z}\Hom_\Bbbk^\Z(V,\Bbbk(i)),
\qquad \bbD(V)_i=D(V_{-i}).
\]
Here $\Bbbk$ is concentrated in degree $0$, and the summand $\Hom_\Bbbk^\Z(V,\Bbbk(i))$ is placed in degree $i$.
\end{definition}

Linear duality reverses the side of a module action.
For a right $A$-module $M$ and a left $A$-module $N$, set
\begin{equation}\label{eq:linear-dual-actions}
(af)(m)=f(ma),\qquad (ga)(n)=g(an)
\quad\text{for }a\in A,\ f\in D(M),\ g\in D(N),\ m\in M,\ n\in N.
\end{equation}
For graded modules these actions restrict to the graded linear duals: if $a\in A_p$ and $f\in\bbD(M)_q$, then $af$ vanishes outside $M_{-p-q}$.
Precomposition, $f\mapsto f\circ u$ for a module map $u:M\to N$, gives four exact functors:
\begin{equation}\label{eq:linear-dual-functors}
\begin{aligned}
D:(\Mod A)^\op&\longrightarrow\Mod(A^\op),
&D:(\Mod(A^\op))^\op&\longrightarrow\Mod A,\\
\bbD:(\Grmod A)^\op&\longrightarrow\Grmod(A^\op),
&\bbD:(\Grmod(A^\op))^\op&\longrightarrow\Grmod A.
\end{aligned}
\end{equation}
No finiteness assumption is needed for these functors or their exactness.
Exactness follows from Example~\ref{ex:linear-duality}, degree by degree for $\bbD$.
Thus working over a field supplies exact dual functors; recovering a module from its bidual requires the finiteness conditions below.

\begin{example}\label{ex:row-linear-dual}
Let $A=\Bbbk A_3$ and $P_1=e_{11}A$ as in Example~\ref{ex:shifted-row}.
The functionals $\varepsilon_{1j}(e_{1\ell})=\delta_{j\ell}$ for $1\leq j,\ell\leq 3$ form a basis of $\bbD(P_1)$, with
\[
\deg\varepsilon_{1j}=1-j,\qquad
e_{12}\varepsilon_{12}=\varepsilon_{11},\qquad
e_{23}\varepsilon_{13}=\varepsilon_{12},\qquad
e_{jj}\varepsilon_{1j}=\varepsilon_{1j}.
\]
The actions follow from \eqref{eq:linear-dual-actions}.
%For comparison with an infinite-dimensional space, take $V=\bigoplus_{i\geq 0}\Bbbk v_i$ with $\deg v_i=i$.
%The functional $\lambda(v_i)=1$ for every $i$ belongs to $D(V)$ but not to $\bbD(V)$.
\end{example}

\begin{lemma}\label{lem:linear-bidual}
The functors $D$ give inverse dualities between finite-dimensional right and left $A$-modules.
The functors $\bbD$ give inverse dualities between locally finite graded right and left $A$-modules:
\[
\bbD:(\grmod A)^\op\xrightarrow{\sim}\grmod(A^\op),\qquad
\bbD:(\grmod(A^\op))^\op\xrightarrow{\sim}\grmod A.
\]
For locally finite $M$, evaluation is a natural graded module isomorphism
\begin{equation}\label{eq:linear-bidual-evaluation}
\mathrm{ev}_M:M\xrightarrow{\sim}\bbD(\bbD(M)),\qquad
m\longmapsto(f\mapsto f(m)).
\end{equation}
\end{lemma}

\begin{proof}
Evaluation is a vector space isomorphism by \eqref{eq:vector-bidual-evaluation}, degree by degree in the graded case.
For a right module, $\mathrm{ev}_M(ma)(f)=f(ma)=\mathrm{ev}_M(m)(af)$, proving $A$-linearity.
Naturality follows from \eqref{eq:vector-bidual-evaluation}; applying the same argument to $A^\op$ gives the other bidual isomorphism.
\end{proof}

\begin{corollary}[Finiteness and duality]\label{cor:dual-finiteness}
\begin{enumerate}
\item If $A$ is finite-dimensional, its finitely generated modules are finite-dimensional, and
\[
D:(\mod A)^\op\xrightarrow{\sim}\mod(A^\op)
\]
is a duality.
\item If $A$ is locally finite, every finitely generated graded $A$-module $M$ is locally finite. Thus
\[
M\xrightarrow[\mathrm{ev}_M]{\sim}\bbD(\bbD(M)),
\]
and $\bbD(M)$ is locally finite, though it need not be finitely generated.
\end{enumerate}
\end{corollary}
\begin{proof}
For (1), apply Example~\ref{ex:module-categories} and Lemma~\ref{lem:linear-bidual}.
For (2), a finite homogeneous generating set gives a surjection from a finite direct sum of shifts of $A$ to $M$; hence every $M_i$ is finite-dimensional. Apply Lemma~\ref{lem:linear-bidual}.
\end{proof}
Part (2) applies to polynomial rings with their usual grading and to their homogeneous quotients.

\begin{advanced}
For a locally finite graded vector space $V$, restriction gives
\[
\bbD(V)=\bigoplus_{i\in\Z}D(V_{-i})\subset
D(V)\cong\prod_{i\in\Z}D(V_i).
\]
The inclusion is equality exactly when only finitely many $V_i$ are non-zero.
For an arbitrary vector space, evaluation $V\to D(D(V))$ is injective but need not be surjective; hence the functors in \eqref{eq:linear-dual-functors} are not dualities on all modules.

\begin{example}
Graded linear duality need not preserve finite generation, even for a polynomial ring.
Let $A=\Bbbk[x]$ with $\deg x=1$ and let $\varepsilon_n(x^m)=\delta_{nm}$ for $n,m\geq0$.
Then $\deg\varepsilon_n=-n$, $x\varepsilon_0=0$, and $x\varepsilon_n=\varepsilon_{n-1}$ for $n\geq1$.
Any finite set of elements of $\bbD(A)$ lies in the span of $\varepsilon_0,\ldots,\varepsilon_N$ for some $N$, and multiplication by $x$ preserves that span.
Thus $\bbD(A)$ is locally finite but not finitely generated.
\end{example}
\end{advanced}

```

</details>

---

## Replacement 11: Keep S-Module and Bimodule Duals as the Basic S-Dual Constructions

**Source:** [Lecture 1, line 1055](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1055)  
**Added:** `+33` lines | **Removed:** `-39` lines

Follow the refined organisation from our discussion: canonical linear duals handle $A$-modules; one-sided $S$-duals handle generators and relations. Make their bimodule actions part of the main text because Lecture 2 uses them. Keep enveloping-algebra duals advanced, correct evaluation terminology, and remove the repeated graded formula. Transported $A$-actions are treated separately in Replacement 15.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1055,12 +1096,10 @@
 \subsection{\texorpdfstring{Left, right, and two-sided duals over $S$}{Left, right, and two-sided duals over S}}
 
-\comm{
-This section has hugely deviated from my intention.  My desired result is (graded) $A$-module duality under taking $S$-dual, not $S$-module duality under $S$-dual, which is stupid.  Results for $S$-module are just special case when $A=S$ (that does not even worth mentioning as example until its actual application).
-}
 
 Fix a finite-dimensional semisimple $\Bbbk$-algebra $S$, which is regarded as concentrated in degree $0$ when treated as a graded algebra.
-Besides the $\Bbbk$-linear dual, we will also work with duals defined by left $S$-linear maps and right $S$-linear maps.
-We first define these duals without grading, then apply the constructions in each degree.
+For a graded algebra $A$ with $A_0=S$, every $A_i$ is an $S$-bimodule.
+To dualise these components while retaining both actions, we distinguish maps to $S$ that are right or left $S$-linear.
+For duality of arbitrary $A$-modules we already have the canonical functors in \eqref{eq:linear-dual-functors}.
 %Their tensor and biduality isomorphisms in Proposition~\ref{prop:tensor-duals} and Lemma~\ref{lem:S-bidual} therefore construct quadratic duality without a choice of form; replacing them throughout by $D$ requires an identification $S\cong D(S)$.
 %\comm{what is said here is not understandable to beginner; you should not mention `quadratic dual' when nobody knows what it is yet}
 
@@ -1083,7 +1122,7 @@
 N\in\Mod(S^\op)\ \Longrightarrow\ {}^*N\in\Mod S.
 \]
 The same implications hold with $\Mod$ replaced by $\mod$, since $S$ is finite-dimensional.
-\comm{$A$-module??????}
+
 %The position of the star records the side of the original action: $f(ms)=f(m)s$ in $M^*$, whereas $g(sn)=sg(n)$ in $ {}^*N$.
 %\comm{why repeat what is already written????}
 
@@ -1104,8 +1143,9 @@
 =\bigoplus_{i\in\Z}\Hom_S^{\Z}(M,S(i)),\qquad
 {}^{\grstar}M:=\bigoplus_{i\in\Z}{}^*(M_{-i})=\bigoplus_{i\in\Z}\Hom_{S^\op}^{\Z}(M,S(i)),
 \]
-\comm{check correct $i$ indexing in Hom notation.  $i$ or $-i$ next to $S$?}
+
 where each indicated summand has degree $i$.
+The shift is $S(i)$, since $S(i)_{-i}=S_0$.
 \end{definition}
 
 For a degree $0$ right $S$-module map $u:M\to N$, define $u^{\grstar}:N^{\grstar}\to M^{\grstar}$ by
@@ -1122,7 +1162,7 @@
 {}^{\grstar}(-)&:(\Grmod(S^\op))^\op\longrightarrow\Grmod S.
 \end{aligned}
 \end{equation}
-\comm{$A$-module??????????????}
+
 Each functor in \eqref{eq:graded-S-dual-functors} restricts to locally finite modules: replace $\Grmod$ by $\grmod$ in its source and target.
 Indeed, for $R=S$ or $S^\op$ and $M\in\grmod R$,
 \begin{equation}\label{eq:graded-S-dual-finiteness}
@@ -1131,14 +1171,10 @@
 \quad(i\in\Z).
 \end{equation}
 
-Parentheses on the stars distinguish the graded constructions from the full $S$-duals. In the notation \eqref{eq:graded-hom},
-\[
-M^{\grstar}=\bigoplus_{i\in\Z}\Hom_S^{\Z}(M,S(i)),\qquad
-{}^{\grstar}M=\bigoplus_{i\in\Z}\Hom_{S^\op}^{\Z}(M,S(i)).
-\]
+Parentheses on the stars distinguish the graded constructions from the full $S$-duals.
 
 \begin{lemma}\label{lem:S-bidual}
-Coevaluation gives natural isomorphisms of functors
+Evaluation gives natural isomorphisms of functors
 \[
 \id_{\mod S}\xrightarrow{\sim}{}^*((-)^*),
 \qquad
@@ -1147,10 +1183,10 @@
 with components
 \[
 \begin{aligned}
-\mathrm{coev}_M:M&\xrightarrow{\sim}{}^*(M^*),
+\mathrm{ev}_M:M&\xrightarrow{\sim}{}^*(M^*),
 & m&\longmapsto(f\mapsto f(m))
 && (M\in\mod S),\\
-\mathrm{coev}_N:N&\xrightarrow{\sim}({}^*N)^*,
+\mathrm{ev}_N:N&\xrightarrow{\sim}({}^*N)^*,
 & n&\longmapsto(g\mapsto g(n))
 && (N\in\mod(S^\op)).
 \end{aligned}
@@ -1158,20 +1194,22 @@
 Thus $(-)^*:(\mod S)^\op\to\mod(S^\op)$ and $ {}^*(-):(\mod(S^\op))^\op\to\mod S$ are inverse dualities.
 \end{lemma}
 
+\begin{supplementary}
 \begin{proof}
 For $u:M\to N$ in $\mod S$, $m\in M$, and $f\in N^*$,
 \[
-\bigl({}^*(u^*)(\mathrm{coev}_M(m))\bigr)(f)
-=(u^*f)(m)=f(u(m))=\mathrm{coev}_N(u(m))(f).
-\]
-Hence $ {}^*(u^*)\circ\mathrm{coev}_M=\mathrm{coev}_N\circ u$.
-For $M=S$, coevaluation is an isomorphism: its inverse sends $F\in{}^*(S^*)$ to $F(\id_S)$.
+\bigl({}^*(u^*)(\mathrm{ev}_M(m))\bigr)(f)
+=(u^*f)(m)=f(u(m))=\mathrm{ev}_N(u(m))(f).
+\]
+Hence $ {}^*(u^*)\circ\mathrm{ev}_M=\mathrm{ev}_N\circ u$.
+For $M=S$, evaluation is an isomorphism: its inverse sends $F\in{}^*(S^*)$ to $F(\id_S)$.
 Indeed, every $f\in S^*$ satisfies $f(s)=f(1)s$, so $F(f)=f(1)F(\id_S)=f(F(\id_S))$.
-Restriction to summands identifies the dual of a finite direct sum with the direct sum of the duals; coevaluation therefore is an isomorphism for $S^{\oplus n}$.
+Restriction to summands identifies the dual of a finite direct sum with the direct sum of the duals; evaluation therefore is an isomorphism for $S^{\oplus n}$.
 By Corollary~\ref{cor:semisimple-summands}, $M\oplus L\cong S^{\oplus n}$ for some $L$.
-Under the direct sum identifications, $\mathrm{coev}_{M\oplus L}=\mathrm{coev}_M\oplus\mathrm{coev}_L$, so $\mathrm{coev}_M$ is an isomorphism.
+Under the direct sum identifications, $\mathrm{ev}_{M\oplus L}=\mathrm{ev}_M\oplus\mathrm{ev}_L$, so $\mathrm{ev}_M$ is an isomorphism.
 Replacing $S$ by $S^\op$ proves the left module statement.
 \end{proof}
+\end{supplementary}
 
 Applying Lemma~\ref{lem:S-bidual} in each degree gives natural isomorphisms
 \[
@@ -1182,27 +1220,24 @@
 Their components are again given by $m\mapsto(f\mapsto f(m))$.
 Thus the functors in \eqref{eq:graded-S-dual-functors} restrict to inverse dualities on locally finite graded modules.
 
-\begin{advanced}
-Recall from Definition~\ref{def:enveloping-algebra} and \eqref{eq:enveloping-action} that
-\[
-S^\en=S\otimes_\Bbbk S^\op,\qquad
-m\cdot(s\otimes t^\op)=tms,
-\]
-so $S$-bimodules are the objects of $\Mod S^\en$.
-All three spaces $D(M)$, $M^*$, and $ {}^*M$ inherit bimodule structures:
+For an $S$-bimodule $M$, the one-sided duals also retain the other action:
 \begin{equation}\label{eq:bimodule-dual-actions}
 (s\lambda t)(m)=\lambda(tms),\qquad
 (sft)(m)=sf(tm),\qquad
 (sgt)(m)=g(ms)t,
 \end{equation}
-where $\lambda\in D(M)$, $f\in M^*$, $g\in{}^*M$, $s,t\in S$, and $m\in M$.
-
-For a finite-dimensional $S$-bimodule $M$, coevaluation in Lemma~\ref{lem:S-bidual} preserves both actions:
-\[
-(s\,\mathrm{coev}_M(m)\,t)(f)=f(sm)t=f(smt)=\mathrm{coev}_M(smt)(f)
-\quad(s,t\in S,\ m\in M,\ f\in M^*).
-\]
-The graded coevaluation maps preserve both actions by the same calculation in each degree.
+where $s,t\in S$, $m\in M$, $\lambda\in D(M)$, $f\in M^*$, and $g\in{}^*M$.
+These formulas also define the graded bimodule duals.
+For finite-dimensional bimodules, evaluation in Lemma~\ref{lem:S-bidual} is a bimodule isomorphism; the graded statement holds for locally finite bimodules.
+\begin{supplementary}
+Using \eqref{eq:bimodule-dual-actions} twice gives
+$(s\,\mathrm{ev}_M(m)\,t)(f)=f(sm)t=f(smt)=\mathrm{ev}_M(smt)(f)$.
+\end{supplementary}
+
+\begin{advanced}
+Recall from Definition~\ref{def:enveloping-algebra} and \eqref{eq:enveloping-action} that
+$S^\en=S\otimes_\Bbbk S^\op$ and $m\cdot(s\otimes t^\op)=tms$.
+Thus $S$-bimodules are the objects of $\Mod S^\en$.
 
 \begin{definition}\label{def:en-dual}
 The \defn{two-sided dual} of an $S$-bimodule $M$ is
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\subsection{\texorpdfstring{Left, right, and two-sided duals over $S$}{Left, right, and two-sided duals over S}}

\comm{
This section has hugely deviated from my intention.  My desired result is (graded) $A$-module duality under taking $S$-dual, not $S$-module duality under $S$-dual, which is stupid.  Results for $S$-module are just special case when $A=S$ (that does not even worth mentioning as example until its actual application).
}

Fix a finite-dimensional semisimple $\Bbbk$-algebra $S$, which is regarded as concentrated in degree $0$ when treated as a graded algebra.
Besides the $\Bbbk$-linear dual, we will also work with duals defined by left $S$-linear maps and right $S$-linear maps.
We first define these duals without grading, then apply the constructions in each degree.
%Their tensor and biduality isomorphisms in Proposition~\ref{prop:tensor-duals} and Lemma~\ref{lem:S-bidual} therefore construct quadratic duality without a choice of form; replacing them throughout by $D$ requires an identification $S\cong D(S)$.
%\comm{what is said here is not understandable to beginner; you should not mention `quadratic dual' when nobody knows what it is yet}

\begin{definition}\label{def:S-duals}
For a right $S$-module $M$ and a left $S$-module $N$, define their \defn{$S$-duals} by
\[
\begin{aligned}
M^*&:=\Hom_S(M,S),&
(sf)(m)&:=sf(m),\\
{}^*N&:=\Hom_{S^\op}(N,S),&
(gs)(n)&:=g(n)s.
\end{aligned}
\]
Here $s\in S$, $m\in M$, $n\in N$, $f\in M^*$, and $g\in{}^*N$.
\end{definition}

\[
M\in\Mod S\ \Longrightarrow\ M^*\in\Mod(S^\op),
\qquad
N\in\Mod(S^\op)\ \Longrightarrow\ {}^*N\in\Mod S.
\]
The same implications hold with $\Mod$ replaced by $\mod$, since $S$ is finite-dimensional.
\comm{$A$-module??????}
%The position of the star records the side of the original action: $f(ms)=f(m)s$ in $M^*$, whereas $g(sn)=sg(n)$ in $ {}^*N$.
%\comm{why repeat what is already written????}

For a right module map $u:M\to N$, define $u^*:N^*\to M^*$ by $u^*(f)=f\circ u$; for a left module map $u:M\to N$, the same recipe defines ${}^*u:{}^*N\to{}^*M$.
Precomposition gives functors
\[
(-)^*:(\Mod S)^\op\longrightarrow\Mod(S^\op),
\qquad
{}^*(-):(\Mod(S^\op))^\op\longrightarrow\Mod S.
\]

The grading is introduced in the same way as in Definition~\ref{def:linear-duals}.

\begin{definition}\label{def:graded-S-duals}
For graded right and left $S$-modules $M$, respectively, define their \defn{graded $S$-duals} by
\[
M^{\grstar}:=\bigoplus_{i\in\Z}(M_{-i})^*
=\bigoplus_{i\in\Z}\Hom_S^{\Z}(M,S(i)),\qquad
{}^{\grstar}M:=\bigoplus_{i\in\Z}{}^*(M_{-i})=\bigoplus_{i\in\Z}\Hom_{S^\op}^{\Z}(M,S(i)),
\]
\comm{check correct $i$ indexing in Hom notation.  $i$ or $-i$ next to $S$?}
where each indicated summand has degree $i$.
\end{definition}

For a degree $0$ right $S$-module map $u:M\to N$, define $u^{\grstar}:N^{\grstar}\to M^{\grstar}$ by
\[
(u^{\grstar})_i:(N_{-i})^*\longrightarrow(M_{-i})^*,
\qquad f\longmapsto f\circ u|_{M_{-i}}
\quad(i\in\Z).
\]
For a degree $0$ left module map $u:M\to N$, the same formula defines ${}^{\grstar}u:{}^{\grstar}N\to{}^{\grstar}M$.
With the actions from Definition~\ref{def:S-duals}, we obtain functors
\begin{equation}\label{eq:graded-S-dual-functors}
\begin{aligned}
(-)^{\grstar}&:(\Grmod S)^\op\longrightarrow\Grmod(S^\op),\\
{}^{\grstar}(-)&:(\Grmod(S^\op))^\op\longrightarrow\Grmod S.
\end{aligned}
\end{equation}
\comm{$A$-module??????????????}
Each functor in \eqref{eq:graded-S-dual-functors} restricts to locally finite modules: replace $\Grmod$ by $\grmod$ in its source and target.
Indeed, for $R=S$ or $S^\op$ and $M\in\grmod R$,
\begin{equation}\label{eq:graded-S-dual-finiteness}
\dim_\Bbbk\Hom_R(M_{-i},R)
\leq(\dim_\Bbbk M_{-i})(\dim_\Bbbk R)<\infty
\quad(i\in\Z).
\end{equation}

Parentheses on the stars distinguish the graded constructions from the full $S$-duals. In the notation \eqref{eq:graded-hom},
\[
M^{\grstar}=\bigoplus_{i\in\Z}\Hom_S^{\Z}(M,S(i)),\qquad
{}^{\grstar}M=\bigoplus_{i\in\Z}\Hom_{S^\op}^{\Z}(M,S(i)).
\]

\begin{lemma}\label{lem:S-bidual}
Coevaluation gives natural isomorphisms of functors
\[
\id_{\mod S}\xrightarrow{\sim}{}^*((-)^*),
\qquad
\id_{\mod(S^\op)}\xrightarrow{\sim}({}^*(-))^*,
\]
with components
\[
\begin{aligned}
\mathrm{coev}_M:M&\xrightarrow{\sim}{}^*(M^*),
& m&\longmapsto(f\mapsto f(m))
&& (M\in\mod S),\\
\mathrm{coev}_N:N&\xrightarrow{\sim}({}^*N)^*,
& n&\longmapsto(g\mapsto g(n))
&& (N\in\mod(S^\op)).
\end{aligned}
\]
Thus $(-)^*:(\mod S)^\op\to\mod(S^\op)$ and $ {}^*(-):(\mod(S^\op))^\op\to\mod S$ are inverse dualities.
\end{lemma}

\begin{proof}
For $u:M\to N$ in $\mod S$, $m\in M$, and $f\in N^*$,
\[
\bigl({}^*(u^*)(\mathrm{coev}_M(m))\bigr)(f)
=(u^*f)(m)=f(u(m))=\mathrm{coev}_N(u(m))(f).
\]
Hence $ {}^*(u^*)\circ\mathrm{coev}_M=\mathrm{coev}_N\circ u$.
For $M=S$, coevaluation is an isomorphism: its inverse sends $F\in{}^*(S^*)$ to $F(\id_S)$.
Indeed, every $f\in S^*$ satisfies $f(s)=f(1)s$, so $F(f)=f(1)F(\id_S)=f(F(\id_S))$.
Restriction to summands identifies the dual of a finite direct sum with the direct sum of the duals; coevaluation therefore is an isomorphism for $S^{\oplus n}$.
By Corollary~\ref{cor:semisimple-summands}, $M\oplus L\cong S^{\oplus n}$ for some $L$.
Under the direct sum identifications, $\mathrm{coev}_{M\oplus L}=\mathrm{coev}_M\oplus\mathrm{coev}_L$, so $\mathrm{coev}_M$ is an isomorphism.
Replacing $S$ by $S^\op$ proves the left module statement.
\end{proof}

Applying Lemma~\ref{lem:S-bidual} in each degree gives natural isomorphisms
\[
\id_{\grmod S}\xrightarrow{\sim}{}^{\grstar}((-)^{\grstar}),
\qquad
\id_{\grmod(S^\op)}\xrightarrow{\sim}({}^{\grstar}(-))^{\grstar}.
\]
Their components are again given by $m\mapsto(f\mapsto f(m))$.
Thus the functors in \eqref{eq:graded-S-dual-functors} restrict to inverse dualities on locally finite graded modules.

\begin{advanced}
Recall from Definition~\ref{def:enveloping-algebra} and \eqref{eq:enveloping-action} that
\[
S^\en=S\otimes_\Bbbk S^\op,\qquad
m\cdot(s\otimes t^\op)=tms,
\]
so $S$-bimodules are the objects of $\Mod S^\en$.
All three spaces $D(M)$, $M^*$, and $ {}^*M$ inherit bimodule structures:
\begin{equation}\label{eq:bimodule-dual-actions}
(s\lambda t)(m)=\lambda(tms),\qquad
(sft)(m)=sf(tm),\qquad
(sgt)(m)=g(ms)t,
\end{equation}
where $\lambda\in D(M)$, $f\in M^*$, $g\in{}^*M$, $s,t\in S$, and $m\in M$.

For a finite-dimensional $S$-bimodule $M$, coevaluation in Lemma~\ref{lem:S-bidual} preserves both actions:
\[
(s\,\mathrm{coev}_M(m)\,t)(f)=f(sm)t=f(smt)=\mathrm{coev}_M(smt)(f)
\quad(s,t\in S,\ m\in M,\ f\in M^*).
\]
The graded coevaluation maps preserve both actions by the same calculation in each degree.

\begin{definition}\label{def:en-dual}
The \defn{two-sided dual} of an $S$-bimodule $M$ is
\[
M^{*_{\en}}:=\Hom_{S^{\en}}(M,S^{\en}),
\qquad (sFt)(m):=(s\otimes t^\op)F(m)
\quad(s,t\in S,\ F\in M^{*_{\en}},\ m\in M).
\]
\end{definition}

In Definition~\ref{def:en-dual}, $M$ has the right action \eqref{eq:enveloping-action}, so $F(tms)=F(m)(s\otimes t^\op)$.
The output is a left $S^{\en}$-module by multiplication on the values, which gives the displayed bimodule action.
The two-sided dual takes values in $S^{\en}$, not in $S$.
On bimodule morphisms it acts by precomposition, as do $D$, $(-)^*$, and ${}^*(-)$; each is a contravariant functor on the category of $S$-bimodules.
The two-sided dual records both module actions in the target algebra $S^\en$.

For a graded $S$-bimodule $M$, define its \defn{graded two-sided dual} by
\[
M^{\grstar[_{\en}]}:=\bigoplus_{i\in\Z}(M_{-i})^{*_{\en}},
\qquad (M^{\grstar[_{\en}]})_i=(M_{-i})^{*_{\en}}.
\]
The bimodule actions in \eqref{eq:bimodule-dual-actions} and Definition~\ref{def:en-dual} give functors
\begin{equation}\label{eq:graded-bimodule-dual-functors}
(-)^{\grstar},\ {}^{\grstar}(-),\ (-)^{\grstar[_{\en}]}
:(\Grmod S^\en)^\op\longrightarrow\Grmod S^\en.
\end{equation}
On a degree $0$ bimodule map $u:M\to N$, each functor acts by precomposition in each degree; in particular,
\[
(u^{\grstar[_{\en}]})_i:(N_{-i})^{*_{\en}}\longrightarrow(M_{-i})^{*_{\en}},
\qquad F\longmapsto F\circ u|_{M_{-i}}.
\]
These functors restrict to locally finite bimodules: the dimension bound \eqref{eq:graded-S-dual-finiteness} also applies with $R=S^\en$.

The four duals above follow the distinction in Grant--Iyama \cite[\S2.1, pp.~2592--2593]{GI20}, with the following notation changes:
\[
\begin{array}{c|c|c}
\text{construction}&\text{Grant--Iyama}&\text{these notes}\\ \hline
\Bbbk\text{-linear dual}&M^*&D(M)\\
\text{left }S\text{-linear dual}&M^{*_\ell}&{}^*M\\
\text{right }S\text{-linear dual}&M^{*_r}&M^*\\
\text{two-sided dual}&M^\vee&M^{*_{\en}}
\end{array}
\]
The last row also changes the convention for enveloping modules.
Their $F:M\to S^\en$ is left $S^\en$-linear.
Define
\[
\sigma:S^\en\longrightarrow S^\en,\qquad
a\otimes b^\op\longmapsto b\otimes a^\op.
\]
Since $\sigma(xy)=\sigma(y)\sigma(x)$ for $x,y\in S^\en$, the map $\sigma\circ F:M\to S^\en$ satisfies
\[
(\sigma\circ F)(tms)=(\sigma\circ F)(m)(s\otimes t^\op)
\quad(s,t\in S,\ m\in M),
\]
and belongs to our $M^{*_{\en}}$.
Thus $M^\vee\to M^{*_{\en}}$, $F\mapsto\sigma\circ F$, translates their two-sided dual into our convention.
In particular, their star denotes the linear dual; our star denotes the right $S$-dual.
\end{advanced}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\subsection{\texorpdfstring{Left, right, and two-sided duals over $S$}{Left, right, and two-sided duals over S}}


Fix a finite-dimensional semisimple $\Bbbk$-algebra $S$, which is regarded as concentrated in degree $0$ when treated as a graded algebra.
For a graded algebra $A$ with $A_0=S$, every $A_i$ is an $S$-bimodule.
To dualise these components while retaining both actions, we distinguish maps to $S$ that are right or left $S$-linear.
For duality of arbitrary $A$-modules we already have the canonical functors in \eqref{eq:linear-dual-functors}.
%Their tensor and biduality isomorphisms in Proposition~\ref{prop:tensor-duals} and Lemma~\ref{lem:S-bidual} therefore construct quadratic duality without a choice of form; replacing them throughout by $D$ requires an identification $S\cong D(S)$.
%\comm{what is said here is not understandable to beginner; you should not mention `quadratic dual' when nobody knows what it is yet}

\begin{definition}\label{def:S-duals}
For a right $S$-module $M$ and a left $S$-module $N$, define their \defn{$S$-duals} by
\[
\begin{aligned}
M^*&:=\Hom_S(M,S),&
(sf)(m)&:=sf(m),\\
{}^*N&:=\Hom_{S^\op}(N,S),&
(gs)(n)&:=g(n)s.
\end{aligned}
\]
Here $s\in S$, $m\in M$, $n\in N$, $f\in M^*$, and $g\in{}^*N$.
\end{definition}

\[
M\in\Mod S\ \Longrightarrow\ M^*\in\Mod(S^\op),
\qquad
N\in\Mod(S^\op)\ \Longrightarrow\ {}^*N\in\Mod S.
\]
The same implications hold with $\Mod$ replaced by $\mod$, since $S$ is finite-dimensional.

%The position of the star records the side of the original action: $f(ms)=f(m)s$ in $M^*$, whereas $g(sn)=sg(n)$ in $ {}^*N$.
%\comm{why repeat what is already written????}

For a right module map $u:M\to N$, define $u^*:N^*\to M^*$ by $u^*(f)=f\circ u$; for a left module map $u:M\to N$, the same recipe defines ${}^*u:{}^*N\to{}^*M$.
Precomposition gives functors
\[
(-)^*:(\Mod S)^\op\longrightarrow\Mod(S^\op),
\qquad
{}^*(-):(\Mod(S^\op))^\op\longrightarrow\Mod S.
\]

The grading is introduced in the same way as in Definition~\ref{def:linear-duals}.

\begin{definition}\label{def:graded-S-duals}
For graded right and left $S$-modules $M$, respectively, define their \defn{graded $S$-duals} by
\[
M^{\grstar}:=\bigoplus_{i\in\Z}(M_{-i})^*
=\bigoplus_{i\in\Z}\Hom_S^{\Z}(M,S(i)),\qquad
{}^{\grstar}M:=\bigoplus_{i\in\Z}{}^*(M_{-i})=\bigoplus_{i\in\Z}\Hom_{S^\op}^{\Z}(M,S(i)),
\]

where each indicated summand has degree $i$.
The shift is $S(i)$, since $S(i)_{-i}=S_0$.
\end{definition}

For a degree $0$ right $S$-module map $u:M\to N$, define $u^{\grstar}:N^{\grstar}\to M^{\grstar}$ by
\[
(u^{\grstar})_i:(N_{-i})^*\longrightarrow(M_{-i})^*,
\qquad f\longmapsto f\circ u|_{M_{-i}}
\quad(i\in\Z).
\]
For a degree $0$ left module map $u:M\to N$, the same formula defines ${}^{\grstar}u:{}^{\grstar}N\to{}^{\grstar}M$.
With the actions from Definition~\ref{def:S-duals}, we obtain functors
\begin{equation}\label{eq:graded-S-dual-functors}
\begin{aligned}
(-)^{\grstar}&:(\Grmod S)^\op\longrightarrow\Grmod(S^\op),\\
{}^{\grstar}(-)&:(\Grmod(S^\op))^\op\longrightarrow\Grmod S.
\end{aligned}
\end{equation}

Each functor in \eqref{eq:graded-S-dual-functors} restricts to locally finite modules: replace $\Grmod$ by $\grmod$ in its source and target.
Indeed, for $R=S$ or $S^\op$ and $M\in\grmod R$,
\begin{equation}\label{eq:graded-S-dual-finiteness}
\dim_\Bbbk\Hom_R(M_{-i},R)
\leq(\dim_\Bbbk M_{-i})(\dim_\Bbbk R)<\infty
\quad(i\in\Z).
\end{equation}

Parentheses on the stars distinguish the graded constructions from the full $S$-duals.

\begin{lemma}\label{lem:S-bidual}
Evaluation gives natural isomorphisms of functors
\[
\id_{\mod S}\xrightarrow{\sim}{}^*((-)^*),
\qquad
\id_{\mod(S^\op)}\xrightarrow{\sim}({}^*(-))^*,
\]
with components
\[
\begin{aligned}
\mathrm{ev}_M:M&\xrightarrow{\sim}{}^*(M^*),
& m&\longmapsto(f\mapsto f(m))
&& (M\in\mod S),\\
\mathrm{ev}_N:N&\xrightarrow{\sim}({}^*N)^*,
& n&\longmapsto(g\mapsto g(n))
&& (N\in\mod(S^\op)).
\end{aligned}
\]
Thus $(-)^*:(\mod S)^\op\to\mod(S^\op)$ and $ {}^*(-):(\mod(S^\op))^\op\to\mod S$ are inverse dualities.
\end{lemma}

\begin{supplementary}
\begin{proof}
For $u:M\to N$ in $\mod S$, $m\in M$, and $f\in N^*$,
\[
\bigl({}^*(u^*)(\mathrm{ev}_M(m))\bigr)(f)
=(u^*f)(m)=f(u(m))=\mathrm{ev}_N(u(m))(f).
\]
Hence $ {}^*(u^*)\circ\mathrm{ev}_M=\mathrm{ev}_N\circ u$.
For $M=S$, evaluation is an isomorphism: its inverse sends $F\in{}^*(S^*)$ to $F(\id_S)$.
Indeed, every $f\in S^*$ satisfies $f(s)=f(1)s$, so $F(f)=f(1)F(\id_S)=f(F(\id_S))$.
Restriction to summands identifies the dual of a finite direct sum with the direct sum of the duals; evaluation therefore is an isomorphism for $S^{\oplus n}$.
By Corollary~\ref{cor:semisimple-summands}, $M\oplus L\cong S^{\oplus n}$ for some $L$.
Under the direct sum identifications, $\mathrm{ev}_{M\oplus L}=\mathrm{ev}_M\oplus\mathrm{ev}_L$, so $\mathrm{ev}_M$ is an isomorphism.
Replacing $S$ by $S^\op$ proves the left module statement.
\end{proof}
\end{supplementary}

Applying Lemma~\ref{lem:S-bidual} in each degree gives natural isomorphisms
\[
\id_{\grmod S}\xrightarrow{\sim}{}^{\grstar}((-)^{\grstar}),
\qquad
\id_{\grmod(S^\op)}\xrightarrow{\sim}({}^{\grstar}(-))^{\grstar}.
\]
Their components are again given by $m\mapsto(f\mapsto f(m))$.
Thus the functors in \eqref{eq:graded-S-dual-functors} restrict to inverse dualities on locally finite graded modules.

For an $S$-bimodule $M$, the one-sided duals also retain the other action:
\begin{equation}\label{eq:bimodule-dual-actions}
(s\lambda t)(m)=\lambda(tms),\qquad
(sft)(m)=sf(tm),\qquad
(sgt)(m)=g(ms)t,
\end{equation}
where $s,t\in S$, $m\in M$, $\lambda\in D(M)$, $f\in M^*$, and $g\in{}^*M$.
These formulas also define the graded bimodule duals.
For finite-dimensional bimodules, evaluation in Lemma~\ref{lem:S-bidual} is a bimodule isomorphism; the graded statement holds for locally finite bimodules.
\begin{supplementary}
Using \eqref{eq:bimodule-dual-actions} twice gives
$(s\,\mathrm{ev}_M(m)\,t)(f)=f(sm)t=f(smt)=\mathrm{ev}_M(smt)(f)$.
\end{supplementary}

\begin{advanced}
Recall from Definition~\ref{def:enveloping-algebra} and \eqref{eq:enveloping-action} that
$S^\en=S\otimes_\Bbbk S^\op$ and $m\cdot(s\otimes t^\op)=tms$.
Thus $S$-bimodules are the objects of $\Mod S^\en$.

\begin{definition}\label{def:en-dual}
The \defn{two-sided dual} of an $S$-bimodule $M$ is
\[
M^{*_{\en}}:=\Hom_{S^{\en}}(M,S^{\en}),
\qquad (sFt)(m):=(s\otimes t^\op)F(m)
\quad(s,t\in S,\ F\in M^{*_{\en}},\ m\in M).
\]
\end{definition}

In Definition~\ref{def:en-dual}, $M$ has the right action \eqref{eq:enveloping-action}, so $F(tms)=F(m)(s\otimes t^\op)$.
The output is a left $S^{\en}$-module by multiplication on the values, which gives the displayed bimodule action.
The two-sided dual takes values in $S^{\en}$, not in $S$.
On bimodule morphisms it acts by precomposition, as do $D$, $(-)^*$, and ${}^*(-)$; each is a contravariant functor on the category of $S$-bimodules.
The two-sided dual records both module actions in the target algebra $S^\en$.

For a graded $S$-bimodule $M$, define its \defn{graded two-sided dual} by
\[
M^{\grstar[_{\en}]}:=\bigoplus_{i\in\Z}(M_{-i})^{*_{\en}},
\qquad (M^{\grstar[_{\en}]})_i=(M_{-i})^{*_{\en}}.
\]
The bimodule actions in \eqref{eq:bimodule-dual-actions} and Definition~\ref{def:en-dual} give functors
\begin{equation}\label{eq:graded-bimodule-dual-functors}
(-)^{\grstar},\ {}^{\grstar}(-),\ (-)^{\grstar[_{\en}]}
:(\Grmod S^\en)^\op\longrightarrow\Grmod S^\en.
\end{equation}
On a degree $0$ bimodule map $u:M\to N$, each functor acts by precomposition in each degree; in particular,
\[
(u^{\grstar[_{\en}]})_i:(N_{-i})^{*_{\en}}\longrightarrow(M_{-i})^{*_{\en}},
\qquad F\longmapsto F\circ u|_{M_{-i}}.
\]
These functors restrict to locally finite bimodules: the dimension bound \eqref{eq:graded-S-dual-finiteness} also applies with $R=S^\en$.

The four duals above follow the distinction in Grant--Iyama \cite[\S2.1, pp.~2592--2593]{GI20}, with the following notation changes:
\[
\begin{array}{c|c|c}
\text{construction}&\text{Grant--Iyama}&\text{these notes}\\ \hline
\Bbbk\text{-linear dual}&M^*&D(M)\\
\text{left }S\text{-linear dual}&M^{*_\ell}&{}^*M\\
\text{right }S\text{-linear dual}&M^{*_r}&M^*\\
\text{two-sided dual}&M^\vee&M^{*_{\en}}
\end{array}
\]
The last row also changes the convention for enveloping modules.
Their $F:M\to S^\en$ is left $S^\en$-linear.
Define
\[
\sigma:S^\en\longrightarrow S^\en,\qquad
a\otimes b^\op\longmapsto b\otimes a^\op.
\]
Since $\sigma(xy)=\sigma(y)\sigma(x)$ for $x,y\in S^\en$, the map $\sigma\circ F:M\to S^\en$ satisfies
\[
(\sigma\circ F)(tms)=(\sigma\circ F)(m)(s\otimes t^\op)
\quad(s,t\in S,\ m\in M),
\]
and belongs to our $M^{*_{\en}}$.
Thus $M^\vee\to M^{*_{\en}}$, $F\mapsto\sigma\circ F$, translates their two-sided dual into our convention.
In particular, their star denotes the linear dual; our star denotes the right $S$-dual.
\end{advanced}

```

</details>

---

## Replacement 12: Supply Symmetrising Forms for General Semisimple Algebras

**Source:** [Lecture 1, line 1268](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1268)  
**Added:** `+19` lines | **Removed:** `-4` lines

Do not restrict to split semisimple algebras. Put the division-algebra construction and its published reference in advanced material. A complete citation in a footnote keeps this proposal entirely within Lecture 1 and requires no bibliography edit.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1268,6 +1303,6 @@
-To identify $S$-dual with $\Bbbk$-dual, we need a suitable linear functional $S\to\Bbbk$.
+The one-sided $S$-duals and the $\Bbbk$-linear dual are naturally isomorphic after choosing a symmetrising form on $S$.
 
-\comm{as in previous subsection, this is hugely deviated from my intention.  we should talk about $A$-module, not just $S$-module.  The main theorem of this section is pretty useless now.... we want $A$-module version.}
+
 
 \begin{definition}\label{def:symmetrising-form}
 A \defn{symmetrising form} on a finite-dimensional $\Bbbk$-algebra $S$ is a linear map $\tau:S\to\Bbbk$ satisfying
@@ -1281,10 +1316,11 @@
 
 The second condition in Definition~\ref{def:symmetrising-form} says that the bilinear form $(s,t)\mapsto\tau(st)$ is \defn{non-degenerate}: every non-zero $s\in S$ pairs non-trivially with some $t\in S$.
 
-In practice (including within the scope of these lectures), we only really use the following explicit symmetrising forms.
+Every finite-dimensional semisimple $\Bbbk$-algebra admits a symmetrising form.
+For products of matrix algebras over $\Bbbk$, the forms are explicit:
 
 \begin{example}\label{ex:symmetrising-form}
-The following maps are symmetrising forms:\comm{what about matrix over division algebra over $\Bbbk$??}
+The following maps are symmetrising forms:
 \[
 \begin{aligned}
 \tau:\Bbbk^{\oplus r}&\longrightarrow\Bbbk,
@@ -1297,3 +1333,17 @@
 \]
 \end{example}
 
+\begin{advanced}
+For a finite-dimensional division $\Bbbk$-algebra $\Delta$, there exists a non-zero linear map $\lambda:\Delta\to\Bbbk$ satisfying $\lambda(ab)=\lambda(ba)$.
+Consequently, for $S=\prod_{j=1}^r\Mat_{n_j}(\Delta_j)$, choose such maps $\lambda_j$ and set
+\[
+\tau:S\longrightarrow\Bbbk,\qquad
+(a_1,\ldots,a_r)\longmapsto
+\sum_{j=1}^r\sum_{i=1}^{n_j}\lambda_j((a_j)_{ii}).
+\]
+Symmetry follows by expanding the diagonal entries of a product.
+For non-degeneracy, if $(a_j)_{pq}=d\neq0$, choose $c\in\Delta_j$ with $\lambda_j(c)\neq0$ and let $b$ have only the entry $d^{-1}c$ in position $(q,p)$ of block $j$.
+Then $\tau(ab)=\lambda_j(c)\neq0$.
+The existence of $\lambda_j$, and the resulting symmetric structure on every finite-dimensional semisimple algebra, are proved by Eilenberg--Nakayama.\footnote{S.~Eilenberg and T.~Nakayama, \emph{On the dimension of modules and algebras, II. Frobenius algebras and quasi-Frobenius rings}, Nagoya Math. J. \textbf{9} (1955), 1--16, \S2, Propositions 3--5, pp.~4--5; \href{https://doi.org/10.1017/S0027763000023229}{doi:10.1017/S0027763000023229}.}
+\end{advanced}
+
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
To identify $S$-dual with $\Bbbk$-dual, we need a suitable linear functional $S\to\Bbbk$.

\comm{as in previous subsection, this is hugely deviated from my intention.  we should talk about $A$-module, not just $S$-module.  The main theorem of this section is pretty useless now.... we want $A$-module version.}

\begin{definition}\label{def:symmetrising-form}
A \defn{symmetrising form} on a finite-dimensional $\Bbbk$-algebra $S$ is a linear map $\tau:S\to\Bbbk$ satisfying
\[
\tau(st)=\tau(ts)\quad\text{for all }s,t\in S,
\qquad
\bigl(\tau(st)=0\text{ for all }t\in S\bigr)\ \Longrightarrow\ s=0.
\]
An algebra admitting such a form is \defn{symmetric}.
\end{definition}

The second condition in Definition~\ref{def:symmetrising-form} says that the bilinear form $(s,t)\mapsto\tau(st)$ is \defn{non-degenerate}: every non-zero $s\in S$ pairs non-trivially with some $t\in S$.

In practice (including within the scope of these lectures), we only really use the following explicit symmetrising forms.

\begin{example}\label{ex:symmetrising-form}
The following maps are symmetrising forms:\comm{what about matrix over division algebra over $\Bbbk$??}
\[
\begin{aligned}
\tau:\Bbbk^{\oplus r}&\longrightarrow\Bbbk,
& (a_1,\ldots,a_r)&\longmapsto\sum_{j=1}^r a_j,\\
\tau:\Mat_n(\Bbbk)&\longrightarrow\Bbbk,
& a&\longmapsto\Tr(a):=\sum_{i=1}^n a_{ii},\\
\text{and more generally,}\quad \tau:\prod_{j=1}^r\Mat_{n_j}(\Bbbk)&\longrightarrow\Bbbk,
& (a_1,\ldots,a_r)&\longmapsto\sum_{j=1}^r\Tr(a_j).
\end{aligned}
\]
\end{example}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
The one-sided $S$-duals and the $\Bbbk$-linear dual are naturally isomorphic after choosing a symmetrising form on $S$.



\begin{definition}\label{def:symmetrising-form}
A \defn{symmetrising form} on a finite-dimensional $\Bbbk$-algebra $S$ is a linear map $\tau:S\to\Bbbk$ satisfying
\[
\tau(st)=\tau(ts)\quad\text{for all }s,t\in S,
\qquad
\bigl(\tau(st)=0\text{ for all }t\in S\bigr)\ \Longrightarrow\ s=0.
\]
An algebra admitting such a form is \defn{symmetric}.
\end{definition}

The second condition in Definition~\ref{def:symmetrising-form} says that the bilinear form $(s,t)\mapsto\tau(st)$ is \defn{non-degenerate}: every non-zero $s\in S$ pairs non-trivially with some $t\in S$.

Every finite-dimensional semisimple $\Bbbk$-algebra admits a symmetrising form.
For products of matrix algebras over $\Bbbk$, the forms are explicit:

\begin{example}\label{ex:symmetrising-form}
The following maps are symmetrising forms:
\[
\begin{aligned}
\tau:\Bbbk^{\oplus r}&\longrightarrow\Bbbk,
& (a_1,\ldots,a_r)&\longmapsto\sum_{j=1}^r a_j,\\
\tau:\Mat_n(\Bbbk)&\longrightarrow\Bbbk,
& a&\longmapsto\Tr(a):=\sum_{i=1}^n a_{ii},\\
\text{and more generally,}\quad \tau:\prod_{j=1}^r\Mat_{n_j}(\Bbbk)&\longrightarrow\Bbbk,
& (a_1,\ldots,a_r)&\longmapsto\sum_{j=1}^r\Tr(a_j).
\end{aligned}
\]
\end{example}

\begin{advanced}
For a finite-dimensional division $\Bbbk$-algebra $\Delta$, there exists a non-zero linear map $\lambda:\Delta\to\Bbbk$ satisfying $\lambda(ab)=\lambda(ba)$.
Consequently, for $S=\prod_{j=1}^r\Mat_{n_j}(\Delta_j)$, choose such maps $\lambda_j$ and set
\[
\tau:S\longrightarrow\Bbbk,\qquad
(a_1,\ldots,a_r)\longmapsto
\sum_{j=1}^r\sum_{i=1}^{n_j}\lambda_j((a_j)_{ii}).
\]
Symmetry follows by expanding the diagonal entries of a product.
For non-degeneracy, if $(a_j)_{pq}=d\neq0$, choose $c\in\Delta_j$ with $\lambda_j(c)\neq0$ and let $b$ have only the entry $d^{-1}c$ in position $(q,p)$ of block $j$.
Then $\tau(ab)=\lambda_j(c)\neq0$.
The existence of $\lambda_j$, and the resulting symmetric structure on every finite-dimensional semisimple algebra, are proved by Eilenberg--Nakayama.\footnote{S.~Eilenberg and T.~Nakayama, \emph{On the dimension of modules and algebras, II. Frobenius algebras and quasi-Frobenius rings}, Nagoya Math. J. \textbf{9} (1955), 1--16, \S2, Propositions 3--5, pp.~4--5; \href{https://doi.org/10.1017/S0027763000023229}{doi:10.1017/S0027763000023229}.}
\end{advanced}

```

</details>

---

## Replacement 13: Make the Comparison Theorem the Common Summary

**Source:** [Lecture 1, line 1300](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1300)  
**Added:** `+13` lines | **Removed:** `-3` lines

Keep the ungraded and graded comparisons together, state bimodule compatibility in the main theorem, and explain postcomposition as pushforward. Only the genuinely two-sided enveloping-algebra dual remains advanced.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1308,7 +1358,7 @@
 \qquad
 \beta_N:{}^*N\longrightarrow D(N),\quad g\longmapsto\tau\circ g
 \end{equation}
-are $S$-module isomorphisms and give natural isomorphisms
+are $S$-module isomorphisms\footnote{These are pushforwards by $\tau$, meaning postcomposition: $\tau_*(f)=\tau\circ f$.} and give natural isomorphisms
 \begin{equation}\label{eq:dual-comparison-functors}
 \begin{aligned}
 \alpha:(-)^*&\xrightarrow{\sim}D
@@ -1330,11 +1380,21 @@
 \end{equation}
 For $M\in\grmod S$ and $N\in\grmod(S^\op)$, the degree $i$ components are $\alpha_{M_{-i}}$ and $\beta_{N_{-i}}$, respectively.
 
-\comm{so the natural transformation are really just pullback... footnote something about it??}
+
+
+\underline{\emph{Bimodule duals.}}
+With the actions in \eqref{eq:bimodule-dual-actions}, we obtain natural isomorphisms of functors
+\begin{equation}\label{eq:bimodule-dual-comparison}
+\begin{aligned}
+(-)^*\xrightarrow[\alpha]{\sim}D\xleftarrow[\beta]{\sim}{}^*(-)
+&\quad:(\mod S^\en)^\op\longrightarrow\mod S^\en,\\
+(-)^{\grstar}\xrightarrow[\alpha]{\sim}\bbD\xleftarrow[\beta]{\sim}{}^{\grstar}(-)
+&\quad:(\grmod S^\en)^\op\longrightarrow\grmod S^\en.
+\end{aligned}
+\end{equation}
 
 \begin{advanced}
 \emph{Two-sided duals.}
-If $M$ is a finite-dimensional $S$-bimodule, $\alpha_M$ and $\beta_M$ preserve both actions from \eqref{eq:bimodule-dual-actions}.
 There is also a natural isomorphism $\gamma:(-)^{*_\en}\xrightarrow{\sim}(-)^*$ given by
 \begin{equation}\label{eq:en-dual-comparison}
 \gamma_M:M^{*_{\en}}\to M^*, \qquad F\mapsto \big(m\mapsto \sum_j a_j\tau(b_j)\big)
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{theorem}[Comparison of duals]\label{prop:dual-comparison}\label{cor:graded-dual-comparison}
Choose a symmetrising form $\tau:S\to\Bbbk$.
The right and left $S$-dual functors are naturally isomorphic to the corresponding $\Bbbk$-linear dual functors, both without grading and with grading as follows. 

\underline{\emph{Ungraded duals.}}
For $M\in\mod S$ and $N\in\mod(S^\op)$, the maps
\begin{equation}\label{eq:dual-comparison}
\alpha_M:M^*\longrightarrow D(M),\quad f\longmapsto\tau\circ f,
\qquad
\beta_N:{}^*N\longrightarrow D(N),\quad g\longmapsto\tau\circ g
\end{equation}
are $S$-module isomorphisms and give natural isomorphisms
\begin{equation}\label{eq:dual-comparison-functors}
\begin{aligned}
\alpha:(-)^*&\xrightarrow{\sim}D
&&\text{of functors }(\mod S)^\op\longrightarrow\mod(S^\op),\\
\beta:{}^*(-)&\xrightarrow{\sim}D
&&\text{of functors }(\mod(S^\op))^\op\longrightarrow\mod S.
\end{aligned}
\end{equation}

\underline{\emph{Graded duals.}}
Composition with $\tau$ in each degree gives natural isomorphisms
\begin{equation}\label{eq:graded-dual-comparison}
\begin{aligned}
\alpha:(-)^{\grstar}&\xrightarrow{\sim}\bbD
&&\text{of functors }(\grmod S)^\op\longrightarrow\grmod(S^\op),\\
\beta:{}^{\grstar}(-)&\xrightarrow{\sim}\bbD
&&\text{of functors }(\grmod(S^\op))^\op\longrightarrow\grmod S.
\end{aligned}
\end{equation}
For $M\in\grmod S$ and $N\in\grmod(S^\op)$, the degree $i$ components are $\alpha_{M_{-i}}$ and $\beta_{N_{-i}}$, respectively.

\comm{so the natural transformation are really just pullback... footnote something about it??}

\begin{advanced}
\emph{Two-sided duals.}
If $M$ is a finite-dimensional $S$-bimodule, $\alpha_M$ and $\beta_M$ preserve both actions from \eqref{eq:bimodule-dual-actions}.
There is also a natural isomorphism $\gamma:(-)^{*_\en}\xrightarrow{\sim}(-)^*$ given by
\begin{equation}\label{eq:en-dual-comparison}
\gamma_M:M^{*_{\en}}\to M^*, \qquad F\mapsto \big(m\mapsto \sum_j a_j\tau(b_j)\big)
\quad\text{for}\quad
F(m)=\sum_j a_j\otimes b_j^\op.
\end{equation}
Consequently, on finite-dimensional $S$-bimodules all four dual functors are naturally isomorphic:
\[
(-)^{*_{\en}}\xrightarrow[\gamma]{\sim}(-)^*
\xrightarrow[\alpha]{\sim}D\xleftarrow[\beta]{\sim}{}^*(-).
\]
Applying $\gamma$ in each degree gives the corresponding natural isomorphisms on locally finite graded $S$-bimodules:
\[
(-)^{\grstar[_{\en}]}\xrightarrow[\gamma]{\sim}(-)^{\grstar}
\xrightarrow[\alpha]{\sim}\bbD\xleftarrow[\beta]{\sim}{}^{\grstar}(-).
\]
The first chain consists of functors $(\mod S^\en)^\op\to\mod S^\en$; the second consists of functors $(\grmod S^\en)^\op\to\grmod S^\en$.
\end{advanced}
\end{theorem}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{theorem}[Comparison of duals]\label{prop:dual-comparison}\label{cor:graded-dual-comparison}
Choose a symmetrising form $\tau:S\to\Bbbk$.
The right and left $S$-dual functors are naturally isomorphic to the corresponding $\Bbbk$-linear dual functors, both without grading and with grading as follows. 

\underline{\emph{Ungraded duals.}}
For $M\in\mod S$ and $N\in\mod(S^\op)$, the maps
\begin{equation}\label{eq:dual-comparison}
\alpha_M:M^*\longrightarrow D(M),\quad f\longmapsto\tau\circ f,
\qquad
\beta_N:{}^*N\longrightarrow D(N),\quad g\longmapsto\tau\circ g
\end{equation}
are $S$-module isomorphisms\footnote{These are pushforwards by $\tau$, meaning postcomposition: $\tau_*(f)=\tau\circ f$.} and give natural isomorphisms
\begin{equation}\label{eq:dual-comparison-functors}
\begin{aligned}
\alpha:(-)^*&\xrightarrow{\sim}D
&&\text{of functors }(\mod S)^\op\longrightarrow\mod(S^\op),\\
\beta:{}^*(-)&\xrightarrow{\sim}D
&&\text{of functors }(\mod(S^\op))^\op\longrightarrow\mod S.
\end{aligned}
\end{equation}

\underline{\emph{Graded duals.}}
Composition with $\tau$ in each degree gives natural isomorphisms
\begin{equation}\label{eq:graded-dual-comparison}
\begin{aligned}
\alpha:(-)^{\grstar}&\xrightarrow{\sim}\bbD
&&\text{of functors }(\grmod S)^\op\longrightarrow\grmod(S^\op),\\
\beta:{}^{\grstar}(-)&\xrightarrow{\sim}\bbD
&&\text{of functors }(\grmod(S^\op))^\op\longrightarrow\grmod S.
\end{aligned}
\end{equation}
For $M\in\grmod S$ and $N\in\grmod(S^\op)$, the degree $i$ components are $\alpha_{M_{-i}}$ and $\beta_{N_{-i}}$, respectively.



\underline{\emph{Bimodule duals.}}
With the actions in \eqref{eq:bimodule-dual-actions}, we obtain natural isomorphisms of functors
\begin{equation}\label{eq:bimodule-dual-comparison}
\begin{aligned}
(-)^*\xrightarrow[\alpha]{\sim}D\xleftarrow[\beta]{\sim}{}^*(-)
&\quad:(\mod S^\en)^\op\longrightarrow\mod S^\en,\\
(-)^{\grstar}\xrightarrow[\alpha]{\sim}\bbD\xleftarrow[\beta]{\sim}{}^{\grstar}(-)
&\quad:(\grmod S^\en)^\op\longrightarrow\grmod S^\en.
\end{aligned}
\end{equation}

\begin{advanced}
\emph{Two-sided duals.}
There is also a natural isomorphism $\gamma:(-)^{*_\en}\xrightarrow{\sim}(-)^*$ given by
\begin{equation}\label{eq:en-dual-comparison}
\gamma_M:M^{*_{\en}}\to M^*, \qquad F\mapsto \big(m\mapsto \sum_j a_j\tau(b_j)\big)
\quad\text{for}\quad
F(m)=\sum_j a_j\otimes b_j^\op.
\end{equation}
Consequently, on finite-dimensional $S$-bimodules all four dual functors are naturally isomorphic:
\[
(-)^{*_{\en}}\xrightarrow[\gamma]{\sim}(-)^*
\xrightarrow[\alpha]{\sim}D\xleftarrow[\beta]{\sim}{}^*(-).
\]
Applying $\gamma$ in each degree gives the corresponding natural isomorphisms on locally finite graded $S$-bimodules:
\[
(-)^{\grstar[_{\en}]}\xrightarrow[\gamma]{\sim}(-)^{\grstar}
\xrightarrow[\alpha]{\sim}\bbD\xleftarrow[\beta]{\sim}{}^{\grstar}(-).
\]
The first chain consists of functors $(\mod S^\en)^\op\to\mod S^\en$; the second consists of functors $(\grmod S^\en)^\op\to\grmod S^\en$.
\end{advanced}
\end{theorem}

```

</details>

---

## Replacement 14: Concentrate the Comparison Proof on Right Modules

**Source:** [Lecture 1, line 1358](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1358)  
**Added:** `+22` lines | **Removed:** `-26` lines

Prove the right-module statement directly, including the inverse and naturality; obtain the left-module statement by passing to the opposite algebra. Keep routine bimodule verification supplementary and the two-sided proof advanced.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1358,38 +1418,34 @@
 \begin{proof}
-\comm{concentrate proof on the right side.  left side put in complement, with minimal content; make good use of ``analogously'' instead of just repeat calculation on the other side.}
-\emph{Ungraded duals.}
-Non-degeneracy makes $S\to D(S)$, $a\mapsto(s\mapsto\tau(as))$, injective, hence bijective because both spaces have the same finite dimension.
-Thus for $\lambda\in D(M)$, according to whether $M$ is a right or left module, there exist unique $f(m)$ or $g(m)$ in $S$ satisfying
+We prove the right $S$-module comparison.
+Non-degeneracy gives an isomorphism $S\to D(S)$, $a\mapsto(s\mapsto\tau(as))$.
+Hence, for $\lambda\in D(M)$, there is a unique linear map $f:M\to S$ satisfying
 \begin{equation}\label{eq:dual-inverses}
-\tau(f(m)s)=\lambda(ms),\qquad
-\tau(sg(m))=\lambda(sm)
-\quad(s\in S,\ m\in M).
+\tau(f(m)s)=\lambda(ms)\quad\text{for all }m\in M,\ s\in S.
 \end{equation}
-The inverse of $S\to D(S)$ is linear, so $m\mapsto f(m)$ and $m\mapsto g(m)$ are linear.
-By non-degeneracy, \eqref{eq:dual-inverses} gives $f(ms)=f(m)s$ in the right module case and $g(sm)=sg(m)$ in the left module case.
-Taking $s=1$ gives $\alpha_M(f)=\lambda$ or $\beta_M(g)=\lambda$, respectively.
-Conversely, right or left $S$-linearity forces any preimage of $\lambda$ to satisfy the corresponding identity in \eqref{eq:dual-inverses}.
-The uniqueness in \eqref{eq:dual-inverses} therefore proves that $\alpha_M$ and $\beta_M$ are bijective.
-For $s\in S$, $f\in M^*$, and $m\in M$, symmetry and right $S$-linearity give
+For $m\in M$ and $s,t\in S$,
 \[
-\alpha_M(sf)(m)=\tau(sf(m))=\tau(f(m)s)=\tau(f(ms))=(s\alpha_M(f))(m).
+\tau(f(mt)s)=\lambda(mts)=\tau(f(m)ts),
 \]
-Likewise, $\beta_M(gs)(m)=\tau(g(m)s)=\tau(sg(m))=\tau(g(sm))=(\beta_M(g)s)(m)$ for a left module $M$ and $g\in{}^*M$.
-Naturality in \eqref{eq:dual-comparison-functors} is routine to check.
+so non-degeneracy implies $f(mt)=f(m)t$.
+Taking $s=1$ in \eqref{eq:dual-inverses} gives $\tau\circ f=\lambda$; conversely, every right $S$-linear preimage of $\lambda$ must satisfy \eqref{eq:dual-inverses}.
+Thus $\alpha_M$ is bijective.
+Symmetry gives $\alpha_M(sf)(m)=\tau(sf(m))=\tau(f(ms))=(s\alpha_M(f))(m)$, proving left $S$-linearity.
+For a right module map $u:M\to N$, associativity of composition gives
+$\alpha_M(f\circ u)=\alpha_N(f)\circ u$, proving naturality.
 
-\emph{Graded duals.}
-For a locally finite graded module $M$, take the direct sum over $i\in\Z$ of the ungraded comparison maps on $M_{-i}$.
-Each summand is an isomorphism, so the resulting maps are isomorphisms of degree $0$.
-Naturality in \eqref{eq:graded-dual-comparison} follows by applying the natural isomorphisms \eqref{eq:dual-comparison-functors} in each degree.
+\begin{supplementary}
+Apply the same argument to $S^\op$ to obtain $\beta$.
+For an $S$-bimodule, \eqref{eq:bimodule-dual-actions} gives
+\[
+\tau(sf(tm))=\tau(f(tms)),\qquad
+\tau(g(ms)t)=\tau(g(tms)),
+\]
+which proves that $\alpha_M$ and $\beta_M$ preserve both actions.
+\end{supplementary}
+For the graded comparisons, take the direct sum of these natural isomorphisms on $M_{-i}$ over $i\in\Z$.
 
 \begin{advanced}
 \emph{Two-sided duals.}
-For bimodule compatibility, use \eqref{eq:bimodule-dual-actions} and
-\[
-\tau(sf(tm))=\tau(f(tm)s)=\tau(f(tms)),\qquad
-\tau(g(ms)t)=\tau(tg(ms))=\tau(g(tms)).
-\]
-
 The form $\tau_{\en}(a\otimes b^\op)=\tau(a)\tau(b)$ is symmetrising on $S^{\en}$.
 Indeed, $\tau_{\en}((a\otimes b^\op)(c\otimes d^\op))=\tau(ac)\tau(db)=\tau(ca)\tau(bd)$, and its pairing is the tensor product of two non-degenerate pairings.
 The formula \eqref{eq:en-dual-comparison} satisfies
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{proof}
\comm{concentrate proof on the right side.  left side put in complement, with minimal content; make good use of ``analogously'' instead of just repeat calculation on the other side.}
\emph{Ungraded duals.}
Non-degeneracy makes $S\to D(S)$, $a\mapsto(s\mapsto\tau(as))$, injective, hence bijective because both spaces have the same finite dimension.
Thus for $\lambda\in D(M)$, according to whether $M$ is a right or left module, there exist unique $f(m)$ or $g(m)$ in $S$ satisfying
\begin{equation}\label{eq:dual-inverses}
\tau(f(m)s)=\lambda(ms),\qquad
\tau(sg(m))=\lambda(sm)
\quad(s\in S,\ m\in M).
\end{equation}
The inverse of $S\to D(S)$ is linear, so $m\mapsto f(m)$ and $m\mapsto g(m)$ are linear.
By non-degeneracy, \eqref{eq:dual-inverses} gives $f(ms)=f(m)s$ in the right module case and $g(sm)=sg(m)$ in the left module case.
Taking $s=1$ gives $\alpha_M(f)=\lambda$ or $\beta_M(g)=\lambda$, respectively.
Conversely, right or left $S$-linearity forces any preimage of $\lambda$ to satisfy the corresponding identity in \eqref{eq:dual-inverses}.
The uniqueness in \eqref{eq:dual-inverses} therefore proves that $\alpha_M$ and $\beta_M$ are bijective.
For $s\in S$, $f\in M^*$, and $m\in M$, symmetry and right $S$-linearity give
\[
\alpha_M(sf)(m)=\tau(sf(m))=\tau(f(m)s)=\tau(f(ms))=(s\alpha_M(f))(m).
\]
Likewise, $\beta_M(gs)(m)=\tau(g(m)s)=\tau(sg(m))=\tau(g(sm))=(\beta_M(g)s)(m)$ for a left module $M$ and $g\in{}^*M$.
Naturality in \eqref{eq:dual-comparison-functors} is routine to check.

\emph{Graded duals.}
For a locally finite graded module $M$, take the direct sum over $i\in\Z$ of the ungraded comparison maps on $M_{-i}$.
Each summand is an isomorphism, so the resulting maps are isomorphisms of degree $0$.
Naturality in \eqref{eq:graded-dual-comparison} follows by applying the natural isomorphisms \eqref{eq:dual-comparison-functors} in each degree.

\begin{advanced}
\emph{Two-sided duals.}
For bimodule compatibility, use \eqref{eq:bimodule-dual-actions} and
\[
\tau(sf(tm))=\tau(f(tm)s)=\tau(f(tms)),\qquad
\tau(g(ms)t)=\tau(tg(ms))=\tau(g(tms)).
\]

The form $\tau_{\en}(a\otimes b^\op)=\tau(a)\tau(b)$ is symmetrising on $S^{\en}$.
Indeed, $\tau_{\en}((a\otimes b^\op)(c\otimes d^\op))=\tau(ac)\tau(db)=\tau(ca)\tau(bd)$, and its pairing is the tensor product of two non-degenerate pairings.
The formula \eqref{eq:en-dual-comparison} satisfies
\[
\gamma_M(F)(ms)=\gamma_M(F)(m)s,\qquad
\gamma_M(sFt)=s\gamma_M(F)t,\qquad
\alpha_M(\gamma_M(F))=\tau_{\en}\circ F.
\]
The argument \eqref{eq:dual-inverses}, applied to $S^{\en}$ and $\tau_{\en}$, makes $F\mapsto\tau_{\en}\circ F$ an isomorphism.
Thus $\gamma_M$ is an isomorphism.
For a bimodule map $u:M\to N$ and $F\in N^{*_{\en}}$, the formula \eqref{eq:en-dual-comparison} gives $\gamma_M(F\circ u)=\gamma_N(F)\circ u$, proving naturality.
Taking the direct sum of $\gamma_{M_{-i}}$ over $i\in\Z$ gives the graded two-sided comparison.
Each component is a bimodule isomorphism, and naturality follows in each degree from the ungraded comparison.\qedhere
\end{advanced}
\end{proof}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{proof}
We prove the right $S$-module comparison.
Non-degeneracy gives an isomorphism $S\to D(S)$, $a\mapsto(s\mapsto\tau(as))$.
Hence, for $\lambda\in D(M)$, there is a unique linear map $f:M\to S$ satisfying
\begin{equation}\label{eq:dual-inverses}
\tau(f(m)s)=\lambda(ms)\quad\text{for all }m\in M,\ s\in S.
\end{equation}
For $m\in M$ and $s,t\in S$,
\[
\tau(f(mt)s)=\lambda(mts)=\tau(f(m)ts),
\]
so non-degeneracy implies $f(mt)=f(m)t$.
Taking $s=1$ in \eqref{eq:dual-inverses} gives $\tau\circ f=\lambda$; conversely, every right $S$-linear preimage of $\lambda$ must satisfy \eqref{eq:dual-inverses}.
Thus $\alpha_M$ is bijective.
Symmetry gives $\alpha_M(sf)(m)=\tau(sf(m))=\tau(f(ms))=(s\alpha_M(f))(m)$, proving left $S$-linearity.
For a right module map $u:M\to N$, associativity of composition gives
$\alpha_M(f\circ u)=\alpha_N(f)\circ u$, proving naturality.

\begin{supplementary}
Apply the same argument to $S^\op$ to obtain $\beta$.
For an $S$-bimodule, \eqref{eq:bimodule-dual-actions} gives
\[
\tau(sf(tm))=\tau(f(tms)),\qquad
\tau(g(ms)t)=\tau(g(tms)),
\]
which proves that $\alpha_M$ and $\beta_M$ preserve both actions.
\end{supplementary}
For the graded comparisons, take the direct sum of these natural isomorphisms on $M_{-i}$ over $i\in\Z$.

\begin{advanced}
\emph{Two-sided duals.}
The form $\tau_{\en}(a\otimes b^\op)=\tau(a)\tau(b)$ is symmetrising on $S^{\en}$.
Indeed, $\tau_{\en}((a\otimes b^\op)(c\otimes d^\op))=\tau(ac)\tau(db)=\tau(ca)\tau(bd)$, and its pairing is the tensor product of two non-degenerate pairings.
The formula \eqref{eq:en-dual-comparison} satisfies
\[
\gamma_M(F)(ms)=\gamma_M(F)(m)s,\qquad
\gamma_M(sFt)=s\gamma_M(F)t,\qquad
\alpha_M(\gamma_M(F))=\tau_{\en}\circ F.
\]
The argument \eqref{eq:dual-inverses}, applied to $S^{\en}$ and $\tau_{\en}$, makes $F\mapsto\tau_{\en}\circ F$ an isomorphism.
Thus $\gamma_M$ is an isomorphism.
For a bimodule map $u:M\to N$ and $F\in N^{*_{\en}}$, the formula \eqref{eq:en-dual-comparison} gives $\gamma_M(F\circ u)=\gamma_N(F)\circ u$, proving naturality.
Taking the direct sum of $\gamma_{M_{-i}}$ over $i\in\Z$ gives the graded two-sided comparison.
Each component is a bimodule isomorphism, and naturality follows in each degree from the ungraded comparison.\qedhere
\end{advanced}
\end{proof}

```

</details>

---

## Replacement 15: Remove the Duplicate Worked Example and Separate Transported Actions

**Source:** [Lecture 1, line 1409](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1409)  
**Added:** `+22` lines | **Removed:** `-56` lines

Remove the worked block-dual calculation that duplicates homework; Replacement 16 makes its exercise self-contained. Retain the dependence on the form, put transported $A$-actions in advanced material, and distinguish them from the commuting-action construction in BGS. No Ext or Tor terminology is introduced before its lecture.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1409,65 +1465,31 @@
-\begin{example}\label{ex:dual-blocks}
-\comm{what is the purpose of the example?? Is this example also homework exercise???  If this is about dual on $S$-modules, then it is useless.  We work with $S$-dual on $A$-modules, then compare $M^*$ and ${}^*M$ makes no sense anymore... }
-The right and left $S$-duals may consist of different maps to $S$, even though \eqref{eq:dual-comparison} identifies both with the linear dual.
-Let $S=(\Bbbk A_2)_0=\Bbbk e_1\oplus\Bbbk e_2$ and $V=(\Bbbk A_2)_1=\Bbbk e_{12}$, where $e_1=e_{11}$ and $e_2=e_{22}$.
-Use the symmetrising form and linear functional
-\[
-\begin{aligned}
-\tau:S&\longrightarrow\Bbbk,& ae_1+be_2&\longmapsto a+b,\\
-\varepsilon:V&\longrightarrow\Bbbk,& ce_{12}&\longmapsto c
-\quad(a,b,c\in\Bbbk).
-\end{aligned}
-\]
-
-For a right $S$-linear map $f:V\to S$,
-\[
-f(e_{12})=f(e_{12}e_2)=f(e_{12})e_2\in\Bbbk e_2.
-\]
-Requiring \comm{what do you want to do to make you say `require' here????} $\tau\circ f=\varepsilon$ therefore forces $f(e_{12})=e_2$.
-Conversely, the $\Bbbk$-linear map determined by $f(e_{12})=e_2$ is right $S$-linear: for $s=ae_1+be_2\in S$, we have $f(e_{12}s)=f(be_{12})=be_2=f(e_{12})s$.
-
-For a left $S$-linear map $g:V\to S$,
-\[
-g(e_{12})=g(e_1e_{12})=e_1g(e_{12})\in\Bbbk e_1.
-\]
-Requiring $\tau\circ g=\varepsilon$ instead forces $g(e_{12})=e_1$.
-Conversely, the $\Bbbk$-linear map determined by $g(e_{12})=e_1$ is left $S$-linear: for $s=ae_1+be_2\in S$, we have $g(se_{12})=g(ae_{12})=ae_1=sg(e_{12})$.
-
-The maps are not interchangeable: $f$ is not left $S$-linear, and $g$ is not right $S$-linear, since
-\[
-f(e_1e_{12})=e_2\neq0=e_1f(e_{12}),
-\qquad
-g(e_{12}e_2)=e_1\neq0=g(e_{12})e_2.
-\]
-Nevertheless, composing either map with $\tau$ gives $\varepsilon$.
-Thus the comparison maps in \eqref{eq:dual-comparison} satisfy
-\[
-\alpha_V(f)=\varepsilon=\beta_V(g),
-\qquad
-(\beta_V^{-1}\circ\alpha_V)(f)=g\neq f.
-\]
-The isomorphism $V^*\xrightarrow{\sim}{}^*V$ sends $f$ to $g$; it is not equality of the two spaces of maps inside $\Hom_\Bbbk(V,S)$.
-Although $S$ is commutative, its left and right actions on $V$ differ.
-\end{example}
-
 \begin{remark}
-The ungraded and graded identifications in Theorem~\ref{prop:dual-comparison} depend on $\tau$.
-For instance, $\tau(a_1,\ldots,a_r)=\sum_i c_i a_i$ is symmetrising on $\Bbbk^{\oplus r}$ for any $c_i\neq 0$.
-The theorem compares the different dual constructions separately in the ungraded and graded settings; it does not identify $D(M)$ with $\bbD(M)$ for an arbitrary infinite-dimensional graded module.\comm{what's the point of infinite-dim graded module??? our stress is on locally finite graded modules, talking about infinite-dimensional without saying locally finite just does not add any value to the content}
+The natural isomorphisms in Theorem~\ref{prop:dual-comparison} depend on the chosen symmetrising form.
+For example, every choice $c_1,\ldots,c_r\in\Bbbk\setminus\{0\}$ gives a form
+$\tau(a_1,\ldots,a_r)=\sum_{i=1}^r c_i a_i$ on $\Bbbk^{\oplus r}$.
 \begin{advanced}
-The two-sided comparison \eqref{eq:en-dual-comparison} also depends on $\tau$; it does not require $S^{\en}$ to be semisimple.
+The two-sided comparison \eqref{eq:en-dual-comparison} also depends on $\tau$ and does not require $S^\en$ to be semisimple.
 \end{advanced}
 \end{remark}
 
-For a graded algebra $A$ with $S=A_0$, Theorem~\ref{cor:graded-dual-comparison} transports the $A$-action \eqref{eq:linear-dual-actions} to the graded $S$-duals of a locally finite graded $A$-module:
+\begin{advanced}
+\begin{remark}\label{rem:transported-dual-action}
+Let $A$ be a graded algebra with $A_0=S$.
+For a right $A$-module $M$, the formula $(af)(m)=f(ma)$ need not preserve $\Hom_S(M,S)$: the subalgebra $S$ need not be central in $A$.
+After choosing $\tau$, the comparison \eqref{eq:graded-dual-comparison} transports the canonical action on $\bbD(M)$ to the graded $S$-dual of a locally finite module:
 \[
 af=\alpha_M^{-1}(a\alpha_M(f))\quad\text{for right }M,
-\qquad
-ga=\beta_M^{-1}(\beta_M(g)a)\quad\text{for left }M.
+\qquad ga=\beta_N^{-1}(\beta_N(g)a)\quad\text{for left }N,
 \]
-Here $\alpha_M(f)=\tau\circ f$ and $\beta_M(g)=\tau\circ g$ are the restrictions of \eqref{eq:dual-comparison}; $a\in A$, $f\in M^{\grstar}$, and $g\in{}^{\grstar}M$.
-The restrictions to $S$ agree with Definition~\ref{def:S-duals}.
-These remain duals over $S$, not duals taking values in $A$.
-The graded $S$-duals are defined without $\tau$, but these transported $A$-actions depend on $\tau$. The canonical graded $A$-module is $\bbD(M)$.
-Exercise~\ref{ex:transported-dual-action} computes this dependence.
+where $a\in A$, $f\in M^{\grstar}$, and $g\in{}^{\grstar}N$.
+The action on the right-hand sides is \eqref{eq:linear-dual-actions}.
+The restrictions to $S$ are the actions in Definition~\ref{def:S-duals}.
+No extra hypothesis on $A$ is needed, but the transported actions depend on $\tau$; the canonical module is $\bbD(M)$.
+The ungraded construction works in the same way for finite-dimensional $A$-modules.
 
+For comparison, if $X$ is an $(A,S)$-bimodule, its commuting actions directly give $\Hom_S(X,S)$ an $(S,A)$-bimodule structure by
+$(sfa)(x)=s f(ax)$.
+This is the construction used in \cite[\S2.2]{BGS96}; it uses commuting actions on opposite sides, not merely restriction of a right $A$-module to $S$.
+Exercise~\ref{ex:transported-dual-action} compares two transported actions on one graded $S$-dual.
+\end{remark}
+\end{advanced}
+
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:dual-blocks}
\comm{what is the purpose of the example?? Is this example also homework exercise???  If this is about dual on $S$-modules, then it is useless.  We work with $S$-dual on $A$-modules, then compare $M^*$ and ${}^*M$ makes no sense anymore... }
The right and left $S$-duals may consist of different maps to $S$, even though \eqref{eq:dual-comparison} identifies both with the linear dual.
Let $S=(\Bbbk A_2)_0=\Bbbk e_1\oplus\Bbbk e_2$ and $V=(\Bbbk A_2)_1=\Bbbk e_{12}$, where $e_1=e_{11}$ and $e_2=e_{22}$.
Use the symmetrising form and linear functional
\[
\begin{aligned}
\tau:S&\longrightarrow\Bbbk,& ae_1+be_2&\longmapsto a+b,\\
\varepsilon:V&\longrightarrow\Bbbk,& ce_{12}&\longmapsto c
\quad(a,b,c\in\Bbbk).
\end{aligned}
\]

For a right $S$-linear map $f:V\to S$,
\[
f(e_{12})=f(e_{12}e_2)=f(e_{12})e_2\in\Bbbk e_2.
\]
Requiring \comm{what do you want to do to make you say `require' here????} $\tau\circ f=\varepsilon$ therefore forces $f(e_{12})=e_2$.
Conversely, the $\Bbbk$-linear map determined by $f(e_{12})=e_2$ is right $S$-linear: for $s=ae_1+be_2\in S$, we have $f(e_{12}s)=f(be_{12})=be_2=f(e_{12})s$.

For a left $S$-linear map $g:V\to S$,
\[
g(e_{12})=g(e_1e_{12})=e_1g(e_{12})\in\Bbbk e_1.
\]
Requiring $\tau\circ g=\varepsilon$ instead forces $g(e_{12})=e_1$.
Conversely, the $\Bbbk$-linear map determined by $g(e_{12})=e_1$ is left $S$-linear: for $s=ae_1+be_2\in S$, we have $g(se_{12})=g(ae_{12})=ae_1=sg(e_{12})$.

The maps are not interchangeable: $f$ is not left $S$-linear, and $g$ is not right $S$-linear, since
\[
f(e_1e_{12})=e_2\neq0=e_1f(e_{12}),
\qquad
g(e_{12}e_2)=e_1\neq0=g(e_{12})e_2.
\]
Nevertheless, composing either map with $\tau$ gives $\varepsilon$.
Thus the comparison maps in \eqref{eq:dual-comparison} satisfy
\[
\alpha_V(f)=\varepsilon=\beta_V(g),
\qquad
(\beta_V^{-1}\circ\alpha_V)(f)=g\neq f.
\]
The isomorphism $V^*\xrightarrow{\sim}{}^*V$ sends $f$ to $g$; it is not equality of the two spaces of maps inside $\Hom_\Bbbk(V,S)$.
Although $S$ is commutative, its left and right actions on $V$ differ.
\end{example}

\begin{remark}
The ungraded and graded identifications in Theorem~\ref{prop:dual-comparison} depend on $\tau$.
For instance, $\tau(a_1,\ldots,a_r)=\sum_i c_i a_i$ is symmetrising on $\Bbbk^{\oplus r}$ for any $c_i\neq 0$.
The theorem compares the different dual constructions separately in the ungraded and graded settings; it does not identify $D(M)$ with $\bbD(M)$ for an arbitrary infinite-dimensional graded module.\comm{what's the point of infinite-dim graded module??? our stress is on locally finite graded modules, talking about infinite-dimensional without saying locally finite just does not add any value to the content}
\begin{advanced}
The two-sided comparison \eqref{eq:en-dual-comparison} also depends on $\tau$; it does not require $S^{\en}$ to be semisimple.
\end{advanced}
\end{remark}

For a graded algebra $A$ with $S=A_0$, Theorem~\ref{cor:graded-dual-comparison} transports the $A$-action \eqref{eq:linear-dual-actions} to the graded $S$-duals of a locally finite graded $A$-module:
\[
af=\alpha_M^{-1}(a\alpha_M(f))\quad\text{for right }M,
\qquad
ga=\beta_M^{-1}(\beta_M(g)a)\quad\text{for left }M.
\]
Here $\alpha_M(f)=\tau\circ f$ and $\beta_M(g)=\tau\circ g$ are the restrictions of \eqref{eq:dual-comparison}; $a\in A$, $f\in M^{\grstar}$, and $g\in{}^{\grstar}M$.
The restrictions to $S$ agree with Definition~\ref{def:S-duals}.
These remain duals over $S$, not duals taking values in $A$.
The graded $S$-duals are defined without $\tau$, but these transported $A$-actions depend on $\tau$. The canonical graded $A$-module is $\bbD(M)$.
Exercise~\ref{ex:transported-dual-action} computes this dependence.

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{remark}
The natural isomorphisms in Theorem~\ref{prop:dual-comparison} depend on the chosen symmetrising form.
For example, every choice $c_1,\ldots,c_r\in\Bbbk\setminus\{0\}$ gives a form
$\tau(a_1,\ldots,a_r)=\sum_{i=1}^r c_i a_i$ on $\Bbbk^{\oplus r}$.
\begin{advanced}
The two-sided comparison \eqref{eq:en-dual-comparison} also depends on $\tau$ and does not require $S^\en$ to be semisimple.
\end{advanced}
\end{remark}

\begin{advanced}
\begin{remark}\label{rem:transported-dual-action}
Let $A$ be a graded algebra with $A_0=S$.
For a right $A$-module $M$, the formula $(af)(m)=f(ma)$ need not preserve $\Hom_S(M,S)$: the subalgebra $S$ need not be central in $A$.
After choosing $\tau$, the comparison \eqref{eq:graded-dual-comparison} transports the canonical action on $\bbD(M)$ to the graded $S$-dual of a locally finite module:
\[
af=\alpha_M^{-1}(a\alpha_M(f))\quad\text{for right }M,
\qquad ga=\beta_N^{-1}(\beta_N(g)a)\quad\text{for left }N,
\]
where $a\in A$, $f\in M^{\grstar}$, and $g\in{}^{\grstar}N$.
The action on the right-hand sides is \eqref{eq:linear-dual-actions}.
The restrictions to $S$ are the actions in Definition~\ref{def:S-duals}.
No extra hypothesis on $A$ is needed, but the transported actions depend on $\tau$; the canonical module is $\bbD(M)$.
The ungraded construction works in the same way for finite-dimensional $A$-modules.

For comparison, if $X$ is an $(A,S)$-bimodule, its commuting actions directly give $\Hom_S(X,S)$ an $(S,A)$-bimodule structure by
$(sfa)(x)=s f(ax)$.
This is the construction used in \cite[\S2.2]{BGS96}; it uses commuting actions on opposite sides, not merely restriction of a right $A$-module to $S$.
Exercise~\ref{ex:transported-dual-action} compares two transported actions on one graded $S$-dual.
\end{remark}
\end{advanced}

```

</details>

---

## Replacement 16: Make the Exercises Self-Contained and Retain Hidden Solutions

**Source:** [Lecture 1, line 1488](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1488)  
**Added:** `+48` lines | **Removed:** `-6` lines

The two problems occur in Homework1.tex as Exercise 1(3) and Exercise 2(1). Keep their solutions in hidden blocks immediately after the corresponding lecture exercise statements, not in the main exposition. Move the existing labels to the exercises. The homework retains the questions and uses its native hidden solution environment.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1488,10 +1510,52 @@
-\begin{exercise}[Homogeneous maps]
-For the map $f$ in Example~\ref{ex:infinite-hom}, write every non-zero homogeneous component $f_d$ explicitly and prove that no finite sum equals $f$.
+\begin{exercise}[Homogeneous maps]\label{ex:infinite-hom}
+The finite-generation hypothesis in Lemma~\ref{lem:homogeneous-hom-sum} is needed.
+Let $S=\Bbbk e_1\oplus\Bbbk e_2$ with componentwise multiplication, let $N=e_1S$ have degree $0$, and put
+\[
+M=\bigoplus_{i\geq0}(e_1S)(-i)=\bigoplus_{i\geq0}\Bbbk m_i,
+\qquad \deg m_i=i,\quad m_i e_1=m_i,\quad m_i e_2=0.
+\]
+For the $S$-linear map $f:M\to N$ with $f(m_i)=e_1$ for every $i\geq0$, determine all homogeneous components and prove that $f$ is not a finite sum of homogeneous maps.
 \end{exercise}
 
-\begin{exercise}[Dependence on the form]
-Repeat Example~\ref{ex:dual-blocks} with $\tau(e_i)=c_i\neq0$.
-For $V=\Bbbk e_{12}$, find the right and left $S$-linear maps corresponding to the functional $\varepsilon(e_{12})=1$ under \eqref{eq:dual-comparison}.
-\emph{Check.} Their values on $e_{12}$ are $c_2^{-1}e_2$ and $c_1^{-1}e_1$, respectively.
+\begin{hidden}
+\begin{proof}[Solution]
+For a finitely supported family $(c_i)_{i\geq0}$,
+\[
+f\Bigl(\sum_{i\geq0}c_i m_i\Bigr)=\sum_{c_i\neq0}c_i e_1.
+\]
+On the summand $(e_1S)(-i)$, the restriction $f|_{(e_1S)(-i)}:(e_1S)(-i)\to e_1S$ is the underlying identity map, of degree $-i$.
+Explicitly, the homogeneous components are
+\[
+f_{-r}:M\longrightarrow N,\qquad f_{-r}(m_i)=\delta_{ri}e_1
+\quad\text{for }r,i\geq0,
+\]
+and $f_d=0$ for $d>0$.
+A homogeneous map $M\to N$ of degree $d$ vanishes on $m_i$ unless $d=-i$.
+Every finite sum of homogeneous maps therefore vanishes on all but finitely many $m_i$, whereas $f(m_i)=e_1$ for every $i\geq0$.
+Hence $f$ is not a finite sum of homogeneous maps.
+\end{proof}
+\end{hidden}
+
+\begin{exercise}[Dependence on the form]\label{ex:dual-blocks}
+Let $S=(\Bbbk A_2)_0=\Bbbk e_{11}\oplus\Bbbk e_{22}$, $V=(\Bbbk A_2)_1=\Bbbk e_{12}$, and $c_1,c_2\in\Bbbk\setminus\{0\}$.
+Set $\tau(ae_{11}+be_{22})=c_1a+c_2b$ and let $\varepsilon:V\to\Bbbk$ satisfy $\varepsilon(e_{12})=1$.
+Find the right and left $S$-linear maps corresponding to $\varepsilon$ under \eqref{eq:dual-comparison}, and determine how they depend on $c_1,c_2$.
 \end{exercise}
 
+\begin{hidden}
+\begin{proof}[Solution]
+Right $S$-linearity forces $f(e_{12})=f(e_{12})e_{22}\in\Bbbk e_{22}$, and left $S$-linearity forces $g(e_{12})=e_{11}g(e_{12})\in\Bbbk e_{11}$.
+Thus $\tau\circ f=\varepsilon=\tau\circ g$ requires
+\[
+f(e_{12})=c_2^{-1}e_{22},\qquad g(e_{12})=c_1^{-1}e_{11}.
+\]
+Conversely, the linear maps with these values satisfy, for $s=ae_{11}+be_{22}\in S$,
+\[
+f(e_{12}s)=bc_2^{-1}e_{22}=f(e_{12})s,\qquad
+g(se_{12})=ac_1^{-1}e_{11}=sg(e_{12}).
+\]
+Their compositions with $\tau$ take $e_{12}$ to $1$, as required.
+The original worked example is the case $c_1=c_2=1$.
+\end{proof}
+\end{hidden}
+
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{exercise}[Homogeneous maps]
For the map $f$ in Example~\ref{ex:infinite-hom}, write every non-zero homogeneous component $f_d$ explicitly and prove that no finite sum equals $f$.
\end{exercise}

\begin{exercise}[Dependence on the form]
Repeat Example~\ref{ex:dual-blocks} with $\tau(e_i)=c_i\neq0$.
For $V=\Bbbk e_{12}$, find the right and left $S$-linear maps corresponding to the functional $\varepsilon(e_{12})=1$ under \eqref{eq:dual-comparison}.
\emph{Check.} Their values on $e_{12}$ are $c_2^{-1}e_2$ and $c_1^{-1}e_1$, respectively.
\end{exercise}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{exercise}[Homogeneous maps]\label{ex:infinite-hom}
The finite-generation hypothesis in Lemma~\ref{lem:homogeneous-hom-sum} is needed.
Let $S=\Bbbk e_1\oplus\Bbbk e_2$ with componentwise multiplication, let $N=e_1S$ have degree $0$, and put
\[
M=\bigoplus_{i\geq0}(e_1S)(-i)=\bigoplus_{i\geq0}\Bbbk m_i,
\qquad \deg m_i=i,\quad m_i e_1=m_i,\quad m_i e_2=0.
\]
For the $S$-linear map $f:M\to N$ with $f(m_i)=e_1$ for every $i\geq0$, determine all homogeneous components and prove that $f$ is not a finite sum of homogeneous maps.
\end{exercise}

\begin{hidden}
\begin{proof}[Solution]
For a finitely supported family $(c_i)_{i\geq0}$,
\[
f\Bigl(\sum_{i\geq0}c_i m_i\Bigr)=\sum_{c_i\neq0}c_i e_1.
\]
On the summand $(e_1S)(-i)$, the restriction $f|_{(e_1S)(-i)}:(e_1S)(-i)\to e_1S$ is the underlying identity map, of degree $-i$.
Explicitly, the homogeneous components are
\[
f_{-r}:M\longrightarrow N,\qquad f_{-r}(m_i)=\delta_{ri}e_1
\quad\text{for }r,i\geq0,
\]
and $f_d=0$ for $d>0$.
A homogeneous map $M\to N$ of degree $d$ vanishes on $m_i$ unless $d=-i$.
Every finite sum of homogeneous maps therefore vanishes on all but finitely many $m_i$, whereas $f(m_i)=e_1$ for every $i\geq0$.
Hence $f$ is not a finite sum of homogeneous maps.
\end{proof}
\end{hidden}

\begin{exercise}[Dependence on the form]\label{ex:dual-blocks}
Let $S=(\Bbbk A_2)_0=\Bbbk e_{11}\oplus\Bbbk e_{22}$, $V=(\Bbbk A_2)_1=\Bbbk e_{12}$, and $c_1,c_2\in\Bbbk\setminus\{0\}$.
Set $\tau(ae_{11}+be_{22})=c_1a+c_2b$ and let $\varepsilon:V\to\Bbbk$ satisfy $\varepsilon(e_{12})=1$.
Find the right and left $S$-linear maps corresponding to $\varepsilon$ under \eqref{eq:dual-comparison}, and determine how they depend on $c_1,c_2$.
\end{exercise}

\begin{hidden}
\begin{proof}[Solution]
Right $S$-linearity forces $f(e_{12})=f(e_{12})e_{22}\in\Bbbk e_{22}$, and left $S$-linearity forces $g(e_{12})=e_{11}g(e_{12})\in\Bbbk e_{11}$.
Thus $\tau\circ f=\varepsilon=\tau\circ g$ requires
\[
f(e_{12})=c_2^{-1}e_{22},\qquad g(e_{12})=c_1^{-1}e_{11}.
\]
Conversely, the linear maps with these values satisfy, for $s=ae_{11}+be_{22}\in S$,
\[
f(e_{12}s)=bc_2^{-1}e_{22}=f(e_{12})s,\qquad
g(se_{12})=ac_1^{-1}e_{11}=sg(e_{12}).
\]
Their compositions with $\tau$ take $e_{12}$ to $1$, as required.
The original worked example is the case $c_1=c_2=1$.
\end{proof}
\end{hidden}

```

</details>

---

## Replacement 17: Use Only the Needed Characteristic Assumption

**Source:** [Lecture 1, line 1498](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1498)  
**Added:** `+5` lines | **Removed:** `-2` lines

Replace the unnecessary rational-field restriction by characteristic not 2. State that the point is comparing the transported $A$-actions, and place the exercise in advanced material. The existing hidden solution is unchanged and the hidden setting is not toggled.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1498,5 +1562,7 @@
+\begin{advanced}
 \begin{exercise}[Dependence of the action on the form]\label{ex:transported-dual-action}
-In this exercise take $\Bbbk=\mathbb Q$.  \comm{not asking you to do edit, but tell me why need to restrict to rational number}
+Assume $\operatorname{char}\Bbbk\neq2$.
+This exercise compares the $A$-actions transported through two symmetrising forms as in Remark~\ref{rem:transported-dual-action}.
 Let $A=\Bbbk A_2$, $S=\Bbbk e_{11}\oplus\Bbbk e_{22}$, and $M=e_{11}A$.
 For $c_1,c_2\in\Bbbk\setminus\{0\}$, define
 \begin{equation}\label{eq:transported-dual-form}
@@ -1513,7 +1579,7 @@
 \end{aligned}
 \end{equation}
 \begin{enumerate}
-\item Verify that $\tau$ is symmetrising and that $\varphi_0,\varphi_1$ form a homogeneous basis of $M^{\grstar}$. Determine their degrees.  \comm{if we only concern $S$-module, then this exercise is time-wasting.  we concern $A$-modules.}
+\item Verify that $\tau$ is symmetrising and that $\varphi_0,\varphi_1$ form a homogeneous basis of $M^{\grstar}$. Determine their degrees.  
 \item Set $\tau_1(ae_{11}+be_{22})=a+b$ and $\tau_2(ae_{11}+be_{22})=a+2b$.
 Write $\cdot_1,\cdot_2$ for the respective left $A$-actions transported from $\bbD(M)$ using \eqref{eq:dual-comparison}.
 Calculate the actions of $e_{11},e_{22},e_{12}$ on $\varphi_0,\varphi_1$ for both forms.
@@ -1525,4 +1591,5 @@
 by giving $t(\varphi_0)$ and $t(\varphi_1)$.
 \end{enumerate}
 \end{exercise}
+\end{advanced}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{exercise}[Dependence of the action on the form]\label{ex:transported-dual-action}
In this exercise take $\Bbbk=\mathbb Q$.  \comm{not asking you to do edit, but tell me why need to restrict to rational number}
Let $A=\Bbbk A_2$, $S=\Bbbk e_{11}\oplus\Bbbk e_{22}$, and $M=e_{11}A$.
For $c_1,c_2\in\Bbbk\setminus\{0\}$, define
\begin{equation}\label{eq:transported-dual-form}
\tau:S\longrightarrow\Bbbk,\qquad
a e_{11}+b e_{22}\longmapsto c_1a+c_2b
\quad(a,b\in\Bbbk).
\end{equation}
Consider the right $S$-linear maps
\begin{equation}\label{eq:transported-dual-functionals}
\begin{aligned}
\varphi_0:M&\longrightarrow S,& a e_{11}+b e_{12}&\longmapsto a e_{11},\\
\varphi_1:M&\longrightarrow S,& a e_{11}+b e_{12}&\longmapsto b e_{22}
\quad(a,b\in\Bbbk).
\end{aligned}
\end{equation}
\begin{enumerate}
\item Verify that $\tau$ is symmetrising and that $\varphi_0,\varphi_1$ form a homogeneous basis of $M^{\grstar}$. Determine their degrees.  \comm{if we only concern $S$-module, then this exercise is time-wasting.  we concern $A$-modules.}
\item Set $\tau_1(ae_{11}+be_{22})=a+b$ and $\tau_2(ae_{11}+be_{22})=a+2b$.
Write $\cdot_1,\cdot_2$ for the respective left $A$-actions transported from $\bbD(M)$ using \eqref{eq:dual-comparison}.
Calculate the actions of $e_{11},e_{22},e_{12}$ on $\varphi_0,\varphi_1$ for both forms.
Are the two actions equal?
\item Construct a graded $A$-module isomorphism
\[
t:(M^{\grstar},\cdot_1)\longrightarrow(M^{\grstar},\cdot_2)
\]
by giving $t(\varphi_0)$ and $t(\varphi_1)$.
\end{enumerate}
\end{exercise}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{advanced}
\begin{exercise}[Dependence of the action on the form]\label{ex:transported-dual-action}
Assume $\operatorname{char}\Bbbk\neq2$.
This exercise compares the $A$-actions transported through two symmetrising forms as in Remark~\ref{rem:transported-dual-action}.
Let $A=\Bbbk A_2$, $S=\Bbbk e_{11}\oplus\Bbbk e_{22}$, and $M=e_{11}A$.
For $c_1,c_2\in\Bbbk\setminus\{0\}$, define
\begin{equation}\label{eq:transported-dual-form}
\tau:S\longrightarrow\Bbbk,\qquad
a e_{11}+b e_{22}\longmapsto c_1a+c_2b
\quad(a,b\in\Bbbk).
\end{equation}
Consider the right $S$-linear maps
\begin{equation}\label{eq:transported-dual-functionals}
\begin{aligned}
\varphi_0:M&\longrightarrow S,& a e_{11}+b e_{12}&\longmapsto a e_{11},\\
\varphi_1:M&\longrightarrow S,& a e_{11}+b e_{12}&\longmapsto b e_{22}
\quad(a,b\in\Bbbk).
\end{aligned}
\end{equation}
\begin{enumerate}
\item Verify that $\tau$ is symmetrising and that $\varphi_0,\varphi_1$ form a homogeneous basis of $M^{\grstar}$. Determine their degrees.  
\item Set $\tau_1(ae_{11}+be_{22})=a+b$ and $\tau_2(ae_{11}+be_{22})=a+2b$.
Write $\cdot_1,\cdot_2$ for the respective left $A$-actions transported from $\bbD(M)$ using \eqref{eq:dual-comparison}.
Calculate the actions of $e_{11},e_{22},e_{12}$ on $\varphi_0,\varphi_1$ for both forms.
Are the two actions equal?
\item Construct a graded $A$-module isomorphism
\[
t:(M^{\grstar},\cdot_1)\longrightarrow(M^{\grstar},\cdot_2)
\]
by giving $t(\varphi_0)$ and $t(\varphi_1)$.
\end{enumerate}
\end{exercise}
\end{advanced}

```

</details>

---
