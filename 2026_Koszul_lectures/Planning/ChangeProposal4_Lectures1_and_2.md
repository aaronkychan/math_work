# Change Proposal 4: Lectures 1 and 2

> **Applied on 9 October 2026.** All eleven revised replacements have been applied, and the updated PDF has been compiled and saved alongside the TeX.

**Application note:** the quoted proposals below are retained as reviewed. In addition, the new counterexample begins with its purpose, as requested at approval: the tensor-direct product comparison need not be surjective when the fixed factor is infinite-dimensional. Its set-builder spacing was also tidied. The existing hidden-content setting was left unchanged; no on/off tests were performed.

**Prepared:** 9 October 2026  
**Source:** [2026_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex)

## Revision After Your Review

- **Replacement 4:** remove the proposed naturality squares; number the natural isomorphisms themselves.
- **Replacements 5 and 7:** refer to those natural isomorphisms. The previously proposed version of Replacement 7 is withdrawn and rephrased below.
- **Replacement 11:** retain the mathematical content entirely inside an advanced block.
- **Replacement 2:** apply the same principle in Lecture 1: direct-sum distributivity stays central; the additional direct-product comparison and counterexample are advanced.

These are revisions of **Change Proposal 4**, not a new proposal. The original TeX quotations remain unchanged.

## Scope

| Area | Proposed treatment |
| --- | --- |
| Seven active Lecture 1 comments | Address every comment, including the requested hidden exercise solution. |
| Lecture 1: direct sums and products | Keep direct-sum distributivity in the main text; place the tensor-direct product comparison, proof, and counterexample in advanced material. |
| Lecture 2: tensor products | Expand the existing advanced paragraph to a proposition covering both variables, with its proof and discussion still entirely advanced. |
| Existing advanced material | Keep literature citations and the two-sided notation comparison advanced. |
| Existing hidden environment | Reuse it for the full exercise solution; leave the preamble switch unchanged. |
| Commented-out material, other content, and Lecture 3 | Preserve unchanged. |

## Placement and Emphasis

Direct sums are the main setting for these lectures on locally finite graded algebras. Replacements **2 and 11** develop the requested tensor-direct product interaction as advanced material, without making it a prerequisite for the main exposition. Basic direct-product notation is retained where it already supports the comparison between graded and full linear duals.

Once a natural isomorphism has been stated, later uses should cite its numbered statement. Do not repeat a commuting square merely to restate the definition of naturality. Replacement **4** numbers the natural isomorphisms, and Replacements **5 and 7** refer directly to that equation.

**The mathematical distinction:** tensor products distribute over all direct sums and over finite direct products. For an infinite direct product, the canonical comparison need not be surjective. Over vector spaces it is injective, and it is an isomorphism when the fixed tensor factor is finite-dimensional. Over a finite-dimensional semisimple algebra, the same injectivity and finite-dimensional isomorphism statements hold on either side. The module proposition also records the more general sufficient condition of being a summand of a finite free module; it does **not** assert injectivity over an arbitrary algebra.

## Replacement Index

| No. | Replacement | Line changes | Dependencies |
| --- | --- | --- | --- |
| **1** | [Cite the enveloping-module convention inside advanced material](#replacement-1) | `+4` / `-1` | Independent |
| **2** | [Keep tensor-direct sum distributivity central and direct products advanced](#replacement-2) | `+53` / `-0` | Review with 11 |
| **3** | [Give the Grant-Iyama notation dictionary](#replacement-3) | `+25` / `-1` | Independent |
| **4** | [State and number the natural isomorphisms without drawing squares](#replacement-4) | `+10` / `-5` | Review with 5 and 7 |
| **5** | [Keep the naturality verification concise](#replacement-5) | `+1` / `-1` | Requires 4 |
| **6** | [Correct the graded two-sided component notation](#replacement-6) | `+1` / `-1` | Independent |
| **7** | [Deduce graded naturality from the numbered natural isomorphisms](#replacement-7) | `+1` / `-1` | Requires 4 |
| **8** | [Turn dependence on the form into an exercise with a hidden solution](#replacement-8) | `+63` / `-9` | Independent |
| **9** | [State the purpose of the bimodule-block example first](#replacement-9) | `+2` / `-1` | Independent |
| **10** | [Replace the vague conclusion by identities between maps](#replacement-10) | `+8` / `-1` | Independent |
| **11** | [Keep the full tensor-direct product proposition in advanced material](#replacement-11) | `+56` / `-17` | Requires 2 |

## Comment Checklist

| Original location | Comment addressed | Replacement |
| --- | --- | --- |
| [Line 705](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:705) | Reference for enveloping modules; citations only in advanced material. | **1** |
| [Line 962](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:962) | Compare notation with Grant-Iyama and identify the borrowed conventions. | **3** |
| [Line 1007](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1007) | Write out the natural isomorphisms. | **4** |
| [Line 1039](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1039) | Shorten the naturality check and cite the numbered natural isomorphisms. | **5** |
| [Line 1189](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1189) | Make the form-dependence example an exercise, give two forms, and hide a full solution. | **8** |
| [Line 1192](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1192) | State the purpose of the block example first. | **9** |
| [Line 1235](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1235) | Replace the vague conclusion by explicit symbols. | **10** |

Replacement **6** corrects a stray `f` in a graded-component subscript. Replacement **7**, rephrased after rejection of its previous version, deduces graded naturality from the numbered natural isomorphisms without referring to a displayed square.

## How to Review

Each **diff** shows removals with `-`, additions with `+`, and unchanged context with a leading space. Colour is supplementary; the signs identify every change. Hunk headers give exact old and proposed line numbers, assuming all eleven replacements are applied. Original locations refer to the source read on 9 October 2026.

Expand the **Existing content** and **Proposed replacement** sections to see both full, exact TeX passages. No source text has been abbreviated.

### Checks Completed

- [x] All eleven existing passages match the current source uniquely and do not overlap.
- [x] All seven active Lecture 1 comments are addressed in the proposed source.
- [x] All cross-reference targets exist in the proposed source, including the new label for the natural isomorphisms; no duplicate labels.
- [x] All environments balance; hidden delimiters are on separate, unindented lines.
- [x] Existing commented-out material is preserved.
- [x] All new literature citations are inside advanced blocks.
- [x] The additional tensor-direct product statements, proofs, and counterexample are entirely advanced.
- [x] No naturality diagrams are added; subsequent references point to the numbered natural isomorphisms.
- [x] Lecture 3 and the preamble are unchanged.
- [x] The new exercise includes both distinct actions and an explicit graded module isomorphism.
- [x] Apply the approved replacements, compile with the existing hidden-content setting, inspect the changed layout, and save the PDF alongside the source.
- [x] Add the example-purpose distinction and the instruction not to retest hidden-content settings to the math-discussion skill.

**Compilation:** successful, with no unresolved references. The PDF has 35 pages. The two pre-existing line-overflow warnings remain; there are no new ones.

**Source check:** Grant-Iyama, Section 2, printed page 2591, for enveloping modules; Section 2.1, printed pages 2592-2593, for the four duals. These were checked in the local paper. The notes retain their own right-module convention and explicitly translate the two-sided dual by flipping the tensor factors.

---

<a id="replacement-1"></a>

## Replacement 1: Cite the enveloping-module convention inside advanced material

**Source location:** [line 705](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:705)  
**Purpose:** Address the reference comment without placing a literature citation in the main exposition; specify Grant-Iyama's left-module convention and the notes' right-module convention.  
**Dependencies:** Independent

### Line-by-Line Diff

**Added:** `+4` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -705,4 +705,7 @@
-\comm{add a reference to this fact (we should avoid citing things in min lecture content, but advanced material are fine.)}
 Thus $\Mod A^\en$ is also the category of $A$-bimodules and maps preserving both actions.
 
 \begin{advanced}
+Grant--Iyama \cite[\S2, p.~2591]{GI20} identify bimodules with left modules over $A^\en$, using $(a\otimes b^\op)m=amb$.
+Our right module convention is \eqref{eq:enveloping-action}: $m\cdot(a\otimes b^\op)=bma$.
+Both describe the same bimodules; the side on which $A^\en$ acts determines the formula.
+
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
\comm{add a reference to this fact (we should avoid citing things in min lecture content, but advanced material are fine.)}
Thus $\Mod A^\en$ is also the category of $A$-bimodules and maps preserving both actions.

\begin{advanced}
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
Thus $\Mod A^\en$ is also the category of $A$-bimodules and maps preserving both actions.

\begin{advanced}
Grant--Iyama \cite[\S2, p.~2591]{GI20} identify bimodules with left modules over $A^\en$, using $(a\otimes b^\op)m=amb$.
Our right module convention is \eqref{eq:enveloping-action}: $m\cdot(a\otimes b^\op)=bma$.
Both describe the same bimodules; the side on which $A^\en$ acts determines the formula.

```

</details>

[Back to the replacement index](#replacement-index)

---

<a id="replacement-2"></a>

## Replacement 2: Keep tensor-direct sum distributivity central and direct products advanced

**Source location:** [line 762](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:762)  
**Purpose:** Give the direct-sum formula and its short proof in the main exposition. Put the tensor-direct product comparison, its proof, and its counterexample in an advanced block.  
**Dependencies:** Review with 11

### Line-by-Line Diff

**Added:** `+53` lines &nbsp; **Removed:** `-0` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -762,2 +765,55 @@
 In a direct sum, an element is a finite sum of its components; no notion of convergence is involved.
 
+Tensor products distribute over direct sums: for vector spaces $U_i$ ($i\in I$) and $V$, there is a canonical linear isomorphism
+\[
+\Bigl(\bigoplus_iU_i\Bigr)\otimes_\Bbbk V
+\xrightarrow{\sim}\bigoplus_i(U_i\otimes_\Bbbk V),
+\qquad (u_i)_i\otimes v\longmapsto(u_i\otimes v)_i.
+\]
+The map is defined by the universal property in Definition~\ref{def:vector-tensor}.
+If $\iota_i:U_i\to\bigoplus_jU_j$ is the inclusion, the inverse sends $u\otimes v$ in summand $i$ to $\iota_i(u)\otimes v$.
+The same construction applies in the other tensor variable.
+
+\begin{advanced}
+For direct products, the corresponding map need not be an isomorphism.
+
+\begin{lemma}\label{lem:vector-tensor-products}
+For vector spaces $U_i$ ($i\in I$) and $V$, the coordinate projections define a linear map
+\begin{equation}\label{eq:vector-tensor-products}
+\Bigl(\prod_iU_i\Bigr)\otimes_\Bbbk V
+\longrightarrow\prod_i(U_i\otimes_\Bbbk V),
+\qquad (u_i)_i\otimes v\longmapsto(u_i\otimes v)_i.
+\end{equation}
+This map is injective, and is an isomorphism if $I$ is finite or $V$ is finite-dimensional.
+The same statements hold with the two tensor factors reversed.
+\end{lemma}
+
+\begin{proof}
+The map is defined by the universal property in Definition~\ref{def:vector-tensor}.
+Every tensor can be written $\sum_{\ell=1}^r u^{(\ell)}\otimes v_\ell$ with the $v_\ell$ linearly independent: choose a basis of the span of its finitely many second factors.
+If its image is zero, then $\sum_{\ell=1}^r u_i^{(\ell)}\otimes v_\ell=0$ for every $i$.
+The tensor-product basis construction gives $u_i^{(\ell)}=0$ for all $i,\ell$, proving injectivity.
+If $v_1,\ldots,v_r$ is a basis of $V$, the inverse is
+\[
+\prod_i(U_i\otimes_\Bbbk V)\longrightarrow
+\Bigl(\prod_iU_i\Bigr)\otimes_\Bbbk V,\qquad
+\Bigl(\sum_{\ell=1}^r u_i^{(\ell)}\otimes v_\ell\Bigr)_i
+\longmapsto\sum_{\ell=1}^r(u_i^{(\ell)})_i\otimes v_\ell.
+\]
+For finite $I$, products equal sums.
+Reversing the tensor factors gives the other statements, since $U\otimes_\Bbbk V\to V\otimes_\Bbbk U$, $u\otimes v\mapsto v\otimes u$, is an isomorphism.
+\end{proof}
+
+\begin{example}\label{ex:tensor-product-product-failure}
+Take $U_i=\Bbbk$ for $i\geq1$ and $V=\bigoplus_{j\geq1}\Bbbk v_j$.
+Under $\Bbbk\otimes_\Bbbk V\cong V$, the image of the product comparison in \eqref{eq:vector-tensor-products} is
+\[
+\left\{(w_i)_i\in\prod_{i\geq1}V\ \middle|\ 
+\dim_\Bbbk\operatorname{span}_\Bbbk\{w_i\mid i\geq1\}<\infty\right\}.
+\]
+Indeed, the image of $\sum_{\ell=1}^r(c_i^{(\ell)})_i\otimes w_\ell$ has every entry in $\operatorname{span}_\Bbbk\{w_1,\ldots,w_r\}$.
+Conversely, expand all entries in a basis of their common finite-dimensional span.
+Since the $v_i$ are linearly independent, $(v_i)_i$ is not in the image.
+\end{example}
+\end{advanced}
+
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
In a direct sum, an element is a finite sum of its components; no notion of convergence is involved.

```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
In a direct sum, an element is a finite sum of its components; no notion of convergence is involved.

Tensor products distribute over direct sums: for vector spaces $U_i$ ($i\in I$) and $V$, there is a canonical linear isomorphism
\[
\Bigl(\bigoplus_iU_i\Bigr)\otimes_\Bbbk V
\xrightarrow{\sim}\bigoplus_i(U_i\otimes_\Bbbk V),
\qquad (u_i)_i\otimes v\longmapsto(u_i\otimes v)_i.
\]
The map is defined by the universal property in Definition~\ref{def:vector-tensor}.
If $\iota_i:U_i\to\bigoplus_jU_j$ is the inclusion, the inverse sends $u\otimes v$ in summand $i$ to $\iota_i(u)\otimes v$.
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
Take $U_i=\Bbbk$ for $i\geq1$ and $V=\bigoplus_{j\geq1}\Bbbk v_j$.
Under $\Bbbk\otimes_\Bbbk V\cong V$, the image of the product comparison in \eqref{eq:vector-tensor-products} is
\[
\left\{(w_i)_i\in\prod_{i\geq1}V\ \middle|\ 
\dim_\Bbbk\operatorname{span}_\Bbbk\{w_i\mid i\geq1\}<\infty\right\}.
\]
Indeed, the image of $\sum_{\ell=1}^r(c_i^{(\ell)})_i\otimes w_\ell$ has every entry in $\operatorname{span}_\Bbbk\{w_1,\ldots,w_r\}$.
Conversely, expand all entries in a basis of their common finite-dimensional span.
Since the $v_i$ are linearly independent, $(v_i)_i$ is not in the image.
\end{example}
\end{advanced}

```

</details>

[Back to the replacement index](#replacement-index)

---

<a id="replacement-3"></a>

## Replacement 3: Give the Grant-Iyama notation dictionary

**Source location:** [line 962](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:962)  
**Purpose:** Address the comparison comment with all four ungraded duals, distinguish left and right linearity, and explain the flip needed for the two-sided dual. The entire addition stays inside the existing advanced block.  
**Dependencies:** Independent

### Line-by-Line Diff

**Added:** `+25` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -962 +1018,25 @@
-\comm{add notes about difference of notations compare to Grant-Iyama and things that are taken from it.}
+The four duals above follow the distinction in Grant--Iyama \cite[\S2.1, pp.~2592--2593]{GI20}, with the following notation changes:
+\[
+\begin{array}{c|c|c}
+\text{construction}&\text{Grant--Iyama}&\text{these notes}\\ \hline
+\Bbbk\text{-linear dual}&M^*&D(M)\\
+\text{left }S\text{-linear dual}&M^{*_\ell}&{}^*M\\
+\text{right }S\text{-linear dual}&M^{*_r}&M^*\\
+\text{two-sided dual}&M^\vee&M^{*_{\en}}
+\end{array}
+\]
+The last row also changes the convention for enveloping modules.
+Their $F:M\to S^\en$ is left $S^\en$-linear.
+Define
+\[
+\sigma:S^\en\longrightarrow S^\en,\qquad
+a\otimes b^\op\longmapsto b\otimes a^\op.
+\]
+Since $\sigma(xy)=\sigma(y)\sigma(x)$ for $x,y\in S^\en$, the map $\sigma\circ F:M\to S^\en$ satisfies
+\[
+(\sigma\circ F)(tms)=(\sigma\circ F)(m)(s\otimes t^\op)
+\quad(s,t\in S,\ m\in M),
+\]
+and belongs to our $M^{*_{\en}}$.
+Thus $M^\vee\to M^{*_{\en}}$, $F\mapsto\sigma\circ F$, translates their two-sided dual into our convention.
+In particular, their star denotes the linear dual; our star denotes the right $S$-dual.
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
\comm{add notes about difference of notations compare to Grant-Iyama and things that are taken from it.}
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
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
```

</details>

[Back to the replacement index](#replacement-index)

---

<a id="replacement-4"></a>

## Replacement 4: State and number the natural isomorphisms without drawing squares

**Source location:** [line 999](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:999)  
**Purpose:** Keep the component maps and state the natural isomorphisms between the precise functors in one numbered equation. Do not restore the intentionally removed naturality diagrams.  
**Dependencies:** Review with 5 and 7

### Line-by-Line Diff

**Added:** `+10` lines &nbsp; **Removed:** `-5` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -999,10 +1079,15 @@
-For finite-dimensional right $S$-module $M$ and left $S$-modules $N$, the maps
+For $M\in\mod S$ and $N\in\mod(S^\op)$, the maps
 \begin{equation}\label{eq:dual-comparison}
 \alpha_M:M^*\longrightarrow D(M),\quad f\longmapsto\tau\circ f,
 \qquad
 \beta_N:{}^*N\longrightarrow D(N),\quad g\longmapsto\tau\circ g
 \end{equation}
-are isomorphisms of $S$-modules, which induces a natural isomorphisms of the corresponding contravariant functors.
-\[
-\comm{write them out}
-\]
+are $S$-module isomorphisms and give natural isomorphisms
+\begin{equation}\label{eq:dual-comparison-functors}
+\begin{aligned}
+\alpha:(-)^*&\xrightarrow{\sim}D
+&&\text{of functors }(\mod S)^\op\longrightarrow\mod(S^\op),\\
+\beta:{}^*(-)&\xrightarrow{\sim}D
+&&\text{of functors }(\mod(S^\op))^\op\longrightarrow\mod S.
+\end{aligned}
+\end{equation}
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
For finite-dimensional right $S$-module $M$ and left $S$-modules $N$, the maps
\begin{equation}\label{eq:dual-comparison}
\alpha_M:M^*\longrightarrow D(M),\quad f\longmapsto\tau\circ f,
\qquad
\beta_N:{}^*N\longrightarrow D(N),\quad g\longmapsto\tau\circ g
\end{equation}
are isomorphisms of $S$-modules, which induces a natural isomorphisms of the corresponding contravariant functors.
\[
\comm{write them out}
\]
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
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
```

</details>

[Back to the replacement index](#replacement-index)

---

<a id="replacement-5"></a>

## Replacement 5: Keep the naturality verification concise

**Source location:** [line 1039](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1039)  
**Purpose:** Keep a routine-check sentence for naturality and refer to the numbered natural isomorphisms, not to a displayed commuting square.  
**Dependencies:** Requires 4

### Line-by-Line Diff

**Added:** `+1` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1039 +1124 @@
-\old{For \eqref{eq:dual-comparison-naturality}, both routes send $f\in N^*$ to $\tau\circ f\circ u$; the calculation for $\beta$ is identical.}\comm{say something like routine to check something something commutes}
+Naturality in \eqref{eq:dual-comparison-functors} is routine to check.
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
\old{For \eqref{eq:dual-comparison-naturality}, both routes send $f\in N^*$ to $\tau\circ f\circ u$; the calculation for $\beta$ is identical.}\comm{say something like routine to check something something commutes}
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
Naturality in \eqref{eq:dual-comparison-functors} is routine to check.
```

</details>

[Back to the replacement index](#replacement-index)

---

<a id="replacement-6"></a>

## Replacement 6: Correct the graded two-sided component notation

**Source location:** [line 1110](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1110)  
**Purpose:** Correct the adjacent stray f in the component formula; no change of mathematical convention.  
**Dependencies:** Independent

### Line-by-Line Diff

**Added:** `+1` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1110 +1195 @@
-\qquad (M^{\grstar[_{\en}]})f_i=(M_{-i})^{*_{\en}}.
+\qquad (M^{\grstar[_{\en}]})_i=(M_{-i})^{*_{\en}}.
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
\qquad (M^{\grstar[_{\en}]})f_i=(M_{-i})^{*_{\en}}.
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
\qquad (M^{\grstar[_{\en}]})_i=(M_{-i})^{*_{\en}}.
```

</details>

[Back to the replacement index](#replacement-index)

---

<a id="replacement-7"></a>

## Replacement 7: Deduce graded naturality from the numbered natural isomorphisms

**Source location:** [line 1149](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1149)  
**Purpose:** Replace the rejected reference to restored squares. The graded maps inherit naturality degreewise from the natural isomorphisms already stated; no diagram needs to be repeated.  
**Dependencies:** Requires 4

### Line-by-Line Diff

**Added:** `+1` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1149 +1234 @@
-They are isomorphisms of degree $0$, and their naturality squares are the direct sums of the squares in \eqref{eq:dual-comparison-naturality} and its counterpart for $\beta$.
+They are isomorphisms of degree $0$; naturality follows by applying the natural isomorphisms \eqref{eq:dual-comparison-functors} in each degree.
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
They are isomorphisms of degree $0$, and their naturality squares are the direct sums of the squares in \eqref{eq:dual-comparison-naturality} and its counterpart for $\beta$.
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
They are isomorphisms of degree $0$; naturality follows by applying the natural isomorphisms \eqref{eq:dual-comparison-functors} in each degree.
```

</details>

[Back to the replacement index](#replacement-index)

---

<a id="replacement-8"></a>

## Replacement 8: Turn dependence on the form into an exercise with a hidden solution

**Source location:** [line 1167](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1167)  
**Purpose:** Use two explicit forms over the rational field, ask for all matrix-unit actions and an isomorphism between the resulting modules, and retain a complete solution in the preamble-controlled hidden environment. Preserve the existing labels for the form and functionals.  
**Dependencies:** Independent

### Line-by-Line Diff

**Added:** `+63` lines &nbsp; **Removed:** `-9` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1167,12 +1252,13 @@
-\begin{example}\label{ex:transported-dual-action}
+\begin{exercise}[Dependence of the action on the form]\label{ex:transported-dual-action}
+In this exercise take $\Bbbk=\mathbb Q$.
 Let $A=\Bbbk A_2$, $S=\Bbbk e_{11}\oplus\Bbbk e_{22}$, and $M=e_{11}A$.
-For $c_1,c_2\in\Bbbk\setminus\{0\}$, choose the symmetrising form
+For $c_1,c_2\in\Bbbk\setminus\{0\}$, define
 \begin{equation}\label{eq:transported-dual-form}
 \tau:S\longrightarrow\Bbbk,\qquad
 a e_{11}+b e_{22}\longmapsto c_1a+c_2b
 \quad(a,b\in\Bbbk).
 \end{equation}
-Define right $S$-linear maps
+Consider the right $S$-linear maps
 \begin{equation}\label{eq:transported-dual-functionals}
 \begin{aligned}
 \varphi_0:M&\longrightarrow S,& a e_{11}+b e_{12}&\longmapsto a e_{11},\\
@@ -1180,12 +1266,65 @@
 \quad(a,b\in\Bbbk).
 \end{aligned}
 \end{equation}
-Their degrees in $M^{\grstar}$ are $0,-1$, respectively, and
+\begin{enumerate}
+\item Verify that $\tau$ is symmetrising and that $\varphi_0,\varphi_1$ form a homogeneous basis of $M^{\grstar}$. Determine their degrees.
+\item Set $\tau_1(ae_{11}+be_{22})=a+b$ and $\tau_2(ae_{11}+be_{22})=a+2b$.
+Write $\cdot_1,\cdot_2$ for the respective left $A$-actions transported from $\bbD(M)$ using \eqref{eq:dual-comparison}.
+Calculate the actions of $e_{11},e_{22},e_{12}$ on $\varphi_0,\varphi_1$ for both forms.
+Are the two actions equal?
+\item Construct a graded $A$-module isomorphism
 \[
-\alpha_M(e_{12}\varphi_1)(e_{11})
-=\alpha_M(\varphi_1)(e_{12})=c_2,
-\qquad e_{12}\varphi_1=\frac{c_2}{c_1}\varphi_0.
+t:(M^{\grstar},\cdot_1)\longrightarrow(M^{\grstar},\cdot_2)
 \]
-Thus changing the form can change the action on the same vector space. Two choices give isomorphic $A$-modules by composing their identifications with $\bbD(M)$.\comm{make this an exercise (hide the solution); exercise should also give two different choices of symmeterising form and ask for how things change; prepare full solution to this.}
-\end{example}
+by giving $t(\varphi_0)$ and $t(\varphi_1)$.
+\end{enumerate}
+\end{exercise}
 
+\begin{hidden}
+\begin{proof}[Solution]
+\emph{The form and the basis.}
+The algebra $S$ is commutative, so $\tau(st)=\tau(ts)$.
+If $s=ae_{11}+be_{22}$ satisfies $\tau(se_{11})=\tau(se_{22})=0$, then $c_1a=c_2b=0$, hence $s=0$.
+Thus $\tau$ is non-degenerate.
+
+A right $S$-linear map $f:M\to S$ must satisfy $f(e_{11})\in Se_{11}=\Bbbk e_{11}$ and $f(e_{12})\in Se_{22}=\Bbbk e_{22}$.
+Conversely, any choices of these two values define such a map.
+Consequently, $\varphi_0,\varphi_1$ form a basis, with degrees $0,-1$, respectively.
+
+\emph{The actions.}
+For the general form \eqref{eq:transported-dual-form}, write $\alpha_M(f)=\tau\circ f$.
+For $m=ae_{11}+be_{12}$,
+\[
+\alpha_M(\varphi_0)(m)=c_1a,\qquad
+\alpha_M(\varphi_1)(m)=c_2b,\qquad
+\alpha_M(e_{12}\cdot\varphi_1)(m)
+=\alpha_M(\varphi_1)(me_{12})=c_2a.
+\]
+Using also $me_{11}=ae_{11}$ and $me_{22}=be_{12}$ gives all non-zero actions:
+\[
+e_{11}\cdot\varphi_0=\varphi_0,\qquad
+e_{22}\cdot\varphi_1=\varphi_1,\qquad
+e_{12}\cdot\varphi_1=\frac{c_2}{c_1}\varphi_0.
+\]
+All other actions of the three matrix units on the two basis vectors are zero.
+Thus $e_{12}\cdot_1\varphi_1=\varphi_0$ whereas $e_{12}\cdot_2\varphi_1=2\varphi_0$, so the actions are not equal.
+
+\emph{The isomorphism.}
+Define
+\[
+t:(M^{\grstar},\cdot_1)\longrightarrow(M^{\grstar},\cdot_2),
+\qquad
+t(\varphi_0)=\varphi_0,\quad t(\varphi_1)=\tfrac12\varphi_1.
+\]
+The map is invertible, preserves degrees, and commutes with the actions of $e_{11}$ and $e_{22}$.
+For the remaining matrix unit,
+\[
+t(e_{12}\cdot_1\varphi_1)=t(\varphi_0)=\varphi_0
+=e_{12}\cdot_2(\tfrac12\varphi_1)
+=e_{12}\cdot_2t(\varphi_1).
+\]
+Both sides vanish on $\varphi_0$.
+Since the three matrix units span $A$, the map $t$ is $A$-linear.
+\end{proof}
+\end{hidden}
+
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
\begin{example}\label{ex:transported-dual-action}
Let $A=\Bbbk A_2$, $S=\Bbbk e_{11}\oplus\Bbbk e_{22}$, and $M=e_{11}A$.
For $c_1,c_2\in\Bbbk\setminus\{0\}$, choose the symmetrising form
\begin{equation}\label{eq:transported-dual-form}
\tau:S\longrightarrow\Bbbk,\qquad
a e_{11}+b e_{22}\longmapsto c_1a+c_2b
\quad(a,b\in\Bbbk).
\end{equation}
Define right $S$-linear maps
\begin{equation}\label{eq:transported-dual-functionals}
\begin{aligned}
\varphi_0:M&\longrightarrow S,& a e_{11}+b e_{12}&\longmapsto a e_{11},\\
\varphi_1:M&\longrightarrow S,& a e_{11}+b e_{12}&\longmapsto b e_{22}
\quad(a,b\in\Bbbk).
\end{aligned}
\end{equation}
Their degrees in $M^{\grstar}$ are $0,-1$, respectively, and
\[
\alpha_M(e_{12}\varphi_1)(e_{11})
=\alpha_M(\varphi_1)(e_{12})=c_2,
\qquad e_{12}\varphi_1=\frac{c_2}{c_1}\varphi_0.
\]
Thus changing the form can change the action on the same vector space. Two choices give isomorphic $A$-modules by composing their identifications with $\bbD(M)$.\comm{make this an exercise (hide the solution); exercise should also give two different choices of symmeterising form and ask for how things change; prepare full solution to this.}
\end{example}

```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
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

[Back to the replacement index](#replacement-index)

---

<a id="replacement-9"></a>

## Replacement 9: State the purpose of the bimodule-block example first

**Source location:** [line 1192](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1192)  
**Purpose:** Explain what the example computes before introducing its matrix notation.  
**Dependencies:** Independent

### Line-by-Line Diff

**Added:** `+2` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1192 +1331,2 @@
-\begin{example}\label{ex:dual-blocks}\comm{starting saying the purpose of the example first.}
+\begin{example}\label{ex:dual-blocks}
+We compute how duality transposes bimodule blocks and how one linear functional gives different left and right $S$-linear maps.
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
\begin{example}\label{ex:dual-blocks}\comm{starting saying the purpose of the example first.}
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
\begin{example}\label{ex:dual-blocks}
We compute how duality transposes bimodule blocks and how one linear functional gives different left and right $S$-linear maps.
```

</details>

[Back to the replacement index](#replacement-index)

---

<a id="replacement-10"></a>

## Replacement 10: Replace the vague conclusion by identities between maps

**Source location:** [line 1235](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1235)  
**Purpose:** Distinguish the two S-valued maps in their common underlying Hom space, and state explicitly that composing either with the form gives the original functional.  
**Dependencies:** Independent

### Line-by-Line Diff

**Added:** `+8` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1235 +1375,8 @@
-Thus the same scalar-valued functional corresponds to distinct $S$-valued maps on the two sides.\comm{this sentence is hard to read, use symbols, not words.}
+As $\Bbbk$-linear maps $V\to S$,
+\[
+\alpha_V^{-1}(\varepsilon)\neq\beta_V^{-1}(\varepsilon),
+\qquad
+\tau\circ\alpha_V^{-1}(\varepsilon)
+=\varepsilon
+=\tau\circ\beta_V^{-1}(\varepsilon).
+\]
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
Thus the same scalar-valued functional corresponds to distinct $S$-valued maps on the two sides.\comm{this sentence is hard to read, use symbols, not words.}
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
As $\Bbbk$-linear maps $V\to S$,
\[
\alpha_V^{-1}(\varepsilon)\neq\beta_V^{-1}(\varepsilon),
\qquad
\tau\circ\alpha_V^{-1}(\varepsilon)
=\varepsilon
=\tau\circ\beta_V^{-1}(\varepsilon).
\]
```

</details>

[Back to the replacement index](#replacement-index)

---

<a id="replacement-11"></a>

## Replacement 11: Keep the full tensor-direct product proposition in advanced material

**Source location:** [line 1418](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1418)  
**Purpose:** Retain both comparison maps, the finite-product case, the finite-summand criterion, and the semisimple injectivity and isomorphism statements, but enclose the entire proposition, proof, and discussion in an advanced block. The main exposition continues to use direct sums.  
**Dependencies:** Requires 2

### Line-by-Line Diff

**Added:** `+56` lines &nbsp; **Removed:** `-17` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1418,24 +1565,63 @@
 \begin{advanced}
+\begin{proposition}[Tensor products and direct products]\label{prop:tensor-direct-products}
+Let $S$ be a $\Bbbk$-algebra, $M,M_i$ right $S$-modules, and $N,N_i$ left $S$-modules, with $i\in I$.
+The coordinate projections define linear maps
+\begin{equation}\label{eq:module-tensor-products}
+\begin{aligned}
+\kappa_N:\Bigl(\prod_iM_i\Bigr)\otimes_S N
+&\longrightarrow\prod_i(M_i\otimes_S N),
+& (m_i)_i\otimes n&\longmapsto(m_i\otimes n)_i,\\
+\lambda_M:M\otimes_S\Bigl(\prod_iN_i\Bigr)
+&\longrightarrow\prod_i(M\otimes_S N_i),
+& m\otimes(n_i)_i&\longmapsto(m\otimes n_i)_i.
+\end{aligned}
+\end{equation}
+\begin{enumerate}
+\item If $I$ is finite, both maps are isomorphisms.
+\item The map $\kappa_N$ is an isomorphism if $N$ is a direct summand of $S^{\oplus r}$ as a left module for some finite $r$.
+The corresponding condition on the right module $M$ makes $\lambda_M$ an isomorphism.
+\item If $S$ is finite-dimensional semisimple, both maps are injective.
+Moreover, $\kappa_N$ is an isomorphism when $N$ is finite-dimensional, and $\lambda_M$ is an isomorphism when $M$ is finite-dimensional.
+\end{enumerate}
+\end{proposition}
+
+\begin{proof}
+The formulas in \eqref{eq:module-tensor-products} respect the tensor relations in Definition~\ref{def:module-tensor}, so both maps are well-defined.
+For finite $I$, products equal sums, and Lemma~\ref{lem:tensor-properties}(4) proves (1).
+
+For $N=S$, the map $\kappa_S$ is the identity on $\prod_iM_i$ under $m\otimes s\mapsto ms$.
+For $N=S^{\oplus r}$, both sides are $(\prod_iM_i)^{\oplus r}$, since a finite direct sum commutes with a direct product.
+If $N\oplus N'\cong S^{\oplus r}$, the comparison for $N\oplus N'$ is $\kappa_N\oplus\kappa_{N'}$.
+Its bijectivity implies the bijectivity of $\kappa_N$.
+This proves the assertion about $\kappa_N$ in (2).
+
+Now let $S$ be finite-dimensional semisimple.
+For finite-dimensional $N$, Corollary~\ref{cor:semisimple-summands} gives (2).
+For arbitrary $N$, take $z=\sum_{\ell=1}^r m^{(\ell)}\otimes n_\ell$ in $\Ker\kappa_N$ and set $N_0=\sum_{\ell=1}^r Sn_\ell$.
+The submodule $N_0$ is finite-dimensional and has a complement in $N$ by Theorem~\ref{thm:artin-wedderburn}.
+Thus the inclusions
+\[
+\Bigl(\prod_iM_i\Bigr)\otimes_S N_0
+\longrightarrow\Bigl(\prod_iM_i\Bigr)\otimes_S N,
+\qquad
+M_i\otimes_S N_0\longrightarrow M_i\otimes_S N
+\]
+are injective, by the direct sum formula in Lemma~\ref{lem:tensor-properties}(4).
+Regard $z$ as a tensor with second factors in $N_0$.
+The equality $\kappa_N(z)=0$ then gives $\kappa_{N_0}(z)=0$.
+Since $\kappa_{N_0}$ is an isomorphism, $z=0$.
+
+For $\lambda_M$, apply the same arguments over $S^\op$, using
+$N\otimes_{S^\op}M\cong M\otimes_S N$, $n\otimes m\mapsto m\otimes n$.
+\end{proof}
+
+The finite-dimensional hypothesis on the fixed factor cannot be dropped from the isomorphism assertion: Example~\ref{ex:tensor-product-product-failure} gives a non-surjective comparison even for vector spaces.
+Thus tensor products always distribute over direct sums, but not over arbitrary direct products.
+
 \begin{remark}\label{rem:infinite-products}
-For infinite families, $\Hom$ need not preserve direct sums in its second variable, and tensor product need not preserve direct products.
-
+For infinite families, $\Hom$ need not preserve direct sums in its second variable.
 For $M=\bigoplus_{i\geq1}\Bbbk v_i$, the identity $M\to M$ does not come from $\bigoplus_i\Hom_\Bbbk(M,\Bbbk v_i)$: its projection onto every $\Bbbk v_i$ is non-zero.
 Thus the injection in Lemma~\ref{lem:hom-sums-products} need not be surjective.
-
-For right $S$-modules $M_i$ and a left $S$-module $N$, the coordinate projections give a natural map
-\[
-\Bigl(\prod_iM_i\Bigr)\otimes_S N
-\longrightarrow\prod_i(M_i\otimes_S N),
-\qquad (m_i)_i\otimes n\longmapsto(m_i\otimes n)_i,
-\]
-but not always an isomorphism.
-For vector spaces, take $M_i=\Bbbk$ for $i\geq1$ and $N=\bigoplus_{j\geq1}\Bbbk v_j$.
-Every element in the image is a sequence whose entries lie in a common finite-dimensional subspace of $N$: a tensor is a finite sum $\sum_{\ell=1}^r(c_i^{(\ell)})_i\otimes n_\ell$, whose $i$th entry is $\sum_{\ell=1}^r c_i^{(\ell)}n_\ell$.
-The sequence $(v_i)_i\in\prod_iN$ is therefore not in the image.
-
-If $N$ is a direct summand of $S^{\oplus r}$ as a left module for some finite $r$, the tensor comparison is an isomorphism.
-For $N=S$, both sides are $\prod_iM_i$ under $m\otimes s\mapsto ms$; finite direct sums and direct summands preserve this conclusion.
-In particular, Corollary~\ref{cor:semisimple-summands} applies when $S$ is finite-dimensional semisimple and $N$ is finite-dimensional.
 
 A product in the source of $\Hom$ behaves differently from a product in the target.
 For example, a linear map $\prod_{i\geq1}\Bbbk\to\Bbbk$ need not be determined by its restrictions to the coordinate copies of $\Bbbk$.
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
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

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
\begin{advanced}
\begin{proposition}[Tensor products and direct products]\label{prop:tensor-direct-products}
Let $S$ be a $\Bbbk$-algebra, $M,M_i$ right $S$-modules, and $N,N_i$ left $S$-modules, with $i\in I$.
The coordinate projections define linear maps
\begin{equation}\label{eq:module-tensor-products}
\begin{aligned}
\kappa_N:\Bigl(\prod_iM_i\Bigr)\otimes_S N
&\longrightarrow\prod_i(M_i\otimes_S N),
& (m_i)_i\otimes n&\longmapsto(m_i\otimes n)_i,\\
\lambda_M:M\otimes_S\Bigl(\prod_iN_i\Bigr)
&\longrightarrow\prod_i(M\otimes_S N_i),
& m\otimes(n_i)_i&\longmapsto(m\otimes n_i)_i.
\end{aligned}
\end{equation}
\begin{enumerate}
\item If $I$ is finite, both maps are isomorphisms.
\item The map $\kappa_N$ is an isomorphism if $N$ is a direct summand of $S^{\oplus r}$ as a left module for some finite $r$.
The corresponding condition on the right module $M$ makes $\lambda_M$ an isomorphism.
\item If $S$ is finite-dimensional semisimple, both maps are injective.
Moreover, $\kappa_N$ is an isomorphism when $N$ is finite-dimensional, and $\lambda_M$ is an isomorphism when $M$ is finite-dimensional.
\end{enumerate}
\end{proposition}

\begin{proof}
The formulas in \eqref{eq:module-tensor-products} respect the tensor relations in Definition~\ref{def:module-tensor}, so both maps are well-defined.
For finite $I$, products equal sums, and Lemma~\ref{lem:tensor-properties}(4) proves (1).

For $N=S$, the map $\kappa_S$ is the identity on $\prod_iM_i$ under $m\otimes s\mapsto ms$.
For $N=S^{\oplus r}$, both sides are $(\prod_iM_i)^{\oplus r}$, since a finite direct sum commutes with a direct product.
If $N\oplus N'\cong S^{\oplus r}$, the comparison for $N\oplus N'$ is $\kappa_N\oplus\kappa_{N'}$.
Its bijectivity implies the bijectivity of $\kappa_N$.
This proves the assertion about $\kappa_N$ in (2).

Now let $S$ be finite-dimensional semisimple.
For finite-dimensional $N$, Corollary~\ref{cor:semisimple-summands} gives (2).
For arbitrary $N$, take $z=\sum_{\ell=1}^r m^{(\ell)}\otimes n_\ell$ in $\Ker\kappa_N$ and set $N_0=\sum_{\ell=1}^r Sn_\ell$.
The submodule $N_0$ is finite-dimensional and has a complement in $N$ by Theorem~\ref{thm:artin-wedderburn}.
Thus the inclusions
\[
\Bigl(\prod_iM_i\Bigr)\otimes_S N_0
\longrightarrow\Bigl(\prod_iM_i\Bigr)\otimes_S N,
\qquad
M_i\otimes_S N_0\longrightarrow M_i\otimes_S N
\]
are injective, by the direct sum formula in Lemma~\ref{lem:tensor-properties}(4).
Regard $z$ as a tensor with second factors in $N_0$.
The equality $\kappa_N(z)=0$ then gives $\kappa_{N_0}(z)=0$.
Since $\kappa_{N_0}$ is an isomorphism, $z=0$.

For $\lambda_M$, apply the same arguments over $S^\op$, using
$N\otimes_{S^\op}M\cong M\otimes_S N$, $n\otimes m\mapsto m\otimes n$.
\end{proof}

The finite-dimensional hypothesis on the fixed factor cannot be dropped from the isomorphism assertion: Example~\ref{ex:tensor-product-product-failure} gives a non-surjective comparison even for vector spaces.
Thus tensor products always distribute over direct sums, but not over arbitrary direct products.

\begin{remark}\label{rem:infinite-products}
For infinite families, $\Hom$ need not preserve direct sums in its second variable.
For $M=\bigoplus_{i\geq1}\Bbbk v_i$, the identity $M\to M$ does not come from $\bigoplus_i\Hom_\Bbbk(M,\Bbbk v_i)$: its projection onto every $\Bbbk v_i$ is non-zero.
Thus the injection in Lemma~\ref{lem:hom-sums-products} need not be surjective.

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
