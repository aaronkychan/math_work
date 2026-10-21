# Change Proposal 15: Lecture 4

> **Status: approved and applied on 21 October 2026. Compilation succeeded, and the PDF was saved in the course folder.**

**Prepared and revised:** 21 October 2026, against the current saved sources.

## Scope

Address all **12 active comments** in [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex). The only proposed changes outside Lecture 4 are the new `\grtop` macro and its notation-table entry in [Lecture_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex).

- Keep ordinary modules first, followed by the graded version.
- Retain your section title, subsection organisation, and supplementary placement of the Nakayama proof.
- Remove unnecessary finite-dimensionality assumptions on modules, while stating the algebra hypotheses explicitly.
- When $A$ is finite-dimensional, use $\rad M$ rather than repeatedly writing $M\rad A$.
- Define minimality using kernel maps; mention syzygies only in a remark after uniqueness of minimal resolutions.
- Use **`\grtop` = $\operatorname{top}_{\mathrm{gr}}$**, as confirmed; reserve `\top` for the ordinary top.
- Keep the longer cover-existence argument supplementary and the infinite-dimensional counterexample advanced.
- Leave Lectures 1, 2, 3, and 5, homework, hidden-content settings, and commented-out material unchanged.

## Reading the Proposal

In each diff, **`-` removes a line**, **`+` adds a line**, and an unmarked line is retained context. Added/removed counts accompany each passage. Expand the separately labelled blocks for the complete exact old and new TeX.

Source locations refer to the **current saved files before changes**. New-line coordinates refer to the combined proposed version, including the location-only corrections. As requested, repeated substitutions of `J` by `\rad A` are **listed by line number only**.

## Contents

| Replacement | Change |
|---|---|
| [1](#replacement-1) | State what Nakayama detects |
| [2](#replacement-2) | Condense the finite-dimensional case into a Nakayama remark |
| [3](#replacement-3) | Remove the dimension bound from the cover criterion |
| [4](#replacement-4) | Generalise projective covers and explain finiteness |
| [5](#replacement-5) | Shorten the construction of free resolutions |
| [6](#replacement-6) | Define minimality using kernel maps |
| [7](#replacement-7) | Generalise minimal resolutions |
| [8](#replacement-8) | State graded projectivity as a corollary |
| [9](#replacement-9) | Separate ordinary and graded tops |
| [10](#replacement-10) | Define noetherianity and explain its role |
| [Mechanical changes](#mechanical-changes) | Radical notation, graded-top notation, and one grammatical correction |
| [Checks](#checks) | Comment coverage and verification status |

**Dependencies:** Replacements 2-4 establish the general cover statements needed by Replacement 7. Replacement 6 supplies the precise kernel maps reused in Replacement 9c. Replacement 9a and all graded-top substitutions must be applied together. Replacement 10 uses the existing graded-cover construction, not a new existence hypothesis.

---

<a id="replacement-1"></a>
## Replacement 1: State what Nakayama detects

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:155), line 155. **Changes:** +2 / -1 lines.

Replace the imprecise claim that generators lie in a quotient by the actual generator-lifting statement. The algebra is still arbitrary here, so use $M/M\rad A$ rather than silently identifying it with $M/\rad M$.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -155,1 +153,2 @@
-For a finitely generated module $M$, it turns out that the generators must like in the quotient $M/\rad M$; the core of this lies in the following famous lemma.
+For a finitely generated right $A$-module $M$, a set of elements generates $M$ if its images generate $M/M\rad A$.
+This is the content of Nakayama's lemma.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
For a finitely generated module $M$, it turns out that the generators must like in the quotient $M/\rad M$; the core of this lies in the following famous lemma.
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
For a finitely generated right $A$-module $M$, a set of elements generates $M$ if its images generate $M/M\rad A$.
This is the content of Nakayama's lemma.
```

</details>

---

<a id="replacement-2"></a>
## Replacement 2: Condense the finite-dimensional case into a Nakayama remark

### 2a. Add a compact remark after Nakayama's lemma

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:181), line 181. **Changes:** +7 / -0 lines.

Condense the nilpotence observation and its consequence into one remark immediately after the proof of Nakayama's lemma. There is no separate lemma or proof block.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -181,1 +180,8 @@
 \end{supplementary}
+
+\begin{remark}\label{rem:nakayama-finite-dimensional}
+If $A$ is finite-dimensional, then $\rad A$ is \defn{nilpotent}: $(\rad A)^r=0$ for some integer $r\geq1$.
+Indeed, the powers stabilise at $(\rad A)^r=(\rad A)^{r+1}$, and Lemma~\ref{lem:nakayama} applied to the finite-dimensional module $(\rad A)^r$ gives $(\rad A)^r=0$.
+Thus finite generation is unnecessary in Nakayama's lemma: $M=\rad M$ implies $M=M(\rad A)^r=0$.
+Applying this to $M/N$ also gives $N+\rad M=M\Longrightarrow N=M$ for every submodule $N\subseteq M$.
+\end{remark}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\end{supplementary}
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
\end{supplementary}

\begin{remark}\label{rem:nakayama-finite-dimensional}
If $A$ is finite-dimensional, then $\rad A$ is \defn{nilpotent}: $(\rad A)^r=0$ for some integer $r\geq1$.
Indeed, the powers stabilise at $(\rad A)^r=(\rad A)^{r+1}$, and Lemma~\ref{lem:nakayama} applied to the finite-dimensional module $(\rad A)^r$ gives $(\rad A)^r=0$.
Thus finite generation is unnecessary in Nakayama's lemma: $M=\rad M$ implies $M=M(\rad A)^r=0$.
Applying this to $M/N$ also gives $N+\rad M=M\Longrightarrow N=M$ for every submodule $N\subseteq M$.
\end{remark}
```

</details>

### 2b. Remove the old later nilpotence paragraph

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:213), lines 213-217. **Changes:** +0 / -5 lines.

The observation and its proof are now included in Replacement 2a, so remove the later duplicate.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -213,5 +218,0 @@
-\begin{supplementary}
-The ideal $J$ is \defn{nilpotent} when $A$ is finite-dimensional: $J^r=0$ for some integer $r\geq1$.
-Indeed, the descending sequence $J\supseteq J^2\supseteq\cdots$ stabilises, say at $J^r=J^{r+1}$.
-The finite-dimensional right module $J^r$ is finitely generated, so Lemma~\ref{lem:nakayama} gives $J^r=0$.
-\end{supplementary}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{supplementary}
The ideal $J$ is \defn{nilpotent} when $A$ is finite-dimensional: $J^r=0$ for some integer $r\geq1$.
Indeed, the descending sequence $J\supseteq J^2\supseteq\cdots$ stabilises, say at $J^r=J^{r+1}$.
The finite-dimensional right module $J^r$ is finitely generated, so Lemma~\ref{lem:nakayama} gives $J^r=0$.
\end{supplementary}
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

Delete the passage without replacement.

```tex
```

</details>

---

<a id="replacement-3"></a>
## Replacement 3: Remove the dimension bound from the cover criterion

### 3a. Remove the unnecessary dimension bound on the cover

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:233), line 233. **Changes:** +1 / -1 lines.

The finite-dimensionality assumption on $A$ previously ended with the preceding subsection. State it here explicitly; impose no dimension or finite-generation assumption on $P$ or $M$.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -233,1 +234,1 @@
-Suppose that $P$ is finite-dimensional\comm{where require finite-dimensional?} and projective, and $p:P\to M$ is surjective.
+Let $A$ be finite-dimensional, let $P$ be a projective right $A$-module, and let $p:P\to M$ be surjective.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
Suppose that $P$ is finite-dimensional\comm{where require finite-dimensional?} and projective, and $p:P\to M$ is surjective.
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
Let $A$ be finite-dimensional, let $P$ be a projective right $A$-module, and let $p:P\to M$ be surjective.
```

</details>

### 3b. Use nilpotence instead of finite-generation Nakayama

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:251), line 251. **Changes:** +2 / -1 lines.

Use the finite-dimensional version of Nakayama from Replacement 2a on the quotient, without a finite-generation assumption on $P$. Write module radicals throughout the criterion; the remaining substitutions are listed by location below.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -251,1 +252,2 @@
-Condition (2) gives $U+PJ=P$, and Nakayama's lemma gives $U=P$.
+Condition (2) gives $U+\rad P=P$, hence $\rad(P/U)=P/U$.
+Remark~\ref{rem:nakayama-finite-dimensional} gives $P/U=0$, so $U=P$.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
Condition (2) gives $U+PJ=P$, and Nakayama's lemma gives $U=P$.
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
Condition (2) gives $U+\rad P=P$, hence $\rad(P/U)=P/U$.
Remark~\ref{rem:nakayama-finite-dimensional} gives $P/U=0$, so $U=P$.
```

</details>

---

<a id="replacement-4"></a>
## Replacement 4: Generalise projective covers and explain finiteness

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:258), lines 258-289. **Changes:** +30 / -4 lines.

Keep your finite-dimensional existence argument, and append its extension to arbitrary modules inside the same supplementary block. Uniqueness stays in the main proof and is stated for any algebra. The new remark identifies precisely where the finite-dimensional argument uses the hypotheses.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -258,8 +260,8 @@
 \begin{theorem}\label{thm:ordinary-projective-covers}
-Every finite-dimensional right module over a finite-dimensional algebra has a finite-dimensional projective cover.
-For any two projective covers $p:P\to M$ and $q:Q\to M$, there is an isomorphism $f:P\to Q$ with $qf=p$.
+Let $A$ be a finite-dimensional algebra.
+Every right $A$-module $M$ has a projective cover; if $M$ is finite-dimensional, then so is its cover.
+Over any algebra, for any two projective covers $p:P\to M$ and $q:Q\to M$, there is an isomorphism $f:P\to Q$ with $qf=p$.
 \end{theorem}
-\comm{clarify in remark or something where f.d. of $A$ and of $M$ is used.}
 \begin{proof}
 \underline{Uniqueness:}
 Projectivity of $P$ gives $f:P\to Q$ with $qf=p$.
@@ -269,7 +271,7 @@
 Thus $f$ and $s$ are inverse isomorphisms.
 
 \begin{supplementary}
-\underline{Existence:}
+\underline{Existence for finite-dimensional $M$:}
 Choose a surjection $p:P\to M$ from a finite-dimensional projective module with $\dim_\Bbbk P$ as small as possible.
 Such a surjection exists because $M$ is a quotient of some $A^{\oplus m}$.
 Suppose $U\subsetneq P$ and $p(U)=M$.
@@ -285,5 +287,31 @@
 Thus $\Im u^r$ is projective, and $pu^r=p$ shows that $p(\Im u^r)=M$.
 But $\Im u^r\subseteq U\subsetneq P$ contradicts the minimal choice of $\dim_\Bbbk P$.
 Therefore $p$ is a projective cover.
+
+\underline{Existence for arbitrary $M$:}
+By Theorem~\ref{thm:artin-wedderburn}, choose a decomposition
+$\top M\cong\bigoplus_{\lambda\in I}L_\lambda$ into simple right $A/\rad A$-modules, indexed by a set $I$.
+Each $L_\lambda$ is finite-dimensional, so the preceding argument gives a finite-dimensional projective cover $q_\lambda:Q_\lambda\to L_\lambda$.
+Projectivity lifts each composite $Q_\lambda\to L_\lambda\hookrightarrow\top M$ through the quotient $M\to\top M$ to a map $f_\lambda:Q_\lambda\to M$.
+Set
+\[
+P:=\bigoplus_{\lambda\in I}Q_\lambda,\qquad
+p:P\longrightarrow M,\qquad
+(x_\lambda)_{\lambda\in I}\longmapsto\sum_{\lambda\in I}f_\lambda(x_\lambda).
+\]
+The sum defining $p$ is finite for each element of $P$.
+Corollary~\ref{cor:projective-sums} makes $P$ projective.
+The equality $\rad P=\bigoplus_{\lambda\in I}\rad Q_\lambda$ gives $\top P\cong\bigoplus_{\lambda\in I}\top Q_\lambda$.
+Thus the isomorphisms $\top q_\lambda$ identify $\top p$ with
+$\bigoplus_{\lambda\in I}L_\lambda\xrightarrow{\sim}\top M$.
+Thus $M=p(P)+\rad M$, and Remark~\ref{rem:nakayama-finite-dimensional} applied to $M/p(P)$ shows that $p$ is surjective.
+Proposition~\ref{prop:cover-top} now makes $p$ a projective cover.
 \end{supplementary}
 \end{proof}
+
+\begin{remark}
+For finite-dimensional $M$, finite generation gives a surjection $A^{\oplus m}\to M$, and finite-dimensionality of $A$ makes its domain finite-dimensional.
+Finite-dimensionality of $P$ ensures that the kernels and images of powers of $u$ stabilise.
+For arbitrary $M$, the argument instead uses semisimplicity of $A/\rad A$ and nilpotence of $\rad A$.
+Uniqueness of projective covers requires no finiteness assumption.
+\end{remark}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{theorem}\label{thm:ordinary-projective-covers}
Every finite-dimensional right module over a finite-dimensional algebra has a finite-dimensional projective cover.
For any two projective covers $p:P\to M$ and $q:Q\to M$, there is an isomorphism $f:P\to Q$ with $qf=p$.
\end{theorem}
\comm{clarify in remark or something where f.d. of $A$ and of $M$ is used.}
\begin{proof}
\underline{Uniqueness:}
Projectivity of $P$ gives $f:P\to Q$ with $qf=p$.
Since $q(f(P))=M$ and $q$ is a cover, $f(P)=Q$.
Projectivity of $Q$ now gives a section $s:Q\to P$ of $f$.
The equality $p(s(Q))=q(Q)=M$ and the cover property of $p$ give $s(Q)=P$.
Thus $f$ and $s$ are inverse isomorphisms.

\begin{supplementary}
\underline{Existence:}
Choose a surjection $p:P\to M$ from a finite-dimensional projective module with $\dim_\Bbbk P$ as small as possible.
Such a surjection exists because $M$ is a quotient of some $A^{\oplus m}$.
Suppose $U\subsetneq P$ and $p(U)=M$.
Projectivity gives $h:P\to U$ with $(p|_U)h=p$.
Composing $h$ with the inclusion $U\hookrightarrow P$ gives $u:P\to P$ with $pu=p$ and $u(P)\subseteq U$.

Choose an integer $r\geq1$ such that the kernels and images of the powers of $u$ have stabilised.
Then
\[
P=\Ker u^r\oplus\Im u^r.
\]
Indeed, if $u^r(x)\in\Ker u^r$, then $x\in\Ker u^{2r}=\Ker u^r$, so $u^r(x)=0$; equality follows by the dimension formula.
Thus $\Im u^r$ is projective, and $pu^r=p$ shows that $p(\Im u^r)=M$.
But $\Im u^r\subseteq U\subsetneq P$ contradicts the minimal choice of $\dim_\Bbbk P$.
Therefore $p$ is a projective cover.
\end{supplementary}
\end{proof}
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
\begin{theorem}\label{thm:ordinary-projective-covers}
Let $A$ be a finite-dimensional algebra.
Every right $A$-module $M$ has a projective cover; if $M$ is finite-dimensional, then so is its cover.
Over any algebra, for any two projective covers $p:P\to M$ and $q:Q\to M$, there is an isomorphism $f:P\to Q$ with $qf=p$.
\end{theorem}
\begin{proof}
\underline{Uniqueness:}
Projectivity of $P$ gives $f:P\to Q$ with $qf=p$.
Since $q(f(P))=M$ and $q$ is a cover, $f(P)=Q$.
Projectivity of $Q$ now gives a section $s:Q\to P$ of $f$.
The equality $p(s(Q))=q(Q)=M$ and the cover property of $p$ give $s(Q)=P$.
Thus $f$ and $s$ are inverse isomorphisms.

\begin{supplementary}
\underline{Existence for finite-dimensional $M$:}
Choose a surjection $p:P\to M$ from a finite-dimensional projective module with $\dim_\Bbbk P$ as small as possible.
Such a surjection exists because $M$ is a quotient of some $A^{\oplus m}$.
Suppose $U\subsetneq P$ and $p(U)=M$.
Projectivity gives $h:P\to U$ with $(p|_U)h=p$.
Composing $h$ with the inclusion $U\hookrightarrow P$ gives $u:P\to P$ with $pu=p$ and $u(P)\subseteq U$.

Choose an integer $r\geq1$ such that the kernels and images of the powers of $u$ have stabilised.
Then
\[
P=\Ker u^r\oplus\Im u^r.
\]
Indeed, if $u^r(x)\in\Ker u^r$, then $x\in\Ker u^{2r}=\Ker u^r$, so $u^r(x)=0$; equality follows by the dimension formula.
Thus $\Im u^r$ is projective, and $pu^r=p$ shows that $p(\Im u^r)=M$.
But $\Im u^r\subseteq U\subsetneq P$ contradicts the minimal choice of $\dim_\Bbbk P$.
Therefore $p$ is a projective cover.

\underline{Existence for arbitrary $M$:}
By Theorem~\ref{thm:artin-wedderburn}, choose a decomposition
$\top M\cong\bigoplus_{\lambda\in I}L_\lambda$ into simple right $A/\rad A$-modules, indexed by a set $I$.
Each $L_\lambda$ is finite-dimensional, so the preceding argument gives a finite-dimensional projective cover $q_\lambda:Q_\lambda\to L_\lambda$.
Projectivity lifts each composite $Q_\lambda\to L_\lambda\hookrightarrow\top M$ through the quotient $M\to\top M$ to a map $f_\lambda:Q_\lambda\to M$.
Set
\[
P:=\bigoplus_{\lambda\in I}Q_\lambda,\qquad
p:P\longrightarrow M,\qquad
(x_\lambda)_{\lambda\in I}\longmapsto\sum_{\lambda\in I}f_\lambda(x_\lambda).
\]
The sum defining $p$ is finite for each element of $P$.
Corollary~\ref{cor:projective-sums} makes $P$ projective.
The equality $\rad P=\bigoplus_{\lambda\in I}\rad Q_\lambda$ gives $\top P\cong\bigoplus_{\lambda\in I}\top Q_\lambda$.
Thus the isomorphisms $\top q_\lambda$ identify $\top p$ with
$\bigoplus_{\lambda\in I}L_\lambda\xrightarrow{\sim}\top M$.
Thus $M=p(P)+\rad M$, and Remark~\ref{rem:nakayama-finite-dimensional} applied to $M/p(P)$ shows that $p$ is surjective.
Proposition~\ref{prop:cover-top} now makes $p$ a projective cover.
\end{supplementary}
\end{proof}

\begin{remark}
For finite-dimensional $M$, finite generation gives a surjection $A^{\oplus m}\to M$, and finite-dimensionality of $A$ makes its domain finite-dimensional.
Finite-dimensionality of $P$ ensures that the kernels and images of powers of $u$ stabilise.
For arbitrary $M$, the argument instead uses semisimplicity of $A/\rad A$ and nilpotence of $\rad A$.
Uniqueness of projective covers requires no finiteness assumption.
\end{remark}
```

</details>

---

<a id="replacement-5"></a>
## Replacement 5: Shorten the construction of free resolutions

### 5a. Describe resolutions as sequences of maps

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:298), lines 298-299. **Changes:** +3 / -2 lines.

A small adjacent correction: exactness describes the sequence of maps, not individual projective modules.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -298,2 +326,3 @@
-If we consider the kernel of a projective cover, or more generally surjective map from a projective, then (say, when $A$ is finite-dimensional) we can take again projective cover, and repeat this construction; this yields a sequence of (exact) projective modules.
-A resolution is such a sequence; let us set this up more properly for general $\Bbbk$-algebra $A$.
+Starting with a surjection from a projective module onto $M$, one can repeat the construction for each successive kernel.
+Composing each surjection with the inclusion of its target kernel gives an exact sequence.
+We now define such resolutions over an arbitrary $\Bbbk$-algebra $A$.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
If we consider the kernel of a projective cover, or more generally surjective map from a projective, then (say, when $A$ is finite-dimensional) we can take again projective cover, and repeat this construction; this yields a sequence of (exact) projective modules.
A resolution is such a sequence; let us set this up more properly for general $\Bbbk$-algebra $A$.
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
Starting with a surjection from a projective module onto $M$, one can repeat the construction for each successive kernel.
Composing each surjection with the inclusion of its target kernel gives an exact sequence.
We now define such resolutions over an arbitrary $\Bbbk$-algebra $A$.
```

</details>

### 5b. Shorten the free-resolution existence proof

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:339), lines 339-350. **Changes:** +5 / -8 lines.

Use your suggested free module indexed by the underlying set, then iterate over kernels. Each displayed sum is finite because its input lies in a direct sum.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -339,12 +368,9 @@
 \begin{proof}
-\comm{proof can be much shorter?  every $M$ has a surjection from $A^{
-\oplus M}$, where $\oplus M$ means direct sum with one copy of $A$ for each element of $M$.  Then iterate this for kernel of the surjection.}
-Choose a free surjection $p_0:P_0\to M$, set $K_1=\Ker p_0$, and choose a free surjection $p_1:P_1\to K_1$.
-Continue with $K_{i+1}=\Ker p_i$ and free surjections $p_{i+1}:P_{i+1}\to K_{i+1}$ for $i\geq1$.
-For the inclusions $\iota_i:K_i\hookrightarrow P_{i-1}$, set
+For every right $A$-module $N$, the free module $A^{\oplus N}:=\bigoplus_{n\in N}A$, indexed by the underlying set of $N$, surjects onto $N$ by
 \[
-d_i:=\iota_i p_i:P_i\longrightarrow P_{i-1}\quad\text{for all }i\geq1.
+A^{\oplus N}\longrightarrow N,\qquad
+(a_n)_{n\in N}\longmapsto\sum_{n\in N}na_n.
 \]
-Then $\Im d_1=K_1=\Ker p_0$ and
-$\Im d_{i+1}=K_{i+1}=\Ker p_i=\Ker d_i$ for every $i\geq1$.
+Start with $N=M$ and repeat for each successive kernel.
+Compose each new surjection with the inclusion of that kernel into the preceding free module; its image is exactly that kernel, so the resulting sequence is exact.
 \end{proof}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{proof}
\comm{proof can be much shorter?  every $M$ has a surjection from $A^{
\oplus M}$, where $\oplus M$ means direct sum with one copy of $A$ for each element of $M$.  Then iterate this for kernel of the surjection.}
Choose a free surjection $p_0:P_0\to M$, set $K_1=\Ker p_0$, and choose a free surjection $p_1:P_1\to K_1$.
Continue with $K_{i+1}=\Ker p_i$ and free surjections $p_{i+1}:P_{i+1}\to K_{i+1}$ for $i\geq1$.
For the inclusions $\iota_i:K_i\hookrightarrow P_{i-1}$, set
\[
d_i:=\iota_i p_i:P_i\longrightarrow P_{i-1}\quad\text{for all }i\geq1.
\]
Then $\Im d_1=K_1=\Ker p_0$ and
$\Im d_{i+1}=K_{i+1}=\Ker p_i=\Ker d_i$ for every $i\geq1$.
\end{proof}
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
\begin{proof}
For every right $A$-module $N$, the free module $A^{\oplus N}:=\bigoplus_{n\in N}A$, indexed by the underlying set of $N$, surjects onto $N$ by
\[
A^{\oplus N}\longrightarrow N,\qquad
(a_n)_{n\in N}\longmapsto\sum_{n\in N}na_n.
\]
Start with $N=M$ and repeat for each successive kernel.
Compose each new surjection with the inclusion of that kernel into the preceding free module; its image is exactly that kernel, so the resulting sequence is exact.
\end{proof}
```

</details>

---

<a id="replacement-6"></a>
## Replacement 6: Define minimality using kernel maps

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:352), lines 352-355. **Changes:** +20 / -2 lines.

Define minimality directly using the kernel maps, without calling the kernels syzygies. The diagram uses $K_i$ only as notation for the displayed kernels. A short remark after the uniqueness theorem in Replacement 7c introduces syzygies for minimal resolutions.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -352,4 +378,22 @@
 \begin{definition}\label{def:ordinary-minimal-resolution}
-A projective resolution \eqref{eq:projective-resolution} is \defn{minimal} if $p_0:P_0\to M$, $d_1:P_1\to\Ker p_0$, and $d_i:P_i\to\Ker d_{i-1}$ for every $i\geq2$ are projective covers, with the codomains restricted as indicated\comm{do not use vague language... as indicated -- what? where? use precise language}.
-\comm{draw a picture of the resolution, syzygies factoring through each differential, then label the arrow going into the syzygies are `proj. cover'}
+A projective resolution \eqref{eq:projective-resolution} is \defn{minimal} if $p_0:P_0\to M$ and the surjections
+\[
+\begin{aligned}
+p_1:P_1&\longrightarrow\Ker p_0,& x&\longmapsto d_1(x),\\
+p_i:P_i&\longrightarrow\Ker d_{i-1},& x&\longmapsto d_i(x)
+\quad\text{for all }i\geq2
+\end{aligned}
+\]
+are projective covers.
 \end{definition}
+
+For the diagram, put $K_1:=\Ker p_0$ and $K_i:=\Ker d_{i-1}$ for all $i\geq2$.
+In a minimal resolution, each differential factors as a projective cover onto its image followed by inclusion:
+\[
+\xymatrix@C=60pt@R=42pt{
+\cdots\ar[r] & P_2\ar[r]^{d_2}\ar[dr]^{\substack{p_2\\\text{proj.\ cover}}}
+& P_1\ar[r]^{d_1}\ar[dr]^{\substack{p_1\\\text{proj.\ cover}}}
+& P_0\ar[r]^{p_0}_{\text{proj.\ cover}} & M\ar[r] & 0\\
+& & K_2\ar@{^{(}->}[u] & K_1\ar@{^{(}->}[u]
+}
+\]
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{definition}\label{def:ordinary-minimal-resolution}
A projective resolution \eqref{eq:projective-resolution} is \defn{minimal} if $p_0:P_0\to M$, $d_1:P_1\to\Ker p_0$, and $d_i:P_i\to\Ker d_{i-1}$ for every $i\geq2$ are projective covers, with the codomains restricted as indicated\comm{do not use vague language... as indicated -- what? where? use precise language}.
\comm{draw a picture of the resolution, syzygies factoring through each differential, then label the arrow going into the syzygies are `proj. cover'}
\end{definition}
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
\begin{definition}\label{def:ordinary-minimal-resolution}
A projective resolution \eqref{eq:projective-resolution} is \defn{minimal} if $p_0:P_0\to M$ and the surjections
\[
\begin{aligned}
p_1:P_1&\longrightarrow\Ker p_0,& x&\longmapsto d_1(x),\\
p_i:P_i&\longrightarrow\Ker d_{i-1},& x&\longmapsto d_i(x)
\quad\text{for all }i\geq2
\end{aligned}
\]
are projective covers.
\end{definition}

For the diagram, put $K_1:=\Ker p_0$ and $K_i:=\Ker d_{i-1}$ for all $i\geq2$.
In a minimal resolution, each differential factors as a projective cover onto its image followed by inclusion:
\[
\xymatrix@C=60pt@R=42pt{
\cdots\ar[r] & P_2\ar[r]^{d_2}\ar[dr]^{\substack{p_2\\\text{proj.\ cover}}}
& P_1\ar[r]^{d_1}\ar[dr]^{\substack{p_1\\\text{proj.\ cover}}}
& P_0\ar[r]^{p_0}_{\text{proj.\ cover}} & M\ar[r] & 0\\
& & K_2\ar@{^{(}->}[u] & K_1\ar@{^{(}->}[u]
}
\]
```

</details>

---

<a id="replacement-7"></a>
## Replacement 7: Generalise minimal resolutions

### 7a. Relax the ordinary minimality criterion

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:357), line 357. **Changes:** +1 / -1 lines.

No finite-dimensionality assumption on $M$ or the resolution terms remains after Replacement 3.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -357,1 +401,1 @@
-When $A$, $M$, and all $P_i$ are finite-dimensional, Proposition~\ref{prop:cover-top} gives the criterion
+When $A$ is finite-dimensional, Proposition~\ref{prop:cover-top} gives the criterion
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
When $A$, $M$, and all $P_i$ are finite-dimensional, Proposition~\ref{prop:cover-top} gives the criterion
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
When $A$ is finite-dimensional, Proposition~\ref{prop:cover-top} gives the criterion
```

</details>

### 7b. Generalise existence and uniqueness of minimal resolutions

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:363), lines 363-371. **Changes:** +3 / -3 lines.

Existence extends to arbitrary modules over finite-dimensional $A$. Uniqueness does not require $A$ or $M$ to be finite-dimensional, provided minimal resolutions exist.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -363,7 +407,7 @@
 \begin{theorem}\label{thm:ordinary-minimal-resolutions}
-\comm{relax some of the f.d.-ness as much as possible; proof can be use f.d., then remark where things get complicated for general setting}
-Every finite-dimensional right module over a finite-dimensional algebra has a minimal projective resolution with finite-dimensional terms.
-Any two minimal resolutions $P_\bullet\to M$ and $P'_\bullet\to M$ are \defn{isomorphic}: there are isomorphisms $f_i:P_i\to P'_i$ satisfying
+Every right module over a finite-dimensional algebra has a minimal projective resolution.
+If the module is finite-dimensional, every term of its minimal resolution is finite-dimensional.
+Over any algebra, any two minimal resolutions $P_\bullet\to M$ and $P'_\bullet\to M$ are \defn{isomorphic}: there are isomorphisms $f_i:P_i\to P'_i$ satisfying
 \[
 p'_0f_0=p_0,\qquad
 d'_i f_i=f_{i-1}d_i\quad\text{for all }i\geq1.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{theorem}\label{thm:ordinary-minimal-resolutions}
\comm{relax some of the f.d.-ness as much as possible; proof can be use f.d., then remark where things get complicated for general setting}
Every finite-dimensional right module over a finite-dimensional algebra has a minimal projective resolution with finite-dimensional terms.
Any two minimal resolutions $P_\bullet\to M$ and $P'_\bullet\to M$ are \defn{isomorphic}: there are isomorphisms $f_i:P_i\to P'_i$ satisfying
\[
p'_0f_0=p_0,\qquad
d'_i f_i=f_{i-1}d_i\quad\text{for all }i\geq1.
\]
\end{theorem}
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
\begin{theorem}\label{thm:ordinary-minimal-resolutions}
Every right module over a finite-dimensional algebra has a minimal projective resolution.
If the module is finite-dimensional, every term of its minimal resolution is finite-dimensional.
Over any algebra, any two minimal resolutions $P_\bullet\to M$ and $P'_\bullet\to M$ are \defn{isomorphic}: there are isomorphisms $f_i:P_i\to P'_i$ satisfying
\[
p'_0f_0=p_0,\qquad
d'_i f_i=f_{i-1}d_i\quad\text{for all }i\geq1.
\]
\end{theorem}
```

</details>

### 7c. Explain the scope of the generalisation

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:383), lines 383-389. **Changes:** +15 / -4 lines.

Keep the existing map-of-resolutions paragraph and diagram unchanged. Mention syzygies only after minimality and the uniqueness theorem: use kernels from a minimal resolution and explicitly state independence up to isomorphism. Distinguish the existence of free resolutions over any algebra from the stronger existence of projective covers.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -383,7 +427,18 @@
 \begin{proof}
 Use projective covers in place of free surjections in Proposition~\ref{prop:resolutions-exist}.
-Each successive kernel is finite-dimensional, so Theorem~\ref{thm:ordinary-projective-covers} applies at every step.
-For uniqueness, choose an isomorphism $f_0$ between the covers of $M$.
-It restricts to an isomorphism of their kernels; uniqueness of the projective covers of these kernels gives $f_1$.
-Repeating gives $f_i$ with $d'_i f_i=f_{i-1}d_i$ at every step.
+For finite-dimensional $A$, Theorem~\ref{thm:ordinary-projective-covers} applies to every successive kernel.
+If $M$ is finite-dimensional, choose a finite-dimensional cover at each step; its kernel is again finite-dimensional.
+For uniqueness, choose an isomorphism $f_0:P_0\to P'_0$ between the covers of $M$.
+It restricts to an isomorphism $\Ker p_0\to\Ker p'_0$; uniqueness of covers of these kernels gives $f_1:P_1\to P'_1$.
+Repeating gives $f_i$ with $d'_i f_i=f_{i-1}d_i$ at every step, without finiteness assumptions.
 \end{proof}
+
+\begin{remark}
+For a minimal projective resolution of $M$, the kernels $\Ker p_0$ and $\Ker d_i$ for $i\geq1$ are called the successive \defn{syzygies} of $M$.
+Their isomorphism classes are independent of the chosen minimal resolution by Theorem~\ref{thm:ordinary-minimal-resolutions}.
+\end{remark}
+
+\begin{remark}
+Over an arbitrary algebra, Proposition~\ref{prop:resolutions-exist} still gives a free resolution, but projective covers of the successive kernels need not exist.
+The obstruction is to existence, not to uniqueness of a minimal resolution.
+\end{remark}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{proof}
Use projective covers in place of free surjections in Proposition~\ref{prop:resolutions-exist}.
Each successive kernel is finite-dimensional, so Theorem~\ref{thm:ordinary-projective-covers} applies at every step.
For uniqueness, choose an isomorphism $f_0$ between the covers of $M$.
It restricts to an isomorphism of their kernels; uniqueness of the projective covers of these kernels gives $f_1$.
Repeating gives $f_i$ with $d'_i f_i=f_{i-1}d_i$ at every step.
\end{proof}
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
\begin{proof}
Use projective covers in place of free surjections in Proposition~\ref{prop:resolutions-exist}.
For finite-dimensional $A$, Theorem~\ref{thm:ordinary-projective-covers} applies to every successive kernel.
If $M$ is finite-dimensional, choose a finite-dimensional cover at each step; its kernel is again finite-dimensional.
For uniqueness, choose an isomorphism $f_0:P_0\to P'_0$ between the covers of $M$.
It restricts to an isomorphism $\Ker p_0\to\Ker p'_0$; uniqueness of covers of these kernels gives $f_1:P_1\to P'_1$.
Repeating gives $f_i$ with $d'_i f_i=f_{i-1}d_i$ at every step, without finiteness assumptions.
\end{proof}

\begin{remark}
For a minimal projective resolution of $M$, the kernels $\Ker p_0$ and $\Ker d_i$ for $i\geq1$ are called the successive \defn{syzygies} of $M$.
Their isomorphism classes are independent of the chosen minimal resolution by Theorem~\ref{thm:ordinary-minimal-resolutions}.
\end{remark}

\begin{remark}
Over an arbitrary algebra, Proposition~\ref{prop:resolutions-exist} still gives a free resolution, but projective covers of the successive kernels need not exist.
The obstruction is to existence, not to uniqueness of a minimal resolution.
\end{remark}
```

</details>

---

<a id="replacement-8"></a>
## Replacement 8: State graded projectivity as a corollary

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:430), lines 430-441. **Changes:** +21 / -12 lines.

Give the four equivalent conditions a numbered corollary, retain the direct-sum and induced-projective consequences, and cite the ordinary module proofs rather than repeating them.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -430,12 +485,21 @@
-The proof of Proposition~\ref{prop:projective-characterisations} therefore gives
-\comm{write as corollary}
-\[
-\begin{aligned}
-P\text{ graded projective}
-&\Longleftrightarrow \Hom_A^\Z(P,-)\text{ is exact}\\
-&\Longleftrightarrow \text{every graded surjection onto }P\text{ splits}\\
-&\Longleftrightarrow P\text{ is a graded direct summand of a graded free module}.
-\end{aligned}
-\]
-Direct sums and graded direct summands of graded projectives are graded projective by the proof of Corollary~\ref{cor:projective-sums}.
-In particular, if $Q$ is a finite-dimensional right $S$-module, then $Q\otimes_S A(-d)$ is graded projective: Corollary~\ref{cor:semisimple-summands} expresses $Q$ as a summand of a finite direct sum of copies of $S$.
+\begin{corollary}\label{cor:graded-projective-characterisations}
+For a graded right $A$-module $P$, the following are equivalent.
+\begin{enumerate}
+\item $P$ is graded projective.
+\item The functor $\Hom_A^\Z(P,-)$ is exact on graded modules.
+\item Every degree-preserving surjection onto $P$ has a degree-preserving section.
+\item $P$ is a graded direct summand of a graded free module.
+\end{enumerate}
+Arbitrary direct sums and graded direct summands of graded projective modules are graded projective.
+In particular, $Q\otimes_S A(-d)$ is graded projective for every finite-dimensional right $S$-module $Q$ and every $d\in\Z$.
+\end{corollary}
+
+\begin{proof}
+We follow $(1)\Leftrightarrow(2)$ and $(1)\Rightarrow(3)\Rightarrow(4)\Rightarrow(1)$ from Proposition~\ref{prop:projective-characterisations}, using degree-preserving maps.
+\underline{$(1)\Leftrightarrow(2)$.} The proof of Lemma~\ref{lem:Hom-left-exact} applies to graded Hom; surjectivity on Hom is the graded lifting property.
+\underline{$(1)\Rightarrow(3)$.} Lift $\id_P$.
+\underline{$(3)\Rightarrow(4)$.} Split a graded free surjection onto $P$.
+\underline{$(4)\Rightarrow(1)$.} Restrict lifts from the graded free module to its summand $P$.
+The proof of Corollary~\ref{cor:projective-sums} also applies with degree-preserving maps.
+For the last assertion, Corollary~\ref{cor:semisimple-summands} makes $Q$ a direct summand of $S^{\oplus m}$ for some $m$, so $Q\otimes_S A(-d)$ is a graded direct summand of $A(-d)^{\oplus m}$.
+\end{proof}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
The proof of Proposition~\ref{prop:projective-characterisations} therefore gives
\comm{write as corollary}
\[
\begin{aligned}
P\text{ graded projective}
&\Longleftrightarrow \Hom_A^\Z(P,-)\text{ is exact}\\
&\Longleftrightarrow \text{every graded surjection onto }P\text{ splits}\\
&\Longleftrightarrow P\text{ is a graded direct summand of a graded free module}.
\end{aligned}
\]
Direct sums and graded direct summands of graded projectives are graded projective by the proof of Corollary~\ref{cor:projective-sums}.
In particular, if $Q$ is a finite-dimensional right $S$-module, then $Q\otimes_S A(-d)$ is graded projective: Corollary~\ref{cor:semisimple-summands} expresses $Q$ as a summand of a finite direct sum of copies of $S$.
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
\begin{corollary}\label{cor:graded-projective-characterisations}
For a graded right $A$-module $P$, the following are equivalent.
\begin{enumerate}
\item $P$ is graded projective.
\item The functor $\Hom_A^\Z(P,-)$ is exact on graded modules.
\item Every degree-preserving surjection onto $P$ has a degree-preserving section.
\item $P$ is a graded direct summand of a graded free module.
\end{enumerate}
Arbitrary direct sums and graded direct summands of graded projective modules are graded projective.
In particular, $Q\otimes_S A(-d)$ is graded projective for every finite-dimensional right $S$-module $Q$ and every $d\in\Z$.
\end{corollary}

\begin{proof}
We follow $(1)\Leftrightarrow(2)$ and $(1)\Rightarrow(3)\Rightarrow(4)\Rightarrow(1)$ from Proposition~\ref{prop:projective-characterisations}, using degree-preserving maps.
\underline{$(1)\Leftrightarrow(2)$.} The proof of Lemma~\ref{lem:Hom-left-exact} applies to graded Hom; surjectivity on Hom is the graded lifting property.
\underline{$(1)\Rightarrow(3)$.} Lift $\id_P$.
\underline{$(3)\Rightarrow(4)$.} Split a graded free surjection onto $P$.
\underline{$(4)\Rightarrow(1)$.} Restrict lifts from the graded free module to its summand $P$.
The proof of Corollary~\ref{cor:projective-sums} also applies with degree-preserving maps.
For the last assertion, Corollary~\ref{cor:semisimple-summands} makes $Q$ a direct summand of $S^{\oplus m}$ for some $m$, so $Q\otimes_S A(-d)$ is a graded direct summand of $A(-d)^{\oplus m}$.
\end{proof}
```

</details>

---

<a id="replacement-9"></a>
## Replacement 9: Separate ordinary and graded tops

### 9a. Add the confirmed graded-top macro

**Source:** [Lecture_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:177), line 177. **Changes:** +1 / -0 lines.

Use your confirmed subscript convention: $\operatorname{top}_{\mathrm{gr}}$, not a superscript $\mathbb Z$. The ordinary macro stays unchanged.

```diff
--- a/Lecture_Koszul.tex
+++ b/Lecture_Koszul.tex
@@ -177,1 +177,2 @@
 \renewcommand{\top}{\operatorname{top}\nolimits}
+\newcommand{\grtop}{\operatorname{top}\nolimits_{\mathrm{gr}}}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\renewcommand{\top}{\operatorname{top}\nolimits}
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
\renewcommand{\top}{\operatorname{top}\nolimits}
\newcommand{\grtop}{\operatorname{top}\nolimits_{\mathrm{gr}}}
```

</details>

### 9b. Separate the two tops and prove when they agree

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:443), lines 443-459. **Changes:** +36 / -9 lines.

Define the graded top separately, turn the finite-dimensional radical equality into a lemma with supplementary proof, and put the infinite-dimensional counterexample in an advanced block. The example also demonstrates the obstruction mentioned in Replacement 7: ordinary covers can fail to exist. The ordinary-top notation is not extended to infinite-dimensional algebras.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -443,17 +507,44 @@
-\phantomsection\label{not:graded-top}
-In the graded setting, write\comm{use other symbol(make a macro) to not confused with ungraded one}
+\begin{definition}\label{not:graded-top}
+The \defn{graded top} of a graded right $A$-module $M$ is the graded right $S$-module
 \[
-\top M:=M/MA_+
+\grtop M:=M/MA_+.
 \]
-and call this quotient the \defn{graded top}.
-It is a graded right $S$-module.
-For finite-dimensional $A$, we have $A_+=\rad A$\comm{write lemma for this claim??}, so it agrees with Definition~\ref{def:module-top}.
-For infinite-dimensional $A$, the two ideals need not agree \comm{example? put in advanced}; $\top M$ in the graded discussion always denotes $M/MA_+$.
+\end{definition}
 
+For a degree-preserving map $f:M\to N$, write
+$\grtop f:\grtop M\to\grtop N$, $m+MA_+\mapsto f(m)+NA_+$.
+
+\begin{lemma}\label{lem:graded-radical}
+If $A$ is finite-dimensional, then $A_+=\rad A$.
+Consequently, $\grtop M=\top M$ for every graded right $A$-module $M$, with $\top M$ carrying the quotient grading.
+\end{lemma}
+
 \begin{supplementary}
-If $A$ is finite-dimensional, then $A_d=0$ for all sufficiently large $d$, so $(A_+)^r=0$ for some $r$.
+\begin{proof}
+If $A$ is finite-dimensional, then $A_d=0$ for all sufficiently large $d$, so $(A_+)^r=0$ for some integer $r\geq1$.
 For any simple right module $L$, the submodule $LA_+$ is either $0$ or $L$.
 The latter gives $L=L(A_+)^r=0$, a contradiction.
 Thus $A_+$ annihilates every simple module and is contained in $\rad A$.
-Since $A/A_+\cong S$ is semisimple, the reverse inclusion follows, giving $A_+=\rad A$.
+Since $A/A_+\cong S$ is semisimple, every non-zero element of $S$ acts non-trivially on some simple right $S$-module.
+Regarding these as simple $A$-modules shows that $\rad A\subseteq A_+$.
+\end{proof}
 \end{supplementary}
+
+\begin{advanced}
+\begin{example}\label{ex:graded-radical-infinite}
+The equality $A_+=\rad A$ can fail when $A$ is infinite-dimensional.
+Take $A=\Bbbk[x]$ with $\deg x=1$.
+Then $A_+=(x)$, whereas $\rad A=0$.
+Indeed, if $0\neq f\in\rad A$, then $xf\in\rad A$, and the first paragraph of the proof of Lemma~\ref{lem:nakayama} gives a right inverse to $1-xf$.
+This is impossible because $1-xf$ has positive degree.
+In particular, $A/\rad A=A$, whereas $\grtop A=\Bbbk$.
+
+Over this algebra, even the ordinary module $\Bbbk=A/(x)$ has no projective cover.
+Suppose $p:P\to\Bbbk$ were one, and choose $u\in P$ with $p(u)=1$.
+Then $p(uA)=\Bbbk$, so $P=uA$.
+The surjection $A\to P$, $a\mapsto ua$, splits because $P$ is projective.
+The resulting projection $A\to A$ is multiplication by an idempotent $e\neq0$, and $P\cong eA$.
+Since $\Bbbk[x]$ has no idempotents other than $0$ and $1$, we have $P\cong A$.
+But every surjection $A\to\Bbbk$ maps the proper submodule $(x-1)A$ onto $\Bbbk$, contradicting the cover property.
+\end{example}
+\end{advanced}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\phantomsection\label{not:graded-top}
In the graded setting, write\comm{use other symbol(make a macro) to not confused with ungraded one}
\[
\top M:=M/MA_+
\]
and call this quotient the \defn{graded top}.
It is a graded right $S$-module.
For finite-dimensional $A$, we have $A_+=\rad A$\comm{write lemma for this claim??}, so it agrees with Definition~\ref{def:module-top}.
For infinite-dimensional $A$, the two ideals need not agree \comm{example? put in advanced}; $\top M$ in the graded discussion always denotes $M/MA_+$.

\begin{supplementary}
If $A$ is finite-dimensional, then $A_d=0$ for all sufficiently large $d$, so $(A_+)^r=0$ for some $r$.
For any simple right module $L$, the submodule $LA_+$ is either $0$ or $L$.
The latter gives $L=L(A_+)^r=0$, a contradiction.
Thus $A_+$ annihilates every simple module and is contained in $\rad A$.
Since $A/A_+\cong S$ is semisimple, the reverse inclusion follows, giving $A_+=\rad A$.
\end{supplementary}
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
\begin{definition}\label{not:graded-top}
The \defn{graded top} of a graded right $A$-module $M$ is the graded right $S$-module
\[
\grtop M:=M/MA_+.
\]
\end{definition}

For a degree-preserving map $f:M\to N$, write
$\grtop f:\grtop M\to\grtop N$, $m+MA_+\mapsto f(m)+NA_+$.

\begin{lemma}\label{lem:graded-radical}
If $A$ is finite-dimensional, then $A_+=\rad A$.
Consequently, $\grtop M=\top M$ for every graded right $A$-module $M$, with $\top M$ carrying the quotient grading.
\end{lemma}

\begin{supplementary}
\begin{proof}
If $A$ is finite-dimensional, then $A_d=0$ for all sufficiently large $d$, so $(A_+)^r=0$ for some integer $r\geq1$.
For any simple right module $L$, the submodule $LA_+$ is either $0$ or $L$.
The latter gives $L=L(A_+)^r=0$, a contradiction.
Thus $A_+$ annihilates every simple module and is contained in $\rad A$.
Since $A/A_+\cong S$ is semisimple, every non-zero element of $S$ acts non-trivially on some simple right $S$-module.
Regarding these as simple $A$-modules shows that $\rad A\subseteq A_+$.
\end{proof}
\end{supplementary}

\begin{advanced}
\begin{example}\label{ex:graded-radical-infinite}
The equality $A_+=\rad A$ can fail when $A$ is infinite-dimensional.
Take $A=\Bbbk[x]$ with $\deg x=1$.
Then $A_+=(x)$, whereas $\rad A=0$.
Indeed, if $0\neq f\in\rad A$, then $xf\in\rad A$, and the first paragraph of the proof of Lemma~\ref{lem:nakayama} gives a right inverse to $1-xf$.
This is impossible because $1-xf$ has positive degree.
In particular, $A/\rad A=A$, whereas $\grtop A=\Bbbk$.

Over this algebra, even the ordinary module $\Bbbk=A/(x)$ has no projective cover.
Suppose $p:P\to\Bbbk$ were one, and choose $u\in P$ with $p(u)=1$.
Then $p(uA)=\Bbbk$, so $P=uA$.
The surjection $A\to P$, $a\mapsto ua$, splits because $P$ is projective.
The resulting projection $A\to A$ is multiplication by an idempotent $e\neq0$, and $P\cong eA$.
Since $\Bbbk[x]$ has no idempotents other than $0$ and $1$, we have $P\cong A$.
But every surjection $A\to\Bbbk$ maps the proper submodule $(x-1)A$ onto $\Bbbk$, contradicting the cover property.
\end{example}
\end{advanced}
```

</details>

### 9c. Use the explicit kernel maps in the graded definition

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:530), line 530. **Changes:** +1 / -1 lines.

Carry the clarification of Replacement 6 into the graded definition. Keep the actual domains, codomains, and kernel formulae visible.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -530,1 +621,1 @@
-It is \defn{minimal} if each surjection onto the preceding kernel, including $p_0:P_0\to M$, is a graded projective cover.
+It is \defn{minimal} if $p_0:P_0\to M$ and the maps $p_i:P_i\to K_i$, $x\mapsto d_i(x)$, with $K_1=\Ker p_0$ and $K_i=\Ker d_{i-1}$ for $i\geq2$, are graded projective covers for all $i\geq1$.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
It is \defn{minimal} if each surjection onto the preceding kernel, including $p_0:P_0\to M$, is a graded projective cover.
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
It is \defn{minimal} if $p_0:P_0\to M$ and the maps $p_i:P_i\to K_i$, $x\mapsto d_i(x)$, with $K_1=\Ker p_0$ and $K_i=\Ker d_{i-1}$ for $i\geq2$, are graded projective covers for all $i\geq1$.
```

</details>

### 9d. Link the graded-top notation table entry to its definition

**Source:** [Lecture_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:366), line 366. **Changes:** +1 / -1 lines.

Update the symbol and explanation while retaining the original hyperlink label. The ordinary-top entry remains unchanged.

```diff
--- a/Lecture_Koszul.tex
+++ b/Lecture_Koszul.tex
@@ -366,1 +367,1 @@
-$\top M=M/MA_+$ & Graded top; used in place of the ordinary top in the graded setting. & \hyperref[not:graded-top]{\pageref*{not:graded-top}}\\[3pt]
+$\grtop M=M/MA_+$ & Graded top of a graded right $A$-module. & \hyperref[not:graded-top]{\pageref*{not:graded-top}}\\[3pt]
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
$\top M=M/MA_+$ & Graded top; used in place of the ordinary top in the graded setting. & \hyperref[not:graded-top]{\pageref*{not:graded-top}}\\[3pt]
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
$\grtop M=M/MA_+$ & Graded top of a graded right $A$-module. & \hyperref[not:graded-top]{\pageref*{not:graded-top}}\\[3pt]
```

</details>

### 9e. Avoid repeating the radical calculation

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:590), line 590. **Changes:** +0 / -1 lines.

Remove the bare repeated radical assertion: Replacement 9b now gives its statement and proof in the requested advanced block. The surrounding supplementary explanation that forgetting grading need not preserve covers stays unchanged.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -590,1 +680,0 @@
-Also, $\rad\Bbbk[x]=0$, whereas $A_+=(x)$.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
Also, $\rad\Bbbk[x]=0$, whereas $A_+=(x)$.
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

Delete the passage without replacement.

```tex
```

</details>

---

<a id="replacement-10"></a>
## Replacement 10: Define noetherianity and explain its role

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:622), lines 622-626. **Changes:** +24 / -5 lines.

Keep this entire discussion in the main text. Define both one-sided conditions, then separate existence of minimal resolutions from finite generation of their terms. The case $S=A/A_+$ prepares the next lecture without using any not-yet-defined Koszul terminology.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -622,5 +712,24 @@
-\comm{put right/left noetherian in definition environment.  this paragraph is important and explains why noetherian is important when it comes to considering Koszul algebras.}
-If $M$ is finitely generated, then $\top M$ is finite-dimensional, so its first graded projective cover is finitely generated by \eqref{eq:graded-cover-terms}.
-But the kernel need not be finitely generated.
-One sufficient condition is that $A$ be \defn{right noetherian}, meaning that every submodule of a finitely generated \emph{right} $A$-module is finitely generated.
-Without this assumption, boundedness below and local finite-dimensionality still suffice for the minimal resolution above.
+\begin{definition}\label{def:noetherian-algebra}
+An algebra $A$ is \defn{right noetherian} if every submodule of every finitely generated right $A$-module is finitely generated.
+It is \defn{left noetherian} if the same condition holds for left $A$-modules.
+It is \defn{noetherian} if it is both right and left noetherian.
+\end{definition}
+
+If a graded module $M$ is finitely generated, then $\grtop M$ is finite-dimensional: the images of a finite homogeneous generating set generate $\grtop M$ over the finite-dimensional algebra $S$.
+Its graded projective cover is therefore finitely generated by \eqref{eq:graded-cover-terms}.
+The kernel need not be finitely generated unless we impose an additional condition.
+
+\begin{corollary}\label{cor:noetherian-minimal-resolution}
+Assume that $A$ is right noetherian.
+Every finitely generated graded right $A$-module has a minimal graded projective resolution whose terms and successive kernels are finitely generated.
+In particular, this applies to $S=A/A_+$.
+\end{corollary}
+
+\begin{proof}
+A finitely generated graded module is bounded below and locally finite-dimensional, since it is a quotient of a finite direct sum of shifts of $A$.
+Its graded projective cover is finitely generated by the preceding paragraph.
+Right noetherianity makes the kernel finitely generated, so the same argument applies successively to every kernel.
+\end{proof}
+
+Right noetherianity ensures finite generation at every step.
+Without that assumption, boundedness below and local finite-dimensionality still suffice for existence of a minimal graded resolution by Theorem~\ref{thm:minimal-resolution}.
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\comm{put right/left noetherian in definition environment.  this paragraph is important and explains why noetherian is important when it comes to considering Koszul algebras.}
If $M$ is finitely generated, then $\top M$ is finite-dimensional, so its first graded projective cover is finitely generated by \eqref{eq:graded-cover-terms}.
But the kernel need not be finitely generated.
One sufficient condition is that $A$ be \defn{right noetherian}, meaning that every submodule of a finitely generated \emph{right} $A$-module is finitely generated.
Without this assumption, boundedness below and local finite-dimensionality still suffice for the minimal resolution above.
```

</details>

<details>
<summary><strong>Proposed replacement: exact TeX</strong></summary>

```tex
\begin{definition}\label{def:noetherian-algebra}
An algebra $A$ is \defn{right noetherian} if every submodule of every finitely generated right $A$-module is finitely generated.
It is \defn{left noetherian} if the same condition holds for left $A$-modules.
It is \defn{noetherian} if it is both right and left noetherian.
\end{definition}

If a graded module $M$ is finitely generated, then $\grtop M$ is finite-dimensional: the images of a finite homogeneous generating set generate $\grtop M$ over the finite-dimensional algebra $S$.
Its graded projective cover is therefore finitely generated by \eqref{eq:graded-cover-terms}.
The kernel need not be finitely generated unless we impose an additional condition.

\begin{corollary}\label{cor:noetherian-minimal-resolution}
Assume that $A$ is right noetherian.
Every finitely generated graded right $A$-module has a minimal graded projective resolution whose terms and successive kernels are finitely generated.
In particular, this applies to $S=A/A_+$.
\end{corollary}

\begin{proof}
A finitely generated graded module is bounded below and locally finite-dimensional, since it is a quotient of a finite direct sum of shifts of $A$.
Its graded projective cover is finitely generated by the preceding paragraph.
Right noetherianity makes the kernel finitely generated, so the same argument applies successively to every kernel.
\end{proof}

Right noetherianity ensures finite generation at every step.
Without that assumption, boundedness below and local finite-dimensionality still suffice for existence of a minimal graded resolution by Theorem~\ref{thm:minimal-resolution}.
```

</details>

---

<a id="mechanical-changes"></a>
## Mechanical Changes

All locations in this section are in **Lecture_Koszul_S4.tex**, except where explicitly stated.

### Radical notation

- Remove the resolved comment and abbreviation at **lines 144-145**.
- Replace $J$ by $\rad A$ at **146, 150-152, 159-160, 165, 169-171, 179, 184, 194, and 206**.
- When $A$ is finite-dimensional, use module radicals at **190, 195, 198, 200, 203, 237, 246, 254-255, 292, and 359**: for example, $\rad M$, $\rad P$, $\rad(e_{11}A)$, and $\rad P_{i-1}$.
- At **190 and 246**, remove the redundant product expression rather than repeating the same module radical on both sides of an equality.
- The corresponding changes at **251** and in the general-cover proof are included in Replacements 3b and 4. The old paragraph at **214-216** is removed in Replacement 2b.
- Retain $M\rad A$ in the general Nakayama statement and proof, and in Replacement 1: $A$ is not assumed finite-dimensional there. Retain the higher-power product $M(\rad A)^r$ where it is used to prove the finite-dimensional version.
- Write powers as $(\rad A)^r$, not $\rad A^r$. No abbreviation $J$ remains.

### Graded-top notation

- Replace `\top` by `\grtop` at **467, 479, 484, 491, 493-495, 502, 504, 508, 511, 516-517, 521, 555, 557, 612, and 618**.
- Replacements 9b and 10 already handle **446, 451, and 623**.
- This includes maps such as $\grtop p$ as well as modules such as $\grtop M$ and $(\grtop P_i)_d$.
- Keep ordinary $\top$ unchanged. In particular, the comparison $\grtop M=\top M$ in Replacement 9b intentionally uses both symbols.
- The mother-file macro and notation-table entry are quoted in Replacements 9a and 9d. No other lecture uses the `\top` macro in a graded formula requiring a dependent correction.

### Minor grammatical correction

- **Line 196:** change “the maximal semisimple quotients of $M$” to “the maximal semisimple quotient of $M$”.

---

<a id="checks"></a>
## Checks

### Comment Coverage

| Original comment | Proposed response |
|---|---|
| 144: use $\rad A$, not $J$ | Location-only radical changes, using module radicals where $A$ is finite-dimensional |
| 233: why must $P$ be finite-dimensional? | Replacements 2 and 3 remove the restriction and repair the proof |
| 262: where are the finite-dimensionality assumptions used? | Replacement 4 separates existence cases and adds the requested remark |
| 340-341: shorten the free-resolution proof | Replacement 5b uses $A^{\oplus N}$ and iterates kernels |
| 353: remove “as indicated” | Replacement 6 specifies the domains and codomains of the kernel maps |
| 354: draw the syzygy factorisations | Replacement 6 adds the labelled kernel-factorisation diagram, without using syzygies to define minimality |
| 364: relax finite-dimensionality assumptions | Replacement 7 treats arbitrary modules over finite-dimensional algebras and unrestricted uniqueness |
| 431: use a corollary | Replacement 8 |
| 444: distinguish the graded top | Replacement 9 and the location-only substitutions |
| 450: prove $A_+=\rad A$ as a lemma | Replacement 9b, with supplementary proof |
| 451: give an infinite-dimensional example, advanced | Replacement 9b |
| 622: define right/left noetherian and retain the important consequence | Replacement 10, all in the main text |

### Mathematical Dependencies

- The extension of Nakayama to arbitrary modules is contained in the compact remark after Nakayama's lemma. It uses **nilpotence of $\rad A$**, not finite-generation Nakayama without its hypothesis.
- Module radicals replace products with $\rad A$ only where the finite-dimensionality of $A$ has been specified.
- The general cover construction uses the preceding finite-dimensional case, semisimplicity of $A/\rad A$, arbitrary direct sums of projectives, and the finite-dimensional Nakayama remark.
- Uniqueness of covers and minimal resolutions uses projectivity and the cover property only.
- Minimality is defined using explicit kernel maps. Only after the uniqueness theorem does a remark name the kernels in a minimal resolution as syzygies of $M$ and state independence up to isomorphism.
- The graded-top map on morphisms is specified before writing $\grtop p$.
- The polynomial-ring radical counterexample works over any field and does not assume infinitely many field elements.
- Right noetherianity is used for finite generation of successive kernels, not for existence of bounded below locally finite-dimensional graded resolutions.

### Verification Status

- The proposal is based on the synced Lecture 4 source, not an earlier revision.
- All 12 active comments are covered; existing labels are retained.
- The proposed new labels and macro have been checked against the saved sources.
- Applied the approved replacements and notation changes to Lecture 4, together with the macro and notation-table entry in the mother file. Other lecture sources and homework remain unchanged.
- Both the built-in compiler and the local TeX Live build succeeded with the existing hidden-content setting. The updated **Lecture_Koszul.pdf** is saved in the course folder.
- Visually checked the kernel-factorisation diagram on page 51. Increased its column and row spacing and moved the diagonal labels above the arrows to prevent overlap; the passages above record this layout-only adjustment.
- The existing undefined reference **eq:tensor-dual-actions** in Lecture 3 remains outside the scope of these edits. The build also reports frame-break warnings, a small overfull line in Lecture 1, and an underfull notation-table entry.
- No document or preview was opened in the side panel.
