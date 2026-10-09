# Lecture 2: Approved Revisions

> **Applied on 9 October 2026.** All nine replacements were approved and applied. The TeX and PDF are updated, with hidden material switched off.

**Approved modification to Replacement 8:** the solution uses `\begin{hidden} ... \end{hidden}` instead of `\iffalse ... \fi`. The preamble loads the `comment` package and provides `\showhiddenfalse`; change that line to `\showhiddentrue` to typeset all hidden contents. Put each environment delimiter on its own, unindented line. Both settings were compiled and checked.

**Record of the proposal:** the diffs and exact TeX quotations below retain the proposal as reviewed. The applied version differs only in the requested hidden environment and its preamble setup, plus a local `\emergencystretch=1em` in the new matrix example to prevent a line overflow; the mathematical text is unchanged.

**Prepared:** 9 October 2026  
**Source:** [2026_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex)

## Scope

| Item | Treatment |
| --- | --- |
| Lecture 2 | Address the four active comments and resolve the merge markers. |
| Your edits | Use the current source as the starting point. |
| Preamble | Add the switchable `hidden` environment. |
| Lecture 1 and Lecture 3 | Unchanged, including the new Lecture 1 comments. |
| Section 2.6 | Keep the whole section advanced and preserve its compact heading margin. |
| Proposed mathematical content | Unchanged by this Markdown reformatting. |

## Changes at a Glance

- **Hom, sums, and products:** add explicit formulas, the finite generation condition, and advanced caveats for infinite products.
- **Tensor-duality proof:** turn it into an exercise and retain the full solution in the switchable `hidden` environment requested at approval.
- **Canonical identifications:** specify the two tensor-dual maps, remove the main-text citation and merge markers, and put form-dependent comparisons in advanced blocks.
- **Examples:** introduce polynomial generators early, move symmetric and exterior algebras immediately after the tensor-algebra definition, and add an infinite-dimensional non-commutative example with two degree zero simple summands.

> **Standing preference for examples:** a representation-theoretic viewpoint does not exclude commutative examples. Include symmetric and exterior algebras when relevant, use simple finite-dimensional local examples sparingly, and include non-commutative examples with several degree zero simple summands.

## Replacement Index

| No. | Proposed Change | Line Changes | Review Together |
| --- | --- | --- | --- |
| **1** | [Hom formulas and the limitations for infinite products](#replacement-1-hom-formulas-and-the-limitations-for-infinite-products) | `+61` / `-1` | Independent |
| **2** | [State the canonical identifications precisely and resolve the merge conflict](#replacement-2-state-the-canonical-identifications-precisely-and-resolve-the-merge-conflict) | `+9` / `-52` | **8** |
| **3** | [Make the advanced linear-dual argument independent of the hidden proof](#replacement-3-make-the-advanced-linear-dual-argument-independent-of-the-hidden-proof) | `+2` / `-1` | Independent |
| **4** | [Balance the examples of generation in degree 1](#replacement-4-balance-the-examples-of-generation-in-degree-1) | `+22` / `-1` | Independent |
| **5** | [Introduce symmetric and exterior algebras as soon as tensor algebras are defined](#replacement-5-introduce-symmetric-and-exterior-algebras-as-soon-as-tensor-algebras-are-defined) | `+21` / `-0` | **6** |
| **6** | [Keep the later quadratic example concise](#replacement-6-keep-the-later-quadratic-example-concise) | `+2` / `-19` | **5** |
| **7** | [Put the form-dependent orthogonal comparison in an advanced block](#replacement-7-put-the-form-dependent-orthogonal-comparison-in-an-advanced-block) | `+2` / `-0` | Independent |
| **8** | [Turn the tensor-duality proof into an exercise with a hidden full solution](#replacement-8-turn-the-tensor-duality-proof-into-an-exercise-with-a-hidden-full-solution) | `+64` / `-0` | **2** |
| **9** | [Use the declared tensor-dual convention in the orthogonal example](#replacement-9-use-the-declared-tensor-dual-convention-in-the-orthogonal-example) | `+1` / `-1` | Independent |

## How to Review

Read the **line-by-line diff** first. Each changed line is marked explicitly; supporting Markdown readers also colour removals red and additions green.

| Marker | Meaning |
| --- | --- |
| `- old line` | **Remove** this line from the existing source. |
| `+ new line` | **Add** this line to the proposed source. |
| A leading space | **Keep** this line; it is shown only for context. |
| `@@ -old,count +new,count @@` | Source line numbers and the number of lines in each displayed block. |

The `--- existing/...` and `+++ proposed/...` lines identify the two versions; they are not changes to the TeX. Only nearby unchanged lines are shown. Proposed line numbers assume **all nine replacements** are applied.

**Full exact source remains available:** expand **Existing content** or **Proposed replacement** beneath any diff. Those `tex` blocks are unchanged, including their blank lines. Source locations refer to the file read on 9 October 2026.

> **Linked replacements:** review **2 and 8 together**, since they relocate the tensor-duality proof. Review **5 and 6 together**, since they relocate the classical examples.

### Checks Recorded During Preparation

- [x] Every existing passage occurs exactly once; the replacements do not overlap.
- [x] Lecture 1 and Lecture 3 are unchanged; only the requested hidden-environment setup changes the preamble.
- [x] All pre-existing commented-out content is preserved.
- [x] All four active Lecture 2 comments are addressed.
- [x] No merge markers remain in the proposed source.
- [x] New Lecture 2 cross-reference targets exist, with no duplicate labels.
- [x] Active Lecture 2 environments are balanced.
- [x] All remaining Lecture 2 citations are inside advanced blocks.
- [x] The tensor-duality proof is retained verbatim as a hidden solution.
- [x] Apply the approved replacements to the existing TeX.
- [x] Compile, inspect the changed layout, and save the updated PDF.
- [x] Test both hidden-content settings; leave `\showhiddenfalse` in the final source.

**Compilation completed.** The final PDF has 33 pages. There are no new Lecture 2 overflow warnings. Existing Lecture 1 warnings remain outside the approved scope: two references to the missing label `eq:dual-comparison-naturality`, and two small line overflows.

---

## Replacement 1: Hom formulas and the limitations for infinite products

**Source location:** [line 1352](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1352)  
**Purpose:** Add the missing Hom formulas with explicit maps and the correct finite generation hypothesis. Keep the counterexamples for infinite products in an advanced block.

### Line-by-Line Diff

**Added:** `+61` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1352,4 +1352,4 @@
-\]\comm{add also interaction of direct sum with Hom.  add remark about direct product interaction with Hom and tensor}
+\]
 \end{enumerate}
 \end{lemma}
 
@@ -1375,3 +1375,63 @@
 The same construction works in the other variable.
 \end{proof}
 
+\begin{lemma}[Hom, direct sums, and direct products]\label{lem:hom-sums-products}
+Let $M,N,M_i,N_i$ be right $S$-modules, with $i\in I$.
+Write $\iota_i:M_i\to\bigoplus_{j\in I}M_j$ for the inclusions and $\pi_i:\prod_{j\in I}N_j\to N_i$ for the projections.
+There are natural linear isomorphisms
+\[
+\begin{aligned}
+\Hom_S\Bigl(\bigoplus_iM_i,N\Bigr)&\xrightarrow{\sim}\prod_i\Hom_S(M_i,N),
+& f&\longmapsto(f\circ\iota_i)_i,\\
+\Hom_S\Bigl(M,\prod_iN_i\Bigr)&\xrightarrow{\sim}\prod_i\Hom_S(M,N_i),
+& f&\longmapsto(\pi_i\circ f)_i.
+\end{aligned}
+\]
+There is also a natural injection
+\[
+\bigoplus_i\Hom_S(M,N_i)\longrightarrow
+\Hom_S\Bigl(M,\bigoplus_iN_i\Bigr),
+\qquad (f_i)_i\longmapsto\bigl(m\mapsto(f_i(m))_i\bigr),
+\]
+which is an isomorphism when $M$ is finitely generated.
+\end{lemma}
+
+\begin{proof}
+The inverse of the first map sends $(f_i)_i$ to $(m_i)_i\mapsto\sum_i f_i(m_i)$; the sum is finite because $(m_i)_i$ has finite support.
+The inverse of the second sends $(f_i)_i$ to $m\mapsto(f_i(m))_i$; a direct product imposes no support condition.
+For the third map, coordinate projections recover each $f_i$, proving injectivity.
+If $m_1,\ldots,m_r$ generate $M$, the images of these generators under $f:M\to\bigoplus_iN_i$ are supported on a common finite subset $J\subset I$.
+Then $f(M)\subset\bigoplus_{i\in J}N_i$, so $f$ comes from a finite family of maps.
+All three constructions commute with precomposition and postcomposition.
+\end{proof}
+
+\begin{advanced}
+\begin{remark}\label{rem:infinite-products}
+For infinite families, $\Hom$ need not preserve direct sums in its second variable, and tensor product need not preserve direct products.
+
+For $M=\bigoplus_{i\geq1}\Bbbk v_i$, the identity $M\to M$ does not come from $\bigoplus_i\Hom_\Bbbk(M,\Bbbk v_i)$: its projection onto every $\Bbbk v_i$ is non-zero.
+Thus the injection in Lemma~\ref{lem:hom-sums-products} need not be surjective.
+
+For right $S$-modules $M_i$ and a left $S$-module $N$, the coordinate projections give a natural map
+\[
+\Bigl(\prod_iM_i\Bigr)\otimes_S N
+\longrightarrow\prod_i(M_i\otimes_S N),
+\qquad (m_i)_i\otimes n\longmapsto(m_i\otimes n)_i,
+\]
+but not always an isomorphism.
+For vector spaces, take $M_i=\Bbbk$ for $i\geq1$ and $N=\bigoplus_{j\geq1}\Bbbk v_j$.
+Every element in the image is a sequence whose entries lie in a common finite-dimensional subspace of $N$: a tensor is a finite sum $\sum_{\ell=1}^r(c_i^{(\ell)})_i\otimes n_\ell$, whose $i$th entry is $\sum_{\ell=1}^r c_i^{(\ell)}n_\ell$.
+The sequence $(v_i)_i\in\prod_iN$ is therefore not in the image.
+
+If $N$ is a direct summand of $S^{\oplus r}$ as a left module for some finite $r$, the tensor comparison is an isomorphism.
+For $N=S$, both sides are $\prod_iM_i$ under $m\otimes s\mapsto ms$; finite direct sums and direct summands preserve this conclusion.
+In particular, Corollary~\ref{cor:semisimple-summands} applies when $S$ is finite-dimensional semisimple and $N$ is finite-dimensional.
+
+A product in the source of $\Hom$ behaves differently from a product in the target.
+For example, a linear map $\prod_{i\geq1}\Bbbk\to\Bbbk$ need not be determined by its restrictions to the coordinate copies of $\Bbbk$.
+Indeed, $(1,1,\ldots)\notin\bigoplus_{i\geq1}\Bbbk$.
+Define a functional on $\bigoplus_{i\geq1}\Bbbk+\Bbbk(1,1,\ldots)$ to vanish on the direct sum and take value $1$ at $(1,1,\ldots)$, and extend it to the product by extending a basis.
+The resulting non-zero functional vanishes on every coordinate copy.
+\end{remark}
+\end{advanced}
+
```

<details>
<summary><strong>Existing content: full exact TeX before the change</strong></summary>

```tex
\]\comm{add also interaction of direct sum with Hom.  add remark about direct product interaction with Hom and tensor}
\end{enumerate}
\end{lemma}

\begin{proof}
For (1), Definition~\ref{def:vector-tensor} gives a unique linear map $M\otimes_\Bbbk N\to W$ sending $m\otimes n$ to $b(m,n)$.
It descends to the quotient precisely when $b(ms,n)-b(m,sn)=0$.
Uniqueness follows because the elements $m\otimes_S n$ span the quotient.

For (2), the outer actions preserve the defining relations: for $a,s,t\in S$,
\[
s(ma\otimes n-m\otimes an)t
=(sm)a\otimes nt-sm\otimes a(nt).
\]
The module axioms follow from those on $M,N$.
In (3), both parenthesisations impose the relations that move an element of $S$ between adjacent factors, so the displayed associativity map and its reverse are well-defined.
Their composites fix every $(u\otimes v)\otimes w$ and $u\otimes(v\otimes w)$.
The unit inverses are $V\to S\otimes_S V$, $v\mapsto1\otimes v$, and $V\to V\otimes_S S$, $v\mapsto v\otimes1$; the tensor relations give the required identities.

For (4), the displayed map has finite support because $(m_i)_i$ does.
It is well-defined by (1).
If $\iota_i:M_i\to\bigoplus_{j\in I}M_j$ is the canonical inclusion, the inverse sends $m\otimes n$ in the $i$th summand to $\iota_i(m)\otimes n$ and extends linearly over the direct sum.
Both composites fix the displayed generators.
The same construction works in the other variable.
\end{proof}

```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX after the change</strong></summary>

```tex
\]
\end{enumerate}
\end{lemma}

\begin{proof}
For (1), Definition~\ref{def:vector-tensor} gives a unique linear map $M\otimes_\Bbbk N\to W$ sending $m\otimes n$ to $b(m,n)$.
It descends to the quotient precisely when $b(ms,n)-b(m,sn)=0$.
Uniqueness follows because the elements $m\otimes_S n$ span the quotient.

For (2), the outer actions preserve the defining relations: for $a,s,t\in S$,
\[
s(ma\otimes n-m\otimes an)t
=(sm)a\otimes nt-sm\otimes a(nt).
\]
The module axioms follow from those on $M,N$.
In (3), both parenthesisations impose the relations that move an element of $S$ between adjacent factors, so the displayed associativity map and its reverse are well-defined.
Their composites fix every $(u\otimes v)\otimes w$ and $u\otimes(v\otimes w)$.
The unit inverses are $V\to S\otimes_S V$, $v\mapsto1\otimes v$, and $V\to V\otimes_S S$, $v\mapsto v\otimes1$; the tensor relations give the required identities.

For (4), the displayed map has finite support because $(m_i)_i$ does.
It is well-defined by (1).
If $\iota_i:M_i\to\bigoplus_{j\in I}M_j$ is the canonical inclusion, the inverse sends $m\otimes n$ in the $i$th summand to $\iota_i(m)\otimes n$ and extends linearly over the direct sum.
Both composites fix the displayed generators.
The same construction works in the other variable.
\end{proof}

\begin{lemma}[Hom, direct sums, and direct products]\label{lem:hom-sums-products}
Let $M,N,M_i,N_i$ be right $S$-modules, with $i\in I$.
Write $\iota_i:M_i\to\bigoplus_{j\in I}M_j$ for the inclusions and $\pi_i:\prod_{j\in I}N_j\to N_i$ for the projections.
There are natural linear isomorphisms
\[
\begin{aligned}
\Hom_S\Bigl(\bigoplus_iM_i,N\Bigr)&\xrightarrow{\sim}\prod_i\Hom_S(M_i,N),
& f&\longmapsto(f\circ\iota_i)_i,\\
\Hom_S\Bigl(M,\prod_iN_i\Bigr)&\xrightarrow{\sim}\prod_i\Hom_S(M,N_i),
& f&\longmapsto(\pi_i\circ f)_i.
\end{aligned}
\]
There is also a natural injection
\[
\bigoplus_i\Hom_S(M,N_i)\longrightarrow
\Hom_S\Bigl(M,\bigoplus_iN_i\Bigr),
\qquad (f_i)_i\longmapsto\bigl(m\mapsto(f_i(m))_i\bigr),
\]
which is an isomorphism when $M$ is finitely generated.
\end{lemma}

\begin{proof}
The inverse of the first map sends $(f_i)_i$ to $(m_i)_i\mapsto\sum_i f_i(m_i)$; the sum is finite because $(m_i)_i$ has finite support.
The inverse of the second sends $(f_i)_i$ to $m\mapsto(f_i(m))_i$; a direct product imposes no support condition.
For the third map, coordinate projections recover each $f_i$, proving injectivity.
If $m_1,\ldots,m_r$ generate $M$, the images of these generators under $f:M\to\bigoplus_iN_i$ are supported on a common finite subset $J\subset I$.
Then $f(M)\subset\bigoplus_{i\in J}N_i$, so $f$ comes from a finite family of maps.
All three constructions commute with precomposition and postcomposition.
\end{proof}

\begin{advanced}
\begin{remark}\label{rem:infinite-products}
For infinite families, $\Hom$ need not preserve direct sums in its second variable, and tensor product need not preserve direct products.

For $M=\bigoplus_{i\geq1}\Bbbk v_i$, the identity $M\to M$ does not come from $\bigoplus_i\Hom_\Bbbk(M,\Bbbk v_i)$: its projection onto every $\Bbbk v_i$ is non-zero.
Thus the injection in Lemma~\ref{lem:hom-sums-products} need not be surjective.

For right $S$-modules $M_i$ and a left $S$-module $N$, the coordinate projections give a natural map
\[
\Bigl(\prod_iM_i\Bigr)\otimes_S N
\longrightarrow\prod_i(M_i\otimes_S N),
\qquad (m_i)_i\otimes n\longmapsto(m_i\otimes n)_i,
\]
but not always an isomorphism.
For vector spaces, take $M_i=\Bbbk$ for $i\geq1$ and $N=\bigoplus_{j\geq1}\Bbbk v_j$.
Every element in the image is a sequence whose entries lie in a common finite-dimensional subspace of $N$: a tensor is a finite sum $\sum_{\ell=1}^r(c_i^{(\ell)})_i\otimes n_\ell$, whose $i$th entry is $\sum_{\ell=1}^r c_i^{(\ell)}n_\ell$.
The sequence $(v_i)_i\in\prod_iN$ is therefore not in the image.

If $N$ is a direct summand of $S^{\oplus r}$ as a left module for some finite $r$, the tensor comparison is an isomorphism.
For $N=S$, both sides are $\prod_iM_i$ under $m\otimes s\mapsto ms$; finite direct sums and direct summands preserve this conclusion.
In particular, Corollary~\ref{cor:semisimple-summands} applies when $S$ is finite-dimensional semisimple and $N$ is finite-dimensional.

A product in the source of $\Hom$ behaves differently from a product in the target.
For example, a linear map $\prod_{i\geq1}\Bbbk\to\Bbbk$ need not be determined by its restrictions to the coordinate copies of $\Bbbk$.
Indeed, $(1,1,\ldots)\notin\bigoplus_{i\geq1}\Bbbk$.
Define a functional on $\bigoplus_{i\geq1}\Bbbk+\Bbbk(1,1,\ldots)$ to vanish on the direct sum and take value $1$ at $(1,1,\ldots)$, and extend it to the product by extending a basis.
The resulting non-zero functional vanishes on every coordinate copy.
\end{remark}
\end{advanced}

```

</details>

[Back to the replacement index](#replacement-index)

---

## Replacement 2: State the canonical identifications precisely and resolve the merge conflict

**Source location:** [line 1417](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1417)  
**Purpose:** Explain exactly which tensor-dual spaces are identified, distinguish those maps from form-dependent comparisons between different duals, and remove the citation and merge markers.

> **Review together with [Replacement 8](#replacement-8-turn-the-tensor-duality-proof-into-an-exercise-with-a-hidden-full-solution).**

### Line-by-Line Diff

**Added:** `+9` lines &nbsp; **Removed:** `-52` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1417,6 +1477,7 @@
 Tensor duality reverses the order of the factors.
+The following maps use only the $S$-module actions; no basis or symmetrising form is chosen.
 
-\begin{proposition}\label{prop:tensor-duals}
+\begin{proposition}[Tensor duality]\label{prop:tensor-duals}
 Let $S$ be finite-dimensional semisimple and let $V,W$ be finite-dimensional $S$-bimodules.
 There are bimodule isomorphisms, natural in $V,W$,
 \begin{equation}\label{eq:tensor-duals}
@@ -1433,56 +1494,12 @@
 \end{equation}
 \end{proposition}
 
-\comm{hide proof and make proof an exercise }
-\begin{proof}
-\emph{Well-definedness.}
-For the right duals, right $S$-linearity gives
-\[
-g(f(vs)w)=g(f(v)sw),\qquad
-(gs)(f(v)w)=g(sf(v)w)=g((sf)(v)w).
-\]
-The first identity respects the relation in $V\otimes_S W$, and the second respects the relation in $W^*\otimes_S V^*$.
-The resulting functional is right $S$-linear because $g$ is.
-For the left duals, the corresponding identities are
-\[
-f(vs\,g(w))=f(vg(sw)),\qquad
-f(v(gs)(w))=f(vg(w)s)=(sf)(vg(w)).
-\]
-Left $S$-linearity of $f$ makes the resulting functional left $S$-linear.
-The outer actions in \eqref{eq:tensor-dual-actions} give
-\[
-\begin{aligned}
-\theta_r(sg\otimes ft)(v\otimes w)&=s\,g(f(tv)w),\\
-\theta_\ell(sg\otimes ft)(v\otimes w)&=f(vg(ws))t,
-\end{aligned}
-\]
-which are the required bimodule identities.
+\begin{convention}[Tensor duals]
+For $S,V,W$ as in Proposition~\ref{prop:tensor-duals}, we use $\theta_r$ and $\theta_\ell$ in \eqref{eq:tensor-duals} to identify the dual of a tensor product with the tensor product of the corresponding duals in reverse order.
+The values of these functionals are always given by \eqref{eq:tensor-evaluations}.
+These are the canonical identifications used below; they do not identify $M^*$, $ {}^*M$, and $D(M)$ with one another.
+Comparisons with $D(M)$ use a chosen symmetrising form, as in \eqref{eq:dual-comparison}.
+\end{convention}
 
-\emph{Bijectivity.}
-To check $\theta_r$, forget the left action on $V$.
-For $V=S$, identify $S^*\cong S$ by $f\mapsto f(1)$; then $\theta_r$ is $W^*\otimes_S S\to W^*$, $g\otimes s\mapsto gs$, an isomorphism by Lemma~\ref{lem:tensor-properties}(3).
-The formula commutes with maps of right $S$-modules in $V$, so it is an isomorphism for finite direct sums and direct summands of $S$.
-Corollary~\ref{cor:semisimple-summands} applies to $V$.
-For $\theta_\ell$, use $W=S$ as a left module, where the map is $S\otimes_S{}^*V\to{}^*V$, $s\otimes f\mapsto sf$, and apply the same argument to $W$.
+The proof of Proposition~\ref{prop:tensor-duals} is Exercise~\ref{ex:tensor-duality-proof}.
 
-\emph{Naturality.}
-For bimodule maps $p:V\to V'$ and $q:W\to W'$, the square
-\[
-\xymatrix@C=48pt@R=22pt{
-(W')^*\otimes_S(V')^* \ar[r]^{\theta_r} \ar[d]_{q^*\otimes p^*}
-& (V'\otimes_S W')^* \ar[d]^{(p\otimes q)^*}\\
-W^*\otimes_S V^* \ar[r]_{\theta_r}
-& (V\otimes_S W)^*
-}
-\]
-commutes: both routes send $g\otimes f$, evaluated at $v\otimes w$, to $g(f(p(v))q(w))$.
-For $\theta_\ell$, the corresponding two routes give $f(p(v)g(q(w)))$.
-\end{proof}
-
-Neither map in \eqref{eq:tensor-duals} requires a symmetrising form.
-<<<<<<< HEAD
-These canonical identifications are the reason for using $S$-duals in tensor calculations; see \cite[\S2.7]{BGS96}. \comm{no citation!!! in fact, the statement here is imprecise.  what is the canonical identification you are talk about.  if there is something we can identified cananoically and used throughout, then it should be highlighted much more properly, much earlier.  what's the point of doing all the dual isomorphisms if there are cananoical identification????  if there is something canonical we can use, then exposition should be significantly shorten by using it; any pedantic detail drilling using non-canonical thing should be put as advanced material}
-=======
-These canonical identifications are the reason for using $S$-duals in tensor calculations.
->>>>>>> aa2be17dc4763fa87fbf1499d88d20b770595b0d
-
```

<details>
<summary><strong>Existing content: full exact TeX before the change</strong></summary>

```tex
Tensor duality reverses the order of the factors.

\begin{proposition}\label{prop:tensor-duals}
Let $S$ be finite-dimensional semisimple and let $V,W$ be finite-dimensional $S$-bimodules.
There are bimodule isomorphisms, natural in $V,W$,
\begin{equation}\label{eq:tensor-duals}
\begin{aligned}
\theta_r &: W^*\otimes_S V^*\xrightarrow{\sim}(V\otimes_S W)^*,\\
\theta_\ell &: {}^*W\otimes_S {}^*V\xrightarrow{\sim}{}^*(V\otimes_S W),
\end{aligned}
\end{equation}
defined by
\begin{equation}\label{eq:tensor-evaluations}
\theta_r(g\otimes f)(v\otimes w)=g(f(v)w),
\qquad
\theta_\ell(g\otimes f)(v\otimes w)=f(vg(w)).
\end{equation}
\end{proposition}

\comm{hide proof and make proof an exercise }
\begin{proof}
\emph{Well-definedness.}
For the right duals, right $S$-linearity gives
\[
g(f(vs)w)=g(f(v)sw),\qquad
(gs)(f(v)w)=g(sf(v)w)=g((sf)(v)w).
\]
The first identity respects the relation in $V\otimes_S W$, and the second respects the relation in $W^*\otimes_S V^*$.
The resulting functional is right $S$-linear because $g$ is.
For the left duals, the corresponding identities are
\[
f(vs\,g(w))=f(vg(sw)),\qquad
f(v(gs)(w))=f(vg(w)s)=(sf)(vg(w)).
\]
Left $S$-linearity of $f$ makes the resulting functional left $S$-linear.
The outer actions in \eqref{eq:tensor-dual-actions} give
\[
\begin{aligned}
\theta_r(sg\otimes ft)(v\otimes w)&=s\,g(f(tv)w),\\
\theta_\ell(sg\otimes ft)(v\otimes w)&=f(vg(ws))t,
\end{aligned}
\]
which are the required bimodule identities.

\emph{Bijectivity.}
To check $\theta_r$, forget the left action on $V$.
For $V=S$, identify $S^*\cong S$ by $f\mapsto f(1)$; then $\theta_r$ is $W^*\otimes_S S\to W^*$, $g\otimes s\mapsto gs$, an isomorphism by Lemma~\ref{lem:tensor-properties}(3).
The formula commutes with maps of right $S$-modules in $V$, so it is an isomorphism for finite direct sums and direct summands of $S$.
Corollary~\ref{cor:semisimple-summands} applies to $V$.
For $\theta_\ell$, use $W=S$ as a left module, where the map is $S\otimes_S{}^*V\to{}^*V$, $s\otimes f\mapsto sf$, and apply the same argument to $W$.

\emph{Naturality.}
For bimodule maps $p:V\to V'$ and $q:W\to W'$, the square
\[
\xymatrix@C=48pt@R=22pt{
(W')^*\otimes_S(V')^* \ar[r]^{\theta_r} \ar[d]_{q^*\otimes p^*}
& (V'\otimes_S W')^* \ar[d]^{(p\otimes q)^*}\\
W^*\otimes_S V^* \ar[r]_{\theta_r}
& (V\otimes_S W)^*
}
\]
commutes: both routes send $g\otimes f$, evaluated at $v\otimes w$, to $g(f(p(v))q(w))$.
For $\theta_\ell$, the corresponding two routes give $f(p(v)g(q(w)))$.
\end{proof}

Neither map in \eqref{eq:tensor-duals} requires a symmetrising form.
<<<<<<< HEAD
These canonical identifications are the reason for using $S$-duals in tensor calculations; see \cite[\S2.7]{BGS96}. \comm{no citation!!! in fact, the statement here is imprecise.  what is the canonical identification you are talk about.  if there is something we can identified cananoically and used throughout, then it should be highlighted much more properly, much earlier.  what's the point of doing all the dual isomorphisms if there are cananoical identification????  if there is something canonical we can use, then exposition should be significantly shorten by using it; any pedantic detail drilling using non-canonical thing should be put as advanced material}
=======
These canonical identifications are the reason for using $S$-duals in tensor calculations.
>>>>>>> aa2be17dc4763fa87fbf1499d88d20b770595b0d

```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX after the change</strong></summary>

```tex
Tensor duality reverses the order of the factors.
The following maps use only the $S$-module actions; no basis or symmetrising form is chosen.

\begin{proposition}[Tensor duality]\label{prop:tensor-duals}
Let $S$ be finite-dimensional semisimple and let $V,W$ be finite-dimensional $S$-bimodules.
There are bimodule isomorphisms, natural in $V,W$,
\begin{equation}\label{eq:tensor-duals}
\begin{aligned}
\theta_r &: W^*\otimes_S V^*\xrightarrow{\sim}(V\otimes_S W)^*,\\
\theta_\ell &: {}^*W\otimes_S {}^*V\xrightarrow{\sim}{}^*(V\otimes_S W),
\end{aligned}
\end{equation}
defined by
\begin{equation}\label{eq:tensor-evaluations}
\theta_r(g\otimes f)(v\otimes w)=g(f(v)w),
\qquad
\theta_\ell(g\otimes f)(v\otimes w)=f(vg(w)).
\end{equation}
\end{proposition}

\begin{convention}[Tensor duals]
For $S,V,W$ as in Proposition~\ref{prop:tensor-duals}, we use $\theta_r$ and $\theta_\ell$ in \eqref{eq:tensor-duals} to identify the dual of a tensor product with the tensor product of the corresponding duals in reverse order.
The values of these functionals are always given by \eqref{eq:tensor-evaluations}.
These are the canonical identifications used below; they do not identify $M^*$, $ {}^*M$, and $D(M)$ with one another.
Comparisons with $D(M)$ use a chosen symmetrising form, as in \eqref{eq:dual-comparison}.
\end{convention}

The proof of Proposition~\ref{prop:tensor-duals} is Exercise~\ref{ex:tensor-duality-proof}.

```

</details>

[Back to the replacement index](#replacement-index)

---

## Replacement 3: Make the advanced linear-dual argument independent of the hidden proof

**Source location:** [line 1499](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1499)  
**Purpose:** Keep the advanced argument complete after moving the main tensor-duality proof into a hidden exercise solution.

### Line-by-Line Diff

**Added:** `+2` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1499 +1516,2 @@
-For $V=S$, the map is $D(W)\otimes_S S\to D(W)$, $\lambda\otimes s\mapsto\lambda s$; the direct summand argument in Proposition~\ref{prop:tensor-duals} proves bijectivity.
+For $V=S$, the map is the isomorphism $D(W)\otimes_S S\to D(W)$, $\lambda\otimes s\mapsto\lambda s$.
+The formula commutes with right $S$-module maps in $V$, so finite direct sums and direct summands preserve bijectivity; Corollary~\ref{cor:semisimple-summands} applies to $V$.
```

<details>
<summary><strong>Existing content: full exact TeX before the change</strong></summary>

```tex
For $V=S$, the map is $D(W)\otimes_S S\to D(W)$, $\lambda\otimes s\mapsto\lambda s$; the direct summand argument in Proposition~\ref{prop:tensor-duals} proves bijectivity.
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX after the change</strong></summary>

```tex
For $V=S$, the map is the isomorphism $D(W)\otimes_S S\to D(W)$, $\lambda\otimes s\mapsto\lambda s$.
The formula commutes with right $S$-module maps in $V$, so finite direct sums and direct summands preserve bijectivity; Corollary~\ref{cor:semisimple-summands} applies to $V$.
```

</details>

[Back to the replacement index](#replacement-index)

---

## Replacement 4: Balance the examples of generation in degree 1

**Source location:** [line 1572](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1572)  
**Purpose:** Include polynomial algebras alongside an infinite-dimensional, non-commutative example whose degree zero algebra has two simple summands.

### Line-by-Line Diff

**Added:** `+22` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1572 +1590,22 @@
-\comm{we avoid leaning towards commutative algebras, but it does not mean that we should remove them.  it is unnatural to not give symmetric algebra and exterior algebra as examples.  remember this for all future lecture notes preparation.  we should give sporadic local finite-dimensional algebra examples because they are easy to descibe but we should avoid using too much; the reader needs to be reminded there are many non-commutative algebra with multiple primitive idempotents}
+\begin{example}\label{ex:polynomial-generators}
+The polynomial algebra $\Bbbk[x_1,\ldots,x_n]$, with each $x_i$ in degree $1$, is generated in degree $1$ over $\Bbbk$.
+Indeed, every monomial of total degree $d$ is a product of $d$ variables, and these monomials span the degree $d$ component.
+\end{example}
+
+\begin{example}\label{ex:triangular-polynomials}
+Let $A$ be the algebra of upper triangular $2\times2$ matrices over $\Bbbk[x]$, graded by $\deg(x^m e_{ij})=m+j-i$ for $m\geq0$ and $1\leq i\leq j\leq2$.
+Then
+\[
+A_0=\Bbbk e_{11}\oplus\Bbbk e_{22},\qquad
+A_d=\Bbbk x^d e_{11}\oplus\Bbbk x^d e_{22}\oplus\Bbbk x^{d-1}e_{12}
+\quad(d\geq1).
+\]
+It is generated in degree $1$ over $A_0$, since
+\[
+x^d e_{11}=(xe_{11})^d,\qquad
+x^d e_{22}=(xe_{22})^d,\qquad
+x^{d-1}e_{12}=(xe_{11})^{d-1}e_{12}
+\quad(d\geq1).
+\]
+Here $A_0$ has two simple summands, $A_d\neq0$ for every $d\geq0$, and $A$ is non-commutative: $e_{11}e_{12}=e_{12}$ whereas $e_{12}e_{11}=0$.
+\end{example}
```

<details>
<summary><strong>Existing content: full exact TeX before the change</strong></summary>

```tex
\comm{we avoid leaning towards commutative algebras, but it does not mean that we should remove them.  it is unnatural to not give symmetric algebra and exterior algebra as examples.  remember this for all future lecture notes preparation.  we should give sporadic local finite-dimensional algebra examples because they are easy to descibe but we should avoid using too much; the reader needs to be reminded there are many non-commutative algebra with multiple primitive idempotents}
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX after the change</strong></summary>

```tex
\begin{example}\label{ex:polynomial-generators}
The polynomial algebra $\Bbbk[x_1,\ldots,x_n]$, with each $x_i$ in degree $1$, is generated in degree $1$ over $\Bbbk$.
Indeed, every monomial of total degree $d$ is a product of $d$ variables, and these monomials span the degree $d$ component.
\end{example}

\begin{example}\label{ex:triangular-polynomials}
Let $A$ be the algebra of upper triangular $2\times2$ matrices over $\Bbbk[x]$, graded by $\deg(x^m e_{ij})=m+j-i$ for $m\geq0$ and $1\leq i\leq j\leq2$.
Then
\[
A_0=\Bbbk e_{11}\oplus\Bbbk e_{22},\qquad
A_d=\Bbbk x^d e_{11}\oplus\Bbbk x^d e_{22}\oplus\Bbbk x^{d-1}e_{12}
\quad(d\geq1).
\]
It is generated in degree $1$ over $A_0$, since
\[
x^d e_{11}=(xe_{11})^d,\qquad
x^d e_{22}=(xe_{22})^d,\qquad
x^{d-1}e_{12}=(xe_{11})^{d-1}e_{12}
\quad(d\geq1).
\]
Here $A_0$ has two simple summands, $A_d\neq0$ for every $d\geq0$, and $A$ is non-commutative: $e_{11}e_{12}=e_{12}$ whereas $e_{12}e_{11}=0$.
\end{example}
```

</details>

[Back to the replacement index](#replacement-index)

---

## Replacement 5: Introduce symmetric and exterior algebras as soon as tensor algebras are defined

**Source location:** [line 1596](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1596)  
**Purpose:** Introduce the symmetric and exterior algebras at the earliest point where their tensor-algebra presentations can be defined without forward dependencies.

> **Review together with [Replacement 6](#replacement-6-keep-the-later-quadratic-example-concise).**

### Line-by-Line Diff

**Added:** `+21` lines &nbsp; **Removed:** `-0` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1596,2 +1635,23 @@
 Juxtaposition $v_1\cdots v_d$ in $T_S(V)$ denotes $v_1\otimes_S\cdots\otimes_S v_d$; in a specified quotient it denotes the image of that tensor.
 
+\begin{example}[Polynomial and exterior algebras]\label{ex:polynomial-exterior}
+Let $V$ be a finite-dimensional vector space with basis $x_1,\ldots,x_n$.
+The \defn{symmetric algebra} and \defn{exterior algebra} are
+\begin{equation}\label{eq:polynomial-exterior}
+\begin{aligned}
+\Symm(V)&=T_\Bbbk(V)/(x_ix_j-x_jx_i\mid i<j)
+            \cong\Bbbk[x_1,\ldots,x_n],\\
+\bigwedge V&=T_\Bbbk(V)/(v^2\mid v\in V).
+\end{aligned}
+\end{equation}
+Both algebras have degree $0$ component $\Bbbk$, degree $1$ component $V$, and are generated in degree $1$: their elements are linear combinations of products of the images of the $x_i$.
+The polynomial basis allows repetitions; the exterior basis consists of $1$ and $x_{i_1}\cdots x_{i_d}$ with $i_1<\cdots<i_d$.
+The exterior relations are equivalently $x_i^2=0$ for $1\leq i\leq n$ and $x_ix_j+x_jx_i=0$ for $i<j$, in every characteristic.
+\end{example}
+
+The bases in Example~\ref{ex:polynomial-exterior} can be checked directly.
+For $\Symm(V)$, commuting adjacent generators gives the ordered monomials, which are independent under the map to the polynomial ring.
+For $\bigwedge V$, the relations reduce every word to a multiple of a strictly increasing word or to zero.
+To prove independence in degree $d$, fix $i_1<\cdots<i_d$ and send $v_1\otimes\cdots\otimes v_d$ to the determinant of their coordinates in rows $i_1,\ldots,i_d$.
+This functional vanishes on tensors with two equal adjacent factors, hence on the degree $d$ part of $(v^2\mid v\in V)$. On increasing basis words it is $1$ on $x_{i_1}\cdots x_{i_d}$ and $0$ on the others, proving independence in every characteristic.
+
```

<details>
<summary><strong>Existing content: full exact TeX before the change</strong></summary>

```tex
Juxtaposition $v_1\cdots v_d$ in $T_S(V)$ denotes $v_1\otimes_S\cdots\otimes_S v_d$; in a specified quotient it denotes the image of that tensor.

```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX after the change</strong></summary>

```tex
Juxtaposition $v_1\cdots v_d$ in $T_S(V)$ denotes $v_1\otimes_S\cdots\otimes_S v_d$; in a specified quotient it denotes the image of that tensor.

\begin{example}[Polynomial and exterior algebras]\label{ex:polynomial-exterior}
Let $V$ be a finite-dimensional vector space with basis $x_1,\ldots,x_n$.
The \defn{symmetric algebra} and \defn{exterior algebra} are
\begin{equation}\label{eq:polynomial-exterior}
\begin{aligned}
\Symm(V)&=T_\Bbbk(V)/(x_ix_j-x_jx_i\mid i<j)
            \cong\Bbbk[x_1,\ldots,x_n],\\
\bigwedge V&=T_\Bbbk(V)/(v^2\mid v\in V).
\end{aligned}
\end{equation}
Both algebras have degree $0$ component $\Bbbk$, degree $1$ component $V$, and are generated in degree $1$: their elements are linear combinations of products of the images of the $x_i$.
The polynomial basis allows repetitions; the exterior basis consists of $1$ and $x_{i_1}\cdots x_{i_d}$ with $i_1<\cdots<i_d$.
The exterior relations are equivalently $x_i^2=0$ for $1\leq i\leq n$ and $x_ix_j+x_jx_i=0$ for $i<j$, in every characteristic.
\end{example}

The bases in Example~\ref{ex:polynomial-exterior} can be checked directly.
For $\Symm(V)$, commuting adjacent generators gives the ordered monomials, which are independent under the map to the polynomial ring.
For $\bigwedge V$, the relations reduce every word to a multiple of a strictly increasing word or to zero.
To prove independence in degree $d$, fix $i_1<\cdots<i_d$ and send $v_1\otimes\cdots\otimes v_d$ to the determinant of their coordinates in rows $i_1,\ldots,i_d$.
This functional vanishes on tensors with two equal adjacent factors, hence on the degree $d$ part of $(v^2\mid v\in V)$. On increasing basis words it is $1$ on $x_{i_1}\cdots x_{i_d}$ and $0$ on the others, proving independence in every characteristic.

```

</details>

[Back to the replacement index](#replacement-index)

---

## Replacement 6: Keep the later quadratic example concise

**Source location:** [line 1753](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1753)  
**Purpose:** Refer back to the relocated classical examples and state only why their relations make them quadratic.

> **Review together with [Replacement 5](#replacement-5-introduce-symmetric-and-exterior-algebras-as-soon-as-tensor-algebras-are-defined).**

### Line-by-Line Diff

**Added:** `+2` lines &nbsp; **Removed:** `-19` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1753,21 +1813,4 @@
-\begin{example}[Polynomial and exterior algebras]\label{ex:polynomial-exterior}
-For the classical comparison, take $S=\Bbbk$ and $V=\bigoplus_{i=1}^n\Bbbk x_i$.
-The \defn{symmetric algebra} and \defn{exterior algebra} are
-\begin{equation}\label{eq:polynomial-exterior}
-\begin{aligned}
-\Symm(V)&=T_\Bbbk(V)/(x_ix_j-x_jx_i\mid i<j)
-            \cong\Bbbk[x_1,\ldots,x_n],\\
-\bigwedge V&=T_\Bbbk(V)/(v^2\mid v\in V).
-\end{aligned}
-\end{equation}
-Both are quadratic.
-The polynomial basis allows repetitions; the exterior basis consists of $1$ and $x_{i_1}\cdots x_{i_d}$ with $i_1<\cdots<i_d$.
-The exterior relations are equivalently $x_i^2=0$ for $1\leq i\leq n$ and $x_ix_j+x_jx_i=0$ for $i<j$, in every characteristic.
+\begin{example}
+The symmetric and exterior algebras of Example~\ref{ex:polynomial-exterior} are quadratic: all defining relations in \eqref{eq:polynomial-exterior} belong to $V\otimes_\Bbbk V$.
 \end{example}
 
-The bases in Example~\ref{ex:polynomial-exterior} can be checked directly.
-For $\Symm(V)$, commuting adjacent generators gives the ordered monomials, which are independent under the map to the polynomial ring.
-For $\bigwedge V$, the relations reduce every word to a multiple of a strictly increasing word or to zero.
-To prove independence in degree $d$, fix $i_1<\cdots<i_d$ and send $v_1\otimes\cdots\otimes v_d$ to the determinant of their coordinates in rows $i_1,\ldots,i_d$.
-This functional vanishes on tensors with two equal adjacent factors, hence on the degree $d$ part of $(v^2\mid v\in V)$. On increasing basis words it is $1$ on $x_{i_1}\cdots x_{i_d}$ and $0$ on the others, proving independence in every characteristic.
-
```

<details>
<summary><strong>Existing content: full exact TeX before the change</strong></summary>

```tex
\begin{example}[Polynomial and exterior algebras]\label{ex:polynomial-exterior}
For the classical comparison, take $S=\Bbbk$ and $V=\bigoplus_{i=1}^n\Bbbk x_i$.
The \defn{symmetric algebra} and \defn{exterior algebra} are
\begin{equation}\label{eq:polynomial-exterior}
\begin{aligned}
\Symm(V)&=T_\Bbbk(V)/(x_ix_j-x_jx_i\mid i<j)
            \cong\Bbbk[x_1,\ldots,x_n],\\
\bigwedge V&=T_\Bbbk(V)/(v^2\mid v\in V).
\end{aligned}
\end{equation}
Both are quadratic.
The polynomial basis allows repetitions; the exterior basis consists of $1$ and $x_{i_1}\cdots x_{i_d}$ with $i_1<\cdots<i_d$.
The exterior relations are equivalently $x_i^2=0$ for $1\leq i\leq n$ and $x_ix_j+x_jx_i=0$ for $i<j$, in every characteristic.
\end{example}

The bases in Example~\ref{ex:polynomial-exterior} can be checked directly.
For $\Symm(V)$, commuting adjacent generators gives the ordered monomials, which are independent under the map to the polynomial ring.
For $\bigwedge V$, the relations reduce every word to a multiple of a strictly increasing word or to zero.
To prove independence in degree $d$, fix $i_1<\cdots<i_d$ and send $v_1\otimes\cdots\otimes v_d$ to the determinant of their coordinates in rows $i_1,\ldots,i_d$.
This functional vanishes on tensors with two equal adjacent factors, hence on the degree $d$ part of $(v^2\mid v\in V)$. On increasing basis words it is $1$ on $x_{i_1}\cdots x_{i_d}$ and $0$ on the others, proving independence in every characteristic.

```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX after the change</strong></summary>

```tex
\begin{example}
The symmetric and exterior algebras of Example~\ref{ex:polynomial-exterior} are quadratic: all defining relations in \eqref{eq:polynomial-exterior} belong to $V\otimes_\Bbbk V$.
\end{example}

```

</details>

[Back to the replacement index](#replacement-index)

---

## Replacement 7: Put the form-dependent orthogonal comparison in an advanced block

**Source location:** [line 1917](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1917)  
**Purpose:** Keep the form-independent definition of orthogonals in the main text and put the comparison using a symmetrising form in an advanced block.

### Line-by-Line Diff

**Added:** `+2` lines &nbsp; **Removed:** `-0` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1917,3 +1960,4 @@
+\begin{advanced}
 If $S$ is equipped with a symmetrising form $\tau:S\to\Bbbk$, the comparison maps $\alpha_M,\beta_M$ of \eqref{eq:dual-comparison} satisfy
 \begin{equation}\label{eq:orthogonal-comparison}
 \alpha_M(U^\perp)=\beta_M({}^\perp U)
@@ -1928,4 +1972,5 @@
 Non-degeneracy of $\tau$ forces $f(u)=0$ for every $u\in U$.
 For the left dual, $\tau(sg(u))=\tau(g(su))=0$ gives $g(u)=0$ instead.
 Bijectivity of $\alpha_M,\beta_M$ in Proposition~\ref{prop:dual-comparison} proves \eqref{eq:orthogonal-comparison}.
+\end{advanced}
 
```

<details>
<summary><strong>Existing content: full exact TeX before the change</strong></summary>

```tex
If $S$ is equipped with a symmetrising form $\tau:S\to\Bbbk$, the comparison maps $\alpha_M,\beta_M$ of \eqref{eq:dual-comparison} satisfy
\begin{equation}\label{eq:orthogonal-comparison}
\alpha_M(U^\perp)=\beta_M({}^\perp U)
=\{\lambda\in D(M)\mid\lambda(u)=0\text{ for all }u\in U\}.
\end{equation}
The forward inclusions follow by composing with $\tau$.
Conversely, $\alpha_M(f)(U)=0$ gives
\[
\tau(f(u)s)=\tau(f(us))=0
\quad\text{for all }s\in S,\ u\in U.
\]
Non-degeneracy of $\tau$ forces $f(u)=0$ for every $u\in U$.
For the left dual, $\tau(sg(u))=\tau(g(su))=0$ gives $g(u)=0$ instead.
Bijectivity of $\alpha_M,\beta_M$ in Proposition~\ref{prop:dual-comparison} proves \eqref{eq:orthogonal-comparison}.

```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX after the change</strong></summary>

```tex
\begin{advanced}
If $S$ is equipped with a symmetrising form $\tau:S\to\Bbbk$, the comparison maps $\alpha_M,\beta_M$ of \eqref{eq:dual-comparison} satisfy
\begin{equation}\label{eq:orthogonal-comparison}
\alpha_M(U^\perp)=\beta_M({}^\perp U)
=\{\lambda\in D(M)\mid\lambda(u)=0\text{ for all }u\in U\}.
\end{equation}
The forward inclusions follow by composing with $\tau$.
Conversely, $\alpha_M(f)(U)=0$ gives
\[
\tau(f(u)s)=\tau(f(us))=0
\quad\text{for all }s\in S,\ u\in U.
\]
Non-degeneracy of $\tau$ forces $f(u)=0$ for every $u\in U$.
For the left dual, $\tau(sg(u))=\tau(g(su))=0$ gives $g(u)=0$ instead.
Bijectivity of $\alpha_M,\beta_M$ in Proposition~\ref{prop:dual-comparison} proves \eqref{eq:orthogonal-comparison}.
\end{advanced}

```

</details>

[Back to the replacement index](#replacement-index)

---

## Replacement 8: Turn the tensor-duality proof into an exercise with a hidden full solution

**Source location:** [line 1952](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1952)  
**Purpose:** Replace the main-text proof with a structured exercise and retain the original full proof verbatim in a hidden source block.

> **Review together with [Replacement 2](#replacement-2-state-the-canonical-identifications-precisely-and-resolve-the-merge-conflict).**

### Line-by-Line Diff

**Added:** `+64` lines &nbsp; **Removed:** `-0` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1952,4 +1997,68 @@
 \subsection{Exercises}
+
+\begin{exercise}[Tensor duality]\label{ex:tensor-duality-proof}
+Prove Proposition~\ref{prop:tensor-duals}.
+\begin{enumerate}
+\item Check that the formulas in \eqref{eq:tensor-evaluations} respect the tensor relations and define $S$-bimodule maps.
+\item Prove bijectivity by first taking $V=S$ for $\theta_r$ and $W=S$ for $\theta_\ell$, and then using Corollary~\ref{cor:semisimple-summands}.
+\item For bimodule maps $p:V\to V'$ and $q:W\to W'$, prove
+\[
+(p\otimes q)^*\circ\theta_r
+=\theta_r\circ(q^*\otimes p^*),
+\qquad
+{}^*(p\otimes q)\circ\theta_\ell
+=\theta_\ell\circ({}^*q\otimes{}^*p).
+\]
+\end{enumerate}
+\end{exercise}
+
+% Solution retained in the source, not typeset.
+\iffalse
+\begin{proof}
+\emph{Well-definedness.}
+For the right duals, right $S$-linearity gives
+\[
+g(f(vs)w)=g(f(v)sw),\qquad
+(gs)(f(v)w)=g(sf(v)w)=g((sf)(v)w).
+\]
+The first identity respects the relation in $V\otimes_S W$, and the second respects the relation in $W^*\otimes_S V^*$.
+The resulting functional is right $S$-linear because $g$ is.
+For the left duals, the corresponding identities are
+\[
+f(vs\,g(w))=f(vg(sw)),\qquad
+f(v(gs)(w))=f(vg(w)s)=(sf)(vg(w)).
+\]
+Left $S$-linearity of $f$ makes the resulting functional left $S$-linear.
+The outer actions in \eqref{eq:tensor-dual-actions} give
+\[
+\begin{aligned}
+\theta_r(sg\otimes ft)(v\otimes w)&=s\,g(f(tv)w),\\
+\theta_\ell(sg\otimes ft)(v\otimes w)&=f(vg(ws))t,
+\end{aligned}
+\]
+which are the required bimodule identities.
+
+\emph{Bijectivity.}
+To check $\theta_r$, forget the left action on $V$.
+For $V=S$, identify $S^*\cong S$ by $f\mapsto f(1)$; then $\theta_r$ is $W^*\otimes_S S\to W^*$, $g\otimes s\mapsto gs$, an isomorphism by Lemma~\ref{lem:tensor-properties}(3).
+The formula commutes with maps of right $S$-modules in $V$, so it is an isomorphism for finite direct sums and direct summands of $S$.
+Corollary~\ref{cor:semisimple-summands} applies to $V$.
+For $\theta_\ell$, use $W=S$ as a left module, where the map is $S\otimes_S{}^*V\to{}^*V$, $s\otimes f\mapsto sf$, and apply the same argument to $W$.
+
+\emph{Naturality.}
+For bimodule maps $p:V\to V'$ and $q:W\to W'$, the square
+\[
+\xymatrix@C=48pt@R=22pt{
+(W')^*\otimes_S(V')^* \ar[r]^{\theta_r} \ar[d]_{q^*\otimes p^*}
+& (V'\otimes_S W')^* \ar[d]^{(p\otimes q)^*}\\
+W^*\otimes_S V^* \ar[r]_{\theta_r}
+& (V\otimes_S W)^*
+}
+\]
+commutes: both routes send $g\otimes f$, evaluated at $v\otimes w$, to $g(f(p(v))q(w))$.
+For $\theta_\ell$, the corresponding two routes give $f(p(v)g(q(w)))$.
+\end{proof}
+\fi
 
 \begin{exercise}
 Let $A=\Bbbk A_4/(e_{13},e_{24})$
```

<details>
<summary><strong>Existing content: full exact TeX before the change</strong></summary>

```tex
\subsection{Exercises}

\begin{exercise}
Let $A=\Bbbk A_4/(e_{13},e_{24})$
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX after the change</strong></summary>

```tex
\subsection{Exercises}

\begin{exercise}[Tensor duality]\label{ex:tensor-duality-proof}
Prove Proposition~\ref{prop:tensor-duals}.
\begin{enumerate}
\item Check that the formulas in \eqref{eq:tensor-evaluations} respect the tensor relations and define $S$-bimodule maps.
\item Prove bijectivity by first taking $V=S$ for $\theta_r$ and $W=S$ for $\theta_\ell$, and then using Corollary~\ref{cor:semisimple-summands}.
\item For bimodule maps $p:V\to V'$ and $q:W\to W'$, prove
\[
(p\otimes q)^*\circ\theta_r
=\theta_r\circ(q^*\otimes p^*),
\qquad
{}^*(p\otimes q)\circ\theta_\ell
=\theta_\ell\circ({}^*q\otimes{}^*p).
\]
\end{enumerate}
\end{exercise}

% Solution retained in the source, not typeset.
\iffalse
\begin{proof}
\emph{Well-definedness.}
For the right duals, right $S$-linearity gives
\[
g(f(vs)w)=g(f(v)sw),\qquad
(gs)(f(v)w)=g(sf(v)w)=g((sf)(v)w).
\]
The first identity respects the relation in $V\otimes_S W$, and the second respects the relation in $W^*\otimes_S V^*$.
The resulting functional is right $S$-linear because $g$ is.
For the left duals, the corresponding identities are
\[
f(vs\,g(w))=f(vg(sw)),\qquad
f(v(gs)(w))=f(vg(w)s)=(sf)(vg(w)).
\]
Left $S$-linearity of $f$ makes the resulting functional left $S$-linear.
The outer actions in \eqref{eq:tensor-dual-actions} give
\[
\begin{aligned}
\theta_r(sg\otimes ft)(v\otimes w)&=s\,g(f(tv)w),\\
\theta_\ell(sg\otimes ft)(v\otimes w)&=f(vg(ws))t,
\end{aligned}
\]
which are the required bimodule identities.

\emph{Bijectivity.}
To check $\theta_r$, forget the left action on $V$.
For $V=S$, identify $S^*\cong S$ by $f\mapsto f(1)$; then $\theta_r$ is $W^*\otimes_S S\to W^*$, $g\otimes s\mapsto gs$, an isomorphism by Lemma~\ref{lem:tensor-properties}(3).
The formula commutes with maps of right $S$-modules in $V$, so it is an isomorphism for finite direct sums and direct summands of $S$.
Corollary~\ref{cor:semisimple-summands} applies to $V$.
For $\theta_\ell$, use $W=S$ as a left module, where the map is $S\otimes_S{}^*V\to{}^*V$, $s\otimes f\mapsto sf$, and apply the same argument to $W$.

\emph{Naturality.}
For bimodule maps $p:V\to V'$ and $q:W\to W'$, the square
\[
\xymatrix@C=48pt@R=22pt{
(W')^*\otimes_S(V')^* \ar[r]^{\theta_r} \ar[d]_{q^*\otimes p^*}
& (V'\otimes_S W')^* \ar[d]^{(p\otimes q)^*}\\
W^*\otimes_S V^* \ar[r]_{\theta_r}
& (V\otimes_S W)^*
}
\]
commutes: both routes send $g\otimes f$, evaluated at $v\otimes w$, to $g(f(p(v))q(w))$.
For $\theta_\ell$, the corresponding two routes give $f(p(v)g(q(w)))$.
\end{proof}
\fi

\begin{exercise}
Let $A=\Bbbk A_4/(e_{13},e_{24})$
```

</details>

[Back to the replacement index](#replacement-index)

---

## Replacement 9: Use the declared tensor-dual convention in the orthogonal example

**Source location:** [line 1942](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1942)  
**Purpose:** Use the explicit convention already established instead of repeating how the tensor-dual spaces are identified.

### Line-by-Line Diff

**Added:** `+1` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1942 +1987 @@
-Identifying $(V\otimes_\Bbbk V)^*$ with $V^*\otimes_\Bbbk V^*$ using $\theta_r$ from \eqref{eq:tensor-evaluations},
+Under the tensor-dual identification \eqref{eq:tensor-evaluations},
```

<details>
<summary><strong>Existing content: full exact TeX before the change</strong></summary>

```tex
Identifying $(V\otimes_\Bbbk V)^*$ with $V^*\otimes_\Bbbk V^*$ using $\theta_r$ from \eqref{eq:tensor-evaluations},
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX after the change</strong></summary>

```tex
Under the tensor-dual identification \eqref{eq:tensor-evaluations},
```

</details>

[Back to the replacement index](#replacement-index)

---
