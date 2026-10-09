# Change Proposal 6: Lecture 1

> **Applied on 9 October 2026.** The approved example revision and structural reorganisation are complete. This file preserves the original replacement and records the expanded changes, compilation, and layout checks.

**Prepared:** 9 October 2026  
**Source:** [2026_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1332)

## Scope

Remove the entire discussion of bimodule blocks and their transposition. Explain instead why one linear functional corresponds to different right and left $S$-linear maps, and why the dual-comparison isomorphism does not identify those maps by equality.

**Related proposal:** [Change Proposal 5](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Planning/ChangeProposal5_Lecture1.md) supplies the separability citation and was applied in the same update.

## Replacement 1: Different Maps, Isomorphic Duals

**Source:** [Example 1.50, line 1332](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1332)  
**Added:** `+40` lines  
**Removed:** `-51` lines

The replacement:

- Removes both block matrices, the general block decomposition, and the block-reversal calculation.
- Uses only $S=\Bbbk e_1\oplus\Bbbk e_2$ and $V=\Bbbk e_{12}$.
- Derives the values $f(e_{12})=e_2$ and $g(e_{12})=e_1$ from the respective linearity conditions and the requirement that composition with $\tau$ gives $\varepsilon$.
- Verifies the required linearity and shows explicitly that neither map has the opposite linearity.
- Explains what the comparison isomorphism does, using the existing equation reference rather than a new diagram.

### Line-by-Line Diff

**Legend:** `-` removes a line; `+` adds a line; a leading space retains context. The hunk numbers refer to the current source and the proposed source.

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1332,53 +1332,42 @@
 \begin{example}\label{ex:dual-blocks}
-We compute how duality transposes bimodule blocks and how one linear functional gives different left and right $S$-linear maps.
-Let $S=\Bbbk^{\oplus r}$ with coordinate idempotents $e_1,\ldots,e_r$ and $\tau(e_i)=1$.
-Thus $1=\sum_i e_i$ and $e_ie_j=\delta_{ij}e_i$; in the diagonal matrix realisation, $e_i=e_{ii}$.
-For an $S$-bimodule $M$, write its elements in blocks:
-\[
-M\cong
-\begin{pmatrix}
-e_1Me_1&\cdots&e_1Me_r\\
-\vdots&\ddots&\vdots\\
-e_rMe_1&\cdots&e_rMe_r
-\end{pmatrix},
-\qquad m\longmapsto(e_i m e_j)_{i,j}.
-\]
-The block matrix denotes the direct sum of its entries; its inverse sends $(m_{ij})_{i,j}$ to $\sum_{i,j}m_{ij}$.
-The action $(s\lambda t)(m)=\lambda(tms)$ from \eqref{eq:bimodule-dual-actions} reverses the blocks:
-\[
-D(M)\cong
-\begin{pmatrix}
-D(e_1Me_1)&\cdots&D(e_rMe_1)\\
-\vdots&\ddots&\vdots\\
-D(e_1Me_r)&\cdots&D(e_rMe_r)
-\end{pmatrix},
-\qquad
-e_jD(M)e_i\cong D(e_iMe_j).
-\]
-The last isomorphism restricts a functional to $e_iMe_j$; its inverse extends that functional by zero on the other blocks.
-
-For $V=(\Bbbk A_2)_1=\Bbbk e_{12}$, the block positions are
-\[
-V=
-\begin{pmatrix}0&\Bbbk\\0&0\end{pmatrix},
-\qquad
-D(V)\cong
-\begin{pmatrix}0&0\\\Bbbk&0\end{pmatrix}.
-\]
-Let $\varepsilon\in D(V)$ satisfy $\varepsilon(e_{12})=1$.
-Then $e_2\varepsilon e_1=\varepsilon$, and $\varepsilon$ has degree $-1$ in $\bbD(V)$.
-Under \eqref{eq:dual-comparison}, the corresponding right and left $S$-linear maps are
-\[
-\alpha_V^{-1}(\varepsilon):V\to S,\quad e_{12}\mapsto e_2,
-\qquad
-\beta_V^{-1}(\varepsilon):V\to S,\quad e_{12}\mapsto e_1.
-\]
-As $\Bbbk$-linear maps $V\to S$,
-\[
-\alpha_V^{-1}(\varepsilon)\neq\beta_V^{-1}(\varepsilon),
-\qquad
-\tau\circ\alpha_V^{-1}(\varepsilon)
-=\varepsilon
-=\tau\circ\beta_V^{-1}(\varepsilon).
-\]
+The right and left $S$-duals may consist of different maps to $S$, even though \eqref{eq:dual-comparison} identifies both with the linear dual.
+Let $S=(\Bbbk A_2)_0=\Bbbk e_1\oplus\Bbbk e_2$ and $V=(\Bbbk A_2)_1=\Bbbk e_{12}$, where $e_1=e_{11}$ and $e_2=e_{22}$.
+Use the symmetrising form and linear functional
+\[
+\begin{aligned}
+\tau:S&\longrightarrow\Bbbk,& ae_1+be_2&\longmapsto a+b,\\
+\varepsilon:V&\longrightarrow\Bbbk,& ce_{12}&\longmapsto c
+\quad(a,b,c\in\Bbbk).
+\end{aligned}
+\]
+
+For a right $S$-linear map $f:V\to S$,
+\[
+f(e_{12})=f(e_{12}e_2)=f(e_{12})e_2\in\Bbbk e_2.
+\]
+Requiring $\tau\circ f=\varepsilon$ therefore forces $f(e_{12})=e_2$.
+Conversely, the $\Bbbk$-linear map determined by $f(e_{12})=e_2$ is right $S$-linear: for $s=ae_1+be_2\in S$, we have $f(e_{12}s)=f(be_{12})=be_2=f(e_{12})s$.
+
+For a left $S$-linear map $g:V\to S$,
+\[
+g(e_{12})=g(e_1e_{12})=e_1g(e_{12})\in\Bbbk e_1.
+\]
+Requiring $\tau\circ g=\varepsilon$ instead forces $g(e_{12})=e_1$.
+Conversely, the $\Bbbk$-linear map determined by $g(e_{12})=e_1$ is left $S$-linear: for $s=ae_1+be_2\in S$, we have $g(se_{12})=g(ae_{12})=ae_1=sg(e_{12})$.
+
+The maps are not interchangeable: $f$ is not left $S$-linear, and $g$ is not right $S$-linear, since
+\[
+f(e_1e_{12})=e_2\neq0=e_1f(e_{12}),
+\qquad
+g(e_{12}e_2)=e_1\neq0=g(e_{12})e_2.
+\]
+Nevertheless, composing either map with $\tau$ gives $\varepsilon$.
+Thus the comparison maps in \eqref{eq:dual-comparison} satisfy
+\[
+\alpha_V(f)=\varepsilon=\beta_V(g),
+\qquad
+(\beta_V^{-1}\circ\alpha_V)(f)=g\neq f.
+\]
+The isomorphism $V^*\xrightarrow{\sim}{}^*V$ sends $f$ to $g$; it is not equality of the two spaces of maps inside $\Hom_\Bbbk(V,S)$.
+Although $S$ is commutative, its left and right actions on $V$ differ.
 \end{example}
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
\begin{example}\label{ex:dual-blocks}
We compute how duality transposes bimodule blocks and how one linear functional gives different left and right $S$-linear maps.
Let $S=\Bbbk^{\oplus r}$ with coordinate idempotents $e_1,\ldots,e_r$ and $\tau(e_i)=1$.
Thus $1=\sum_i e_i$ and $e_ie_j=\delta_{ij}e_i$; in the diagonal matrix realisation, $e_i=e_{ii}$.
For an $S$-bimodule $M$, write its elements in blocks:
\[
M\cong
\begin{pmatrix}
e_1Me_1&\cdots&e_1Me_r\\
\vdots&\ddots&\vdots\\
e_rMe_1&\cdots&e_rMe_r
\end{pmatrix},
\qquad m\longmapsto(e_i m e_j)_{i,j}.
\]
The block matrix denotes the direct sum of its entries; its inverse sends $(m_{ij})_{i,j}$ to $\sum_{i,j}m_{ij}$.
The action $(s\lambda t)(m)=\lambda(tms)$ from \eqref{eq:bimodule-dual-actions} reverses the blocks:
\[
D(M)\cong
\begin{pmatrix}
D(e_1Me_1)&\cdots&D(e_rMe_1)\\
\vdots&\ddots&\vdots\\
D(e_1Me_r)&\cdots&D(e_rMe_r)
\end{pmatrix},
\qquad
e_jD(M)e_i\cong D(e_iMe_j).
\]
The last isomorphism restricts a functional to $e_iMe_j$; its inverse extends that functional by zero on the other blocks.

For $V=(\Bbbk A_2)_1=\Bbbk e_{12}$, the block positions are
\[
V=
\begin{pmatrix}0&\Bbbk\\0&0\end{pmatrix},
\qquad
D(V)\cong
\begin{pmatrix}0&0\\\Bbbk&0\end{pmatrix}.
\]
Let $\varepsilon\in D(V)$ satisfy $\varepsilon(e_{12})=1$.
Then $e_2\varepsilon e_1=\varepsilon$, and $\varepsilon$ has degree $-1$ in $\bbD(V)$.
Under \eqref{eq:dual-comparison}, the corresponding right and left $S$-linear maps are
\[
\alpha_V^{-1}(\varepsilon):V\to S,\quad e_{12}\mapsto e_2,
\qquad
\beta_V^{-1}(\varepsilon):V\to S,\quad e_{12}\mapsto e_1.
\]
As $\Bbbk$-linear maps $V\to S$,
\[
\alpha_V^{-1}(\varepsilon)\neq\beta_V^{-1}(\varepsilon),
\qquad
\tau\circ\alpha_V^{-1}(\varepsilon)
=\varepsilon
=\tau\circ\beta_V^{-1}(\varepsilon).
\]
\end{example}
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
\begin{example}\label{ex:dual-blocks}
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
Requiring $\tau\circ f=\varepsilon$ therefore forces $f(e_{12})=e_2$.
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
```

</details>

## Checks

- [x] The existing passage matches the current source uniquely.
- [x] The block-transposition material is removed entirely.
- [x] The right and left linearity calculations, the failures of opposite linearity, and the comparison formulas have been checked.
- [x] The label `ex:dual-blocks` is retained so the existing exercise reference remains valid; no other passage changes.
- [x] No commented-out content or hidden-content setting changes.
- [x] Approval received for the example revision and the expanded reorganisation below.
- [x] Applied and compiled with the existing hidden-content setting.

---

## Approved Structural Revision: Sections 1.11 and 1.12

**Authorisation:** The user agreed to the refined flow, requested that it be recorded here, and instructed that all pending changes be applied. The earlier example replacement is incorporated into this reorganisation rather than applied as a separate second replacement.

### Agreed Order

| Section | Revised sequence |
| --- | --- |
| **1.11: Duals over $S$** | Ungraded right and left duals; their graded upgrades; biduality without a chosen form and its graded consequence; an advanced block containing the bimodule actions and both two-sided constructions. |
| **1.12: Comparing the duals** | Symmetrising forms and examples; one theorem combining ungraded and graded comparisons, with the two-sided extension in an advanced block; the proof in that order; the revised example; dependence on the form; transported $A$-actions. |
| **Exercises** | Move the longer exercise on transported actions and its hidden solution here without changing their contents. |

The central conclusion is that, **after choosing a symmetrising form, the different dual constructions are naturally isomorphic**, separately in the ungraded and graded settings. This does not identify the full linear dual with the graded linear dual for arbitrary infinite-dimensional modules, or identify distinct maps by equality.

**Scope:** The mathematical changes are in Lecture 1. Three later cross-reference nouns are changed from “Proposition” to “Theorem” to refer correctly to the combined result; no mathematical content of Lectures 2 or 3 changes. The old comparison labels are retained as aliases for the combined theorem. Commented-out content and the preamble are preserved.

### Integrated Line-by-Line Diff

This is the complete diff for this application, including the citation and bibliography entry already recorded in Change Proposal 5. **Added:** `+225` lines; **removed:** `-214` lines. Moved passages necessarily appear as removals and additions.

```diff
--- existing/2026_Koszul.tex
+++ applied/2026_Koszul.tex
@@ -713,7 +713,7 @@
 For a finite-dimensional semisimple $\Bbbk$-algebra $S$, semisimplicity of $S^\en$ requires an additional condition.
 For a field extension $K/\Bbbk$, give $K\otimes_\Bbbk S$ the multiplication $(c\otimes s)(d\otimes t)=cd\otimes st$.
 The algebra $S$ is called \defn{separable over $\Bbbk$} if $K\otimes_\Bbbk S$ is semisimple for every field extension $K/\Bbbk$.
-We record the following fact without proof:
+By \cite[Theorem~6.1.2, p.~105]{DK94},
 \[
 S^\en\text{ is semisimple}
 \quad\Longleftrightarrow\quad
@@ -952,7 +952,7 @@
 
 Fix a finite-dimensional semisimple $\Bbbk$-algebra $S$, which is regarded as concentrated in degree $0$ when treated as a graded algebra.
 Besides the $\Bbbk$-linear dual, we will also work with duals defined by left $S$-linear maps and right $S$-linear maps.
-Their definitions differ, even though the resulting spaces can be identified after a choice of form.
+We first define these duals without grading, then apply the constructions in each degree.
 %Their tensor and biduality isomorphisms in Proposition~\ref{prop:tensor-duals} and Lemma~\ref{lem:S-bidual} therefore construct quadratic duality without a choice of form; replacing them throughout by $D$ requires an identification $S\cong D(S)$.
 %\comm{what is said here is not understandable to beginner; you should not mention `quadratic dual' when nobody knows what it is yet}
 
@@ -986,6 +986,90 @@
 {}^*(-):(\Mod(S^\op))^\op\longrightarrow\Mod S.
 \]
 
+The grading is introduced in the same way as in Definition~\ref{def:linear-duals}.
+
+\begin{definition}\label{def:graded-S-duals}
+For graded right and left $S$-modules $M$, respectively, define their \defn{graded $S$-duals} by
+\[
+M^{\grstar}:=\bigoplus_{i\in\Z}(M_{-i})^*,\qquad
+{}^{\grstar}M:=\bigoplus_{i\in\Z}{}^*(M_{-i}),
+\]
+where each indicated summand has degree $i$.
+\end{definition}
+
+For a degree $0$ right $S$-module map $u:M\to N$, define $u^{\grstar}:N^{\grstar}\to M^{\grstar}$ by
+\[
+(u^{\grstar})_i:(N_{-i})^*\longrightarrow(M_{-i})^*,
+\qquad f\longmapsto f\circ u|_{M_{-i}}
+\quad(i\in\Z).
+\]
+For a degree $0$ left module map $u:M\to N$, the same formula defines ${}^{\grstar}u:{}^{\grstar}N\to{}^{\grstar}M$.
+With the actions from Definition~\ref{def:S-duals}, we obtain functors
+\begin{equation}\label{eq:graded-S-dual-functors}
+\begin{aligned}
+(-)^{\grstar}&:(\Grmod S)^\op\longrightarrow\Grmod(S^\op),\\
+{}^{\grstar}(-)&:(\Grmod(S^\op))^\op\longrightarrow\Grmod S.
+\end{aligned}
+\end{equation}
+Each functor in \eqref{eq:graded-S-dual-functors} restricts to locally finite modules: replace $\Grmod$ by $\grmod$ in its source and target.
+Indeed, for $R=S$ or $S^\op$ and $M\in\grmod R$,
+\begin{equation}\label{eq:graded-S-dual-finiteness}
+\dim_\Bbbk\Hom_R(M_{-i},R)
+\leq(\dim_\Bbbk M_{-i})(\dim_\Bbbk R)<\infty
+\quad(i\in\Z).
+\end{equation}
+
+Parentheses on the stars distinguish the graded constructions from the full $S$-duals. In the notation \eqref{eq:graded-hom},
+\[
+M^{\grstar}=\bigoplus_{i\in\Z}\Hom_S^{\Z}(M,S(i)),\qquad
+{}^{\grstar}M=\bigoplus_{i\in\Z}\Hom_{S^\op}^{\Z}(M,S(i)).
+\]
+
+\begin{lemma}\label{lem:S-bidual}
+Coevaluation gives natural isomorphisms of functors
+\[
+\id_{\mod S}\xrightarrow{\sim}{}^*((-)^*),
+\qquad
+\id_{\mod(S^\op)}\xrightarrow{\sim}({}^*(-))^*,
+\]
+with components
+\[
+\begin{aligned}
+\mathrm{coev}_M:M&\xrightarrow{\sim}{}^*(M^*),
+& m&\longmapsto(f\mapsto f(m))
+&& (M\in\mod S),\\
+\mathrm{coev}_N:N&\xrightarrow{\sim}({}^*N)^*,
+& n&\longmapsto(g\mapsto g(n))
+&& (N\in\mod(S^\op)).
+\end{aligned}
+\]
+Thus $(-)^*:(\mod S)^\op\to\mod(S^\op)$ and $ {}^*(-):(\mod(S^\op))^\op\to\mod S$ are inverse dualities.
+\end{lemma}
+
+\begin{proof}
+For $u:M\to N$ in $\mod S$, $m\in M$, and $f\in N^*$,
+\[
+\bigl({}^*(u^*)(\mathrm{coev}_M(m))\bigr)(f)
+=(u^*f)(m)=f(u(m))=\mathrm{coev}_N(u(m))(f).
+\]
+Hence $ {}^*(u^*)\circ\mathrm{coev}_M=\mathrm{coev}_N\circ u$.
+For $M=S$, coevaluation is an isomorphism: its inverse sends $F\in{}^*(S^*)$ to $F(\id_S)$.
+Indeed, every $f\in S^*$ satisfies $f(s)=f(1)s$, so $F(f)=f(1)F(\id_S)=f(F(\id_S))$.
+Restriction to summands identifies the dual of a finite direct sum with the direct sum of the duals; coevaluation therefore is an isomorphism for $S^{\oplus n}$.
+By Corollary~\ref{cor:semisimple-summands}, $M\oplus L\cong S^{\oplus n}$ for some $L$.
+Under the direct sum identifications, $\mathrm{coev}_{M\oplus L}=\mathrm{coev}_M\oplus\mathrm{coev}_L$, so $\mathrm{coev}_M$ is an isomorphism.
+Replacing $S$ by $S^\op$ proves the left module statement.
+\end{proof}
+
+Applying Lemma~\ref{lem:S-bidual} in each degree gives natural isomorphisms
+\[
+\id_{\grmod S}\xrightarrow{\sim}{}^{\grstar}((-)^{\grstar}),
+\qquad
+\id_{\grmod(S^\op)}\xrightarrow{\sim}({}^{\grstar}(-))^{\grstar}.
+\]
+Their components are again given by $m\mapsto(f\mapsto f(m))$.
+Thus the functors in \eqref{eq:graded-S-dual-functors} restrict to inverse dualities on locally finite graded modules.
+
 \begin{advanced}
 Recall from Definition~\ref{def:enveloping-algebra} and \eqref{eq:enveloping-action} that
 \[
@@ -1001,6 +1085,13 @@
 \end{equation}
 where $\lambda\in D(M)$, $f\in M^*$, $g\in{}^*M$, $s,t\in S$, and $m\in M$.
 
+For a finite-dimensional $S$-bimodule $M$, coevaluation in Lemma~\ref{lem:S-bidual} preserves both actions:
+\[
+(s\,\mathrm{coev}_M(m)\,t)(f)=f(sm)t=f(smt)=\mathrm{coev}_M(smt)(f)
+\quad(s,t\in S,\ m\in M,\ f\in M^*).
+\]
+The graded coevaluation maps preserve both actions by the same calculation in each degree.
+
 \begin{definition}\label{def:en-dual}
 The \defn{two-sided dual} of an $S$-bimodule $M$ is
 \[
@@ -1016,6 +1107,23 @@
 On bimodule morphisms it acts by precomposition, as do $D$, $(-)^*$, and ${}^*(-)$; each is a contravariant functor on the category of $S$-bimodules.
 The two-sided dual records both module actions in the target algebra $S^\en$.
 
+For a graded $S$-bimodule $M$, define its \defn{graded two-sided dual} by
+\[
+M^{\grstar[_{\en}]}:=\bigoplus_{i\in\Z}(M_{-i})^{*_{\en}},
+\qquad (M^{\grstar[_{\en}]})_i=(M_{-i})^{*_{\en}}.
+\]
+The bimodule actions in \eqref{eq:bimodule-dual-actions} and Definition~\ref{def:en-dual} give functors
+\begin{equation}\label{eq:graded-bimodule-dual-functors}
+(-)^{\grstar},\ {}^{\grstar}(-),\ (-)^{\grstar[_{\en}]}
+:(\Grmod S^\en)^\op\longrightarrow\Grmod S^\en.
+\end{equation}
+On a degree $0$ bimodule map $u:M\to N$, each functor acts by precomposition in each degree; in particular,
+\[
+(u^{\grstar[_{\en}]})_i:(N_{-i})^{*_{\en}}\longrightarrow(M_{-i})^{*_{\en}},
+\qquad F\longmapsto F\circ u|_{M_{-i}}.
+\]
+These functors restrict to locally finite bimodules: the dimension bound \eqref{eq:graded-S-dual-finiteness} also applies with $R=S^\en$.
+
 The four duals above follow the distinction in Grant--Iyama \cite[\S2.1, pp.~2592--2593]{GI20}, with the following notation changes:
 \[
 \begin{array}{c|c|c}
@@ -1075,8 +1183,11 @@
 \]
 \end{example}
 
-\begin{proposition}[Dual comparison]\label{prop:dual-comparison}
-Choose a symmetrising form $\tau$ on $S$.
+\begin{theorem}[Comparison of duals]\label{prop:dual-comparison}\label{cor:graded-dual-comparison}
+Choose a symmetrising form $\tau:S\to\Bbbk$.
+The right and left $S$-dual functors are naturally isomorphic to the corresponding $\Bbbk$-linear dual functors, both without grading and with grading.
+
+\emph{Ungraded duals.}
 For $M\in\mod S$ and $N\in\mod(S^\op)$, the maps
 \begin{equation}\label{eq:dual-comparison}
 \alpha_M:M^*\longrightarrow D(M),\quad f\longmapsto\tau\circ f,
@@ -1093,18 +1204,43 @@
 \end{aligned}
 \end{equation}
 
+\emph{Graded duals.}
+Composition with $\tau$ in each degree gives natural isomorphisms
+\begin{equation}\label{eq:graded-dual-comparison}
+\begin{aligned}
+\alpha:(-)^{\grstar}&\xrightarrow{\sim}\bbD
+&&\text{of functors }(\grmod S)^\op\longrightarrow\grmod(S^\op),\\
+\beta:{}^{\grstar}(-)&\xrightarrow{\sim}\bbD
+&&\text{of functors }(\grmod(S^\op))^\op\longrightarrow\grmod S.
+\end{aligned}
+\end{equation}
+For $M\in\grmod S$ and $N\in\grmod(S^\op)$, the degree $i$ components are $\alpha_{M_{-i}}$ and $\beta_{N_{-i}}$, respectively.
+
 \begin{advanced}
-If $M$ is an $S$-bimodule, $\alpha_M$ and $\beta_M$ preserve both actions from \eqref{eq:bimodule-dual-actions}.
+\emph{Two-sided duals.}
+If $M$ is a finite-dimensional $S$-bimodule, $\alpha_M$ and $\beta_M$ preserve both actions from \eqref{eq:bimodule-dual-actions}.
 There is also a natural isomorphism $\gamma:(-)^{*_\en}\xrightarrow{\sim}(-)^*$ given by
 \begin{equation}\label{eq:en-dual-comparison}
 \gamma_M:M^{*_{\en}}\to M^*, \qquad F\mapsto \big(m\mapsto \sum_j a_j\tau(b_j)\big)
 \quad\text{for}\quad
 F(m)=\sum_j a_j\otimes b_j^\op.
 \end{equation}
+Consequently, on finite-dimensional $S$-bimodules all four dual functors are naturally isomorphic:
+\[
+(-)^{*_{\en}}\xrightarrow[\gamma]{\sim}(-)^*
+\xrightarrow[\alpha]{\sim}D\xleftarrow[\beta]{\sim}{}^*(-).
+\]
+Applying $\gamma$ in each degree gives the corresponding natural isomorphisms on locally finite graded $S$-bimodules:
+\[
+(-)^{\grstar[_{\en}]}\xrightarrow[\gamma]{\sim}(-)^{\grstar}
+\xrightarrow[\alpha]{\sim}\bbD\xleftarrow[\beta]{\sim}{}^{\grstar}(-).
+\]
+The first chain consists of functors $(\mod S^\en)^\op\to\mod S^\en$; the second consists of functors $(\grmod S^\en)^\op\to\grmod S^\en$.
 \end{advanced}
-\end{proposition}
+\end{theorem}
 
 \begin{proof}
+\emph{Ungraded duals.}
 Non-degeneracy makes $S\to D(S)$, $a\mapsto(s\mapsto\tau(as))$, injective, hence bijective because both spaces have the same finite dimension.
 Thus for $\lambda\in D(M)$, according to whether $M$ is a right or left module, there exist unique $f(m)$ or $g(m)$ in $S$ satisfying
 \begin{equation}\label{eq:dual-inverses}
@@ -1124,7 +1260,13 @@
 Likewise, $\beta_M(gs)(m)=\tau(g(m)s)=\tau(sg(m))=\tau(g(sm))=(\beta_M(g)s)(m)$ for a left module $M$ and $g\in{}^*M$.
 Naturality in \eqref{eq:dual-comparison-functors} is routine to check.
 
+\emph{Graded duals.}
+For a locally finite graded module $M$, take the direct sum over $i\in\Z$ of the ungraded comparison maps on $M_{-i}$.
+Each summand is an isomorphism, so the resulting maps are isomorphisms of degree $0$.
+Naturality in \eqref{eq:graded-dual-comparison} follows by applying the natural isomorphisms \eqref{eq:dual-comparison-functors} in each degree.
+
 \begin{advanced}
+\emph{Two-sided duals.}
 For bimodule compatibility, use \eqref{eq:bimodule-dual-actions} and
 \[
 \tau(sf(tm))=\tau(f(tm)s)=\tau(f(tms)),\qquad
@@ -1142,104 +1284,64 @@
 The argument \eqref{eq:dual-inverses}, applied to $S^{\en}$ and $\tau_{\en}$, makes $F\mapsto\tau_{\en}\circ F$ an isomorphism.
 Thus $\gamma_M$ is an isomorphism.
 For a bimodule map $u:M\to N$ and $F\in N^{*_{\en}}$, the formula \eqref{eq:en-dual-comparison} gives $\gamma_M(F\circ u)=\gamma_N(F)\circ u$, proving naturality.
+Taking the direct sum of $\gamma_{M_{-i}}$ over $i\in\Z$ gives the graded two-sided comparison.
+Each component is a bimodule isomorphism, and naturality follows in each degree from the ungraded comparison.\qedhere
 \end{advanced}
 \end{proof}
-\begin{remark}
-The identifications \eqref{eq:dual-comparison} depend on $\tau$.
-For instance, $\tau(a_1,\ldots,a_r)=\sum_i c_i a_i$ is symmetrising on $\Bbbk^{\oplus r}$ for any $c_i\neq 0$.
-\begin{advanced}
-The two-sided comparison \eqref{eq:en-dual-comparison} also depends on $\tau$; it does not require $S^{\en}$ to be semisimple.
-\end{advanced}
-\end{remark}
 
-\begin{definition}\label{def:graded-S-duals}
-For graded right and left $S$-modules $M$, respectively, define their \defn{graded $S$-duals} by
-\[
-M^{\grstar}:=\bigoplus_{i\in\Z}(M_{-i})^*,\qquad
-{}^{\grstar}M:=\bigoplus_{i\in\Z}{}^*(M_{-i}),
-\]
-where each indicated summand has degree $i$.
-\end{definition}
-
-For a degree $0$ right $S$-module map $u:M\to N$, define $u^{\grstar}:N^{\grstar}\to M^{\grstar}$ by
+\begin{example}\label{ex:dual-blocks}
+The right and left $S$-duals may consist of different maps to $S$, even though \eqref{eq:dual-comparison} identifies both with the linear dual.
+Let $S=(\Bbbk A_2)_0=\Bbbk e_1\oplus\Bbbk e_2$ and $V=(\Bbbk A_2)_1=\Bbbk e_{12}$, where $e_1=e_{11}$ and $e_2=e_{22}$.
+Use the symmetrising form and linear functional
 \[
-(u^{\grstar})_i:(N_{-i})^*\longrightarrow(M_{-i})^*,
-\qquad f\longmapsto f\circ u|_{M_{-i}}
-\quad(i\in\Z).
-\]
-For a degree $0$ left module map $u:M\to N$, the same formula defines ${}^{\grstar}u:{}^{\grstar}N\to{}^{\grstar}M$.
-With the actions from Definition~\ref{def:S-duals}, we obtain functors
-\begin{equation}\label{eq:graded-S-dual-functors}
 \begin{aligned}
-(-)^{\grstar}&:(\Grmod S)^\op\longrightarrow\Grmod(S^\op),\\
-{}^{\grstar}(-)&:(\Grmod(S^\op))^\op\longrightarrow\Grmod S.
+\tau:S&\longrightarrow\Bbbk,& ae_1+be_2&\longmapsto a+b,\\
+\varepsilon:V&\longrightarrow\Bbbk,& ce_{12}&\longmapsto c
+\quad(a,b,c\in\Bbbk).
 \end{aligned}
-\end{equation}
-Each functor in \eqref{eq:graded-S-dual-functors} restricts to locally finite modules: replace $\Grmod$ by $\grmod$ in its source and target.
-Indeed, for $R=S$ or $S^\op$ and $M\in\grmod R$,
-\begin{equation}\label{eq:graded-S-dual-finiteness}
-\dim_\Bbbk\Hom_R(M_{-i},R)
-\leq(\dim_\Bbbk M_{-i})(\dim_\Bbbk R)<\infty
-\quad(i\in\Z).
-\end{equation}
-
-Parentheses on the stars distinguish the graded constructions from the full $S$-duals. In the notation \eqref{eq:graded-hom},
-\[
-M^{\grstar}=\bigoplus_{i\in\Z}\Hom_S^{\Z}(M,S(i)),\qquad
-{}^{\grstar}M=\bigoplus_{i\in\Z}\Hom_{S^\op}^{\Z}(M,S(i)).
 \]
 
-\begin{advanced}
-For a graded $S$-bimodule $M$, define its \defn{graded two-sided dual} by
+For a right $S$-linear map $f:V\to S$,
 \[
-M^{\grstar[_{\en}]}:=\bigoplus_{i\in\Z}(M_{-i})^{*_{\en}},
-\qquad (M^{\grstar[_{\en}]})_i=(M_{-i})^{*_{\en}}.
+f(e_{12})=f(e_{12}e_2)=f(e_{12})e_2\in\Bbbk e_2.
 \]
-The bimodule actions in \eqref{eq:bimodule-dual-actions} and Definition~\ref{def:en-dual} give functors
-\begin{equation}\label{eq:graded-bimodule-dual-functors}
-(-)^{\grstar},\ {}^{\grstar}(-),\ (-)^{\grstar[_{\en}]}
-:(\Grmod S^\en)^\op\longrightarrow\Grmod S^\en.
-\end{equation}
-On a degree $0$ bimodule map $u:M\to N$, each functor acts by precomposition in each degree; in particular,
+Requiring $\tau\circ f=\varepsilon$ therefore forces $f(e_{12})=e_2$.
+Conversely, the $\Bbbk$-linear map determined by $f(e_{12})=e_2$ is right $S$-linear: for $s=ae_1+be_2\in S$, we have $f(e_{12}s)=f(be_{12})=be_2=f(e_{12})s$.
+
+For a left $S$-linear map $g:V\to S$,
 \[
-(u^{\grstar[_{\en}]})_i:(N_{-i})^{*_{\en}}\longrightarrow(M_{-i})^{*_{\en}},
-\qquad F\longmapsto F\circ u|_{M_{-i}}.
+g(e_{12})=g(e_1e_{12})=e_1g(e_{12})\in\Bbbk e_1.
 \]
-These functors restrict to locally finite bimodules: the dimension bound \eqref{eq:graded-S-dual-finiteness} also applies with $R=S^\en$.
-\end{advanced}
+Requiring $\tau\circ g=\varepsilon$ instead forces $g(e_{12})=e_1$.
+Conversely, the $\Bbbk$-linear map determined by $g(e_{12})=e_1$ is left $S$-linear: for $s=ae_1+be_2\in S$, we have $g(se_{12})=g(ae_{12})=ae_1=sg(e_{12})$.
 
-\begin{corollary}\label{cor:graded-dual-comparison}
-Fix a symmetrising form $\tau:S\to\Bbbk$.
-There are natural isomorphisms
+The maps are not interchangeable: $f$ is not left $S$-linear, and $g$ is not right $S$-linear, since
 \[
-\begin{aligned}
-\alpha:(-)^{\grstar}&\xrightarrow{\sim}\bbD
-&&\text{as functors }(\grmod S)^\op\to\grmod(S^\op),\\
-\beta:{}^{\grstar}(-)&\xrightarrow{\sim}\bbD
-&&\text{as functors }(\grmod(S^\op))^\op\to\grmod S.
-\end{aligned}
+f(e_1e_{12})=e_2\neq0=e_1f(e_{12}),
+\qquad
+g(e_{12}e_2)=e_1\neq0=g(e_{12})e_2.
 \]
-\begin{advanced}
-On locally finite graded $S$-bimodules, there are natural isomorphisms of functors $(\grmod S^\en)^\op\to\grmod S^\en$:
+Nevertheless, composing either map with $\tau$ gives $\varepsilon$.
+Thus the comparison maps in \eqref{eq:dual-comparison} satisfy
 \[
-(-)^{\grstar[_{\en}]}
-\xrightarrow[\gamma]{\sim}(-)^{\grstar}
-\xrightarrow[\alpha]{\sim}\bbD
-\xleftarrow[\beta]{\sim}{}^{\grstar}(-).
+\alpha_V(f)=\varepsilon=\beta_V(g),
+\qquad
+(\beta_V^{-1}\circ\alpha_V)(f)=g\neq f.
 \]
-\end{advanced}
-\end{corollary}
+The isomorphism $V^*\xrightarrow{\sim}{}^*V$ sends $f$ to $g$; it is not equality of the two spaces of maps inside $\Hom_\Bbbk(V,S)$.
+Although $S$ is commutative, its left and right actions on $V$ differ.
+\end{example}
 
-\begin{proof}
-For a locally finite graded module $M$, $\alpha_M$ and $\beta_M$ are the direct sums over $i\in\Z$ of the corresponding maps on $M_{-i}$ in Proposition~\ref{prop:dual-comparison}.
-They are isomorphisms of degree $0$; naturality follows by applying the natural isomorphisms \eqref{eq:dual-comparison-functors} in each degree.
+\begin{remark}
+The ungraded and graded identifications in Theorem~\ref{prop:dual-comparison} depend on $\tau$.
+For instance, $\tau(a_1,\ldots,a_r)=\sum_i c_i a_i$ is symmetrising on $\Bbbk^{\oplus r}$ for any $c_i\neq 0$.
+The theorem compares the different dual constructions separately in the ungraded and graded settings; it does not identify $D(M)$ with $\bbD(M)$ for an arbitrary infinite-dimensional graded module.
 \begin{advanced}
-For a locally finite graded bimodule $M$, take the direct sum of the maps $\gamma_{M_{-i}}$ from \eqref{eq:en-dual-comparison}.
-The same degreewise argument proves that $\gamma_M$ is an isomorphism of graded bimodules and is natural in $M$.
+The two-sided comparison \eqref{eq:en-dual-comparison} also depends on $\tau$; it does not require $S^{\en}$ to be semisimple.
 \end{advanced}
-\end{proof}
+\end{remark}
 
-For a graded algebra $A$ with $S=A_0$, Corollary~\ref{cor:graded-dual-comparison} transports the $A$-action \eqref{eq:linear-dual-actions} to the graded $S$-duals of a locally finite graded $A$-module:
+For a graded algebra $A$ with $S=A_0$, Theorem~\ref{cor:graded-dual-comparison} transports the $A$-action \eqref{eq:linear-dual-actions} to the graded $S$-duals of a locally finite graded $A$-module:
 \[
 af=\alpha_M^{-1}(a\alpha_M(f))\quad\text{for right }M,
 \qquad
@@ -1249,7 +1351,38 @@
 The restrictions to $S$ agree with Definition~\ref{def:S-duals}.
 These remain duals over $S$, not duals taking values in $A$.
 The graded $S$-duals are defined without $\tau$, but these transported $A$-actions depend on $\tau$. The canonical graded $A$-module is $\bbD(M)$.
+Exercise~\ref{ex:transported-dual-action} computes this dependence.
 
+\subsection{Exercises}
+
+\begin{exercise}[Categories and shifts]
+Let $A=\Bbbk A_2$ with the grading of Example~\ref{ex:triangular-grading}.
+Show that $e_{11}A$ and $(e_{11}A)(1)$ are isomorphic in $\Mod A$ but not in $\Grmod A$.
+\emph{Hint.} Compare their degree $1$ components. Explain why this does not contradict the fact that the shift functor is an equivalence.
+\end{exercise}
+
+\begin{exercise}[Matrix calculations]
+Verify the grading on $\Bbbk A_n$ in Example~\ref{ex:triangular-grading} using $e_{ij}e_{pq}=\delta_{jp}e_{iq}$.
+Compute $\rad(\Bbbk A_3)$ from the definition.
+\emph{Hint.} The strictly upper triangular ideal $J$ satisfies $J^3=0$. Apply the argument of Example~\ref{ex:semisimple-algebras} to simple modules and to $A/J\cong\Bbbk^{\oplus3}$.
+\end{exercise}
+
+\begin{exercise}[Shifts and duals]
+For $A=\Bbbk A_3$, compute the degrees and all non-zero matrix-unit actions on $\bbD(e_{22}A)$.
+Show that it is not isomorphic to any left module $Ae_{jj}$, even after a shift.
+\emph{Hint.} Compare dimensions and the actions of $e_{11},e_{22},e_{33}$.
+\end{exercise}
+
+\begin{exercise}[Homogeneous maps]
+For the map $f$ in Example~\ref{ex:infinite-hom}, write every non-zero homogeneous component $f_d$ explicitly and prove that no finite sum equals $f$.
+\end{exercise}
+
+\begin{exercise}[Dependence on the form]
+Repeat Example~\ref{ex:dual-blocks} with $\tau(e_i)=c_i\neq0$.
+For $V=\Bbbk e_{12}$, find the right and left $S$-linear maps corresponding to the functional $\varepsilon(e_{12})=1$ under \eqref{eq:dual-comparison}.
+\emph{Check.} Their values on $e_{12}$ are $c_2^{-1}e_2$ and $c_1^{-1}e_1$, respectively.
+\end{exercise}
+
 \begin{exercise}[Dependence of the action on the form]\label{ex:transported-dual-action}
 In this exercise take $\Bbbk=\mathbb Q$.
 Let $A=\Bbbk A_2$, $S=\Bbbk e_{11}\oplus\Bbbk e_{22}$, and $M=e_{11}A$.
@@ -1329,134 +1462,6 @@
 \end{proof}
 \end{hidden}
 
-\begin{example}\label{ex:dual-blocks}
-We compute how duality transposes bimodule blocks and how one linear functional gives different left and right $S$-linear maps.
-Let $S=\Bbbk^{\oplus r}$ with coordinate idempotents $e_1,\ldots,e_r$ and $\tau(e_i)=1$.
-Thus $1=\sum_i e_i$ and $e_ie_j=\delta_{ij}e_i$; in the diagonal matrix realisation, $e_i=e_{ii}$.
-For an $S$-bimodule $M$, write its elements in blocks:
-\[
-M\cong
-\begin{pmatrix}
-e_1Me_1&\cdots&e_1Me_r\\
-\vdots&\ddots&\vdots\\
-e_rMe_1&\cdots&e_rMe_r
-\end{pmatrix},
-\qquad m\longmapsto(e_i m e_j)_{i,j}.
-\]
-The block matrix denotes the direct sum of its entries; its inverse sends $(m_{ij})_{i,j}$ to $\sum_{i,j}m_{ij}$.
-The action $(s\lambda t)(m)=\lambda(tms)$ from \eqref{eq:bimodule-dual-actions} reverses the blocks:
-\[
-D(M)\cong
-\begin{pmatrix}
-D(e_1Me_1)&\cdots&D(e_rMe_1)\\
-\vdots&\ddots&\vdots\\
-D(e_1Me_r)&\cdots&D(e_rMe_r)
-\end{pmatrix},
-\qquad
-e_jD(M)e_i\cong D(e_iMe_j).
-\]
-The last isomorphism restricts a functional to $e_iMe_j$; its inverse extends that functional by zero on the other blocks.
-
-For $V=(\Bbbk A_2)_1=\Bbbk e_{12}$, the block positions are
-\[
-V=
-\begin{pmatrix}0&\Bbbk\\0&0\end{pmatrix},
-\qquad
-D(V)\cong
-\begin{pmatrix}0&0\\\Bbbk&0\end{pmatrix}.
-\]
-Let $\varepsilon\in D(V)$ satisfy $\varepsilon(e_{12})=1$.
-Then $e_2\varepsilon e_1=\varepsilon$, and $\varepsilon$ has degree $-1$ in $\bbD(V)$.
-Under \eqref{eq:dual-comparison}, the corresponding right and left $S$-linear maps are
-\[
-\alpha_V^{-1}(\varepsilon):V\to S,\quad e_{12}\mapsto e_2,
-\qquad
-\beta_V^{-1}(\varepsilon):V\to S,\quad e_{12}\mapsto e_1.
-\]
-As $\Bbbk$-linear maps $V\to S$,
-\[
-\alpha_V^{-1}(\varepsilon)\neq\beta_V^{-1}(\varepsilon),
-\qquad
-\tau\circ\alpha_V^{-1}(\varepsilon)
-=\varepsilon
-=\tau\circ\beta_V^{-1}(\varepsilon).
-\]
-\end{example}
-
-\begin{lemma}\label{lem:S-bidual}
-Coevaluation gives natural isomorphisms of functors
-\[
-\id_{\mod S}\xrightarrow{\sim}{}^*((-)^*),
-\qquad
-\id_{\mod(S^\op)}\xrightarrow{\sim}({}^*(-))^*,
-\]
-with components
-\[
-\begin{aligned}
-\mathrm{coev}_M:M&\xrightarrow{\sim}{}^*(M^*),
-& m&\longmapsto(f\mapsto f(m))
-&& (M\in\mod S),\\
-\mathrm{coev}_N:N&\xrightarrow{\sim}({}^*N)^*,
-& n&\longmapsto(g\mapsto g(n))
-&& (N\in\mod(S^\op)).
-\end{aligned}
-\]
-Thus $(-)^*:(\mod S)^\op\to\mod(S^\op)$ and $ {}^*(-):(\mod(S^\op))^\op\to\mod S$ are inverse dualities.
-For $S$-bimodules, the coevaluation maps preserve both actions.
-No symmetrising form is required.
-\end{lemma}
-
-\begin{proof}
-For $u:M\to N$ in $\mod S$, $m\in M$, and $f\in N^*$,
-\[
-\bigl({}^*(u^*)(\mathrm{coev}_M(m))\bigr)(f)
-=(u^*f)(m)=f(u(m))=\mathrm{coev}_N(u(m))(f).
-\]
-Hence $ {}^*(u^*)\circ\mathrm{coev}_M=\mathrm{coev}_N\circ u$.
-For $M=S$, coevaluation is an isomorphism: its inverse sends $F\in{}^*(S^*)$ to $F(\id_S)$.
-Indeed, every $f\in S^*$ satisfies $f(s)=f(1)s$, so $F(f)=f(1)F(\id_S)=f(F(\id_S))$.
-Restriction to summands identifies the dual of a finite direct sum with the direct sum of the duals; coevaluation therefore is an isomorphism for $S^{\oplus n}$.
-By Corollary~\ref{cor:semisimple-summands}, $M\oplus L\cong S^{\oplus n}$ for some $L$.
-Under the direct sum identifications, $\mathrm{coev}_{M\oplus L}=\mathrm{coev}_M\oplus\mathrm{coev}_L$, so $\mathrm{coev}_M$ is an isomorphism.
-Replacing $S$ by $S^\op$ proves the left module statement.
-For a bimodule $M$, \eqref{eq:bimodule-dual-actions} gives
-\[
-(s\,\mathrm{coev}_M(m)\,t)(f)=f(sm)t=f(smt)=\mathrm{coev}_M(smt)(f)
-\quad(s,t\in S,\ m\in M,\ f\in M^*),
-\]
-which proves bimodule compatibility.
-\end{proof}
-
-\subsection{Exercises}
-
-\begin{exercise}[Categories and shifts]
-Let $A=\Bbbk A_2$ with the grading of Example~\ref{ex:triangular-grading}.
-Show that $e_{11}A$ and $(e_{11}A)(1)$ are isomorphic in $\Mod A$ but not in $\Grmod A$.
-\emph{Hint.} Compare their degree $1$ components. Explain why this does not contradict the fact that the shift functor is an equivalence.
-\end{exercise}
-
-\begin{exercise}[Matrix calculations]
-Verify the grading on $\Bbbk A_n$ in Example~\ref{ex:triangular-grading} using $e_{ij}e_{pq}=\delta_{jp}e_{iq}$.
-Compute $\rad(\Bbbk A_3)$ from the definition.
-\emph{Hint.} The strictly upper triangular ideal $J$ satisfies $J^3=0$. Apply the argument of Example~\ref{ex:semisimple-algebras} to simple modules and to $A/J\cong\Bbbk^{\oplus3}$.
-\end{exercise}
-
-\begin{exercise}[Shifts and duals]
-For $A=\Bbbk A_3$, compute the degrees and all non-zero matrix-unit actions on $\bbD(e_{22}A)$.
-Show that it is not isomorphic to any left module $Ae_{jj}$, even after a shift.
-\emph{Hint.} Compare dimensions and the actions of $e_{11},e_{22},e_{33}$.
-\end{exercise}
-
-\begin{exercise}[Homogeneous maps]
-For the map $f$ in Example~\ref{ex:infinite-hom}, write every non-zero homogeneous component $f_d$ explicitly and prove that no finite sum equals $f$.
-\end{exercise}
-
-\begin{exercise}[Dependence on the form]
-Repeat Example~\ref{ex:dual-blocks} with $\tau(e_i)=c_i\neq0$.
-For $V=\Bbbk e_{12}$, find the right and left $S$-linear maps corresponding to the functional $\varepsilon(e_{12})=1$ under \eqref{eq:dual-comparison}.
-\emph{Check.} Their values on $e_{12}$ are $c_2^{-1}e_2$ and $c_1^{-1}e_1$, respectively.
-\end{exercise}
-
 \pagebreak
 
 \section{Tensor and quadratic algebras}
@@ -1737,7 +1742,7 @@
 =\theta_r\circ(\id_{W^*}\otimes\gamma_V),
 \]
 since both sides send $g\otimes F$, evaluated at $v\otimes w$, to $\sum_j g(a_jw)\tau(b_j)$.
-Thus $\theta_{\en}$ is an isomorphism by Proposition~\ref{prop:dual-comparison}.
+Thus $\theta_{\en}$ is an isomorphism by Theorem~\ref{prop:dual-comparison}.
 Precomposition shows that $\theta_D$ and $\theta_{\en}$ are natural.
 No assumption that $S^\en$ is semisimple is used; compare Remark~\ref{rem:enveloping-semisimple}.
 
@@ -2169,7 +2174,7 @@
 \]
 Non-degeneracy of $\tau$ forces $f(u)=0$ for every $u\in U$.
 For the left dual, $\tau(sg(u))=\tau(g(su))=0$ gives $g(u)=0$ instead.
-Bijectivity of $\alpha_M,\beta_M$ in Proposition~\ref{prop:dual-comparison} proves \eqref{eq:orthogonal-comparison}.
+Bijectivity of $\alpha_M,\beta_M$ in Theorem~\ref{prop:dual-comparison} proves \eqref{eq:orthogonal-comparison}.
 \end{advanced}
 
 \begin{example}\label{ex:symmetric-orthogonals}
@@ -2336,7 +2341,7 @@
 \xrightarrow{F\mapsto\theta_r(F)|_R}R^*\longrightarrow0.
 \end{equation}
 Surjectivity follows from Theorem~\ref{thm:artin-wedderburn}: $R$ has a complement as a right $S$-module, so a right $S$-linear map $R\to S$ extends by zero on that complement.
-Now use Proposition~\ref{prop:quadratic-basic}; the dimension statement follows from Proposition~\ref{prop:dual-comparison}.
+Now use Proposition~\ref{prop:quadratic-basic}; the dimension statement follows from Theorem~\ref{prop:dual-comparison}.
 \end{proof}
 
 Adding relations has the opposite effect after dualising. For $S$-sub-bimodules $R\subset R'\subset V\otimes_S V$,
@@ -2723,6 +2728,12 @@
 \emph{Koszul duality patterns in representation theory},
 J.~Amer.~Math.~Soc.~9 (1996), 473--527.
 
+\bibitem[DK94]{DK94}
+Yu.~A.~Drozd and V.~V.~Kirichenko,
+\emph{Finite Dimensional Algebras},
+Springer-Verlag, Berlin, 1994,
+\href{https://doi.org/10.1007/978-3-642-76244-4}{doi:10.1007/978-3-642-76244-4}.
+
 \bibitem[DNN17]{DNN17}
 S.~D\u{a}sc\u{a}lescu, C.~N\u{a}st\u{a}sescu, and L.~N\u{a}st\u{a}sescu,
 \emph{Graded semisimple algebras are symmetric},
```

<details>
<summary><strong>Existing content: full exact Sections 1.11-1.13 before reorganisation</strong></summary>

```tex
\subsection{\texorpdfstring{Left, right, and two-sided duals over $S$}{Left, right, and two-sided duals over S}}

Fix a finite-dimensional semisimple $\Bbbk$-algebra $S$, which is regarded as concentrated in degree $0$ when treated as a graded algebra.
Besides the $\Bbbk$-linear dual, we will also work with duals defined by left $S$-linear maps and right $S$-linear maps.
Their definitions differ, even though the resulting spaces can be identified after a choice of form.
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

\subsection{Comparing the duals}

To identify $S$-dual with $\Bbbk$-dual, we need a suitable linear functional $S\to\Bbbk$.

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

\begin{proposition}[Dual comparison]\label{prop:dual-comparison}
Choose a symmetrising form $\tau$ on $S$.
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

\begin{advanced}
If $M$ is an $S$-bimodule, $\alpha_M$ and $\beta_M$ preserve both actions from \eqref{eq:bimodule-dual-actions}.
There is also a natural isomorphism $\gamma:(-)^{*_\en}\xrightarrow{\sim}(-)^*$ given by
\begin{equation}\label{eq:en-dual-comparison}
\gamma_M:M^{*_{\en}}\to M^*, \qquad F\mapsto \big(m\mapsto \sum_j a_j\tau(b_j)\big)
\quad\text{for}\quad
F(m)=\sum_j a_j\otimes b_j^\op.
\end{equation}
\end{advanced}
\end{proposition}

\begin{proof}
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

\begin{advanced}
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
\end{advanced}
\end{proof}
\begin{remark}
The identifications \eqref{eq:dual-comparison} depend on $\tau$.
For instance, $\tau(a_1,\ldots,a_r)=\sum_i c_i a_i$ is symmetrising on $\Bbbk^{\oplus r}$ for any $c_i\neq 0$.
\begin{advanced}
The two-sided comparison \eqref{eq:en-dual-comparison} also depends on $\tau$; it does not require $S^{\en}$ to be semisimple.
\end{advanced}
\end{remark}

\begin{definition}\label{def:graded-S-duals}
For graded right and left $S$-modules $M$, respectively, define their \defn{graded $S$-duals} by
\[
M^{\grstar}:=\bigoplus_{i\in\Z}(M_{-i})^*,\qquad
{}^{\grstar}M:=\bigoplus_{i\in\Z}{}^*(M_{-i}),
\]
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

\begin{advanced}
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
\end{advanced}

\begin{corollary}\label{cor:graded-dual-comparison}
Fix a symmetrising form $\tau:S\to\Bbbk$.
There are natural isomorphisms
\[
\begin{aligned}
\alpha:(-)^{\grstar}&\xrightarrow{\sim}\bbD
&&\text{as functors }(\grmod S)^\op\to\grmod(S^\op),\\
\beta:{}^{\grstar}(-)&\xrightarrow{\sim}\bbD
&&\text{as functors }(\grmod(S^\op))^\op\to\grmod S.
\end{aligned}
\]
\begin{advanced}
On locally finite graded $S$-bimodules, there are natural isomorphisms of functors $(\grmod S^\en)^\op\to\grmod S^\en$:
\[
(-)^{\grstar[_{\en}]}
\xrightarrow[\gamma]{\sim}(-)^{\grstar}
\xrightarrow[\alpha]{\sim}\bbD
\xleftarrow[\beta]{\sim}{}^{\grstar}(-).
\]
\end{advanced}
\end{corollary}

\begin{proof}
For a locally finite graded module $M$, $\alpha_M$ and $\beta_M$ are the direct sums over $i\in\Z$ of the corresponding maps on $M_{-i}$ in Proposition~\ref{prop:dual-comparison}.
They are isomorphisms of degree $0$; naturality follows by applying the natural isomorphisms \eqref{eq:dual-comparison-functors} in each degree.
\begin{advanced}
For a locally finite graded bimodule $M$, take the direct sum of the maps $\gamma_{M_{-i}}$ from \eqref{eq:en-dual-comparison}.
The same degreewise argument proves that $\gamma_M$ is an isomorphism of graded bimodules and is natural in $M$.
\end{advanced}
\end{proof}

For a graded algebra $A$ with $S=A_0$, Corollary~\ref{cor:graded-dual-comparison} transports the $A$-action \eqref{eq:linear-dual-actions} to the graded $S$-duals of a locally finite graded $A$-module:
\[
af=\alpha_M^{-1}(a\alpha_M(f))\quad\text{for right }M,
\qquad
ga=\beta_M^{-1}(\beta_M(g)a)\quad\text{for left }M.
\]
Here $\alpha_M(f)=\tau\circ f$ and $\beta_M(g)=\tau\circ g$ are the restrictions of \eqref{eq:dual-comparison}; $a\in A$, $f\in M^{\grstar}$, and $g\in{}^{\grstar}M$.
The restrictions to $S$ agree with Definition~\ref{def:S-duals}.
These remain duals over $S$, not duals taking values in $A$.
The graded $S$-duals are defined without $\tau$, but these transported $A$-actions depend on $\tau$. The canonical graded $A$-module is $\bbD(M)$.

\begin{exercise}[Dependence of the action on the form]\label{ex:transported-dual-action}
In this exercise take $\Bbbk=\mathbb Q$.
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

\begin{hidden}
\begin{proof}[Solution]
\emph{The form and the basis.}
The algebra $S$ is commutative, so $\tau(st)=\tau(ts)$.
If $s=ae_{11}+be_{22}$ satisfies $\tau(se_{11})=\tau(se_{22})=0$, then $c_1a=c_2b=0$, hence $s=0$.
Thus $\tau$ is non-degenerate.

A right $S$-linear map $f:M\to S$ must satisfy $f(e_{11})\in Se_{11}=\Bbbk e_{11}$ and $f(e_{12})\in Se_{22}=\Bbbk e_{22}$.
Conversely, any choices of these two values define such a map.
Consequently, $\varphi_0,\varphi_1$ form a basis, with degrees $0,-1$, respectively.

\emph{The actions.}
For the general form \eqref{eq:transported-dual-form}, write $\alpha_M(f)=\tau\circ f$.
For $m=ae_{11}+be_{12}$,
\[
\alpha_M(\varphi_0)(m)=c_1a,\qquad
\alpha_M(\varphi_1)(m)=c_2b,\qquad
\alpha_M(e_{12}\cdot\varphi_1)(m)
=\alpha_M(\varphi_1)(me_{12})=c_2a.
\]
Using also $me_{11}=ae_{11}$ and $me_{22}=be_{12}$ gives all non-zero actions:
\[
e_{11}\cdot\varphi_0=\varphi_0,\qquad
e_{22}\cdot\varphi_1=\varphi_1,\qquad
e_{12}\cdot\varphi_1=\frac{c_2}{c_1}\varphi_0.
\]
All other actions of the three matrix units on the two basis vectors are zero.
Thus $e_{12}\cdot_1\varphi_1=\varphi_0$ whereas $e_{12}\cdot_2\varphi_1=2\varphi_0$, so the actions are not equal.

\emph{The isomorphism.}
Define
\[
t:(M^{\grstar},\cdot_1)\longrightarrow(M^{\grstar},\cdot_2),
\qquad
t(\varphi_0)=\varphi_0,\quad t(\varphi_1)=\tfrac12\varphi_1.
\]
The map is invertible, preserves degrees, and commutes with the actions of $e_{11}$ and $e_{22}$.
For the remaining matrix unit,
\[
t(e_{12}\cdot_1\varphi_1)=t(\varphi_0)=\varphi_0
=e_{12}\cdot_2(\tfrac12\varphi_1)
=e_{12}\cdot_2t(\varphi_1).
\]
Both sides vanish on $\varphi_0$.
Since the three matrix units span $A$, the map $t$ is $A$-linear.
\end{proof}
\end{hidden}

\begin{example}\label{ex:dual-blocks}
We compute how duality transposes bimodule blocks and how one linear functional gives different left and right $S$-linear maps.
Let $S=\Bbbk^{\oplus r}$ with coordinate idempotents $e_1,\ldots,e_r$ and $\tau(e_i)=1$.
Thus $1=\sum_i e_i$ and $e_ie_j=\delta_{ij}e_i$; in the diagonal matrix realisation, $e_i=e_{ii}$.
For an $S$-bimodule $M$, write its elements in blocks:
\[
M\cong
\begin{pmatrix}
e_1Me_1&\cdots&e_1Me_r\\
\vdots&\ddots&\vdots\\
e_rMe_1&\cdots&e_rMe_r
\end{pmatrix},
\qquad m\longmapsto(e_i m e_j)_{i,j}.
\]
The block matrix denotes the direct sum of its entries; its inverse sends $(m_{ij})_{i,j}$ to $\sum_{i,j}m_{ij}$.
The action $(s\lambda t)(m)=\lambda(tms)$ from \eqref{eq:bimodule-dual-actions} reverses the blocks:
\[
D(M)\cong
\begin{pmatrix}
D(e_1Me_1)&\cdots&D(e_rMe_1)\\
\vdots&\ddots&\vdots\\
D(e_1Me_r)&\cdots&D(e_rMe_r)
\end{pmatrix},
\qquad
e_jD(M)e_i\cong D(e_iMe_j).
\]
The last isomorphism restricts a functional to $e_iMe_j$; its inverse extends that functional by zero on the other blocks.

For $V=(\Bbbk A_2)_1=\Bbbk e_{12}$, the block positions are
\[
V=
\begin{pmatrix}0&\Bbbk\\0&0\end{pmatrix},
\qquad
D(V)\cong
\begin{pmatrix}0&0\\\Bbbk&0\end{pmatrix}.
\]
Let $\varepsilon\in D(V)$ satisfy $\varepsilon(e_{12})=1$.
Then $e_2\varepsilon e_1=\varepsilon$, and $\varepsilon$ has degree $-1$ in $\bbD(V)$.
Under \eqref{eq:dual-comparison}, the corresponding right and left $S$-linear maps are
\[
\alpha_V^{-1}(\varepsilon):V\to S,\quad e_{12}\mapsto e_2,
\qquad
\beta_V^{-1}(\varepsilon):V\to S,\quad e_{12}\mapsto e_1.
\]
As $\Bbbk$-linear maps $V\to S$,
\[
\alpha_V^{-1}(\varepsilon)\neq\beta_V^{-1}(\varepsilon),
\qquad
\tau\circ\alpha_V^{-1}(\varepsilon)
=\varepsilon
=\tau\circ\beta_V^{-1}(\varepsilon).
\]
\end{example}

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
For $S$-bimodules, the coevaluation maps preserve both actions.
No symmetrising form is required.
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
For a bimodule $M$, \eqref{eq:bimodule-dual-actions} gives
\[
(s\,\mathrm{coev}_M(m)\,t)(f)=f(sm)t=f(smt)=\mathrm{coev}_M(smt)(f)
\quad(s,t\in S,\ m\in M,\ f\in M^*),
\]
which proves bimodule compatibility.
\end{proof}

\subsection{Exercises}

\begin{exercise}[Categories and shifts]
Let $A=\Bbbk A_2$ with the grading of Example~\ref{ex:triangular-grading}.
Show that $e_{11}A$ and $(e_{11}A)(1)$ are isomorphic in $\Mod A$ but not in $\Grmod A$.
\emph{Hint.} Compare their degree $1$ components. Explain why this does not contradict the fact that the shift functor is an equivalence.
\end{exercise}

\begin{exercise}[Matrix calculations]
Verify the grading on $\Bbbk A_n$ in Example~\ref{ex:triangular-grading} using $e_{ij}e_{pq}=\delta_{jp}e_{iq}$.
Compute $\rad(\Bbbk A_3)$ from the definition.
\emph{Hint.} The strictly upper triangular ideal $J$ satisfies $J^3=0$. Apply the argument of Example~\ref{ex:semisimple-algebras} to simple modules and to $A/J\cong\Bbbk^{\oplus3}$.
\end{exercise}

\begin{exercise}[Shifts and duals]
For $A=\Bbbk A_3$, compute the degrees and all non-zero matrix-unit actions on $\bbD(e_{22}A)$.
Show that it is not isomorphic to any left module $Ae_{jj}$, even after a shift.
\emph{Hint.} Compare dimensions and the actions of $e_{11},e_{22},e_{33}$.
\end{exercise}

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
<summary><strong>Approved replacement: full exact Sections 1.11-1.13 after reorganisation</strong></summary>

```tex
\subsection{\texorpdfstring{Left, right, and two-sided duals over $S$}{Left, right, and two-sided duals over S}}

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
M^{\grstar}:=\bigoplus_{i\in\Z}(M_{-i})^*,\qquad
{}^{\grstar}M:=\bigoplus_{i\in\Z}{}^*(M_{-i}),
\]
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

\subsection{Comparing the duals}

To identify $S$-dual with $\Bbbk$-dual, we need a suitable linear functional $S\to\Bbbk$.

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

\begin{theorem}[Comparison of duals]\label{prop:dual-comparison}\label{cor:graded-dual-comparison}
Choose a symmetrising form $\tau:S\to\Bbbk$.
The right and left $S$-dual functors are naturally isomorphic to the corresponding $\Bbbk$-linear dual functors, both without grading and with grading.

\emph{Ungraded duals.}
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

\emph{Graded duals.}
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

\begin{proof}
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

\begin{example}\label{ex:dual-blocks}
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
Requiring $\tau\circ f=\varepsilon$ therefore forces $f(e_{12})=e_2$.
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
The theorem compares the different dual constructions separately in the ungraded and graded settings; it does not identify $D(M)$ with $\bbD(M)$ for an arbitrary infinite-dimensional graded module.
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

\subsection{Exercises}

\begin{exercise}[Categories and shifts]
Let $A=\Bbbk A_2$ with the grading of Example~\ref{ex:triangular-grading}.
Show that $e_{11}A$ and $(e_{11}A)(1)$ are isomorphic in $\Mod A$ but not in $\Grmod A$.
\emph{Hint.} Compare their degree $1$ components. Explain why this does not contradict the fact that the shift functor is an equivalence.
\end{exercise}

\begin{exercise}[Matrix calculations]
Verify the grading on $\Bbbk A_n$ in Example~\ref{ex:triangular-grading} using $e_{ij}e_{pq}=\delta_{jp}e_{iq}$.
Compute $\rad(\Bbbk A_3)$ from the definition.
\emph{Hint.} The strictly upper triangular ideal $J$ satisfies $J^3=0$. Apply the argument of Example~\ref{ex:semisimple-algebras} to simple modules and to $A/J\cong\Bbbk^{\oplus3}$.
\end{exercise}

\begin{exercise}[Shifts and duals]
For $A=\Bbbk A_3$, compute the degrees and all non-zero matrix-unit actions on $\bbD(e_{22}A)$.
Show that it is not isomorphic to any left module $Ae_{jj}$, even after a shift.
\emph{Hint.} Compare dimensions and the actions of $e_{11},e_{22},e_{33}$.
\end{exercise}

\begin{exercise}[Homogeneous maps]
For the map $f$ in Example~\ref{ex:infinite-hom}, write every non-zero homogeneous component $f_d$ explicitly and prove that no finite sum equals $f$.
\end{exercise}

\begin{exercise}[Dependence on the form]
Repeat Example~\ref{ex:dual-blocks} with $\tau(e_i)=c_i\neq0$.
For $V=\Bbbk e_{12}$, find the right and left $S$-linear maps corresponding to the functional $\varepsilon(e_{12})=1$ under \eqref{eq:dual-comparison}.
\emph{Check.} Their values on $e_{12}$ are $c_2^{-1}e_2$ and $c_1^{-1}e_1$, respectively.
\end{exercise}

\begin{exercise}[Dependence of the action on the form]\label{ex:transported-dual-action}
In this exercise take $\Bbbk=\mathbb Q$.
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

\begin{hidden}
\begin{proof}[Solution]
\emph{The form and the basis.}
The algebra $S$ is commutative, so $\tau(st)=\tau(ts)$.
If $s=ae_{11}+be_{22}$ satisfies $\tau(se_{11})=\tau(se_{22})=0$, then $c_1a=c_2b=0$, hence $s=0$.
Thus $\tau$ is non-degenerate.

A right $S$-linear map $f:M\to S$ must satisfy $f(e_{11})\in Se_{11}=\Bbbk e_{11}$ and $f(e_{12})\in Se_{22}=\Bbbk e_{22}$.
Conversely, any choices of these two values define such a map.
Consequently, $\varphi_0,\varphi_1$ form a basis, with degrees $0,-1$, respectively.

\emph{The actions.}
For the general form \eqref{eq:transported-dual-form}, write $\alpha_M(f)=\tau\circ f$.
For $m=ae_{11}+be_{12}$,
\[
\alpha_M(\varphi_0)(m)=c_1a,\qquad
\alpha_M(\varphi_1)(m)=c_2b,\qquad
\alpha_M(e_{12}\cdot\varphi_1)(m)
=\alpha_M(\varphi_1)(me_{12})=c_2a.
\]
Using also $me_{11}=ae_{11}$ and $me_{22}=be_{12}$ gives all non-zero actions:
\[
e_{11}\cdot\varphi_0=\varphi_0,\qquad
e_{22}\cdot\varphi_1=\varphi_1,\qquad
e_{12}\cdot\varphi_1=\frac{c_2}{c_1}\varphi_0.
\]
All other actions of the three matrix units on the two basis vectors are zero.
Thus $e_{12}\cdot_1\varphi_1=\varphi_0$ whereas $e_{12}\cdot_2\varphi_1=2\varphi_0$, so the actions are not equal.

\emph{The isomorphism.}
Define
\[
t:(M^{\grstar},\cdot_1)\longrightarrow(M^{\grstar},\cdot_2),
\qquad
t(\varphi_0)=\varphi_0,\quad t(\varphi_1)=\tfrac12\varphi_1.
\]
The map is invertible, preserves degrees, and commutes with the actions of $e_{11}$ and $e_{22}$.
For the remaining matrix unit,
\[
t(e_{12}\cdot_1\varphi_1)=t(\varphi_0)=\varphi_0
=e_{12}\cdot_2(\tfrac12\varphi_1)
=e_{12}\cdot_2t(\varphi_1).
\]
Both sides vanish on $\varphi_0$.
Since the three matrix units span $A$, the map $t$ is $A$-linear.
\end{proof}
\end{hidden}
```

</details>

### Consequential Cross-References

**Original line 1740:**

```tex
Thus $\theta_{\en}$ is an isomorphism by Proposition~\ref{prop:dual-comparison}.
```

**Replacement:**

```tex
Thus $\theta_{\en}$ is an isomorphism by Theorem~\ref{prop:dual-comparison}.
```

**Original line 2172:**

```tex
Bijectivity of $\alpha_M,\beta_M$ in Proposition~\ref{prop:dual-comparison} proves \eqref{eq:orthogonal-comparison}.
```

**Replacement:**

```tex
Bijectivity of $\alpha_M,\beta_M$ in Theorem~\ref{prop:dual-comparison} proves \eqref{eq:orthogonal-comparison}.
```

**Original line 2339:**

```tex
Now use Proposition~\ref{prop:quadratic-basic}; the dimension statement follows from Proposition~\ref{prop:dual-comparison}.
```

**Replacement:**

```tex
Now use Proposition~\ref{prop:quadratic-basic}; the dimension statement follows from Theorem~\ref{prop:dual-comparison}.
```

### Application Checks

- [x] Reorganisation checked for definition-before-use dependencies.
- [x] All original commented-out lines retained in the same order.
- [x] The transported-action exercise and hidden solution retained verbatim.
- [x] All existing labels retained; the merged results share one theorem number.
- [x] Changes applied to the existing TeX file.
- [x] Built-in compilation and PDF export completed; the PDF in the course folder has 35 pages.
- [x] Affected PDF pages inspected and references checked; no undefined citations or references.

### Final Verification

- The combined comparison result is **Theorem 1.47**; the revised former Example 1.50 is now **Example 1.48**.
- The transported-action exercise is now **Exercise 1.55** in the exercises subsection.
- Pages 8, 11-17, and 35 were inspected. A proof-ending symbol was kept with the final proof paragraph using `\qedhere`; the integrated diff and exact replacement above include this layout adjustment.
- No new overflow warnings were introduced. One pre-existing 11.76479 pt overfull line remains in the unchanged paragraph at source lines 947-950.
- All original labels, commented-out lines, the preamble, and the hidden solution were preserved. The hidden-content switch was not changed or tested in an alternative state.
- The final TeX matches the recorded changes, and whitespace checks pass.
