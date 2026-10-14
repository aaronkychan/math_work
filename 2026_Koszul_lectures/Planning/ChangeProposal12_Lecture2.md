# Change Proposal 12: Lecture 2

> **Status: approved and applied on 15 October 2026.** All four replacements were applied after checking that the current source matched the reviewed snapshot, including the author's edits. The document was then split into the mother file and five lecture files, as requested.

**Current files:** [Mother file](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex), [Lecture 2](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S2.tex), and [compiled PDF](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.pdf). The source locations and exact passages below record the pre-split document. `2026_Koszul.tex` is now a compatibility entry point that inputs the mother file.

**Source:** [2026_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex)  
**Source snapshot:** 15 October 2026. The quoted passages include the author's latest edits.

## Mathematical Point

Equations (2.5)-(2.7) are not independent of tensor duality. Equation (2.5) states the semisimple tensor-duality isomorphisms, (2.6) defines those isomorphisms, and (2.7) recalls the bimodule actions from (1.15). Corollary 1.13 supplies the hypotheses placing the relevant modules in add S; it does not by itself construct the tensor-duality isomorphisms.

The general comparison proposition and its proof can therefore be optional advanced material, while the semisimple tensor-duality formulas remain part of the main course.

## Scope

- Put the general Hom-action construction, Proposition 2.6 with arbitrary outer targets X and Y, and its full proof inside one advanced block.
- Use `\add B` in assertions (1) and (2), explicitly specifying the right and left module categories.
- Keep equations (2.5), (2.6), and (2.7) exactly unchanged, with the same labels and outside both advanced and supplementary blocks.
- Add a direct reference from the main semisimple passage to the tensor-duality proposition.
- Make only the two necessary target-specification updates in the adjacent advanced examples.
- Preserve every percent-commented line. Do not change Lecture 1, Lectures 3-5, homework, diagram spacing, or hidden-material settings.

## Reading the Diff

Lines beginning with - are removed; lines beginning with + are added; other lines are context. Hunk headers use actual source line numbers; new line numbers assume earlier replacements have been applied. Full exact passages appear beneath each diff.

**Dependencies:** Replacement 2 should accompany Replacement 1 so the main formulas retain an explicit explanation. Replacements 3 and 4 specify the targets introduced by Replacement 1.

## Replacement Index

| No. | Change | Current lines | Added / removed |
| --- | --- | --- | --- |
| 1 | [Put the general Hom construction, comparison maps, and proof in advanced material](#replacement-1) | 1962-2053 | +50 / -44 |
| 2 | [Identify the main formulas explicitly as semisimple tensor duality](#replacement-2) | 2054 | +3 / -1 |
| 3 | [Specify the targets in the existing advanced counterexample](#replacement-3) | 2082 | +2 / -1 |
| 4 | [Specify the target in the existing advanced linear-dual application](#replacement-4) | 2093 | +1 / -1 |

---

<a id="replacement-1"></a>

## Replacement 1: Put the general Hom construction, comparison maps, and proof in advanced material

**Location:** [2026_Koszul.tex:1962](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1962)  
**Change size:** 50 lines added; 44 lines removed.

Generalise the outer targets to an arbitrary right C-module X and left A-module Y. Use add B in both isomorphism hypotheses, with the module side explicit. Assert a left outer action on Hom only when the target carries the required commuting action. Keep the entire general discussion and proof in one advanced block, without a nested supplementary block. Preserve the historical percent-commented TODO verbatim.

### Line-by-Line Diff

```diff
--- a/2026_Koszul.tex
+++ b/2026_Koszul.tex
@@ -1962,13 +1962,14 @@
-\comm{this is more general $\Hom_B(M,X)$ has $(B,A)$-bimodule action for any $X\in \Mod B$; then we don't need to do $A$ and $B$ separately....}
-Let $A,B,C$ be arbitrary $\Bbbk$-algebras, and consider bimodules ${}_AM_B$, ${}_BN_C$.
-The Hom spaces below carry the actions: for any $f\in\Hom_B(M,B)$ and $g\in \Hom_{A^\op}(M,A)$, we have
+\begin{advanced}
+Let $A,B,C$ be $\Bbbk$-algebras.
+For bimodules ${}_AM_B$, ${}_CX_B$, we have $\Hom_B(M,X)\in C\Mod A$, with
 \begin{equation}\label{eq:general-tensor-dual-actions}
-(bfa)(m)=bf(am) \text{ and } (bga)(m)=g(mb)a
-\quad \text{for all } a\in A,\ b\in B,\ m\in M.
+(cfa)(m)=cf(am)
+\quad(f\in\Hom_B(M,X),\ c\in C,\ a\in A,\ m\in M).
 \end{equation}
-Replacing $(A,B,M)$ by $(B,C,N)$ gives the actions on $\Hom_C(N,C)$ and $\Hom_{B^\op}(N,B)$.
+If $X\in\Mod B$ has no specified left action, the same formula defines the right $A$-action $(fa)(m)=f(am)$.
+The left-module version follows by passing to opposite algebras.
 
-\begin{proposition}[Tensor duality]\label{prop:tensor-duals}
+\begin{proposition}[Tensor and Hom]\label{prop:tensor-duals}
 % TODO (ChangeProposal9, Lecture 2 follow-up): Explain the general case for
 % an (A,B)-bimodule M and a (B,C)-bimodule N. For right duals, require M_B
 % finitely generated projective; for left duals, require _B N finitely generated
@@ -1976,78 +1977,83 @@
 % Keep the idempotent-matching calculation in the main exposition and move
 % routine verification to supplementary material. Use the one-sided bimodule
 % actions from eq:bimodule-dual-actions, independently of a symmetrising form.
-The following maps are left $C$-linear and right $A$-linear, natural in $M,N$, \comm{do these have to be $C$-dual and $B$-dual and $A$-dual?? general Hom-ing on fixed $C, B, A$-module (respectively) still OK??  Of course for (1) and (2), we need to specialise to $B$, but only for $B$ only??}
+Consider bimodules ${}_AM_B$, ${}_BN_C$, a right $C$-module $X$, and a left $A$-module $Y$.
+There are maps, natural in $M,N$,
 \begin{equation}\label{eq:general-tensor-duals}
 \begin{aligned}
-\theta_r:\Hom_C(N,C)\otimes_B\Hom_B(M,B)
-&\longrightarrow\Hom_C(M\otimes_B N,C),\\
+\theta_r:\Hom_C(N,X)\otimes_B\Hom_B(M,B)
+&\longrightarrow\Hom_C(M\otimes_B N,X),\\
 \theta_r(g\otimes f)(m\otimes n)&=g(f(m)n),\\
-\theta_\ell:\Hom_{B^\op}(N,B)\otimes_B\Hom_{A^\op}(M,A)
-&\longrightarrow\Hom_{A^\op}(M\otimes_B N,A),\\
+\theta_\ell:\Hom_{B^\op}(N,B)\otimes_B\Hom_{A^\op}(M,Y)
+&\longrightarrow\Hom_{A^\op}(M\otimes_B N,Y),\\
 \theta_\ell(g\otimes f)(m\otimes n)&=f(mg(n)).
 \end{aligned}
 \end{equation}
+The maps $\theta_r$ and $\theta_\ell$ are right $A$-linear and left $C$-linear, respectively.
 \begin{enumerate}
-\item The map $\theta_r$ is an isomorphism if $M$ is a direct summand of $B^{\oplus r}$ as a right $B$-module for some integer $r\geq0$.
-\item The map $\theta_\ell$ is an isomorphism if $N$ is a direct summand of $B^{\oplus r}$ as a left $B$-module for some integer $r\geq0$.
+\item The map $\theta_r$ is an isomorphism if $M\in\add B$ as a right $B$-module.
+\item The map $\theta_\ell$ is an isomorphism if $N\in\add B$ as a left $B$-module.
 \end{enumerate}
+Here $\add B$ is formed in the indicated module category, as in Example~\ref{ex:add-category}.
+If ${}_CX_C$ and ${}_AY_A$ are bimodules, the respective maps also preserve the additional actions and are morphisms in $C\Mod A$.
 \end{proposition}
 
-\begin{supplementary}
 \begin{proof}
 \emph{Well-definedness of $\theta_r$.}
-For $\theta_r$, the identities
+For $f\in\Hom_B(M,B)$, $g\in\Hom_C(N,X)$, and $b\in B$,
 \[
 g(f(mb)n)=g(f(m)bn),\qquad
-(gb)(f(m)n)=g(bf(m)n)=g((bf)(m)n)
-\quad(b\in B)
+(gb)(f(m)n)=g(bf(m)n)=g((bf)(m)n).
 \]
-respect the defining identities in both tensor products.
-The resulting functional is right $C$-linear, since $g(f(m)nc)=g(f(m)n)c$.
-The outer actions satisfy
+These identities respect the defining identifications in both tensor products.
+Right $C$-linearity follows from $g(f(m)nc)=g(f(m)n)c$ for $c\in C$.
+For $a\in A$,
 \[
-\theta_r(cg\otimes fa)(m\otimes n)
-=c\,g(f(am)n)=(c\,\theta_r(g\otimes f)a)(m\otimes n)
-\quad(c\in C,\ a\in A).
+\theta_r(g\otimes fa)(m\otimes n)
+=g(f(am)n)=(\theta_r(g\otimes f)a)(m\otimes n).
 \]
+If $X$ also has a commuting left $C$-action, replacing $g$ by $cg$ multiplies the value by $c$, so $\theta_r$ preserves that action as well.
 
 \emph{Bijectivity of $\theta_r$.}
 Regard $M$ only as a right $B$-module.
-When $M=B$, the maps
+For $M=B$, evaluation at $1$ identifies $\Hom_B(B,B)\cong B$, while multiplication identifies $B\otimes_B N\cong N$.
+Under these isomorphisms, $\theta_r$ becomes
 \[
-\Hom_B(B,B)\xrightarrow{\sim}B,\quad f\longmapsto f(1),
-\qquad B\otimes_B N\xrightarrow{\sim}N,\quad b\otimes n\longmapsto bn
+\Hom_C(N,X)\otimes_B B\longrightarrow\Hom_C(N,X),
+\qquad g\otimes b\longmapsto gb,
 \]
-turn $\theta_r$ into the isomorphism
-\[
-\Hom_C(N,C)\otimes_B B\longrightarrow\Hom_C(N,C),
-\qquad g\otimes b\longmapsto gb.
-\]
+which is an isomorphism by Lemma~\ref{lem:tensor-properties}(3).
 Finite direct sums commute with both constructions by Lemma~\ref{lem:tensor-properties}(4) and \eqref{eq:hom-finite-sums}.
-Hence $\theta_r$ is bijective for $M=B^{\oplus r}$.
-If $M\oplus M'\cong B^{\oplus r}$, the comparison for $M\oplus M'$ is the direct sum of the comparisons for $M$ and $M'$, so both summand maps are bijective.
+Thus $\theta_r$ is bijective for $M=B^{\oplus r}$, where $r\geq0$ is finite.
+If $M\in\add B$, choose $M'$ with $M\oplus M'\cong B^{\oplus r}$.
+The comparison for $M\oplus M'$ is the direct sum of the comparisons for $M$ and $M'$, so both summand maps are bijective.
 
 \emph{The left comparison.}
-For $\theta_\ell$, well-definedness follows from
+For $f\in\Hom_{A^\op}(M,Y)$ and $g\in\Hom_{B^\op}(N,B)$, well-definedness follows from
 \[
 f(mb\,g(n))=f(mg(bn)),\qquad
-f(m(gb)(n))=f(mg(n)b)=(bf)(mg(n)).
+f(m(gb)(n))=f(mg(n)b)=(bf)(mg(n))
+\quad(b\in B).
 \]
-Left $A$-linearity of $f$ gives left $A$-linearity of the resulting functional, and the outer actions satisfy
-$\theta_\ell(cg\otimes fa)(m\otimes n)=f(mg(nc))a$.
-For $N=B$ as a left module, evaluation at $1$ identifies
-$\Hom_{B^\op}(B,B)\cong B$ and turns $\theta_\ell$ into
+Left $A$-linearity of $f$ makes the resulting functional left $A$-linear.
+For $c\in C$,
 \[
-B\otimes_B\Hom_{A^\op}(M,A)\longrightarrow\Hom_{A^\op}(M,A),
+\theta_\ell(cg\otimes f)(m\otimes n)
+=f(mg(nc))=(c\theta_\ell(g\otimes f))(m\otimes n).
+\]
+If $Y$ also has a commuting right $A$-action, replacing $f$ by $fa$ multiplies the value by $a$, so $\theta_\ell$ preserves that action as well.
+For $N=B$ as a left module, evaluation at $1$ identifies $\Hom_{B^\op}(B,B)\cong B$ and turns $\theta_\ell$ into
+\[
+B\otimes_B\Hom_{A^\op}(M,Y)\longrightarrow\Hom_{A^\op}(M,Y),
 \qquad b\otimes f\longmapsto bf.
 \]
 The same finite-sum and direct-summand argument proves (2).
 
 \emph{Naturality.}
 Let $p:M\to M'$ and $q:N\to N'$ be bimodule maps.
-For $f\in\Hom_B(M',B)$ and $g\in\Hom_C(N',C)$, applying $\theta_r$ before or after precomposition gives $g(f(p(m))q(n))$ at $m\otimes n$.
-For $f\in\Hom_{A^\op}(M',A)$ and $g\in\Hom_{B^\op}(N',B)$, the two orders give $f(p(m)g(q(n)))$ for $\theta_\ell$.
+For $f\in\Hom_B(M',B)$ and $g\in\Hom_C(N',X)$, applying $\theta_r$ before or after precomposition gives $g(f(p(m))q(n))$ at $m\otimes n$.
+For $f\in\Hom_{A^\op}(M',Y)$ and $g\in\Hom_{B^\op}(N',B)$, the two orders give $f(p(m)g(q(n)))$ for $\theta_\ell$.
 Thus both comparisons are natural.
 \end{proof}
-\end{supplementary}
+\end{advanced}
 
```

<details>
<summary><strong>Existing content (exact)</strong></summary>

```tex
\comm{this is more general $\Hom_B(M,X)$ has $(B,A)$-bimodule action for any $X\in \Mod B$; then we don't need to do $A$ and $B$ separately....}
Let $A,B,C$ be arbitrary $\Bbbk$-algebras, and consider bimodules ${}_AM_B$, ${}_BN_C$.
The Hom spaces below carry the actions: for any $f\in\Hom_B(M,B)$ and $g\in \Hom_{A^\op}(M,A)$, we have
\begin{equation}\label{eq:general-tensor-dual-actions}
(bfa)(m)=bf(am) \text{ and } (bga)(m)=g(mb)a
\quad \text{for all } a\in A,\ b\in B,\ m\in M.
\end{equation}
Replacing $(A,B,M)$ by $(B,C,N)$ gives the actions on $\Hom_C(N,C)$ and $\Hom_{B^\op}(N,B)$.

\begin{proposition}[Tensor duality]\label{prop:tensor-duals}
% TODO (ChangeProposal9, Lecture 2 follow-up): Explain the general case for
% an (A,B)-bimodule M and a (B,C)-bimodule N. For right duals, require M_B
% finitely generated projective; for left duals, require _B N finitely generated
% projective. Finite k-dimension alone does not suffice over a general algebra.
% Keep the idempotent-matching calculation in the main exposition and move
% routine verification to supplementary material. Use the one-sided bimodule
% actions from eq:bimodule-dual-actions, independently of a symmetrising form.
The following maps are left $C$-linear and right $A$-linear, natural in $M,N$, \comm{do these have to be $C$-dual and $B$-dual and $A$-dual?? general Hom-ing on fixed $C, B, A$-module (respectively) still OK??  Of course for (1) and (2), we need to specialise to $B$, but only for $B$ only??}
\begin{equation}\label{eq:general-tensor-duals}
\begin{aligned}
\theta_r:\Hom_C(N,C)\otimes_B\Hom_B(M,B)
&\longrightarrow\Hom_C(M\otimes_B N,C),\\
\theta_r(g\otimes f)(m\otimes n)&=g(f(m)n),\\
\theta_\ell:\Hom_{B^\op}(N,B)\otimes_B\Hom_{A^\op}(M,A)
&\longrightarrow\Hom_{A^\op}(M\otimes_B N,A),\\
\theta_\ell(g\otimes f)(m\otimes n)&=f(mg(n)).
\end{aligned}
\end{equation}
\begin{enumerate}
\item The map $\theta_r$ is an isomorphism if $M$ is a direct summand of $B^{\oplus r}$ as a right $B$-module for some integer $r\geq0$.
\item The map $\theta_\ell$ is an isomorphism if $N$ is a direct summand of $B^{\oplus r}$ as a left $B$-module for some integer $r\geq0$.
\end{enumerate}
\end{proposition}

\begin{supplementary}
\begin{proof}
\emph{Well-definedness of $\theta_r$.}
For $\theta_r$, the identities
\[
g(f(mb)n)=g(f(m)bn),\qquad
(gb)(f(m)n)=g(bf(m)n)=g((bf)(m)n)
\quad(b\in B)
\]
respect the defining identities in both tensor products.
The resulting functional is right $C$-linear, since $g(f(m)nc)=g(f(m)n)c$.
The outer actions satisfy
\[
\theta_r(cg\otimes fa)(m\otimes n)
=c\,g(f(am)n)=(c\,\theta_r(g\otimes f)a)(m\otimes n)
\quad(c\in C,\ a\in A).
\]

\emph{Bijectivity of $\theta_r$.}
Regard $M$ only as a right $B$-module.
When $M=B$, the maps
\[
\Hom_B(B,B)\xrightarrow{\sim}B,\quad f\longmapsto f(1),
\qquad B\otimes_B N\xrightarrow{\sim}N,\quad b\otimes n\longmapsto bn
\]
turn $\theta_r$ into the isomorphism
\[
\Hom_C(N,C)\otimes_B B\longrightarrow\Hom_C(N,C),
\qquad g\otimes b\longmapsto gb.
\]
Finite direct sums commute with both constructions by Lemma~\ref{lem:tensor-properties}(4) and \eqref{eq:hom-finite-sums}.
Hence $\theta_r$ is bijective for $M=B^{\oplus r}$.
If $M\oplus M'\cong B^{\oplus r}$, the comparison for $M\oplus M'$ is the direct sum of the comparisons for $M$ and $M'$, so both summand maps are bijective.

\emph{The left comparison.}
For $\theta_\ell$, well-definedness follows from
\[
f(mb\,g(n))=f(mg(bn)),\qquad
f(m(gb)(n))=f(mg(n)b)=(bf)(mg(n)).
\]
Left $A$-linearity of $f$ gives left $A$-linearity of the resulting functional, and the outer actions satisfy
$\theta_\ell(cg\otimes fa)(m\otimes n)=f(mg(nc))a$.
For $N=B$ as a left module, evaluation at $1$ identifies
$\Hom_{B^\op}(B,B)\cong B$ and turns $\theta_\ell$ into
\[
B\otimes_B\Hom_{A^\op}(M,A)\longrightarrow\Hom_{A^\op}(M,A),
\qquad b\otimes f\longmapsto bf.
\]
The same finite-sum and direct-summand argument proves (2).

\emph{Naturality.}
Let $p:M\to M'$ and $q:N\to N'$ be bimodule maps.
For $f\in\Hom_B(M',B)$ and $g\in\Hom_C(N',C)$, applying $\theta_r$ before or after precomposition gives $g(f(p(m))q(n))$ at $m\otimes n$.
For $f\in\Hom_{A^\op}(M',A)$ and $g\in\Hom_{B^\op}(N',B)$, the two orders give $f(p(m)g(q(n)))$ for $\theta_\ell$.
Thus both comparisons are natural.
\end{proof}
\end{supplementary}

```

</details>

<details>
<summary><strong>Proposed replacement (exact)</strong></summary>

```tex
\begin{advanced}
Let $A,B,C$ be $\Bbbk$-algebras.
For bimodules ${}_AM_B$, ${}_CX_B$, we have $\Hom_B(M,X)\in C\Mod A$, with
\begin{equation}\label{eq:general-tensor-dual-actions}
(cfa)(m)=cf(am)
\quad(f\in\Hom_B(M,X),\ c\in C,\ a\in A,\ m\in M).
\end{equation}
If $X\in\Mod B$ has no specified left action, the same formula defines the right $A$-action $(fa)(m)=f(am)$.
The left-module version follows by passing to opposite algebras.

\begin{proposition}[Tensor and Hom]\label{prop:tensor-duals}
% TODO (ChangeProposal9, Lecture 2 follow-up): Explain the general case for
% an (A,B)-bimodule M and a (B,C)-bimodule N. For right duals, require M_B
% finitely generated projective; for left duals, require _B N finitely generated
% projective. Finite k-dimension alone does not suffice over a general algebra.
% Keep the idempotent-matching calculation in the main exposition and move
% routine verification to supplementary material. Use the one-sided bimodule
% actions from eq:bimodule-dual-actions, independently of a symmetrising form.
Consider bimodules ${}_AM_B$, ${}_BN_C$, a right $C$-module $X$, and a left $A$-module $Y$.
There are maps, natural in $M,N$,
\begin{equation}\label{eq:general-tensor-duals}
\begin{aligned}
\theta_r:\Hom_C(N,X)\otimes_B\Hom_B(M,B)
&\longrightarrow\Hom_C(M\otimes_B N,X),\\
\theta_r(g\otimes f)(m\otimes n)&=g(f(m)n),\\
\theta_\ell:\Hom_{B^\op}(N,B)\otimes_B\Hom_{A^\op}(M,Y)
&\longrightarrow\Hom_{A^\op}(M\otimes_B N,Y),\\
\theta_\ell(g\otimes f)(m\otimes n)&=f(mg(n)).
\end{aligned}
\end{equation}
The maps $\theta_r$ and $\theta_\ell$ are right $A$-linear and left $C$-linear, respectively.
\begin{enumerate}
\item The map $\theta_r$ is an isomorphism if $M\in\add B$ as a right $B$-module.
\item The map $\theta_\ell$ is an isomorphism if $N\in\add B$ as a left $B$-module.
\end{enumerate}
Here $\add B$ is formed in the indicated module category, as in Example~\ref{ex:add-category}.
If ${}_CX_C$ and ${}_AY_A$ are bimodules, the respective maps also preserve the additional actions and are morphisms in $C\Mod A$.
\end{proposition}

\begin{proof}
\emph{Well-definedness of $\theta_r$.}
For $f\in\Hom_B(M,B)$, $g\in\Hom_C(N,X)$, and $b\in B$,
\[
g(f(mb)n)=g(f(m)bn),\qquad
(gb)(f(m)n)=g(bf(m)n)=g((bf)(m)n).
\]
These identities respect the defining identifications in both tensor products.
Right $C$-linearity follows from $g(f(m)nc)=g(f(m)n)c$ for $c\in C$.
For $a\in A$,
\[
\theta_r(g\otimes fa)(m\otimes n)
=g(f(am)n)=(\theta_r(g\otimes f)a)(m\otimes n).
\]
If $X$ also has a commuting left $C$-action, replacing $g$ by $cg$ multiplies the value by $c$, so $\theta_r$ preserves that action as well.

\emph{Bijectivity of $\theta_r$.}
Regard $M$ only as a right $B$-module.
For $M=B$, evaluation at $1$ identifies $\Hom_B(B,B)\cong B$, while multiplication identifies $B\otimes_B N\cong N$.
Under these isomorphisms, $\theta_r$ becomes
\[
\Hom_C(N,X)\otimes_B B\longrightarrow\Hom_C(N,X),
\qquad g\otimes b\longmapsto gb,
\]
which is an isomorphism by Lemma~\ref{lem:tensor-properties}(3).
Finite direct sums commute with both constructions by Lemma~\ref{lem:tensor-properties}(4) and \eqref{eq:hom-finite-sums}.
Thus $\theta_r$ is bijective for $M=B^{\oplus r}$, where $r\geq0$ is finite.
If $M\in\add B$, choose $M'$ with $M\oplus M'\cong B^{\oplus r}$.
The comparison for $M\oplus M'$ is the direct sum of the comparisons for $M$ and $M'$, so both summand maps are bijective.

\emph{The left comparison.}
For $f\in\Hom_{A^\op}(M,Y)$ and $g\in\Hom_{B^\op}(N,B)$, well-definedness follows from
\[
f(mb\,g(n))=f(mg(bn)),\qquad
f(m(gb)(n))=f(mg(n)b)=(bf)(mg(n))
\quad(b\in B).
\]
Left $A$-linearity of $f$ makes the resulting functional left $A$-linear.
For $c\in C$,
\[
\theta_\ell(cg\otimes f)(m\otimes n)
=f(mg(nc))=(c\theta_\ell(g\otimes f))(m\otimes n).
\]
If $Y$ also has a commuting right $A$-action, replacing $f$ by $fa$ multiplies the value by $a$, so $\theta_\ell$ preserves that action as well.
For $N=B$ as a left module, evaluation at $1$ identifies $\Hom_{B^\op}(B,B)\cong B$ and turns $\theta_\ell$ into
\[
B\otimes_B\Hom_{A^\op}(M,Y)\longrightarrow\Hom_{A^\op}(M,Y),
\qquad b\otimes f\longmapsto bf.
\]
The same finite-sum and direct-summand argument proves (2).

\emph{Naturality.}
Let $p:M\to M'$ and $q:N\to N'$ be bimodule maps.
For $f\in\Hom_B(M',B)$ and $g\in\Hom_C(N',X)$, applying $\theta_r$ before or after precomposition gives $g(f(p(m))q(n))$ at $m\otimes n$.
For $f\in\Hom_{A^\op}(M',Y)$ and $g\in\Hom_{B^\op}(N',B)$, the two orders give $f(p(m)g(q(n)))$ for $\theta_\ell$.
Thus both comparisons are natural.
\end{proof}
\end{advanced}

```

</details>

---

<a id="replacement-2"></a>

## Replacement 2: Identify the main formulas explicitly as semisimple tensor duality

**Location:** [2026_Koszul.tex:2054](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2054)  
**Change size:** 3 lines added; 1 lines removed.

Equations (2.5) and (2.6) are exactly the semisimple specialisation of the general comparison; Corollary 1.13 supplies the add S hypotheses, not the comparison maps. Equation (2.7) recalls the actions from (1.15). Replace only the introductory sentence, leaving all three displayed equations and their labels byte-for-byte unchanged in the main text.

### Line-by-Line Diff

```diff
--- a/2026_Koszul.tex
+++ b/2026_Koszul.tex
@@ -2054 +2060,3 @@
-For finite-dimensional semisimple $S$ and bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively, Corollary~\ref{cor:semisimple-summands} gives
+Let $S$ be finite-dimensional semisimple, and consider bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively.
+Corollary~\ref{cor:semisimple-summands} gives $V_S,{}_SW\in\add S$.
+Thus the semisimple case of tensor duality, Proposition~\ref{prop:tensor-duals}, gives natural bimodule isomorphisms
```

<details>
<summary><strong>Existing content (exact)</strong></summary>

```tex
For finite-dimensional semisimple $S$ and bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively, Corollary~\ref{cor:semisimple-summands} gives
```

</details>

<details>
<summary><strong>Proposed replacement (exact)</strong></summary>

```tex
Let $S$ be finite-dimensional semisimple, and consider bimodules ${}_SV_S$, ${}_SW_S$ finitely generated on the right and left, respectively.
Corollary~\ref{cor:semisimple-summands} gives $V_S,{}_SW\in\add S$.
Thus the semisimple case of tensor duality, Proposition~\ref{prop:tensor-duals}, gives natural bimodule isomorphisms
```

</details>

---

<a id="replacement-3"></a>

## Replacement 3: Specify the targets in the existing advanced counterexample

**Location:** [2026_Koszul.tex:2082](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2082)  
**Change size:** 2 lines added; 1 lines removed.

Specify X and Y so the existing counterexample is explicitly a specialisation of the generalised proposition. Its calculations and advanced placement remain unchanged.

### Line-by-Line Diff

```diff
--- a/2026_Koszul.tex
+++ b/2026_Koszul.tex
@@ -2082 +2090,2 @@
-Take $A=C=\Bbbk$, $B=\Bbbk[x]$, and bimodules ${}_\Bbbk M_B$, ${}_BN_\Bbbk$ with $M=N=B/(x)\cong\Bbbk$ and the outer $\Bbbk$-actions given by scalar multiplication.
+Take $A=C=\Bbbk$, $B=\Bbbk[x]$, and $X=Y=\Bbbk$.
+Consider bimodules ${}_\Bbbk M_B$, ${}_BN_\Bbbk$ with $M=N=B/(x)\cong\Bbbk$ and the outer $\Bbbk$-actions given by scalar multiplication.
```

<details>
<summary><strong>Existing content (exact)</strong></summary>

```tex
Take $A=C=\Bbbk$, $B=\Bbbk[x]$, and bimodules ${}_\Bbbk M_B$, ${}_BN_\Bbbk$ with $M=N=B/(x)\cong\Bbbk$ and the outer $\Bbbk$-actions given by scalar multiplication.
```

</details>

<details>
<summary><strong>Proposed replacement (exact)</strong></summary>

```tex
Take $A=C=\Bbbk$, $B=\Bbbk[x]$, and $X=Y=\Bbbk$.
Consider bimodules ${}_\Bbbk M_B$, ${}_BN_\Bbbk$ with $M=N=B/(x)\cong\Bbbk$ and the outer $\Bbbk$-actions given by scalar multiplication.
```

</details>

---

<a id="replacement-4"></a>

## Replacement 4: Specify the target in the existing advanced linear-dual application

**Location:** [2026_Koszul.tex:2093](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2093)  
**Change size:** 1 lines added; 1 lines removed.

Supply the newly generalised target X when deriving the linear-dual isomorphism. Leave the formula, citation, and advanced placement unchanged.

### Line-by-Line Diff

```diff
--- a/2026_Koszul.tex
+++ b/2026_Koszul.tex
@@ -2093 +2102 @@
-For $S,V,W$ as in \eqref{eq:tensor-duals}, take $A=B=S$, $C=\Bbbk$, $M=V$, and $N=W$ in Proposition~\ref{prop:tensor-duals}.
+For $S,V,W$ as in \eqref{eq:tensor-duals}, take $A=B=S$, $C=\Bbbk$, $M=V$, $N=W$, and $X=\Bbbk$ in Proposition~\ref{prop:tensor-duals}(1).
```

<details>
<summary><strong>Existing content (exact)</strong></summary>

```tex
For $S,V,W$ as in \eqref{eq:tensor-duals}, take $A=B=S$, $C=\Bbbk$, $M=V$, and $N=W$ in Proposition~\ref{prop:tensor-duals}.
```

</details>

<details>
<summary><strong>Proposed replacement (exact)</strong></summary>

```tex
For $S,V,W$ as in \eqref{eq:tensor-duals}, take $A=B=S$, $C=\Bbbk$, $M=V$, $N=W$, and $X=\Bbbk$ in Proposition~\ref{prop:tensor-duals}(1).
```

</details>

---

## Verification

- **Checked:** every existing passage matches the source uniquely, and replacement ranges do not overlap.
- **Checked:** equations (2.5)-(2.7) remain byte-for-byte unchanged and outside advanced and supplementary blocks. The counts of numbered equations and propositions before them are unchanged.
- **Checked:** existing labels remain, references resolve, environment nesting is balanced, and all percent-commented source is preserved.
- **Checked:** all changes are confined to Lecture 2; the other lectures and preamble are unchanged.
- **Completed:** all four approved replacements were applied exactly. The built-in compiler succeeded before the split, and the multi-file TeX Live build succeeded with the existing hidden-content setting, producing a 48-page PDF with no unresolved references.
- **Completed:** the preamble, front matter, and bibliography are in `Lecture_Koszul.tex`; Lectures 1-5 are in `Lecture_Koszul_S1.tex` through `Lecture_Koszul_S5.tex`. Recombining the files, excluding their editor root directives, reproduces the updated source exactly. Lectures 1 and 3-5 and all author percent-comments are unchanged.
- **Completed:** equations (2.5)-(2.7) retain their numbers and remain in the main text. The new advanced block and the adjacent main formulas were visually checked in the compiled PDF.
- **Unchanged layout warnings:** Lecture 1 retains one `mdframed` page-break warning and one 4.3234 pt overfull line. No unrelated layout edits were made.

**Source fingerprint (SHA-256):** `6ef02db516a68e95b56f4aacda459b3ad7d7a4cdf843000e3937b15231bef24c`.

