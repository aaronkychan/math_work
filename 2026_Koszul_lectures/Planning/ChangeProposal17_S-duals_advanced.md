# Change Proposal 15: one-sided $S$-duals become advanced (Lectures 1–3)

> **Status: awaiting approval.** The proposed changes have already been applied to copies of the files and compiled; the copies are delivered alongside this proposal.

**Source:** the files produced by Change Proposal 14 (21 October 2026). Line numbers refer to those files.

## What changes

This proposal implements option (B) from Change Proposal 14, which your standing assumption $S=\bigoplus_i\Bbbk e_i$ makes possible:

- **The main text uses only the $\Bbbk$-linear duals $D$ and $\mathbb D$.** All one-sided $S$-dual material moves into advanced blocks: $M^*$, ${}^*N$, their graded versions, symmetrising forms, $\tau_S$, $\alpha$, $\beta$, $\theta_r$, $\theta_\ell$, Hom, evaluation and coevaluation, and the left/right quadratic duals.
- **A new choice-free tool replaces $\theta_r$:** $\theta:D(W)\otimes_S D(V)\cong D(V\otimes_S W)$, $\theta(\lambda\otimes\mu)(v\otimes w)=\sum_i\mu(ve_i)\lambda(e_iw)$ (Proposition `prop:D-tensor-duals`).
- **The quadratic dual is $A^!:=T_S(D(V))/(R^\perp)$, and $(A^!)^!\cong A$ holds canonically** (Theorem `thm:quadratic-involution`).
- **The one-sided definitions remain in advanced material.** They are shown to agree with the new $A^!$ under $\tau_S$.
- **General $S$ remarks** are added at the new $\theta$ and at the involution theorem. The existing ones at Hilbert series and the $\operatorname{Mat}_r$ example are unchanged.

**Notes:**
- The two *General $S$* remarks point into advanced material (`eq:tensor-duals`, `thm:quadratic-bidual`). These are pointers, not dependencies; no other main-text reference points into a box.
- Labels: no label was removed. `def:quadratic-duals`, `eq:quadratic-duals` and `lem:double-orthogonal` now refer to the $D$-based versions. The one-sided versions are renamed to `def:S-quadratic-duals`, `eq:S-quadratic-duals`, `lem:S-double-orthogonal` and `eq:S-bidual-tensor-square`. New labels: `eq:linear-bimodule-dual-action`, `eq:dual-blocks`, `rem:standard-form`, `prop:D-tensor-duals`, `eq:D-tensor-duals`, `def:D-orthogonal`, `thm:quadratic-involution`.
- **Please check S4/S5** for references to `def:quadratic-duals`, `lem:double-orthogonal`, $V^*$ or $\theta_r$, which may need the same $V^*\to D(V)$ treatment.

## Mechanical Corrections

| File | Current line | Change |
| --- | --- | --- |
| [Lecture_Koszul_S1.tex:1206](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1206) | 1206 | Delete the inner wrapper `\begin{advanced}` (Replacement 2). |
| [Lecture_Koszul_S1.tex:1216](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1216) | 1216 | Delete the inner wrapper `\end{advanced}` (Replacement 2). |
| [Lecture_Koszul_S1.tex:1230](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1230) | 1230 | Delete the inner wrapper `\begin{supplementary}` (Replacement 2). |
| [Lecture_Koszul_S1.tex:1289](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1289) | 1289 | Delete the inner wrapper `\end{supplementary}` (Replacement 2). |
| [Lecture_Koszul_S1.tex:1319](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1319) | 1319 | Delete the inner wrapper `\begin{advanced}` (Replacement 2). |
| [Lecture_Koszul_S1.tex:1420](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1420) | after 1420 | Insert `\begin{advanced}` before Exercise `ex:dual-blocks` (exercises on symmetrising forms). |
| [Lecture_Koszul_S1.tex:1535](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1535) | after 1535 | Insert `\end{advanced}` after the hidden solution of Exercise `ex:transported-dual-action`. |
| [Lecture_Koszul_S2.tex:356](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:356) | 356 | Delete the wrapper `\end{advanced}` (Replacement 3). |
| [Lecture_Koszul_S2.tex:379](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:379) | 379 | Delete the wrapper `\begin{advanced}` (Replacement 3). |
| [Lecture_Koszul_S2.tex:473](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:473) | 473 | Delete the wrapper `\begin{supplementary}` (Replacement 3). |
| [Lecture_Koszul_S2.tex:498](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:498) | 498 | Delete the wrapper `\end{supplementary}` (Replacement 3). |
| [Lecture_Koszul_S2.tex:524](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:524) | 524 | Delete the wrapper `\begin{supplementary}` (Replacement 3). |
| [Lecture_Koszul_S2.tex:531](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:531) | 531 | Delete the wrapper `\end{supplementary}` (Replacement 3). |
| [Lecture_Koszul_S2.tex:536](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:536) | 536 | Delete the wrapper `\begin{advanced}` (Replacement 3). |
| [Lecture_Koszul_S2.tex:1128](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:1128) | after 1128 | Insert `\begin{advanced}` before Exercise `ex:tensor-duality-proof` (anti-distributivity of the one-sided $S$-dual). |
| [Lecture_Koszul_S2.tex:1215](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:1215) | after 1215 | Insert `\end{advanced}` after its hidden solution. |
| [Lecture_Koszul.tex:354](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:354) | 354 | `; advanced` added to the $M^*,{}^*N$ entry. |
| [Lecture_Koszul.tex:355](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:355) | 355 | `; advanced` added to the graded $S$-dual entry. |
| [Lecture_Koszul.tex:358](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:358) | 358 | `; advanced` added to the $\tau$ entry. |
| [Lecture_Koszul.tex:359](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:359) | 359 | $\tau_S$ entry marked advanced; link to `rem:standard-form`. |
| [Lecture_Koszul.tex:360](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:360) | 360 | `; advanced` added to the $\alpha_M,\beta_N$ entry. |

## Replacement Index

| No. | Content change | Added / removed |
| --- | --- | --- |
| 1 | [Lecture 1: linear duals of bimodules in the main text; one-sided $S$-duals become advanced](#replacement-1) | +33 / -9 |
| 2 | [Lecture 1: the comparison of duals becomes an advanced subsection](#replacement-2) | +3 / -2 |
| 3 | [Lecture 2: one-sided $S$-dual material becomes advanced](#replacement-3) | +5 / -1 |
| 4 | [Lecture 2: duals of tensor products and orthogonal complements via $D$](#replacement-4) | +45 / -4 |
| 5 | [Lecture 3: the quadratic dual defined with $D$](#replacement-5) | +23 / -58 |
| 6 | [Lecture 3: $(A^!)^!\cong A$ with no choices; one-sided version advanced](#replacement-6) | +70 / -14 |
| 7 | [Lecture 3: dependent edits](#replacement-7) | +21 / -19 |
| 8 | [Main file: Convention sentence, drafting note and notation list](#replacement-8) | +25 / -16 |

---

<a id="replacement-1"></a>

## Replacement 1: Lecture 1: linear duals of bimodules in the main text; one-sided $S$-duals become advanced

The main text keeps only the $\Bbbk$-linear dual. It gains its bimodule structure (new label `eq:linear-bimodule-dual-action`) and the block description $e_jD(M)e_i\cong D(e_iMe_j)$ (new label `eq:dual-blocks`), which Lectures 2–3 use. The assumption no longer mentions $\tau_S$; the standard form is now defined in the advanced comparison subsection (Replacement 2). The one-sided $S$-duals (`def:S-duals`, the graded $S$-duals, `lem:S-bidual`, `eq:bimodule-dual-actions`) are moved verbatim into one advanced block, which merges with the existing advanced block on the two-sided dual. Their supplementary wrappers are dropped, because advanced blocks contain proofs directly. All labels are kept.

### Passage 1: subsection title

**Location:** [Lecture_Koszul_S1.tex:954](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:954) (current line 954)  
**Change size:** 1 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -954,1 +954,1 @@
-\subsection{\texorpdfstring{Left, right, and two-sided duals over $S$}{Left, right, and two-sided duals over S}}
+\subsection{\texorpdfstring{Linear duals of $S$-bimodules}{Linear duals of S-bimodules}}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\subsection{\texorpdfstring{Left, right, and two-sided duals over $S$}{Left, right, and two-sided duals over S}}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\subsection{\texorpdfstring{Linear duals of $S$-bimodules}{Linear duals of S-bimodules}}
```

</details>

### Passage 2: the assumption without $\tau_S$

**Location:** [Lecture_Koszul_S1.tex:960](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:960) (current lines 960–971)  
**Change size:** 2 lines added; 3 lines removed.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -960,12 +960,11 @@
 \begin{assumption}\label{ass:basic-semisimple}
 For simplicity, from now on and unless stated otherwise,
 \[
 S=\bigoplus_{i=1}^n\Bbbk e_i
 \]
 with coordinate idempotents $e_1,\ldots,e_n$.
-We write $\tau_S:S\to\Bbbk$, $\sum_{i=1}^na_ie_i\mapsto\sum_{i=1}^na_i$, for its \defn{standard symmetrising form}; see Definition~\ref{def:symmetrising-form} and Example~\ref{ex:symmetrising-form}.
 \end{assumption}
 
-The coordinate idempotents are the primitive idempotents of $S$, so $\tau_S$ involves no choice.
+The coordinate idempotents are the primitive idempotents of $S$, so they involve no choice.
 Statements already proved for an arbitrary finite-dimensional semisimple $S$ keep their generality.
-A remark headed \emph{General $S$} marks each place where an arbitrary finite-dimensional semisimple $S$ needs extra care, usually the choice of a symmetrising form.
+A remark headed \emph{General $S$} marks each place where an arbitrary finite-dimensional semisimple $S$ needs extra care; usually this means replacing the $\Bbbk$-linear dual by the one-sided $S$-duals of the advanced material below, or choosing a symmetrising form.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\begin{assumption}\label{ass:basic-semisimple}
For simplicity, from now on and unless stated otherwise,
\[
S=\bigoplus_{i=1}^n\Bbbk e_i
\]
with coordinate idempotents $e_1,\ldots,e_n$.
We write $\tau_S:S\to\Bbbk$, $\sum_{i=1}^na_ie_i\mapsto\sum_{i=1}^na_i$, for its \defn{standard symmetrising form}; see Definition~\ref{def:symmetrising-form} and Example~\ref{ex:symmetrising-form}.
\end{assumption}

The coordinate idempotents are the primitive idempotents of $S$, so $\tau_S$ involves no choice.
Statements already proved for an arbitrary finite-dimensional semisimple $S$ keep their generality.
A remark headed \emph{General $S$} marks each place where an arbitrary finite-dimensional semisimple $S$ needs extra care, usually the choice of a symmetrising form.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{assumption}\label{ass:basic-semisimple}
For simplicity, from now on and unless stated otherwise,
\[
S=\bigoplus_{i=1}^n\Bbbk e_i
\]
with coordinate idempotents $e_1,\ldots,e_n$.
\end{assumption}

The coordinate idempotents are the primitive idempotents of $S$, so they involve no choice.
Statements already proved for an arbitrary finite-dimensional semisimple $S$ keep their generality.
A remark headed \emph{General $S$} marks each place where an arbitrary finite-dimensional semisimple $S$ needs extra care; usually this means replacing the $\Bbbk$-linear dual by the one-sided $S$-duals of the advanced material below, or choosing a symmetrising form.
```

</details>

### Passage 3: $D$ on bimodules (main) and the one-sided $S$-duals (advanced)

**Location:** [Lecture_Koszul_S1.tex:975](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:975) (current lines 975–1106)  
**Change size:** 30 lines added; 5 lines removed.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -975,132 +974,157 @@
+For a bimodule ${}_SM_S$, the $\Bbbk$-linear dual retains both actions:
+\begin{equation}\label{eq:linear-bimodule-dual-action}
+(s\lambda t)(m)=\lambda(tms)\qquad(s,t\in S,\ \lambda\in D(M),\ m\in M).
+\end{equation}
+With precomposition on morphisms, we obtain functors
+\[
+D:(\Mod S^\en)^\op\longrightarrow\Mod S^\en,\qquad
+\bbD:(\Grmod S^\en)^\op\longrightarrow\Grmod S^\en,
+\]
+whose restrictions to finite-dimensional bimodules, and to locally finite-dimensional graded bimodules, are dualities by Lemma~\ref{lem:linear-bidual}.
+\begin{supplementary}
+Evaluation preserves both actions: for $m\in M$, $\lambda\in D(M)$, and $s,t\in S$,
+\[
+(s\,\mathrm{ev}_M(m)\,t)(\lambda)=\mathrm{ev}_M(m)(t\lambda s)=(t\lambda s)(m)=\lambda(smt)=\mathrm{ev}_M(smt)(\lambda).
+\]
+Applying this in each degree gives the graded statement.
+\end{supplementary}
+
+Dualising reverses the two idempotents: for $1\leq i,j\leq n$,
+\begin{equation}\label{eq:dual-blocks}
+e_jD(M)e_i=\{\lambda\in D(M)\mid\lambda(e_kMe_\ell)=0\text{ unless }(k,\ell)=(i,j)\}\cong D(e_iMe_j),
+\end{equation}
+since $(e_j\lambda e_i)(m)=\lambda(e_ime_j)$ by \eqref{eq:linear-bimodule-dual-action}.
+
+\begin{advanced}
+\emph{One-sided $S$-duals.}
+Under Assumption~\ref{ass:basic-semisimple}, the $\Bbbk$-linear dual is all we need.
+For an arbitrary finite-dimensional semisimple $S$, the choice-free substitutes are the one-sided $S$-duals below; they are the duals used in \cite[\S2.7]{BGS96}.
+Under Assumption~\ref{ass:basic-semisimple} they are canonically isomorphic to $D$; see Remark~\ref{rem:standard-form}.
+
 \begin{definition}\label{def:S-duals}
 For a right $S$-module $M$ and a left $S$-module $N$, define their \defn{$S$-duals} by
 \[
 \begin{aligned}
 M^*&:=\Hom_S(M,S)\in \Mod(S^\op),&
 (sf)(m)&:=sf(m),\\
 {}^*N&:=\Hom_{S^\op}(N,S) \in \Mod S,&
 (gs)(n)&:=g(n)s.
 \end{aligned}
 \]
 Here $s\in S$, $m\in M$, $n\in N$, $f\in M^*$, and $g\in{}^*N$.
 \end{definition}
 
 %The position of the star records the side of the original action: $f(ms)=f(m)s$ in $M^*$, whereas $g(sn)=sg(n)$ in $ {}^*N$.
 %\comm{why repeat what is already written????}
 
 Similar to $\Bbbk$-lienar duality, this definition extends to exact contravariant functors: for a right module map $u:M\to N$, define $u^*:N^*\to M^*$ by precomposition $u^*(f)=f\circ u$; for a left module map $u:M\to N$, the same recipe defines ${}^*u:{}^*N\to{}^*M$.
 This yields the desired functors
 \[
 (-)^*:(\Mod S)^\op\longrightarrow\Mod(S^\op),
 \qquad
 {}^*(-):(\Mod(S^\op))^\op\longrightarrow\Mod S.
 \]
 
 We also have graded analogue similar to Definition~\ref{def:linear-duals}.
 
 \begin{definition}\label{def:graded-S-duals}
 For graded right and left $S$-modules $M$, respectively, define their \defn{graded $S$-duals} by
 \[
 M^{\grstar}:=\bigoplus_{i\in\Z}(M_{-i})^*
 =\bigoplus_{i\in\Z}\Hom_S^{\Z}(M,S(i)),\qquad
 {}^{\grstar}M:=\bigoplus_{i\in\Z}{}^*(M_{-i})=\bigoplus_{i\in\Z}\Hom_{S^\op}^{\Z}(M,S(i)),
 \]
 
 where each indicated summand has degree $i$.
 %The shift is $S(i)$, since $S(i)_{-i}=S_0$.
 \end{definition}
 
 This also extends to a functor: for a degree $0$ right $S$-module map $u:M\to N$, define $u^{\grstar}:N^{\grstar}\to M^{\grstar}$ by
 \[
 (u^{\grstar})_i:(N_{-i})^*\longrightarrow(M_{-i})^*,
 \qquad f\longmapsto f\circ u|_{M_{-i}}
 \quad(i\in\Z).
 \]
 For a degree $0$ left module map $u:M\to N$, the same formula defines ${}^{\grstar}u:{}^{\grstar}N\to{}^{\grstar}M$.
 With the actions from Definition~\ref{def:S-duals}, we obtain functors
 \begin{equation}\label{eq:graded-S-dual-functors}
 (-)^{\grstar}:(\Grmod S)^\op\longrightarrow\Grmod(S^\op),\qquad 
 {}^{\grstar}(-):(\Grmod(S^\op))^\op\longrightarrow\Grmod S.
 \end{equation}
 
 Each functor in \eqref{eq:graded-S-dual-functors} restricts to locally finite-dimensional modules: replace $\Grmod$ by $\grmod$ in its source and target.
 Indeed, for $R=S$ or $S^\op$ and $M\in\grmod R$,
 \begin{equation}\label{eq:graded-S-dual-finiteness}
 \dim_\Bbbk\Hom_R(M_{-i},R)
 \leq(\dim_\Bbbk M_{-i})(\dim_\Bbbk R)<\infty
 \quad(i\in\Z).
 \end{equation}
 
 \begin{lemma}\label{lem:S-bidual}
 We have dualities
 \[
 \begin{aligned}
 (-)^*:(\mod S)^\op & \xrightarrow{\sim}\mod(S^\op), & {}^*(-):(\mod(S^\op))^\op &\xrightarrow{\sim}\mod S,\\
 (-)^{\grstar}:(\grmod S)^\op&\xrightarrow{\sim}\grmod(S^\op), &
 {}^{\grstar}(-):(\grmod(S^\op))^\op&\xrightarrow{\sim}\grmod S.
 \end{aligned}
 \]
 \end{lemma}
 
-\begin{supplementary}
 \begin{proof}
 We show that evaluation gives natural isomorphisms of functors
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
 
 For the graded cases, apply the ungraded case degree-wise.  Note that since $S$ is finite-dimensional, finitely generated $S$-module is the same as finite-dimensional $S$-modules.
 \end{proof}
-\end{supplementary}
 
 For a bimodule ${}_SM_S$, the linear and one-sided duals retain both actions:
 \begin{equation}\label{eq:bimodule-dual-actions}
 (s\lambda t)(m)=\lambda(tms),\qquad
 (sft)(m)=sf(tm),\qquad
 (sgt)(m)=g(ms)t,
 \end{equation}
 where $s,t\in S$, $m\in M$, $\lambda\in D(M)$, $f\in\Hom_S(M,S)$, and $g\in\Hom_{S^\op}(M,S)$.
 The functionals still take values in $\Bbbk$ or $S$.
 With precomposition on morphisms, we obtain
 \begin{equation}\label{eq:one-sided-bimodule-dual-functors}
 \begin{aligned}
 D,\ (-)^*,\ {}^*(-)&:(\Mod S^\en)^\op\longrightarrow\Mod S^\en,\\
 \bbD,\ (-)^{\grstar},\ {}^{\grstar}(-)&:(\Grmod S^\en)^\op\longrightarrow\Grmod S^\en.
 \end{aligned}
 \end{equation}
 The restrictions to finite-dimensional modules, and to locally finite-dimensional graded modules, are dualities by Lemmas~\ref{lem:linear-bidual} and~\ref{lem:S-bidual}.
-\begin{supplementary}
 Evaluation preserves both actions: for $m\in M$, $f\in M^*$, and $s,t\in S$,
 \[
 (s\,\mathrm{ev}_M(m)\,t)(f)
 =f(sm)t=f(smt)=\mathrm{ev}_M(smt)(f).
 \]
 The corresponding checks for $D$ and the left dual use the same evaluation formula; applying them in each degree gives the graded statements.
-\end{supplementary}
 
-\begin{advanced}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\begin{definition}\label{def:S-duals}
For a right $S$-module $M$ and a left $S$-module $N$, define their \defn{$S$-duals} by
\[
\begin{aligned}
M^*&:=\Hom_S(M,S)\in \Mod(S^\op),&
(sf)(m)&:=sf(m),\\
{}^*N&:=\Hom_{S^\op}(N,S) \in \Mod S,&
(gs)(n)&:=g(n)s.
\end{aligned}
\]
Here $s\in S$, $m\in M$, $n\in N$, $f\in M^*$, and $g\in{}^*N$.
\end{definition}

%The position of the star records the side of the original action: $f(ms)=f(m)s$ in $M^*$, whereas $g(sn)=sg(n)$ in $ {}^*N$.
%\comm{why repeat what is already written????}

Similar to $\Bbbk$-lienar duality, this definition extends to exact contravariant functors: for a right module map $u:M\to N$, define $u^*:N^*\to M^*$ by precomposition $u^*(f)=f\circ u$; for a left module map $u:M\to N$, the same recipe defines ${}^*u:{}^*N\to{}^*M$.
This yields the desired functors
\[
(-)^*:(\Mod S)^\op\longrightarrow\Mod(S^\op),
\qquad
{}^*(-):(\Mod(S^\op))^\op\longrightarrow\Mod S.
\]

We also have graded analogue similar to Definition~\ref{def:linear-duals}.

\begin{definition}\label{def:graded-S-duals}
For graded right and left $S$-modules $M$, respectively, define their \defn{graded $S$-duals} by
\[
M^{\grstar}:=\bigoplus_{i\in\Z}(M_{-i})^*
=\bigoplus_{i\in\Z}\Hom_S^{\Z}(M,S(i)),\qquad
{}^{\grstar}M:=\bigoplus_{i\in\Z}{}^*(M_{-i})=\bigoplus_{i\in\Z}\Hom_{S^\op}^{\Z}(M,S(i)),
\]

where each indicated summand has degree $i$.
%The shift is $S(i)$, since $S(i)_{-i}=S_0$.
\end{definition}

This also extends to a functor: for a degree $0$ right $S$-module map $u:M\to N$, define $u^{\grstar}:N^{\grstar}\to M^{\grstar}$ by
\[
(u^{\grstar})_i:(N_{-i})^*\longrightarrow(M_{-i})^*,
\qquad f\longmapsto f\circ u|_{M_{-i}}
\quad(i\in\Z).
\]
For a degree $0$ left module map $u:M\to N$, the same formula defines ${}^{\grstar}u:{}^{\grstar}N\to{}^{\grstar}M$.
With the actions from Definition~\ref{def:S-duals}, we obtain functors
\begin{equation}\label{eq:graded-S-dual-functors}
(-)^{\grstar}:(\Grmod S)^\op\longrightarrow\Grmod(S^\op),\qquad 
{}^{\grstar}(-):(\Grmod(S^\op))^\op\longrightarrow\Grmod S.
\end{equation}

Each functor in \eqref{eq:graded-S-dual-functors} restricts to locally finite-dimensional modules: replace $\Grmod$ by $\grmod$ in its source and target.
Indeed, for $R=S$ or $S^\op$ and $M\in\grmod R$,
\begin{equation}\label{eq:graded-S-dual-finiteness}
\dim_\Bbbk\Hom_R(M_{-i},R)
\leq(\dim_\Bbbk M_{-i})(\dim_\Bbbk R)<\infty
\quad(i\in\Z).
\end{equation}

\begin{lemma}\label{lem:S-bidual}
We have dualities
\[
\begin{aligned}
(-)^*:(\mod S)^\op & \xrightarrow{\sim}\mod(S^\op), & {}^*(-):(\mod(S^\op))^\op &\xrightarrow{\sim}\mod S,\\
(-)^{\grstar}:(\grmod S)^\op&\xrightarrow{\sim}\grmod(S^\op), &
{}^{\grstar}(-):(\grmod(S^\op))^\op&\xrightarrow{\sim}\grmod S.
\end{aligned}
\]
\end{lemma}

\begin{supplementary}
\begin{proof}
We show that evaluation gives natural isomorphisms of functors
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

For the graded cases, apply the ungraded case degree-wise.  Note that since $S$ is finite-dimensional, finitely generated $S$-module is the same as finite-dimensional $S$-modules.
\end{proof}
\end{supplementary}

For a bimodule ${}_SM_S$, the linear and one-sided duals retain both actions:
\begin{equation}\label{eq:bimodule-dual-actions}
(s\lambda t)(m)=\lambda(tms),\qquad
(sft)(m)=sf(tm),\qquad
(sgt)(m)=g(ms)t,
\end{equation}
where $s,t\in S$, $m\in M$, $\lambda\in D(M)$, $f\in\Hom_S(M,S)$, and $g\in\Hom_{S^\op}(M,S)$.
The functionals still take values in $\Bbbk$ or $S$.
With precomposition on morphisms, we obtain
\begin{equation}\label{eq:one-sided-bimodule-dual-functors}
\begin{aligned}
D,\ (-)^*,\ {}^*(-)&:(\Mod S^\en)^\op\longrightarrow\Mod S^\en,\\
\bbD,\ (-)^{\grstar},\ {}^{\grstar}(-)&:(\Grmod S^\en)^\op\longrightarrow\Grmod S^\en.
\end{aligned}
\end{equation}
The restrictions to finite-dimensional modules, and to locally finite-dimensional graded modules, are dualities by Lemmas~\ref{lem:linear-bidual} and~\ref{lem:S-bidual}.
\begin{supplementary}
Evaluation preserves both actions: for $m\in M$, $f\in M^*$, and $s,t\in S$,
\[
(s\,\mathrm{ev}_M(m)\,t)(f)
=f(sm)t=f(smt)=\mathrm{ev}_M(smt)(f).
\]
The corresponding checks for $D$ and the left dual use the same evaluation formula; applying them in each degree gives the graded statements.
\end{supplementary}

\begin{advanced}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
For a bimodule ${}_SM_S$, the $\Bbbk$-linear dual retains both actions:
\begin{equation}\label{eq:linear-bimodule-dual-action}
(s\lambda t)(m)=\lambda(tms)\qquad(s,t\in S,\ \lambda\in D(M),\ m\in M).
\end{equation}
With precomposition on morphisms, we obtain functors
\[
D:(\Mod S^\en)^\op\longrightarrow\Mod S^\en,\qquad
\bbD:(\Grmod S^\en)^\op\longrightarrow\Grmod S^\en,
\]
whose restrictions to finite-dimensional bimodules, and to locally finite-dimensional graded bimodules, are dualities by Lemma~\ref{lem:linear-bidual}.
\begin{supplementary}
Evaluation preserves both actions: for $m\in M$, $\lambda\in D(M)$, and $s,t\in S$,
\[
(s\,\mathrm{ev}_M(m)\,t)(\lambda)=\mathrm{ev}_M(m)(t\lambda s)=(t\lambda s)(m)=\lambda(smt)=\mathrm{ev}_M(smt)(\lambda).
\]
Applying this in each degree gives the graded statement.
\end{supplementary}

Dualising reverses the two idempotents: for $1\leq i,j\leq n$,
\begin{equation}\label{eq:dual-blocks}
e_jD(M)e_i=\{\lambda\in D(M)\mid\lambda(e_kMe_\ell)=0\text{ unless }(k,\ell)=(i,j)\}\cong D(e_iMe_j),
\end{equation}
since $(e_j\lambda e_i)(m)=\lambda(e_ime_j)$ by \eqref{eq:linear-bimodule-dual-action}.

\begin{advanced}
\emph{One-sided $S$-duals.}
Under Assumption~\ref{ass:basic-semisimple}, the $\Bbbk$-linear dual is all we need.
For an arbitrary finite-dimensional semisimple $S$, the choice-free substitutes are the one-sided $S$-duals below; they are the duals used in \cite[\S2.7]{BGS96}.
Under Assumption~\ref{ass:basic-semisimple} they are canonically isomorphic to $D$; see Remark~\ref{rem:standard-form}.

\begin{definition}\label{def:S-duals}
For a right $S$-module $M$ and a left $S$-module $N$, define their \defn{$S$-duals} by
\[
\begin{aligned}
M^*&:=\Hom_S(M,S)\in \Mod(S^\op),&
(sf)(m)&:=sf(m),\\
{}^*N&:=\Hom_{S^\op}(N,S) \in \Mod S,&
(gs)(n)&:=g(n)s.
\end{aligned}
\]
Here $s\in S$, $m\in M$, $n\in N$, $f\in M^*$, and $g\in{}^*N$.
\end{definition}

%The position of the star records the side of the original action: $f(ms)=f(m)s$ in $M^*$, whereas $g(sn)=sg(n)$ in $ {}^*N$.
%\comm{why repeat what is already written????}

Similar to $\Bbbk$-lienar duality, this definition extends to exact contravariant functors: for a right module map $u:M\to N$, define $u^*:N^*\to M^*$ by precomposition $u^*(f)=f\circ u$; for a left module map $u:M\to N$, the same recipe defines ${}^*u:{}^*N\to{}^*M$.
This yields the desired functors
\[
(-)^*:(\Mod S)^\op\longrightarrow\Mod(S^\op),
\qquad
{}^*(-):(\Mod(S^\op))^\op\longrightarrow\Mod S.
\]

We also have graded analogue similar to Definition~\ref{def:linear-duals}.

\begin{definition}\label{def:graded-S-duals}
For graded right and left $S$-modules $M$, respectively, define their \defn{graded $S$-duals} by
\[
M^{\grstar}:=\bigoplus_{i\in\Z}(M_{-i})^*
=\bigoplus_{i\in\Z}\Hom_S^{\Z}(M,S(i)),\qquad
{}^{\grstar}M:=\bigoplus_{i\in\Z}{}^*(M_{-i})=\bigoplus_{i\in\Z}\Hom_{S^\op}^{\Z}(M,S(i)),
\]

where each indicated summand has degree $i$.
%The shift is $S(i)$, since $S(i)_{-i}=S_0$.
\end{definition}

This also extends to a functor: for a degree $0$ right $S$-module map $u:M\to N$, define $u^{\grstar}:N^{\grstar}\to M^{\grstar}$ by
\[
(u^{\grstar})_i:(N_{-i})^*\longrightarrow(M_{-i})^*,
\qquad f\longmapsto f\circ u|_{M_{-i}}
\quad(i\in\Z).
\]
For a degree $0$ left module map $u:M\to N$, the same formula defines ${}^{\grstar}u:{}^{\grstar}N\to{}^{\grstar}M$.
With the actions from Definition~\ref{def:S-duals}, we obtain functors
\begin{equation}\label{eq:graded-S-dual-functors}
(-)^{\grstar}:(\Grmod S)^\op\longrightarrow\Grmod(S^\op),\qquad 
{}^{\grstar}(-):(\Grmod(S^\op))^\op\longrightarrow\Grmod S.
\end{equation}

Each functor in \eqref{eq:graded-S-dual-functors} restricts to locally finite-dimensional modules: replace $\Grmod$ by $\grmod$ in its source and target.
Indeed, for $R=S$ or $S^\op$ and $M\in\grmod R$,
\begin{equation}\label{eq:graded-S-dual-finiteness}
\dim_\Bbbk\Hom_R(M_{-i},R)
\leq(\dim_\Bbbk M_{-i})(\dim_\Bbbk R)<\infty
\quad(i\in\Z).
\end{equation}

\begin{lemma}\label{lem:S-bidual}
We have dualities
\[
\begin{aligned}
(-)^*:(\mod S)^\op & \xrightarrow{\sim}\mod(S^\op), & {}^*(-):(\mod(S^\op))^\op &\xrightarrow{\sim}\mod S,\\
(-)^{\grstar}:(\grmod S)^\op&\xrightarrow{\sim}\grmod(S^\op), &
{}^{\grstar}(-):(\grmod(S^\op))^\op&\xrightarrow{\sim}\grmod S.
\end{aligned}
\]
\end{lemma}

\begin{proof}
We show that evaluation gives natural isomorphisms of functors
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

For the graded cases, apply the ungraded case degree-wise.  Note that since $S$ is finite-dimensional, finitely generated $S$-module is the same as finite-dimensional $S$-modules.
\end{proof}

For a bimodule ${}_SM_S$, the linear and one-sided duals retain both actions:
\begin{equation}\label{eq:bimodule-dual-actions}
(s\lambda t)(m)=\lambda(tms),\qquad
(sft)(m)=sf(tm),\qquad
(sgt)(m)=g(ms)t,
\end{equation}
where $s,t\in S$, $m\in M$, $\lambda\in D(M)$, $f\in\Hom_S(M,S)$, and $g\in\Hom_{S^\op}(M,S)$.
The functionals still take values in $\Bbbk$ or $S$.
With precomposition on morphisms, we obtain
\begin{equation}\label{eq:one-sided-bimodule-dual-functors}
\begin{aligned}
D,\ (-)^*,\ {}^*(-)&:(\Mod S^\en)^\op\longrightarrow\Mod S^\en,\\
\bbD,\ (-)^{\grstar},\ {}^{\grstar}(-)&:(\Grmod S^\en)^\op\longrightarrow\Grmod S^\en.
\end{aligned}
\end{equation}
The restrictions to finite-dimensional modules, and to locally finite-dimensional graded modules, are dualities by Lemmas~\ref{lem:linear-bidual} and~\ref{lem:S-bidual}.
Evaluation preserves both actions: for $m\in M$, $f\in M^*$, and $s,t\in S$,
\[
(s\,\mathrm{ev}_M(m)\,t)(f)
=f(sm)t=f(smt)=\mathrm{ev}_M(smt)(f).
\]
The corresponding checks for $D$ and the left dual use the same evaluation formula; applying them in each degree gives the graded statements.

```

</details>

---
<a id="replacement-2"></a>

## Replacement 2: Lecture 1: the comparison of duals becomes an advanced subsection

Subsection 1.12 compares one-sided $S$-duals with $D$, so it now sits in a single advanced block, like the tensor-products-and-signs subsection in Lecture 3. The inner advanced and supplementary wrappers (current lines 1206, 1216, 1230, 1289, 1319) are removed; see Mechanical Corrections. The remark on the dependence on the form now *defines* the standard form $\tau_S$ and carries the new label `rem:standard-form`.

### Passage 1: open the advanced block at the subsection heading

**Location:** [Lecture_Koszul_S1.tex:1171](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1171) (current line 1171)  
**Change size:** 1 lines added; 0 lines removed.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -1171,1 +1195,2 @@
+\begin{advanced}[suppressfirstparskip=true,innertopmargin=0pt]
 \subsection{Comparing the duals}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\subsection{Comparing the duals}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{advanced}[suppressfirstparskip=true,innertopmargin=0pt]
\subsection{Comparing the duals}
```

</details>

### Passage 2: define $\tau_S$

**Location:** [Lecture_Koszul_S1.tex:1291](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S1.tex:1291) (current lines 1291–1296)  
**Change size:** 2 lines added; 2 lines removed.

```diff
--- a/Lecture_Koszul_S1.tex
+++ b/Lecture_Koszul_S1.tex
@@ -1291,6 +1312,6 @@
-\begin{remark}
+\begin{remark}\label{rem:standard-form}
 The natural isomorphisms in Theorem~\ref{prop:dual-comparison} depend on the chosen symmetrising form.
 For example, every choice $c_1,\ldots,c_n\in\Bbbk\setminus\{0\}$ gives a form
 $\tau(a_1,\ldots,a_n)=\sum_{i=1}^n c_i a_i$ on $\Bbbk^{\oplus n}$.
-Under Assumption~\ref{ass:basic-semisimple} we always use $\tau=\tau_S$, so $\alpha_M$ and $\beta_N$ involve no choice.
+Under Assumption~\ref{ass:basic-semisimple} we always use the \defn{standard symmetrising form} $\tau_S(\sum_{i=1}^na_ie_i)=\sum_{i=1}^na_i$, which involves no choice; then $\alpha_M$ and $\beta_N$ are canonical isomorphisms.
 \end{remark}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\begin{remark}
The natural isomorphisms in Theorem~\ref{prop:dual-comparison} depend on the chosen symmetrising form.
For example, every choice $c_1,\ldots,c_n\in\Bbbk\setminus\{0\}$ gives a form
$\tau(a_1,\ldots,a_n)=\sum_{i=1}^n c_i a_i$ on $\Bbbk^{\oplus n}$.
Under Assumption~\ref{ass:basic-semisimple} we always use $\tau=\tau_S$, so $\alpha_M$ and $\beta_N$ involve no choice.
\end{remark}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{remark}\label{rem:standard-form}
The natural isomorphisms in Theorem~\ref{prop:dual-comparison} depend on the chosen symmetrising form.
For example, every choice $c_1,\ldots,c_n\in\Bbbk\setminus\{0\}$ gives a form
$\tau(a_1,\ldots,a_n)=\sum_{i=1}^n c_i a_i$ on $\Bbbk^{\oplus n}$.
Under Assumption~\ref{ass:basic-semisimple} we always use the \defn{standard symmetrising form} $\tau_S(\sum_{i=1}^na_ie_i)=\sum_{i=1}^na_i$, which involves no choice; then $\alpha_M$ and $\beta_N$ are canonical isomorphisms.
\end{remark}
```

</details>

---
<a id="replacement-3"></a>

## Replacement 3: Lecture 2: one-sided $S$-dual material becomes advanced

The isomorphisms $\theta_r,\theta_\ell$ (`eq:tensor-duals`) and the Hom, evaluation and coevaluation results are statements about one-sided $S$-duals, so they join the neighbouring advanced blocks. This works by deleting the wrapper lines listed under Mechanical Corrections and adding the two lead-in sentences below. The total grading (`def:total-tensor-grading`) stays in the main text.

### Passage 1: lead-in to $\theta_r,\theta_\ell$

**Location:** [Lecture_Koszul_S2.tex:358](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:358) (current line 358)  
**Change size:** 2 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -358,1 +357,2 @@
-Let $S$ be finite-dimensional semisimple, and consider bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively.
+For an arbitrary finite-dimensional semisimple $S$, the one-sided $S$-duals satisfy an analogue of Proposition~\ref{prop:D-tensor-duals} without any choice.
+Consider bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
Let $S$ be finite-dimensional semisimple, and consider bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
For an arbitrary finite-dimensional semisimple $S$, the one-sided $S$-duals satisfy an analogue of Proposition~\ref{prop:D-tensor-duals} without any choice.
Consider bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively.
```

</details>

### Passage 2: open an advanced block for Hom, evaluation and coevaluation

**Location:** [Lecture_Koszul_S2.tex:451](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:451) (insert after current line 451)  
**Change size:** 3 lines added; 0 lines removed.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -451,1 +450,4 @@
 
+\begin{advanced}
+For an arbitrary finite-dimensional semisimple $S$, the one-sided $S$-duals also describe Hom spaces and give evaluation and coevaluation maps \cite[\S2.7]{BGS96}.
+
```

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{advanced}
For an arbitrary finite-dimensional semisimple $S$, the one-sided $S$-duals also describe Hom spaces and give evaluation and coevaluation maps \cite[\S2.7]{BGS96}.

```

</details>

---
<a id="replacement-4"></a>

## Replacement 4: Lecture 2: duals of tensor products and orthogonal complements via $D$

This is the new main tool. Under the assumption, Proposition `prop:D-tensor-duals` gives a choice-free isomorphism $\theta:D(W)\otimes_S D(V)\cong D(V\otimes_S W)$, $\theta(\lambda\otimes\mu)(v\otimes w)=\sum_i\mu(ve_i)\lambda(e_iw)$, with a supplementary proof. A *General $S$* remark gives the $\tau$-dual-basis version and points to $\theta_r,\theta_\ell$. The orthogonal complement is now taken in $D(M)$ (`def:D-orthogonal`), and the one-sided complements with their $\tau$-comparison move to an advanced block. Under $\tau_S$, $\theta$ is exactly $\theta_r$ transported along $\alpha$ (checked in Replacement 6).

### Passage 1: section opening

**Location:** [Lecture_Koszul_S2.tex:1067](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:1067) (current lines 1067–1103)  
**Change size:** 44 lines added; 3 lines removed.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -1067,37 +1064,78 @@
-Let $S$ be finite-dimensional semisimple.
+Recall Assumption~\ref{ass:basic-semisimple}: $S=\bigoplus_{i=1}^n\Bbbk e_i$.
+
+\begin{proposition}[Duals of tensor products]\label{prop:D-tensor-duals}
+For finite-dimensional bimodules ${}_SV_S$ and ${}_SW_S$, there is a natural bimodule isomorphism
+\begin{equation}\label{eq:D-tensor-duals}
+\theta:D(W)\otimes_S D(V)\xrightarrow{\sim}D(V\otimes_S W),\qquad
+\theta(\lambda\otimes\mu)(v\otimes w)=\sum_{i=1}^n\mu(ve_i)\,\lambda(e_iw).
+\end{equation}
+In words: dualising reverses the order of the tensor factors.
+\end{proposition}
+
+\begin{supplementary}
+\begin{proof}
+By \eqref{eq:linear-bimodule-dual-action}, $(\lambda e_k)(w)=\lambda(e_kw)$ and $(e_k\mu)(v)=\mu(ve_k)$.
+Hence, for every $k$, replacing $v\otimes e_kw$ by $ve_k\otimes w$, or $\lambda\otimes e_k\mu$ by $\lambda e_k\otimes\mu$, leaves the right-hand side equal to $\mu(ve_k)\lambda(e_kw)$.
+By linearity the formula respects both tensor relations, so $\theta$ is well defined.
+For $s,t\in S$, the same rule gives $\theta(s\lambda\otimes\mu t)(v\otimes w)=\theta(\lambda\otimes\mu)(tv\otimes ws)$, so $\theta$ is a bimodule map; it commutes with precomposition by bimodule maps, so it is natural.
+For bijectivity, Lemma~\ref{lem:idempotent-tensors} and \eqref{eq:dual-blocks} decompose both sides into summands indexed by $(i,j,\ell)$, on which $\theta$ is
+\[
+D(e_jWe_\ell)\otimes_\Bbbk D(e_iVe_j)\longrightarrow D(e_iVe_j\otimes_\Bbbk e_jWe_\ell),\qquad
+\lambda\otimes\mu\longmapsto\bigl(v\otimes w\mapsto\mu(v)\lambda(w)\bigr).
+\]
+This map sends tensor products of dual-basis vectors to the dual basis of the tensor-product basis, so it is an isomorphism.
+\end{proof}
+\end{supplementary}
+
+\begin{remark}[General $S$]
+For an arbitrary finite-dimensional semisimple $S$, there are no coordinate idempotents to sum over.
+After choosing a symmetrising form $\tau$ and bases $(x_k)$, $(y_k)$ of $S$ with $\tau(x_ky_l)=\delta_{kl}$, the sum $\sum_k\mu(vx_k)\lambda(y_kw)$ replaces \eqref{eq:D-tensor-duals}.
+Alternatively, the one-sided $S$-duals give the choice-free isomorphisms $\theta_r,\theta_\ell$ in \eqref{eq:tensor-duals} (advanced).
+\end{remark}
+
+\begin{definition}\label{def:D-orthogonal}
+For a sub-bimodule $U$ of a finite-dimensional bimodule ${}_SM_S$, its \defn{orthogonal complement} is
+\[
+U^\perp:=\{\lambda\in D(M)\mid\lambda(u)=0\text{ for all }u\in U\}.
+\]
+\end{definition}
+
+It is a sub-bimodule of $D(M)$: for $s,t\in S$ and $u\in U$, we have $(s\lambda t)(u)=\lambda(tus)=0$ since $tus\in U$.
+
+\begin{advanced}
+For an arbitrary finite-dimensional semisimple $S$, the one-sided $S$-duals give the following choice-free orthogonal complements.
 
 \begin{definition}\label{def:orthogonals}
 For an $S$-sub-bimodule $U$ of a finite-dimensional $S$-bimodule $M$, its \defn{right orthogonal complement} and \defn{left orthogonal complement} are
 \[
 \begin{aligned}
 U^\perp&:=\{f\in M^*\mid f(u)=0\text{ for all }u\in U\},\\
 {}^\perp U&:=\{g\in{}^*M\mid g(u)=0\text{ for all }u\in U\}.
 \end{aligned}
 \]
 \end{definition}
 
 Both orthogonal complements are $S$-sub-bimodules.
 Indeed, for $s,t\in S$ and $u\in U$, the action on $S$-dual \eqref{eq:bimodule-dual-actions} reads
 \[
 (sft)(u)=sf(tu)=0\quad(f\in U^\perp),\qquad
 (sgt)(u)=g(us)t=0\quad(g\in{}^\perp U),
 \]
 since $tu,us\in U$.
 The orthogonal complements are defined without choosing a symmetrising form, but it is possible to realise, through the natural isomorphism associated to a chosen symmetrising form, the orthogonal complements as a sub-bimodule of $D(M)$.
 
-\begin{advanced}
 If $S$ is equipped with a symmetrising form $\tau:S\to\Bbbk$, the comparison maps $\alpha_M,\beta_M$ of \eqref{eq:dual-comparison} satisfy
 \begin{equation}\label{eq:orthogonal-comparison}
 \alpha_M(U^\perp)=\{\lambda\in D(M)\mid\lambda(u)=0\text{ for all }u\in U\}=\beta_M({}^\perp U)
 .
 \end{equation}
-The middle space contains $\alpha_M(U^\perp)$ and $\beta_M({}^\perp U)$: if $f\in U^\perp$ and $g\in{}^\perp U$, then $\tau\circ f$ and $\tau\circ g$ vanish on $U$.
+The middle space is the orthogonal complement of Definition~\ref{def:D-orthogonal}; it contains $\alpha_M(U^\perp)$ and $\beta_M({}^\perp U)$: if $f\in U^\perp$ and $g\in{}^\perp U$, then $\tau\circ f$ and $\tau\circ g$ vanish on $U$.
 Conversely, $\alpha_M(f)(U)=0$ gives
 \[
 \tau(f(u)s)=\tau(f(us))=0
 \quad\text{for all }s\in S,\ u\in U.
 \]
 Non-degeneracy of $\tau$ forces $f(u)=0$ for every $u\in U$.
 For the left dual, $\tau(sg(u))=\tau(g(su))=0$ gives $g(u)=0$ instead.
 Bijectivity of $\alpha_M,\beta_M$ in Theorem~\ref{prop:dual-comparison} proves \eqref{eq:orthogonal-comparison}.
 \end{advanced}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
Let $S$ be finite-dimensional semisimple.

\begin{definition}\label{def:orthogonals}
For an $S$-sub-bimodule $U$ of a finite-dimensional $S$-bimodule $M$, its \defn{right orthogonal complement} and \defn{left orthogonal complement} are
\[
\begin{aligned}
U^\perp&:=\{f\in M^*\mid f(u)=0\text{ for all }u\in U\},\\
{}^\perp U&:=\{g\in{}^*M\mid g(u)=0\text{ for all }u\in U\}.
\end{aligned}
\]
\end{definition}

Both orthogonal complements are $S$-sub-bimodules.
Indeed, for $s,t\in S$ and $u\in U$, the action on $S$-dual \eqref{eq:bimodule-dual-actions} reads
\[
(sft)(u)=sf(tu)=0\quad(f\in U^\perp),\qquad
(sgt)(u)=g(us)t=0\quad(g\in{}^\perp U),
\]
since $tu,us\in U$.
The orthogonal complements are defined without choosing a symmetrising form, but it is possible to realise, through the natural isomorphism associated to a chosen symmetrising form, the orthogonal complements as a sub-bimodule of $D(M)$.

\begin{advanced}
If $S$ is equipped with a symmetrising form $\tau:S\to\Bbbk$, the comparison maps $\alpha_M,\beta_M$ of \eqref{eq:dual-comparison} satisfy
\begin{equation}\label{eq:orthogonal-comparison}
\alpha_M(U^\perp)=\{\lambda\in D(M)\mid\lambda(u)=0\text{ for all }u\in U\}=\beta_M({}^\perp U)
.
\end{equation}
The middle space contains $\alpha_M(U^\perp)$ and $\beta_M({}^\perp U)$: if $f\in U^\perp$ and $g\in{}^\perp U$, then $\tau\circ f$ and $\tau\circ g$ vanish on $U$.
Conversely, $\alpha_M(f)(U)=0$ gives
\[
\tau(f(u)s)=\tau(f(us))=0
\quad\text{for all }s\in S,\ u\in U.
\]
Non-degeneracy of $\tau$ forces $f(u)=0$ for every $u\in U$.
For the left dual, $\tau(sg(u))=\tau(g(su))=0$ gives $g(u)=0$ instead.
Bijectivity of $\alpha_M,\beta_M$ in Theorem~\ref{prop:dual-comparison} proves \eqref{eq:orthogonal-comparison}.
\end{advanced}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
Recall Assumption~\ref{ass:basic-semisimple}: $S=\bigoplus_{i=1}^n\Bbbk e_i$.

\begin{proposition}[Duals of tensor products]\label{prop:D-tensor-duals}
For finite-dimensional bimodules ${}_SV_S$ and ${}_SW_S$, there is a natural bimodule isomorphism
\begin{equation}\label{eq:D-tensor-duals}
\theta:D(W)\otimes_S D(V)\xrightarrow{\sim}D(V\otimes_S W),\qquad
\theta(\lambda\otimes\mu)(v\otimes w)=\sum_{i=1}^n\mu(ve_i)\,\lambda(e_iw).
\end{equation}
In words: dualising reverses the order of the tensor factors.
\end{proposition}

\begin{supplementary}
\begin{proof}
By \eqref{eq:linear-bimodule-dual-action}, $(\lambda e_k)(w)=\lambda(e_kw)$ and $(e_k\mu)(v)=\mu(ve_k)$.
Hence, for every $k$, replacing $v\otimes e_kw$ by $ve_k\otimes w$, or $\lambda\otimes e_k\mu$ by $\lambda e_k\otimes\mu$, leaves the right-hand side equal to $\mu(ve_k)\lambda(e_kw)$.
By linearity the formula respects both tensor relations, so $\theta$ is well defined.
For $s,t\in S$, the same rule gives $\theta(s\lambda\otimes\mu t)(v\otimes w)=\theta(\lambda\otimes\mu)(tv\otimes ws)$, so $\theta$ is a bimodule map; it commutes with precomposition by bimodule maps, so it is natural.
For bijectivity, Lemma~\ref{lem:idempotent-tensors} and \eqref{eq:dual-blocks} decompose both sides into summands indexed by $(i,j,\ell)$, on which $\theta$ is
\[
D(e_jWe_\ell)\otimes_\Bbbk D(e_iVe_j)\longrightarrow D(e_iVe_j\otimes_\Bbbk e_jWe_\ell),\qquad
\lambda\otimes\mu\longmapsto\bigl(v\otimes w\mapsto\mu(v)\lambda(w)\bigr).
\]
This map sends tensor products of dual-basis vectors to the dual basis of the tensor-product basis, so it is an isomorphism.
\end{proof}
\end{supplementary}

\begin{remark}[General $S$]
For an arbitrary finite-dimensional semisimple $S$, there are no coordinate idempotents to sum over.
After choosing a symmetrising form $\tau$ and bases $(x_k)$, $(y_k)$ of $S$ with $\tau(x_ky_l)=\delta_{kl}$, the sum $\sum_k\mu(vx_k)\lambda(y_kw)$ replaces \eqref{eq:D-tensor-duals}.
Alternatively, the one-sided $S$-duals give the choice-free isomorphisms $\theta_r,\theta_\ell$ in \eqref{eq:tensor-duals} (advanced).
\end{remark}

\begin{definition}\label{def:D-orthogonal}
For a sub-bimodule $U$ of a finite-dimensional bimodule ${}_SM_S$, its \defn{orthogonal complement} is
\[
U^\perp:=\{\lambda\in D(M)\mid\lambda(u)=0\text{ for all }u\in U\}.
\]
\end{definition}

It is a sub-bimodule of $D(M)$: for $s,t\in S$ and $u\in U$, we have $(s\lambda t)(u)=\lambda(tus)=0$ since $tus\in U$.

\begin{advanced}
For an arbitrary finite-dimensional semisimple $S$, the one-sided $S$-duals give the following choice-free orthogonal complements.

\begin{definition}\label{def:orthogonals}
For an $S$-sub-bimodule $U$ of a finite-dimensional $S$-bimodule $M$, its \defn{right orthogonal complement} and \defn{left orthogonal complement} are
\[
\begin{aligned}
U^\perp&:=\{f\in M^*\mid f(u)=0\text{ for all }u\in U\},\\
{}^\perp U&:=\{g\in{}^*M\mid g(u)=0\text{ for all }u\in U\}.
\end{aligned}
\]
\end{definition}

Both orthogonal complements are $S$-sub-bimodules.
Indeed, for $s,t\in S$ and $u\in U$, the action on $S$-dual \eqref{eq:bimodule-dual-actions} reads
\[
(sft)(u)=sf(tu)=0\quad(f\in U^\perp),\qquad
(sgt)(u)=g(us)t=0\quad(g\in{}^\perp U),
\]
since $tu,us\in U$.
The orthogonal complements are defined without choosing a symmetrising form, but it is possible to realise, through the natural isomorphism associated to a chosen symmetrising form, the orthogonal complements as a sub-bimodule of $D(M)$.

If $S$ is equipped with a symmetrising form $\tau:S\to\Bbbk$, the comparison maps $\alpha_M,\beta_M$ of \eqref{eq:dual-comparison} satisfy
\begin{equation}\label{eq:orthogonal-comparison}
\alpha_M(U^\perp)=\{\lambda\in D(M)\mid\lambda(u)=0\text{ for all }u\in U\}=\beta_M({}^\perp U)
.
\end{equation}
The middle space is the orthogonal complement of Definition~\ref{def:D-orthogonal}; it contains $\alpha_M(U^\perp)$ and $\beta_M({}^\perp U)$: if $f\in U^\perp$ and $g\in{}^\perp U$, then $\tau\circ f$ and $\tau\circ g$ vanish on $U$.
Conversely, $\alpha_M(f)(U)=0$ gives
\[
\tau(f(u)s)=\tau(f(us))=0
\quad\text{for all }s\in S,\ u\in U.
\]
Non-degeneracy of $\tau$ forces $f(u)=0$ for every $u\in U$.
For the left dual, $\tau(sg(u))=\tau(g(su))=0$ gives $g(u)=0$ instead.
Bijectivity of $\alpha_M,\beta_M$ in Theorem~\ref{prop:dual-comparison} proves \eqref{eq:orthogonal-comparison}.
\end{advanced}
```

</details>

### Passage 2: Example `ex:symmetric-orthogonals`

**Location:** [Lecture_Koszul_S2.tex:1116](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex:1116) (current line 1116)  
**Change size:** 1 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul_S2.tex
+++ b/Lecture_Koszul_S2.tex
@@ -1116,1 +1154,1 @@
-By anti-distributivity of the $S$-dual \eqref{eq:tensor-duals}, with $S=\Bbbk$ and the formulas in \eqref{eq:tensor-evaluations},
+By Proposition~\ref{prop:D-tensor-duals} with $S=\Bbbk$, where $\theta(\lambda\otimes\mu)(v\otimes w)=\mu(v)\lambda(w)$,
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
By anti-distributivity of the $S$-dual \eqref{eq:tensor-duals}, with $S=\Bbbk$ and the formulas in \eqref{eq:tensor-evaluations},
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
By Proposition~\ref{prop:D-tensor-duals} with $S=\Bbbk$, where $\theta(\lambda\otimes\mu)(v\otimes w)=\mu(v)\lambda(w)$,
```

</details>

---
<a id="replacement-5"></a>

## Replacement 5: Lecture 3: the quadratic dual defined with $D$

Now $A^!:=T_S(D(V))/(R^\perp)$, with $R^\perp$ taken via $\theta$. The labels `def:quadratic-duals` and `eq:quadratic-duals` now refer to this definition. The independence paragraph uses functoriality of $D$. Proposition `prop:dual-low-degrees` now gives $A^!_2\cong D(R)$ by exactness of $D$, so the Artin–Wedderburn dimension count is no longer needed.

### Passage 1: opening, definition, independence of presentation

**Location:** [Lecture_Koszul_S3.tex:18](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:18) (current lines 18–58)  
**Change size:** 17 lines added; 29 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -18,41 +18,29 @@
-By anti-distributivity of the $S$-dual \eqref{eq:tensor-duals} we have isomorphisms of bimodules $
-\theta_r:V^*\otimes_S V^*\xrightarrow{\sim}(V\otimes_S V)^*$ and $\theta_\ell:{}^*V\otimes_S{}^*V\xrightarrow{\sim}{}^*(V\otimes_S V)$.
-We will identify $V^*\otimes_S V^*$ with $(V\otimes_S V)^*$ via $\theta_r$, and ${}^*V\otimes_S{}^*V$ with ${}^*(V\otimes_S V)$ via $\theta_\ell$.
-In particular, we can regard the orthogonal complements of the relation spaces as sub-bimodules
+By Proposition~\ref{prop:D-tensor-duals}, there is a bimodule isomorphism $\theta:D(V)\otimes_S D(V)\xrightarrow{\sim}D(V\otimes_S V)$, given by
 \[
-R^\perp \subset (V\otimes_SV)^*\cong V^*\otimes_SV^* \quad \text{and} \quad {}^\perp R \subset {}^*(V\otimes_SV)\cong {}^*V\otimes_S{}^*V. 
+\theta(\lambda\otimes\mu)(v\otimes w)=\sum_{i=1}^n\mu(ve_i)\,\lambda(e_iw)
+\qquad(\lambda,\mu\in D(V),\ v,w\in V).
 \]
+We use $\theta$ to identify $D(V)\otimes_S D(V)$ with $D(V\otimes_S V)$.
+In particular, the orthogonal complement $R^\perp\subset D(V\otimes_S V)$ of Definition~\ref{def:D-orthogonal} becomes a sub-bimodule of $D(V)\otimes_S D(V)$.
 
 \begin{definition}\label{def:quadratic-duals}
-The \defn{right quadratic dual} and \defn{left quadratic dual} of $A$ are
+The \defn{quadratic dual} of $A$ is
 \begin{equation}\label{eq:quadratic-duals}
-\begin{aligned}
-A^!&:=T_S(V^*)/(R^\perp),
-&R^\perp&=\{F\in V^*\otimes_S V^*\mid\theta_r(F)(R)=0\},\\
-{}^!A&:=T_S({}^*V)/({}^\perp R),
-&{}^\perp R&=\{F\in{}^*V\otimes_S{}^*V\mid\theta_\ell(F)(R)=0\}.
-\end{aligned}
+A^!:=T_S(D(V))/(R^\perp),
+\qquad
+R^\perp=\{F\in D(V)\otimes_S D(V)\mid\theta(F)(R)=0\}.
 \end{equation}
 \end{definition}
 
-Note that we only take the ordinary $S$-duals $V^*$ and ${}^*V$, and they are placed in degree $1$ in \eqref{eq:quadratic-duals}  -- in contrast to the graded $S$-dual $V^{\grstar}$ which is placed in degree $-1$.
-
-
-\begin{advanced}
-Our notation is swapped relative to \cite[\S2.7 and Definition~2.8.1]{BGS96}: their $V^*$ uses left $S$-linear maps and their ${}^*V$ uses right $S$-linear maps.
-Thus our $A^!$ is their ${}^!A$, and our ${}^!A$ is their $A^!$.
-The names agree: they also call ${}^!A$ the right dual and $A^!$ the left dual.
-\end{advanced}
+Note that $D(V)$ is placed in degree $1$ in \eqref{eq:quadratic-duals} -- in contrast to the graded dual $\bbD(V)$, which is placed in degree $-1$.
+By \eqref{eq:dual-blocks}, dualising reverses the idempotents of each generator: $e_jD(V)e_i\cong D(e_iVe_j)$.
 
 By Proposition~\ref{prop:quadratic-basic}, a quadratic presentation identifies $S$ with $A_0$, $V$ with $A_1$, and $R$ with $\Ker\mu_2$, where $\mu_2:A_1\otimes_{A_0}A_1\to A_2$ is \eqref{eq:multiplication-maps}.
-Under $S\cong A_0$ and $V\cong A_1$, functoriality of the $S$-duals and anti-distributivity \eqref{eq:tensor-duals} give
+Under $S\cong A_0$ and $V\cong A_1$, functoriality of $D$ and Proposition~\ref{prop:D-tensor-duals} give
 \[
-\begin{aligned}
-V^*&\cong A_1^*,&
-R^\perp&\cong(\Ker\mu_2)^\perp\subset A_1^*\otimes_{A_0}A_1^*,\\
-{}^*V&\cong{}^*(A_1),&
-{}^\perp R&\cong{}^\perp(\Ker\mu_2)\subset{}^*(A_1)\otimes_{A_0}{}^*(A_1).
-\end{aligned}
+D(V)\cong D(A_1),\qquad
+R^\perp\cong(\Ker\mu_2)^\perp\subset D(A_1)\otimes_{A_0}D(A_1).
 \]
-By the universal property of tensor algebra (Proposition~\ref{prop:tensor-universal}), we can extend $V^*\cong A_1^*$ and $ {}^*V\cong{}^*(A_1)$ to tensor algebra isomorphisms, which descend to the quotients by $(R^\perp)$ and $({}^\perp R)$, respectively.
-Thus both quadratic duals are independent of the chosen presentation up to $A_0$-preserving isomorphisms of graded algebras.
+By the universal property of tensor algebra (Proposition~\ref{prop:tensor-universal}), we can extend $D(V)\cong D(A_1)$ to a tensor algebra isomorphism, which descends to the quotients by $(R^\perp)$ and $((\Ker\mu_2)^\perp)$.
+Thus the quadratic dual is independent of the chosen presentation up to $A_0$-preserving isomorphisms of graded algebras.
+
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
By anti-distributivity of the $S$-dual \eqref{eq:tensor-duals} we have isomorphisms of bimodules $
\theta_r:V^*\otimes_S V^*\xrightarrow{\sim}(V\otimes_S V)^*$ and $\theta_\ell:{}^*V\otimes_S{}^*V\xrightarrow{\sim}{}^*(V\otimes_S V)$.
We will identify $V^*\otimes_S V^*$ with $(V\otimes_S V)^*$ via $\theta_r$, and ${}^*V\otimes_S{}^*V$ with ${}^*(V\otimes_S V)$ via $\theta_\ell$.
In particular, we can regard the orthogonal complements of the relation spaces as sub-bimodules
\[
R^\perp \subset (V\otimes_SV)^*\cong V^*\otimes_SV^* \quad \text{and} \quad {}^\perp R \subset {}^*(V\otimes_SV)\cong {}^*V\otimes_S{}^*V. 
\]

\begin{definition}\label{def:quadratic-duals}
The \defn{right quadratic dual} and \defn{left quadratic dual} of $A$ are
\begin{equation}\label{eq:quadratic-duals}
\begin{aligned}
A^!&:=T_S(V^*)/(R^\perp),
&R^\perp&=\{F\in V^*\otimes_S V^*\mid\theta_r(F)(R)=0\},\\
{}^!A&:=T_S({}^*V)/({}^\perp R),
&{}^\perp R&=\{F\in{}^*V\otimes_S{}^*V\mid\theta_\ell(F)(R)=0\}.
\end{aligned}
\end{equation}
\end{definition}

Note that we only take the ordinary $S$-duals $V^*$ and ${}^*V$, and they are placed in degree $1$ in \eqref{eq:quadratic-duals}  -- in contrast to the graded $S$-dual $V^{\grstar}$ which is placed in degree $-1$.


\begin{advanced}
Our notation is swapped relative to \cite[\S2.7 and Definition~2.8.1]{BGS96}: their $V^*$ uses left $S$-linear maps and their ${}^*V$ uses right $S$-linear maps.
Thus our $A^!$ is their ${}^!A$, and our ${}^!A$ is their $A^!$.
The names agree: they also call ${}^!A$ the right dual and $A^!$ the left dual.
\end{advanced}

By Proposition~\ref{prop:quadratic-basic}, a quadratic presentation identifies $S$ with $A_0$, $V$ with $A_1$, and $R$ with $\Ker\mu_2$, where $\mu_2:A_1\otimes_{A_0}A_1\to A_2$ is \eqref{eq:multiplication-maps}.
Under $S\cong A_0$ and $V\cong A_1$, functoriality of the $S$-duals and anti-distributivity \eqref{eq:tensor-duals} give
\[
\begin{aligned}
V^*&\cong A_1^*,&
R^\perp&\cong(\Ker\mu_2)^\perp\subset A_1^*\otimes_{A_0}A_1^*,\\
{}^*V&\cong{}^*(A_1),&
{}^\perp R&\cong{}^\perp(\Ker\mu_2)\subset{}^*(A_1)\otimes_{A_0}{}^*(A_1).
\end{aligned}
\]
By the universal property of tensor algebra (Proposition~\ref{prop:tensor-universal}), we can extend $V^*\cong A_1^*$ and $ {}^*V\cong{}^*(A_1)$ to tensor algebra isomorphisms, which descend to the quotients by $(R^\perp)$ and $({}^\perp R)$, respectively.
Thus both quadratic duals are independent of the chosen presentation up to $A_0$-preserving isomorphisms of graded algebras.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
By Proposition~\ref{prop:D-tensor-duals}, there is a bimodule isomorphism $\theta:D(V)\otimes_S D(V)\xrightarrow{\sim}D(V\otimes_S V)$, given by
\[
\theta(\lambda\otimes\mu)(v\otimes w)=\sum_{i=1}^n\mu(ve_i)\,\lambda(e_iw)
\qquad(\lambda,\mu\in D(V),\ v,w\in V).
\]
We use $\theta$ to identify $D(V)\otimes_S D(V)$ with $D(V\otimes_S V)$.
In particular, the orthogonal complement $R^\perp\subset D(V\otimes_S V)$ of Definition~\ref{def:D-orthogonal} becomes a sub-bimodule of $D(V)\otimes_S D(V)$.

\begin{definition}\label{def:quadratic-duals}
The \defn{quadratic dual} of $A$ is
\begin{equation}\label{eq:quadratic-duals}
A^!:=T_S(D(V))/(R^\perp),
\qquad
R^\perp=\{F\in D(V)\otimes_S D(V)\mid\theta(F)(R)=0\}.
\end{equation}
\end{definition}

Note that $D(V)$ is placed in degree $1$ in \eqref{eq:quadratic-duals} -- in contrast to the graded dual $\bbD(V)$, which is placed in degree $-1$.
By \eqref{eq:dual-blocks}, dualising reverses the idempotents of each generator: $e_jD(V)e_i\cong D(e_iVe_j)$.

By Proposition~\ref{prop:quadratic-basic}, a quadratic presentation identifies $S$ with $A_0$, $V$ with $A_1$, and $R$ with $\Ker\mu_2$, where $\mu_2:A_1\otimes_{A_0}A_1\to A_2$ is \eqref{eq:multiplication-maps}.
Under $S\cong A_0$ and $V\cong A_1$, functoriality of $D$ and Proposition~\ref{prop:D-tensor-duals} give
\[
D(V)\cong D(A_1),\qquad
R^\perp\cong(\Ker\mu_2)^\perp\subset D(A_1)\otimes_{A_0}D(A_1).
\]
By the universal property of tensor algebra (Proposition~\ref{prop:tensor-universal}), we can extend $D(V)\cong D(A_1)$ to a tensor algebra isomorphism, which descends to the quotients by $(R^\perp)$ and $((\Ker\mu_2)^\perp)$.
Thus the quadratic dual is independent of the chosen presentation up to $A_0$-preserving isomorphisms of graded algebras.

```

</details>

### Passage 2: low degrees

**Location:** [Lecture_Koszul_S3.tex:61](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:61) (current lines 61–101)  
**Change size:** 6 lines added; 29 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -61,41 +49,18 @@
 \begin{proposition}\label{prop:dual-low-degrees}
 The algebra $A^!$ is quadratic and
 \[
-A^!_0=S,\qquad A^!_1=V^*,\qquad A^!_2\cong R^*.
+A^!_0=S,\qquad A^!_1=D(V),\qquad A^!_2\cong D(R).
 \]
 In particular, $\dim_\Bbbk A^!_2=\dim_\Bbbk R$.
 \end{proposition}
 
 \begin{proof}
 Restriction to $R$ gives an exact sequence of $S$-bimodules
 \begin{equation}\label{eq:restriction-relations}
-0\longrightarrow R^\perp\longrightarrow V^*\otimes_S V^*
-\xrightarrow{F\mapsto\theta_r(F)|_R}R^*\longrightarrow0.
+0\longrightarrow R^\perp\longrightarrow D(V)\otimes_S D(V)
+\xrightarrow{F\mapsto\theta(F)|_R}D(R)\longrightarrow0,
 \end{equation}
-Surjectivity follows from Theorem~\ref{thm:artin-wedderburn}: $R$ has a complement as a right $S$-module, so a right $S$-linear map $R\to S$ extends by zero on that complement.
-Taking the quotient in \eqref{eq:restriction-relations} gives $A^!_2\cong R^*$; Proposition~\ref{prop:quadratic-basic} gives the remaining assertions about $A^!$.
-
-For the dimension assertion, write
-\[
-S\cong\prod_{j=1}^n\Mat_{d_j}(\Delta_j),
-\qquad
-R_S\cong\bigoplus_{j=1}^n
-(\Delta_j^{1\times d_j})^{\oplus m_j},
-\]
-where each $\Delta_j$ is a finite-dimensional division $\Bbbk$-algebra and $m_j$ is the multiplicity of the corresponding simple right module $\Delta_j^{1\times d_j})$ (the row space).
-For each $j$, there is a left $\Mat_{d_j}(\Delta_j)$-module isomorphism
-\[
-\Delta_j^{d_j\times1}\xrightarrow{\sim}
-\Hom_{\Mat_{d_j}(\Delta_j)}(\Delta_j^{1\times d_j},\Mat_{d_j}(\Delta_j)),
-\qquad c\longmapsto(x\mapsto cx),
-\]
-where $\Delta_j^{d_j\times1}$ is the left simple module given by the column space.
-Thus, as left $S$-modules,
-\[
-{}_S R^*\cong\bigoplus_{j=1}^n
-(\Delta_j^{d_j\times1})^{\oplus m_j},
-\qquad
-\dim_\Bbbk R^*=\sum_{j=1}^n m_jd_j\dim_\Bbbk\Delta_j
-=\dim_\Bbbk R.
-\]
+which is exact on the right because $D$ is exact (Example~\ref{ex:linear-duality}).
+Taking the quotient gives $A^!_2\cong D(R)$, and $\dim_\Bbbk D(R)=\dim_\Bbbk R$ because $R$ is finite-dimensional.
+Proposition~\ref{prop:quadratic-basic} gives the remaining assertions.
 \end{proof}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\begin{proposition}\label{prop:dual-low-degrees}
The algebra $A^!$ is quadratic and
\[
A^!_0=S,\qquad A^!_1=V^*,\qquad A^!_2\cong R^*.
\]
In particular, $\dim_\Bbbk A^!_2=\dim_\Bbbk R$.
\end{proposition}

\begin{proof}
Restriction to $R$ gives an exact sequence of $S$-bimodules
\begin{equation}\label{eq:restriction-relations}
0\longrightarrow R^\perp\longrightarrow V^*\otimes_S V^*
\xrightarrow{F\mapsto\theta_r(F)|_R}R^*\longrightarrow0.
\end{equation}
Surjectivity follows from Theorem~\ref{thm:artin-wedderburn}: $R$ has a complement as a right $S$-module, so a right $S$-linear map $R\to S$ extends by zero on that complement.
Taking the quotient in \eqref{eq:restriction-relations} gives $A^!_2\cong R^*$; Proposition~\ref{prop:quadratic-basic} gives the remaining assertions about $A^!$.

For the dimension assertion, write
\[
S\cong\prod_{j=1}^n\Mat_{d_j}(\Delta_j),
\qquad
R_S\cong\bigoplus_{j=1}^n
(\Delta_j^{1\times d_j})^{\oplus m_j},
\]
where each $\Delta_j$ is a finite-dimensional division $\Bbbk$-algebra and $m_j$ is the multiplicity of the corresponding simple right module $\Delta_j^{1\times d_j})$ (the row space).
For each $j$, there is a left $\Mat_{d_j}(\Delta_j)$-module isomorphism
\[
\Delta_j^{d_j\times1}\xrightarrow{\sim}
\Hom_{\Mat_{d_j}(\Delta_j)}(\Delta_j^{1\times d_j},\Mat_{d_j}(\Delta_j)),
\qquad c\longmapsto(x\mapsto cx),
\]
where $\Delta_j^{d_j\times1}$ is the left simple module given by the column space.
Thus, as left $S$-modules,
\[
{}_S R^*\cong\bigoplus_{j=1}^n
(\Delta_j^{d_j\times1})^{\oplus m_j},
\qquad
\dim_\Bbbk R^*=\sum_{j=1}^n m_jd_j\dim_\Bbbk\Delta_j
=\dim_\Bbbk R.
\]
\end{proof}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{proposition}\label{prop:dual-low-degrees}
The algebra $A^!$ is quadratic and
\[
A^!_0=S,\qquad A^!_1=D(V),\qquad A^!_2\cong D(R).
\]
In particular, $\dim_\Bbbk A^!_2=\dim_\Bbbk R$.
\end{proposition}

\begin{proof}
Restriction to $R$ gives an exact sequence of $S$-bimodules
\begin{equation}\label{eq:restriction-relations}
0\longrightarrow R^\perp\longrightarrow D(V)\otimes_S D(V)
\xrightarrow{F\mapsto\theta(F)|_R}D(R)\longrightarrow0,
\end{equation}
which is exact on the right because $D$ is exact (Example~\ref{ex:linear-duality}).
Taking the quotient gives $A^!_2\cong D(R)$, and $\dim_\Bbbk D(R)=\dim_\Bbbk R$ because $R$ is finite-dimensional.
Proposition~\ref{prop:quadratic-basic} gives the remaining assertions.
\end{proof}
```

</details>

---
<a id="replacement-6"></a>

## Replacement 6: Lecture 3: $(A^!)^!\cong A$ with no choices; one-sided version advanced

The main text gets Lemma `lem:double-orthogonal` for $D$ (plain linear algebra) and the new Theorem `thm:quadratic-involution`: evaluation gives $(A^!)^!\cong A$, via the computation \eqref{eq:bidual-tensor-square} with $\theta$. A *General $S$* remark follows. The right and left quadratic duals, the BGS convention note, the one-sided double-orthogonal lemma, Theorem `thm:quadratic-bidual` and Proposition `prop:quadratic-dual-sides` move verbatim into an advanced block, with renamed labels `def:S-quadratic-duals`, `eq:S-quadratic-duals`, `lem:S-double-orthogonal` and `eq:S-bidual-tensor-square`. The block also adds the check $\theta\circ(\alpha_V\otimes\alpha_V)=\alpha_{V\otimes_SV}\circ\theta_r$ under $\tau_S$, so the two definitions of $A^!$ agree. As a side effect, the previously undefined reference `eq:tensor-dual-actions` and the visible `\comm` in the old lemma are fixed.

### Passage 1: Section 3.2

**Location:** [Lecture_Koszul_S3.tex:117](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:117) (current lines 117–192)  
**Change size:** 70 lines added; 14 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -117,76 +82,132 @@
 \begin{lemma}\label{lem:double-orthogonal}
+Let $U$ be a sub-bimodule of a finite-dimensional bimodule ${}_SM_S$, and identify $M$ with $D(D(M))$ by evaluation (Lemma~\ref{lem:linear-bidual}).
+Then $(U^\perp)^\perp=U$.
+\end{lemma}
+
+\begin{supplementary}
+\begin{proof}
+If $u\in U$ and $\lambda\in U^\perp$, then $\mathrm{ev}_M(u)(\lambda)=\lambda(u)=0$; hence $U\subset(U^\perp)^\perp$.
+If $m\notin U$, extend a basis of $U$ by $m$ to a basis of $M$; the coordinate functional of $m$ lies in $U^\perp$ and does not vanish at $m$, so $m\notin(U^\perp)^\perp$.
+\end{proof}
+\end{supplementary}
+
+\begin{theorem}\label{thm:quadratic-involution}
+Quadratic duality is an involution: evaluation induces an $S$-preserving isomorphism of graded algebras
+\[
+(A^!)^!\cong A.
+\]
+\end{theorem}
+
+\begin{proof}
+\emph{Generators.} Evaluation $\mathrm{ev}_V:V\xrightarrow{\sim}D(D(V))$ is a bimodule isomorphism by Lemma~\ref{lem:linear-bidual} and \eqref{eq:linear-bimodule-dual-action}; it identifies the generators of $A$ and $(A^!)^!$.
+
+\emph{Relations.} The relations of $(A^!)^!$ are $(R^\perp)^\perp\subset D(D(V))\otimes_S D(D(V))$, formed with the map $\theta$ for the bimodule $D(V)$.
+By \eqref{eq:linear-bimodule-dual-action}, $(\lambda e_i)(w)=\lambda(e_iw)$ and $(e_i\mu)(v)=\mu(ve_i)$, so for $v,w\in V$ and $\lambda,\mu\in D(V)$,
+\begin{equation}\label{eq:bidual-tensor-square}
+\theta\bigl(\mathrm{ev}_V(v)\otimes\mathrm{ev}_V(w)\bigr)(\lambda\otimes\mu)
+=\sum_{i=1}^n\mathrm{ev}_V(w)(\lambda e_i)\,\mathrm{ev}_V(v)(e_i\mu)
+=\theta(\lambda\otimes\mu)(v\otimes w).
+\end{equation}
+Thus $\mathrm{ev}_V\otimes\mathrm{ev}_V$ is the evaluation identification of $V\otimes_S V$ with the dual of $D(V\otimes_S V)\cong D(V)\otimes_S D(V)$.
+Lemma~\ref{lem:double-orthogonal}, applied to $R\subset V\otimes_S V$, identifies $(R^\perp)^\perp$ with $R$.
+The presentations \eqref{eq:quadratic-duals} therefore give an $S$-preserving isomorphism of graded algebras $(A^!)^!\cong A$.
+\end{proof}
+
+\begin{remark}[General $S$]
+For an arbitrary finite-dimensional semisimple $S$, the map $\theta$, and hence Definition~\ref{def:quadratic-duals}, needs a choice of symmetrising form.
+The choice-free version uses the right and left $S$-duals: the right and left quadratic duals below satisfy ${}^!(A^!)\cong A\cong({}^!A)^!$ with no choice (Theorem~\ref{thm:quadratic-bidual}, advanced).
+\end{remark}
+
+\begin{advanced}
+\emph{Quadratic duals via one-sided $S$-duals.}
+For an arbitrary finite-dimensional semisimple $S$, we use the isomorphisms $\theta_r,\theta_\ell$ of \eqref{eq:tensor-duals} instead of $\theta$.
+
+\begin{definition}\label{def:S-quadratic-duals}
+The \defn{right quadratic dual} and \defn{left quadratic dual} of $A$ are
+\begin{equation}\label{eq:S-quadratic-duals}
+\begin{aligned}
+A^!&:=T_S(V^*)/(R^\perp),
+&R^\perp&=\{F\in V^*\otimes_S V^*\mid\theta_r(F)(R)=0\},\\
+{}^!A&:=T_S({}^*V)/({}^\perp R),
+&{}^\perp R&=\{F\in{}^*V\otimes_S{}^*V\mid\theta_\ell(F)(R)=0\}.
+\end{aligned}
+\end{equation}
+\end{definition}
+
+Under Assumption~\ref{ass:basic-semisimple}, the map $\alpha_V:V^*\to D(V)$, $f\mapsto\tau_S\circ f$, of Theorem~\ref{prop:dual-comparison} satisfies $\theta\circ(\alpha_V\otimes\alpha_V)=\alpha_{V\otimes_SV}\circ\theta_r$: both sides send $g\otimes f$ to $v\otimes w\mapsto\tau_S(g(f(v)w))$, because $\sum_i\tau_S(se_i)e_i=s$ for $s\in S$.
+Hence $\alpha_V$ induces an isomorphism from the right quadratic dual onto the quadratic dual of Definition~\ref{def:quadratic-duals}; this is why we use the same symbol $A^!$.
+
+Our notation is swapped relative to \cite[\S2.7 and Definition~2.8.1]{BGS96}: their $V^*$ uses left $S$-linear maps and their ${}^*V$ uses right $S$-linear maps.
+Thus our $A^!$ is their ${}^!A$, and our ${}^!A$ is their $A^!$.
+The names agree: they also call ${}^!A$ the right dual and $A^!$ the left dual.
+
+\begin{lemma}\label{lem:S-double-orthogonal}
 Let $U\subset M$ be an $S$-sub-bimodule of a finite-dimensional bimodule $ {}_SM_S$.
 Under $M\cong{}^*(M^*)$ and $M\cong({}^*M)^*$ from the right and left $S$-dualities in Lemma~\ref{lem:S-bidual},
 \[
 {}^\perp(U^\perp)=U,\qquad ({}^\perp U)^\perp=U.
 \]
 \end{lemma}
 
 \begin{proof}
-For $u\in U$ and $f\in U^\perp$, evaluation \comm{state what map this is, from where to where} gives $\mathrm{ev}_M(u)(f)=f(u)=0$, so $U\subset{}^\perp(U^\perp)$ under Lemma~\ref{lem:S-bidual}.
+For $u\in U$ and $f\in U^\perp$, evaluation $\mathrm{ev}_M:M\to{}^*(M^*)$ gives $\mathrm{ev}_M(u)(f)=f(u)=0$, so $U\subset{}^\perp(U^\perp)$ under Lemma~\ref{lem:S-bidual}.
 
 Conversely, suppose that there is some $m\notin U$, semisimplicity of $S$ implies (by Corollary~\ref{cor:semisimple-summands}) that $M/U\hookrightarrow S^{\oplus n}$ as a right $S$-module for some $n$.
 Consider the composition $M\onto M/U\hookrightarrow S^{\oplus n}\twoheadrightarrow S$ which sends $m$ to a non-zero element in a direct summand of $S^{\oplus n}$.
 Then this is a right $S$-linear map in $\Hom_S(M,S)=M^*$ satisfying $f(U)=0$ and $f(m)\neq0$.
 Thus $f\in U^\perp$ and $m\notin{}^\perp(U^\perp)$.
 The proof of $({}^\perp U)^\perp=U$ is similar.
 \end{proof}
 
 \begin{theorem}\label{thm:quadratic-bidual}
 Left and right quadratic duality are canonically inverse:
 \[
 {}^!(A^!)\cong A\cong({}^!A)^!
 \quad\text{by }S\text{-preserving isomorphisms of graded algebras}.
 \]
 \end{theorem}
 
 \begin{proof}
 \emph{Generators.} The right $S$-duality in Lemma~\ref{lem:S-bidual} gives
 $\mathrm{ev}_V:V\xrightarrow{\sim}{}^*(V^*)$, $v\mapsto(f\mapsto f(v))$, identifying the generators of $A$ and $ {}^!(A^!)$.
-It preserves both $S$-actions by \eqref{eq:tensor-dual-actions}.
+It preserves both $S$-actions by \eqref{eq:bimodule-dual-actions}.
 
 \emph{Relations.} The right $S$-action on $V^*$ is $(gs)(w)=g(sw)$ for all $g\in V^*$, $s\in S$, and $w\in V$.
 Applying \eqref{eq:tensor-evaluations} first to $V^*\otimes_S V^*$ and then to $V\otimes_S V$ gives, for all $v,w\in V$ and $f,g\in V^*$,
-\begin{equation}\label{eq:bidual-tensor-square}
+\begin{equation}\label{eq:S-bidual-tensor-square}
 \begin{aligned}
 \theta_\ell(\mathrm{ev}_V(v)\otimes\mathrm{ev}_V(w))(g\otimes f)
 &=\mathrm{ev}_V(w)(g f(v))=g(f(v)w)\\
 &=\mathrm{ev}_{V\otimes_S V}(v\otimes w)(\theta_r(g\otimes f)).
 \end{aligned}
 \end{equation}
 Thus $\mathrm{ev}_V\otimes\mathrm{ev}_V$ is the bidual identification for $V\otimes_S V$ under anti-distributivity of the $S$-dual \eqref{eq:tensor-duals}.
-Lemma~\ref{lem:double-orthogonal}, applied to $R\subset V\otimes_S V$, identifies the relations $ {}^\perp(R^\perp)$ of $ {}^!(A^!)$ with $R$.
-The presentations \eqref{eq:quadratic-duals} therefore give an $S$-preserving isomorphism of graded algebras $ {}^!(A^!)\cong A$.
+Lemma~\ref{lem:S-double-orthogonal}, applied to $R\subset V\otimes_S V$, identifies the relations $ {}^\perp(R^\perp)$ of $ {}^!(A^!)$ with $R$.
+The presentations \eqref{eq:S-quadratic-duals} therefore give an $S$-preserving isomorphism of graded algebras $ {}^!(A^!)\cong A$.
 Interchanging left and right gives $({}^!A)^!\cong A$.
 \end{proof}
 
 \begin{proposition}\label{prop:quadratic-dual-sides}
 A choice of symmetrising form $\tau:S\to\Bbbk$ gives $S$-preserving isomorphisms of graded algebras $A^!\cong{}^!A$ and $(A^!)^!\cong A$.
 \end{proposition}
 
-\begin{advanced}
 \begin{proof}
 The maps $\alpha_V(f)=\tau\circ f$ and $\beta_V(g)=\tau\circ g$ in \eqref{eq:dual-comparison} give a bimodule isomorphism $\beta_V^{-1}\alpha_V:V^*\to{}^*V$.
 For $f,g\in V^*$, write $f'=\beta_V^{-1}\alpha_V(f)$ and $g'=\beta_V^{-1}\alpha_V(g)$. Then
 \[
 \begin{aligned}
 \tau\bigl(f'(vg'(w))\bigr)
 &=\tau\bigl(f(v)g'(w)\bigr)
 =\tau\bigl(g'(f(v)w)\bigr)\\
 &=\tau\bigl(g(f(v)w)\bigr)
 \qquad(v,w\in V).
 \end{aligned}
 \]
 By \eqref{eq:orthogonal-comparison}, $(\beta_V^{-1}\alpha_V)^{\otimes_S2}$ therefore identifies $R^\perp$ with ${}^\perp R$.
 The bimodule map $\beta_V^{-1}\circ\alpha_V$ extends by Proposition~\ref{prop:tensor-universal} to an isomorphism $T_S(V^*)\to T_S({}^*V)$ and hence descends to $A^!\cong{}^!A$.
 Apply the same comparison to $A^!$ and then Theorem~\ref{thm:quadratic-bidual} to obtain $(A^!)^!\cong{}^!(A^!)\cong A$.
 \end{proof}
+
+For an arbitrary finite-dimensional semisimple $S$, the isomorphism $A^!\cong{}^!A$ of Proposition~\ref{prop:quadratic-dual-sides} depends on $\tau$; changing $\tau$ changes it by the central unit of Remark~\ref{rem:general-S-comparison}.
+Theorem~\ref{thm:quadratic-bidual} involves no choice.
 \end{advanced}
-
-Theorem~\ref{thm:quadratic-bidual} needs no choice of form. Proposition~\ref{prop:quadratic-dual-sides} permits the usual statement that quadratic duality is an involution, but the identification of left and right duals uses $\tau$.
-Under Assumption~\ref{ass:basic-semisimple} we use $\tau=\tau_S$, so the identification $A^!\cong{}^!A$ involves no choice.
-
-\begin{remark}[General $S$]
-For an arbitrary finite-dimensional semisimple $S$, the isomorphism $A^!\cong{}^!A$ of Proposition~\ref{prop:quadratic-dual-sides} depends on $\tau$; changing $\tau$ changes it by the central unit of Remark~\ref{rem:general-S-comparison}.
-Theorem~\ref{thm:quadratic-bidual} involves no choice and holds for every finite-dimensional semisimple $S$.
-\end{remark}
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\begin{lemma}\label{lem:double-orthogonal}
Let $U\subset M$ be an $S$-sub-bimodule of a finite-dimensional bimodule $ {}_SM_S$.
Under $M\cong{}^*(M^*)$ and $M\cong({}^*M)^*$ from the right and left $S$-dualities in Lemma~\ref{lem:S-bidual},
\[
{}^\perp(U^\perp)=U,\qquad ({}^\perp U)^\perp=U.
\]
\end{lemma}

\begin{proof}
For $u\in U$ and $f\in U^\perp$, evaluation \comm{state what map this is, from where to where} gives $\mathrm{ev}_M(u)(f)=f(u)=0$, so $U\subset{}^\perp(U^\perp)$ under Lemma~\ref{lem:S-bidual}.

Conversely, suppose that there is some $m\notin U$, semisimplicity of $S$ implies (by Corollary~\ref{cor:semisimple-summands}) that $M/U\hookrightarrow S^{\oplus n}$ as a right $S$-module for some $n$.
Consider the composition $M\onto M/U\hookrightarrow S^{\oplus n}\twoheadrightarrow S$ which sends $m$ to a non-zero element in a direct summand of $S^{\oplus n}$.
Then this is a right $S$-linear map in $\Hom_S(M,S)=M^*$ satisfying $f(U)=0$ and $f(m)\neq0$.
Thus $f\in U^\perp$ and $m\notin{}^\perp(U^\perp)$.
The proof of $({}^\perp U)^\perp=U$ is similar.
\end{proof}

\begin{theorem}\label{thm:quadratic-bidual}
Left and right quadratic duality are canonically inverse:
\[
{}^!(A^!)\cong A\cong({}^!A)^!
\quad\text{by }S\text{-preserving isomorphisms of graded algebras}.
\]
\end{theorem}

\begin{proof}
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
Interchanging left and right gives $({}^!A)^!\cong A$.
\end{proof}

\begin{proposition}\label{prop:quadratic-dual-sides}
A choice of symmetrising form $\tau:S\to\Bbbk$ gives $S$-preserving isomorphisms of graded algebras $A^!\cong{}^!A$ and $(A^!)^!\cong A$.
\end{proposition}

\begin{advanced}
\begin{proof}
The maps $\alpha_V(f)=\tau\circ f$ and $\beta_V(g)=\tau\circ g$ in \eqref{eq:dual-comparison} give a bimodule isomorphism $\beta_V^{-1}\alpha_V:V^*\to{}^*V$.
For $f,g\in V^*$, write $f'=\beta_V^{-1}\alpha_V(f)$ and $g'=\beta_V^{-1}\alpha_V(g)$. Then
\[
\begin{aligned}
\tau\bigl(f'(vg'(w))\bigr)
&=\tau\bigl(f(v)g'(w)\bigr)
=\tau\bigl(g'(f(v)w)\bigr)\\
&=\tau\bigl(g(f(v)w)\bigr)
\qquad(v,w\in V).
\end{aligned}
\]
By \eqref{eq:orthogonal-comparison}, $(\beta_V^{-1}\alpha_V)^{\otimes_S2}$ therefore identifies $R^\perp$ with ${}^\perp R$.
The bimodule map $\beta_V^{-1}\circ\alpha_V$ extends by Proposition~\ref{prop:tensor-universal} to an isomorphism $T_S(V^*)\to T_S({}^*V)$ and hence descends to $A^!\cong{}^!A$.
Apply the same comparison to $A^!$ and then Theorem~\ref{thm:quadratic-bidual} to obtain $(A^!)^!\cong{}^!(A^!)\cong A$.
\end{proof}
\end{advanced}

Theorem~\ref{thm:quadratic-bidual} needs no choice of form. Proposition~\ref{prop:quadratic-dual-sides} permits the usual statement that quadratic duality is an involution, but the identification of left and right duals uses $\tau$.
Under Assumption~\ref{ass:basic-semisimple} we use $\tau=\tau_S$, so the identification $A^!\cong{}^!A$ involves no choice.

\begin{remark}[General $S$]
For an arbitrary finite-dimensional semisimple $S$, the isomorphism $A^!\cong{}^!A$ of Proposition~\ref{prop:quadratic-dual-sides} depends on $\tau$; changing $\tau$ changes it by the central unit of Remark~\ref{rem:general-S-comparison}.
Theorem~\ref{thm:quadratic-bidual} involves no choice and holds for every finite-dimensional semisimple $S$.
\end{remark}
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\begin{lemma}\label{lem:double-orthogonal}
Let $U$ be a sub-bimodule of a finite-dimensional bimodule ${}_SM_S$, and identify $M$ with $D(D(M))$ by evaluation (Lemma~\ref{lem:linear-bidual}).
Then $(U^\perp)^\perp=U$.
\end{lemma}

\begin{supplementary}
\begin{proof}
If $u\in U$ and $\lambda\in U^\perp$, then $\mathrm{ev}_M(u)(\lambda)=\lambda(u)=0$; hence $U\subset(U^\perp)^\perp$.
If $m\notin U$, extend a basis of $U$ by $m$ to a basis of $M$; the coordinate functional of $m$ lies in $U^\perp$ and does not vanish at $m$, so $m\notin(U^\perp)^\perp$.
\end{proof}
\end{supplementary}

\begin{theorem}\label{thm:quadratic-involution}
Quadratic duality is an involution: evaluation induces an $S$-preserving isomorphism of graded algebras
\[
(A^!)^!\cong A.
\]
\end{theorem}

\begin{proof}
\emph{Generators.} Evaluation $\mathrm{ev}_V:V\xrightarrow{\sim}D(D(V))$ is a bimodule isomorphism by Lemma~\ref{lem:linear-bidual} and \eqref{eq:linear-bimodule-dual-action}; it identifies the generators of $A$ and $(A^!)^!$.

\emph{Relations.} The relations of $(A^!)^!$ are $(R^\perp)^\perp\subset D(D(V))\otimes_S D(D(V))$, formed with the map $\theta$ for the bimodule $D(V)$.
By \eqref{eq:linear-bimodule-dual-action}, $(\lambda e_i)(w)=\lambda(e_iw)$ and $(e_i\mu)(v)=\mu(ve_i)$, so for $v,w\in V$ and $\lambda,\mu\in D(V)$,
\begin{equation}\label{eq:bidual-tensor-square}
\theta\bigl(\mathrm{ev}_V(v)\otimes\mathrm{ev}_V(w)\bigr)(\lambda\otimes\mu)
=\sum_{i=1}^n\mathrm{ev}_V(w)(\lambda e_i)\,\mathrm{ev}_V(v)(e_i\mu)
=\theta(\lambda\otimes\mu)(v\otimes w).
\end{equation}
Thus $\mathrm{ev}_V\otimes\mathrm{ev}_V$ is the evaluation identification of $V\otimes_S V$ with the dual of $D(V\otimes_S V)\cong D(V)\otimes_S D(V)$.
Lemma~\ref{lem:double-orthogonal}, applied to $R\subset V\otimes_S V$, identifies $(R^\perp)^\perp$ with $R$.
The presentations \eqref{eq:quadratic-duals} therefore give an $S$-preserving isomorphism of graded algebras $(A^!)^!\cong A$.
\end{proof}

\begin{remark}[General $S$]
For an arbitrary finite-dimensional semisimple $S$, the map $\theta$, and hence Definition~\ref{def:quadratic-duals}, needs a choice of symmetrising form.
The choice-free version uses the right and left $S$-duals: the right and left quadratic duals below satisfy ${}^!(A^!)\cong A\cong({}^!A)^!$ with no choice (Theorem~\ref{thm:quadratic-bidual}, advanced).
\end{remark}

\begin{advanced}
\emph{Quadratic duals via one-sided $S$-duals.}
For an arbitrary finite-dimensional semisimple $S$, we use the isomorphisms $\theta_r,\theta_\ell$ of \eqref{eq:tensor-duals} instead of $\theta$.

\begin{definition}\label{def:S-quadratic-duals}
The \defn{right quadratic dual} and \defn{left quadratic dual} of $A$ are
\begin{equation}\label{eq:S-quadratic-duals}
\begin{aligned}
A^!&:=T_S(V^*)/(R^\perp),
&R^\perp&=\{F\in V^*\otimes_S V^*\mid\theta_r(F)(R)=0\},\\
{}^!A&:=T_S({}^*V)/({}^\perp R),
&{}^\perp R&=\{F\in{}^*V\otimes_S{}^*V\mid\theta_\ell(F)(R)=0\}.
\end{aligned}
\end{equation}
\end{definition}

Under Assumption~\ref{ass:basic-semisimple}, the map $\alpha_V:V^*\to D(V)$, $f\mapsto\tau_S\circ f$, of Theorem~\ref{prop:dual-comparison} satisfies $\theta\circ(\alpha_V\otimes\alpha_V)=\alpha_{V\otimes_SV}\circ\theta_r$: both sides send $g\otimes f$ to $v\otimes w\mapsto\tau_S(g(f(v)w))$, because $\sum_i\tau_S(se_i)e_i=s$ for $s\in S$.
Hence $\alpha_V$ induces an isomorphism from the right quadratic dual onto the quadratic dual of Definition~\ref{def:quadratic-duals}; this is why we use the same symbol $A^!$.

Our notation is swapped relative to \cite[\S2.7 and Definition~2.8.1]{BGS96}: their $V^*$ uses left $S$-linear maps and their ${}^*V$ uses right $S$-linear maps.
Thus our $A^!$ is their ${}^!A$, and our ${}^!A$ is their $A^!$.
The names agree: they also call ${}^!A$ the right dual and $A^!$ the left dual.

\begin{lemma}\label{lem:S-double-orthogonal}
Let $U\subset M$ be an $S$-sub-bimodule of a finite-dimensional bimodule $ {}_SM_S$.
Under $M\cong{}^*(M^*)$ and $M\cong({}^*M)^*$ from the right and left $S$-dualities in Lemma~\ref{lem:S-bidual},
\[
{}^\perp(U^\perp)=U,\qquad ({}^\perp U)^\perp=U.
\]
\end{lemma}

\begin{proof}
For $u\in U$ and $f\in U^\perp$, evaluation $\mathrm{ev}_M:M\to{}^*(M^*)$ gives $\mathrm{ev}_M(u)(f)=f(u)=0$, so $U\subset{}^\perp(U^\perp)$ under Lemma~\ref{lem:S-bidual}.

Conversely, suppose that there is some $m\notin U$, semisimplicity of $S$ implies (by Corollary~\ref{cor:semisimple-summands}) that $M/U\hookrightarrow S^{\oplus n}$ as a right $S$-module for some $n$.
Consider the composition $M\onto M/U\hookrightarrow S^{\oplus n}\twoheadrightarrow S$ which sends $m$ to a non-zero element in a direct summand of $S^{\oplus n}$.
Then this is a right $S$-linear map in $\Hom_S(M,S)=M^*$ satisfying $f(U)=0$ and $f(m)\neq0$.
Thus $f\in U^\perp$ and $m\notin{}^\perp(U^\perp)$.
The proof of $({}^\perp U)^\perp=U$ is similar.
\end{proof}

\begin{theorem}\label{thm:quadratic-bidual}
Left and right quadratic duality are canonically inverse:
\[
{}^!(A^!)\cong A\cong({}^!A)^!
\quad\text{by }S\text{-preserving isomorphisms of graded algebras}.
\]
\end{theorem}

\begin{proof}
\emph{Generators.} The right $S$-duality in Lemma~\ref{lem:S-bidual} gives
$\mathrm{ev}_V:V\xrightarrow{\sim}{}^*(V^*)$, $v\mapsto(f\mapsto f(v))$, identifying the generators of $A$ and $ {}^!(A^!)$.
It preserves both $S$-actions by \eqref{eq:bimodule-dual-actions}.

\emph{Relations.} The right $S$-action on $V^*$ is $(gs)(w)=g(sw)$ for all $g\in V^*$, $s\in S$, and $w\in V$.
Applying \eqref{eq:tensor-evaluations} first to $V^*\otimes_S V^*$ and then to $V\otimes_S V$ gives, for all $v,w\in V$ and $f,g\in V^*$,
\begin{equation}\label{eq:S-bidual-tensor-square}
\begin{aligned}
\theta_\ell(\mathrm{ev}_V(v)\otimes\mathrm{ev}_V(w))(g\otimes f)
&=\mathrm{ev}_V(w)(g f(v))=g(f(v)w)\\
&=\mathrm{ev}_{V\otimes_S V}(v\otimes w)(\theta_r(g\otimes f)).
\end{aligned}
\end{equation}
Thus $\mathrm{ev}_V\otimes\mathrm{ev}_V$ is the bidual identification for $V\otimes_S V$ under anti-distributivity of the $S$-dual \eqref{eq:tensor-duals}.
Lemma~\ref{lem:S-double-orthogonal}, applied to $R\subset V\otimes_S V$, identifies the relations $ {}^\perp(R^\perp)$ of $ {}^!(A^!)$ with $R$.
The presentations \eqref{eq:S-quadratic-duals} therefore give an $S$-preserving isomorphism of graded algebras $ {}^!(A^!)\cong A$.
Interchanging left and right gives $({}^!A)^!\cong A$.
\end{proof}

\begin{proposition}\label{prop:quadratic-dual-sides}
A choice of symmetrising form $\tau:S\to\Bbbk$ gives $S$-preserving isomorphisms of graded algebras $A^!\cong{}^!A$ and $(A^!)^!\cong A$.
\end{proposition}

\begin{proof}
The maps $\alpha_V(f)=\tau\circ f$ and $\beta_V(g)=\tau\circ g$ in \eqref{eq:dual-comparison} give a bimodule isomorphism $\beta_V^{-1}\alpha_V:V^*\to{}^*V$.
For $f,g\in V^*$, write $f'=\beta_V^{-1}\alpha_V(f)$ and $g'=\beta_V^{-1}\alpha_V(g)$. Then
\[
\begin{aligned}
\tau\bigl(f'(vg'(w))\bigr)
&=\tau\bigl(f(v)g'(w)\bigr)
=\tau\bigl(g'(f(v)w)\bigr)\\
&=\tau\bigl(g(f(v)w)\bigr)
\qquad(v,w\in V).
\end{aligned}
\]
By \eqref{eq:orthogonal-comparison}, $(\beta_V^{-1}\alpha_V)^{\otimes_S2}$ therefore identifies $R^\perp$ with ${}^\perp R$.
The bimodule map $\beta_V^{-1}\circ\alpha_V$ extends by Proposition~\ref{prop:tensor-universal} to an isomorphism $T_S(V^*)\to T_S({}^*V)$ and hence descends to $A^!\cong{}^!A$.
Apply the same comparison to $A^!$ and then Theorem~\ref{thm:quadratic-bidual} to obtain $(A^!)^!\cong{}^!(A^!)\cong A$.
\end{proof}

For an arbitrary finite-dimensional semisimple $S$, the isomorphism $A^!\cong{}^!A$ of Proposition~\ref{prop:quadratic-dual-sides} depends on $\tau$; changing $\tau$ changes it by the central unit of Remark~\ref{rem:general-S-comparison}.
Theorem~\ref{thm:quadratic-bidual} involves no choice.
\end{advanced}
```

</details>

---
<a id="replacement-7"></a>

## Replacement 7: Lecture 3: dependent edits

These are the replacements $V^*\to D(V)$, $\theta_r\to\theta$ and ${}^!(\cdot)\to(\cdot)^!$ wherever the main text used the one-sided version. In the monomial proof the pairing value is now $1$ instead of $e_\ell$. The advanced tensor-product proof gains one sentence saying that it uses the right $S$-dual description.

### Passage 1: tensor algebra and square-zero algebra

**Location:** [Lecture_Koszul_S3.tex:202](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:202) (current lines 202–203)  
**Change size:** 2 lines added; 2 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -202,2 +223,2 @@
-&=T_S(V^*)/(V^*\otimes_S V^*)\cong S\oplus V^*,\\
-\bigl(T_S(V)/(V\otimes_S V)\bigr)^!&=T_S(V^*).
+&=T_S(D(V))/(D(V)\otimes_S D(V))\cong S\oplus D(V),\\
+\bigl(T_S(V)/(V\otimes_S V)\bigr)^!&=T_S(D(V)).
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
&=T_S(V^*)/(V^*\otimes_S V^*)\cong S\oplus V^*,\\
\bigl(T_S(V)/(V\otimes_S V)\bigr)^!&=T_S(V^*).
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
&=T_S(D(V))/(D(V)\otimes_S D(V))\cong S\oplus D(V),\\
\bigl(T_S(V)/(V\otimes_S V)\bigr)^!&=T_S(D(V)).
```

</details>

### Passage 2: trivial extension

**Location:** [Lecture_Koszul_S3.tex:206](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:206) (current line 206)  
**Change size:** 1 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -206,1 +227,1 @@
-In $S\oplus V^*$, $(V^*)^2=0$ and $(s,f)(t,g)=(st,sg+ft)$; this construction is also known as \emph{trivial extension of $S$ by $V^*$}.
+In $S\oplus D(V)$, $D(V)^2=0$ and $(s,f)(t,g)=(st,sg+ft)$; this construction is also known as \emph{trivial extension of $S$ by $D(V)$}.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
In $S\oplus V^*$, $(V^*)^2=0$ and $(s,f)(t,g)=(st,sg+ft)$; this construction is also known as \emph{trivial extension of $S$ by $V^*$}.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
In $S\oplus D(V)$, $D(V)^2=0$ and $(s,f)(t,g)=(st,sg+ft)$; this construction is also known as \emph{trivial extension of $S$ by $D(V)$}.
```

</details>

### Passage 3: dual basis $b^*$

**Location:** [Lecture_Koszul_S3.tex:223](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:223) (current lines 223–228)  
**Change size:** 5 lines added; 4 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -223,6 +244,7 @@
-For $b\in\mathcal B_{ij}$, define the right $S$-linear map $b^*:V\to S$ by its values on $\mathcal B$:
+For $b\in\mathcal B_{ij}$, define the functional $b^*\in D(V)$ by its values on $\mathcal B$:
 \begin{equation}\label{eq:dual-basis-idempotents}
-b^*(c)=\delta_{bc}e_j\quad(c\in\mathcal B),
-\qquad e_jb^*e_i=b^*.
+b^*(c)=\delta_{bc}\quad(c\in\mathcal B),
+\qquad e_jb^*e_i=b^*,
 \end{equation}
-The elements $b^*$ form a $\Bbbk$-basis of $V^*$; the left and right local units of each basis element are reversed.
+where the second identity follows from \eqref{eq:dual-blocks}.
+The elements $b^*$ form the dual $\Bbbk$-basis of $D(V)$; the left and right local units of each basis element are reversed.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
For $b\in\mathcal B_{ij}$, define the right $S$-linear map $b^*:V\to S$ by its values on $\mathcal B$:
\begin{equation}\label{eq:dual-basis-idempotents}
b^*(c)=\delta_{bc}e_j\quad(c\in\mathcal B),
\qquad e_jb^*e_i=b^*.
\end{equation}
The elements $b^*$ form a $\Bbbk$-basis of $V^*$; the left and right local units of each basis element are reversed.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
For $b\in\mathcal B_{ij}$, define the functional $b^*\in D(V)$ by its values on $\mathcal B$:
\begin{equation}\label{eq:dual-basis-idempotents}
b^*(c)=\delta_{bc}\quad(c\in\mathcal B),
\qquad e_jb^*e_i=b^*,
\end{equation}
where the second identity follows from \eqref{eq:dual-blocks}.
The elements $b^*$ form the dual $\Bbbk$-basis of $D(V)$; the left and right local units of each basis element are reversed.
```

</details>

### Passage 4: monomial dual proof

**Location:** [Lecture_Koszul_S3.tex:246](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:246) (current lines 246–252)  
**Change size:** 4 lines added; 4 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -246,7 +268,7 @@
-For $b\in\mathcal B_{ij}$ and $c\in\mathcal B_{j\ell}$, \eqref{eq:tensor-evaluations} and \eqref{eq:dual-basis-idempotents} give
+For $b\in\mathcal B_{ij}$ and $c\in\mathcal B_{j\ell}$, \eqref{eq:D-tensor-duals} and \eqref{eq:dual-basis-idempotents} give
 \[
-\theta_r(c^*\otimes b^*)(b\otimes c)=c^*(e_jc)=e_\ell.
+\theta(c^*\otimes b^*)(b\otimes c)=\sum_{k=1}^n b^*(be_k)\,c^*(e_kc)=b^*(b)\,c^*(c)=1.
 \]
 The functional vanishes on every other basis tensor.
-By Lemma~\ref{lem:idempotent-tensors}, the composable $c^*\otimes b^*$ form a basis of $V^*\otimes_S V^*$.
-Evaluating a linear combination on each $b\otimes c\in\mathcal R$ forces precisely the coefficient of $c^*\otimes b^*$ to be zero, since $e_\ell\neq0$.
+By Lemma~\ref{lem:idempotent-tensors}, the composable $c^*\otimes b^*$ form a basis of $D(V)\otimes_S D(V)$.
+Evaluating a linear combination on each $b\otimes c\in\mathcal R$ forces precisely the coefficient of $c^*\otimes b^*$ to be zero.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
For $b\in\mathcal B_{ij}$ and $c\in\mathcal B_{j\ell}$, \eqref{eq:tensor-evaluations} and \eqref{eq:dual-basis-idempotents} give
\[
\theta_r(c^*\otimes b^*)(b\otimes c)=c^*(e_jc)=e_\ell.
\]
The functional vanishes on every other basis tensor.
By Lemma~\ref{lem:idempotent-tensors}, the composable $c^*\otimes b^*$ form a basis of $V^*\otimes_S V^*$.
Evaluating a linear combination on each $b\otimes c\in\mathcal R$ forces precisely the coefficient of $c^*\otimes b^*$ to be zero, since $e_\ell\neq0$.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
For $b\in\mathcal B_{ij}$ and $c\in\mathcal B_{j\ell}$, \eqref{eq:D-tensor-duals} and \eqref{eq:dual-basis-idempotents} give
\[
\theta(c^*\otimes b^*)(b\otimes c)=\sum_{k=1}^n b^*(be_k)\,c^*(e_kc)=b^*(b)\,c^*(c)=1.
\]
The functional vanishes on every other basis tensor.
By Lemma~\ref{lem:idempotent-tensors}, the composable $c^*\otimes b^*$ form a basis of $D(V)\otimes_S D(V)$.
Evaluating a linear combination on each $b\otimes c\in\mathcal R$ forces precisely the coefficient of $c^*\otimes b^*$ to be zero.
```

</details>

### Passage 5: Example `ex:An-quadratic-dual`

**Location:** [Lecture_Koszul_S3.tex:259](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:259) (current line 259)  
**Change size:** 1 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -259,1 +281,1 @@
-There are no quadratic relations, so $A^!$ has the reversed generators $e_{i,i+1}^*\in e_{i+1,i+1}V^*e_{ii}$ and every composable product of two generators is zero.
+There are no quadratic relations, so $A^!$ has the reversed generators $e_{i,i+1}^*\in e_{i+1,i+1}D(V)e_{ii}$ and every composable product of two generators is zero.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
There are no quadratic relations, so $A^!$ has the reversed generators $e_{i,i+1}^*\in e_{i+1,i+1}V^*e_{ii}$ and every composable product of two generators is zero.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
There are no quadratic relations, so $A^!$ has the reversed generators $e_{i,i+1}^*\in e_{i+1,i+1}D(V)e_{ii}$ and every composable product of two generators is zero.
```

</details>

### Passage 6: alternating example (supplementary)

**Location:** [Lecture_Koszul_S3.tex:291](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:291) (current line 291)  
**Change size:** 1 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -291,1 +313,1 @@
-A^!=T_S(V^*)/(a^*b^*),\qquad
+A^!=T_S(D(V))/(a^*b^*),\qquad
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
A^!=T_S(V^*)/(a^*b^*),\qquad
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
A^!=T_S(D(V))/(a^*b^*),\qquad
```

</details>

### Passage 7: symmetric/exterior proof

**Location:** [Lecture_Koszul_S3.tex:317](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:317) (current lines 317–320)  
**Change size:** 2 lines added; 2 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -317,4 +339,4 @@
-Here $S=\Bbbk$, and the evaluation \eqref{eq:tensor-evaluations} reads
+Here $S=\Bbbk$, and \eqref{eq:D-tensor-duals} reads
 \[
-\theta_r(x_j^*\otimes x_i^*)(x_p\otimes x_q)=\delta_{ip}\delta_{jq}.
+\theta(x_j^*\otimes x_i^*)(x_p\otimes x_q)=x_i^*(x_p)\,x_j^*(x_q)=\delta_{ip}\delta_{jq}.
 \]
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
Here $S=\Bbbk$, and the evaluation \eqref{eq:tensor-evaluations} reads
\[
\theta_r(x_j^*\otimes x_i^*)(x_p\otimes x_q)=\delta_{ip}\delta_{jq}.
\]
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
Here $S=\Bbbk$, and \eqref{eq:D-tensor-duals} reads
\[
\theta(x_j^*\otimes x_i^*)(x_p\otimes x_q)=x_i^*(x_p)\,x_j^*(x_q)=\delta_{ip}\delta_{jq}.
\]
```

</details>

### Passage 8: tensor products (advanced)

**Location:** [Lecture_Koszul_S3.tex:417](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:417) (current line 417)  
**Change size:** 1 lines added; 0 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -417,1 +439,2 @@
+We use the description of quadratic duals by right $S$-duals (advanced material in Section~\ref{sec:quadratic-dual}), which applies to the semisimple algebra $S\otimes_\Bbbk T$ and agrees with Definition~\ref{def:quadratic-duals} when $S\otimes_\Bbbk T$ is a product of copies of $\Bbbk$.
 The right $(S\otimes_\Bbbk T)$-duals of the two generator summands are $V^*\otimes_\Bbbk T$ and $S\otimes_\Bbbk W^*$, with evaluations
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
The right $(S\otimes_\Bbbk T)$-duals of the two generator summands are $V^*\otimes_\Bbbk T$ and $S\otimes_\Bbbk W^*$, with evaluations
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
We use the description of quadratic duals by right $S$-duals (advanced material in Section~\ref{sec:quadratic-dual}), which applies to the semisimple algebra $S\otimes_\Bbbk T$ and agrees with Definition~\ref{def:quadratic-duals} when $S\otimes_\Bbbk T$ is a product of copies of $\Bbbk$.
The right $(S\otimes_\Bbbk T)$-duals of the two generator summands are $V^*\otimes_\Bbbk T$ and $S\otimes_\Bbbk W^*$, with evaluations
```

</details>

### Passage 9: exercise

**Location:** [Lecture_Koszul_S3.tex:501](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:501) (current line 501)  
**Change size:** 1 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -501,1 +524,1 @@
-A^!=T_S(V^*),\qquad h_A(t)=I_n+tC,\qquad
+A^!=T_S(D(V)),\qquad h_A(t)=I_n+tC,\qquad
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
A^!=T_S(V^*),\qquad h_A(t)=I_n+tC,\qquad
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
A^!=T_S(D(V)),\qquad h_A(t)=I_n+tC,\qquad
```

</details>

### Passage 10: exercise hint

**Location:** [Lecture_Koszul_S3.tex:506](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:506) (current line 506)  
**Change size:** 1 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -506,1 +529,1 @@
-\emph{Hint for (1).} Find $(V\otimes_S V)^\perp$ and compute the multiplicities $[e_iV^*:e_jS]$.
+\emph{Hint for (1).} Find $(V\otimes_S V)^\perp$ and compute the multiplicities $[e_iD(V):e_jS]$.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\emph{Hint for (1).} Find $(V\otimes_S V)^\perp$ and compute the multiplicities $[e_iV^*:e_jS]$.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\emph{Hint for (1).} Find $(V\otimes_S V)^\perp$ and compute the multiplicities $[e_iD(V):e_jS]$.
```

</details>

### Passage 11: advanced exercise

**Location:** [Lecture_Koszul_S3.tex:519](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S3.tex:519) (current lines 519–520)  
**Change size:** 2 lines added; 2 lines removed.

```diff
--- a/Lecture_Koszul_S3.tex
+++ b/Lecture_Koszul_S3.tex
@@ -519,2 +542,2 @@
-\item Using $\theta_r$, compute $R_\lambda^\perp$ and a presentation of $A_\lambda^!$ for every $\lambda$, including $\lambda=0$.
-\item Compute ${}^!(A_\lambda^!)$ and recover the relation $ab-\lambda cd$ under the canonical identification ${}^*(V^*)\cong V$.
+\item Using $\theta$, compute $R_\lambda^\perp$ and a presentation of $A_\lambda^!$ for every $\lambda$, including $\lambda=0$.
+\item Compute $(A_\lambda^!)^!$ and recover the relation $ab-\lambda cd$ under the canonical identification $D(D(V))\cong V$.
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
\item Using $\theta_r$, compute $R_\lambda^\perp$ and a presentation of $A_\lambda^!$ for every $\lambda$, including $\lambda=0$.
\item Compute ${}^!(A_\lambda^!)$ and recover the relation $ab-\lambda cd$ under the canonical identification ${}^*(V^*)\cong V$.
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
\item Using $\theta$, compute $R_\lambda^\perp$ and a presentation of $A_\lambda^!$ for every $\lambda$, including $\lambda=0$.
\item Compute $(A_\lambda^!)^!$ and recover the relation $ab-\lambda cd$ under the canonical identification $D(D(V))\cong V$.
```

</details>

---
<a id="replacement-8"></a>

## Replacement 8: Main file: Convention sentence, drafting note and notation list

The Convention now states that the main text uses only $D$ and $\mathbb D$. The `%` drafting note records the new rule for later lectures, including the Yoneda-algebra step: under the assumption $\tau_S$ identifies $A_1^*$ with $D(A_1)$ canonically, while general $S$ needs one-sided $S$-duals or a chosen $\tau$. In the notation list, $\theta$, the $D$-orthogonal complement and the $D$-based $A^!$ get main-text entries, and the one-sided entries are marked advanced (the simple substitutions are under Mechanical Corrections).

### Passage 1: Convention and drafting note

**Location:** [Lecture_Koszul.tex:251](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:251) (current lines 251–269)  
**Change size:** 19 lines added; 13 lines removed.

```diff
--- a/Lecture_Koszul.tex
+++ b/Lecture_Koszul.tex
@@ -251,19 +251,25 @@
-From Assumption~\ref{ass:basic-semisimple} onwards, the semisimple algebra $S$ is $\bigoplus_i\Bbbk e_i$ unless stated otherwise; remarks headed \emph{General $S$} explain what changes for an arbitrary finite-dimensional semisimple $S$.
+From Assumption~\ref{ass:basic-semisimple} onwards, the semisimple algebra $S$ is $\bigoplus_i\Bbbk e_i$ unless stated otherwise, and the main text uses only the $\Bbbk$-linear duals $D$ and $\bbD$; one-sided $S$-duals appear only in advanced material.
+Remarks headed \emph{General $S$} explain what changes for an arbitrary finite-dimensional semisimple $S$.
 % ---------------------------------------------------------------------------
-% DRAFTING NOTE (standing assumption; Change Proposal 14).
-% The lectures assume S = A_0 = \bigoplus_i \Bbbk e_i (ass:basic-semisimple),
-% with the standard symmetrising form \tau_S(e_i)=1. When drafting later lectures:
+% DRAFTING NOTE (standing assumption; Change Proposals 14 and 15).
+% The lectures assume S = A_0 = \bigoplus_i \Bbbk e_i (ass:basic-semisimple).
+% The MAIN TEXT uses only the k-linear duals D and \bbD, with
+%   \theta(\lambda\otimes\mu)(v\otimes w) = \sum_i \mu(v e_i)\lambda(e_i w)
+% (prop:D-tensor-duals) and A^! = T_S(D(V))/(R^\perp) (def:quadratic-duals).
+% One-sided S-duals (V^*, {}^*V, \theta_r, \theta_\ell, left/right quadratic
+% duals, symmetrising forms, \tau_S) live ONLY in advanced blocks.
+% When drafting later lectures:
 %  * Keep statements that are already proved for general f.d. semisimple S general.
-%  * Add a remark \begin{remark}[General $S$] ... \end{remark} wherever an argument
-%    uses \tau_S, identifies an S-dual with a k-linear dual (D or \bbD), counts
-%    multiplicities or Hilbert series via coordinate idempotents, or otherwise
-%    uses S = \bigoplus_i \Bbbk e_i.
+%  * Add a remark \begin{remark}[General $S$] ... \end{remark} wherever the main
+%    text uses the coordinate idempotents (e.g. the formula for \theta, dual bases
+%    b^*, Hilbert series and dimension vectors), or where general S would need
+%    one-sided S-duals or a chosen symmetrising form.
 %  * In particular, the identification of the Yoneda algebra
 %    E(A) = Ext^\bullet_A(A_0,A_0) with the quadratic dual (or its opposite):
-%    with right S-duals, Ext^1_A(A_0,A_0) \cong Hom_S(A_1,S) = A_1^* canonically
-%    for A generated in degree 1 and any f.d. semisimple S (cf. BGS Thm 2.10.1);
-%    any step through D(A_1) or \bbD needs a chosen \tau for general S.
+%    Ext^1_A(A_0,A_0) \cong Hom_S(A_1,S) = A_1^* canonically for A generated in
+%    degree 1 and any f.d. semisimple S (cf. BGS Thm 2.10.1). Under the standing
+%    assumption, \tau_S identifies A_1^* with D(A_1) canonically; for general S,
+%    matching this with A^! needs one-sided S-duals or a chosen \tau.
 %  * Likewise: the numerical identity h_A(t)h_{A^!}(-t)^T = I (BGS Lemma 2.11.1
-%    assumes A_0 = \bigoplus F1_x), Koszul complexes written with D instead of
-%    S-duals, and the Koszul duality functor.
+%    assumes A_0 = \bigoplus F1_x), the Koszul complex, and the Koszul duality functor.
 % ---------------------------------------------------------------------------
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
From Assumption~\ref{ass:basic-semisimple} onwards, the semisimple algebra $S$ is $\bigoplus_i\Bbbk e_i$ unless stated otherwise; remarks headed \emph{General $S$} explain what changes for an arbitrary finite-dimensional semisimple $S$.
% ---------------------------------------------------------------------------
% DRAFTING NOTE (standing assumption; Change Proposal 14).
% The lectures assume S = A_0 = \bigoplus_i \Bbbk e_i (ass:basic-semisimple),
% with the standard symmetrising form \tau_S(e_i)=1. When drafting later lectures:
%  * Keep statements that are already proved for general f.d. semisimple S general.
%  * Add a remark \begin{remark}[General $S$] ... \end{remark} wherever an argument
%    uses \tau_S, identifies an S-dual with a k-linear dual (D or \bbD), counts
%    multiplicities or Hilbert series via coordinate idempotents, or otherwise
%    uses S = \bigoplus_i \Bbbk e_i.
%  * In particular, the identification of the Yoneda algebra
%    E(A) = Ext^\bullet_A(A_0,A_0) with the quadratic dual (or its opposite):
%    with right S-duals, Ext^1_A(A_0,A_0) \cong Hom_S(A_1,S) = A_1^* canonically
%    for A generated in degree 1 and any f.d. semisimple S (cf. BGS Thm 2.10.1);
%    any step through D(A_1) or \bbD needs a chosen \tau for general S.
%  * Likewise: the numerical identity h_A(t)h_{A^!}(-t)^T = I (BGS Lemma 2.11.1
%    assumes A_0 = \bigoplus F1_x), Koszul complexes written with D instead of
%    S-duals, and the Koszul duality functor.
% ---------------------------------------------------------------------------
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
From Assumption~\ref{ass:basic-semisimple} onwards, the semisimple algebra $S$ is $\bigoplus_i\Bbbk e_i$ unless stated otherwise, and the main text uses only the $\Bbbk$-linear duals $D$ and $\bbD$; one-sided $S$-duals appear only in advanced material.
Remarks headed \emph{General $S$} explain what changes for an arbitrary finite-dimensional semisimple $S$.
% ---------------------------------------------------------------------------
% DRAFTING NOTE (standing assumption; Change Proposals 14 and 15).
% The lectures assume S = A_0 = \bigoplus_i \Bbbk e_i (ass:basic-semisimple).
% The MAIN TEXT uses only the k-linear duals D and \bbD, with
%   \theta(\lambda\otimes\mu)(v\otimes w) = \sum_i \mu(v e_i)\lambda(e_i w)
% (prop:D-tensor-duals) and A^! = T_S(D(V))/(R^\perp) (def:quadratic-duals).
% One-sided S-duals (V^*, {}^*V, \theta_r, \theta_\ell, left/right quadratic
% duals, symmetrising forms, \tau_S) live ONLY in advanced blocks.
% When drafting later lectures:
%  * Keep statements that are already proved for general f.d. semisimple S general.
%  * Add a remark \begin{remark}[General $S$] ... \end{remark} wherever the main
%    text uses the coordinate idempotents (e.g. the formula for \theta, dual bases
%    b^*, Hilbert series and dimension vectors), or where general S would need
%    one-sided S-duals or a chosen symmetrising form.
%  * In particular, the identification of the Yoneda algebra
%    E(A) = Ext^\bullet_A(A_0,A_0) with the quadratic dual (or its opposite):
%    Ext^1_A(A_0,A_0) \cong Hom_S(A_1,S) = A_1^* canonically for A generated in
%    degree 1 and any f.d. semisimple S (cf. BGS Thm 2.10.1). Under the standing
%    assumption, \tau_S identifies A_1^* with D(A_1) canonically; for general S,
%    matching this with A^! needs one-sided S-duals or a chosen \tau.
%  * Likewise: the numerical identity h_A(t)h_{A^!}(-t)^T = I (BGS Lemma 2.11.1
%    assumes A_0 = \bigoplus F1_x), the Koszul complex, and the Koszul duality functor.
% ---------------------------------------------------------------------------
```

</details>

### Passage 2: $\theta$ entry

**Location:** [Lecture_Koszul.tex:367](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:367) (current line 367)  
**Change size:** 2 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul.tex
+++ b/Lecture_Koszul.tex
@@ -367,1 +373,2 @@
-$\theta_r,\ \theta_\ell$ & Tensor-Hom comparison maps; anti-distributivity of the $S$-dual in the semisimple case. & \hyperref[eq:general-tensor-duals]{\pageref*{eq:general-tensor-duals}}\\[3pt]
+$\theta$ & Duals of tensor products: $D(W)\otimes_S D(V)\cong D(V\otimes_S W)$ for $S=\bigoplus_i\Bbbk e_i$. & \hyperref[prop:D-tensor-duals]{\pageref*{prop:D-tensor-duals}}\\[3pt]
+$\theta_r,\ \theta_\ell$ & Tensor-Hom comparison maps; anti-distributivity of the one-sided $S$-duals; advanced. & \hyperref[eq:general-tensor-duals]{\pageref*{eq:general-tensor-duals}}\\[3pt]
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
$\theta_r,\ \theta_\ell$ & Tensor-Hom comparison maps; anti-distributivity of the $S$-dual in the semisimple case. & \hyperref[eq:general-tensor-duals]{\pageref*{eq:general-tensor-duals}}\\[3pt]
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
$\theta$ & Duals of tensor products: $D(W)\otimes_S D(V)\cong D(V\otimes_S W)$ for $S=\bigoplus_i\Bbbk e_i$. & \hyperref[prop:D-tensor-duals]{\pageref*{prop:D-tensor-duals}}\\[3pt]
$\theta_r,\ \theta_\ell$ & Tensor-Hom comparison maps; anti-distributivity of the one-sided $S$-duals; advanced. & \hyperref[eq:general-tensor-duals]{\pageref*{eq:general-tensor-duals}}\\[3pt]
```

</details>

### Passage 3: $U^\perp$ entry

**Location:** [Lecture_Koszul.tex:380](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:380) (current line 380)  
**Change size:** 2 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul.tex
+++ b/Lecture_Koszul.tex
@@ -380,1 +387,2 @@
-$U^\perp,\ {}^\perp U$ & Right and left $S$-linear functionals vanishing on $U$. & \hyperref[def:orthogonals]{\pageref*{def:orthogonals}}\\[3pt]
+$U^\perp$ & Functionals in $D(M)$ vanishing on $U$. & \hyperref[def:D-orthogonal]{\pageref*{def:D-orthogonal}}\\[3pt]
+$U^\perp,\ {}^\perp U$ (one-sided) & Right and left $S$-linear functionals vanishing on $U$; advanced. & \hyperref[def:orthogonals]{\pageref*{def:orthogonals}}\\[3pt]
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
$U^\perp,\ {}^\perp U$ & Right and left $S$-linear functionals vanishing on $U$. & \hyperref[def:orthogonals]{\pageref*{def:orthogonals}}\\[3pt]
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
$U^\perp$ & Functionals in $D(M)$ vanishing on $U$. & \hyperref[def:D-orthogonal]{\pageref*{def:D-orthogonal}}\\[3pt]
$U^\perp,\ {}^\perp U$ (one-sided) & Right and left $S$-linear functionals vanishing on $U$; advanced. & \hyperref[def:orthogonals]{\pageref*{def:orthogonals}}\\[3pt]
```

</details>

### Passage 4: $A^!$ entry

**Location:** [Lecture_Koszul.tex:383](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex:383) (current line 383)  
**Change size:** 2 lines added; 1 lines removed.

```diff
--- a/Lecture_Koszul.tex
+++ b/Lecture_Koszul.tex
@@ -383,1 +391,2 @@
-$A^!,\ {}^!A$ & Right and left quadratic dual algebras. & \hyperref[def:quadratic-duals]{\pageref*{def:quadratic-duals}}\\[3pt]
+$A^!$ & Quadratic dual algebra $T_S(D(V))/(R^\perp)$. & \hyperref[def:quadratic-duals]{\pageref*{def:quadratic-duals}}\\[3pt]
+$A^!,\ {}^!A$ (one-sided) & Right and left quadratic duals via one-sided $S$-duals; advanced. & \hyperref[def:S-quadratic-duals]{\pageref*{def:S-quadratic-duals}}\\[3pt]
```

<details>
<summary><strong>Existing content</strong></summary>

```tex
$A^!,\ {}^!A$ & Right and left quadratic dual algebras. & \hyperref[def:quadratic-duals]{\pageref*{def:quadratic-duals}}\\[3pt]
```

</details>

<details>
<summary><strong>Proposed replacement</strong></summary>

```tex
$A^!$ & Quadratic dual algebra $T_S(D(V))/(R^\perp)$. & \hyperref[def:quadratic-duals]{\pageref*{def:quadratic-duals}}\\[3pt]
$A^!,\ {}^!A$ (one-sided) & Right and left quadratic duals via one-sided $S$-duals; advanced. & \hyperref[def:S-quadratic-duals]{\pageref*{def:S-quadratic-duals}}\\[3pt]
```

</details>

---

## Verification

**Checked by applying all changes to the files from Change Proposal 14 and compiling with empty S4–S5:**

- Compilation succeeds with no undefined references in Lectures 1–3. The old `eq:tensor-dual-actions` problem is gone, and no labels are multiply defined.
- Supplementary and advanced environments are balanced, with no nesting. Hidden solutions inside the new advanced exercise blocks are still excluded.
- The only main-text references into advanced blocks are the two pointers inside *General $S$* remarks.
- Mathematics checked by hand:
  - $\theta$ is balanced in both tensor products and is a bimodule map; blockwise it is the standard isomorphism $D(Y)\otimes D(X)\cong D(X\otimes Y)$.
  - $\theta(\mathrm{ev}_v\otimes\mathrm{ev}_w)(\lambda\otimes\mu)=\theta(\lambda\otimes\mu)(v\otimes w)$.
  - $\theta\circ(\alpha_V\otimes\alpha_V)=\alpha_{V\otimes V}\circ\theta_r$ under $\tau_S$.
  - In the monomial proof, $\theta(c^*\otimes b^*)(b\otimes c)=1$.
  - The symmetric/exterior computation is unchanged.
