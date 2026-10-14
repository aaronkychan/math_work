# Change Proposal 10: Lecture 2

> **Applied on 14 October 2026.** All 14 Lecture 2 replacements and the separately requested Lecture 1 bimodule-notation update are present in the notes.

**Prepared:** 14 October 2026  
**Source:** [2026_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1653)  
**Scope:** Section 2 only, including its tensor-duality exercise and hidden proof.  
**Total:** 14 replacements; `+302` added lines, `-178` removed lines.

## Agreed Decisions

- Introduce tensor products over an arbitrary algebra. Do not assume that the base is a degree 0 subalgebra or is semisimple.
- Use $A,B,C$ for arbitrary algebras in general tensor-product and duality statements. Retain $S$ for the degree $0$ algebra in tensor-algebra constructions and for a semisimple base when semisimplicity is used.
- Write named bimodules as ${}_AM_B$ and ${}_BN_C$. The left and right subscripts specify the acting algebras, as introduced in Lecture 1.
- For the right tensor-dual comparison, require the first factor to be a direct summand of a finite free right module over the middle algebra. For the left comparison, impose the corresponding left-module condition on the second factor. No finiteness condition is imposed on the other factor in either assertion.
- Over a finite-dimensional semisimple base, finite generation gives the needed direct-summand condition. State that specialisation immediately after the general result. Do not introduce projective-module terminology before Lecture 4.
- Put the counterexample showing that finite generation alone fails over a general algebra in advanced material.
- Shorten the idempotent-decomposition proof to the mismatched-idempotent calculation and the explicit inverse. Leave the inverse checks to the reader.
- Put the tensor-algebra universal property, its proof, and its grading observation in advanced material. Keep the tensor-presentation corollary and multiplication map in the main text; its proof is advanced and specifies both inclusions.

## Reading the Proposal

**Diff legend:** `-` removes a line; `+` adds a line; a leading space retains context. The diff is the primary comparison. Full exact passages are available in the two collapsible sections below each diff.

Old line numbers refer to the source snapshot inspected on 14 October 2026. New line numbers include all preceding replacements in this proposal. These are **source lines**, not page or theorem numbers; automatic theorem numbering will change when the proposal is applied.

## Contents

| Replacement | Change | Lines |
| --- | --- | --- |
| [1](#replacement-1-introduce-tensor-products-over-an-arbitrary-algebra) | Introduce tensor products over an arbitrary algebra | `+51` / `-45` |
| [2](#replacement-2-keep-finite-hom-decompositions-in-the-main-text-and-use-an-arbitrary-base-algebra) | Keep finite Hom decompositions in the main text and use an arbitrary base algebra | `+42` / `-35` |
| [3](#replacement-3-describe-functoriality-by-induced-maps) | Describe functoriality by induced maps | `+14` / `-13` |
| [4](#replacement-4-state-tensor-duality-over-arbitrary-algebras-with-the-precise-hypotheses) | State tensor duality over arbitrary algebras with the precise hypotheses | `+47` / `-19` |
| [5](#replacement-5-explain-the-finiteness-restriction-and-deduce-the-linear-dual-formula) | Explain the finiteness restriction and deduce the linear-dual formula | `+17` / `-7` |
| [6](#replacement-6-use-the-index-k-in-the-outer-idempotent-example) | Use the index k in the outer-idempotent example | `+5` / `-4` |
| [7](#replacement-7-move-the-polynomial-matrix-example-into-supplementary-material) | Move the polynomial-matrix example into supplementary material | `+8` / `-2` |
| [8](#replacement-8-specify-multiplication-in-the-tensor-algebra-explicitly) | Specify multiplication in the tensor algebra explicitly | `+16` / `-10` |
| [9](#replacement-9-make-the-symmetric-and-exterior-algebra-example-symbolic-and-compact) | Make the symmetric and exterior algebra example symbolic and compact | `+22` / `-10` |
| [10](#replacement-10-shorten-the-idempotent-decomposition-proof) | Shorten the idempotent decomposition proof | `+14` / `-17` |
| [11](#replacement-11-remove-the-unexplained-diagonal-subalgebra-phrase) | Remove the unexplained diagonal-subalgebra phrase | `+4` / `-4` |
| [12](#replacement-12-move-the-tensor-algebra-universal-property-into-advanced-material) | Move the tensor-algebra universal property into advanced material | `+24` / `-11` |
| [13](#replacement-13-keep-the-tensor-duality-exercise-self-contained) | Keep the tensor-duality exercise self-contained | `+2` / `-1` |
| [14](#replacement-14-retain-a-hidden-proof-of-the-general-tensor-dual-statement) | Retain a hidden proof of the general tensor-dual statement | `+36` / `-0` |

## Comment Coverage

| Existing source line | Comment | Replacement |
| --- | --- | --- |
| 1663 | General algebras and the general tensor-dual comparison | 1, 3, 4, 5, 14 |
| 1671 | Introduce the phrase 'tensor product over an algebra' naturally | 1 |
| 1716 | Put the basic-properties proof in supplementary material | 1 |
| 1738 | State the finite Hom decomposition; make arbitrary-family results advanced | 2 |
| 1970 | Use k instead of ell for the third idempotent index | 6 |
| 2010 | Make the polynomial-matrix example supplementary | 7 |
| 2011 | Display the algebra symbolically | 7 |
| 2067 | Write the degree components symbolically | 9 |
| 2072 | Make the basis verification supplementary | 9 |
| 2089 | Discuss and shorten the idempotent-decomposition proof | 10; discussion completed |
| 2112 | Remove the unexplained diagonal-subalgebra phrase | 11 |
| 2125 | Discuss moving the universal property into advanced material | 12; discussion completed |
| 2160 | Make the tensor-presentation proof advanced | 12 |
| 2161 | Specify which maps are used in the universal property | 12 |

Replacements 3, 8, 13, and 14 provide the closely related wording, multiplication, exercise, and proof adjustments required by these revisions.

## Dependencies and Preservation

- Apply Replacements 4, 5, 13, and 14 together: they generalise the tensor-dual statement, specialise it back to the course setting, and keep the exercise and proof consistent.
- Replacement 2 opens the existing advanced block earlier. The Hom lemma, direct-product proposition, and infinite-family remark share one block; no advanced blocks are nested.
- All existing proposition and equation labels are retained, including those cited in Lecture 3. No later lecture needs a source edit for these replacements.
- The existing tensor-duality exercise is Homework 1, Exercise 3. Its question and hint remain valid and self-contained, so **no homework change is proposed**. Its existing hidden solution in the notes is preserved verbatim; the general proof is appended inside the same hidden environment.
- Existing percent-commented source, including historical TODO comments, is preserved verbatim. The accepted decisions in this proposal supersede any outdated placement instructions in those non-printing TODO comments.
- These replacements alter only Lecture 2. The separately requested Lecture 1 bimodule-notation update has already been applied; Lectures 3--5, the bibliography, and the notation table are outside this proposal.
- The existing hidden-content switch remains unchanged. No solution-visibility toggling or test of alternative settings is proposed.

## Checks

- Every active Lecture 2 comment is covered. The proposed assembled Lecture 2 contains no remaining active comment macros.
- Every quoted existing passage matches the inspected source exactly and uniquely; replacement ranges do not overlap.
- Static checks on the assembled proposal find no missing or duplicate labels, unresolved references, or mismatched environments. Content outside Lecture 2 is identical to the inspected source.
- The general dual comparison uses right B-linearity for the first factor and left B-linearity for the second, with the correct reversed outer actions. The non-semisimple counterexample has zero source and non-zero target for the comparison.
- New terminology is restricted to constructions already introduced. In particular, the hypothesis is expressed using direct summands, not unexplained projective-module terminology. Citations remain inside advanced material.
- **Completed:** all 14 Lecture 2 replacements were applied exactly and the notes compiled successfully. No homework change was required.

---

## Replacement 1: Introduce tensor products over an arbitrary algebra

**Source:** [Lecture 2, line 1663](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1663)  
**Added:** `+51` lines | **Removed:** `-45` lines

Address the opening comments without assuming a grading or semisimplicity. Give outer actions and associativity over arbitrary algebras, retain the four numbered properties for existing references, and place their proof in supplementary material.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1663,75 +1663,81 @@
-\comm{
-so many things went wrong in this subsection.  we should introduce tensor product over ANY algebra, not just semisimple.   all result in this subsection for general tensor product, even last proposition is really just special case of ${}_C(N^*\otimes_B M^*)_A\cong {}_C(M\otimes_BN)^*_A$; we only need the special case when all $A, B, C$ are all $S$ in later subsections; and these applications are straightforward}
-
-Let $A$ be a graded algebra and set $S=A_0$.
-Multiplication on $A_1$ satisfies $(vs)w=v(sw)$ for $v,w\in A_1$ and $s\in S$.
-A tensor product over $S$ incorporates this identity.
+Let $A$ be any $\Bbbk$-algebra, $M$ a right $A$-module, and $N$ a left $A$-module.
+The tensor product over $A$ imposes the identities $ma\otimes n=m\otimes an$ for $m\in M$, $n\in N$, and $a\in A$.
 
 \begin{definition}\label{def:module-tensor}
-For a $\Bbbk$-algebra $S$, a right $S$-module $M$, and a left $S$-module $N$, the \defn{tensor product} $M\otimes_S N$ is the quotient of $M\otimes_\Bbbk N$ by \comm{introduce the phrase tensor product over an algebra more properly (needs to read naturally; read as in read aloud)}
+The \defn{tensor product of $M$ and $N$ over $A$}, denoted $M\otimes_A N$, is the quotient of the vector space $M\otimes_\Bbbk N$ by
 \[
-\operatorname{span}_\Bbbk\{ms\otimes n-m\otimes sn\mid m\in M,\ n\in N,\ s\in S\}.
+\operatorname{span}_\Bbbk\{ma\otimes n-m\otimes an\mid m\in M,\ n\in N,\ a\in A\}.
 \]
 \end{definition}
 
-It is customary to keep the notation $m\otimes n$ for the image of this element in the tensor product over $S$; if clarification is needed then we will write $m\otimes_S n$.
+Write $m\otimes_A n$ for the image of $m\otimes n$ in this quotient, omitting the subscript when the base algebra is clear.
 
 %No semisimplicity or finiteness assumption on $S,M,N$ is needed for the following properties.
 
 \begin{lemma}[Basic properties of tensor products]\label{lem:tensor-properties}
-Let $S$ be a $\Bbbk$-algebra, $M\in\Mod S$, and $N\in\Mod(S^\op)$.
+Let $A$ be any $\Bbbk$-algebra, $M$ a right $A$-module, and $N$ a left $A$-module.
 \begin{enumerate}
-\item For a vector space $W$ and a bilinear map $b:M\times N\to W$ satisfying $b(ms,n)=b(m,sn)$ for all $m\in M$, $s\in S$, and $n\in N$, there is a unique linear map $\widetilde b$ making the diagram commute:
+\item For a vector space $W$ and a bilinear map $b:M\times N\to W$ satisfying $b(ma,n)=b(m,an)$ for all $m\in M$, $a\in A$, and $n\in N$, there is a unique linear factorisation (commutative diagram)
 \[
 \xymatrix@C=55pt@R=22pt{
-M\times N \ar[r]^{(m,n)\mapsto m\otimes_S n} \ar[dr]_{b}
-& M\otimes_S N \ar@{-->}[d]^{\exists!\,\widetilde b}\\
+M\times N \ar[r]^{(m,n)\mapsto m\otimes_A n} \ar[dr]_{b}
+& M\otimes_A N \ar@{-->}[d]^{\exists!\,\widetilde b}\\
 & W.
 }
 \]
-Conversely, every linear map $M\otimes_S N\to W$ defines such a bilinear map.
-\item If $M,N$ are $S$-bimodules, then $M\otimes_S N$ is an $S$-bimodule with
-$s(m\otimes_S n)t=sm\otimes_S nt$ for $s,t\in S$.
-\item For $S$-bimodules $U,V,W$, there are bimodule isomorphisms
+Conversely, every linear map $M\otimes_A N\to W$ defines such a bilinear map.
+\item If $B,C$ are $\Bbbk$-algebras and ${}_BM_A$, ${}_AN_C$ are bimodules, then $M\otimes_A N$ is a bimodule ${}_B(M\otimes_A N)_C$ with
 \[
-\begin{aligned}
-(U\otimes_S V)\otimes_S W&\xrightarrow{\sim}U\otimes_S(V\otimes_S W),
-&(u\otimes v)\otimes w&\longmapsto u\otimes(v\otimes w),\\
-S\otimes_S V&\xrightarrow{\sim}V,
-&s\otimes v&\longmapsto sv,\\
-V\otimes_S S&\xrightarrow{\sim}V,
-&v\otimes s&\longmapsto vs.
-\end{aligned}
+b(m\otimes_A n)c=bm\otimes_A nc
+\qquad(b\in B,\ c\in C,\ m\in M,\ n\in N).
 \]
-\item Tensor products distribute over direct sums in either variable. For a family $(M_i)_{i\in I}$ of right $S$-modules, the isomorphism is
+\item For $\Bbbk$-algebras $A,B$, a right $A$-module $U$, a bimodule ${}_AV_B$, and a left $B$-module $W$, there is a natural linear isomorphism
 \[
-\Bigl(\bigoplus_{i\in I}M_i\Bigr)\otimes_S N
-\xrightarrow{\sim}\bigoplus_{i\in I}(M_i\otimes_S N),
-\qquad (m_i)_i\otimes n\longmapsto(m_i\otimes n)_i.
+(U\otimes_A V)\otimes_B W\xrightarrow{\sim}U\otimes_A(V\otimes_B W),
+\qquad (u\otimes v)\otimes w\longmapsto u\otimes(v\otimes w).
+\]
+There are also natural module isomorphisms
+\[
+M\otimes_A A\xrightarrow{\sim}M,\quad m\otimes a\longmapsto ma,
+\qquad
+A\otimes_A N\xrightarrow{\sim}N,\quad a\otimes n\longmapsto an.
+\]
+All these maps preserve any additional outer module actions.
+\item Tensor products distribute over direct sums in either variable. For an arbitrary family $(M_i)_{i\in I}$ of right $A$-modules, indexed by a set $I$,
+\[
+\Bigl(\bigoplus_{i\in I}M_i\Bigr)\otimes_A N
+\xrightarrow{\sim}\bigoplus_{i\in I}(M_i\otimes_A N),
+\qquad (m_i)_{i\in I}\otimes n\longmapsto(m_i\otimes n)_{i\in I}.
 \]
 \end{enumerate}
 \end{lemma}
 
+\begin{supplementary}
 \begin{proof}
-\comm{put proof as supplementary material}
-For (1), Proposition~\ref{prop:vector-tensor-universal} gives a unique linear map $M\otimes_\Bbbk N\to W$ sending $m\otimes n$ to $b(m,n)$.
-It descends to the quotient precisely when $b(ms,n)-b(m,sn)=0$.
-Uniqueness follows because the elements $m\otimes_S n$ span the quotient.
+For (1), Proposition~\ref{prop:vector-tensor-universal} gives a unique linear map $M\otimes_\Bbbk N\to W$, $m\otimes n\mapsto b(m,n)$.
+The map vanishes on the defining subspace precisely when $b(ma,n)=b(m,an)$.
 
-For (2), the outer actions preserve the defining relations: for $a,s,t\in S$,
+For (2), the outer actions preserve that subspace: for $b\in B$, $c\in C$, and $a\in A$,
 \[
-s(ma\otimes n-m\otimes an)t
-=(sm)a\otimes nt-sm\otimes a(nt).
+b(ma\otimes n-m\otimes an)c
+=(bm)a\otimes nc-bm\otimes a(nc).
 \]
-The module axioms follow from those on $M,N$.
-In (3), both parenthesisations impose the relations that move an element of $S$ between adjacent factors, so the displayed associativity map and its reverse are well-defined.
-Their composites fix every $(u\otimes v)\otimes w$ and $u\otimes(v\otimes w)$.
-The unit inverses are $V\to S\otimes_S V$, $v\mapsto1\otimes v$, and $V\to V\otimes_S S$, $v\mapsto v\otimes1$; the equalities $1\otimes sv=s\otimes v$ and $vs\otimes1=v\otimes s$ show that these maps are inverses.
+The module axioms follow from those on $M$ and $N$.
 
-For (4), the displayed map has finite support because $(m_i)_i$ does.
-It is well-defined by (1).
-If $\iota_i:M_i\to\bigoplus_{j\in I}M_j$ is the canonical inclusion, the inverse sends $m\otimes n$ in the $i$th summand to $\iota_i(m)\otimes n$ and extends linearly over the direct sum.
-Both composites fix the displayed generators.
-The same construction works in the other variable.
+For (3), both parenthesisations impose
+\[
+(ua)\otimes v\otimes w=u\otimes(av)\otimes w,\qquad
+u\otimes(vb)\otimes w=u\otimes v\otimes(bw)
+\quad(a\in A,\ b\in B).
+\]
+Thus the displayed associativity map and the reverse assignment are well-defined and inverse.
+The unit inverses are $M\to M\otimes_A A$, $m\mapsto m\otimes1$, and $N\to A\otimes_A N$, $n\mapsto1\otimes n$.
+
+For (4), the bilinear map $((m_i)_{i\in I},n)\mapsto(m_i\otimes n)_{i\in I}$ satisfies the identity in (1), so it induces the displayed linear map.
+For each $i\in I$, let $\iota_i:M_i\to\bigoplus_{j\in I}M_j$ be the inclusion.
+The inverse sends $m\otimes n$ in the $i$th summand to $\iota_i(m)\otimes n$ and extends over the direct sum.
+Both composites fix every element $m\otimes n$ from a summand.
+The other variable is handled in the same way.
 \end{proof}
+\end{supplementary}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\comm{
so many things went wrong in this subsection.  we should introduce tensor product over ANY algebra, not just semisimple.   all result in this subsection for general tensor product, even last proposition is really just special case of ${}_C(N^*\otimes_B M^*)_A\cong {}_C(M\otimes_BN)^*_A$; we only need the special case when all $A, B, C$ are all $S$ in later subsections; and these applications are straightforward}

Let $A$ be a graded algebra and set $S=A_0$.
Multiplication on $A_1$ satisfies $(vs)w=v(sw)$ for $v,w\in A_1$ and $s\in S$.
A tensor product over $S$ incorporates this identity.

\begin{definition}\label{def:module-tensor}
For a $\Bbbk$-algebra $S$, a right $S$-module $M$, and a left $S$-module $N$, the \defn{tensor product} $M\otimes_S N$ is the quotient of $M\otimes_\Bbbk N$ by \comm{introduce the phrase tensor product over an algebra more properly (needs to read naturally; read as in read aloud)}
\[
\operatorname{span}_\Bbbk\{ms\otimes n-m\otimes sn\mid m\in M,\ n\in N,\ s\in S\}.
\]
\end{definition}

It is customary to keep the notation $m\otimes n$ for the image of this element in the tensor product over $S$; if clarification is needed then we will write $m\otimes_S n$.

%No semisimplicity or finiteness assumption on $S,M,N$ is needed for the following properties.

\begin{lemma}[Basic properties of tensor products]\label{lem:tensor-properties}
Let $S$ be a $\Bbbk$-algebra, $M\in\Mod S$, and $N\in\Mod(S^\op)$.
\begin{enumerate}
\item For a vector space $W$ and a bilinear map $b:M\times N\to W$ satisfying $b(ms,n)=b(m,sn)$ for all $m\in M$, $s\in S$, and $n\in N$, there is a unique linear map $\widetilde b$ making the diagram commute:
\[
\xymatrix@C=55pt@R=22pt{
M\times N \ar[r]^{(m,n)\mapsto m\otimes_S n} \ar[dr]_{b}
& M\otimes_S N \ar@{-->}[d]^{\exists!\,\widetilde b}\\
& W.
}
\]
Conversely, every linear map $M\otimes_S N\to W$ defines such a bilinear map.
\item If $M,N$ are $S$-bimodules, then $M\otimes_S N$ is an $S$-bimodule with
$s(m\otimes_S n)t=sm\otimes_S nt$ for $s,t\in S$.
\item For $S$-bimodules $U,V,W$, there are bimodule isomorphisms
\[
\begin{aligned}
(U\otimes_S V)\otimes_S W&\xrightarrow{\sim}U\otimes_S(V\otimes_S W),
&(u\otimes v)\otimes w&\longmapsto u\otimes(v\otimes w),\\
S\otimes_S V&\xrightarrow{\sim}V,
&s\otimes v&\longmapsto sv,\\
V\otimes_S S&\xrightarrow{\sim}V,
&v\otimes s&\longmapsto vs.
\end{aligned}
\]
\item Tensor products distribute over direct sums in either variable. For a family $(M_i)_{i\in I}$ of right $S$-modules, the isomorphism is
\[
\Bigl(\bigoplus_{i\in I}M_i\Bigr)\otimes_S N
\xrightarrow{\sim}\bigoplus_{i\in I}(M_i\otimes_S N),
\qquad (m_i)_i\otimes n\longmapsto(m_i\otimes n)_i.
\]
\end{enumerate}
\end{lemma}

\begin{proof}
\comm{put proof as supplementary material}
For (1), Proposition~\ref{prop:vector-tensor-universal} gives a unique linear map $M\otimes_\Bbbk N\to W$ sending $m\otimes n$ to $b(m,n)$.
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
The unit inverses are $V\to S\otimes_S V$, $v\mapsto1\otimes v$, and $V\to V\otimes_S S$, $v\mapsto v\otimes1$; the equalities $1\otimes sv=s\otimes v$ and $vs\otimes1=v\otimes s$ show that these maps are inverses.

For (4), the displayed map has finite support because $(m_i)_i$ does.
It is well-defined by (1).
If $\iota_i:M_i\to\bigoplus_{j\in I}M_j$ is the canonical inclusion, the inverse sends $m\otimes n$ in the $i$th summand to $\iota_i(m)\otimes n$ and extends linearly over the direct sum.
Both composites fix the displayed generators.
The same construction works in the other variable.
\end{proof}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
Let $A$ be any $\Bbbk$-algebra, $M$ a right $A$-module, and $N$ a left $A$-module.
The tensor product over $A$ imposes the identities $ma\otimes n=m\otimes an$ for $m\in M$, $n\in N$, and $a\in A$.

\begin{definition}\label{def:module-tensor}
The \defn{tensor product of $M$ and $N$ over $A$}, denoted $M\otimes_A N$, is the quotient of the vector space $M\otimes_\Bbbk N$ by
\[
\operatorname{span}_\Bbbk\{ma\otimes n-m\otimes an\mid m\in M,\ n\in N,\ a\in A\}.
\]
\end{definition}

Write $m\otimes_A n$ for the image of $m\otimes n$ in this quotient, omitting the subscript when the base algebra is clear.

%No semisimplicity or finiteness assumption on $S,M,N$ is needed for the following properties.

\begin{lemma}[Basic properties of tensor products]\label{lem:tensor-properties}
Let $A$ be any $\Bbbk$-algebra, $M$ a right $A$-module, and $N$ a left $A$-module.
\begin{enumerate}
\item For a vector space $W$ and a bilinear map $b:M\times N\to W$ satisfying $b(ma,n)=b(m,an)$ for all $m\in M$, $a\in A$, and $n\in N$, there is a unique linear factorisation (commutative diagram)
\[
\xymatrix@C=55pt@R=22pt{
M\times N \ar[r]^{(m,n)\mapsto m\otimes_A n} \ar[dr]_{b}
& M\otimes_A N \ar@{-->}[d]^{\exists!\,\widetilde b}\\
& W.
}
\]
Conversely, every linear map $M\otimes_A N\to W$ defines such a bilinear map.
\item If $B,C$ are $\Bbbk$-algebras and ${}_BM_A$, ${}_AN_C$ are bimodules, then $M\otimes_A N$ is a bimodule ${}_B(M\otimes_A N)_C$ with
\[
b(m\otimes_A n)c=bm\otimes_A nc
\qquad(b\in B,\ c\in C,\ m\in M,\ n\in N).
\]
\item For $\Bbbk$-algebras $A,B$, a right $A$-module $U$, a bimodule ${}_AV_B$, and a left $B$-module $W$, there is a natural linear isomorphism
\[
(U\otimes_A V)\otimes_B W\xrightarrow{\sim}U\otimes_A(V\otimes_B W),
\qquad (u\otimes v)\otimes w\longmapsto u\otimes(v\otimes w).
\]
There are also natural module isomorphisms
\[
M\otimes_A A\xrightarrow{\sim}M,\quad m\otimes a\longmapsto ma,
\qquad
A\otimes_A N\xrightarrow{\sim}N,\quad a\otimes n\longmapsto an.
\]
All these maps preserve any additional outer module actions.
\item Tensor products distribute over direct sums in either variable. For an arbitrary family $(M_i)_{i\in I}$ of right $A$-modules, indexed by a set $I$,
\[
\Bigl(\bigoplus_{i\in I}M_i\Bigr)\otimes_A N
\xrightarrow{\sim}\bigoplus_{i\in I}(M_i\otimes_A N),
\qquad (m_i)_{i\in I}\otimes n\longmapsto(m_i\otimes n)_{i\in I}.
\]
\end{enumerate}
\end{lemma}

\begin{supplementary}
\begin{proof}
For (1), Proposition~\ref{prop:vector-tensor-universal} gives a unique linear map $M\otimes_\Bbbk N\to W$, $m\otimes n\mapsto b(m,n)$.
The map vanishes on the defining subspace precisely when $b(ma,n)=b(m,an)$.

For (2), the outer actions preserve that subspace: for $b\in B$, $c\in C$, and $a\in A$,
\[
b(ma\otimes n-m\otimes an)c
=(bm)a\otimes nc-bm\otimes a(nc).
\]
The module axioms follow from those on $M$ and $N$.

For (3), both parenthesisations impose
\[
(ua)\otimes v\otimes w=u\otimes(av)\otimes w,\qquad
u\otimes(vb)\otimes w=u\otimes v\otimes(bw)
\quad(a\in A,\ b\in B).
\]
Thus the displayed associativity map and the reverse assignment are well-defined and inverse.
The unit inverses are $M\to M\otimes_A A$, $m\mapsto m\otimes1$, and $N\to A\otimes_A N$, $n\mapsto1\otimes n$.

For (4), the bilinear map $((m_i)_{i\in I},n)\mapsto(m_i\otimes n)_{i\in I}$ satisfies the identity in (1), so it induces the displayed linear map.
For each $i\in I$, let $\iota_i:M_i\to\bigoplus_{j\in I}M_j$ be the inclusion.
The inverse sends $m\otimes n$ in the $i$th summand to $\iota_i(m)\otimes n$ and extends over the direct sum.
Both composites fix every element $m\otimes n$ from a summand.
The other variable is handled in the same way.
\end{proof}
\end{supplementary}

```

</details>

---

## Replacement 2: Keep finite Hom decompositions in the main text and use an arbitrary base algebra

**Source:** [Lecture 2, line 1738](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1738)  
**Added:** `+42` lines | **Removed:** `-35` lines

State the finite direct-sum formula as a fact, as requested. Move the arbitrary-family Hom lemma and proof into the existing advanced block, which continues through the direct-product discussion. Specify all index ranges.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1738,89 +1744,96 @@
-\comm{
-just quote as fact that $\Hom_A(\bigoplus_{j\in J}M_j, \bigoplus_{i\in I}N_i)\cong \bigoplus_{i,j}\Hom_A(M_j,N_i)$ for finite $I,J$.  Then put this lemma as advanced material.
-}
+For finite sets $I,J$ and right $A$-modules $M_j,N_i$, there is a natural isomorphism
+\begin{equation}\label{eq:hom-finite-sums}
+\begin{aligned}
+\Hom_A\Bigl(\bigoplus_{j\in J}M_j,\bigoplus_{i\in I}N_i\Bigr)
+&\xrightarrow{\sim}\bigoplus_{\substack{i\in I\\j\in J}}\Hom_A(M_j,N_i),\\
+f&\longmapsto(\pi_i f\iota_j)_{i\in I,\ j\in J},
+\end{aligned}
+\end{equation}
+where $\iota_j:M_j\to\bigoplus_{j'\in J}M_{j'}$ and $\pi_i:\bigoplus_{i'\in I}N_{i'}\to N_i$ are the inclusions and projections.
+
+\begin{advanced}
 \begin{lemma}[Hom, direct sums, and direct products]\label{lem:hom-sums-products}
-Let $M,N,M_i,N_i$ be right $S$-modules, with $i\in I$.
+Let $M,N$ be right $A$-modules, and let $(M_i)_{i\in I}$ and $(N_i)_{i\in I}$ be arbitrary families of right $A$-modules, indexed by a set $I$.
 Write $\iota_i:M_i\to\bigoplus_{j\in I}M_j$ for the inclusions and $\pi_i:\prod_{j\in I}N_j\to N_i$ for the projections.
 There are natural linear isomorphisms
 \[
 \begin{aligned}
-\Hom_S\Bigl(\bigoplus_iM_i,N\Bigr)&\xrightarrow{\sim}\prod_i\Hom_S(M_i,N),
-& f&\longmapsto(f\circ\iota_i)_i,\\
-\Hom_S\Bigl(M,\prod_iN_i\Bigr)&\xrightarrow{\sim}\prod_i\Hom_S(M,N_i),
-& f&\longmapsto(\pi_i\circ f)_i.
+\Hom_A\Bigl(\bigoplus_{i\in I}M_i,N\Bigr)&\xrightarrow{\sim}\prod_{i\in I}\Hom_A(M_i,N),
+& f&\longmapsto(f\circ\iota_i)_{i\in I},\\
+\Hom_A\Bigl(M,\prod_{i\in I}N_i\Bigr)&\xrightarrow{\sim}\prod_{i\in I}\Hom_A(M,N_i),
+& f&\longmapsto(\pi_i\circ f)_{i\in I}.
 \end{aligned}
 \]
 There is also a natural injection
 \[
-\bigoplus_i\Hom_S(M,N_i)\longrightarrow
-\Hom_S\Bigl(M,\bigoplus_iN_i\Bigr),
-\qquad (f_i)_i\longmapsto\bigl(m\mapsto(f_i(m))_i\bigr),
+\bigoplus_{i\in I}\Hom_A(M,N_i)\longrightarrow
+\Hom_A\Bigl(M,\bigoplus_{i\in I}N_i\Bigr),
+\qquad (f_i)_{i\in I}\longmapsto\bigl(m\mapsto(f_i(m))_{i\in I}\bigr),
 \]
 which is an isomorphism when $M$ is finitely generated.
 \end{lemma}
 
 \begin{proof}
-The inverse of the first map sends $(f_i)_i$ to $(m_i)_i\mapsto\sum_i f_i(m_i)$; the sum is finite because $(m_i)_i$ has finite support.
-The inverse of the second sends $(f_i)_i$ to $m\mapsto(f_i(m))_i$; a direct product imposes no support condition.
+The inverse of the first map sends $(f_i)_{i\in I}$ to $(m_i)_{i\in I}\mapsto\sum_{i\in I}f_i(m_i)$; the sum is finite because $(m_i)_{i\in I}$ has finite support.
+The inverse of the second sends $(f_i)_{i\in I}$ to $m\mapsto(f_i(m))_{i\in I}$; a direct product imposes no support condition.
 For the third map, coordinate projections recover each $f_i$, proving injectivity.
-If $m_1,\ldots,m_r$ generate $M$, the images of these generators under $f:M\to\bigoplus_iN_i$ are supported on a common finite subset $J\subset I$.
+If $m_1,\ldots,m_r$ generate $M$, the images of these generators under $f:M\to\bigoplus_{i\in I}N_i$ are supported on a common finite subset $J\subset I$.
 Then $f(M)\subset\bigoplus_{i\in J}N_i$, so $f$ comes from a finite family of maps.
 All three constructions commute with precomposition and postcomposition.
 \end{proof}
 
-\begin{advanced}
 \begin{proposition}[Tensor products and direct products]\label{prop:tensor-direct-products}
-Let $S$ be a $\Bbbk$-algebra, $M,M_i$ right $S$-modules, and $N,N_i$ left $S$-modules, with $i\in I$.
+Let $A$ be a $\Bbbk$-algebra, $M,M_i$ right $A$-modules, and $N,N_i$ left $A$-modules, with $i\in I$.
 The coordinate projections define linear maps
 \begin{equation}\label{eq:module-tensor-products}
 \begin{aligned}
-\kappa_N:\Bigl(\prod_iM_i\Bigr)\otimes_S N
-&\longrightarrow\prod_i(M_i\otimes_S N),
+\kappa_N:\Bigl(\prod_iM_i\Bigr)\otimes_A N
+&\longrightarrow\prod_i(M_i\otimes_A N),
 & (m_i)_i\otimes n&\longmapsto(m_i\otimes n)_i,\\
-\lambda_M:M\otimes_S\Bigl(\prod_iN_i\Bigr)
-&\longrightarrow\prod_i(M\otimes_S N_i),
+\lambda_M:M\otimes_A\Bigl(\prod_iN_i\Bigr)
+&\longrightarrow\prod_i(M\otimes_A N_i),
 & m\otimes(n_i)_i&\longmapsto(m\otimes n_i)_i.
 \end{aligned}
 \end{equation}
 \begin{enumerate}
 \item If $I$ is finite, both maps are isomorphisms.
-\item The map $\kappa_N$ is an isomorphism if $N$ is a direct summand of $S^{\oplus r}$ as a left module for some finite $r$.
+\item The map $\kappa_N$ is an isomorphism if $N$ is a direct summand of $A^{\oplus r}$ as a left module for some finite $r$.
 The corresponding condition on the right module $M$ makes $\lambda_M$ an isomorphism.
-\item If $S$ is finite-dimensional semisimple, both maps are injective.
+\item If $A$ is finite-dimensional semisimple, both maps are injective.
 Moreover, $\kappa_N$ is an isomorphism when $N$ is finite-dimensional, and $\lambda_M$ is an isomorphism when $M$ is finite-dimensional.
 \end{enumerate}
 \end{proposition}
 
 \begin{proof}
-The formulas in \eqref{eq:module-tensor-products} are bilinear. For $s\in S$, the component identities
+The formulas in \eqref{eq:module-tensor-products} are bilinear. For $s\in A$, the component identities
 $(m_is)\otimes n=m_i\otimes sn$ and $(ms)\otimes n_i=m\otimes sn_i$
 show that both formulas give well-defined maps from the indicated tensor products.
 For finite $I$, products equal sums, and Lemma~\ref{lem:tensor-properties}(4) proves (1).
 
-For $N=S$, the map $\kappa_S$ is the identity on $\prod_iM_i$ under $m\otimes s\mapsto ms$.
-For $N=S^{\oplus r}$, both sides are $(\prod_iM_i)^{\oplus r}$, since a finite direct sum commutes with a direct product.
-If $N\oplus N'\cong S^{\oplus r}$, the comparison for $N\oplus N'$ is $\kappa_N\oplus\kappa_{N'}$.
+For $N=A$, the map $\kappa_A$ is the identity on $\prod_iM_i$ under $m\otimes s\mapsto ms$.
+For $N=A^{\oplus r}$, both sides are $(\prod_iM_i)^{\oplus r}$, since a finite direct sum commutes with a direct product.
+If $N\oplus N'\cong A^{\oplus r}$, the comparison for $N\oplus N'$ is $\kappa_N\oplus\kappa_{N'}$.
 Its bijectivity implies the bijectivity of $\kappa_N$.
 This proves the assertion about $\kappa_N$ in (2).
 
-Now let $S$ be finite-dimensional semisimple.
+Now let $A$ be finite-dimensional semisimple.
 For finite-dimensional $N$, Corollary~\ref{cor:semisimple-summands} gives (2).
-For arbitrary $N$, take $z=\sum_{\ell=1}^r m^{(\ell)}\otimes n_\ell$ in $\Ker\kappa_N$ and set $N_0=\sum_{\ell=1}^r Sn_\ell$.
+For arbitrary $N$, take $z=\sum_{\ell=1}^r m^{(\ell)}\otimes n_\ell$ in $\Ker\kappa_N$ and set $N_0=\sum_{\ell=1}^r An_\ell$.
 The submodule $N_0$ is finite-dimensional and has a complement in $N$ by Theorem~\ref{thm:artin-wedderburn}.
 Thus the inclusions
 \[
-\Bigl(\prod_iM_i\Bigr)\otimes_S N_0
-\longrightarrow\Bigl(\prod_iM_i\Bigr)\otimes_S N,
+\Bigl(\prod_iM_i\Bigr)\otimes_A N_0
+\longrightarrow\Bigl(\prod_iM_i\Bigr)\otimes_A N,
 \qquad
-M_i\otimes_S N_0\longrightarrow M_i\otimes_S N
+M_i\otimes_A N_0\longrightarrow M_i\otimes_A N
 \]
 are injective, by the direct sum formula in Lemma~\ref{lem:tensor-properties}(4).
-Regard $z$ as a tensor with second factors in $N_0$.
+Regard $z$ as an element with second factors in $N_0$.
 The equality $\kappa_N(z)=0$ then gives $\kappa_{N_0}(z)=0$.
-Since $\kappa_{N_0}$ is an isomorphism, $z=0$.
+Aince $\kappa_{N_0}$ is an isomorphism, $z=0$.
 
-For $\lambda_M$, apply the same arguments over $S^\op$, using
-$N\otimes_{S^\op}M\cong M\otimes_S N$, $n\otimes m\mapsto m\otimes n$.
+For $\lambda_M$, apply the same arguments over $A^\op$, using
+$N\otimes_{A^\op}M\cong M\otimes_A N$, $n\otimes m\mapsto m\otimes n$.
 \end{proof}
 
 The finite-dimensional hypothesis on the fixed factor cannot be dropped from the isomorphism assertion: Example~\ref{ex:tensor-product-product-failure} gives a non-surjective comparison even for vector spaces.
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\comm{
just quote as fact that $\Hom_A(\bigoplus_{j\in J}M_j, \bigoplus_{i\in I}N_i)\cong \bigoplus_{i,j}\Hom_A(M_j,N_i)$ for finite $I,J$.  Then put this lemma as advanced material.
}
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
The formulas in \eqref{eq:module-tensor-products} are bilinear. For $s\in S$, the component identities
$(m_is)\otimes n=m_i\otimes sn$ and $(ms)\otimes n_i=m\otimes sn_i$
show that both formulas give well-defined maps from the indicated tensor products.
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

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
For finite sets $I,J$ and right $A$-modules $M_j,N_i$, there is a natural isomorphism
\begin{equation}\label{eq:hom-finite-sums}
\begin{aligned}
\Hom_A\Bigl(\bigoplus_{j\in J}M_j,\bigoplus_{i\in I}N_i\Bigr)
&\xrightarrow{\sim}\bigoplus_{\substack{i\in I\\j\in J}}\Hom_A(M_j,N_i),\\
f&\longmapsto(\pi_i f\iota_j)_{i\in I,\ j\in J},
\end{aligned}
\end{equation}
where $\iota_j:M_j\to\bigoplus_{j'\in J}M_{j'}$ and $\pi_i:\bigoplus_{i'\in I}N_{i'}\to N_i$ are the inclusions and projections.

\begin{advanced}
\begin{lemma}[Hom, direct sums, and direct products]\label{lem:hom-sums-products}
Let $M,N$ be right $A$-modules, and let $(M_i)_{i\in I}$ and $(N_i)_{i\in I}$ be arbitrary families of right $A$-modules, indexed by a set $I$.
Write $\iota_i:M_i\to\bigoplus_{j\in I}M_j$ for the inclusions and $\pi_i:\prod_{j\in I}N_j\to N_i$ for the projections.
There are natural linear isomorphisms
\[
\begin{aligned}
\Hom_A\Bigl(\bigoplus_{i\in I}M_i,N\Bigr)&\xrightarrow{\sim}\prod_{i\in I}\Hom_A(M_i,N),
& f&\longmapsto(f\circ\iota_i)_{i\in I},\\
\Hom_A\Bigl(M,\prod_{i\in I}N_i\Bigr)&\xrightarrow{\sim}\prod_{i\in I}\Hom_A(M,N_i),
& f&\longmapsto(\pi_i\circ f)_{i\in I}.
\end{aligned}
\]
There is also a natural injection
\[
\bigoplus_{i\in I}\Hom_A(M,N_i)\longrightarrow
\Hom_A\Bigl(M,\bigoplus_{i\in I}N_i\Bigr),
\qquad (f_i)_{i\in I}\longmapsto\bigl(m\mapsto(f_i(m))_{i\in I}\bigr),
\]
which is an isomorphism when $M$ is finitely generated.
\end{lemma}

\begin{proof}
The inverse of the first map sends $(f_i)_{i\in I}$ to $(m_i)_{i\in I}\mapsto\sum_{i\in I}f_i(m_i)$; the sum is finite because $(m_i)_{i\in I}$ has finite support.
The inverse of the second sends $(f_i)_{i\in I}$ to $m\mapsto(f_i(m))_{i\in I}$; a direct product imposes no support condition.
For the third map, coordinate projections recover each $f_i$, proving injectivity.
If $m_1,\ldots,m_r$ generate $M$, the images of these generators under $f:M\to\bigoplus_{i\in I}N_i$ are supported on a common finite subset $J\subset I$.
Then $f(M)\subset\bigoplus_{i\in J}N_i$, so $f$ comes from a finite family of maps.
All three constructions commute with precomposition and postcomposition.
\end{proof}

\begin{proposition}[Tensor products and direct products]\label{prop:tensor-direct-products}
Let $A$ be a $\Bbbk$-algebra, $M,M_i$ right $A$-modules, and $N,N_i$ left $A$-modules, with $i\in I$.
The coordinate projections define linear maps
\begin{equation}\label{eq:module-tensor-products}
\begin{aligned}
\kappa_N:\Bigl(\prod_iM_i\Bigr)\otimes_A N
&\longrightarrow\prod_i(M_i\otimes_A N),
& (m_i)_i\otimes n&\longmapsto(m_i\otimes n)_i,\\
\lambda_M:M\otimes_A\Bigl(\prod_iN_i\Bigr)
&\longrightarrow\prod_i(M\otimes_A N_i),
& m\otimes(n_i)_i&\longmapsto(m\otimes n_i)_i.
\end{aligned}
\end{equation}
\begin{enumerate}
\item If $I$ is finite, both maps are isomorphisms.
\item The map $\kappa_N$ is an isomorphism if $N$ is a direct summand of $A^{\oplus r}$ as a left module for some finite $r$.
The corresponding condition on the right module $M$ makes $\lambda_M$ an isomorphism.
\item If $A$ is finite-dimensional semisimple, both maps are injective.
Moreover, $\kappa_N$ is an isomorphism when $N$ is finite-dimensional, and $\lambda_M$ is an isomorphism when $M$ is finite-dimensional.
\end{enumerate}
\end{proposition}

\begin{proof}
The formulas in \eqref{eq:module-tensor-products} are bilinear. For $s\in A$, the component identities
$(m_is)\otimes n=m_i\otimes sn$ and $(ms)\otimes n_i=m\otimes sn_i$
show that both formulas give well-defined maps from the indicated tensor products.
For finite $I$, products equal sums, and Lemma~\ref{lem:tensor-properties}(4) proves (1).

For $N=A$, the map $\kappa_A$ is the identity on $\prod_iM_i$ under $m\otimes s\mapsto ms$.
For $N=A^{\oplus r}$, both sides are $(\prod_iM_i)^{\oplus r}$, since a finite direct sum commutes with a direct product.
If $N\oplus N'\cong A^{\oplus r}$, the comparison for $N\oplus N'$ is $\kappa_N\oplus\kappa_{N'}$.
Its bijectivity implies the bijectivity of $\kappa_N$.
This proves the assertion about $\kappa_N$ in (2).

Now let $A$ be finite-dimensional semisimple.
For finite-dimensional $N$, Corollary~\ref{cor:semisimple-summands} gives (2).
For arbitrary $N$, take $z=\sum_{\ell=1}^r m^{(\ell)}\otimes n_\ell$ in $\Ker\kappa_N$ and set $N_0=\sum_{\ell=1}^r An_\ell$.
The submodule $N_0$ is finite-dimensional and has a complement in $N$ by Theorem~\ref{thm:artin-wedderburn}.
Thus the inclusions
\[
\Bigl(\prod_iM_i\Bigr)\otimes_A N_0
\longrightarrow\Bigl(\prod_iM_i\Bigr)\otimes_A N,
\qquad
M_i\otimes_A N_0\longrightarrow M_i\otimes_A N
\]
are injective, by the direct sum formula in Lemma~\ref{lem:tensor-properties}(4).
Regard $z$ as an element with second factors in $N_0$.
The equality $\kappa_N(z)=0$ then gives $\kappa_{N_0}(z)=0$.
Aince $\kappa_{N_0}$ is an isomorphism, $z=0$.

For $\lambda_M$, apply the same arguments over $A^\op$, using
$N\otimes_{A^\op}M\cong M\otimes_A N$, $n\otimes m\mapsto m\otimes n$.
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

---

## Replacement 3: Describe functoriality by induced maps

**Source:** [Lecture 2, line 1842](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1842)  
**Added:** `+14` lines | **Removed:** `-13` lines

Keep the existing functors over an arbitrary algebra. Distinguish the defining bilinear formula from the induced linear map, name the module sides, and avoid calling a non-central element of S a scalar.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1842,30 +1855,31 @@
-For right module maps $u:M\to M'$ and left module maps $v:N\to N'$, the universal property defines
+For right $A$-module maps $u:M\to M'$ and left $A$-module maps $v:N\to N'$, the bilinear map
+$M\times N\to M'\otimes_A N'$, $(m,n)\mapsto u(m)\otimes v(n)$, induces
 \[
-u\otimes_S v:M\otimes_S N\longrightarrow M'\otimes_S N',
+u\otimes_A v:M\otimes_A N\longrightarrow M'\otimes_A N',
 \qquad m\otimes n\longmapsto u(m)\otimes v(n).
 \]
 These maps satisfy
 \[
 (u'\otimes v')\circ(u\otimes v)=(u'\circ u)\otimes(v'\circ v),
 \qquad
-\id_M\otimes\id_N=\id_{M\otimes_S N}
+\id_M\otimes\id_N=\id_{M\otimes_A N}
 \]
 whenever the maps are composable.
 Thus, for fixed $N$ and fixed $M$, respectively, tensor product gives functors
 \[
-(-)\otimes_S N:\Mod S\longrightarrow\Mod\Bbbk,
+(-)\otimes_A N:\Mod A\longrightarrow\Mod\Bbbk,
 \qquad
-M\otimes_S(-):\Mod(S^\op)\longrightarrow\Mod\Bbbk.
+M\otimes_A(-):\Mod(A^\op)\longrightarrow\Mod\Bbbk.
 \]
-For bimodules and bimodule maps, the same construction preserves the outer actions in Lemma~\ref{lem:tensor-properties}(2).
+For bimodule maps $u,v$, the map $u\otimes_A v$ preserves the outer actions in Lemma~\ref{lem:tensor-properties}(2).
 
-The equality $ms\otimes_S n=m\otimes_S sn$ allows a scalar from $S$ to pass between adjacent factors.
-For an $S$-bimodule $V$, define
+The identity $ms\otimes_A n=m\otimes_A sn$ moves an element of $A$ between adjacent factors.
+For a bimodule ${}_AV_A$, define
 \[
-V^{\otimes_S 0}:=S,\qquad
-V^{\otimes_S i}:=
-\underbrace{V\otimes_S\cdots\otimes_S V}_{i\text{ factors}}
-\quad (i\geq 1).
+V^{\otimes_A 0}:=A,\qquad
+V^{\otimes_A i}:=
+\underbrace{V\otimes_A\cdots\otimes_A V}_{i\text{ factors}}
+\quad(i\geq1).
 \]
-Lemma~\ref{lem:tensor-properties} makes these $S$-bimodules independent of parenthesisation and supplies the identifications used in concatenation.
+Lemma~\ref{lem:tensor-properties}(3) identifies all parenthesisations as $A$-bimodules.
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
For right module maps $u:M\to M'$ and left module maps $v:N\to N'$, the universal property defines
\[
u\otimes_S v:M\otimes_S N\longrightarrow M'\otimes_S N',
\qquad m\otimes n\longmapsto u(m)\otimes v(n).
\]
These maps satisfy
\[
(u'\otimes v')\circ(u\otimes v)=(u'\circ u)\otimes(v'\circ v),
\qquad
\id_M\otimes\id_N=\id_{M\otimes_S N}
\]
whenever the maps are composable.
Thus, for fixed $N$ and fixed $M$, respectively, tensor product gives functors
\[
(-)\otimes_S N:\Mod S\longrightarrow\Mod\Bbbk,
\qquad
M\otimes_S(-):\Mod(S^\op)\longrightarrow\Mod\Bbbk.
\]
For bimodules and bimodule maps, the same construction preserves the outer actions in Lemma~\ref{lem:tensor-properties}(2).

The equality $ms\otimes_S n=m\otimes_S sn$ allows a scalar from $S$ to pass between adjacent factors.
For an $S$-bimodule $V$, define
\[
V^{\otimes_S 0}:=S,\qquad
V^{\otimes_S i}:=
\underbrace{V\otimes_S\cdots\otimes_S V}_{i\text{ factors}}
\quad (i\geq 1).
\]
Lemma~\ref{lem:tensor-properties} makes these $S$-bimodules independent of parenthesisation and supplies the identifications used in concatenation.

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
For right $A$-module maps $u:M\to M'$ and left $A$-module maps $v:N\to N'$, the bilinear map
$M\times N\to M'\otimes_A N'$, $(m,n)\mapsto u(m)\otimes v(n)$, induces
\[
u\otimes_A v:M\otimes_A N\longrightarrow M'\otimes_A N',
\qquad m\otimes n\longmapsto u(m)\otimes v(n).
\]
These maps satisfy
\[
(u'\otimes v')\circ(u\otimes v)=(u'\circ u)\otimes(v'\circ v),
\qquad
\id_M\otimes\id_N=\id_{M\otimes_A N}
\]
whenever the maps are composable.
Thus, for fixed $N$ and fixed $M$, respectively, tensor product gives functors
\[
(-)\otimes_A N:\Mod A\longrightarrow\Mod\Bbbk,
\qquad
M\otimes_A(-):\Mod(A^\op)\longrightarrow\Mod\Bbbk.
\]
For bimodule maps $u,v$, the map $u\otimes_A v$ preserves the outer actions in Lemma~\ref{lem:tensor-properties}(2).

The identity $ms\otimes_A n=m\otimes_A sn$ moves an element of $A$ between adjacent factors.
For a bimodule ${}_AV_A$, define
\[
V^{\otimes_A 0}:=A,\qquad
V^{\otimes_A i}:=
\underbrace{V\otimes_A\cdots\otimes_A V}_{i\text{ factors}}
\quad(i\geq1).
\]
Lemma~\ref{lem:tensor-properties}(3) identifies all parenthesisations as $A$-bimodules.

```

</details>

---

## Replacement 4: State tensor duality over arbitrary algebras with the precise hypotheses

**Source:** [Lecture 2, line 1872](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1872)  
**Added:** `+47` lines | **Removed:** `-19` lines

Implement the accepted general (A,B,C) formulation. State the right- and left-module direct-summand hypotheses separately, introduce all four duals and their actions, and then specialise to semisimple S. Retain the existing proposition and equation labels used in later lectures. The proof remains with the exercise and its hidden solution; Replacement 14 supplies the general proof there.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1872,14 +1886,19 @@
-For an $S$-bimodule $M$, the right and left $S$-duals of Definition~\ref{def:S-duals} are themselves $S$-bimodules, with actions
-\begin{equation}\label{eq:tensor-dual-actions}
-(sft)(m)=sf(tm),\qquad
-(sgt)(m)=g(ms)t
-\quad(s,t\in S,\ m\in M).
+Let $A,B,C$ be arbitrary $\Bbbk$-algebras, and consider bimodules ${}_AM_B$, ${}_BN_C$.
+The dual constructions of Definition~\ref{def:S-duals} make sense over these algebras:
+\[
+\begin{aligned}
+M^*&=\Hom_B(M,B),&{}^*M&=\Hom_{A^\op}(M,A),\\
+N^*&=\Hom_C(N,C),&{}^*N&=\Hom_{B^\op}(N,B).
+\end{aligned}
+\]
+Both $M^*$ and ${}^*M$ are bimodules ${}_B(M^*)_A$ and ${}_B({}^*M)_A$, respectively.
+For $b\in B$, $a\in A$, and $m\in M$, the actions are
+\begin{equation}\label{eq:general-tensor-dual-actions}
+(bfa)(m)=bf(am)\quad(f\in M^*),\qquad
+(bga)(m)=g(mb)a\quad(g\in{}^*M).
 \end{equation}
-Here $f\in M^*$ and $g\in{}^*M$.
-The duals are ungraded; the parenthesised stars of Definition~\ref{def:graded-S-duals} denote different, graded constructions.
-
-Tensor duality reverses the order of the factors.
-The following maps use only the $S$-module actions; no basis or symmetrising form is chosen.
+Replacing $(A,B,M)$ by $(B,C,N)$ gives the actions on the bimodules ${}_C(N^*)_B$ and ${}_C({}^*N)_B$.
+The right dual of $M\otimes_B N$ is taken over $C$, and the left dual over $A$.
 
 \begin{proposition}[Tensor duality]\label{prop:tensor-duals}
 % TODO (ChangeProposal9, Lecture 2 follow-up): Explain the general case for
@@ -1889,28 +1908,51 @@
 % Keep the idempotent-matching calculation in the main exposition and move
 % routine verification to supplementary material. Use the one-sided bimodule
 % actions from eq:bimodule-dual-actions, independently of a symmetrising form.
-Let $S$ be finite-dimensional semisimple and let $V,W$ be finite-dimensional $S$-bimodules.
-There are bimodule isomorphisms, natural in $V,W$,
+There are bimodule maps, natural in $M,N$,
+\begin{equation}\label{eq:general-tensor-duals}
+\begin{aligned}
+\theta_r &: N^*\otimes_B M^*\longrightarrow(M\otimes_B N)^*,\\
+\theta_r(g\otimes f)(m\otimes n)&=g(f(m)n),\\
+\theta_\ell &: {}^*N\otimes_B{}^*M\longrightarrow{}^*(M\otimes_B N),\\
+\theta_\ell(g\otimes f)(m\otimes n)&=f(mg(n)).
+\end{aligned}
+\end{equation}
+\begin{enumerate}
+\item The map $\theta_r$ is an isomorphism if $M$ is a direct summand of $B^{\oplus r}$ as a right $B$-module for some integer $r\geq0$.
+\item The map $\theta_\ell$ is an isomorphism if $N$ is a direct summand of $B^{\oplus r}$ as a left $B$-module for some integer $r\geq0$.
+\end{enumerate}
+\end{proposition}
+
+Now let $S$ be finite-dimensional semisimple, and consider bimodules ${}_SV_S$, ${}_SW_S$, with $V$ finitely generated on the right and $W$ finitely generated on the left.
+Since $S$ is finite-dimensional, $V,W$ are finite-dimensional.
+Corollary~\ref{cor:semisimple-summands} gives both direct-summand conditions with $A=B=C=S$, $M=V$, and $N=W$.
+Hence
 \begin{equation}\label{eq:tensor-duals}
 \begin{aligned}
 \theta_r &: W^*\otimes_S V^*\xrightarrow{\sim}(V\otimes_S W)^*,\\
 \theta_\ell &: {}^*W\otimes_S {}^*V\xrightarrow{\sim}{}^*(V\otimes_S W),
 \end{aligned}
 \end{equation}
-defined by
+where
 \begin{equation}\label{eq:tensor-evaluations}
 \theta_r(g\otimes f)(v\otimes w)=g(f(v)w),
 \qquad
 \theta_\ell(g\otimes f)(v\otimes w)=f(vg(w)).
 \end{equation}
-\end{proposition}
+For $M\in\{V,W\}$, the bimodule ${}_SM_S$ has actions
+\begin{equation}\label{eq:tensor-dual-actions}
+(sft)(m)=sf(tm),\qquad
+(sgt)(m)=g(ms)t
+\quad(s,t\in S,\ m\in M).
+\end{equation}
+Here $f\in M^*$ and $g\in{}^*M$.
+These duals are ungraded; the parenthesised stars in Definition~\ref{def:graded-S-duals} denote the graded duals.
 
 \begin{convention}[Tensor duals]
-For $S,V,W$ as in Proposition~\ref{prop:tensor-duals}, we use $\theta_r$ and $\theta_\ell$ in \eqref{eq:tensor-duals} to identify the dual of a tensor product with the tensor product of the corresponding duals in reverse order.
-The values of these functionals are always given by \eqref{eq:tensor-evaluations}.
-These are the canonical identifications used below; they do not identify $M^*$, $ {}^*M$, and $D(M)$ with one another.
-Comparisons with $D(M)$ use a chosen symmetrising form, as in \eqref{eq:dual-comparison}.
+For $S,V,W$ as in \eqref{eq:tensor-duals}, identify the dual of a tensor product with the tensor product of the corresponding duals in reverse order, using the maps in \eqref{eq:tensor-evaluations}.
+No basis or symmetrising form is needed.
+Comparisons of $M^*$, $ {}^*M$, and $D(M)$ instead use a chosen symmetrising form, as in \eqref{eq:dual-comparison}.
 \end{convention}
 
-The proof of Proposition~\ref{prop:tensor-duals} is Exercise~\ref{ex:tensor-duality-proof}.
+Exercise~\ref{ex:tensor-duality-proof} proves the semisimple case of Proposition~\ref{prop:tensor-duals}.
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
For an $S$-bimodule $M$, the right and left $S$-duals of Definition~\ref{def:S-duals} are themselves $S$-bimodules, with actions
\begin{equation}\label{eq:tensor-dual-actions}
(sft)(m)=sf(tm),\qquad
(sgt)(m)=g(ms)t
\quad(s,t\in S,\ m\in M).
\end{equation}
Here $f\in M^*$ and $g\in{}^*M$.
The duals are ungraded; the parenthesised stars of Definition~\ref{def:graded-S-duals} denote different, graded constructions.

Tensor duality reverses the order of the factors.
The following maps use only the $S$-module actions; no basis or symmetrising form is chosen.

\begin{proposition}[Tensor duality]\label{prop:tensor-duals}
% TODO (ChangeProposal9, Lecture 2 follow-up): Explain the general case for
% an (A,B)-bimodule M and a (B,C)-bimodule N. For right duals, require M_B
% finitely generated projective; for left duals, require _B N finitely generated
% projective. Finite k-dimension alone does not suffice over a general algebra.
% Keep the idempotent-matching calculation in the main exposition and move
% routine verification to supplementary material. Use the one-sided bimodule
% actions from eq:bimodule-dual-actions, independently of a symmetrising form.
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

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
Let $A,B,C$ be arbitrary $\Bbbk$-algebras, and consider bimodules ${}_AM_B$, ${}_BN_C$.
The dual constructions of Definition~\ref{def:S-duals} make sense over these algebras:
\[
\begin{aligned}
M^*&=\Hom_B(M,B),&{}^*M&=\Hom_{A^\op}(M,A),\\
N^*&=\Hom_C(N,C),&{}^*N&=\Hom_{B^\op}(N,B).
\end{aligned}
\]
Both $M^*$ and ${}^*M$ are bimodules ${}_B(M^*)_A$ and ${}_B({}^*M)_A$, respectively.
For $b\in B$, $a\in A$, and $m\in M$, the actions are
\begin{equation}\label{eq:general-tensor-dual-actions}
(bfa)(m)=bf(am)\quad(f\in M^*),\qquad
(bga)(m)=g(mb)a\quad(g\in{}^*M).
\end{equation}
Replacing $(A,B,M)$ by $(B,C,N)$ gives the actions on the bimodules ${}_C(N^*)_B$ and ${}_C({}^*N)_B$.
The right dual of $M\otimes_B N$ is taken over $C$, and the left dual over $A$.

\begin{proposition}[Tensor duality]\label{prop:tensor-duals}
% TODO (ChangeProposal9, Lecture 2 follow-up): Explain the general case for
% an (A,B)-bimodule M and a (B,C)-bimodule N. For right duals, require M_B
% finitely generated projective; for left duals, require _B N finitely generated
% projective. Finite k-dimension alone does not suffice over a general algebra.
% Keep the idempotent-matching calculation in the main exposition and move
% routine verification to supplementary material. Use the one-sided bimodule
% actions from eq:bimodule-dual-actions, independently of a symmetrising form.
There are bimodule maps, natural in $M,N$,
\begin{equation}\label{eq:general-tensor-duals}
\begin{aligned}
\theta_r &: N^*\otimes_B M^*\longrightarrow(M\otimes_B N)^*,\\
\theta_r(g\otimes f)(m\otimes n)&=g(f(m)n),\\
\theta_\ell &: {}^*N\otimes_B{}^*M\longrightarrow{}^*(M\otimes_B N),\\
\theta_\ell(g\otimes f)(m\otimes n)&=f(mg(n)).
\end{aligned}
\end{equation}
\begin{enumerate}
\item The map $\theta_r$ is an isomorphism if $M$ is a direct summand of $B^{\oplus r}$ as a right $B$-module for some integer $r\geq0$.
\item The map $\theta_\ell$ is an isomorphism if $N$ is a direct summand of $B^{\oplus r}$ as a left $B$-module for some integer $r\geq0$.
\end{enumerate}
\end{proposition}

Now let $S$ be finite-dimensional semisimple, and consider bimodules ${}_SV_S$, ${}_SW_S$, with $V$ finitely generated on the right and $W$ finitely generated on the left.
Since $S$ is finite-dimensional, $V,W$ are finite-dimensional.
Corollary~\ref{cor:semisimple-summands} gives both direct-summand conditions with $A=B=C=S$, $M=V$, and $N=W$.
Hence
\begin{equation}\label{eq:tensor-duals}
\begin{aligned}
\theta_r &: W^*\otimes_S V^*\xrightarrow{\sim}(V\otimes_S W)^*,\\
\theta_\ell &: {}^*W\otimes_S {}^*V\xrightarrow{\sim}{}^*(V\otimes_S W),
\end{aligned}
\end{equation}
where
\begin{equation}\label{eq:tensor-evaluations}
\theta_r(g\otimes f)(v\otimes w)=g(f(v)w),
\qquad
\theta_\ell(g\otimes f)(v\otimes w)=f(vg(w)).
\end{equation}
For $M\in\{V,W\}$, the bimodule ${}_SM_S$ has actions
\begin{equation}\label{eq:tensor-dual-actions}
(sft)(m)=sf(tm),\qquad
(sgt)(m)=g(ms)t
\quad(s,t\in S,\ m\in M).
\end{equation}
Here $f\in M^*$ and $g\in{}^*M$.
These duals are ungraded; the parenthesised stars in Definition~\ref{def:graded-S-duals} denote the graded duals.

\begin{convention}[Tensor duals]
For $S,V,W$ as in \eqref{eq:tensor-duals}, identify the dual of a tensor product with the tensor product of the corresponding duals in reverse order, using the maps in \eqref{eq:tensor-evaluations}.
No basis or symmetrising form is needed.
Comparisons of $M^*$, $ {}^*M$, and $D(M)$ instead use a chosen symmetrising form, as in \eqref{eq:dual-comparison}.
\end{convention}

Exercise~\ref{ex:tensor-duality-proof} proves the semisimple case of Proposition~\ref{prop:tensor-duals}.

```

</details>

---

## Replacement 5: Explain the finiteness restriction and deduce the linear-dual formula

**Source:** [Lecture 2, line 1917](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1917)  
**Added:** `+17` lines | **Removed:** `-7` lines

Record the accepted cyclic-module counterexample only as advanced material. Deduce the existing linear-dual comparison directly from the general proposition instead of repeating the finite-summand proof. Keep the citation and all subsequent two-sided-dual material inside the advanced block.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1917,5 +1959,20 @@
 \begin{advanced}
-For the ungraded $\Bbbk$-linear dual $D$, there is also a natural bimodule isomorphism \cite[\S2.1]{GI20}
+\begin{example}\label{ex:tensor-dual-finite-generation}
+Finite generation alone does not suffice in Proposition~\ref{prop:tensor-duals} over a general algebra.
+Take $A=C=\Bbbk$, $B=\Bbbk[x]$, and bimodules ${}_\Bbbk M_B$, ${}_BN_\Bbbk$ with $M=N=B/(x)\cong\Bbbk$ and the outer $\Bbbk$-actions given by scalar multiplication.
+Every $f\in\Hom_B(M,B)$ satisfies $f(\overline1)x=f(\overline1x)=0$, hence $f=0$.
+Consequently
+\[
+N^*\otimes_B M^*=0,\qquad
+(M\otimes_B N)^*
+=\Hom_\Bbbk(\Bbbk,\Bbbk)\cong\Bbbk.
+\]
+Both $M_B$ and $ {}_B N$ are generated by $\overline1$, so neither direct-summand hypothesis can be replaced by finite generation alone.
+For the left dual, $ {}^*N=\Hom_{B^\op}(N,B)=0$, whereas $ {}^*(M\otimes_B N)\cong\Bbbk$.
+\end{example}
+
+For $S,V,W$ as in \eqref{eq:tensor-duals}, take $A=B=S$, $C=\Bbbk$, $M=V$, and $N=W$ in Proposition~\ref{prop:tensor-duals}.
+Then $N^*=D(W)$, giving the natural bimodule isomorphism \cite[\S2.1]{GI20}
 \[
 \begin{aligned}
 \theta_D:D(W)\otimes_S V^*&\xrightarrow{\sim}D(V\otimes_S W),\\
@@ -1923,10 +1980,5 @@
 \end{aligned}
 \]
 The actions on $D(W)$ are those in \eqref{eq:bimodule-dual-actions}.
-For $s\in S$, the equalities
-$\lambda(f(vs)w)=\lambda(f(v)sw)$ and
-$(\lambda s)(f(v)w)=\lambda(sf(v)w)=\lambda((sf)(v)w)$
-show that the formula gives the same value on $vs\otimes w$ and $v\otimes sw$, and on $\lambda s\otimes f$ and $\lambda\otimes sf$.
-For $V=S$, the map is the isomorphism $D(W)\otimes_S S\to D(W)$, $\lambda\otimes s\mapsto\lambda s$.
-The formula commutes with right $S$-module maps in $V$, so finite direct sums and direct summands preserve bijectivity; Corollary~\ref{cor:semisimple-summands} applies to $V$.
+For $s\in S$, naturality with respect to $W\to W$, $w\mapsto ws$, gives left $S$-linearity of $\theta_D$.
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{advanced}
For the ungraded $\Bbbk$-linear dual $D$, there is also a natural bimodule isomorphism \cite[\S2.1]{GI20}
\[
\begin{aligned}
\theta_D:D(W)\otimes_S V^*&\xrightarrow{\sim}D(V\otimes_S W),\\
\theta_D(\lambda\otimes f)(v\otimes w)&=\lambda(f(v)w).
\end{aligned}
\]
The actions on $D(W)$ are those in \eqref{eq:bimodule-dual-actions}.
For $s\in S$, the equalities
$\lambda(f(vs)w)=\lambda(f(v)sw)$ and
$(\lambda s)(f(v)w)=\lambda(sf(v)w)=\lambda((sf)(v)w)$
show that the formula gives the same value on $vs\otimes w$ and $v\otimes sw$, and on $\lambda s\otimes f$ and $\lambda\otimes sf$.
For $V=S$, the map is the isomorphism $D(W)\otimes_S S\to D(W)$, $\lambda\otimes s\mapsto\lambda s$.
The formula commutes with right $S$-module maps in $V$, so finite direct sums and direct summands preserve bijectivity; Corollary~\ref{cor:semisimple-summands} applies to $V$.

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{advanced}
\begin{example}\label{ex:tensor-dual-finite-generation}
Finite generation alone does not suffice in Proposition~\ref{prop:tensor-duals} over a general algebra.
Take $A=C=\Bbbk$, $B=\Bbbk[x]$, and bimodules ${}_\Bbbk M_B$, ${}_BN_\Bbbk$ with $M=N=B/(x)\cong\Bbbk$ and the outer $\Bbbk$-actions given by scalar multiplication.
Every $f\in\Hom_B(M,B)$ satisfies $f(\overline1)x=f(\overline1x)=0$, hence $f=0$.
Consequently
\[
N^*\otimes_B M^*=0,\qquad
(M\otimes_B N)^*
=\Hom_\Bbbk(\Bbbk,\Bbbk)\cong\Bbbk.
\]
Both $M_B$ and $ {}_B N$ are generated by $\overline1$, so neither direct-summand hypothesis can be replaced by finite generation alone.
For the left dual, $ {}^*N=\Hom_{B^\op}(N,B)=0$, whereas $ {}^*(M\otimes_B N)\cong\Bbbk$.
\end{example}

For $S,V,W$ as in \eqref{eq:tensor-duals}, take $A=B=S$, $C=\Bbbk$, $M=V$, and $N=W$ in Proposition~\ref{prop:tensor-duals}.
Then $N^*=D(W)$, giving the natural bimodule isomorphism \cite[\S2.1]{GI20}
\[
\begin{aligned}
\theta_D:D(W)\otimes_S V^*&\xrightarrow{\sim}D(V\otimes_S W),\\
\theta_D(\lambda\otimes f)(v\otimes w)&=\lambda(f(v)w).
\end{aligned}
\]
The actions on $D(W)$ are those in \eqref{eq:bimodule-dual-actions}.
For $s\in S$, naturality with respect to $W\to W$, $w\mapsto ws$, gives left $S$-linearity of $\theta_D$.

```

</details>

---

## Replacement 6: Use the index k in the outer-idempotent example

**Source:** [Lecture 2, line 1969](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:1969)  
**Added:** `+5` lines | **Removed:** `-4` lines

Replace the unexplained choice of ell by k, state the index range, and lead with the precise purpose of the example.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -1969,10 +2021,11 @@
 \begin{example}
-Let $S=\Bbbk^{\oplus r}$ with coordinate idempotents $e_1,\ldots,e_r$, and suppose $V=e_iVe_j$ and $W=e_jWe_\ell$. \comm{why not use $k$ but use $\ell$????}
+Tensor duality reverses the two outer idempotents.
+Let $S=\Bbbk^{\oplus r}$ with coordinate idempotents $e_1,\ldots,e_r$, and consider bimodules ${}_SV_S$, ${}_SW_S$ with $V=e_iVe_j$ and $W=e_jWe_k$, where $1\leq i,j,k\leq r$.
 By \eqref{eq:tensor-dual-actions},
 \[
-V\otimes_S W=e_i(V\otimes_S W)e_\ell,\qquad
-W^*\otimes_S V^*=e_\ell(W^*\otimes_S V^*)e_i.
+V\otimes_S W=e_i(V\otimes_S W)e_k,\qquad
+W^*\otimes_S V^*=e_k(W^*\otimes_S V^*)e_i.
 \]
-Thus $\theta_r$ in \eqref{eq:tensor-duals} reverses the two outer idempotents.
+The isomorphism $\theta_r$ in \eqref{eq:tensor-duals} therefore interchanges the left index $i$ and the right index $k$.
 \end{example}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{example}
Let $S=\Bbbk^{\oplus r}$ with coordinate idempotents $e_1,\ldots,e_r$, and suppose $V=e_iVe_j$ and $W=e_jWe_\ell$. \comm{why not use $k$ but use $\ell$????}
By \eqref{eq:tensor-dual-actions},
\[
V\otimes_S W=e_i(V\otimes_S W)e_\ell,\qquad
W^*\otimes_S V^*=e_\ell(W^*\otimes_S V^*)e_i.
\]
Thus $\theta_r$ in \eqref{eq:tensor-duals} reverses the two outer idempotents.
\end{example}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{example}
Tensor duality reverses the two outer idempotents.
Let $S=\Bbbk^{\oplus r}$ with coordinate idempotents $e_1,\ldots,e_r$, and consider bimodules ${}_SV_S$, ${}_SW_S$ with $V=e_iVe_j$ and $W=e_jWe_k$, where $1\leq i,j,k\leq r$.
By \eqref{eq:tensor-dual-actions},
\[
V\otimes_S W=e_i(V\otimes_S W)e_k,\qquad
W^*\otimes_S V^*=e_k(W^*\otimes_S V^*)e_i.
\]
The isomorphism $\theta_r$ in \eqref{eq:tensor-duals} therefore interchanges the left index $i$ and the right index $k$.
\end{example}

```

</details>

---

## Replacement 7: Move the polynomial-matrix example into supplementary material

**Source:** [Lecture 2, line 2008](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2008)  
**Added:** `+8` lines | **Removed:** `-2` lines

Use the requested symbolic matrix description and make the entire example supplementary. Preserve its grading and computations.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2008,7 +2061,12 @@
+\begin{supplementary}
 \begin{example}\label{ex:triangular-polynomials}
 \emergencystretch=1em
-\comm{put as supplementary}
-Let $A$ be the algebra of upper triangular $2\times2$ matrices over $\Bbbk[x]$ \comm{write the symbolic instead of using word}, graded by $\deg(x^m e_{ij})=m+j-i$ for $m\geq0$ and $1\leq i\leq j\leq2$.
+Let
+\[
+A=\begin{pmatrix}\Bbbk[x]&\Bbbk[x]\\0&\Bbbk[x]\end{pmatrix},
+\qquad \deg(x^m e_{ij})=m+j-i
+\quad(m\geq0,\ 1\leq i\leq j\leq2).
+\]
 Then
 \[
 A_0=\Bbbk e_{11}\oplus\Bbbk e_{22},\qquad
@@ -2024,4 +2082,5 @@
 \]
 Here $A_0$ has two simple summands, $A_d\neq0$ for every $d\geq0$, and $A$ is non-commutative: $e_{11}e_{12}=e_{12}$ whereas $e_{12}e_{11}=0$.
 \end{example}
+\end{supplementary}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:triangular-polynomials}
\emergencystretch=1em
\comm{put as supplementary}
Let $A$ be the algebra of upper triangular $2\times2$ matrices over $\Bbbk[x]$ \comm{write the symbolic instead of using word}, graded by $\deg(x^m e_{ij})=m+j-i$ for $m\geq0$ and $1\leq i\leq j\leq2$.
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

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{supplementary}
\begin{example}\label{ex:triangular-polynomials}
\emergencystretch=1em
Let
\[
A=\begin{pmatrix}\Bbbk[x]&\Bbbk[x]\\0&\Bbbk[x]\end{pmatrix},
\qquad \deg(x^m e_{ij})=m+j-i
\quad(m\geq0,\ 1\leq i\leq j\leq2).
\]
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
\end{supplementary}

```

</details>

---

## Replacement 8: Specify multiplication in the tensor algebra explicitly

**Source:** [Lecture 2, line 2035](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2035)  
**Added:** `+16` lines | **Removed:** `-10` lines

Make the multiplication precise without unexplained 'concatenation of tensors' or the ambiguous instruction to extend S-linearly. Move the alternative name outside the definition and use 'element' consistently in this passage.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2035,22 +2094,28 @@
 \begin{definition}\label{def:tensor-algebra}
-Let $S$ be a $\Bbbk$-algebra and $V$ an $S$-bimodule.
-The \defn{tensor algebra of $V$ (over $S$)} is
+Let $S$ be a $\Bbbk$-algebra and consider a bimodule ${}_SV_S$.
+The \defn{tensor algebra of $V$ over $S$} is
 \[
 T_S(V):=\bigoplus_{i\in\Z}T_S(V)_i,
 \quad\text{where}\quad
 T_S(V)_i=
 \begin{cases}
-V^{\otimes_S i},&i\geq 1,\\
+V^{\otimes_S i},&i\geq1,\\
 S,&i=0,\\
 0,&i<0,
-\end{cases}
+\end{cases}.
 \]
-with multiplication given by concatenation of tensors and extend $S$-linearly.  We also speak of tensor algebra generated by $V$ to mean the same thing.
+For $v_1,\ldots,v_{p+q}\in V$, multiplication is determined $\Bbbk$-bilinearly by
+\[
+(v_1\otimes_S\cdots\otimes_S v_p)(v_{p+1}\otimes_S\cdots\otimes_S v_{p+q})
+=v_1\otimes_S\cdots\otimes_S v_{p+q}
+\qquad(p,q\geq1),
+\]
+and by the left and right $S$-actions when a factor has degree $0$.
 \end{definition}
 
-Every element of $T_S(V)$ is a finite sum of tensors, since the grading is a direct sum.
-The unit is $1_S\in T_S(V)_0$.
-Associativity follows from the associativity and unit isomorphisms in Lemma~\ref{lem:tensor-properties}(3).
-The left and right $S$-actions determine which factors can be concatenated.
-Juxtaposition $v_1\cdots v_d$ in $T_S(V)$ denotes $v_1\otimes_S\cdots\otimes_S v_d$; in any quotient algebra of $T_S(V)$ it denotes the image of (the canoncial projection) that tensor.
+We also call $T_S(V)$ the tensor algebra generated by $V$ over $S$.
+Every element has finitely many non-zero homogeneous components.
+The unit is $1_S$, and associativity follows from Lemma~\ref{lem:tensor-properties}(3).
+Write $v_1\cdots v_d$ for $v_1\otimes_S\cdots\otimes_S v_d$ in $T_S(V)$.
+In a quotient algebra of $T_S(V)$, the notation $v_1\cdots v_d$ denotes the image of $v_1\otimes_S\cdots\otimes_S v_d$.
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{definition}\label{def:tensor-algebra}
Let $S$ be a $\Bbbk$-algebra and $V$ an $S$-bimodule.
The \defn{tensor algebra of $V$ (over $S$)} is
\[
T_S(V):=\bigoplus_{i\in\Z}T_S(V)_i,
\quad\text{where}\quad
T_S(V)_i=
\begin{cases}
V^{\otimes_S i},&i\geq 1,\\
S,&i=0,\\
0,&i<0,
\end{cases}
\]
with multiplication given by concatenation of tensors and extend $S$-linearly.  We also speak of tensor algebra generated by $V$ to mean the same thing.
\end{definition}

Every element of $T_S(V)$ is a finite sum of tensors, since the grading is a direct sum.
The unit is $1_S\in T_S(V)_0$.
Associativity follows from the associativity and unit isomorphisms in Lemma~\ref{lem:tensor-properties}(3).
The left and right $S$-actions determine which factors can be concatenated.
Juxtaposition $v_1\cdots v_d$ in $T_S(V)$ denotes $v_1\otimes_S\cdots\otimes_S v_d$; in any quotient algebra of $T_S(V)$ it denotes the image of (the canoncial projection) that tensor.

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

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
In a quotient algebra of $T_S(V)$, the notation $v_1\cdots v_d$ denotes the image of $v_1\otimes_S\cdots\otimes_S v_d$.

```

</details>

---

## Replacement 9: Make the symmetric and exterior algebra example symbolic and compact

**Source:** [Lecture 2, line 2057](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2057)  
**Added:** `+22` lines | **Removed:** `-10` lines

Replace the verbal description of the degree 0 and degree 1 components by equalities. Keep V and W independent, retain the bases and characteristic-free relations, and place the basis verification in supplementary material.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2057,23 +2122,35 @@
 \begin{example}[Polynomial and exterior algebras]\label{ex:polynomial-exterior}
-Let $V,W$ be finite-dimensional vector spaces with bases $x_1,\ldots,x_n$ and $y_1,\ldots,y_m$, respectively.
+Let $V,W$ be finite-dimensional vector spaces with bases $\{x_i\mid1\leq i\leq n\}$ and $\{y_j\mid1\leq j\leq m\}$, respectively.
 The \defn{symmetric algebra} of $V$ and the \defn{exterior algebra} of $W$ are
 \begin{equation}\label{eq:polynomial-exterior}
 \begin{aligned}
-\Symm(V)&=T_\Bbbk(V)/(x_ix_j-x_jx_i\mid i<j)
+\Symm(V)&=T_\Bbbk(V)/(x_ix_j-x_jx_i\mid1\leq i<j\leq n)
             \cong\Bbbk[x_1,\ldots,x_n],\\
 \bigwedge W&=T_\Bbbk(W)/(w^2\mid w\in W).
 \end{aligned}
 \end{equation}
-\comm{write symbollically, use less words!!!!!!!}Both algebras have degree $0$ component $\Bbbk$ and are generated in degree $1$, with degree $1$ components $V$ and $W$, respectively.
-The polynomial basis allows repetitions; the exterior basis consists of $1$ and $y_{j_1}\cdots y_{j_d}$ with $j_1<\cdots<j_d$.
-The exterior relations are equivalently $y_j^2=0$ for $1\leq j\leq m$ and $y_iy_j+y_jy_i=0$ for $i<j$, in every characteristic.
+They are generated in degree $1$, with
+\[
+\Symm(V)_0=(\bigwedge W)_0=\Bbbk,\qquad
+\Symm(V)_1=V,\qquad(\bigwedge W)_1=W.
+\]
+Their respective bases are
+\[
+\begin{gathered}
+\{x_1^{a_1}\cdots x_n^{a_n}\mid a_1,\ldots,a_n\in\Z,\ a_1,\ldots,a_n\geq0\},\\
+\{y_{j_1}\cdots y_{j_d}\mid0\leq d\leq m,\ 1\leq j_1<\cdots<j_d\leq m\},
+\end{gathered}
+\]
+where the empty product is $1$.
+The exterior relations are equivalently $y_j^2=0$ for $1\leq j\leq m$ and $y_iy_j+y_jy_i=0$ for $1\leq i<j\leq m$, in every characteristic.
 \end{example}
 
-\comm{this para. is supplementary}
+\begin{supplementary}
 The bases in Example~\ref{ex:polynomial-exterior} can be checked directly.
 For $\Symm(V)$, commuting adjacent generators gives the ordered monomials, which are independent under the map to the polynomial ring.
-For $\bigwedge W$, the relations reduce every word to a multiple of a strictly increasing word or to zero.
-To prove independence in degree $d$, fix $j_1<\cdots<j_d$ and use the linear functional $W^{\otimes_\Bbbk d}\to\Bbbk$ sending $w_1\otimes\cdots\otimes w_d$ to the determinant of their coordinates in rows $j_1,\ldots,j_d$ relative to the basis $y_1,\ldots,y_m$.
-The determinant vanishes on tensors with two equal adjacent factors, hence on the degree $d$ part of $(w^2\mid w\in W)$. On increasing basis words it is $1$ on $y_{j_1}\cdots y_{j_d}$ and $0$ on the others, proving independence in every characteristic.
+For $\bigwedge W$, the relations reduce every product of basis elements to a multiple of a strictly increasing product or to zero.
+For $1\leq d\leq m$, fix $j_1<\cdots<j_d$ and consider the linear functional $W^{\otimes_\Bbbk d}\to\Bbbk$ sending $w_1\otimes\cdots\otimes w_d$ to the determinant of their coordinates in rows $j_1,\ldots,j_d$ relative to the basis $\{y_j\mid1\leq j\leq m\}$.
+The determinant vanishes whenever two adjacent factors agree, hence on the degree $d$ component of $(w^2\mid w\in W)$.
+On increasing products it is $1$ on $y_{j_1}\cdots y_{j_d}$ and $0$ on the others, proving independence in every characteristic.
+\end{supplementary}
 
-
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

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
\comm{write symbollically, use less words!!!!!!!}Both algebras have degree $0$ component $\Bbbk$ and are generated in degree $1$, with degree $1$ components $V$ and $W$, respectively.
The polynomial basis allows repetitions; the exterior basis consists of $1$ and $y_{j_1}\cdots y_{j_d}$ with $j_1<\cdots<j_d$.
The exterior relations are equivalently $y_j^2=0$ for $1\leq j\leq m$ and $y_iy_j+y_jy_i=0$ for $i<j$, in every characteristic.
\end{example}

\comm{this para. is supplementary}
The bases in Example~\ref{ex:polynomial-exterior} can be checked directly.
For $\Symm(V)$, commuting adjacent generators gives the ordered monomials, which are independent under the map to the polynomial ring.
For $\bigwedge W$, the relations reduce every word to a multiple of a strictly increasing word or to zero.
To prove independence in degree $d$, fix $j_1<\cdots<j_d$ and use the linear functional $W^{\otimes_\Bbbk d}\to\Bbbk$ sending $w_1\otimes\cdots\otimes w_d$ to the determinant of their coordinates in rows $j_1,\ldots,j_d$ relative to the basis $y_1,\ldots,y_m$.
The determinant vanishes on tensors with two equal adjacent factors, hence on the degree $d$ part of $(w^2\mid w\in W)$. On increasing basis words it is $1$ on $y_{j_1}\cdots y_{j_d}$ and $0$ on the others, proving independence in every characteristic.


```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{example}[Polynomial and exterior algebras]\label{ex:polynomial-exterior}
Let $V,W$ be finite-dimensional vector spaces with bases $\{x_i\mid1\leq i\leq n\}$ and $\{y_j\mid1\leq j\leq m\}$, respectively.
The \defn{symmetric algebra} of $V$ and the \defn{exterior algebra} of $W$ are
\begin{equation}\label{eq:polynomial-exterior}
\begin{aligned}
\Symm(V)&=T_\Bbbk(V)/(x_ix_j-x_jx_i\mid1\leq i<j\leq n)
            \cong\Bbbk[x_1,\ldots,x_n],\\
\bigwedge W&=T_\Bbbk(W)/(w^2\mid w\in W).
\end{aligned}
\end{equation}
They are generated in degree $1$, with
\[
\Symm(V)_0=(\bigwedge W)_0=\Bbbk,\qquad
\Symm(V)_1=V,\qquad(\bigwedge W)_1=W.
\]
Their respective bases are
\[
\begin{gathered}
\{x_1^{a_1}\cdots x_n^{a_n}\mid a_1,\ldots,a_n\in\Z,\ a_1,\ldots,a_n\geq0\},\\
\{y_{j_1}\cdots y_{j_d}\mid0\leq d\leq m,\ 1\leq j_1<\cdots<j_d\leq m\},
\end{gathered}
\]
where the empty product is $1$.
The exterior relations are equivalently $y_j^2=0$ for $1\leq j\leq m$ and $y_iy_j+y_jy_i=0$ for $1\leq i<j\leq m$, in every characteristic.
\end{example}

\begin{supplementary}
The bases in Example~\ref{ex:polynomial-exterior} can be checked directly.
For $\Symm(V)$, commuting adjacent generators gives the ordered monomials, which are independent under the map to the polynomial ring.
For $\bigwedge W$, the relations reduce every product of basis elements to a multiple of a strictly increasing product or to zero.
For $1\leq d\leq m$, fix $j_1<\cdots<j_d$ and consider the linear functional $W^{\otimes_\Bbbk d}\to\Bbbk$ sending $w_1\otimes\cdots\otimes w_d$ to the determinant of their coordinates in rows $j_1,\ldots,j_d$ relative to the basis $\{y_j\mid1\leq j\leq m\}$.
The determinant vanishes whenever two adjacent factors agree, hence on the degree $d$ component of $(w^2\mid w\in W)$.
On increasing products it is $1$ on $y_{j_1}\cdots y_{j_d}$ and $0$ on the others, proving independence in every characteristic.
\end{supplementary}

```

</details>

---

## Replacement 10: Shorten the idempotent decomposition proof

**Source:** [Lecture 2, line 2080](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2080)  
**Added:** `+14` lines | **Removed:** `-17` lines

Implement the agreed shorter proof: retain the vanishing calculation and the explicit inverse, but leave the routine verification to the reader. Use k consistently and preserve both equation labels.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2080,31 +2157,28 @@
 \begin{lemma}\label{lem:idempotent-tensors}
-Let $S=\bigoplus_{i=1}^r\Bbbk e_i$ with coordinate idempotents and let $V,W$ be $S$-bimodules. There is a bimodule isomorphism
+Let $S=\bigoplus_{i=1}^r\Bbbk e_i$ with coordinate idempotents, and consider bimodules ${}_SV_S$, ${}_SW_S$.
+There is a bimodule isomorphism
 \begin{equation}\label{eq:idempotent-tensor-decomposition}
-V\otimes_S W\cong\bigoplus_{i,j,\ell}e_iVe_j\otimes_\Bbbk e_jWe_\ell.
+V\otimes_S W\cong\bigoplus_{i,j,k=1}^r e_iVe_j\otimes_\Bbbk e_jWe_k.
 \end{equation}
-Consequently, after choosing a basis of each $e_iVe_j$, a basis of $V^{\otimes_S d}$ for $d\geq1$ consists of the words of length $d$ whose adjacent idempotents match.
+Consequently, after choosing a basis of each $e_iVe_j$, a basis of $V^{\otimes_S d}$ for $d\geq1$ consists of products of $d$ chosen basis elements whose adjacent idempotents match.
 \end{lemma}
 
 \begin{proof}
-\comm{proof is unnecessarily long and verbal?? just say routine to check the second (the unlabeled) displayed equation provides the bijection will be enough?  there is nothing difficult in showing the bijection?? (voice your opinion before suggesting edit)}
-The mutually orthogonal idempotents sum to $1$, so
+The orthogonal idempotents sum to $1$, so
 \begin{equation}\label{eq:composable-tensors}
-V=\bigoplus_{i,j}e_iVe_j,\qquad
-(e_iVe_j)\otimes_S(e_pWe_\ell)=0
-\quad\text{if }j\neq p.
+V=\bigoplus_{i,j=1}^r e_iVe_j,\qquad
+(e_iVe_j)\otimes_S(e_pWe_k)=0
+\quad(1\leq i,j,p,k\leq r,\ j\neq p).
 \end{equation}
-For the second identity, $v\otimes w=ve_j\otimes w=v\otimes e_jw=0$.
-The inclusions of the matching components define the map from right to left in \eqref{eq:idempotent-tensor-decomposition}.
+Indeed, $v\otimes_S w=ve_j\otimes_S w=v\otimes_S e_jw=0$ for $v\in e_iVe_j$, $w\in e_pWe_k$, and $j\neq p$.
+The map from right to left in \eqref{eq:idempotent-tensor-decomposition} sends $v\otimes_\Bbbk w$ to $v\otimes_S w$ on each summand.
 Its inverse is
 \[
-V\otimes_S W\longrightarrow
-\bigoplus_{i,j,\ell}e_iVe_j\otimes_\Bbbk e_jWe_\ell,
+V\otimes_S W\longrightarrow\bigoplus_{i,j,k=1}^r e_iVe_j\otimes_\Bbbk e_jWe_k,
 \qquad
-v\otimes_S w\longmapsto\sum_{i,j,\ell}e_ive_j\otimes_\Bbbk e_jwe_\ell.
+v\otimes_S w\longmapsto\sum_{i,j,k=1}^r e_ive_j\otimes_\Bbbk e_jwe_k.
 \]
-For $s=\sum_j s_je_j\in S$, replacing $(v,w)$ by $(vs,w)$ or $(v,sw)$ multiplies the summands with middle index $j$ by the same scalar $s_j$, so the inverse is well-defined.
-One composite sends $v\otimes_S w$ to $\sum_{i,j,\ell}e_ive_j\otimes_S e_jwe_\ell=v\otimes_S w$.
-On $v\otimes_\Bbbk w$ with $v\in e_iVe_j$ and $w\in e_jWe_\ell$, the other composite has only the $(i,j,\ell)$ component, equal to $v\otimes_\Bbbk w$.
-Iterating \eqref{eq:idempotent-tensor-decomposition} and using the basis construction in Definition~\ref{def:vector-tensor} proves the assertion about words.
+Checking that these two assignments induce well-defined, mutually inverse maps is left to the reader.
+Iterating \eqref{eq:idempotent-tensor-decomposition} and using Definition~\ref{def:vector-tensor} gives the stated basis.
 \end{proof}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{lemma}\label{lem:idempotent-tensors}
Let $S=\bigoplus_{i=1}^r\Bbbk e_i$ with coordinate idempotents and let $V,W$ be $S$-bimodules. There is a bimodule isomorphism
\begin{equation}\label{eq:idempotent-tensor-decomposition}
V\otimes_S W\cong\bigoplus_{i,j,\ell}e_iVe_j\otimes_\Bbbk e_jWe_\ell.
\end{equation}
Consequently, after choosing a basis of each $e_iVe_j$, a basis of $V^{\otimes_S d}$ for $d\geq1$ consists of the words of length $d$ whose adjacent idempotents match.
\end{lemma}

\begin{proof}
\comm{proof is unnecessarily long and verbal?? just say routine to check the second (the unlabeled) displayed equation provides the bijection will be enough?  there is nothing difficult in showing the bijection?? (voice your opinion before suggesting edit)}
The mutually orthogonal idempotents sum to $1$, so
\begin{equation}\label{eq:composable-tensors}
V=\bigoplus_{i,j}e_iVe_j,\qquad
(e_iVe_j)\otimes_S(e_pWe_\ell)=0
\quad\text{if }j\neq p.
\end{equation}
For the second identity, $v\otimes w=ve_j\otimes w=v\otimes e_jw=0$.
The inclusions of the matching components define the map from right to left in \eqref{eq:idempotent-tensor-decomposition}.
Its inverse is
\[
V\otimes_S W\longrightarrow
\bigoplus_{i,j,\ell}e_iVe_j\otimes_\Bbbk e_jWe_\ell,
\qquad
v\otimes_S w\longmapsto\sum_{i,j,\ell}e_ive_j\otimes_\Bbbk e_jwe_\ell.
\]
For $s=\sum_j s_je_j\in S$, replacing $(v,w)$ by $(vs,w)$ or $(v,sw)$ multiplies the summands with middle index $j$ by the same scalar $s_j$, so the inverse is well-defined.
One composite sends $v\otimes_S w$ to $\sum_{i,j,\ell}e_ive_j\otimes_S e_jwe_\ell=v\otimes_S w$.
On $v\otimes_\Bbbk w$ with $v\in e_iVe_j$ and $w\in e_jWe_\ell$, the other composite has only the $(i,j,\ell)$ component, equal to $v\otimes_\Bbbk w$.
Iterating \eqref{eq:idempotent-tensor-decomposition} and using the basis construction in Definition~\ref{def:vector-tensor} proves the assertion about words.
\end{proof}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{lemma}\label{lem:idempotent-tensors}
Let $S=\bigoplus_{i=1}^r\Bbbk e_i$ with coordinate idempotents, and consider bimodules ${}_SV_S$, ${}_SW_S$.
There is a bimodule isomorphism
\begin{equation}\label{eq:idempotent-tensor-decomposition}
V\otimes_S W\cong\bigoplus_{i,j,k=1}^r e_iVe_j\otimes_\Bbbk e_jWe_k.
\end{equation}
Consequently, after choosing a basis of each $e_iVe_j$, a basis of $V^{\otimes_S d}$ for $d\geq1$ consists of products of $d$ chosen basis elements whose adjacent idempotents match.
\end{lemma}

\begin{proof}
The orthogonal idempotents sum to $1$, so
\begin{equation}\label{eq:composable-tensors}
V=\bigoplus_{i,j=1}^r e_iVe_j,\qquad
(e_iVe_j)\otimes_S(e_pWe_k)=0
\quad(1\leq i,j,p,k\leq r,\ j\neq p).
\end{equation}
Indeed, $v\otimes_S w=ve_j\otimes_S w=v\otimes_S e_jw=0$ for $v\in e_iVe_j$, $w\in e_pWe_k$, and $j\neq p$.
The map from right to left in \eqref{eq:idempotent-tensor-decomposition} sends $v\otimes_\Bbbk w$ to $v\otimes_S w$ on each summand.
Its inverse is
\[
V\otimes_S W\longrightarrow\bigoplus_{i,j,k=1}^r e_iVe_j\otimes_\Bbbk e_jWe_k,
\qquad
v\otimes_S w\longmapsto\sum_{i,j,k=1}^r e_ive_j\otimes_\Bbbk e_jwe_k.
\]
Checking that these two assignments induce well-defined, mutually inverse maps is left to the reader.
Iterating \eqref{eq:idempotent-tensor-decomposition} and using Definition~\ref{def:vector-tensor} gives the stated basis.
\end{proof}

```

</details>

---

## Replacement 11: Remove the unexplained diagonal-subalgebra phrase

**Source:** [Lecture 2, line 2111](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2111)  
**Added:** `+4` lines | **Removed:** `-4` lines

Keep the stated purpose of the example, remove the marked phrase, and identify the algebra isomorphism explicitly without invoking the universal property before it has been stated.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2111,13 +2185,13 @@
 \begin{example}\label{ex:tensor-A3}
-We apply Lemma~\ref{lem:idempotent-tensors} to realise $\Bbbk A_3$ as a tensor algebra \old{over its diagonal subalgebra}\comm{do not use term that you have not introduce!! how many times have I reminded you about this??}.
-Let $S=\Bbbk^{\oplus 3}$ with coordinate idempotents $e_1,e_2,e_3$, and let $V=\Bbbk a\oplus\Bbbk b$ have actions $e_1ae_2=a$ and $e_2be_3=b$, with all other idempotent actions zero.
+We apply Lemma~\ref{lem:idempotent-tensors} to realise $\Bbbk A_3$ as a tensor algebra.
+Let $S=\Bbbk^{\oplus3}$ with coordinate idempotents $e_1,e_2,e_3$, and take the bimodule ${}_SV_S$ with $V=\Bbbk a\oplus\Bbbk b$, $e_1ae_2=a$, and $e_2be_3=b$; all other idempotent actions are zero.
 By Lemma~\ref{lem:idempotent-tensors},
 \[
 V\otimes_S V=\Bbbk(a\otimes b),\qquad
-V^{\otimes_S 3}=0,\qquad
+V^{\otimes_S3}=0,\qquad
 T_S(V)=S\oplus\Bbbk a\oplus\Bbbk b\oplus\Bbbk ab.
 \]
 Here $ab=a\otimes b$.
-The assignments $e_i\mapsto e_{ii}$, $a\mapsto e_{12}$, and $b\mapsto e_{23}$ give $T_S(V)\cong\Bbbk A_3$; the tensor $ab$ maps to $e_{13}$.
+The linear map $T_S(V)\to\Bbbk A_3$ given by $e_i\mapsto e_{ii}$, $a\mapsto e_{12}$, $b\mapsto e_{23}$, and $ab\mapsto e_{13}$ preserves multiplication and sends a basis to a basis, hence is an algebra isomorphism.
 \end{example}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:tensor-A3}
We apply Lemma~\ref{lem:idempotent-tensors} to realise $\Bbbk A_3$ as a tensor algebra \old{over its diagonal subalgebra}\comm{do not use term that you have not introduce!! how many times have I reminded you about this??}.
Let $S=\Bbbk^{\oplus 3}$ with coordinate idempotents $e_1,e_2,e_3$, and let $V=\Bbbk a\oplus\Bbbk b$ have actions $e_1ae_2=a$ and $e_2be_3=b$, with all other idempotent actions zero.
By Lemma~\ref{lem:idempotent-tensors},
\[
V\otimes_S V=\Bbbk(a\otimes b),\qquad
V^{\otimes_S 3}=0,\qquad
T_S(V)=S\oplus\Bbbk a\oplus\Bbbk b\oplus\Bbbk ab.
\]
Here $ab=a\otimes b$.
The assignments $e_i\mapsto e_{ii}$, $a\mapsto e_{12}$, and $b\mapsto e_{23}$ give $T_S(V)\cong\Bbbk A_3$; the tensor $ab$ maps to $e_{13}$.
\end{example}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{example}\label{ex:tensor-A3}
We apply Lemma~\ref{lem:idempotent-tensors} to realise $\Bbbk A_3$ as a tensor algebra.
Let $S=\Bbbk^{\oplus3}$ with coordinate idempotents $e_1,e_2,e_3$, and take the bimodule ${}_SV_S$ with $V=\Bbbk a\oplus\Bbbk b$, $e_1ae_2=a$, and $e_2be_3=b$; all other idempotent actions are zero.
By Lemma~\ref{lem:idempotent-tensors},
\[
V\otimes_S V=\Bbbk(a\otimes b),\qquad
V^{\otimes_S3}=0,\qquad
T_S(V)=S\oplus\Bbbk a\oplus\Bbbk b\oplus\Bbbk ab.
\]
Here $ab=a\otimes b$.
The linear map $T_S(V)\to\Bbbk A_3$ given by $e_i\mapsto e_{ii}$, $a\mapsto e_{12}$, $b\mapsto e_{23}$, and $ab\mapsto e_{13}$ preserves multiplication and sends a basis to a basis, hence is an algebra isomorphism.
\end{example}

```

</details>

---

## Replacement 12: Move the tensor-algebra universal property into advanced material

**Source:** [Lecture 2, line 2124](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2124)  
**Added:** `+24` lines | **Removed:** `-11` lines

Implement the agreed placement: the universal property, its proof, and the grading observation are advanced; the tensor-presentation corollary and multiplication formula remain in the main text. Put the corollary proof in advanced material and specify V, B, varphi, and f explicitly.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2124,7 +2198,7 @@
+\begin{advanced}
 \begin{proposition}[Universal property of the tensor algebra]\label{prop:tensor-universal}
-\comm{advance material this prop?? the only use is to get the next corollay??  (if you disagree, voice your opinion first) we don't have so much time to cover so much details in lectures}
-Let $\iota_S:S\to T_S(V)$ and $\iota_V:V\to T_S(V)$ be the canonical inclusions.
-Given a unital $\Bbbk$-algebra homomorphism $\varphi:S\to B$ and an $S$-bimodule map $f:V\to B$, where $sbt=\varphi(s)b\varphi(t)$ on $B$, there is a unique $\Bbbk$-algebra homomorphism $\widetilde f:T_S(V)\to B$ making the diagram commute:
+Let $S$ be a $\Bbbk$-algebra, consider a bimodule ${}_SV_S$, and let $\iota_S:S\to T_S(V)$ and $\iota_V:V\to T_S(V)$ be the canonical inclusions.
+Given a unital $\Bbbk$-algebra homomorphism $\varphi:S\to B$ and a bimodule map $f:{}_SV_S\to{}_SB_S$, where $sbt=\varphi(s)b\varphi(t)$ on $B$, there is a unique $\Bbbk$-algebra homomorphism $\widetilde f:T_S(V)\to B$ making the diagram commute:
 \begin{equation}\label{eq:tensor-universal}
 \xymatrix@C=42pt@R=28pt{
 V \ar[r]^{\iota_V} \ar[dr]_{f}
@@ -2143,22 +2217,35 @@
 \quad(s\in S,\ i\geq1).
 \end{equation}
 The identity $f(vs)f(w)=f(v)\varphi(s)f(w)=f(v)f(sw)$ shows that replacing adjacent factors $vs\otimes w$ by $v\otimes sw$ does not change the value in \eqref{eq:tensor-extension}.
-Since every element of $T_S(V)$ has finitely many non-zero components, these formulas extend to a linear map $T_S(V)\to B$.
-Concatenation of tensors becomes multiplication in $B$, and the identities $f(sv)=\varphi(s)f(v)$ and $f(vs)=f(v)\varphi(s)$ handle the degree $0$ factors.
-Also, $\widetilde f(1_S)=\varphi(1_S)=1_B$.
+The formulas therefore induce linear maps on the tensor powers, which extend to their direct sum.
+Multiplication is preserved by \eqref{eq:tensor-extension}, including the degree $0$ factors because $f(sv)=\varphi(s)f(v)$ and $f(vs)=f(v)\varphi(s)$.
+Also, $\widetilde f(1_S)=1_B$.
 Every algebra homomorphism making \eqref{eq:tensor-universal} commute must have the values in \eqref{eq:tensor-extension}, proving uniqueness.
 \end{proof}
 
-If $B$ is graded, $\varphi(S)\subset B_0$, and $f(V)\subset B_1$, then \eqref{eq:tensor-extension} gives $\widetilde f(V^{\otimes_S i})\subset B_i$.
+If $B$ is graded, $\varphi(S)\subset B_0$, and $f(V)\subset B_1$, then \eqref{eq:tensor-extension} gives $\widetilde f(V^{\otimes_S i})\subset B_i$ for every $i\geq0$.
 Thus $\widetilde f$ is a graded algebra homomorphism.
+\end{advanced}
 
 \begin{corollary}\label{cor:tensor-presentation}
-If $A$ is generated in degree $1$ over $S=A_0$, there is a surjective graded algebra homomorphism $\mu:T_S(A_1)\onto A$ whose degree $i$ component is $\mu_i$ from \eqref{eq:multiplication-maps}.
+If $A$ is generated in degree $1$ over $S=A_0$, multiplication gives a surjective graded algebra homomorphism
+\[
+\mu:T_S(A_1)\onto A,\qquad
+a_1\otimes_S\cdots\otimes_S a_i\longmapsto a_1\cdots a_i
+\quad(i\geq1),\qquad \mu(s)=s\quad(s\in S).
+\]
+Its degree $i$ component is $\mu_i$ from \eqref{eq:multiplication-maps}.
 \end{corollary}
 
+\begin{advanced}
 \begin{proof}
-\comm{put proof in advanced, if previous prop is put in advanced}
-Apply Proposition~\ref{prop:tensor-universal} to the inclusions $S\to A$ and $A_1\to A$ \comm{specify which map corresp to which in the prop??? now it is just not understandable}.
-Surjectivity of each $\mu_i$ gives surjectivity of $\mu$. 
+In Proposition~\ref{prop:tensor-universal}, take $V=A_1$, $B=A$, and the inclusions
+\[
+\varphi:S\hookrightarrow A,\quad s\longmapsto s,
+\qquad f:A_1\hookrightarrow A,\quad a\longmapsto a.
+\]
+Then \eqref{eq:tensor-extension} gives $\widetilde f=\mu$.
+The map $\mu$ preserves degrees, and each component $\mu_i$ is surjective by the assumption that $A$ is generated in degree $1$.
 \end{proof}
+\end{advanced}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{proposition}[Universal property of the tensor algebra]\label{prop:tensor-universal}
\comm{advance material this prop?? the only use is to get the next corollay??  (if you disagree, voice your opinion first) we don't have so much time to cover so much details in lectures}
Let $\iota_S:S\to T_S(V)$ and $\iota_V:V\to T_S(V)$ be the canonical inclusions.
Given a unital $\Bbbk$-algebra homomorphism $\varphi:S\to B$ and an $S$-bimodule map $f:V\to B$, where $sbt=\varphi(s)b\varphi(t)$ on $B$, there is a unique $\Bbbk$-algebra homomorphism $\widetilde f:T_S(V)\to B$ making the diagram commute:
\begin{equation}\label{eq:tensor-universal}
\xymatrix@C=42pt@R=28pt{
V \ar[r]^{\iota_V} \ar[dr]_{f}
& T_S(V) \ar@{-->}[d]^{\exists!\,\widetilde f}
& S \ar[l]_{\iota_S} \ar[dl]^{\varphi}\\
& B. &
}
\end{equation}
\end{proposition}

\begin{proof}
Define $\widetilde f$ on $S$ and each tensor power by
\begin{equation}\label{eq:tensor-extension}
\widetilde f(s)=\varphi(s),\qquad
\widetilde f(v_1\otimes_S\cdots\otimes_S v_i)=f(v_1)\cdots f(v_i)
\quad(s\in S,\ i\geq1).
\end{equation}
The identity $f(vs)f(w)=f(v)\varphi(s)f(w)=f(v)f(sw)$ shows that replacing adjacent factors $vs\otimes w$ by $v\otimes sw$ does not change the value in \eqref{eq:tensor-extension}.
Since every element of $T_S(V)$ has finitely many non-zero components, these formulas extend to a linear map $T_S(V)\to B$.
Concatenation of tensors becomes multiplication in $B$, and the identities $f(sv)=\varphi(s)f(v)$ and $f(vs)=f(v)\varphi(s)$ handle the degree $0$ factors.
Also, $\widetilde f(1_S)=\varphi(1_S)=1_B$.
Every algebra homomorphism making \eqref{eq:tensor-universal} commute must have the values in \eqref{eq:tensor-extension}, proving uniqueness.
\end{proof}

If $B$ is graded, $\varphi(S)\subset B_0$, and $f(V)\subset B_1$, then \eqref{eq:tensor-extension} gives $\widetilde f(V^{\otimes_S i})\subset B_i$.
Thus $\widetilde f$ is a graded algebra homomorphism.

\begin{corollary}\label{cor:tensor-presentation}
If $A$ is generated in degree $1$ over $S=A_0$, there is a surjective graded algebra homomorphism $\mu:T_S(A_1)\onto A$ whose degree $i$ component is $\mu_i$ from \eqref{eq:multiplication-maps}.
\end{corollary}

\begin{proof}
\comm{put proof in advanced, if previous prop is put in advanced}
Apply Proposition~\ref{prop:tensor-universal} to the inclusions $S\to A$ and $A_1\to A$ \comm{specify which map corresp to which in the prop??? now it is just not understandable}.
Surjectivity of each $\mu_i$ gives surjectivity of $\mu$. 
\end{proof}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{advanced}
\begin{proposition}[Universal property of the tensor algebra]\label{prop:tensor-universal}
Let $S$ be a $\Bbbk$-algebra, consider a bimodule ${}_SV_S$, and let $\iota_S:S\to T_S(V)$ and $\iota_V:V\to T_S(V)$ be the canonical inclusions.
Given a unital $\Bbbk$-algebra homomorphism $\varphi:S\to B$ and a bimodule map $f:{}_SV_S\to{}_SB_S$, where $sbt=\varphi(s)b\varphi(t)$ on $B$, there is a unique $\Bbbk$-algebra homomorphism $\widetilde f:T_S(V)\to B$ making the diagram commute:
\begin{equation}\label{eq:tensor-universal}
\xymatrix@C=42pt@R=28pt{
V \ar[r]^{\iota_V} \ar[dr]_{f}
& T_S(V) \ar@{-->}[d]^{\exists!\,\widetilde f}
& S \ar[l]_{\iota_S} \ar[dl]^{\varphi}\\
& B. &
}
\end{equation}
\end{proposition}

\begin{proof}
Define $\widetilde f$ on $S$ and each tensor power by
\begin{equation}\label{eq:tensor-extension}
\widetilde f(s)=\varphi(s),\qquad
\widetilde f(v_1\otimes_S\cdots\otimes_S v_i)=f(v_1)\cdots f(v_i)
\quad(s\in S,\ i\geq1).
\end{equation}
The identity $f(vs)f(w)=f(v)\varphi(s)f(w)=f(v)f(sw)$ shows that replacing adjacent factors $vs\otimes w$ by $v\otimes sw$ does not change the value in \eqref{eq:tensor-extension}.
The formulas therefore induce linear maps on the tensor powers, which extend to their direct sum.
Multiplication is preserved by \eqref{eq:tensor-extension}, including the degree $0$ factors because $f(sv)=\varphi(s)f(v)$ and $f(vs)=f(v)\varphi(s)$.
Also, $\widetilde f(1_S)=1_B$.
Every algebra homomorphism making \eqref{eq:tensor-universal} commute must have the values in \eqref{eq:tensor-extension}, proving uniqueness.
\end{proof}

If $B$ is graded, $\varphi(S)\subset B_0$, and $f(V)\subset B_1$, then \eqref{eq:tensor-extension} gives $\widetilde f(V^{\otimes_S i})\subset B_i$ for every $i\geq0$.
Thus $\widetilde f$ is a graded algebra homomorphism.
\end{advanced}

\begin{corollary}\label{cor:tensor-presentation}
If $A$ is generated in degree $1$ over $S=A_0$, multiplication gives a surjective graded algebra homomorphism
\[
\mu:T_S(A_1)\onto A,\qquad
a_1\otimes_S\cdots\otimes_S a_i\longmapsto a_1\cdots a_i
\quad(i\geq1),\qquad \mu(s)=s\quad(s\in S).
\]
Its degree $i$ component is $\mu_i$ from \eqref{eq:multiplication-maps}.
\end{corollary}

\begin{advanced}
\begin{proof}
In Proposition~\ref{prop:tensor-universal}, take $V=A_1$, $B=A$, and the inclusions
\[
\varphi:S\hookrightarrow A,\quad s\longmapsto s,
\qquad f:A_1\hookrightarrow A,\quad a\longmapsto a.
\]
Then \eqref{eq:tensor-extension} gives $\widetilde f=\mu$.
The map $\mu$ preserves degrees, and each component $\mu_i$ is surjective by the assumption that $A$ is generated in degree $1$.
\end{proof}
\end{advanced}

```

</details>

---

## Replacement 13: Keep the tensor-duality exercise self-contained

**Source:** [Lecture 2, line 2562](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2562)  
**Added:** `+2` lines | **Removed:** `-1` lines

After generalising the proposition, state the exercise's semisimple assumptions explicitly instead of referring to S,V,W as though they were still the proposition's parameters. Retain all exercise parts, the labelled hint, and the existing hidden solution.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2562,2 +2649,3 @@
 \begin{exercise}[Interaction of tensor product with $S$-dual]\label{ex:tensor-duality-proof}
-For $S,V,W$ as in Proposition~\ref{prop:tensor-duals}, prove the assertion about right $S$-duals.
+Let $S$ be finite-dimensional semisimple, and consider finite-dimensional bimodules ${}_SV_S$, ${}_SW_S$.
+Prove the right $S$-dual isomorphism \eqref{eq:tensor-duals}, the semisimple case of Proposition~\ref{prop:tensor-duals}.
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
\begin{exercise}[Interaction of tensor product with $S$-dual]\label{ex:tensor-duality-proof}
For $S,V,W$ as in Proposition~\ref{prop:tensor-duals}, prove the assertion about right $S$-duals.
```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
\begin{exercise}[Interaction of tensor product with $S$-dual]\label{ex:tensor-duality-proof}
Let $S$ be finite-dimensional semisimple, and consider finite-dimensional bimodules ${}_SV_S$, ${}_SW_S$.
Prove the right $S$-dual isomorphism \eqref{eq:tensor-duals}, the semisimple case of Proposition~\ref{prop:tensor-duals}.
```

</details>

---

## Replacement 14: Retain a hidden proof of the general tensor-dual statement

**Source:** [Lecture 2, line 2629](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2629)  
**Added:** `+36` lines | **Removed:** `-0` lines

Append the general proof inside the existing hidden environment, without altering the existing semisimple solution or exposing a solution in the main or supplementary text. The proof uses only the direct-summand condition, the finite Hom formula, and the tensor-product properties already introduced. The hidden-content switch is not changed.

### Line-by-Line Diff

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2629,4 +2717,40 @@
 For $\theta_\ell$, the corresponding two routes give $f(p(v)g(q(w)))$.
+\end{proof}
+
+\begin{proof}[Proof of Proposition~\ref{prop:tensor-duals} over arbitrary algebras]
+For the right duals, the identities
+\[
+g(f(mb)n)=g(f(m)bn),\qquad
+(gb)(f(m)n)=g(bf(m)n)=g((bf)(m)n)
+\quad(b\in B)
+\]
+make $\theta_r$ in \eqref{eq:general-tensor-duals} well-defined.
+Right $C$-linearity follows from $g(f(m)nc)=g(f(m)n)c$.
+The outer actions satisfy
+\[
+\theta_r(cg\otimes fa)(m\otimes n)=c\,g(f(am)n)
+\quad(c\in C,\ a\in A),
+\]
+so $\theta_r$ is a bimodule map.
+Substitution in \eqref{eq:general-tensor-duals} shows that $\theta_r$ commutes with precomposition in $M$ and $N$.
+
+For bijectivity, forget the left $A$-action on $M$.
+When $M=B$, the identifications $M^*\cong B$, $f\mapsto f(1)$, and $B\otimes_B N\cong N$ identify $\theta_r$ with $N^*\otimes_B B\to N^*$, $g\otimes b\mapsto gb$.
+This is an isomorphism by Lemma~\ref{lem:tensor-properties}(3).
+The direct-sum formulas of Lemma~\ref{lem:tensor-properties}(4) and \eqref{eq:hom-finite-sums} give bijectivity for $M=B^{\oplus r}$.
+If $M\oplus M'\cong B^{\oplus r}$ as right modules, naturality identifies that comparison with the direct sum of the comparisons for $M$ and $M'$; both summand maps are therefore bijective.
+
+For the left duals, the identities are
+\[
+f(mb\,g(n))=f(mg(bn)),\qquad
+f(m(gb)(n))=f(mg(n)b)=(bf)(mg(n)).
+\]
+Left $A$-linearity of $f$ gives left $A$-linearity of the resulting functional, and
+$\theta_\ell(cg\otimes fa)(m\otimes n)=f(mg(nc))a$ gives the outer actions.
+For bijectivity, forget the right $C$-action on $N$.
+When $N=B$, identify $ {}^*N\cong B$ by $g\mapsto g(1)$; then $\theta_\ell$ is $B\otimes_B{}^*M\to{}^*M$, $b\otimes f\mapsto bf$.
+Finite direct sums and direct summands on the left give (2) by the same argument.
+Naturality again follows by substitution in \eqref{eq:general-tensor-duals}.
 \end{proof}
 \end{hidden}
 
```

<details>
<summary><strong>Existing Content (Full, Exact Passage)</strong></summary>

```tex
For $\theta_\ell$, the corresponding two routes give $f(p(v)g(q(w)))$.
\end{proof}
\end{hidden}

```

</details>

<details>
<summary><strong>Proposed Replacement (Full, Exact Passage)</strong></summary>

```tex
For $\theta_\ell$, the corresponding two routes give $f(p(v)g(q(w)))$.
\end{proof}

\begin{proof}[Proof of Proposition~\ref{prop:tensor-duals} over arbitrary algebras]
For the right duals, the identities
\[
g(f(mb)n)=g(f(m)bn),\qquad
(gb)(f(m)n)=g(bf(m)n)=g((bf)(m)n)
\quad(b\in B)
\]
make $\theta_r$ in \eqref{eq:general-tensor-duals} well-defined.
Right $C$-linearity follows from $g(f(m)nc)=g(f(m)n)c$.
The outer actions satisfy
\[
\theta_r(cg\otimes fa)(m\otimes n)=c\,g(f(am)n)
\quad(c\in C,\ a\in A),
\]
so $\theta_r$ is a bimodule map.
Substitution in \eqref{eq:general-tensor-duals} shows that $\theta_r$ commutes with precomposition in $M$ and $N$.

For bijectivity, forget the left $A$-action on $M$.
When $M=B$, the identifications $M^*\cong B$, $f\mapsto f(1)$, and $B\otimes_B N\cong N$ identify $\theta_r$ with $N^*\otimes_B B\to N^*$, $g\otimes b\mapsto gb$.
This is an isomorphism by Lemma~\ref{lem:tensor-properties}(3).
The direct-sum formulas of Lemma~\ref{lem:tensor-properties}(4) and \eqref{eq:hom-finite-sums} give bijectivity for $M=B^{\oplus r}$.
If $M\oplus M'\cong B^{\oplus r}$ as right modules, naturality identifies that comparison with the direct sum of the comparisons for $M$ and $M'$; both summand maps are therefore bijective.

For the left duals, the identities are
\[
f(mb\,g(n))=f(mg(bn)),\qquad
f(m(gb)(n))=f(mg(n)b)=(bf)(mg(n)).
\]
Left $A$-linearity of $f$ gives left $A$-linearity of the resulting functional, and
$\theta_\ell(cg\otimes fa)(m\otimes n)=f(mg(nc))a$ gives the outer actions.
For bijectivity, forget the right $C$-action on $N$.
When $N=B$, identify $ {}^*N\cong B$ by $g\mapsto g(1)$; then $\theta_\ell$ is $B\otimes_B{}^*M\to{}^*M$, $b\otimes f\mapsto bf$.
Finite direct sums and direct summands on the left give (2) by the same argument.
Naturality again follows by substitution in \eqref{eq:general-tensor-duals}.
\end{proof}
\end{hidden}

```

</details>

---

## Source Snapshot

Source SHA-256: `98dc195c3df165b22478db25d21f939954d084cc36b435a9757323e077e6d0c5`.

Before applying, compare each existing passage with the then-current source again; preserve any intervening user edits.

