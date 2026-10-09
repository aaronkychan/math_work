# Change Proposal 8: Lectures 2 and 3

> **Applied on 9 October 2026.** All eight approved replacements are in the TeX source, and the PDF has been updated. The passages below preserve the revised proposal; the earlier version identifying the generating spaces at the outset was not applied.

**Prepared and revised:** 9 October 2026  
**Source:** [2026_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1884)  
**Total:** `+45` added lines, `-37` removed lines

## Scope

Introduce $\operatorname{Sym}(V)$ and $\bigwedge W$ independently:
- $V$ has basis $x_1,\ldots,x_n$.
- $W$ has basis $y_1,\ldots,y_m$.
- No pairing, identification, or equality of dimensions is assumed.

The Lecture 2 orthogonal-complement example computes the two annihilators separately, in the tensor squares of $D(V)$ and $D(W)$.

In Lecture 3, the quadratic-dual calculation gives
$$
\operatorname{Sym}(V)^!\cong\bigwedge D(V),
\qquad
\bigl(\bigwedge W\bigr)^!\cong\operatorname{Sym}(D(W)).
$$
**Only then** take $W=D(V)$ and $y_i=x_i^*$ to obtain the symmetric/exterior dual pair. Evaluation $D(D(V))\cong V$ gives the reverse identification.

## Replacements

| Replacement | Lecture | Change |
| --- | --- | --- |
| [1](#replacement-1-introduce-independent-generating-spaces) | 2 | Introduce Independent Generating Spaces |
| [2](#replacement-2-locate-the-two-relation-spaces) | 2 | Locate the Two Relation Spaces |
| [3](#replacement-3-keep-the-hilbert-series-dimensions-separate) | 2 | Keep the Hilbert Series Dimensions Separate |
| [4](#replacement-4-compute-the-orthogonal-complements-separately) | 2 | Compute the Orthogonal Complements Separately |
| [5](#replacement-5-keep-the-exercise-dimensions-separate) | 2 | Keep the Exercise Dimensions Separate |
| [6](#replacement-6-identify-the-dual-pair-after-computing) | 3 | Identify the Dual Pair After Computing |
| [7](#replacement-7-use-the-identified-pair-in-the-tensor-calculation) | 3 | Use the Identified Pair in the Tensor Calculation |
| [8](#replacement-8-specify-the-pair-in-the-hilbert-series-identity) | 3 | Specify the Pair in the Hilbert Series Identity |

**Dependency:** Apply all eight replacements together. The computations and exercises use the independent spaces introduced in Replacement 1; Replacement 6 explains when they form a dual pair.

**Diff legend:** `-` removes a line; `+` adds a line; a leading space retains context. Old line numbers refer to the current source; new line numbers include the preceding replacements.

---

## Replacement 1: Introduce Independent Generating Spaces

**Source:** [Lecture 2, line 1884](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1884)  
**Added:** `+9` lines  
**Removed:** `-9` lines

Define $\operatorname{Sym}(V)$ using $x_1,\ldots,x_n$ and $\bigwedge W$ using $y_1,\ldots,y_m$. There is no pairing or identification between $V$ and $W$, and their dimensions may differ.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1884,20 +1884,20 @@
 \begin{example}[Polynomial and exterior algebras]\label{ex:polynomial-exterior}
-Let $V$ be a finite-dimensional vector space with basis $x_1,\ldots,x_n$.
-The \defn{symmetric algebra} and \defn{exterior algebra} are
+Let $V,W$ be finite-dimensional vector spaces with bases $x_1,\ldots,x_n$ and $y_1,\ldots,y_m$, respectively.
+The \defn{symmetric algebra} of $V$ and the \defn{exterior algebra} of $W$ are
 \begin{equation}\label{eq:polynomial-exterior}
 \begin{aligned}
 \Symm(V)&=T_\Bbbk(V)/(x_ix_j-x_jx_i\mid i<j)
             \cong\Bbbk[x_1,\ldots,x_n],\\
-\bigwedge V&=T_\Bbbk(V)/(v^2\mid v\in V).
+\bigwedge W&=T_\Bbbk(W)/(w^2\mid w\in W).
 \end{aligned}
 \end{equation}
-Both algebras have degree $0$ component $\Bbbk$, degree $1$ component $V$, and are generated in degree $1$: their elements are linear combinations of products of the images of the $x_i$.
-The polynomial basis allows repetitions; the exterior basis consists of $1$ and $x_{i_1}\cdots x_{i_d}$ with $i_1<\cdots<i_d$.
-The exterior relations are equivalently $x_i^2=0$ for $1\leq i\leq n$ and $x_ix_j+x_jx_i=0$ for $i<j$, in every characteristic.
+Both algebras have degree $0$ component $\Bbbk$ and are generated in degree $1$, with degree $1$ components $V$ and $W$, respectively.
+The polynomial basis allows repetitions; the exterior basis consists of $1$ and $y_{j_1}\cdots y_{j_d}$ with $j_1<\cdots<j_d$.
+The exterior relations are equivalently $y_j^2=0$ for $1\leq j\leq m$ and $y_iy_j+y_jy_i=0$ for $i<j$, in every characteristic.
 \end{example}
 
 The bases in Example~\ref{ex:polynomial-exterior} can be checked directly.
 For $\Symm(V)$, commuting adjacent generators gives the ordered monomials, which are independent under the map to the polynomial ring.
-For $\bigwedge V$, the relations reduce every word to a multiple of a strictly increasing word or to zero.
-To prove independence in degree $d$, fix $i_1<\cdots<i_d$ and send $v_1\otimes\cdots\otimes v_d$ to the determinant of their coordinates in rows $i_1,\ldots,i_d$.
-This functional vanishes on tensors with two equal adjacent factors, hence on the degree $d$ part of $(v^2\mid v\in V)$. On increasing basis words it is $1$ on $x_{i_1}\cdots x_{i_d}$ and $0$ on the others, proving independence in every characteristic.
+For $\bigwedge W$, the relations reduce every word to a multiple of a strictly increasing word or to zero.
+To prove independence in degree $d$, fix $j_1<\cdots<j_d$ and use the linear functional $W^{\otimes_\Bbbk d}\to\Bbbk$ sending $w_1\otimes\cdots\otimes w_d$ to the determinant of their coordinates in rows $j_1,\ldots,j_d$ relative to the basis $y_1,\ldots,y_m$.
+The determinant vanishes on tensors with two equal adjacent factors, hence on the degree $d$ part of $(w^2\mid w\in W)$. On increasing basis words it is $1$ on $y_{j_1}\cdots y_{j_d}$ and $0$ on the others, proving independence in every characteristic.
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
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

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{example}[Polynomial and exterior algebras]\label{ex:polynomial-exterior}
Let $V,W$ be finite-dimensional vector spaces with bases $x_1,\ldots,x_n$ and $y_1,\ldots,y_m$, respectively.
The \defn{symmetric algebra} of $V$ and the \defn{exterior algebra} of $W$ are
\begin{equation}\label{eq:polynomial-exterior}
\begin{aligned}
\Symm(V)&=T_\Bbbk(V)/(x_ix_j-x_jx_i\mid i<j)
            \cong\Bbbk[x_1,\ldots,x_n],\\
\bigwedge W&=T_\Bbbk(W)/(w^2\mid w\in W).
\end{aligned}
\end{equation}
Both algebras have degree $0$ component $\Bbbk$ and are generated in degree $1$, with degree $1$ components $V$ and $W$, respectively.
The polynomial basis allows repetitions; the exterior basis consists of $1$ and $y_{j_1}\cdots y_{j_d}$ with $j_1<\cdots<j_d$.
The exterior relations are equivalently $y_j^2=0$ for $1\leq j\leq m$ and $y_iy_j+y_jy_i=0$ for $i<j$, in every characteristic.
\end{example}

The bases in Example~\ref{ex:polynomial-exterior} can be checked directly.
For $\Symm(V)$, commuting adjacent generators gives the ordered monomials, which are independent under the map to the polynomial ring.
For $\bigwedge W$, the relations reduce every word to a multiple of a strictly increasing word or to zero.
To prove independence in degree $d$, fix $j_1<\cdots<j_d$ and use the linear functional $W^{\otimes_\Bbbk d}\to\Bbbk$ sending $w_1\otimes\cdots\otimes w_d$ to the determinant of their coordinates in rows $j_1,\ldots,j_d$ relative to the basis $y_1,\ldots,y_m$.
The determinant vanishes on tensors with two equal adjacent factors, hence on the degree $d$ part of $(w^2\mid w\in W)$. On increasing basis words it is $1$ on $y_{j_1}\cdots y_{j_d}$ and $0$ on the others, proving independence in every characteristic.
```

</details>

---

## Replacement 2: Locate the Two Relation Spaces

**Source:** [Lecture 2, line 2065](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2065)  
**Added:** `+1` lines  
**Removed:** `-1` lines

Locate the symmetric relations in $V\otimes_\Bbbk V$ and the exterior relations in $W\otimes_\Bbbk W$, without identifying the spaces.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2065,1 +2065,1 @@
-The symmetric and exterior algebras of Example~\ref{ex:polynomial-exterior} are quadratic: all defining relations in \eqref{eq:polynomial-exterior} belong to $V\otimes_\Bbbk V$.
+The symmetric and exterior algebras of Example~\ref{ex:polynomial-exterior} are quadratic: the defining relations in \eqref{eq:polynomial-exterior} belong to $V\otimes_\Bbbk V$ and $W\otimes_\Bbbk W$, respectively.
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
The symmetric and exterior algebras of Example~\ref{ex:polynomial-exterior} are quadratic: all defining relations in \eqref{eq:polynomial-exterior} belong to $V\otimes_\Bbbk V$.
```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
The symmetric and exterior algebras of Example~\ref{ex:polynomial-exterior} are quadratic: the defining relations in \eqref{eq:polynomial-exterior} belong to $V\otimes_\Bbbk V$ and $W\otimes_\Bbbk W$, respectively.
```

</details>

---

## Replacement 3: Keep the Hilbert Series Dimensions Separate

**Source:** [Lecture 2, line 2111](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2111)  
**Added:** `+2` lines  
**Removed:** `-2` lines

Use independent dimensions $n=\dim_\Bbbk V$ and $m=\dim_\Bbbk W$; equality of dimensions is not assumed.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2111,3 +2111,3 @@
 h_{\Symm(V)}(t)=\frac{1}{(1-t)^n},\qquad
-h_{\bigwedge V}(t)=(1+t)^n
-\quad\text{where }n=\dim_\Bbbk V.
+h_{\bigwedge W}(t)=(1+t)^m
+\quad\text{where }n=\dim_\Bbbk V,\ m=\dim_\Bbbk W.
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
h_{\Symm(V)}(t)=\frac{1}{(1-t)^n},\qquad
h_{\bigwedge V}(t)=(1+t)^n
\quad\text{where }n=\dim_\Bbbk V.
```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
h_{\Symm(V)}(t)=\frac{1}{(1-t)^n},\qquad
h_{\bigwedge W}(t)=(1+t)^m
\quad\text{where }n=\dim_\Bbbk V,\ m=\dim_\Bbbk W.
```

</details>

---

## Replacement 4: Compute the Orthogonal Complements Separately

**Source:** [Lecture 2, line 2228](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2228)  
**Added:** `+9` lines  
**Removed:** `-8` lines

Retain independent spaces in the two-generator calculation. Their orthogonal complements lie in the respective dual tensor squares; do not identify $W$ with $D(V)$ here.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2228,19 +2228,20 @@
 \begin{example}\label{ex:symmetric-orthogonals}
-For $\Symm(V)$ and $\bigwedge V$ in Example~\ref{ex:polynomial-exterior}, take $V=\Bbbk x\oplus\Bbbk y$.
-The relation spaces are
+We compute the orthogonal complements of the symmetric and exterior relation spaces separately.
+Take $V=\Bbbk x_1\oplus\Bbbk x_2$ and $W=\Bbbk y_1\oplus\Bbbk y_2$ in Example~\ref{ex:polynomial-exterior}.
+The relation spaces in $V\otimes_\Bbbk V$ and $W\otimes_\Bbbk W$, respectively, are
 \[
 \begin{aligned}
-R_{\Symm(V)}&=\Bbbk(x\otimes y-y\otimes x),\\
-R_{\bigwedge V}&=\Bbbk(x\otimes x)\oplus\Bbbk(y\otimes y)\oplus\Bbbk(x\otimes y+y\otimes x).
+R_{\Symm(V)}&=\Bbbk(x_1\otimes x_2-x_2\otimes x_1),\\
+R_{\bigwedge W}&=\Bbbk(y_1\otimes y_1)\oplus\Bbbk(y_2\otimes y_2)\oplus\Bbbk(y_1\otimes y_2+y_2\otimes y_1).
 \end{aligned}
 \]
-Let $x^*,y^*\in V^*$ be the coordinate functionals.
+Let $x_1^*,x_2^*$ and $y_1^*,y_2^*$ be the dual bases of $D(V)$ and $D(W)$, respectively.
 Under the tensor-dual identification \eqref{eq:tensor-evaluations},
 \[
 \begin{aligned}
-R_{\Symm(V)}^\perp&=\operatorname{span}_\Bbbk\{x^*\otimes x^*,\,y^*\otimes y^*,\,x^*\otimes y^*+y^*\otimes x^*\},\\
-R_{\bigwedge V}^\perp&=\Bbbk(x^*\otimes y^*-y^*\otimes x^*).
+R_{\Symm(V)}^\perp&=\operatorname{span}_\Bbbk\{x_1^*\otimes x_1^*,\,x_2^*\otimes x_2^*,\,x_1^*\otimes x_2^*+x_2^*\otimes x_1^*\},\\
+R_{\bigwedge W}^\perp&=\Bbbk(y_1^*\otimes y_2^*-y_2^*\otimes y_1^*).
 \end{aligned}
 \]
-Thus taking orthogonal complements exchanges the symmetric and exterior relation spaces.
+The first space consists of the exterior relations on $D(V)$; the second consists of the symmetric relations on $D(W)$.
 \end{example}
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:symmetric-orthogonals}
For $\Symm(V)$ and $\bigwedge V$ in Example~\ref{ex:polynomial-exterior}, take $V=\Bbbk x\oplus\Bbbk y$.
The relation spaces are
\[
\begin{aligned}
R_{\Symm(V)}&=\Bbbk(x\otimes y-y\otimes x),\\
R_{\bigwedge V}&=\Bbbk(x\otimes x)\oplus\Bbbk(y\otimes y)\oplus\Bbbk(x\otimes y+y\otimes x).
\end{aligned}
\]
Let $x^*,y^*\in V^*$ be the coordinate functionals.
Under the tensor-dual identification \eqref{eq:tensor-evaluations},
\[
\begin{aligned}
R_{\Symm(V)}^\perp&=\operatorname{span}_\Bbbk\{x^*\otimes x^*,\,y^*\otimes y^*,\,x^*\otimes y^*+y^*\otimes x^*\},\\
R_{\bigwedge V}^\perp&=\Bbbk(x^*\otimes y^*-y^*\otimes x^*).
\end{aligned}
\]
Thus taking orthogonal complements exchanges the symmetric and exterior relation spaces.
\end{example}
```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:symmetric-orthogonals}
We compute the orthogonal complements of the symmetric and exterior relation spaces separately.
Take $V=\Bbbk x_1\oplus\Bbbk x_2$ and $W=\Bbbk y_1\oplus\Bbbk y_2$ in Example~\ref{ex:polynomial-exterior}.
The relation spaces in $V\otimes_\Bbbk V$ and $W\otimes_\Bbbk W$, respectively, are
\[
\begin{aligned}
R_{\Symm(V)}&=\Bbbk(x_1\otimes x_2-x_2\otimes x_1),\\
R_{\bigwedge W}&=\Bbbk(y_1\otimes y_1)\oplus\Bbbk(y_2\otimes y_2)\oplus\Bbbk(y_1\otimes y_2+y_2\otimes y_1).
\end{aligned}
\]
Let $x_1^*,x_2^*$ and $y_1^*,y_2^*$ be the dual bases of $D(V)$ and $D(W)$, respectively.
Under the tensor-dual identification \eqref{eq:tensor-evaluations},
\[
\begin{aligned}
R_{\Symm(V)}^\perp&=\operatorname{span}_\Bbbk\{x_1^*\otimes x_1^*,\,x_2^*\otimes x_2^*,\,x_1^*\otimes x_2^*+x_2^*\otimes x_1^*\},\\
R_{\bigwedge W}^\perp&=\Bbbk(y_1^*\otimes y_2^*-y_2^*\otimes y_1^*).
\end{aligned}
\]
The first space consists of the exterior relations on $D(V)$; the second consists of the symmetric relations on $D(W)$.
\end{example}
```

</details>

---

## Replacement 5: Keep the Exercise Dimensions Separate

**Source:** [Lecture 2, line 2328](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2328)  
**Added:** `+2` lines  
**Removed:** `-2` lines

Use $W$ and its dimension $m$ for the exterior-algebra calculation.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2328,3 +2329,3 @@
 \dim_\Bbbk\Symm(V)_2=\frac{n(n+1)}2,\qquad
-\dim_\Bbbk(\bigwedge V)_2=\frac{n(n-1)}2
-\quad\text{where }n=\dim_\Bbbk V.
+\dim_\Bbbk(\bigwedge W)_2=\frac{m(m-1)}2
+\quad\text{where }n=\dim_\Bbbk V,\ m=\dim_\Bbbk W.
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\dim_\Bbbk\Symm(V)_2=\frac{n(n+1)}2,\qquad
\dim_\Bbbk(\bigwedge V)_2=\frac{n(n-1)}2
\quad\text{where }n=\dim_\Bbbk V.
```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\dim_\Bbbk\Symm(V)_2=\frac{n(n+1)}2,\qquad
\dim_\Bbbk(\bigwedge W)_2=\frac{m(m-1)}2
\quad\text{where }n=\dim_\Bbbk V,\ m=\dim_\Bbbk W.
```

</details>

---

## Replacement 6: Identify the Dual Pair After Computing

**Source:** [Lecture 3, line 2555](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2555)  
**Added:** `+14` lines  
**Removed:** `-8` lines

Compute $\operatorname{Sym}(V)^!$ and $(\bigwedge W)^!$ for independent $V,W$. Only after the calculation, take $W=D(V)$ and $y_i=x_i^*$ to obtain a dual pair.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2555,19 +2556,25 @@
 \begin{proposition}\label{prop:symmetric-exterior-dual}
-For a finite-dimensional $\Bbbk$-vector space $V$,
+For finite-dimensional $\Bbbk$-vector spaces $V,W$,
 \[
 \Symm(V)^!\cong\bigwedge D(V),\qquad
-\bigl(\bigwedge V\bigr)^!\cong\Symm(D(V)).
+\bigl(\bigwedge W\bigr)^!\cong\Symm(D(W)).
 \]
 \end{proposition}
 
 \begin{proof}
-Here $S=\Bbbk$ and $V^*=D(V)$. Choose a basis $x_1,\ldots,x_n$ of $V$, with coordinate functionals $x_1^*,\ldots,x_n^*$.
-The evaluation \eqref{eq:quadratic-pairings} reads
+For $\Symm(V)$, choose a basis $x_1,\ldots,x_n$ of $V$, with dual basis $x_1^*,\ldots,x_n^*$ of $D(V)$.
+Here $S=\Bbbk$, and the evaluation \eqref{eq:quadratic-pairings} reads
 \[
 \theta_r(x_j^*\otimes x_i^*)(x_p\otimes x_q)=\delta_{ip}\delta_{jq}.
 \]
-For $F=\sum_{i,j}c_{ij}x_i^*\otimes x_j^*$, vanishing on each $x_p\otimes x_q-x_q\otimes x_p$ is equivalent to $c_{pq}=c_{qp}$.
-Thus the orthogonal complement of the symmetric relations is spanned by $(x_i^*)^2$ and $x_i^*x_j^*+x_j^*x_i^*$ for $i<j$, which are the exterior relations.
-Vanishing on the exterior relations instead gives $c_{ii}=0$ and $c_{pq}+c_{qp}=0$. The orthogonal complement is therefore spanned by $x_i^*x_j^*-x_j^*x_i^*$ for $i<j$.
-Now use the presentations in \eqref{eq:polynomial-exterior}.
+A tensor $\sum_{i,j=1}^n c_{ij}x_i^*\otimes x_j^*$ vanishes on each $x_p\otimes x_q-x_q\otimes x_p$ precisely when $c_{pq}=c_{qp}$ for $1\leq p<q\leq n$.
+Thus the orthogonal complement of the symmetric relations is spanned by $(x_i^*)^2$ for $1\leq i\leq n$ and $x_i^*x_j^*+x_j^*x_i^*$ for $1\leq i<j\leq n$, which are the exterior relations on $D(V)$.
+
+For $\bigwedge W$, choose a basis $y_1,\ldots,y_m$ of $W$, with dual basis $y_1^*,\ldots,y_m^*$ of $D(W)$.
+A tensor $\sum_{i,j=1}^m c_{ij}y_i^*\otimes y_j^*$ annihilates the exterior relations precisely when $c_{ii}=0$ for $1\leq i\leq m$ and $c_{pq}+c_{qp}=0$ for $1\leq p<q\leq m$.
+The orthogonal complement is therefore spanned by $y_i^*y_j^*-y_j^*y_i^*$ for $1\leq i<j\leq m$, which are the symmetric relations on $D(W)$.
+The presentations in \eqref{eq:polynomial-exterior} give both isomorphisms.
 \end{proof}
+
+Consequently, to pair $\Symm(V)$ with $\bigwedge W$ by quadratic duality, take $W=D(V)$ and $y_i=x_i^*$, so $m=n$.
+Evaluation $D(D(V))\cong V$ from Example~\ref{ex:linear-duality} then identifies $(\bigwedge W)^!$ with $\Symm(V)$.
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{proposition}\label{prop:symmetric-exterior-dual}
For a finite-dimensional $\Bbbk$-vector space $V$,
\[
\Symm(V)^!\cong\bigwedge D(V),\qquad
\bigl(\bigwedge V\bigr)^!\cong\Symm(D(V)).
\]
\end{proposition}

\begin{proof}
Here $S=\Bbbk$ and $V^*=D(V)$. Choose a basis $x_1,\ldots,x_n$ of $V$, with coordinate functionals $x_1^*,\ldots,x_n^*$.
The evaluation \eqref{eq:quadratic-pairings} reads
\[
\theta_r(x_j^*\otimes x_i^*)(x_p\otimes x_q)=\delta_{ip}\delta_{jq}.
\]
For $F=\sum_{i,j}c_{ij}x_i^*\otimes x_j^*$, vanishing on each $x_p\otimes x_q-x_q\otimes x_p$ is equivalent to $c_{pq}=c_{qp}$.
Thus the orthogonal complement of the symmetric relations is spanned by $(x_i^*)^2$ and $x_i^*x_j^*+x_j^*x_i^*$ for $i<j$, which are the exterior relations.
Vanishing on the exterior relations instead gives $c_{ii}=0$ and $c_{pq}+c_{qp}=0$. The orthogonal complement is therefore spanned by $x_i^*x_j^*-x_j^*x_i^*$ for $i<j$.
Now use the presentations in \eqref{eq:polynomial-exterior}.
\end{proof}
```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{proposition}\label{prop:symmetric-exterior-dual}
For finite-dimensional $\Bbbk$-vector spaces $V,W$,
\[
\Symm(V)^!\cong\bigwedge D(V),\qquad
\bigl(\bigwedge W\bigr)^!\cong\Symm(D(W)).
\]
\end{proposition}

\begin{proof}
For $\Symm(V)$, choose a basis $x_1,\ldots,x_n$ of $V$, with dual basis $x_1^*,\ldots,x_n^*$ of $D(V)$.
Here $S=\Bbbk$, and the evaluation \eqref{eq:quadratic-pairings} reads
\[
\theta_r(x_j^*\otimes x_i^*)(x_p\otimes x_q)=\delta_{ip}\delta_{jq}.
\]
A tensor $\sum_{i,j=1}^n c_{ij}x_i^*\otimes x_j^*$ vanishes on each $x_p\otimes x_q-x_q\otimes x_p$ precisely when $c_{pq}=c_{qp}$ for $1\leq p<q\leq n$.
Thus the orthogonal complement of the symmetric relations is spanned by $(x_i^*)^2$ for $1\leq i\leq n$ and $x_i^*x_j^*+x_j^*x_i^*$ for $1\leq i<j\leq n$, which are the exterior relations on $D(V)$.

For $\bigwedge W$, choose a basis $y_1,\ldots,y_m$ of $W$, with dual basis $y_1^*,\ldots,y_m^*$ of $D(W)$.
A tensor $\sum_{i,j=1}^m c_{ij}y_i^*\otimes y_j^*$ annihilates the exterior relations precisely when $c_{ii}=0$ for $1\leq i\leq m$ and $c_{pq}+c_{qp}=0$ for $1\leq p<q\leq m$.
The orthogonal complement is therefore spanned by $y_i^*y_j^*-y_j^*y_i^*$ for $1\leq i<j\leq m$, which are the symmetric relations on $D(W)$.
The presentations in \eqref{eq:polynomial-exterior} give both isomorphisms.
\end{proof}

Consequently, to pair $\Symm(V)$ with $\bigwedge W$ by quadratic duality, take $W=D(V)$ and $y_i=x_i^*$, so $m=n$.
Evaluation $D(D(V))\cong V$ from Example~\ref{ex:linear-duality} then identifies $(\bigwedge W)^!$ with $\Symm(V)$.
```

</details>

---

## Replacement 7: Use the Identified Pair in the Tensor Calculation

**Source:** [Lecture 3, line 2699](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2699)  
**Added:** `+7` lines  
**Removed:** `-6` lines

After the quadratic-duality result, use $W=D(V)$ with dual bases $x_1,x_2$ and $y_1,y_2$ in the existing calculation of the tensor-product sign.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2699,12 +2706,13 @@
 \begin{example}\label{ex:essential-tensor-sign}
-For $V=\Bbbk x\oplus\Bbbk y$, Proposition~\ref{prop:dual-tensor-products} gives
+The symmetric/exterior pair shows that the sign in a graded tensor product cannot always be omitted.
+Let $V=\Bbbk x_1\oplus\Bbbk x_2$ and let $y_1,y_2$ be the dual basis of $W=D(V)$. Proposition~\ref{prop:dual-tensor-products} gives
 \[
 \Symm(V)^!
-\cong\bigl(\Bbbk[x]\otimes_\Bbbk\Bbbk[y]\bigr)^!
-\cong\frac{\Bbbk[x^*]}{((x^*)^2)}\otimes_\Bbbk^{\mathrm{gr}}
-       \frac{\Bbbk[y^*]}{((y^*)^2)}
-\cong\bigwedge D(V).
+\cong\bigl(\Bbbk[x_1]\otimes_\Bbbk\Bbbk[x_2]\bigr)^!
+\cong\frac{\Bbbk[y_1]}{(y_1^2)}\otimes_\Bbbk^{\mathrm{gr}}
+       \frac{\Bbbk[y_2]}{(y_2^2)}
+\cong\bigwedge W.
 \]
-If $\Char\Bbbk\neq2$, the ordinary tensor product of the two square-zero algebras is commutative, whereas the graded tensor product is not: $x^*y^*=-y^*x^*\neq0$.
+If $\Char\Bbbk\neq2$, the ordinary tensor product of the two square-zero algebras is commutative, whereas the graded tensor product is not: $y_1y_2=-y_2y_1\neq0$.
 They are therefore not isomorphic. This sign cannot be removed by a change of generators.
 \end{example}
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:essential-tensor-sign}
For $V=\Bbbk x\oplus\Bbbk y$, Proposition~\ref{prop:dual-tensor-products} gives
\[
\Symm(V)^!
\cong\bigl(\Bbbk[x]\otimes_\Bbbk\Bbbk[y]\bigr)^!
\cong\frac{\Bbbk[x^*]}{((x^*)^2)}\otimes_\Bbbk^{\mathrm{gr}}
       \frac{\Bbbk[y^*]}{((y^*)^2)}
\cong\bigwedge D(V).
\]
If $\Char\Bbbk\neq2$, the ordinary tensor product of the two square-zero algebras is commutative, whereas the graded tensor product is not: $x^*y^*=-y^*x^*\neq0$.
They are therefore not isomorphic. This sign cannot be removed by a change of generators.
\end{example}
```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:essential-tensor-sign}
The symmetric/exterior pair shows that the sign in a graded tensor product cannot always be omitted.
Let $V=\Bbbk x_1\oplus\Bbbk x_2$ and let $y_1,y_2$ be the dual basis of $W=D(V)$. Proposition~\ref{prop:dual-tensor-products} gives
\[
\Symm(V)^!
\cong\bigl(\Bbbk[x_1]\otimes_\Bbbk\Bbbk[x_2]\bigr)^!
\cong\frac{\Bbbk[y_1]}{(y_1^2)}\otimes_\Bbbk^{\mathrm{gr}}
       \frac{\Bbbk[y_2]}{(y_2^2)}
\cong\bigwedge W.
\]
If $\Char\Bbbk\neq2$, the ordinary tensor product of the two square-zero algebras is commutative, whereas the graded tensor product is not: $y_1y_2=-y_2y_1\neq0$.
They are therefore not isomorphic. This sign cannot be removed by a change of generators.
\end{example}
```

</details>

---

## Replacement 8: Specify the Pair in the Hilbert Series Identity

**Source:** [Lecture 3, line 2742](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2742)  
**Added:** `+1` lines  
**Removed:** `-1` lines

Tie the scalar identity to the computed quadratic dual, rather than to arbitrary independent $V,W$.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2742,1 +2750,1 @@
-For the polynomial and exterior pair, the scalar instance is $(1-t)^{-n}(1-t)^n=1$.
+For $\Symm(V)$ and its quadratic dual $\bigwedge D(V)$, with $n=\dim_\Bbbk V$, the scalar instance is $(1-t)^{-n}(1-t)^n=1$.
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
For the polynomial and exterior pair, the scalar instance is $(1-t)^{-n}(1-t)^n=1$.
```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
For $\Symm(V)$ and its quadratic dual $\bigwedge D(V)$, with $n=\dim_\Bbbk V$, the scalar instance is $(1-t)^{-n}(1-t)^n=1$.
```

</details>

---

## Checks

**Checked:**
- Every existing passage matches the current source exactly.
- The initial definitions, Hilbert series, and exercise keep $V,W$ and $n,m$ independent.
- The Lecture 2 annihilator calculation uses separate dual bases and does not identify $W$ with $D(V)$.
- The choice $W=D(V)$ is made only after the Lecture 3 quadratic-dual calculation.
- The orthogonal complements agree with the reverse-order tensor evaluation, including in characteristic $2$.
- Existing labels, comments, and hidden-content settings are preserved.

**Completed:** Applied the eight replacements exactly and verified that all other TeX content and labels are unchanged. Both compilation checks succeeded with the existing hidden-content setting; the saved PDF has 36 pages. Visually checked pages 24, 27--29, 32--33, and 35--36. There are no unresolved references or new layout warnings; the pre-existing overfull line in Lecture 1 is unchanged. No document-opening or preview-opening action was used.
