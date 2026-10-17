# Change Proposal 13: Lectures 1, 2, and 3

> **Status: revised following your feedback; awaiting approval. No TeX or PDF files have been changed.**

**Source snapshot:** 16 October 2026. **Latest revision:** 17 October 2026. Source line numbers refer to your current TeX files, before the proposed changes.

## Revisions Requested

| Replacement | Revised treatment |
| --- | --- |
| 1 | Keep the corollary statement verbatim. Change only its proof; add no separate left-module statement. |
| 2 | Keep the entire convention following the definition verbatim, including both items of your quoted block. Revise only the bimodule definition and its morphisms. |
| 4 | Give the actual map from a vector space tensored with the dual of the source to Hom, explain its meaning, and give its inverse in the finite-dimensional case. |
| 5 | Put the S-dual Hom description and evaluation/coevaluation immediately after the S-dual subsection in Lecture 1. Move only the short tensor-product definition forward; leave the general properties in Lecture 2. |
| 6 | Count composition factors of right modules; compute them using Hom from P_j=e_jA over the division algebra End_A(L_j). Collect h_{P_i} as the rows of h_A. Remove all bimodule dimension-vector notation and adjust the dependent tensor-counting formulas. |
| 7 | State the resulting Hilbert-series properties directly for graded A-modules and use composition-factor additivity. The dependent tensor-counting correction now belongs to Replacement 6. |

**Protected passages:** the corollary statement at [Lecture_Koszul_S1.tex:220](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:220) and the complete convention at [Lecture_Koszul_S1.tex:718](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:718) remain unchanged, including the original wording.

**Indexing convention:** use `(v_i)_{1\leq i\leq n}`, never `(v_i)_{i=1}^{n}`. This rule is saved in the math-discussion skill. It does not change the usual bounds on sums or products.

**Scope:** Lectures 1–3, the notation list, and the dependent Homework 1 corrections. Lectures 4–5 require no changes for the requested terminology or Hilbert-series convention.

## Reading This Proposal

Mechanical corrections list only the operation and the source line numbers. Content changes have line-by-line diffs: `-` marks removals, `+` marks additions. Full exact passages are available in the collapsible blocks.

The diff's new line numbers include the other proposed changes earlier in the same file. Replacement numbers are retained from the first version.

**Dependencies:** Replacements 4–5 form the linear and S-module versions of the Hom description. The two moves in Replacement 5 must be applied together, so the tensor-product definition appears once. The four passages in Replacement 6 belong together: the definition, notation list, tensor-counting formulas, and alternating-generator example. Replacement 7 gives the accompanying additivity correction. Replacement 10 keeps the homework comparison consistent with Replacement 9.

## Mechanical Corrections

| File | Current line numbers | Replacement |
| --- | --- | --- |
| [Lecture_Koszul.tex:353](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:353) | 353, 354 | Hilbert series: `H` to `h` (all occurrences on these lines). |
| [Lecture_Koszul_S2.tex:909](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:909) | 909, 1144, 1151 | Hilbert series: `H` to `h` (all occurrences on these lines). |
| [Lecture_Koszul_S3.tex:220](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:220) | 220, 235, 236, 237, 255, 256, 296, 372, 373, 375, 455, 461 | Hilbert series: `H` to `h` (all occurrences on these lines). |
| [Homework1.tex:280](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Homework1.tex:280) | 280, 288, 299, 376, 429, 431 | Hilbert series: `H` to `h` (all occurrences on these lines). |
| [Lecture_Koszul.tex:315](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:315) | 315 | `locally finite` to `locally finite-dimensional` in the notation list. |
| [Lecture_Koszul_S2.tex:683](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:683) | 683 | Remove the duplicated `-dimensional`. |

**Audit:** the Hilbert-series correction affects 23 source lines. Lecture 1 already consistently uses “locally finite-dimensional”; the remaining bare phrase is in the notation list, and Lecture 2 has one duplicated “-dimensional”. The relevant passages in Lectures 3–4 are already consistent, and Lecture 5 has no obsolete occurrence. Its homotopy symbols remain unchanged.

Historical proposals and reference documents are not part of the replacements.

## Comments Addressed

| Current comment location | Response |
| --- | --- |
| [Lecture_Koszul_S1.tex:225](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:225) | [Replacement 1](#replacement-1): explain the kernel complement without changing the statement. |
| [Lecture_Koszul_S1.tex:713](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:713) | [Replacement 2](#replacement-2): specify bimodule maps, preserving your convention. [Replacement 3](#replacement-3) gives the category identification's formula later, in supplementary material. |
| [Lecture_Koszul_S1.tex:924](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:924) | [Replacement 4](#replacement-4): explain the vector-space Hom identification. |
| [Lecture_Koszul_S1.tex:1130](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1130) | [Replacement 5](#replacement-5): add the S-module Hom identification and evaluation/coevaluation in Lecture 1. |
| [Lecture_Koszul_S2.tex:745](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:745), lines 753 and 784 | [Replacements 6–7](#replacement-6): count right-module composition factors with their degrees, compute them using Hom, and remove the bimodule dimension-vector notation. |
| [Lecture_Koszul_S3.tex:306](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:306) | [Replacement 8](#replacement-8): remove the algebra direct-sum subsection. |
| [Lecture_Koszul_S3.tex:345](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:345) | [Replacements 9–10](#replacement-9): make the tensor-product/sign material and the dependent comparison advanced. |

## Replacement Index

| No. | Content change | Added / removed |
| --- | --- | --- |
| 1 | [Make the direct-summand argument explicit](#replacement-1) | +4 / -1 |
| 2 | [Specify bimodule maps; preserve the convention verbatim](#replacement-2) | +5 / -5 |
| 3 | [Explain the bimodule-category identification after its algebra multiplication](#replacement-3) | +11 / -1 |
| 4 | [Explain the vector-space Hom and dual identification](#replacement-4) | +24 / -1 |
| 5 | [Place Hom, evaluation, and coevaluation immediately after S-duals](#replacement-5) | +93 / -13 |
| 6 | [Count composition factors degree by degree](#replacement-6) | +72 / -84 |
| 7 | [Use composition-factor additivity in the Hilbert-series properties](#replacement-7) | +2 / -2 |
| 8 | [Remove the algebra direct-sum subsection](#replacement-8) | +0 / -39 |
| 9 | [Make tensor products and signs entirely advanced](#replacement-9) | +5 / -4 |
| 10 | [Keep the homework tensor-product comparison optional](#replacement-10) | +5 / -2 |

## Placement

The vector-space Hom description follows the linear-dual discussion. The S-module Hom description and evaluation/coevaluation follow the S-dual subsection immediately, before comparing the different duals. Only the brief definition of tensor products over an algebra moves from Lecture 2; their universal property and other general properties remain there.

The BGS source is the last two paragraphs of Section 2.7, printed pp. 484–485, in the [local paper](</Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/[BGS] Koszul duality patterns in representation theory.pdf>). Citations in the proposed notes remain inside advanced material.

Lecture 3's tensor-product/sign subsection is not used by the current Lectures 4–5. The plan returns to tensor products of Koszul algebras in Lecture 8, so the subsection remains available as advanced material.

---

<a id="replacement-1"></a>

## Replacement 1: Make the direct-summand argument explicit

Keep the corollary statement verbatim, as requested. Change only the proof, showing explicitly that a complement of the kernel maps isomorphically onto the quotient. Do not add a separate left-module statement.

**Location:** [Lecture_Koszul_S1.tex:224](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:224) (current lines 224–226)  
**Change size:** 4 lines added; 1 line removed.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -224,3 +224,6 @@
 \begin{proof}
-A finite generating set gives a surjection $S^{\oplus n}\onto M$. By Theorem~\ref{thm:artin-wedderburn}, its kernel has a complement, which maps isomorphically onto $M$. \comm{what is this talking about?? we need kernel to be direct summand of $S^{\oplus n}$??}
+Choose a surjection $p:S^{\oplus n}\onto M$.
+By Theorem~\ref{thm:artin-wedderburn}, there is a submodule $L$ such that $S^{\oplus n}=\Ker p\oplus L$.
+The restriction $p|_L:L\to M$ has kernel $L\cap\Ker p=0$ and image $p(L)=p(S^{\oplus n})=M$.
+Hence $L\cong M$, so $S^{\oplus n}\cong\Ker p\oplus M$.
 \end{proof}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\begin{proof}
A finite generating set gives a surjection $S^{\oplus n}\onto M$. By Theorem~\ref{thm:artin-wedderburn}, its kernel has a complement, which maps isomorphically onto $M$. \comm{what is this talking about?? we need kernel to be direct summand of $S^{\oplus n}$??}
\end{proof}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{proof}
Choose a surjection $p:S^{\oplus n}\onto M$.
By Theorem~\ref{thm:artin-wedderburn}, there is a submodule $L$ such that $S^{\oplus n}=\Ker p\oplus L$.
The restriction $p|_L:L\to M$ has kernel $L\cap\Ker p=0$ and image $p(L)=p(S^{\oplus n})=M$.
Hence $L\cong M$, so $S^{\oplus n}\cong\Ker p\oplus M$.
\end{proof}
```

</details>

---

<a id="replacement-2"></a>

## Replacement 2: Specify bimodule maps; preserve the convention verbatim

Revise only the definition and its account of morphisms. The entire following convention, including both items of the author's itemize block, stays byte-for-byte unchanged.

**Location:** [Lecture_Koszul_S1.tex:710](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:710) (current lines 710–716)  
**Change size:** 5 lines added; 5 lines removed.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -710,7 +713,7 @@
 \begin{definition}\label{def:bimodule}
-For $\Bbbk$-algebras $B,C$, we say that $M$ is a \defn{left $B$ right $C$ bimodule}, or simply \defn{$(B,C)$-bimodule}, if it is a vector space equipped with commuting left $B$-action and right $C$-action, i.e. $(bm)c=b(mc)$ for all $b\in B$, $c\in C$, and $m\in M$.
-When $B=C=A$, we simply call $M$ an \defn{$A$-bimodule}.
-\comm{check}
-A homomorphism of bimodule is a homorphism of both left $B$-module and right $C$-module.
-For graded $B,C$, a bimodule $M$ is \defn{graded} if $M=\bigoplus_{i\in \Z}M_i$ as vector space and $B_iM_jC_k\subset M_{i+j+k}$ for all $i,j,k\in\Z$.   Homomorphisms of graded bimodules are defined analogously.
+For $\Bbbk$-algebras $B,C$, a \defn{bimodule} $ {}_BM_C$ is a vector space with $\Bbbk$-bilinear left $B$- and right $C$-module actions satisfying $(bm)c=b(mc)$ for all $b\in B$, $c\in C$, and $m\in M$.
+The subscripts indicate the left and right acting algebras; when $B=C=A$, we call $M$ an \defn{$A$-bimodule}.
+A \defn{bimodule homomorphism} $f:{}_BM_C\to{}_BN_C$ is a linear map satisfying $f(bmc)=bf(m)c$ for all $b\in B$, $c\in C$, and $m\in M$.
+For graded $B,C$, a bimodule $M$ is \defn{graded} if $M=\bigoplus_{i\in\Z}M_i$ and $B_iM_jC_k\subset M_{i+j+k}$ for all $i,j,k\in\Z$.
+A \defn{graded bimodule homomorphism} is a bimodule homomorphism $f:M\to N$ satisfying $f(M_i)\subset N_i$ for all $i\in\Z$.
 \end{definition}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\begin{definition}\label{def:bimodule}
For $\Bbbk$-algebras $B,C$, we say that $M$ is a \defn{left $B$ right $C$ bimodule}, or simply \defn{$(B,C)$-bimodule}, if it is a vector space equipped with commuting left $B$-action and right $C$-action, i.e. $(bm)c=b(mc)$ for all $b\in B$, $c\in C$, and $m\in M$.
When $B=C=A$, we simply call $M$ an \defn{$A$-bimodule}.
\comm{check}
A homomorphism of bimodule is a homorphism of both left $B$-module and right $C$-module.
For graded $B,C$, a bimodule $M$ is \defn{graded} if $M=\bigoplus_{i\in \Z}M_i$ as vector space and $B_iM_jC_k\subset M_{i+j+k}$ for all $i,j,k\in\Z$.   Homomorphisms of graded bimodules are defined analogously.
\end{definition}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{definition}\label{def:bimodule}
For $\Bbbk$-algebras $B,C$, a \defn{bimodule} $ {}_BM_C$ is a vector space with $\Bbbk$-bilinear left $B$- and right $C$-module actions satisfying $(bm)c=b(mc)$ for all $b\in B$, $c\in C$, and $m\in M$.
The subscripts indicate the left and right acting algebras; when $B=C=A$, we call $M$ an \defn{$A$-bimodule}.
A \defn{bimodule homomorphism} $f:{}_BM_C\to{}_BN_C$ is a linear map satisfying $f(bmc)=bf(m)c$ for all $b\in B$, $c\in C$, and $m\in M$.
For graded $B,C$, a bimodule $M$ is \defn{graded} if $M=\bigoplus_{i\in\Z}M_i$ and $B_iM_jC_k\subset M_{i+j+k}$ for all $i,j,k\in\Z$.
A \defn{graded bimodule homomorphism} is a bimodule homomorphism $f:M\to N$ satisfying $f(M_i)\subset N_i$ for all $i\in\Z$.
\end{definition}
```

</details>

---

<a id="replacement-3"></a>

## Replacement 3: Explain the bimodule-category identification after its algebra multiplication

Add the multiplication and the right action underlying the category identification in the existing supplementary block. This is an explanation of the author's retained convention, not a replacement or relocation of that convention.

**Location:** [Lecture_Koszul_S1.tex:767](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:767) (current lines 767–768)  
**Change size:** 11 lines added; 1 line removed.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -767,2 +770,12 @@
-Thus $\Mod A^\en$ is also the category of $A$-bimodules and maps preserving both actions.
+Thus $A\Mod A$ is identified with $\Mod A^\en$.
+More generally, for $\Bbbk$-algebras $B,C$, the vector space $C\otimes_\Bbbk B^\op$ is an algebra with
+\[
+(c\otimes b^\op)(c'\otimes(b')^\op)=cc'\otimes(b'b)^\op,
+\qquad 1=1_C\otimes1_B^\op.
+\]
+The same construction identifies the categories
+\[
+B\Mod C\simeq\Mod(C\otimes_\Bbbk B^\op),
+\qquad m\cdot(c\otimes b^\op)=bmc.
+\]
 \end{supplementary}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
Thus $\Mod A^\en$ is also the category of $A$-bimodules and maps preserving both actions.
\end{supplementary}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
Thus $A\Mod A$ is identified with $\Mod A^\en$.
More generally, for $\Bbbk$-algebras $B,C$, the vector space $C\otimes_\Bbbk B^\op$ is an algebra with
\[
(c\otimes b^\op)(c'\otimes(b')^\op)=cc'\otimes(b'b)^\op,
\qquad 1=1_C\otimes1_B^\op.
\]
The same construction identifies the categories
\[
B\Mod C\simeq\Mod(C\otimes_\Bbbk B^\op),
\qquad m\cdot(c\otimes b^\op)=bmc.
\]
\end{supplementary}
```

</details>

---

<a id="replacement-4"></a>

## Replacement 4: Explain the vector-space Hom and dual identification

Replace the first BGS comment with the actual linear-algebra statement and its elementary inverse, rather than a forward reference. The second BGS comment is addressed by Replacement 5, directly after the S-dual subsection.

**Location:** [Lecture_Koszul_S1.tex:924](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:924) (current lines 924–926)  
**Change size:** 24 lines added; 1 line removed.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -924,3 +937,26 @@
-\comm{there should be contents related to the last 2 paragraphs of BGS subsec 2.7 here}
+For vector spaces $V,W$, a functional $f\in D(V)$ and a vector $w\in W$ define a linear map $V\to W$, $v\mapsto f(v)w$.
+Finite sums of these maps give the following description of Hom.
 
+\begin{proposition}\label{prop:linear-Hom-tensor}
+For vector spaces $V,W$, there is a natural linear map
+\begin{equation}\label{eq:linear-Hom-tensor}
+W\otimes_\Bbbk D(V)\longrightarrow\Hom_\Bbbk(V,W),
+\qquad w\otimes f\longmapsto\bigl(v\mapsto f(v)w\bigr).
+\end{equation}
+It is an isomorphism if either $V$ or $W$ is finite-dimensional.
+\end{proposition}
+
+\begin{supplementary}
+\begin{proof}
+If $V$ has a finite basis $\{v_i\mid 1\leq i\leq n\}$ with dual basis $\{v_i^*\mid 1\leq i\leq n\}$, the inverse of \eqref{eq:linear-Hom-tensor} is
+\[
+\Hom_\Bbbk(V,W)\longrightarrow W\otimes_\Bbbk D(V),
+\qquad F\longmapsto\sum_{i=1}^nF(v_i)\otimes v_i^*,
+\]
+since $v=\sum_{i=1}^n v_i^*(v)v_i$.
+If instead $W$ has a finite basis $\{w_j\mid 1\leq j\leq m\}$, write $F(v)=\sum_{j=1}^m f_j(v)w_j$; the uniquely determined coordinate functionals $f_j\in D(V)$ give the inverse $F\mapsto\sum_{j=1}^m w_j\otimes f_j$.
+The formulas commute with precomposition and postcomposition, so the comparison is natural.
+\end{proof}
+\end{supplementary}
+
 \subsection{\texorpdfstring{Left, right, and two-sided duals over $S$}{Left, right, and two-sided duals over S}}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\comm{there should be contents related to the last 2 paragraphs of BGS subsec 2.7 here}

\subsection{\texorpdfstring{Left, right, and two-sided duals over $S$}{Left, right, and two-sided duals over S}}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
For vector spaces $V,W$, a functional $f\in D(V)$ and a vector $w\in W$ define a linear map $V\to W$, $v\mapsto f(v)w$.
Finite sums of these maps give the following description of Hom.

\begin{proposition}\label{prop:linear-Hom-tensor}
For vector spaces $V,W$, there is a natural linear map
\begin{equation}\label{eq:linear-Hom-tensor}
W\otimes_\Bbbk D(V)\longrightarrow\Hom_\Bbbk(V,W),
\qquad w\otimes f\longmapsto\bigl(v\mapsto f(v)w\bigr).
\end{equation}
It is an isomorphism if either $V$ or $W$ is finite-dimensional.
\end{proposition}

\begin{supplementary}
\begin{proof}
If $V$ has a finite basis $\{v_i\mid 1\leq i\leq n\}$ with dual basis $\{v_i^*\mid 1\leq i\leq n\}$, the inverse of \eqref{eq:linear-Hom-tensor} is
\[
\Hom_\Bbbk(V,W)\longrightarrow W\otimes_\Bbbk D(V),
\qquad F\longmapsto\sum_{i=1}^nF(v_i)\otimes v_i^*,
\]
since $v=\sum_{i=1}^n v_i^*(v)v_i$.
If instead $W$ has a finite basis $\{w_j\mid 1\leq j\leq m\}$, write $F(v)=\sum_{j=1}^m f_j(v)w_j$; the uniquely determined coordinate functionals $f_j\in D(V)$ give the inverse $F\mapsto\sum_{j=1}^m w_j\otimes f_j$.
The formulas commute with precomposition and postcomposition, so the comparison is natural.
\end{proof}
\end{supplementary}

\subsection{\texorpdfstring{Left, right, and two-sided duals over $S$}{Left, right, and two-sided duals over S}}
```

</details>

---

<a id="replacement-5"></a>

## Replacement 5: Place Hom, evaluation, and coevaluation immediately after S-duals

Put the S-module Hom formulas and evaluation/coevaluation in Lecture 1, immediately after the S-dual subsection. Move the short definition of tensor products over an algebra from Lecture 2 to the beginning of this passage, preserving its label. Keep the general tensor-product properties in Lecture 2. The proofs use the defining quotient and the already established finite-free-summand result, not statements from a later lecture. Retain the graded refinement after the total grading has been introduced.

### Passage 1

**Location:** [Lecture_Koszul_S1.tex:1130](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1130) (current lines 1130–1132)  
**Change size:** 88 lines added; 1 line removed.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -1130,3 +1166,90 @@
-\comm{there should be contents related to the last 2 paragraphs of BGS subsec 2.7 here}
+\subsection{Hom spaces and evaluation}
 
+For the $S$-module version of \eqref{eq:linear-Hom-tensor}, we need tensor products over an algebra.
+Let $A$ be any $\Bbbk$-algebra, $M$ a right $A$-module, and $N$ a left $A$-module.
+
+\begin{definition}\label{def:module-tensor}
+The \defn{tensor product of $M$ and $N$ over $A$}, denoted $M\otimes_A N$, is the quotient of the vector space $M\otimes_\Bbbk N$ by
+\[
+\operatorname{span}_\Bbbk\{ma\otimes n-m\otimes an\mid m\in M,\ n\in N,\ a\in A\}.
+\]
+\end{definition}
+
+Write $m\otimes_A n$, or simply $m\otimes n$, for the image of $m\otimes n$ in this quotient.
+Thus $ma\otimes_A n=m\otimes_A an$ for all $m\in M$, $n\in N$, and $a\in A$.
+
+\begin{proposition}\label{prop:hom-from-S-duals}
+Let $S$ be finite-dimensional semisimple.
+For right $S$-modules $V,W$, and respectively left $S$-modules $V,W$, there are natural linear maps
+\begin{equation}\label{eq:hom-from-S-duals}
+\begin{aligned}
+W\otimes_S V^*&\longrightarrow\Hom_S(V,W),
+& w\otimes f&\longmapsto\bigl(v\mapsto wf(v)\bigr),\\
+{}^*V\otimes_S W&\longrightarrow\Hom_{S^\op}(V,W),
+& g\otimes w&\longmapsto\bigl(v\mapsto g(v)w\bigr).
+\end{aligned}
+\end{equation}
+Each map is an isomorphism if either $V$ or $W$ is finite-dimensional.
+For bimodules $ {}_SV_S$, $ {}_SW_S$, both maps preserve the outer actions on Hom, given for $s,t\in S$ and $v\in V$ by
+\[
+\begin{aligned}
+(sFt)(v)&=sF(tv)&&\text{for }F\in\Hom_S(V,W),\\
+(sFt)(v)&=F(vs)t&&\text{for }F\in\Hom_{S^\op}(V,W).
+\end{aligned}
+\]
+\end{proposition}
+
+\begin{supplementary}
+\begin{proof}
+For the first map in \eqref{eq:hom-from-S-duals}, the identities $(ws)f(v)=w(sf)(v)$ and $wf(vs)=wf(v)s$ give a well-defined map with right $S$-linear values.
+If $V=S$, evaluation at $1$ identifies the map with $W\otimes_S S\to W$, whose inverse is $w\mapsto w\otimes1$.
+If $W=S$, the map is $S\otimes_S V^*\to V^*$, whose inverse is $f\mapsto1\otimes f$.
+Distributing finite direct sums in the defining quotient and in Hom shows that the comparison is an isomorphism when either variable is a finite sum of copies of $S$.
+Restriction to a direct summand and Corollary~\ref{cor:semisimple-summands} give the assertion when either variable is finite-dimensional.
+Passing to $S^\op$ proves the assertion for the second map in \eqref{eq:hom-from-S-duals}.
+Precomposition and postcomposition commute with the formulas, proving naturality and compatibility with the outer actions.
+\end{proof}
+\end{supplementary}
+
+Evaluation applies a functional to an element.
+Coevaluation expresses the identity endomorphism as an element of a tensor product.
+
+\begin{proposition}\label{prop:S-evaluation-coevaluation}
+For a bimodule $ {}_SV_S$, where $S$ is finite-dimensional semisimple, evaluation gives bimodule maps
+\begin{equation}\label{eq:S-evaluation-pairings}
+\begin{aligned}
+V^*\otimes_S V&\longrightarrow S,& f\otimes v&\longmapsto f(v),\\
+V\otimes_S{}^*V&\longrightarrow S,& v\otimes g&\longmapsto g(v).
+\end{aligned}
+\end{equation}
+If $V$ is finite-dimensional, the \defn{coevaluation maps} are
+\begin{equation}\label{eq:S-coevaluation}
+\begin{aligned}
+S&\longrightarrow V\otimes_S V^*\xrightarrow{\sim}\End_S(V),
+& s&\longmapsto\bigl(v\mapsto sv\bigr),\\
+S&\longrightarrow{}^*V\otimes_S V\xrightarrow{\sim}\End_{S^\op}(V),
+& s&\longmapsto\bigl(v\mapsto vs\bigr).
+\end{aligned}
+\end{equation}
+The isomorphisms are those in \eqref{eq:hom-from-S-duals}, with $W=V$.
+Both coevaluation maps are bimodule maps, and each image of $1$ corresponds to $\id_V$.
+\end{proposition}
+
+\begin{supplementary}
+\begin{proof}
+The identities $(fs)(v)=f(sv)$ and $(sg)(v)=g(vs)$ from \eqref{eq:bimodule-dual-actions} make evaluation well-defined on the two tensor products; the other two actions give its bimodule linearity.
+For coevaluation, left multiplication is right $S$-linear and right multiplication is left $S$-linear because the two actions on $V$ commute.
+Under the Hom actions in Proposition~\ref{prop:hom-from-S-duals}, both multiplication assignments preserve the two $S$-actions.
+The isomorphisms in \eqref{eq:hom-from-S-duals} therefore give the stated bimodule maps.
+\end{proof}
+\end{supplementary}
+
+\begin{advanced}
+These are the constructions in the last two paragraphs of \cite[\S2.7, pp.~484--485]{BGS96}, translated to our notation.
+
+For a locally finite-dimensional graded bimodule $ {}_SV_S$, \eqref{eq:S-coevaluation} applies to each $V_d$; a coevaluation for the whole module need not exist.
+For example, take $S\neq0$ and $V=\bigoplus_{d\geq0}S(-d)$.
+Every element $\sum_{i=1}^n v_i\otimes f_i$ of $V\otimes_S V^{\grstar}$ defines an endomorphism with image contained in the finite-dimensional submodule $\sum_{i=1}^n v_iS$, so it cannot represent $\id_V$.
+\end{advanced}
+
 \subsection{Comparing the duals}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\comm{there should be contents related to the last 2 paragraphs of BGS subsec 2.7 here}

\subsection{Comparing the duals}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\subsection{Hom spaces and evaluation}

For the $S$-module version of \eqref{eq:linear-Hom-tensor}, we need tensor products over an algebra.
Let $A$ be any $\Bbbk$-algebra, $M$ a right $A$-module, and $N$ a left $A$-module.

\begin{definition}\label{def:module-tensor}
The \defn{tensor product of $M$ and $N$ over $A$}, denoted $M\otimes_A N$, is the quotient of the vector space $M\otimes_\Bbbk N$ by
\[
\operatorname{span}_\Bbbk\{ma\otimes n-m\otimes an\mid m\in M,\ n\in N,\ a\in A\}.
\]
\end{definition}

Write $m\otimes_A n$, or simply $m\otimes n$, for the image of $m\otimes n$ in this quotient.
Thus $ma\otimes_A n=m\otimes_A an$ for all $m\in M$, $n\in N$, and $a\in A$.

\begin{proposition}\label{prop:hom-from-S-duals}
Let $S$ be finite-dimensional semisimple.
For right $S$-modules $V,W$, and respectively left $S$-modules $V,W$, there are natural linear maps
\begin{equation}\label{eq:hom-from-S-duals}
\begin{aligned}
W\otimes_S V^*&\longrightarrow\Hom_S(V,W),
& w\otimes f&\longmapsto\bigl(v\mapsto wf(v)\bigr),\\
{}^*V\otimes_S W&\longrightarrow\Hom_{S^\op}(V,W),
& g\otimes w&\longmapsto\bigl(v\mapsto g(v)w\bigr).
\end{aligned}
\end{equation}
Each map is an isomorphism if either $V$ or $W$ is finite-dimensional.
For bimodules $ {}_SV_S$, $ {}_SW_S$, both maps preserve the outer actions on Hom, given for $s,t\in S$ and $v\in V$ by
\[
\begin{aligned}
(sFt)(v)&=sF(tv)&&\text{for }F\in\Hom_S(V,W),\\
(sFt)(v)&=F(vs)t&&\text{for }F\in\Hom_{S^\op}(V,W).
\end{aligned}
\]
\end{proposition}

\begin{supplementary}
\begin{proof}
For the first map in \eqref{eq:hom-from-S-duals}, the identities $(ws)f(v)=w(sf)(v)$ and $wf(vs)=wf(v)s$ give a well-defined map with right $S$-linear values.
If $V=S$, evaluation at $1$ identifies the map with $W\otimes_S S\to W$, whose inverse is $w\mapsto w\otimes1$.
If $W=S$, the map is $S\otimes_S V^*\to V^*$, whose inverse is $f\mapsto1\otimes f$.
Distributing finite direct sums in the defining quotient and in Hom shows that the comparison is an isomorphism when either variable is a finite sum of copies of $S$.
Restriction to a direct summand and Corollary~\ref{cor:semisimple-summands} give the assertion when either variable is finite-dimensional.
Passing to $S^\op$ proves the assertion for the second map in \eqref{eq:hom-from-S-duals}.
Precomposition and postcomposition commute with the formulas, proving naturality and compatibility with the outer actions.
\end{proof}
\end{supplementary}

Evaluation applies a functional to an element.
Coevaluation expresses the identity endomorphism as an element of a tensor product.

\begin{proposition}\label{prop:S-evaluation-coevaluation}
For a bimodule $ {}_SV_S$, where $S$ is finite-dimensional semisimple, evaluation gives bimodule maps
\begin{equation}\label{eq:S-evaluation-pairings}
\begin{aligned}
V^*\otimes_S V&\longrightarrow S,& f\otimes v&\longmapsto f(v),\\
V\otimes_S{}^*V&\longrightarrow S,& v\otimes g&\longmapsto g(v).
\end{aligned}
\end{equation}
If $V$ is finite-dimensional, the \defn{coevaluation maps} are
\begin{equation}\label{eq:S-coevaluation}
\begin{aligned}
S&\longrightarrow V\otimes_S V^*\xrightarrow{\sim}\End_S(V),
& s&\longmapsto\bigl(v\mapsto sv\bigr),\\
S&\longrightarrow{}^*V\otimes_S V\xrightarrow{\sim}\End_{S^\op}(V),
& s&\longmapsto\bigl(v\mapsto vs\bigr).
\end{aligned}
\end{equation}
The isomorphisms are those in \eqref{eq:hom-from-S-duals}, with $W=V$.
Both coevaluation maps are bimodule maps, and each image of $1$ corresponds to $\id_V$.
\end{proposition}

\begin{supplementary}
\begin{proof}
The identities $(fs)(v)=f(sv)$ and $(sg)(v)=g(vs)$ from \eqref{eq:bimodule-dual-actions} make evaluation well-defined on the two tensor products; the other two actions give its bimodule linearity.
For coevaluation, left multiplication is right $S$-linear and right multiplication is left $S$-linear because the two actions on $V$ commute.
Under the Hom actions in Proposition~\ref{prop:hom-from-S-duals}, both multiplication assignments preserve the two $S$-actions.
The isomorphisms in \eqref{eq:hom-from-S-duals} therefore give the stated bimodule maps.
\end{proof}
\end{supplementary}

\begin{advanced}
These are the constructions in the last two paragraphs of \cite[\S2.7, pp.~484--485]{BGS96}, translated to our notation.

For a locally finite-dimensional graded bimodule $ {}_SV_S$, \eqref{eq:S-coevaluation} applies to each $V_d$; a coevaluation for the whole module need not exist.
For example, take $S\neq0$ and $V=\bigoplus_{d\geq0}S(-d)$.
Every element $\sum_{i=1}^n v_i\otimes f_i$ of $V\otimes_S V^{\grstar}$ defines an endomorphism with image contained in the finite-dimensional submodule $\sum_{i=1}^n v_iS$, so it cannot represent $\id_V$.
\end{advanced}

\subsection{Comparing the duals}
```

</details>

### Passage 2

**Location:** [Lecture_Koszul_S2.tex:12](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:12) (current lines 12–23)  
**Change size:** 2 lines added; 12 lines removed.

Replace the moved definition with a short recall; the following lemma and all percent-commented lines stay in Lecture 2.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -12,12 +12,2 @@
-Let $A$ be any $\Bbbk$-algebra, $M$ a right $A$-module, and $N$ a left $A$-module.
-The tensor product over $A$ imposes the identities $ma\otimes n=m\otimes an$ for $m\in M$, $n\in N$, and $a\in A$.
-
-\begin{definition}\label{def:module-tensor}
-The \defn{tensor product of $M$ and $N$ over $A$}, denoted $M\otimes_A N$, is the quotient of the vector space $M\otimes_\Bbbk N$ by
-\[
-\operatorname{span}_\Bbbk\{ma\otimes n-m\otimes an\mid m\in M,\ n\in N,\ a\in A\}.
-\]
-\end{definition}
-
-
-By abuse of notation, we write $m\otimes n$ for the its own image in the $M\otimes_\Bbbk N \to M\otimes_AN$; if clarity is needed, then we will write $m\otimes_A n$.
+Recall the tensor product $M\otimes_A N$ from Definition~\ref{def:module-tensor}, for a right $A$-module $M$ and a left $A$-module $N$.
+Its defining identity is $ma\otimes_A n=m\otimes_A an$ for all $m\in M$, $n\in N$, and $a\in A$.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
Let $A$ be any $\Bbbk$-algebra, $M$ a right $A$-module, and $N$ a left $A$-module.
The tensor product over $A$ imposes the identities $ma\otimes n=m\otimes an$ for $m\in M$, $n\in N$, and $a\in A$.

\begin{definition}\label{def:module-tensor}
The \defn{tensor product of $M$ and $N$ over $A$}, denoted $M\otimes_A N$, is the quotient of the vector space $M\otimes_\Bbbk N$ by
\[
\operatorname{span}_\Bbbk\{ma\otimes n-m\otimes an\mid m\in M,\ n\in N,\ a\in A\}.
\]
\end{definition}


By abuse of notation, we write $m\otimes n$ for the its own image in the $M\otimes_\Bbbk N \to M\otimes_AN$; if clarity is needed, then we will write $m\otimes_A n$.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
Recall the tensor product $M\otimes_A N$ from Definition~\ref{def:module-tensor}, for a right $A$-module $M$ and a left $A$-module $N$.
Its defining identity is $ma\otimes_A n=m\otimes_A an$ for all $m\in M$, $n\in N$, and $a\in A$.
```

</details>

### Passage 3

**Location:** [Lecture_Koszul_S2.tex:839](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:839)  
**Change size:** 3 lines added; 0 lines removed.

Keep only the graded refinement here, after the total grading has been defined.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -839,1 +816,4 @@
 When $M,N$ are locally finite-dimensional and bounded below, only finitely many pairs $(p,q)$ contribute in a fixed degree, so the tensor product is locally finite-dimensional and bounded below.
+
+For a finite-dimensional graded bimodule $ {}_SV_S$, use $V^{\grstar}$ and $ {}^{\grstar}V$ in Proposition~\ref{prop:S-evaluation-coevaluation}.
+With the total grading, evaluation and coevaluation preserve degree: evaluation pairs degrees $i$ and $-i$, and $\id_V$ has degree $0$.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
When $M,N$ are locally finite-dimensional and bounded below, only finitely many pairs $(p,q)$ contribute in a fixed degree, so the tensor product is locally finite-dimensional and bounded below.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
When $M,N$ are locally finite-dimensional and bounded below, only finitely many pairs $(p,q)$ contribute in a fixed degree, so the tensor product is locally finite-dimensional and bounded below.

For a finite-dimensional graded bimodule $ {}_SV_S$, use $V^{\grstar}$ and $ {}^{\grstar}V$ in Proposition~\ref{prop:S-evaluation-coevaluation}.
With the total grading, evaluation and coevaluation preserve degree: evaluation pairs degrees $i$ and $-i$, and $\id_V$ has degree $0$.
```

</details>

---

<a id="replacement-6"></a>

## Replacement 6: Count composition factors degree by degree

Define Hilbert series solely by composition multiplicities of right modules. Keep the notes' notation L_j for the simple modules (called S_j in our discussion), choose P_j=e_jA, and compute each coefficient as the dimension of Hom_A(P_j,M_d) over End_A(L_j). The algebra series collects the series h_{P_i} as rows. Remove the bimodule dimension-vector definition and its notation-list entry. Update the dependent tensor-counting lemma and examples using right-module multiplicities, without introducing a replacement bimodule invariant.

### Passage 1

**Location:** [Lecture_Koszul_S2.tex:740](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:740) (current lines 740–809)  
**Change size:** 45 lines added; 58 lines removed.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -740,70 +730,57 @@
-Fix a finite-dimensional semisimple $\Bbbk$-algebra $S$, concentrated in degree $0$.
-We record dimensions relative to all simple right $S$-modules.
-We define module series first, then collect them in an array for a graded algebra.
-
-\begin{definition}\label{def:dimension-vector}
-\comm{why do $S$-module.  It should be do-able for any $A$-module???  If needed, can just assume $A$ is lfd graded algebra.}
-Choose representatives $L_1,\ldots,L_r$ of the isomorphism classes of simple right $S$-modules.
-For a finite-dimensional right $S$-module $M$, write, with $m_j\in\Z_{\geq0}$,
-\[
-M\cong\bigoplus_{j=1}^r L_j^{\oplus m_j},
-\qquad \dimvec M:=(m_1,\ldots,m_r).
-\]
-The row vector $\dimvec M$ is the \defn{dimension vector} of $M$.
-\comm{we don't use bimodule???}
-For a finite-dimensional bimodule ${}_SU_S$, arrange the vectors $\dimvec(L_i\otimes_S U)$ as rows:
-\[
-\dimvec U=(u_{ij})_{1\leq i,j\leq r},
-\qquad (\dimvec U)_{ij}:=\bigl(\dimvec(L_i\otimes_S U)\bigr)_j.
-\]
-Thus $L_i\otimes_S U\cong\bigoplus_{j=1}^rL_j^{\oplus u_{ij}}$.
-\end{definition}
-
-The decompositions exist by Theorem~\ref{thm:artin-wedderburn}.
-Their multiplicities are unique: a non-zero homomorphism between simple modules is an isomorphism, since its kernel and image are submodules.
-Consequently
+Let $A$ be a locally finite-dimensional graded algebra with $S=A_0$ finite-dimensional semisimple.
+Each degree piece of a graded right $A$-module $M$ is naturally an $A$-module:
 \[
-m_j=\frac{\dim_\Bbbk\Hom_S(L_j,M)}{\dim_\Bbbk\End_S(L_j)},
+M_d\cong M_{\geq d}/M_{\geq d+1},
+\qquad M_{\geq d}:=\bigoplus_{j\geq d}M_j.
 \]
-and the same formula applies to each $L_i\otimes_S U$.
-In particular, the dimension data do not depend on choices of decompositions.
-For the $S$-bimodule $S$, we have $\dimvec S=I_r$, the $r\times r$ identity array.
+The action on $M_d$ factors through $A/A_+=S$, so $M_d$ is semisimple.
+The simple summands in a direct sum decomposition of $M_d$ are its \defn{composition factors}.
 
-\begin{example}\label{ex:dimension-vector-coordinate}
-If $S=\bigoplus_{i=1}^r\Bbbk e_i$ with coordinate idempotents, take $L_i=e_iS$.
-Then
-\[
-\dimvec M=(\dim_\Bbbk Me_j)_{1\le j\le r},
-\qquad (\dimvec U)_{ij}=\dim_\Bbbk(e_iUe_j).
-\]
-Indeed, $L_i\otimes_S U\cong e_iU$ by multiplication, and the multiplicity of $e_jS$ in $e_iU$ is $\dim_\Bbbk(e_iUe_j)$.
-For $S=\Bbbk$, the dimension vector has one entry, the usual vector space dimension.
-\end{example}
+By Theorem~\ref{thm:artin-wedderburn}, choose primitive idempotents $e_1,\ldots,e_r\in S$ so that $L_j:=e_jS$ represents each isomorphism class of simple right $S$-modules once.
+Then $L_j\cong e_jA/e_jA_+$ is a graded simple $A$-module.
+\phantomsection\label{not:hilbert-simples-summands}
 
-\begin{definition}\label{def:hilbert-series}
-\comm{why this definition is separated with graded $S$-modules first then graded $A$ modules.  It can be just with graded $A$-modules from the get go?? }
-Let $M=\bigoplus_{d\in\Z}M_d$ be a locally finite-dimensional graded right $S$-module, with $M_d=0$ for all sufficiently negative $d$.
-Its \defn{Hilbert series} is
+\begin{definition}\label{def:dimension-vector}\label{def:hilbert-series}
+For a locally finite-dimensional graded right $A$-module $M$, write $[M_d:L_j]$ for the multiplicity of $L_j$ in $M_d$.
+Its degree $d$ \defn{dimension vector} is the row vector
 \[
-h_M(t):=\sum_{d\in\Z}(\dimvec M_d)t^d.
+\dimvec M_d:=\bigl([M_d:L_j]\bigr)_{1\leq j\leq r}.
 \]
-For a locally finite-dimensional graded algebra $A$ with $A_0=S$, its \defn{Hilbert series} records the preceding module series row by row:
+The module $M$ is \defn{bounded below} if $M_d=0$ for all sufficiently negative $d$.
+For such $M$, its \defn{Hilbert series} is
 \[
-h_A(t)_{ij}:=\bigl(h_{L_i\otimes_S A}(t)\bigr)_j
-\quad(1\leq i,j\leq r),
-\qquad
-h_A(t)=\sum_{d\geq0}(\dimvec A_d)t^d.
+h_M(t):=\sum_{d\in\Z}(\dimvec M_d)t^d
+=\sum_{d\in\Z}\bigl([M_d:L_j]\bigr)_{1\leq j\leq r}t^d.
 \]
-Here each $L_i$ is placed in degree $0$, and $L_i\otimes_S A$ is regarded as a right $S$-module by restriction.
-In particular, $h_A(0)=I_r$.
-For $S=\bigoplus_{i=1}^r\Bbbk e_i$, this gives
+For $P_i:=e_iA$, the \defn{Hilbert series} of the algebra $A$ collects the right-module series $h_{P_i}(t)$ as rows:
 \[
-h_A(t)_{ij}=\sum_{d\geq0}\dim_\Bbbk(e_iA_de_j)t^d
-\quad(1\leq i,j\leq r).
+h_A(t)_{ij}:=\bigl(h_{P_i}(t)\bigr)_j
+=\sum_{d\geq0}[(P_i)_d:L_j]t^d
+\quad\text{for all }1\leq i,j\leq r.
 \]
 \end{definition}
 
-The entries are formal Laurent series with integer coefficients; for algebras they are formal power series.
-A finite-dimensional graded module or algebra gives a Laurent polynomial or polynomial, respectively.
-No numerical convergence is required: a coefficient is specified degree by degree.
-For an algebra, keeping both indices records where products can be formed.
+Thus the coefficients count composition factors, and the powers of $t$ record their degrees.
+The entries are formal Laurent series; for algebras they are formal power series.
+Finite support gives Laurent polynomials or polynomials, respectively.
+Since $(P_i)_0=L_i$, we have $h_A(0)=I_r$, the $r\times r$ identity array.
+For a finite-dimensional right $S$-module $N$, use the same multiplicity notation and write $\dimvec N=([N:L_j])_{1\leq j\leq r}$.
+
+The multiplicities can be computed using Hom spaces:
+\begin{equation}\label{eq:composition-Hom}
+[M_d:L_j]=\dim_{\End_A(L_j)}\Hom_A(P_j,M_d)
+\quad\text{for all }d\in\Z,\ 1\leq j\leq r.
+\end{equation}
+Indeed, $M_dA_+=0$, so every map $P_j\to M_d$ factors uniquely through $P_j/P_jA_+\cong L_j$.
+This identifies $\Hom_A(P_j,M_d)$ with $\Hom_A(L_j,M_d)$; precomposition gives its right vector-space structure over the division algebra $\End_A(L_j)$.
+A non-zero map between simple modules is an isomorphism, so each copy of $L_j$ contributes one copy of $\End_A(L_j)$, and the other simples contribute zero.
+This also shows that the multiplicities are independent of the chosen decomposition.
+
+\begin{example}\label{ex:dimension-vector-coordinate}
+If $S=\bigoplus_{j=1}^r\Bbbk e_j$ with coordinate idempotents, then $\End_A(L_j)=\Bbbk$.
+The Yoneda lemma~\ref{lem:idempotent-hom} identifies $\Hom_A(P_j,M_d)$ with $M_de_j$, so
+\[
+[M_d:L_j]=\dim_\Bbbk(M_de_j),
+\qquad \dimvec M_d=(\dim_\Bbbk M_de_j)_{1\leq j\leq r}.
+\]
+\end{example}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
Fix a finite-dimensional semisimple $\Bbbk$-algebra $S$, concentrated in degree $0$.
We record dimensions relative to all simple right $S$-modules.
We define module series first, then collect them in an array for a graded algebra.

\begin{definition}\label{def:dimension-vector}
\comm{why do $S$-module.  It should be do-able for any $A$-module???  If needed, can just assume $A$ is lfd graded algebra.}
Choose representatives $L_1,\ldots,L_r$ of the isomorphism classes of simple right $S$-modules.
For a finite-dimensional right $S$-module $M$, write, with $m_j\in\Z_{\geq0}$,
\[
M\cong\bigoplus_{j=1}^r L_j^{\oplus m_j},
\qquad \dimvec M:=(m_1,\ldots,m_r).
\]
The row vector $\dimvec M$ is the \defn{dimension vector} of $M$.
\comm{we don't use bimodule???}
For a finite-dimensional bimodule ${}_SU_S$, arrange the vectors $\dimvec(L_i\otimes_S U)$ as rows:
\[
\dimvec U=(u_{ij})_{1\leq i,j\leq r},
\qquad (\dimvec U)_{ij}:=\bigl(\dimvec(L_i\otimes_S U)\bigr)_j.
\]
Thus $L_i\otimes_S U\cong\bigoplus_{j=1}^rL_j^{\oplus u_{ij}}$.
\end{definition}

The decompositions exist by Theorem~\ref{thm:artin-wedderburn}.
Their multiplicities are unique: a non-zero homomorphism between simple modules is an isomorphism, since its kernel and image are submodules.
Consequently
\[
m_j=\frac{\dim_\Bbbk\Hom_S(L_j,M)}{\dim_\Bbbk\End_S(L_j)},
\]
and the same formula applies to each $L_i\otimes_S U$.
In particular, the dimension data do not depend on choices of decompositions.
For the $S$-bimodule $S$, we have $\dimvec S=I_r$, the $r\times r$ identity array.

\begin{example}\label{ex:dimension-vector-coordinate}
If $S=\bigoplus_{i=1}^r\Bbbk e_i$ with coordinate idempotents, take $L_i=e_iS$.
Then
\[
\dimvec M=(\dim_\Bbbk Me_j)_{1\le j\le r},
\qquad (\dimvec U)_{ij}=\dim_\Bbbk(e_iUe_j).
\]
Indeed, $L_i\otimes_S U\cong e_iU$ by multiplication, and the multiplicity of $e_jS$ in $e_iU$ is $\dim_\Bbbk(e_iUe_j)$.
For $S=\Bbbk$, the dimension vector has one entry, the usual vector space dimension.
\end{example}

\begin{definition}\label{def:hilbert-series}
\comm{why this definition is separated with graded $S$-modules first then graded $A$ modules.  It can be just with graded $A$-modules from the get go?? }
Let $M=\bigoplus_{d\in\Z}M_d$ be a locally finite-dimensional graded right $S$-module, with $M_d=0$ for all sufficiently negative $d$.
Its \defn{Hilbert series} is
\[
h_M(t):=\sum_{d\in\Z}(\dimvec M_d)t^d.
\]
For a locally finite-dimensional graded algebra $A$ with $A_0=S$, its \defn{Hilbert series} records the preceding module series row by row:
\[
h_A(t)_{ij}:=\bigl(h_{L_i\otimes_S A}(t)\bigr)_j
\quad(1\leq i,j\leq r),
\qquad
h_A(t)=\sum_{d\geq0}(\dimvec A_d)t^d.
\]
Here each $L_i$ is placed in degree $0$, and $L_i\otimes_S A$ is regarded as a right $S$-module by restriction.
In particular, $h_A(0)=I_r$.
For $S=\bigoplus_{i=1}^r\Bbbk e_i$, this gives
\[
h_A(t)_{ij}=\sum_{d\geq0}\dim_\Bbbk(e_iA_de_j)t^d
\quad(1\leq i,j\leq r).
\]
\end{definition}

The entries are formal Laurent series with integer coefficients; for algebras they are formal power series.
A finite-dimensional graded module or algebra gives a Laurent polynomial or polynomial, respectively.
No numerical convergence is required: a coefficient is specified degree by degree.
For an algebra, keeping both indices records where products can be formed.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
Let $A$ be a locally finite-dimensional graded algebra with $S=A_0$ finite-dimensional semisimple.
Each degree piece of a graded right $A$-module $M$ is naturally an $A$-module:
\[
M_d\cong M_{\geq d}/M_{\geq d+1},
\qquad M_{\geq d}:=\bigoplus_{j\geq d}M_j.
\]
The action on $M_d$ factors through $A/A_+=S$, so $M_d$ is semisimple.
The simple summands in a direct sum decomposition of $M_d$ are its \defn{composition factors}.

By Theorem~\ref{thm:artin-wedderburn}, choose primitive idempotents $e_1,\ldots,e_r\in S$ so that $L_j:=e_jS$ represents each isomorphism class of simple right $S$-modules once.
Then $L_j\cong e_jA/e_jA_+$ is a graded simple $A$-module.
\phantomsection\label{not:hilbert-simples-summands}

\begin{definition}\label{def:dimension-vector}\label{def:hilbert-series}
For a locally finite-dimensional graded right $A$-module $M$, write $[M_d:L_j]$ for the multiplicity of $L_j$ in $M_d$.
Its degree $d$ \defn{dimension vector} is the row vector
\[
\dimvec M_d:=\bigl([M_d:L_j]\bigr)_{1\leq j\leq r}.
\]
The module $M$ is \defn{bounded below} if $M_d=0$ for all sufficiently negative $d$.
For such $M$, its \defn{Hilbert series} is
\[
h_M(t):=\sum_{d\in\Z}(\dimvec M_d)t^d
=\sum_{d\in\Z}\bigl([M_d:L_j]\bigr)_{1\leq j\leq r}t^d.
\]
For $P_i:=e_iA$, the \defn{Hilbert series} of the algebra $A$ collects the right-module series $h_{P_i}(t)$ as rows:
\[
h_A(t)_{ij}:=\bigl(h_{P_i}(t)\bigr)_j
=\sum_{d\geq0}[(P_i)_d:L_j]t^d
\quad\text{for all }1\leq i,j\leq r.
\]
\end{definition}

Thus the coefficients count composition factors, and the powers of $t$ record their degrees.
The entries are formal Laurent series; for algebras they are formal power series.
Finite support gives Laurent polynomials or polynomials, respectively.
Since $(P_i)_0=L_i$, we have $h_A(0)=I_r$, the $r\times r$ identity array.
For a finite-dimensional right $S$-module $N$, use the same multiplicity notation and write $\dimvec N=([N:L_j])_{1\leq j\leq r}$.

The multiplicities can be computed using Hom spaces:
\begin{equation}\label{eq:composition-Hom}
[M_d:L_j]=\dim_{\End_A(L_j)}\Hom_A(P_j,M_d)
\quad\text{for all }d\in\Z,\ 1\leq j\leq r.
\end{equation}
Indeed, $M_dA_+=0$, so every map $P_j\to M_d$ factors uniquely through $P_j/P_jA_+\cong L_j$.
This identifies $\Hom_A(P_j,M_d)$ with $\Hom_A(L_j,M_d)$; precomposition gives its right vector-space structure over the division algebra $\End_A(L_j)$.
A non-zero map between simple modules is an isomorphism, so each copy of $L_j$ contributes one copy of $\End_A(L_j)$, and the other simples contribute zero.
This also shows that the multiplicities are independent of the chosen decomposition.

\begin{example}\label{ex:dimension-vector-coordinate}
If $S=\bigoplus_{j=1}^r\Bbbk e_j$ with coordinate idempotents, then $\End_A(L_j)=\Bbbk$.
The Yoneda lemma~\ref{lem:idempotent-hom} identifies $\Hom_A(P_j,M_d)$ with $M_de_j$, so
\[
[M_d:L_j]=\dim_\Bbbk(M_de_j),
\qquad \dimvec M_d=(\dim_\Bbbk M_de_j)_{1\leq j\leq r}.
\]
\end{example}
```

</details>

### Passage 2

**Location:** [Lecture_Koszul.tex:350](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:350) (current lines 350–352)  
**Change size:** 3 lines added; 3 lines removed.

Replace the bimodule entry with the agreed one-sided notation and link the Hom computation. Keep L_j to avoid a notation change in later lectures.

```diff
--- a/Lecture_Koszul.tex
+++ b/Lecture_Koszul.tex
@@ -350,3 +350,3 @@
-$L_1,\ldots,L_r$ & Representatives of the simple right $S$-modules. & \hyperref[def:dimension-vector]{\pageref*{def:dimension-vector}}\\[3pt]
-$\dimvec M$ & Row vector of simple-module multiplicities in $M_S$. & \hyperref[def:dimension-vector]{\pageref*{def:dimension-vector}}\\[3pt]
-$\dimvec U$ & Bimodule dimension array; row $i$ is $\dimvec(L_i\otimes_S U)$. & \hyperref[def:dimension-vector]{\pageref*{def:dimension-vector}}\\[3pt]
+$L_j=e_jS,\ P_j=e_jA$ & Simple modules and the corresponding right-module summands of $A$ used to index Hilbert series. & \hyperref[not:hilbert-simples-summands]{\pageref*{not:hilbert-simples-summands}}\\[3pt]
+$[M_d:L_j]$ & Composition multiplicity in degree $d$; computed by \eqref{eq:composition-Hom}. & \hyperref[def:dimension-vector]{\pageref*{def:dimension-vector}}\\[3pt]
+$\dimvec M_d$ & Row vector $([M_d:L_j])_{1\leq j\leq r}$. & \hyperref[def:dimension-vector]{\pageref*{def:dimension-vector}}\\[3pt]
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
$L_1,\ldots,L_r$ & Representatives of the simple right $S$-modules. & \hyperref[def:dimension-vector]{\pageref*{def:dimension-vector}}\\[3pt]
$\dimvec M$ & Row vector of simple-module multiplicities in $M_S$. & \hyperref[def:dimension-vector]{\pageref*{def:dimension-vector}}\\[3pt]
$\dimvec U$ & Bimodule dimension array; row $i$ is $\dimvec(L_i\otimes_S U)$. & \hyperref[def:dimension-vector]{\pageref*{def:dimension-vector}}\\[3pt]
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
$L_j=e_jS,\ P_j=e_jA$ & Simple modules and the corresponding right-module summands of $A$ used to index Hilbert series. & \hyperref[not:hilbert-simples-summands]{\pageref*{not:hilbert-simples-summands}}\\[3pt]
$[M_d:L_j]$ & Composition multiplicity in degree $d$; computed by \eqref{eq:composition-Hom}. & \hyperref[def:dimension-vector]{\pageref*{def:dimension-vector}}\\[3pt]
$\dimvec M_d$ & Row vector $([M_d:L_j])_{1\leq j\leq r}$. & \hyperref[def:dimension-vector]{\pageref*{def:dimension-vector}}\\[3pt]
```

</details>

### Passage 3

**Location:** [Lecture_Koszul_S2.tex:849](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:849) (current lines 849–895)  
**Change size:** 22 lines added; 21 lines removed.

Dependent correction: replace the bimodule dimension-vector identities by a composition-multiplicity formula for right modules. Keep the existing tensor-algebra Hilbert-series result.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -849,47 +829,48 @@
 \begin{lemma}\label{lem:dimension-tensor}\label{lem:hilbert-tensor}
-Let ${}_SU_S$, ${}_SW_S$ be finite-dimensional bimodules and $M$ a finite-dimensional right $S$-module. Then
+Let $N$ be a finite-dimensional right $S$-module and ${}_SU_S$ a finite-dimensional bimodule.
+Then
 \[
-\dimvec(U\otimes_S W)=(\dimvec U)(\dimvec W),
-\qquad \dimvec(M\otimes_S U)=(\dimvec M)(\dimvec U).
+[N\otimes_S U:L_j]
+=\sum_{i=1}^r[N:L_i][e_iU:L_j]
+\quad\text{for all }1\leq j\leq r.
 \]
-For a locally finite-dimensional graded right $S$-module $M$ bounded below and a locally finite-dimensional graded algebra $A$ with $A_0=S$, this gives
+For a locally finite-dimensional graded right $A$-module $M$ bounded below,
 \[
 h_{M\otimes_S A}(t)=h_M(t)h_A(t).
 \]
 \end{lemma}
 
 \begin{proof}
-Write $C=\dimvec U$ and $D=\dimvec W$.
-Associativity and distribution over direct sums give
+Decompose $N\cong\bigoplus_{i=1}^r(e_iS)^{\oplus[N:L_i]}$.
+Multiplication $e_iS\otimes_S U\to e_iU$, $e_is\otimes u\mapsto e_isu$, is an isomorphism with inverse $u\mapsto e_i\otimes u$.
+Distribution over direct sums therefore gives
 \[
-\begin{aligned}
-L_i\otimes_S(U\otimes_S W)
-&\cong (L_i\otimes_S U)\otimes_S W\\
-&\cong\bigoplus_j(L_j\otimes_S W)^{\oplus c_{ij}}
-\cong\bigoplus_\ell L_\ell^{\oplus\sum_j c_{ij}d_{j\ell}}.
-\end{aligned}
+N\otimes_S U\cong\bigoplus_{i=1}^r(e_iU)^{\oplus[N:L_i]}.
 \]
-This proves the first equality. Decomposing $M\cong\bigoplus_iL_i^{\oplus m_i}$ proves the second in the same way.
-Apply the second equality to each $M_p\otimes_S A_q$ and sum over $p+q=d$ to obtain the series identity.
+Counting copies of $L_j$ proves the first formula.
+Apply the first formula to $M_p\otimes_S A_q$ and sum over all $p,q\in\Z$ with $p+q=d$.
+Since $e_iA_q=(P_i)_q$, the resulting coefficient is the coefficient of $t^d$ in $h_M(t)h_A(t)$.
 \end{proof}
 
 \begin{example}[Hilbert series of a tensor algebra]\label{ex:hilbert-tensor-algebra}
-Let ${}_SV_S$ be a finite-dimensional bimodule, placed in degree $1$, and put $C=\dimvec V$.
-Since $T_S(V)_d=V^{\otimes_S d}$ and $V^{\otimes_S0}=S$, Lemma~\ref{lem:dimension-tensor} gives
+Let ${}_SV_S$ be a finite-dimensional bimodule, placed in degree $1$, and put $C=([e_iV:L_j])_{1\leq i,j\leq r}$.
+The rows of $C$ count composition factors of the right modules $e_iV$.
+Since $e_iT_S(V)_0=L_i$ and $e_iT_S(V)_{d+1}\cong(e_iT_S(V)_d)\otimes_S V$, Lemma~\ref{lem:dimension-tensor} gives, by induction,
 \[
-\dimvec T_S(V)_d=C^d\quad(d\geq0),\qquad C^0=I_r.
+[e_iT_S(V)_d:L_j]=(C^d)_{ij},
+\qquad C^0=I_r
+\quad\text{for all }d\geq0,\ 1\leq i,j\leq r.
 \]
 Consequently,
 \begin{equation}\label{eq:hilbert-tensor-algebra}
 \boxed{\displaystyle
-h_{T_S(V)}(t)=\sum_{d\geq0}t^dC^d
-=(I_r-tC)^{-1}=(I_r-t\,\dimvec V)^{-1}.}
+h_{T_S(V)}(t)=\sum_{d\geq0}t^dC^d=(I_r-tC)^{-1}.}
 \end{equation}
 Indeed, multiplying the series on either side by $I_r-tC$ gives constant coefficient $I_r$; the coefficient of $t^d$ for $d\geq1$ is $C^d-C^d=0$.
 The inverse is therefore an identity of formal power series with the coefficient multiplication defined above.
 
 For $S=\Bbbk$ and $\dim_\Bbbk V=m$, the formula is $h_{T_\Bbbk(V)}(t)=1/(1-mt)$.
-More generally, for $S=\operatorname{Mat}_n(\Bbbk)$ and $V=S^{\oplus m}$ as an $S$-bimodule, there is one simple right $S$-module $L=\Bbbk^{1\times n}$.
-Since $L\otimes_S V\cong L^{\oplus m}$, we again have $C=(m)$ and $h_{T_S(V)}(t)=1/(1-mt)$.
+More generally, for $S=\operatorname{Mat}_n(\Bbbk)$ and $V=S^{\oplus m}$ as an $S$-bimodule, choose $e_1=e_{11}$.
+Since $e_1V\cong(e_1S)^{\oplus m}$ as right $S$-modules, we again have $C=(m)$ and $h_{T_S(V)}(t)=1/(1-mt)$.
 Here the coefficient records simple-module multiplicities, not $\dim_\Bbbk V=mn^2$.
 \end{example}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\begin{lemma}\label{lem:dimension-tensor}\label{lem:hilbert-tensor}
Let ${}_SU_S$, ${}_SW_S$ be finite-dimensional bimodules and $M$ a finite-dimensional right $S$-module. Then
\[
\dimvec(U\otimes_S W)=(\dimvec U)(\dimvec W),
\qquad \dimvec(M\otimes_S U)=(\dimvec M)(\dimvec U).
\]
For a locally finite-dimensional graded right $S$-module $M$ bounded below and a locally finite-dimensional graded algebra $A$ with $A_0=S$, this gives
\[
h_{M\otimes_S A}(t)=h_M(t)h_A(t).
\]
\end{lemma}

\begin{proof}
Write $C=\dimvec U$ and $D=\dimvec W$.
Associativity and distribution over direct sums give
\[
\begin{aligned}
L_i\otimes_S(U\otimes_S W)
&\cong (L_i\otimes_S U)\otimes_S W\\
&\cong\bigoplus_j(L_j\otimes_S W)^{\oplus c_{ij}}
\cong\bigoplus_\ell L_\ell^{\oplus\sum_j c_{ij}d_{j\ell}}.
\end{aligned}
\]
This proves the first equality. Decomposing $M\cong\bigoplus_iL_i^{\oplus m_i}$ proves the second in the same way.
Apply the second equality to each $M_p\otimes_S A_q$ and sum over $p+q=d$ to obtain the series identity.
\end{proof}

\begin{example}[Hilbert series of a tensor algebra]\label{ex:hilbert-tensor-algebra}
Let ${}_SV_S$ be a finite-dimensional bimodule, placed in degree $1$, and put $C=\dimvec V$.
Since $T_S(V)_d=V^{\otimes_S d}$ and $V^{\otimes_S0}=S$, Lemma~\ref{lem:dimension-tensor} gives
\[
\dimvec T_S(V)_d=C^d\quad(d\geq0),\qquad C^0=I_r.
\]
Consequently,
\begin{equation}\label{eq:hilbert-tensor-algebra}
\boxed{\displaystyle
h_{T_S(V)}(t)=\sum_{d\geq0}t^dC^d
=(I_r-tC)^{-1}=(I_r-t\,\dimvec V)^{-1}.}
\end{equation}
Indeed, multiplying the series on either side by $I_r-tC$ gives constant coefficient $I_r$; the coefficient of $t^d$ for $d\geq1$ is $C^d-C^d=0$.
The inverse is therefore an identity of formal power series with the coefficient multiplication defined above.

For $S=\Bbbk$ and $\dim_\Bbbk V=m$, the formula is $h_{T_\Bbbk(V)}(t)=1/(1-mt)$.
More generally, for $S=\operatorname{Mat}_n(\Bbbk)$ and $V=S^{\oplus m}$ as an $S$-bimodule, there is one simple right $S$-module $L=\Bbbk^{1\times n}$.
Since $L\otimes_S V\cong L^{\oplus m}$, we again have $C=(m)$ and $h_{T_S(V)}(t)=1/(1-mt)$.
Here the coefficient records simple-module multiplicities, not $\dim_\Bbbk V=mn^2$.
\end{example}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{lemma}\label{lem:dimension-tensor}\label{lem:hilbert-tensor}
Let $N$ be a finite-dimensional right $S$-module and ${}_SU_S$ a finite-dimensional bimodule.
Then
\[
[N\otimes_S U:L_j]
=\sum_{i=1}^r[N:L_i][e_iU:L_j]
\quad\text{for all }1\leq j\leq r.
\]
For a locally finite-dimensional graded right $A$-module $M$ bounded below,
\[
h_{M\otimes_S A}(t)=h_M(t)h_A(t).
\]
\end{lemma}

\begin{proof}
Decompose $N\cong\bigoplus_{i=1}^r(e_iS)^{\oplus[N:L_i]}$.
Multiplication $e_iS\otimes_S U\to e_iU$, $e_is\otimes u\mapsto e_isu$, is an isomorphism with inverse $u\mapsto e_i\otimes u$.
Distribution over direct sums therefore gives
\[
N\otimes_S U\cong\bigoplus_{i=1}^r(e_iU)^{\oplus[N:L_i]}.
\]
Counting copies of $L_j$ proves the first formula.
Apply the first formula to $M_p\otimes_S A_q$ and sum over all $p,q\in\Z$ with $p+q=d$.
Since $e_iA_q=(P_i)_q$, the resulting coefficient is the coefficient of $t^d$ in $h_M(t)h_A(t)$.
\end{proof}

\begin{example}[Hilbert series of a tensor algebra]\label{ex:hilbert-tensor-algebra}
Let ${}_SV_S$ be a finite-dimensional bimodule, placed in degree $1$, and put $C=([e_iV:L_j])_{1\leq i,j\leq r}$.
The rows of $C$ count composition factors of the right modules $e_iV$.
Since $e_iT_S(V)_0=L_i$ and $e_iT_S(V)_{d+1}\cong(e_iT_S(V)_d)\otimes_S V$, Lemma~\ref{lem:dimension-tensor} gives, by induction,
\[
[e_iT_S(V)_d:L_j]=(C^d)_{ij},
\qquad C^0=I_r
\quad\text{for all }d\geq0,\ 1\leq i,j\leq r.
\]
Consequently,
\begin{equation}\label{eq:hilbert-tensor-algebra}
\boxed{\displaystyle
h_{T_S(V)}(t)=\sum_{d\geq0}t^dC^d=(I_r-tC)^{-1}.}
\end{equation}
Indeed, multiplying the series on either side by $I_r-tC$ gives constant coefficient $I_r$; the coefficient of $t^d$ for $d\geq1$ is $C^d-C^d=0$.
The inverse is therefore an identity of formal power series with the coefficient multiplication defined above.

For $S=\Bbbk$ and $\dim_\Bbbk V=m$, the formula is $h_{T_\Bbbk(V)}(t)=1/(1-mt)$.
More generally, for $S=\operatorname{Mat}_n(\Bbbk)$ and $V=S^{\oplus m}$ as an $S$-bimodule, choose $e_1=e_{11}$.
Since $e_1V\cong(e_1S)^{\oplus m}$ as right $S$-modules, we again have $C=(m)$ and $h_{T_S(V)}(t)=1/(1-mt)$.
Here the coefficient records simple-module multiplicities, not $\dim_\Bbbk V=mn^2$.
\end{example}
```

</details>

### Passage 4

**Location:** [Lecture_Koszul_S2.tex:915](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:915) (current lines 915–917)  
**Change size:** 2 lines added; 2 lines removed.

Remove the last use of the bimodule symbol in the alternating-generator example; retain the computed array and series.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -915,3 +896,3 @@
-For $S,V,a,b$ in Example~\ref{ex:two-vertex-relations}, use the order $e_1,e_2$. Then
+For $S,V,a,b$ in Example~\ref{ex:two-vertex-relations}, use the order $e_1,e_2$ and the array $C$ of Example~\ref{ex:hilbert-tensor-algebra}. Then
 \[
-C=\dimvec V=\begin{pmatrix}0&1\\1&0\end{pmatrix},
+C=\begin{pmatrix}0&1\\1&0\end{pmatrix},
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
For $S,V,a,b$ in Example~\ref{ex:two-vertex-relations}, use the order $e_1,e_2$. Then
\[
C=\dimvec V=\begin{pmatrix}0&1\\1&0\end{pmatrix},
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
For $S,V,a,b$ in Example~\ref{ex:two-vertex-relations}, use the order $e_1,e_2$ and the array $C$ of Example~\ref{ex:hilbert-tensor-algebra}. Then
\[
C=\begin{pmatrix}0&1\\1&0\end{pmatrix},
```

</details>

---

<a id="replacement-7"></a>

## Replacement 7: Use composition-factor additivity in the Hilbert-series properties

State the properties for graded A-modules. In the proof, use the exact sequence of semisimple degree pieces and add their composition-factor multiplicities. Remove the earlier proposed restriction-of-scalars explanation; it is unnecessary here.

### Passage 1

**Location:** [Lecture_Koszul_S2.tex:812](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:812)  
**Change size:** 1 line added; 1 line removed.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -812,1 +789,1 @@
-For locally finite-dimensional graded right $S$-modules bounded below:
+For locally finite-dimensional graded right $A$-modules bounded below:
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
For locally finite-dimensional graded right $S$-modules bounded below:
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
For locally finite-dimensional graded right $A$-modules bounded below:
```

</details>

### Passage 2

**Location:** [Lecture_Koszul_S2.tex:822](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:822)  
**Change size:** 1 line added; 1 line removed.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -822,1 +799,1 @@
-A short exact sequence of right $S$-modules splits by semisimplicity, so multiplicities add.
+In each degree, a graded short exact sequence gives $0\to L_d\to M_d\to N_d\to0$, so $[M_d:L_j]=[L_d:L_j]+[N_d:L_j]$ for all $1\leq j\leq r$.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
A short exact sequence of right $S$-modules splits by semisimplicity, so multiplicities add.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
In each degree, a graded short exact sequence gives $0\to L_d\to M_d\to N_d\to0$, so $[M_d:L_j]=[L_d:L_j]+[N_d:L_j]$ for all $1\leq j\leq r$.
```

</details>

---

<a id="replacement-8"></a>

## Replacement 8: Remove the algebra direct-sum subsection

Delete the subsection as requested. No retained lecture, homework question, or notation-list entry refers to its proposition. This does not alter direct sums of modules or vector spaces elsewhere.

**Location:** [Lecture_Koszul_S3.tex:304](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:304) (current lines 304–342)  
**Change size:** 0 lines added; 39 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -304,39 +303,0 @@
-\subsection{Direct sums}
-
-\comm{don't do this for rings.  this should be direct products.  remove this subsection; it is too elementary. no added value to lecture, just waste time.}
-For graded algebras $A,B$, the finite direct sum $A\oplus B$ has componentwise multiplication, unit $(1_A,1_B)$, and $(A\oplus B)_i=A_i\oplus B_i$.
-In particular, its degree $0$ algebra is $A_0\oplus B_0$.
-
-\begin{proposition}\label{prop:dual-direct-sum}
-Let $A=T_S(V)/(R)$ and $B=T_T(W)/(Q)$ be quadratic algebras. Then $A\oplus B$ is quadratic over $S\oplus T$, and
-\[
-(A\oplus B)^!\cong A^!\oplus B^!.
-\]
-\end{proposition}
-
-\begin{proof}
-Let $(s,t)\in S\oplus T$ act on $V$ through $s$ and on $W$ through $t$, on both sides.
-The local unit $(1_S,0)$ is the identity on $V$ and acts as zero on $W$, so
-\[
-v\otimes_{S\oplus T}w
-=v(1_S,0)\otimes_{S\oplus T}w
-=v\otimes_{S\oplus T}(1_S,0)w=0
-\quad(v\in V,\ w\in W).
-\]
-Likewise $w\otimes_{S\oplus T}v=0$.
-Distributing tensor products over direct sums by Lemma~\ref{lem:tensor-properties}(4) gives
-\[
-\begin{aligned}
-T_{S\oplus T}(V\oplus W)&\cong T_S(V)\oplus T_T(W),\\
-(V\oplus W)\otimes_{S\oplus T}(V\oplus W)
-&\cong(V\otimes_S V)\oplus(W\otimes_T W).
-\end{aligned}
-\]
-The relation space is $R\oplus Q$.
-A right $(S\oplus T)$-linear map $V\oplus W\to S\oplus T$ maps $V$ into $S$ and $W$ into $T$, so the generator dual is $V^*\oplus W^*$.
-The annihilator of $R\oplus Q$ is therefore $R^\perp\oplus Q^\perp$, giving the assertion by Definition~\ref{def:quadratic-duals}.
-\end{proof}
-
-For example, $\bigl((\Bbbk A_2)^{\oplus2}\bigr)^!\cong\bigl((\Bbbk A_2)^\op\bigr)^{\oplus2}$ by Example~\ref{ex:An-quadratic-dual}.
-Both degree $0$ algebras are $\Bbbk^{\oplus4}$; there are no products connecting the two summands.
-
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\subsection{Direct sums}

\comm{don't do this for rings.  this should be direct products.  remove this subsection; it is too elementary. no added value to lecture, just waste time.}
For graded algebras $A,B$, the finite direct sum $A\oplus B$ has componentwise multiplication, unit $(1_A,1_B)$, and $(A\oplus B)_i=A_i\oplus B_i$.
In particular, its degree $0$ algebra is $A_0\oplus B_0$.

\begin{proposition}\label{prop:dual-direct-sum}
Let $A=T_S(V)/(R)$ and $B=T_T(W)/(Q)$ be quadratic algebras. Then $A\oplus B$ is quadratic over $S\oplus T$, and
\[
(A\oplus B)^!\cong A^!\oplus B^!.
\]
\end{proposition}

\begin{proof}
Let $(s,t)\in S\oplus T$ act on $V$ through $s$ and on $W$ through $t$, on both sides.
The local unit $(1_S,0)$ is the identity on $V$ and acts as zero on $W$, so
\[
v\otimes_{S\oplus T}w
=v(1_S,0)\otimes_{S\oplus T}w
=v\otimes_{S\oplus T}(1_S,0)w=0
\quad(v\in V,\ w\in W).
\]
Likewise $w\otimes_{S\oplus T}v=0$.
Distributing tensor products over direct sums by Lemma~\ref{lem:tensor-properties}(4) gives
\[
\begin{aligned}
T_{S\oplus T}(V\oplus W)&\cong T_S(V)\oplus T_T(W),\\
(V\oplus W)\otimes_{S\oplus T}(V\oplus W)
&\cong(V\otimes_S V)\oplus(W\otimes_T W).
\end{aligned}
\]
The relation space is $R\oplus Q$.
A right $(S\oplus T)$-linear map $V\oplus W\to S\oplus T$ maps $V$ into $S$ and $W$ into $T$, so the generator dual is $V^*\oplus W^*$.
The annihilator of $R\oplus Q$ is therefore $R^\perp\oplus Q^\perp$, giving the assertion by Definition~\ref{def:quadratic-duals}.
\end{proof}

For example, $\bigl((\Bbbk A_2)^{\oplus2}\bigr)^!\cong\bigl((\Bbbk A_2)^\op\bigr)^{\oplus2}$ by Example~\ref{ex:An-quadratic-dual}.
Both degree $0$ algebras are $\Bbbk^{\oplus4}$; there are no products connecting the two summands.

```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
```

</details>

---

<a id="replacement-9"></a>

## Replacement 9: Make tensor products and signs entirely advanced

The current Lectures 4 and 5 do not use this subsection. The plan returns to tensor products of Koszul algebras in Lecture 8. Retain the material for reference, but put the heading, both products, the compatibility proposition, its proof, and both examples inside a single advanced block. Remove the existing inner advanced wrapper to avoid nested blocks. Mark the dependent final exercise advanced as well.

### Passage 1

**Location:** [Lecture_Koszul_S3.tex:343](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:343) (current lines 343–345)  
**Change size:** 1 line added; 2 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -343,3 +304,2 @@
+\begin{advanced}[suppressfirstparskip=true,innertopmargin=0pt]
 \subsection{Tensor products and signs}
-
-\comm{this whole subsection should be advanced.  do we really use it in the future?  maybe leave until finished defining koszul algebra and all the fundamental theorem}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\subsection{Tensor products and signs}

\comm{this whole subsection should be advanced.  do we really use it in the future?  maybe leave until finished defining koszul algebra and all the fundamental theorem}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{advanced}[suppressfirstparskip=true,innertopmargin=0pt]
\subsection{Tensor products and signs}
```

</details>

### Passage 2

**Location:** [Lecture_Koszul_S3.tex:388](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:388) (current lines 388–389)  
**Change size:** 0 lines added; 1 line removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -388,2 +348,1 @@
-\begin{advanced}
 The assumption on $S\otimes_\Bbbk T$ holds when $S,T$ are products of matrix algebras over $\Bbbk$, since $\Mat_a(\Bbbk)\otimes_\Bbbk\Mat_b(\Bbbk)\cong\Mat_{ab}(\Bbbk)$.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\begin{advanced}
The assumption on $S\otimes_\Bbbk T$ holds when $S,T$ are products of matrix algebras over $\Bbbk$, since $\Mat_a(\Bbbk)\otimes_\Bbbk\Mat_b(\Bbbk)\cong\Mat_{ab}(\Bbbk)$.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
The assumption on $S\otimes_\Bbbk T$ holds when $S,T$ are products of matrix algebras over $\Bbbk$, since $\Mat_a(\Bbbk)\otimes_\Bbbk\Mat_b(\Bbbk)\cong\Mat_{ab}(\Bbbk)$.
```

</details>

### Passage 3

**Location:** [Lecture_Koszul_S3.tex:431](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:431) (current lines 431–434)  
**Change size:** 0 lines added; 1 line removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -431,4 +390,3 @@
 \end{proof}
-\end{advanced}
 
 \begin{example}\label{ex:commuting-square-dual}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\end{proof}
\end{advanced}

\begin{example}\label{ex:commuting-square-dual}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\end{proof}

\begin{example}\label{ex:commuting-square-dual}
```

</details>

### Passage 4

**Location:** [Lecture_Koszul_S3.tex:478](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:478) (current lines 478–481)  
**Change size:** 1 line added; 0 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -478,4 +436,5 @@
 They are therefore not isomorphic. This sign cannot be removed by a change of generators.
 \end{example}
+\end{advanced}
 
 \subsection{Exercises}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
They are therefore not isomorphic. This sign cannot be removed by a change of generators.
\end{example}

\subsection{Exercises}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
They are therefore not isomorphic. This sign cannot be removed by a change of generators.
\end{example}
\end{advanced}

\subsection{Exercises}
```

</details>

### Passage 5

**Location:** [Lecture_Koszul_S3.tex:500](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:500) (current lines 500–504)  
**Change size:** 3 lines added; 0 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -500,5 +459,8 @@
+\begin{advanced}
 \begin{exercise}
 For the four generators in Example~\ref{ex:commuting-square-dual}, replace the relation $ab-cd$ by $ab-\lambda cd$, where $\lambda\in\Bbbk$.
 Compute the quadratic dual relation for every $\lambda$, including $\lambda=0$, and recover the original relation by dualising again.
+
 \emph{Hint.} Evaluate $\mu b^*a^*+\nu d^*c^*$ on $ab-\lambda cd$. For $\lambda\neq0$, rescale $d$ to compare with Example~\ref{ex:commuting-square-dual}.
 \end{exercise}
+\end{advanced}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\begin{exercise}
For the four generators in Example~\ref{ex:commuting-square-dual}, replace the relation $ab-cd$ by $ab-\lambda cd$, where $\lambda\in\Bbbk$.
Compute the quadratic dual relation for every $\lambda$, including $\lambda=0$, and recover the original relation by dualising again.
\emph{Hint.} Evaluate $\mu b^*a^*+\nu d^*c^*$ on $ab-\lambda cd$. For $\lambda\neq0$, rescale $d$ to compare with Example~\ref{ex:commuting-square-dual}.
\end{exercise}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{advanced}
\begin{exercise}
For the four generators in Example~\ref{ex:commuting-square-dual}, replace the relation $ab-cd$ by $ab-\lambda cd$, where $\lambda\in\Bbbk$.
Compute the quadratic dual relation for every $\lambda$, including $\lambda=0$, and recover the original relation by dualising again.

\emph{Hint.} Evaluate $\mu b^*a^*+\nu d^*c^*$ on $ab-\lambda cd$. For $\lambda\neq0$, rescale $d$ to compare with Example~\ref{ex:commuting-square-dual}.
\end{exercise}
\end{advanced}
```

</details>

---

<a id="replacement-10"></a>

## Replacement 10: Keep the homework tensor-product comparison optional

Homework 1, Question 5(c)(iii), explicitly asks about ordinary and graded algebra tensor products. Once the Lecture 3 subsection is advanced, label only that comparison advanced. The quadratic-dual calculation stays part of the main question. Question 6(a) gives its own generators and relation, so it remains self-contained and needs no content change.

**Location:** [Homework1.tex:381](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Homework1.tex:381) (current lines 381–385)  
**Change size:** 5 lines added; 2 lines removed.

```diff
--- a/Homework1.tex
+++ b/Homework1.tex
@@ -381,5 +381,8 @@
 \subpart Compute a quadratic presentation of $C_q^!$ using the reversed
-pairing. Identify $C_1$ and $C_{-1}$ as the graded and ordinary tensor
-products, respectively, of two copies of $\kk[z]/(z^2)$ with $\deg z=1$.
+pairing.
+
+\emph{Advanced comparison.} Identify $C_1$ and $C_{-1}$ as the graded
+and ordinary tensor products, respectively, of two copies of
+$\kk[z]/(z^2)$ with $\deg z=1$.
 When the characteristic of $\kk$ is not $2$, are $C_1$ and $C_{-1}$
 isomorphic as algebras? Explain what changes in characteristic $2$.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\subpart Compute a quadratic presentation of $C_q^!$ using the reversed
pairing. Identify $C_1$ and $C_{-1}$ as the graded and ordinary tensor
products, respectively, of two copies of $\kk[z]/(z^2)$ with $\deg z=1$.
When the characteristic of $\kk$ is not $2$, are $C_1$ and $C_{-1}$
isomorphic as algebras? Explain what changes in characteristic $2$.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\subpart Compute a quadratic presentation of $C_q^!$ using the reversed
pairing.

\emph{Advanced comparison.} Identify $C_1$ and $C_{-1}$ as the graded
and ordinary tensor products, respectively, of two copies of
$\kk[z]/(z^2)$ with $\deg z=1$.
When the characteristic of $\kk$ is not $2$, are $C_1$ and $C_{-1}$
isomorphic as algebras? Explain what changes in characteristic $2$.
```

</details>

---

## Verification

**Checked against the proposed in-memory document:**

- Your complete convention block and the corollary statement remain verbatim.
- All nine active comments are addressed.
- Each quoted existing passage matches the current source exactly.
- The moved tensor-product definition appears once, in Lecture 1; Lecture 2 refers back to it.
- The new Hom and evaluation/coevaluation statements are in Lecture 1, after the relevant dual definitions.
- Retained and new references resolve, with no duplicate labels.
- Proposed lecture environments are balanced; no nested advanced block is introduced in Lecture 3.
- Vector index ranges remain in one subscript.
- Hilbert series are defined by composition multiplicities of right modules; the Hom computation uses the division algebra End_A(L_j).
- No bimodule dimension-vector notation remains in the proposed notes or notation list. The tensor-counting lemma and examples use right-module multiplicities.
- Replacements 1–5 and 8–10 retain their proposed content; Replacement 7 loses the tensor-counting passage now covered by Replacement 6.
- No uppercase Hilbert-series symbol, bare “locally finite”, or duplicated “-dimensional” remains in the proposed active lecture and homework text.
- Percent-commented source, hidden-content settings, and Lectures 4–5 remain unchanged.

**Pending approval:** apply the changes and compile the notes and Homework 1 with the existing hidden-content settings. No compilation or PDF update has been performed for this proposal.
