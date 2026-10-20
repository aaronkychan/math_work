# Change Proposal 14: Lectures 1, 2, and 3

> **Status: approved and applied on 20 October 2026.** The revised replacements and mechanical changes have been applied. The lecture notes and Homework 1 compiled successfully, and their PDFs were saved in the course folder.

**Prepared:** 20 October 2026, against the current saved sources.

## Scope

- Address all **15 active comments** in Lectures 1-3.
- Move the complete evaluation/coevaluation proposition to supplementary material immediately before its graded application in Lecture 2.
- Put the kernel and quotient assertions in the tensor-presentation corollary, keeping the definition of the ideal of relations separate.
- Use $n$ for the number of simple-module classes; use $n,m$ when two different algebras are considered.
- Add Homework 1, Question 4(2), with a specified bimodule isomorphism $V\cong A_1$ and a hidden solution.
- Update the corresponding notation-table entries in the mother file. Lectures 4 and 5, the preamble, and the hidden-content settings stay unchanged.

The deleted two-vertex example and commented-out pairing equation are **not restored**. Their remaining references are repaired. Two nearby mathematical corrections, Replacements 6 and 12, are identified separately.

## Reading the Proposal

In each diff, **`-` removes a line**, **`+` adds a line**, and an unmarked line is retained context. Added/removed counts accompany each passage. Full, exact old and new passages are available in separate expandable blocks.

All source locations refer to the **current files before any changes**. The new-line coordinates in the diffs describe the combined proposed version. Mechanical notation and terminology changes appear only as operations and line numbers, without full-line quotations.

## Contents

| Replacement | Change | Files |
|---|---|---|
| [1](#replacement-1) | Move evaluation and coevaluation to their first application | [Lecture_Koszul_S1.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex), [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex) |
| [2](#replacement-2) | Name anti-distributivity explicitly | [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex) |
| [3](#replacement-3) | Make the tensor grading explicit in the definition | [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex) |
| [4](#replacement-4) | Put the kernel and quotient assertions in the corollary | [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex) |
| [5](#replacement-5) | Keep the Hilbert-series notation one-sided and precise | [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex) |
| [6](#replacement-6) | Correct the matrix-algebra specialisation | [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex) |
| [7](#replacement-7) | Add Homework 1, Question 4(2), with a hidden solution | [Homework1.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Homework1.tex), [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex) |
| [8](#replacement-8) | Explain why the quadratic dual is independent of presentation | [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex) |
| [9](#replacement-9) | Compute the right dual of the relation space explicitly | [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex) |
| [10](#replacement-10) | Specify the dualities and the action in the bidual calculation | [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex) |
| [11](#replacement-11) | Repair references to the removed two-vertex example | [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex), [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex) |
| [12](#replacement-12) | Correct the polynomial Hilbert-series justification | [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex) |
| [Mechanical changes](#mechanical-changes) | Notation, terminology, and reference updates | Lectures 1-3 and the notation table |

**Dependencies:** the two sides of the relocation in Replacement 1 must be applied together. Replacement 7 uses the corollary and notation clarified in Replacements 4 and 5. Replacements 8-10 use the terminology in Replacement 2. The mechanical changes complete the consistency pass.

---

<a id="replacement-1"></a>
## Replacement 1: Move evaluation and coevaluation to their first application

As agreed, the entire proposition and proof move from Lecture 1 into supplementary material in Lecture 2, immediately before the graded refinement. The total-grading and tensor-counting passage marked by your two comments also becomes supplementary. The existing advanced warning and citation remain advanced, separately from the supplementary block. All existing labels are retained.

### 1a. Lecture_Koszul_S1.tex

**Source:** [Lecture_Koszul_S1.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1214), lines 1214-1255. **Changes:** +0 / -42 lines.

Remove this passage from Lecture 1; its destination is the following replacement.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -1214,42 +1213,0 @@
-Evaluation applies a functional to an element.
-Coevaluation expresses the identity endomorphism as an element of a tensor product.
-
-\begin{proposition}\label{prop:S-evaluation-coevaluation}
-\comm{not sure this is really important for the course, should it be left like this or just put as supplementary}
-For a bimodule $ {}_SV_S$, where $S$ is finite-dimensional semisimple, evaluation gives bimodule maps
-\begin{equation}\label{eq:S-evaluation-pairings}
-\begin{aligned}
-V^*\otimes_S V&\longrightarrow S,& f\otimes v&\longmapsto f(v),\\
-V\otimes_S{}^*V&\longrightarrow S,& v\otimes g&\longmapsto g(v).
-\end{aligned}
-\end{equation}
-If $V$ is finite-dimensional, the \defn{coevaluation maps} are
-\begin{equation}\label{eq:S-coevaluation}
-\begin{aligned}
-S&\longrightarrow V\otimes_S V^*\xrightarrow{\sim}\End_S(V),
-& s&\longmapsto\bigl(v\mapsto sv\bigr),\\
-S&\longrightarrow{}^*V\otimes_S V\xrightarrow{\sim}\End_{S^\op}(V),
-& s&\longmapsto\bigl(v\mapsto vs\bigr).
-\end{aligned}
-\end{equation}
-The isomorphisms are those in \eqref{eq:hom-from-S-duals}, with $W=V$.
-Both coevaluation maps are bimodule maps, and each image of $1$ corresponds to $\id_V$.
-\end{proposition}
-
-\begin{supplementary}
-\begin{proof}
-The identities $(fs)(v)=f(sv)$ and $(sg)(v)=g(vs)$ from \eqref{eq:bimodule-dual-actions} make evaluation well-defined on the two tensor products; the other two actions give its bimodule linearity.
-For coevaluation, left multiplication is right $S$-linear and right multiplication is left $S$-linear because the two actions on $V$ commute.
-Under the Hom actions in Proposition~\ref{prop:hom-from-S-duals}, both multiplication assignments preserve the two $S$-actions.
-The isomorphisms in \eqref{eq:hom-from-S-duals} therefore give the stated bimodule maps.
-\end{proof}
-\end{supplementary}
-
-\begin{advanced}
-These are the constructions in the last two paragraphs of \cite[\S2.7, pp.~484--485]{BGS96}, translated to our notation.
-
-For a locally finite-dimensional graded bimodule $ {}_SV_S$, \eqref{eq:S-coevaluation} applies to each $V_d$; a coevaluation for the whole module need not exist.
-For example, take $S\neq0$ and $V=\bigoplus_{d\geq0}S(-d)$.
-Every element $\sum_{i=1}^n v_i\otimes f_i$ of $V\otimes_S V^{\grstar}$ defines an endomorphism with image contained in the finite-dimensional submodule $\sum_{i=1}^n v_iS$, so it cannot represent $\id_V$.
-\end{advanced}
-
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
Evaluation applies a functional to an element.
Coevaluation expresses the identity endomorphism as an element of a tensor product.

\begin{proposition}\label{prop:S-evaluation-coevaluation}
\comm{not sure this is really important for the course, should it be left like this or just put as supplementary}
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

```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

Delete the existing passage; insert no text at this location.

</details>

### 1b. Lecture_Koszul_S2.tex

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:795), lines 795-844. **Changes:** +48 / -10 lines.

The proposition now immediately precedes its graded application. The proof uses $e_iA_q$ directly, without introducing $P_i$.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -795,4 +793,3 @@
-\comm{From here}
-
+\begin{supplementary}
 \begin{definition}\label{def:total-tensor-grading}
 For graded right and left $S$-modules $M,N$, their tensor product has \defn{total grading}
@@ -806,4 +803,35 @@
 When $M,N$ are locally finite-dimensional and bounded below, only finitely many pairs $(p,q)$ contribute in a fixed degree, so the tensor product is locally finite-dimensional and bounded below.
 
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
+\begin{proof}
+The identities $(fs)(v)=f(sv)$ and $(sg)(v)=g(vs)$ from \eqref{eq:bimodule-dual-actions} make evaluation well-defined on the two tensor products; the other two actions give its bimodule linearity.
+For coevaluation, left multiplication is right $S$-linear and right multiplication is left $S$-linear because the two actions on $V$ commute.
+Under the Hom actions in Proposition~\ref{prop:hom-from-S-duals}, both multiplication assignments preserve the two $S$-actions.
+The isomorphisms in \eqref{eq:hom-from-S-duals} therefore give the stated bimodule maps.
+\end{proof}
+
 For a finite-dimensional graded bimodule $ {}_SV_S$, use $V^{\grstar}$ and $ {}^{\grstar}V$ in Proposition~\ref{prop:S-evaluation-coevaluation}.
 With the total grading, evaluation and coevaluation preserve degree: evaluation pairs degrees $i$ and $-i$, and $\id_V$ has degree $0$.
@@ -811,6 +839,6 @@
 To multiply two arrays $C=(c_{ij})$ and $D=(d_{ij})$, or a row vector $m=(m_i)$ and an array $C$, use
 \[
-(CD)_{i\ell}=\sum_{j=1}^r c_{ij}d_{j\ell},
-\qquad (mC)_j=\sum_{i=1}^r m_i c_{ij}.
+(CD)_{i\ell}=\sum_{j=1}^n c_{ij}d_{j\ell},
+\qquad (mC)_j=\sum_{i=1}^n m_i c_{ij}.
 \]
 Thus multiplication sums over the matching middle index, rather than multiplying individual entries independently.
@@ -822,6 +850,6 @@
 \[
 [N\otimes_S U:L_j]
-=\sum_{i=1}^r[N:L_i][e_iU:L_j]
-\quad\text{for all }1\leq j\leq r.
+=\sum_{i=1}^n[N:L_i][e_iU:L_j]
+\quad\text{for all }1\leq j\leq n.
 \]
 For a locally finite-dimensional graded right $A$-module $M$ bounded below,
@@ -832,13 +860,21 @@
 
 \begin{proof}
-Decompose $N\cong\bigoplus_{i=1}^r(e_iS)^{\oplus[N:L_i]}$.
+Decompose $N\cong\bigoplus_{i=1}^n(e_iS)^{\oplus[N:L_i]}$.
 Multiplication $e_iS\otimes_S U\to e_iU$, $e_is\otimes u\mapsto e_isu$, is an isomorphism with inverse $u\mapsto e_i\otimes u$.
 Distribution over direct sums therefore gives
 \[
-N\otimes_S U\cong\bigoplus_{i=1}^r(e_iU)^{\oplus[N:L_i]}.
+N\otimes_S U\cong\bigoplus_{i=1}^n(e_iU)^{\oplus[N:L_i]}.
 \]
 Counting copies of $L_j$ proves the first formula.
 Apply the first formula to $M_p\otimes_S A_q$ and sum over all $p,q\in\Z$ with $p+q=d$.
-Since $e_iA_q=(P_i)_q$, the resulting coefficient is the coefficient of $t^d$ in $h_M(t)h_A(t)$.
+By the definition of $h_A(t)$, the resulting sum is the coefficient of $t^d$ in $h_M(t)h_A(t)$.
 \end{proof}
-\comm{up to here.  make as supplementary}
+\end{supplementary}
+
+\begin{advanced}
+The evaluation and coevaluation maps in Proposition~\ref{prop:S-evaluation-coevaluation} are the constructions in the last two paragraphs of \cite[\S2.7, pp.~484--485]{BGS96}, translated to our notation.
+
+For a locally finite-dimensional graded bimodule $ {}_SV_S$, \eqref{eq:S-coevaluation} applies to each $V_d$; a coevaluation for the whole module need not exist.
+For example, take $S\neq0$ and $V=\bigoplus_{d\geq0}S(-d)$.
+Every element $\sum_{i=1}^n v_i\otimes f_i$ of $V\otimes_S V^{\grstar}$ defines an endomorphism with image contained in the finite-dimensional submodule $\sum_{i=1}^n v_iS$, so it cannot represent $\id_V$.
+\end{advanced}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\comm{From here}

\begin{definition}\label{def:total-tensor-grading}
For graded right and left $S$-modules $M,N$, their tensor product has \defn{total grading}
\[
(M\otimes_S N)_d=\bigoplus_{p+q=d}M_p\otimes_S N_q.
\]
The same definition applies to bimodules, and to vector spaces by taking $S=\Bbbk$.
\end{definition}

The decomposition follows by distributing tensor products over direct sums, as in Lemma~\ref{lem:tensor-properties}(4).
When $M,N$ are locally finite-dimensional and bounded below, only finitely many pairs $(p,q)$ contribute in a fixed degree, so the tensor product is locally finite-dimensional and bounded below.

For a finite-dimensional graded bimodule $ {}_SV_S$, use $V^{\grstar}$ and $ {}^{\grstar}V$ in Proposition~\ref{prop:S-evaluation-coevaluation}.
With the total grading, evaluation and coevaluation preserve degree: evaluation pairs degrees $i$ and $-i$, and $\id_V$ has degree $0$.

To multiply two arrays $C=(c_{ij})$ and $D=(d_{ij})$, or a row vector $m=(m_i)$ and an array $C$, use
\[
(CD)_{i\ell}=\sum_{j=1}^r c_{ij}d_{j\ell},
\qquad (mC)_j=\sum_{i=1}^r m_i c_{ij}.
\]
Thus multiplication sums over the matching middle index, rather than multiplying individual entries independently.
For series, use the same products on coefficients and collect terms with the same total power of $t$.

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
\comm{up to here.  make as supplementary}
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
\begin{supplementary}
\begin{definition}\label{def:total-tensor-grading}
For graded right and left $S$-modules $M,N$, their tensor product has \defn{total grading}
\[
(M\otimes_S N)_d=\bigoplus_{p+q=d}M_p\otimes_S N_q.
\]
The same definition applies to bimodules, and to vector spaces by taking $S=\Bbbk$.
\end{definition}

The decomposition follows by distributing tensor products over direct sums, as in Lemma~\ref{lem:tensor-properties}(4).
When $M,N$ are locally finite-dimensional and bounded below, only finitely many pairs $(p,q)$ contribute in a fixed degree, so the tensor product is locally finite-dimensional and bounded below.

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

\begin{proof}
The identities $(fs)(v)=f(sv)$ and $(sg)(v)=g(vs)$ from \eqref{eq:bimodule-dual-actions} make evaluation well-defined on the two tensor products; the other two actions give its bimodule linearity.
For coevaluation, left multiplication is right $S$-linear and right multiplication is left $S$-linear because the two actions on $V$ commute.
Under the Hom actions in Proposition~\ref{prop:hom-from-S-duals}, both multiplication assignments preserve the two $S$-actions.
The isomorphisms in \eqref{eq:hom-from-S-duals} therefore give the stated bimodule maps.
\end{proof}

For a finite-dimensional graded bimodule $ {}_SV_S$, use $V^{\grstar}$ and $ {}^{\grstar}V$ in Proposition~\ref{prop:S-evaluation-coevaluation}.
With the total grading, evaluation and coevaluation preserve degree: evaluation pairs degrees $i$ and $-i$, and $\id_V$ has degree $0$.

To multiply two arrays $C=(c_{ij})$ and $D=(d_{ij})$, or a row vector $m=(m_i)$ and an array $C$, use
\[
(CD)_{i\ell}=\sum_{j=1}^n c_{ij}d_{j\ell},
\qquad (mC)_j=\sum_{i=1}^n m_i c_{ij}.
\]
Thus multiplication sums over the matching middle index, rather than multiplying individual entries independently.
For series, use the same products on coefficients and collect terms with the same total power of $t$.

\begin{lemma}\label{lem:dimension-tensor}\label{lem:hilbert-tensor}
Let $N$ be a finite-dimensional right $S$-module and ${}_SU_S$ a finite-dimensional bimodule.
Then
\[
[N\otimes_S U:L_j]
=\sum_{i=1}^n[N:L_i][e_iU:L_j]
\quad\text{for all }1\leq j\leq n.
\]
For a locally finite-dimensional graded right $A$-module $M$ bounded below,
\[
h_{M\otimes_S A}(t)=h_M(t)h_A(t).
\]
\end{lemma}

\begin{proof}
Decompose $N\cong\bigoplus_{i=1}^n(e_iS)^{\oplus[N:L_i]}$.
Multiplication $e_iS\otimes_S U\to e_iU$, $e_is\otimes u\mapsto e_isu$, is an isomorphism with inverse $u\mapsto e_i\otimes u$.
Distribution over direct sums therefore gives
\[
N\otimes_S U\cong\bigoplus_{i=1}^n(e_iU)^{\oplus[N:L_i]}.
\]
Counting copies of $L_j$ proves the first formula.
Apply the first formula to $M_p\otimes_S A_q$ and sum over all $p,q\in\Z$ with $p+q=d$.
By the definition of $h_A(t)$, the resulting sum is the coefficient of $t^d$ in $h_M(t)h_A(t)$.
\end{proof}
\end{supplementary}

\begin{advanced}
The evaluation and coevaluation maps in Proposition~\ref{prop:S-evaluation-coevaluation} are the constructions in the last two paragraphs of \cite[\S2.7, pp.~484--485]{BGS96}, translated to our notation.

For a locally finite-dimensional graded bimodule $ {}_SV_S$, \eqref{eq:S-coevaluation} applies to each $V_d$; a coevaluation for the whole module need not exist.
For example, take $S\neq0$ and $V=\bigoplus_{d\geq0}S(-d)$.
Every element $\sum_{i=1}^n v_i\otimes f_i$ of $V\otimes_S V^{\grstar}$ defines an endomorphism with image contained in the finite-dimensional submodule $\sum_{i=1}^n v_iS$, so it cannot represent $\id_V$.
\end{advanced}
```

</details>

### 1c. Lecture_Koszul_S2.tex

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:894), lines 894-921. **Changes:** +4 / -5 lines.

Keep the proof with its already supplementary statement. Here $n,m$ count the simple classes of the two different degree-zero algebras.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -898,6 +935,6 @@
 h_{U\otimes_\Bbbk W}(t)=h_U(t)h_W(t).
 \]
-Let $A,B$ be locally finite-dimensional graded algebras with $A_0=\Bbbk^{\oplus r}$ and $B_0=\Bbbk^{\oplus s}$.
-Write $e_1,\ldots,e_r$ and $f_1,\ldots,f_s$ for the coordinate idempotents.
+Let $A,B$ be locally finite-dimensional graded algebras with $A_0=\Bbbk^{\oplus n}$ and $B_0=\Bbbk^{\oplus m}$.
+Write $e_1,\ldots,e_n$ and $f_1,\ldots,f_m$ for the coordinate idempotents.
 Give $A\otimes_\Bbbk B$ the total grading and multiplication
 $(a\otimes b)(a'\otimes b')=aa'\otimes bb'$.
@@ -906,9 +943,7 @@
 h_{A\otimes_\Bbbk B}(t)_{(i,p),(j,q)}
 =h_A(t)_{ij}h_B(t)_{pq}
-\quad(1\leq i,j\leq r,\ 1\leq p,q\leq s).
+\quad\text{for all }1\leq i,j\leq n,\ 1\leq p,q\leq m.
 \]
 \end{lemma}
-\end{supplementary}
-
 \begin{proof}
 For vector spaces, take dimensions in each summand of the total grading.
@@ -920,2 +955,3 @@
 Take vector space dimensions and sum over $a+b=d$ to obtain the coefficient of $t^d$.
 \end{proof}
+\end{supplementary}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{supplementary}
\begin{lemma}\label{lem:hilbert-field-tensor}
For locally finite-dimensional graded vector spaces $U,W$ bounded below,
\[
h_{U\otimes_\Bbbk W}(t)=h_U(t)h_W(t).
\]
Let $A,B$ be locally finite-dimensional graded algebras with $A_0=\Bbbk^{\oplus r}$ and $B_0=\Bbbk^{\oplus s}$.
Write $e_1,\ldots,e_r$ and $f_1,\ldots,f_s$ for the coordinate idempotents.
Give $A\otimes_\Bbbk B$ the total grading and multiplication
$(a\otimes b)(a'\otimes b')=aa'\otimes bb'$.
Then
\[
h_{A\otimes_\Bbbk B}(t)_{(i,p),(j,q)}
=h_A(t)_{ij}h_B(t)_{pq}
\quad(1\leq i,j\leq r,\ 1\leq p,q\leq s).
\]
\end{lemma}
\end{supplementary}

\begin{proof}
For vector spaces, take dimensions in each summand of the total grading.
For algebras,
\[
(e_i\otimes f_p)(A_a\otimes_\Bbbk B_b)(e_j\otimes f_q)
=(e_iA_ae_j)\otimes_\Bbbk(f_pB_bf_q).
\]
Take vector space dimensions and sum over $a+b=d$ to obtain the coefficient of $t^d$.
\end{proof}
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
\begin{supplementary}
\begin{lemma}\label{lem:hilbert-field-tensor}
For locally finite-dimensional graded vector spaces $U,W$ bounded below,
\[
h_{U\otimes_\Bbbk W}(t)=h_U(t)h_W(t).
\]
Let $A,B$ be locally finite-dimensional graded algebras with $A_0=\Bbbk^{\oplus n}$ and $B_0=\Bbbk^{\oplus m}$.
Write $e_1,\ldots,e_n$ and $f_1,\ldots,f_m$ for the coordinate idempotents.
Give $A\otimes_\Bbbk B$ the total grading and multiplication
$(a\otimes b)(a'\otimes b')=aa'\otimes bb'$.
Then
\[
h_{A\otimes_\Bbbk B}(t)_{(i,p),(j,q)}
=h_A(t)_{ij}h_B(t)_{pq}
\quad\text{for all }1\leq i,j\leq n,\ 1\leq p,q\leq m.
\]
\end{lemma}
\begin{proof}
For vector spaces, take dimensions in each summand of the total grading.
For algebras,
\[
(e_i\otimes f_p)(A_a\otimes_\Bbbk B_b)(e_j\otimes f_q)
=(e_iA_ae_j)\otimes_\Bbbk(f_pB_bf_q).
\]
Take vector space dimensions and sum over $a+b=d$ to obtain the coefficient of $t^d$.
\end{proof}
\end{supplementary}
```

</details>

---

<a id="replacement-2"></a>
## Replacement 2: Name anti-distributivity explicitly

Use the requested name for the order-reversing $S$-dual comparison. The three central formulas and their labels remain unchanged; later terminology-only replacements are listed in the mechanical-change table.

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:339), lines 339-351. **Changes:** +2 / -1 lines.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -339,5 +339,5 @@
 Let $S$ be finite-dimensional semisimple, and consider bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively.
 Corollary~\ref{cor:semisimple-summands} gives $V_S\in\add S$ and ${}_SW\in\add_{\mod S^\op}(S)$.
-Thus the semisimple case of tensor duality, Proposition~\ref{prop:tensor-duals}, gives natural bimodule isomorphisms \comm{you always call this tensor-dual isomorphism, but this name is very ambiguous... it is more like anti-distributivity of $S$-dual over tensor-over-$S$.  you can use emphasise on this phrase to make it more easy to remember, if you need to use word, then say ``we refer to this as anti-distributivity of $S$-dual" from now on; then apply changes for any further use of this (whenever you say `tensor-dual isom', it should be clarified)}
+Proposition~\ref{prop:tensor-duals} therefore gives natural bimodule isomorphisms
 \begin{equation}\label{eq:tensor-duals}
 \theta_r:W^*\otimes_S V^*\xrightarrow{\sim}(V\otimes_S W)^*,
@@ -350,2 +350,3 @@
 \theta_\ell(g\otimes f)(v\otimes w)=f(vg(w)).
 \end{equation}
+We refer to \eqref{eq:tensor-duals} as \emph{anti-distributivity of the $S$-dual over $\otimes_S$}: dualising reverses the order of the factors.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
Let $S$ be finite-dimensional semisimple, and consider bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively.
Corollary~\ref{cor:semisimple-summands} gives $V_S\in\add S$ and ${}_SW\in\add_{\mod S^\op}(S)$.
Thus the semisimple case of tensor duality, Proposition~\ref{prop:tensor-duals}, gives natural bimodule isomorphisms \comm{you always call this tensor-dual isomorphism, but this name is very ambiguous... it is more like anti-distributivity of $S$-dual over tensor-over-$S$.  you can use emphasise on this phrase to make it more easy to remember, if you need to use word, then say ``we refer to this as anti-distributivity of $S$-dual" from now on; then apply changes for any further use of this (whenever you say `tensor-dual isom', it should be clarified)}
\begin{equation}\label{eq:tensor-duals}
\theta_r:W^*\otimes_S V^*\xrightarrow{\sim}(V\otimes_S W)^*,
\qquad
\theta_\ell:{}^*W\otimes_S{}^*V\xrightarrow{\sim}{}^*(V\otimes_S W),
\end{equation}
\begin{equation}\label{eq:tensor-evaluations}
\theta_r(g\otimes f)(v\otimes w)=g(f(v)w),
\qquad
\theta_\ell(g\otimes f)(v\otimes w)=f(vg(w)).
\end{equation}
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
Let $S$ be finite-dimensional semisimple, and consider bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively.
Corollary~\ref{cor:semisimple-summands} gives $V_S\in\add S$ and ${}_SW\in\add_{\mod S^\op}(S)$.
Proposition~\ref{prop:tensor-duals} therefore gives natural bimodule isomorphisms
\begin{equation}\label{eq:tensor-duals}
\theta_r:W^*\otimes_S V^*\xrightarrow{\sim}(V\otimes_S W)^*,
\qquad
\theta_\ell:{}^*W\otimes_S{}^*V\xrightarrow{\sim}{}^*(V\otimes_S W),
\end{equation}
\begin{equation}\label{eq:tensor-evaluations}
\theta_r(g\otimes f)(v\otimes w)=g(f(v)w),
\qquad
\theta_\ell(g\otimes f)(v\otimes w)=f(vg(w)).
\end{equation}
We refer to \eqref{eq:tensor-duals} as \emph{anti-distributivity of the $S$-dual over $\otimes_S$}: dualising reverses the order of the factors.
```

</details>

---

<a id="replacement-3"></a>
## Replacement 3: Make the tensor grading explicit in the definition

State at the definition, before the universal property, that the tensor algebra is graded. Name the tensor grading and specify degrees 0 and 1.

### 3a. Lecture_Koszul_S2.tex

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:490), lines 490-515. **Changes:** +4 / -2 lines.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -490,5 +491,5 @@
 \begin{definition}\label{def:tensor-algebra}
 Let $S$ be a $\Bbbk$-algebra and consider a bimodule ${}_SV_S$.
-The \defn{tensor algebra of $V$ over $S$} is
+The \defn{tensor algebra of $V$ over $S$} is the graded $\Bbbk$-algebra
 \[
 T_S(V):=\bigoplus_{i\in\Z}T_S(V)_i,
@@ -505,9 +506,11 @@
 (v_1\otimes_S\cdots\otimes_S v_p)(v_{p+1}\otimes_S\cdots\otimes_S v_{p+q})
 =v_1\otimes_S\cdots\otimes_S v_{p+q}
-\qquad(p,q\geq1),
+\qquad\text{for all }p,q\geq1,
 \]
 and by the left and right $S$-actions when a factor has degree $0$.
 \end{definition}
 
+The displayed decomposition is the \defn{tensor grading}: $S=T_S(V)_0$ and $V=T_S(V)_1$.
+Multiplication satisfies $T_S(V)_pT_S(V)_q\subset T_S(V)_{p+q}$ for all $p,q\in\Z$.
 We also call $T_S(V)$ the tensor algebra generated by $V$ over $S$.
 Every element has finitely many non-zero homogeneous components.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{definition}\label{def:tensor-algebra}
Let $S$ be a $\Bbbk$-algebra and consider a bimodule ${}_SV_S$.
The \defn{tensor algebra of $V$ over $S$} is
\[
T_S(V):=\bigoplus_{i\in\Z}T_S(V)_i,
\quad\text{where}\quad
T_S(V)_i=
\begin{cases}
V^{\otimes_S i},&i\geq1,\\
S,&i=0,\\
0,&i<0,
\end{cases}.
\]
For $v_1,\ldots,v_{p+q}\in V$, multiplication is determined $\Bbbk$-bilinearly by
\[
(v_1\otimes_S\cdots\otimes_S v_p)(v_{p+1}\otimes_S\cdots\otimes_S v_{p+q})
=v_1\otimes_S\cdots\otimes_S v_{p+q}
\qquad(p,q\geq1),
\]
and by the left and right $S$-actions when a factor has degree $0$.
\end{definition}

We also call $T_S(V)$ the tensor algebra generated by $V$ over $S$.
Every element has finitely many non-zero homogeneous components.
The unit is $1_S$, and associativity follows from Lemma~\ref{lem:tensor-properties}(3).
Write $v_1\cdots v_d$ for $v_1\otimes_S\cdots\otimes_S v_d$ in $T_S(V)$.
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
\begin{definition}\label{def:tensor-algebra}
Let $S$ be a $\Bbbk$-algebra and consider a bimodule ${}_SV_S$.
The \defn{tensor algebra of $V$ over $S$} is the graded $\Bbbk$-algebra
\[
T_S(V):=\bigoplus_{i\in\Z}T_S(V)_i,
\quad\text{where}\quad
T_S(V)_i=
\begin{cases}
V^{\otimes_S i},&i\geq1,\\
S,&i=0,\\
0,&i<0,
\end{cases}.
\]
For $v_1,\ldots,v_{p+q}\in V$, multiplication is determined $\Bbbk$-bilinearly by
\[
(v_1\otimes_S\cdots\otimes_S v_p)(v_{p+1}\otimes_S\cdots\otimes_S v_{p+q})
=v_1\otimes_S\cdots\otimes_S v_{p+q}
\qquad\text{for all }p,q\geq1,
\]
and by the left and right $S$-actions when a factor has degree $0$.
\end{definition}

The displayed decomposition is the \defn{tensor grading}: $S=T_S(V)_0$ and $V=T_S(V)_1$.
Multiplication satisfies $T_S(V)_pT_S(V)_q\subset T_S(V)_{p+q}$ for all $p,q\in\Z$.
We also call $T_S(V)$ the tensor algebra generated by $V$ over $S$.
Every element has finitely many non-zero homogeneous components.
The unit is $1_S$, and associativity follows from Lemma~\ref{lem:tensor-properties}(3).
Write $v_1\cdots v_d$ for $v_1\otimes_S\cdots\otimes_S v_d$ in $T_S(V)$.
```

</details>

### 3b. Lecture_Koszul_S2.tex

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:594), lines 594-595. **Changes:** +0 / -2 lines.

Remove the comment once the grading is stated in the definition.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -594,2 +596,0 @@
-\comm{at some point before universal property prop, it should be clarified that tensor algebra is a graded algebra.  the current definition just says something of degree 0, without saying degree 0 in where.  If necessary, we will refer to the canonical grading structure $\deg S=0, \deg V=1$ as tensor grading.}
-
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\comm{at some point before universal property prop, it should be clarified that tensor algebra is a graded algebra.  the current definition just says something of degree 0, without saying degree 0 in where.  If necessary, we will refer to the canonical grading structure $\deg S=0, \deg V=1$ as tensor grading.}

```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

Delete the existing passage; insert no text at this location.

</details>

---

<a id="replacement-4"></a>
## Replacement 4: Put the kernel and quotient assertions in the corollary

Use the agreed arrangement: the corollary states the homogeneous-kernel and quotient facts, while the definition only names the ideal of relations. Write $A_1$, not an unspecified $V$, in the canonical presentation.

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:628), lines 628-662. **Changes:** +7 / -8 lines.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -634,4 +635,8 @@
 \]
 Its degree $i$ component is $\mu_i$ from \eqref{eq:multiplication-maps}.
+The kernel $I:=\Ker\mu$ is homogeneous, $I_0=I_1=0$, and $\mu$ induces a graded algebra isomorphism
+\[
+T_S(A_1)/I\xrightarrow{\sim}A,\qquad z+I\longmapsto\mu(z).
+\]
 \end{corollary}
 
@@ -645,4 +650,6 @@
 Then \eqref{eq:tensor-extension} gives $\widetilde f=\mu$.
 The map $\mu$ preserves degrees, and each component $\mu_i$ is surjective by the assumption that $A$ is generated in degree $1$.
+Thus $\Ker\mu$ is homogeneous, and $\mu_0=\id_S$, $\mu_1=\id_{A_1}$ give $I_0=I_1=0$.
+The map $z+I\mapsto\mu(z)$ is therefore a degree-preserving bijective algebra homomorphism.
 \end{proof}
 \end{supplementary}
@@ -652,11 +659,4 @@
 \end{definition}
 
-\comm{this paragraph, up to `Homegentiy is essential...', should be inside the corollary??}
-Note that $I_0=I_1=0$ since $\mu_0=\id_S$ and $\mu_1=\id_{V=A_1}$.
-Since $\mu$ preserves degrees, its kernel is homogeneous, and
-\[
-T_S(V)/I\xrightarrow{\sim}A,\qquad z+I\longmapsto\mu(z)
-\]
-is a graded algebra isomorphism.
-The bimodule $V$ specifies the generators and their left and right $S$-actions; $I$ specifies the relations between their products.
+The bimodule $A_1$ specifies the generators and their left and right $S$-actions; $I$ specifies the relations between their products.
 Homogeneity is essential for the quotient grading: the relation $x-x^2$ in Example~\ref{ex:nonhomogeneous-ideal} does not satisfy this condition.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{corollary}\label{cor:tensor-presentation}
If $A$ is generated in degree $1$ over $S=A_0$, then the multiplication map defines a surjective graded algebra homomorphism
\[
\mu:T_S(A_1)\onto A,\qquad \mu|_S=\id_S, \qquad 
a_1\otimes_S\cdots\otimes_S a_i\longmapsto a_1\cdots a_i
\quad \forall i\geq1.
\]
Its degree $i$ component is $\mu_i$ from \eqref{eq:multiplication-maps}.
\end{corollary}

\begin{supplementary}
\begin{proof}
In Proposition~\ref{prop:tensor-universal}, take $V=A_1$, $B=A$, and the inclusions
\[
\varphi:S\hookrightarrow A,\quad s\longmapsto s,
\qquad f:A_1\hookrightarrow A,\quad a\longmapsto a.
\]
Then \eqref{eq:tensor-extension} gives $\widetilde f=\mu$.
The map $\mu$ preserves degrees, and each component $\mu_i$ is surjective by the assumption that $A$ is generated in degree $1$.
\end{proof}
\end{supplementary}

\begin{definition}\label{def:relations}
For the map $\mu$ in Corollary~\ref{cor:tensor-presentation}, the homogeneous two-sided ideal $I:=\Ker\mu$ is the \defn{ideal of relations}.
\end{definition}

\comm{this paragraph, up to `Homegentiy is essential...', should be inside the corollary??}
Note that $I_0=I_1=0$ since $\mu_0=\id_S$ and $\mu_1=\id_{V=A_1}$.
Since $\mu$ preserves degrees, its kernel is homogeneous, and
\[
T_S(V)/I\xrightarrow{\sim}A,\qquad z+I\longmapsto\mu(z)
\]
is a graded algebra isomorphism.
The bimodule $V$ specifies the generators and their left and right $S$-actions; $I$ specifies the relations between their products.
Homogeneity is essential for the quotient grading: the relation $x-x^2$ in Example~\ref{ex:nonhomogeneous-ideal} does not satisfy this condition.
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
\begin{corollary}\label{cor:tensor-presentation}
If $A$ is generated in degree $1$ over $S=A_0$, then the multiplication map defines a surjective graded algebra homomorphism
\[
\mu:T_S(A_1)\onto A,\qquad \mu|_S=\id_S, \qquad 
a_1\otimes_S\cdots\otimes_S a_i\longmapsto a_1\cdots a_i
\quad \forall i\geq1.
\]
Its degree $i$ component is $\mu_i$ from \eqref{eq:multiplication-maps}.
The kernel $I:=\Ker\mu$ is homogeneous, $I_0=I_1=0$, and $\mu$ induces a graded algebra isomorphism
\[
T_S(A_1)/I\xrightarrow{\sim}A,\qquad z+I\longmapsto\mu(z).
\]
\end{corollary}

\begin{supplementary}
\begin{proof}
In Proposition~\ref{prop:tensor-universal}, take $V=A_1$, $B=A$, and the inclusions
\[
\varphi:S\hookrightarrow A,\quad s\longmapsto s,
\qquad f:A_1\hookrightarrow A,\quad a\longmapsto a.
\]
Then \eqref{eq:tensor-extension} gives $\widetilde f=\mu$.
The map $\mu$ preserves degrees, and each component $\mu_i$ is surjective by the assumption that $A$ is generated in degree $1$.
Thus $\Ker\mu$ is homogeneous, and $\mu_0=\id_S$, $\mu_1=\id_{A_1}$ give $I_0=I_1=0$.
The map $z+I\mapsto\mu(z)$ is therefore a degree-preserving bijective algebra homomorphism.
\end{proof}
\end{supplementary}

\begin{definition}\label{def:relations}
For the map $\mu$ in Corollary~\ref{cor:tensor-presentation}, the homogeneous two-sided ideal $I:=\Ker\mu$ is the \defn{ideal of relations}.
\end{definition}

The bimodule $A_1$ specifies the generators and their left and right $S$-actions; $I$ specifies the relations between their products.
Homogeneity is essential for the quotient grading: the relation $x-x^2$ in Example~\ref{ex:nonhomogeneous-ideal} does not satisfy this condition.
```

</details>

---

<a id="replacement-5"></a>
## Replacement 5: Keep the Hilbert-series notation one-sided and precise

Choose one representative of each simple right $S$-module class, not an arbitrary list of primitive idempotents. The degree components are viewed through $A\to S$, and each row of $h_A$ counts composition factors of $e_iA$. No separate bimodule dimension vector or $P_i$ notation is introduced.

### 5a. Lecture_Koszul_S2.tex

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:719), lines 719-732. **Changes:** +5 / -7 lines.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -719,14 +719,12 @@
-\comm{TODO: throughout, use $n$ instead of $r$ for number of simples?  Avoid using $P_i$, and just stick with $e_iA$.}
-
 Let $A$ be a locally finite-dimensional graded algebra with $S=A_0$ finite-dimensional semisimple.
-Then each degree piece of a graded right $A$-module is semisimple as $A$-module.  We call the simple direct summands in a direct sum decomposition of $M_d$  \defn{composition factors}.
+For a graded right $A$-module $M$, regard $M_d$ as an $A$-module via $A\to A/A_+=S$.
+The simple direct summands of the semisimple module $M_d$ are its \defn{composition factors}.
 
 \begin{notation}
-By Theorem~\ref{thm:artin-wedderburn}, choose primitive idempotents $e_1,\ldots,e_r\in S$.  Then  
-\[L_j:=e_jS\cong e_j A/e_jA_+\]
-gives the full list of isomorphism class of (graded) simple right $S$-modules.
+By Theorem~\ref{thm:artin-wedderburn}, choose primitive idempotents $e_1,\ldots,e_n\in S$ such that $e_1S,\ldots,e_nS$ represent the simple right $S$-modules once each.
+Then $L_j:=e_jS\cong e_jA/e_jA_+$ is a graded simple $A$-module concentrated in degree $0$ for every $1\leq j\leq n$.
 \phantomsection\label{not:hilbert-simples-summands}
 \end{notation}
 
 \begin{definition}\label{def:dimension-vector}\label{def:hilbert-series}
-For a locally finite-dimensional graded right $A$-module $M$ with primitive idempotent $e_1, \ldots e_r$, write $[M_d:L_j]$ for the multiplicity of the composition factor $L_j$ in $M_d$.
+For a locally finite-dimensional graded right $A$-module $M$, write $[M_d:L_j]$ for the multiplicity of the composition factor $L_j$ in $M_d$.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\comm{TODO: throughout, use $n$ instead of $r$ for number of simples?  Avoid using $P_i$, and just stick with $e_iA$.}

Let $A$ be a locally finite-dimensional graded algebra with $S=A_0$ finite-dimensional semisimple.
Then each degree piece of a graded right $A$-module is semisimple as $A$-module.  We call the simple direct summands in a direct sum decomposition of $M_d$  \defn{composition factors}.

\begin{notation}
By Theorem~\ref{thm:artin-wedderburn}, choose primitive idempotents $e_1,\ldots,e_r\in S$.  Then  
\[L_j:=e_jS\cong e_j A/e_jA_+\]
gives the full list of isomorphism class of (graded) simple right $S$-modules.
\phantomsection\label{not:hilbert-simples-summands}
\end{notation}

\begin{definition}\label{def:dimension-vector}\label{def:hilbert-series}
For a locally finite-dimensional graded right $A$-module $M$ with primitive idempotent $e_1, \ldots e_r$, write $[M_d:L_j]$ for the multiplicity of the composition factor $L_j$ in $M_d$.
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
Let $A$ be a locally finite-dimensional graded algebra with $S=A_0$ finite-dimensional semisimple.
For a graded right $A$-module $M$, regard $M_d$ as an $A$-module via $A\to A/A_+=S$.
The simple direct summands of the semisimple module $M_d$ are its \defn{composition factors}.

\begin{notation}
By Theorem~\ref{thm:artin-wedderburn}, choose primitive idempotents $e_1,\ldots,e_n\in S$ such that $e_1S,\ldots,e_nS$ represent the simple right $S$-modules once each.
Then $L_j:=e_jS\cong e_jA/e_jA_+$ is a graded simple $A$-module concentrated in degree $0$ for every $1\leq j\leq n$.
\phantomsection\label{not:hilbert-simples-summands}
\end{notation}

\begin{definition}\label{def:dimension-vector}\label{def:hilbert-series}
For a locally finite-dimensional graded right $A$-module $M$, write $[M_d:L_j]$ for the multiplicity of the composition factor $L_j$ in $M_d$.
```

</details>

### 5b. Lecture_Koszul_S2.tex

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:751), line 751. **Changes:** +1 / -1 lines.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -751,1 +749,1 @@
-We think of the Hilbert series as ``graded dimension matrix" with one indecomposable per row. 
+Row $i$ of $h_A(t)$ records the composition factors of $e_iA$ degree by degree.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
We think of the Hilbert series as ``graded dimension matrix" with one indecomposable per row. 
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
Row $i$ of $h_A(t)$ records the composition factors of $e_iA$ degree by degree.
```

</details>

---

<a id="replacement-6"></a>
## Replacement 6: Correct the matrix-algebra specialisation

For a matrix algebra, the relevant number is the multiplicity $[eV:eS]$, not $\dim_\Bbbk V$. Keep a noncommutative example by taking $V=S^{\oplus m}$.

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:863), line 863. **Changes:** +3 / -1 lines.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -863,1 +899,3 @@
-When $S=\Mat_n(\Bbbk)$ and $\dim_\Bbbk V=m$, the formula specialises to $h_{T_\Bbbk(V)}(t)=1/(1-mt)$.
+For $S=\Mat_d(\Bbbk)$, take the bimodule $V=S^{\oplus m}$ and $e=e_{11}$.
+There is one simple right $S$-module $eS$, and $[eV:eS]=m$, whereas $\dim_\Bbbk V=md^2$.
+Hence $h_{T_S(V)}(t)=1/(1-mt)$.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
When $S=\Mat_n(\Bbbk)$ and $\dim_\Bbbk V=m$, the formula specialises to $h_{T_\Bbbk(V)}(t)=1/(1-mt)$.
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
For $S=\Mat_d(\Bbbk)$, take the bimodule $V=S^{\oplus m}$ and $e=e_{11}$.
There is one simple right $S$-module $eS$, and $[eV:eS]=m$, whereas $\dim_\Bbbk V=md^2$.
Hence $h_{T_S(V)}(t)=1/(1-mt)$.
```

</details>

---

<a id="replacement-7"></a>
## Replacement 7: Add Homework 1, Question 4(2), with a hidden solution

Insert the two-part exercise after the present part (1). The positive result uses general semisimple $S$ and a specified bimodule isomorphism $V\cong A_1$, as requested. The counterexample isolates the degree-1 generation hypothesis. Keep the current hidden-solution setting unchanged.

### 7a. Homework1.tex

**Source:** [Homework1.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Homework1.tex:277), lines 277-285. **Changes:** +5 / -7 lines.

```diff
--- a/Homework1.tex
+++ b/Homework1.tex
@@ -277,9 +277,7 @@
-The following parts are independent. Throughout this sheet, for an algebra
-$A=\bigoplus_{d\geq0}A_d$ with $A_0=\bigoplus_{i=1}^r\kk e_i$, use
+When $A_0=\bigoplus_{i=1}^n\kk e_i$ with coordinate idempotents,
 \[
-  h_A(t)_{ij}=\sum_{d\geq0}\dim_{\kk}(e_iA_de_j)t^d
-  \qquad(1\leq i,j\leq r),
+  h_A(t)_{ij}=\sum_{d\geq0}[e_iA_d:e_jA_0]t^d
+  =\sum_{d\geq0}\dim_{\kk}(e_iA_de_j)t^d
+  \quad\text{for all }1\leq i,j\leq n.
 \]
-with the idempotents in their listed order. Thus the coefficient of $t^d$
-is the dimension vector of the $A_0$-bimodule $A_d$, recorded with two
-indices as in Lecture~2. When $A_0=\kk$, there is just one entry.
+Use the listed order of the idempotents. When $A_0=\kk$, there is just one entry.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
The following parts are independent. Throughout this sheet, for an algebra
$A=\bigoplus_{d\geq0}A_d$ with $A_0=\bigoplus_{i=1}^r\kk e_i$, use
\[
  h_A(t)_{ij}=\sum_{d\geq0}\dim_{\kk}(e_iA_de_j)t^d
  \qquad(1\leq i,j\leq r),
\]
with the idempotents in their listed order. Thus the coefficient of $t^d$
is the dimension vector of the $A_0$-bimodule $A_d$, recorded with two
indices as in Lecture~2. When $A_0=\kk$, there is just one entry.
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
When $A_0=\bigoplus_{i=1}^n\kk e_i$ with coordinate idempotents,
\[
  h_A(t)_{ij}=\sum_{d\geq0}[e_iA_d:e_jA_0]t^d
  =\sum_{d\geq0}\dim_{\kk}(e_iA_de_j)t^d
  \quad\text{for all }1\leq i,j\leq n.
\]
Use the listed order of the idempotents. When $A_0=\kk$, there is just one entry.
```

</details>

### 7b. Homework1.tex

**Source:** [Homework1.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Homework1.tex:290), line 290. **Changes:** +44 / -0 lines.

```diff
--- a/Homework1.tex
+++ b/Homework1.tex
@@ -290,1 +288,45 @@
 
+\part Equality of Hilbert series detects a tensor algebra when the degree $1$ generators are fixed.
+\begin{subparts}
+\subpart Let $A$ be a locally finite-dimensional graded algebra generated in degree $1$ over the finite-dimensional semisimple algebra $S=A_0$.
+Fix a bimodule $ {}_SV_S$ and an $S$-bimodule isomorphism $\varphi:V\xrightarrow{\sim}A_1$.
+Prove that
+\[
+h_A(t)=h_{T_S(V)}(t)
+\quad\Longrightarrow\quad
+T_S(V)\xrightarrow{\sim}A,
+\]
+where the isomorphism is induced by $\id_S$ and $\varphi$ and fixes $S$.
+\subpart Show that the degree $1$ generation hypothesis cannot be omitted: construct a graded algebra $B$ with $B_0=\kk$, $\dim_\kk B_1=1$, and a generator in degree $2$, such that
+\[
+h_B(t)=h_{T_\kk(B_1)}(t)
+\qquad\text{but}\qquad B\not\cong T_\kk(B_1)
+\]
+as graded algebras.
+\end{subparts}
+\emph{Hint.} For (a), use the tensor-presentation corollary and count composition factors of its kernel in each degree. For (b), consider $\kk[x,z]/(x^2)$ with $\deg x=1$ and $\deg z=2$.
+
+\begin{solution}
+For (a), the universal property gives a surjective graded algebra map
+$\mu:T_S(V)\to A$ with $\mu|_S=\id_S$ and $\mu|_V=\varphi$.
+Put $K=\ker\mu$, and choose primitive idempotents $e_1,\ldots,e_n\in S$ so that the $e_iS$ represent the simple right $S$-modules once each.
+For every $d\geq0$ and $1\leq i\leq n$,
+\[
+0\longrightarrow e_iK_d\longrightarrow e_iT_S(V)_d
+\longrightarrow e_iA_d\longrightarrow0
+\]
+is exact as a sequence of right $S$-modules.
+Equality of Hilbert series gives $[e_iK_d:e_jS]=0$ for every $1\leq j\leq n$, hence $e_iK_d=0$.
+Since the $e_i$ include a primitive idempotent in each matrix factor of $S$, Artin--Wedderburn gives $S(\sum_{i=1}^n e_i)S=S$.
+Therefore $K_d=0$ for every $d$, and $\mu$ is an isomorphism.
+
+For (b), let $B=\kk[x,z]/(x^2)$ with the stated degrees, writing $x,z$ also for their residue classes.
+The elements $\{z^q,xz^q\mid q\geq0\}$ form a basis, so
+\[
+h_B(t)=\sum_{q\geq0}(t^{2q}+t^{2q+1})
+=\frac{1}{1-t}=h_{T_\kk(B_1)}(t).
+\]
+Here $B_1=\kk x$, but $z$ does not belong to the subalgebra generated by $x$.
+Also $x\neq0$ and $x^2=0$, whereas non-zero polynomials in $T_\kk(B_1)\cong\kk[t]$ have non-zero squares.
+\end{solution}
+
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex

```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex

\part Equality of Hilbert series detects a tensor algebra when the degree $1$ generators are fixed.
\begin{subparts}
\subpart Let $A$ be a locally finite-dimensional graded algebra generated in degree $1$ over the finite-dimensional semisimple algebra $S=A_0$.
Fix a bimodule $ {}_SV_S$ and an $S$-bimodule isomorphism $\varphi:V\xrightarrow{\sim}A_1$.
Prove that
\[
h_A(t)=h_{T_S(V)}(t)
\quad\Longrightarrow\quad
T_S(V)\xrightarrow{\sim}A,
\]
where the isomorphism is induced by $\id_S$ and $\varphi$ and fixes $S$.
\subpart Show that the degree $1$ generation hypothesis cannot be omitted: construct a graded algebra $B$ with $B_0=\kk$, $\dim_\kk B_1=1$, and a generator in degree $2$, such that
\[
h_B(t)=h_{T_\kk(B_1)}(t)
\qquad\text{but}\qquad B\not\cong T_\kk(B_1)
\]
as graded algebras.
\end{subparts}
\emph{Hint.} For (a), use the tensor-presentation corollary and count composition factors of its kernel in each degree. For (b), consider $\kk[x,z]/(x^2)$ with $\deg x=1$ and $\deg z=2$.

\begin{solution}
For (a), the universal property gives a surjective graded algebra map
$\mu:T_S(V)\to A$ with $\mu|_S=\id_S$ and $\mu|_V=\varphi$.
Put $K=\ker\mu$, and choose primitive idempotents $e_1,\ldots,e_n\in S$ so that the $e_iS$ represent the simple right $S$-modules once each.
For every $d\geq0$ and $1\leq i\leq n$,
\[
0\longrightarrow e_iK_d\longrightarrow e_iT_S(V)_d
\longrightarrow e_iA_d\longrightarrow0
\]
is exact as a sequence of right $S$-modules.
Equality of Hilbert series gives $[e_iK_d:e_jS]=0$ for every $1\leq j\leq n$, hence $e_iK_d=0$.
Since the $e_i$ include a primitive idempotent in each matrix factor of $S$, Artin--Wedderburn gives $S(\sum_{i=1}^n e_i)S=S$.
Therefore $K_d=0$ for every $d$, and $\mu$ is an isomorphism.

For (b), let $B=\kk[x,z]/(x^2)$ with the stated degrees, writing $x,z$ also for their residue classes.
The elements $\{z^q,xz^q\mid q\geq0\}$ form a basis, so
\[
h_B(t)=\sum_{q\geq0}(t^{2q}+t^{2q+1})
=\frac{1}{1-t}=h_{T_\kk(B_1)}(t).
\]
Here $B_1=\kk x$, but $z$ does not belong to the subalgebra generated by $x$.
Also $x\neq0$ and $x^2=0$, whereas non-zero polynomials in $T_\kk(B_1)\cong\kk[t]$ have non-zero squares.
\end{solution}

```

</details>

### 7c. Lecture_Koszul_S2.tex

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:866), lines 866-867. **Changes:** +0 / -2 lines.

Remove the lecture comment after the exercise is added to Homework 1.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -866,2 +903,0 @@
-\comm{make an exercise to show that if $A$ is generated in degree 1, then $h_A=h_{T_S(V)}$ yields isom $A\cong T_S(V)$, and another part of the exercise show an example when this is false if there is generator in degree 2.  put this exercise into homework 1 Q4 after part (1) before the current (2)}
-
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\comm{make an exercise to show that if $A$ is generated in degree 1, then $h_A=h_{T_S(V)}$ yields isom $A\cong T_S(V)$, and another part of the exercise show an example when this is false if there is generator in degree 2.  put this exercise into homework 1 Q4 after part (1) before the current (2)}

```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

Delete the existing passage; insert no text at this location.

</details>

---

<a id="replacement-8"></a>
## Replacement 8: Explain why the quadratic dual is independent of presentation

Display both dual-generator spaces and both annihilators, including their ambient spaces. Use $S$-preserving as ordinary descriptive wording, without introducing a definition.

**Source:** [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:46), lines 46-48. **Changes:** +11 / -2 lines.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -46,3 +46,12 @@
 By Proposition~\ref{prop:quadratic-basic}, a quadratic presentation identifies $S$ with $A_0$, $V$ with $A_1$, and $R$ with $\Ker\mu_2$, where $\mu_2:A_1\otimes_{A_0}A_1\to A_2$ is \eqref{eq:multiplication-maps}.
-The natural isomorphisms \eqref{eq:tensor-duals} therefore make the quadratic dual independent of the chosen presentation up to isomorphism.\comm{this is just saying quadratic dual is indept of presentation of $A$ because of universal property of tensor algebra, combine with $R\cong \Ker(\mu_2)$???}
-An isomorphism \defn{over $S$} means one restricting to $\id_S$ on degree $0$.\comm{use `$S$-preserving isomorphism' instead}
+Under $S\cong A_0$ and $V\cong A_1$, anti-distributivity \eqref{eq:tensor-duals} gives
+\[
+\begin{aligned}
+V^*&\cong A_1^*,&
+R^\perp&\cong(\Ker\mu_2)^\perp\subset A_1^*\otimes_{A_0}A_1^*,\\
+{}^*V&\cong{}^*(A_1),&
+{}^\perp R&\cong{}^\perp(\Ker\mu_2)\subset{}^*(A_1)\otimes_{A_0}{}^*(A_1).
+\end{aligned}
+\]
+Proposition~\ref{prop:tensor-universal} extends $V^*\cong A_1^*$ and $ {}^*V\cong{}^*(A_1)$ to tensor-algebra isomorphisms, which descend to the quotients by $(R^\perp)$ and $({}^\perp R)$, respectively.
+Thus both quadratic duals are independent of the chosen presentation up to $A_0$-preserving isomorphisms of graded algebras.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
By Proposition~\ref{prop:quadratic-basic}, a quadratic presentation identifies $S$ with $A_0$, $V$ with $A_1$, and $R$ with $\Ker\mu_2$, where $\mu_2:A_1\otimes_{A_0}A_1\to A_2$ is \eqref{eq:multiplication-maps}.
The natural isomorphisms \eqref{eq:tensor-duals} therefore make the quadratic dual independent of the chosen presentation up to isomorphism.\comm{this is just saying quadratic dual is indept of presentation of $A$ because of universal property of tensor algebra, combine with $R\cong \Ker(\mu_2)$???}
An isomorphism \defn{over $S$} means one restricting to $\id_S$ on degree $0$.\comm{use `$S$-preserving isomorphism' instead}
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
By Proposition~\ref{prop:quadratic-basic}, a quadratic presentation identifies $S$ with $A_0$, $V$ with $A_1$, and $R$ with $\Ker\mu_2$, where $\mu_2:A_1\otimes_{A_0}A_1\to A_2$ is \eqref{eq:multiplication-maps}.
Under $S\cong A_0$ and $V\cong A_1$, anti-distributivity \eqref{eq:tensor-duals} gives
\[
\begin{aligned}
V^*&\cong A_1^*,&
R^\perp&\cong(\Ker\mu_2)^\perp\subset A_1^*\otimes_{A_0}A_1^*,\\
{}^*V&\cong{}^*(A_1),&
{}^\perp R&\cong{}^\perp(\Ker\mu_2)\subset{}^*(A_1)\otimes_{A_0}{}^*(A_1).
\end{aligned}
\]
Proposition~\ref{prop:tensor-universal} extends $V^*\cong A_1^*$ and $ {}^*V\cong{}^*(A_1)$ to tensor-algebra isomorphisms, which descend to the quotients by $(R^\perp)$ and $({}^\perp R)$, respectively.
Thus both quadratic duals are independent of the chosen presentation up to $A_0$-preserving isomorphisms of graded algebras.
```

</details>

---

<a id="replacement-9"></a>
## Replacement 9: Compute the right dual of the relation space explicitly

Replace the prose-only reduction by the Artin-Wedderburn decomposition of $R_S$, the corresponding decomposition of ${}_S R^*$, and the dimension equality. No symmetrising form is used.

**Source:** [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:68), lines 68-71. **Changes:** +23 / -4 lines.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -68,4 +77,23 @@
-For the dimension assertion, Theorem~\ref{thm:artin-wedderburn} reduces to simple right modules over matrix rings.\comm{where is $R^*$ actually calculated to get the claim????}
-For a finite-dimensional division algebra $\Delta$, the right $\Mat_n(\Delta)$-module $\Delta^{1\times n}$ given by a row space has dual that can be identified with the column space $\Delta^{n\times1}$: a column $c$ gives the homomorphism $x\mapsto cx$.
-The row and column spaces have the same $\Bbbk$-dimension, and dimensions add over simple summands.\comm{use symbol instead of words to explain}
-Hence $\dim_\Bbbk R^*=\dim_\Bbbk R$ without choosing a symmetrising form.
+For the dimension assertion, write
+\[
+S\cong\prod_{j=1}^n\Mat_{d_j}(\Delta_j),
+\qquad
+R_S\cong\bigoplus_{j=1}^n
+(\Delta_j^{1\times d_j})^{\oplus m_j},
+\]
+where each $\Delta_j$ is a finite-dimensional division $\Bbbk$-algebra and $m_j$ is the multiplicity of the corresponding simple right module.
+For each $j$, there is a left $\Mat_{d_j}(\Delta_j)$-module isomorphism
+\[
+\Delta_j^{d_j\times1}\xrightarrow{\sim}
+\Hom_{\Mat_{d_j}(\Delta_j)}(\Delta_j^{1\times d_j},\Mat_{d_j}(\Delta_j)),
+\qquad c\longmapsto(x\mapsto cx).
+\]
+Indeed, a homomorphism is determined by its value on the first coordinate row, and that value has only its first column non-zero.
+Thus, as left $S$-modules,
+\[
+{}_S R^*\cong\bigoplus_{j=1}^n
+(\Delta_j^{d_j\times1})^{\oplus m_j},
+\qquad
+\dim_\Bbbk R^*=\sum_{j=1}^n m_jd_j\dim_\Bbbk\Delta_j
+=\dim_\Bbbk R.
+\]
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
For the dimension assertion, Theorem~\ref{thm:artin-wedderburn} reduces to simple right modules over matrix rings.\comm{where is $R^*$ actually calculated to get the claim????}
For a finite-dimensional division algebra $\Delta$, the right $\Mat_n(\Delta)$-module $\Delta^{1\times n}$ given by a row space has dual that can be identified with the column space $\Delta^{n\times1}$: a column $c$ gives the homomorphism $x\mapsto cx$.
The row and column spaces have the same $\Bbbk$-dimension, and dimensions add over simple summands.\comm{use symbol instead of words to explain}
Hence $\dim_\Bbbk R^*=\dim_\Bbbk R$ without choosing a symmetrising form.
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
For the dimension assertion, write
\[
S\cong\prod_{j=1}^n\Mat_{d_j}(\Delta_j),
\qquad
R_S\cong\bigoplus_{j=1}^n
(\Delta_j^{1\times d_j})^{\oplus m_j},
\]
where each $\Delta_j$ is a finite-dimensional division $\Bbbk$-algebra and $m_j$ is the multiplicity of the corresponding simple right module.
For each $j$, there is a left $\Mat_{d_j}(\Delta_j)$-module isomorphism
\[
\Delta_j^{d_j\times1}\xrightarrow{\sim}
\Hom_{\Mat_{d_j}(\Delta_j)}(\Delta_j^{1\times d_j},\Mat_{d_j}(\Delta_j)),
\qquad c\longmapsto(x\mapsto cx).
\]
Indeed, a homomorphism is determined by its value on the first coordinate row, and that value has only its first column non-zero.
Thus, as left $S$-modules,
\[
{}_S R^*\cong\bigoplus_{j=1}^n
(\Delta_j^{d_j\times1})^{\oplus m_j},
\qquad
\dim_\Bbbk R^*=\sum_{j=1}^n m_jd_j\dim_\Bbbk\Delta_j
=\dim_\Bbbk R.
\]
```

</details>

---

<a id="replacement-10"></a>
## Replacement 10: Specify the dualities and the action in the bidual calculation

Name the right and left $S$-dualities. In the relation calculation, specify the right $S$-action on $V^*$ and refer to the existing pairing formulas, rather than the equation you commented out. The displayed computation is retained.

### 10a. Lecture_Koszul_S3.tex

**Source:** [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:89), line 89. **Changes:** +2 / -1 lines.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -89,1 +117,2 @@
-Let $U\subset M$ be an $S$-sub-bimodule of a finite-dimensional $S$-bimodule. Under the evaluation isomorphisms \comm{do not use `evaluation isomorphism', use `duality of (specific which one)'  (apply this rule throughout all lectures from now on)} of Lemma~\ref{lem:S-bidual},
+Let $U\subset M$ be an $S$-sub-bimodule of a finite-dimensional bimodule $ {}_SM_S$.
+Under $M\cong{}^*(M^*)$ and $M\cong({}^*M)^*$ from the right and left $S$-dualities in Lemma~\ref{lem:S-bidual},
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
Let $U\subset M$ be an $S$-sub-bimodule of a finite-dimensional $S$-bimodule. Under the evaluation isomorphisms \comm{do not use `evaluation isomorphism', use `duality of (specific which one)'  (apply this rule throughout all lectures from now on)} of Lemma~\ref{lem:S-bidual},
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
Let $U\subset M$ be an $S$-sub-bimodule of a finite-dimensional bimodule $ {}_SM_S$.
Under $M\cong{}^*(M^*)$ and $M\cong({}^*M)^*$ from the right and left $S$-dualities in Lemma~\ref{lem:S-bidual},
```

</details>

### 10b. Lecture_Koszul_S3.tex

**Source:** [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:113), lines 113-126. **Changes:** +7 / -5 lines.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -113,6 +142,8 @@
-\emph{Generators.} The evaluation $\mathrm{ev}_V:V\xrightarrow{\sim}{}^*(V^*)$, $v\mapsto(f\mapsto f(v))$, of Lemma~\ref{lem:S-bidual} identifies the generators of $A$ and ${}^!(A^!)$.
+\emph{Generators.} The right $S$-duality in Lemma~\ref{lem:S-bidual} gives
+$\mathrm{ev}_V:V\xrightarrow{\sim}{}^*(V^*)$, $v\mapsto(f\mapsto f(v))$, identifying the generators of $A$ and $ {}^!(A^!)$.
 It preserves both $S$-actions by \eqref{eq:tensor-dual-actions}.
 
-\emph{Relations.} For $v,w\in V$ and $f,g\in V^*$, the same actions  \comm{what do you mean by action, what acts on what} and \eqref{eq:quadratic-pairings} \comm{this is just \eqref{eq:tensor-duals} with $W=V$} give
+\emph{Relations.} The right $S$-action on $V^*$ is $(gs)(w)=g(sw)$ for all $g\in V^*$, $s\in S$, and $w\in V$.
+Applying \eqref{eq:tensor-evaluations} first to $V^*\otimes_S V^*$ and then to $V\otimes_S V$ gives, for all $v,w\in V$ and $f,g\in V^*$,
 \begin{equation}\label{eq:bidual-tensor-square}
 \begin{aligned}
@@ -122,5 +153,5 @@
 \end{aligned}
 \end{equation}
-Thus $\mathrm{ev}_V\otimes\mathrm{ev}_V$ agrees with evaluation on $V\otimes_S V$ under the tensor-dual identifications \eqref{eq:tensor-duals}.
-Lemma~\ref{lem:double-orthogonal}, applied to $R\subset V\otimes_S V$, identifies the relations ${}^\perp(R^\perp)$ of ${}^!(A^!)$ with $R$.
-The presentations \eqref{eq:quadratic-duals} therefore give an isomorphism ${}^!(A^!)\cong A$ over $S$.
+Thus $\mathrm{ev}_V\otimes\mathrm{ev}_V$ is the bidual identification for $V\otimes_S V$ under anti-distributivity of the $S$-dual \eqref{eq:tensor-duals}.
+Lemma~\ref{lem:double-orthogonal}, applied to $R\subset V\otimes_S V$, identifies the relations $ {}^\perp(R^\perp)$ of $ {}^!(A^!)$ with $R$.
+The presentations \eqref{eq:quadratic-duals} therefore give an $S$-preserving isomorphism of graded algebras $ {}^!(A^!)\cong A$.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\emph{Generators.} The evaluation $\mathrm{ev}_V:V\xrightarrow{\sim}{}^*(V^*)$, $v\mapsto(f\mapsto f(v))$, of Lemma~\ref{lem:S-bidual} identifies the generators of $A$ and ${}^!(A^!)$.
It preserves both $S$-actions by \eqref{eq:tensor-dual-actions}.

\emph{Relations.} For $v,w\in V$ and $f,g\in V^*$, the same actions  \comm{what do you mean by action, what acts on what} and \eqref{eq:quadratic-pairings} \comm{this is just \eqref{eq:tensor-duals} with $W=V$} give
\begin{equation}\label{eq:bidual-tensor-square}
\begin{aligned}
\theta_\ell(\mathrm{ev}_V(v)\otimes\mathrm{ev}_V(w))(g\otimes f)
&=\mathrm{ev}_V(w)(g f(v))=g(f(v)w)\\
&=\mathrm{ev}_{V\otimes_S V}(v\otimes w)(\theta_r(g\otimes f)).
\end{aligned}
\end{equation}
Thus $\mathrm{ev}_V\otimes\mathrm{ev}_V$ agrees with evaluation on $V\otimes_S V$ under the tensor-dual identifications \eqref{eq:tensor-duals}.
Lemma~\ref{lem:double-orthogonal}, applied to $R\subset V\otimes_S V$, identifies the relations ${}^\perp(R^\perp)$ of ${}^!(A^!)$ with $R$.
The presentations \eqref{eq:quadratic-duals} therefore give an isomorphism ${}^!(A^!)\cong A$ over $S$.
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
\emph{Generators.} The right $S$-duality in Lemma~\ref{lem:S-bidual} gives
$\mathrm{ev}_V:V\xrightarrow{\sim}{}^*(V^*)$, $v\mapsto(f\mapsto f(v))$, identifying the generators of $A$ and $ {}^!(A^!)$.
It preserves both $S$-actions by \eqref{eq:tensor-dual-actions}.

\emph{Relations.} The right $S$-action on $V^*$ is $(gs)(w)=g(sw)$ for all $g\in V^*$, $s\in S$, and $w\in V$.
Applying \eqref{eq:tensor-evaluations} first to $V^*\otimes_S V^*$ and then to $V\otimes_S V$ gives, for all $v,w\in V$ and $f,g\in V^*$,
\begin{equation}\label{eq:bidual-tensor-square}
\begin{aligned}
\theta_\ell(\mathrm{ev}_V(v)\otimes\mathrm{ev}_V(w))(g\otimes f)
&=\mathrm{ev}_V(w)(g f(v))=g(f(v)w)\\
&=\mathrm{ev}_{V\otimes_S V}(v\otimes w)(\theta_r(g\otimes f)).
\end{aligned}
\end{equation}
Thus $\mathrm{ev}_V\otimes\mathrm{ev}_V$ is the bidual identification for $V\otimes_S V$ under anti-distributivity of the $S$-dual \eqref{eq:tensor-duals}.
Lemma~\ref{lem:double-orthogonal}, applied to $R\subset V\otimes_S V$, identifies the relations $ {}^\perp(R^\perp)$ of $ {}^!(A^!)$ with $R$.
The presentations \eqref{eq:quadratic-duals} therefore give an $S$-preserving isomorphism of graded algebras $ {}^!(A^!)\cong A$.
```

</details>

---

<a id="replacement-11"></a>
## Replacement 11: Repair references to the removed two-vertex example

Specify the two-dimensional bimodule where it is used, without restoring the example you deleted. References to the commented-out pairing equation are redirected to the existing equation, as listed under mechanical changes.

### 11a. Lecture_Koszul_S2.tex

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:1107), line 1107. **Changes:** +2 / -1 lines.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -1107,1 +1143,2 @@
-For the bimodule $V$ in Example~\ref{ex:two-vertex-relations}, find a basis of each $T_S(V)_d$ and show that
+Let $S=\Bbbk e_1\oplus\Bbbk e_2$ with coordinate idempotents, and let the bimodule $V=\Bbbk a\oplus\Bbbk b$ satisfy $e_1ae_2=a$, $e_2be_1=b$, with all other idempotent actions zero.
+Find a basis of each $T_S(V)_d$ and show that
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
For the bimodule $V$ in Example~\ref{ex:two-vertex-relations}, find a basis of each $T_S(V)_d$ and show that
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
Let $S=\Bbbk e_1\oplus\Bbbk e_2$ with coordinate idempotents, and let the bimodule $V=\Bbbk a\oplus\Bbbk b$ satisfy $e_1ae_2=a$, $e_2be_1=b$, with all other idempotent actions zero.
Find a basis of each $T_S(V)_d$ and show that
```

</details>

### 11b. Lecture_Koszul_S3.tex

**Source:** [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:243), line 243. **Changes:** +2 / -1 lines.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -243,1 +274,2 @@
-Take $A=T_S(V)/(ab)$ from Example~\ref{ex:two-vertex-relations}, where $S=\Bbbk e_1\oplus\Bbbk e_2$, $e_1ae_2=a$, and $e_2be_1=b$.
+Let $S=\Bbbk e_1\oplus\Bbbk e_2$ with coordinate idempotents, and let the bimodule $V=\Bbbk a\oplus\Bbbk b$ satisfy $e_1ae_2=a$, $e_2be_1=b$, with all other idempotent actions zero.
+Take $A=T_S(V)/(ab)$.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
Take $A=T_S(V)/(ab)$ from Example~\ref{ex:two-vertex-relations}, where $S=\Bbbk e_1\oplus\Bbbk e_2$, $e_1ae_2=a$, and $e_2be_1=b$.
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
Let $S=\Bbbk e_1\oplus\Bbbk e_2$ with coordinate idempotents, and let the bimodule $V=\Bbbk a\oplus\Bbbk b$ satisfy $e_1ae_2=a$, $e_2be_1=b$, with all other idempotent actions zero.
Take $A=T_S(V)/(ab)$.
```

</details>

---

<a id="replacement-12"></a>
## Replacement 12: Correct the polynomial Hilbert-series justification

The current footnote differentiates the geometric series the wrong number of times. Count monomials directly instead; the formulas also cover zero-dimensional generating spaces.

**Source:** [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:885), lines 885-892. **Changes:** +5 / -4 lines.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -885,8 +921,9 @@
 \begin{example}\label{ex:hilbert-polynomial-exterior}
-For the symmetric algebra $\SymAlg(V)$ and exterior algebra $\bigwedge W$ in Example~\ref{ex:polynomial-exterior} with $n=\dim_\Bbbk V, m=\dim_\Bbbk W$. 
-Using the description of their basis we get
+Let $n=\dim_\Bbbk V$ and $m=\dim_\Bbbk W$ in Example~\ref{ex:polynomial-exterior}.
+Choosing an exponent independently for each $x_i$, and choosing whether each $y_j$ occurs, gives
 \[
-h_{\SymAlg(V)}(t)=\sum_{d\ge 0}\binom{d+n-1}{n-1}t^d=\frac{1}{(1-t)^n},\footnote{differential $1/(1-t)=\sum_{d\ge 0} t^d$ on both side $n$ times to see this}\qquad
-h_{\bigwedge W}(t)=(1+t)^m.
+h_{\SymAlg(V)}(t)=\left(\sum_{a\geq0}t^a\right)^n=\frac{1}{(1-t)^n},
+\qquad h_{\bigwedge W}(t)=(1+t)^m.
 \]
+For $n\geq1$, the coefficient of $t^d$ in $h_{\SymAlg(V)}(t)$ is $\binom{d+n-1}{n-1}$, the number of $n$-tuples of non-negative integers with sum $d$.
 \end{example}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{example}\label{ex:hilbert-polynomial-exterior}
For the symmetric algebra $\SymAlg(V)$ and exterior algebra $\bigwedge W$ in Example~\ref{ex:polynomial-exterior} with $n=\dim_\Bbbk V, m=\dim_\Bbbk W$. 
Using the description of their basis we get
\[
h_{\SymAlg(V)}(t)=\sum_{d\ge 0}\binom{d+n-1}{n-1}t^d=\frac{1}{(1-t)^n},\footnote{differential $1/(1-t)=\sum_{d\ge 0} t^d$ on both side $n$ times to see this}\qquad
h_{\bigwedge W}(t)=(1+t)^m.
\]
\end{example}
```

</details>

<details>
<summary><strong>Proposed replacement: exact new passage</strong></summary>

```tex
\begin{example}\label{ex:hilbert-polynomial-exterior}
Let $n=\dim_\Bbbk V$ and $m=\dim_\Bbbk W$ in Example~\ref{ex:polynomial-exterior}.
Choosing an exponent independently for each $x_i$, and choosing whether each $y_j$ occurs, gives
\[
h_{\SymAlg(V)}(t)=\left(\sum_{a\geq0}t^a\right)^n=\frac{1}{(1-t)^n},
\qquad h_{\bigwedge W}(t)=(1+t)^m.
\]
For $n\geq1$, the coefficient of $t^d$ in $h_{\SymAlg(V)}(t)$ is $\binom{d+n-1}{n-1}$, the number of $n$-tuples of non-negative integers with sum $d$.
\end{example}
```

</details>

---

<a id="mechanical-changes"></a>
## Mechanical Changes

These are notation or terminology changes only. As requested, the full source lines are not quoted.

| Operation | File | Original line numbers |
|---|---|---|
| Simple-class count: r to n | [Lecture_Koszul_S1.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:213) | 213, 215, 232, 800, 801, 1281, 1282, 1285, 1286, 1294, 1297, 1298, 1376, 1377 |
| Simple-class count: r to n | [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:552) | 552, 555, 563, 565, 571, 573, 735, 741, 747, 754, 755, 760, 768, 772, 787, 848, 852, 853, 858, 860 |
| Simple-class count: r to n | [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:170) | 170, 172, 293, 294 |
| Two algebras: simple-class counts n and m | [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:327) | 327 |
| Simple-class count: r to n | [Lecture_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:352) | 352 |
| Subsection heading after relocation | [Lecture_Koszul_S1.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1166) | 1166 |
| Anti-distributivity terminology | [Lecture_Koszul_S2.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:359) | 359, 1014, 1027, 1029 |
| Anti-distributivity terminology | [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:18) | 18 |
| Anti-distributivity terminology | [Lecture_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:343) | 343 |
| Remove P_j shorthand in Hilbert-series notation | [Lecture_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:350) | 350 |
| S-preserving terminology | [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:108) | 108, 131 |
| Name the specific duality | [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:284) | 284 |
| Repair references to the commented-out pairing equation | [Lecture_Koszul_S3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:201) | 201, 270 |

The simple-class renaming is also incorporated in the substantive replacements at Lecture 2 lines 725, 732, 813-814, 824-825, 834, 838, 900-901, and 908, and Homework 1 lines 278 and 281.

**Limits of the terminology changes:**

- Replace vague references to tensor-dual isomorphisms by **anti-distributivity of the $S$-dual**, retaining the existing equation labels.
- Use “$S$-preserving isomorphism of graded algebras” in place of “graded isomorphism over $S$” and its variants, without defining a new term. The check covers all five lectures, the mother file, and Homework 1: the obsolete definition at Lecture 3 line 48 is removed, and the wording at lines 108, 126, and 131 is replaced. Tensor products and tensor algebras *over* $S$, and isomorphisms *over a module* $M$, retain their usual wording.
- Name the **right/left $S$-dualities** or **$\Bbbk$-linear duality** where the point is recovery from the bidual. Actual evaluation maps, their symbols, and evaluation at an idempotent are not renamed.
- Remove $P_i$ only as shorthand for $e_iA$ in the Hilbert-series discussion and notation table. Resolution notation and unrelated homework notation remain unchanged.
- Unrelated uses of $r$, including grading shifts, finite numbers of summands, matrix-diagram arrows, and $\theta_r$, remain unchanged.
- The Lecture 1 heading “Hom spaces and evaluation” becomes “Hom spaces and duals” after the proposition moves.

## Comment Coverage

| Current comment location | Addressed by |
|---|---|
| Lecture 1: 1218 | Replacement 1 |
| Lecture 2: 341 | Replacement 2 and mechanical terminology updates |
| Lecture 2: 594 | Replacement 3 |
| Lecture 2: 654 | Replacement 4 |
| Lecture 2: 719 | Replacement 5 and the simple-class notation updates |
| Lecture 2: 795, 844 | Replacement 1 |
| Lecture 2: 866 | Replacement 7 |
| Lecture 3: 47, 48 | Replacement 8 and $S$-preserving terminology |
| Lecture 3: 68, 70 | Replacement 9 |
| Lecture 3: 89 | Replacement 10 and specific-duality terminology |
| Lecture 3: 116, both comments | Replacement 10 |

## Checks and Application Status

**Checked on the applied text:**

- All 15 active comments are addressed.
- No unresolved lecture references or duplicate labels remain.
- The evaluation/coevaluation proposition occurs exactly once, before its first application.
- Supplementary and advanced environments are balanced and separate.
- Percent-commented passages and the commented-out pairing equation are unchanged.
- Hilbert-series formulas retain both simple-module indices, with each row counting right-module composition factors.
- The homework implication is proved over general finite-dimensional semisimple $S$, without assuming that one representative primitive idempotent per simple class sums to $1$.
- Lectures 4 and 5 are unchanged.

**Compilation completed:** both files compiled successfully with the built-in compiler and TeX Live. Updated PDFs: `Lecture_Koszul.pdf` (51 pages) and `Homework1.pdf` (6 pages). The existing hidden-content settings were preserved. No side panel or preview was opened.

The lecture build retains two line-overflow warnings in unchanged Lecture 1 paragraphs and one underfull line in the notation table. No compiler errors, unresolved references, or duplicate labels remain; the homework build has no warnings.

