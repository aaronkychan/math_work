# Change Proposal 19: Lectures 4, 5, and 6

> **Status: applied on 23 October 2026, on your instruction. The mother file compiled without errors and without undefined references. Nothing was opened in the side panel.**

**Prepared:** 23 October 2026, against the saved sources of that day.

## Scope

1. Lecture 4: the one active `\comm` comment, and the notation it asks for.
2. A new Lecture 5, **Ext and Tor**, inserted before the Koszul complex.
3. The former Lecture 5 (Koszul complex and Koszul algebras) becomes **Lecture 6**; its content is unchanged except for notation.
4. Short exercises for Lectures 4, 5, and 6.

Lectures 1--3, the homework, the hidden-content setting, and commented-out material are unchanged.

## Contents

| Item | Change |
|---|---|
| [1](#item-1) | Notation decision and the Lecture 4 comment |
| [2](#item-2) | Mechanical notation changes in Lectures 4 and 6 |
| [3](#item-3) | New Lecture 5: Ext and Tor |
| [4](#item-4) | File moves and mother-file changes |
| [5](#item-5) | Exercises |
| [Flow check](#flow-check) | Whether Lectures 4, 5, 6 follow naturally |
| [Open suggestions](#open-suggestions) | Not applied |
| [Verification](#verification) | What was checked |

---

<a id="item-1"></a>
## 1. Notation decision and the Lecture 4 comment

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:618), line 618. **Changes:** +4 / -4 lines (the line numbers are unchanged).

The comment asked for another letter for the homological degree, so that it is not confused with the differential $d$, and said it prefers $h,k$ for homological degree and $i,j$ for internal (Adams) grading.
Because $i,j$ were already used for idempotents and simples, I asked, and you decided:

> From Lecture 4 onwards: **$h,k$ homological degree, $i,j$ internal degree, $x,y$ for simple (idempotent) indexing.**

Lectures 1--3 are final and keep $d$ for degrees and $i,j$ for idempotents and simples.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -618,4 +618,4 @@
-The homological degree $i$ and the grading degree $d$\comm{use another letter to not confuse with the differential.  I prefer using $h,k$ for homological degree and $i,j$ for internal/Adams grading} are distinct:
-\[
-d_i:(P_i)_d\longrightarrow(P_{i-1})_d.
-\]
+The homological degree $h$ and the grading degree $i$ are distinct:
+\[
+d_h:(P_h)_i\longrightarrow(P_{h-1})_i.
+\]
```

---

<a id="item-2"></a>
## 2. Mechanical notation changes

Substitutions, applied in this order from the subsection "Complexes and resolutions" of Lecture 4 onwards, and in the whole of the former Lecture 5:

| Step | Substitution | Examples |
|---|---|---|
| 1 | Homological index $i\to h$ | $P_i,\ d_i,\ C_i,\ H_i,\ K_i,\ p_i,\ f_i,\ \bigwedge^iV$ |
| 2 | Internal degree $d\to i$ (not in $d_h$, $d'_h$, or arrow labels) | $A_d,\ M_d,\ A(-d),\ s_d$, $(\operatorname{top}_{\mathrm{gr}}M)_d$ |
| 3 | Degree bound $q\to j$ in the cover proof | $P_q\to P_j$ |
| 4 | Simple index $j\to y$ in the graded Betti remark | $L_j,\ \beta_{i,d,j}\to L_y,\ \beta_{h,i,y}$ |
| 5 | Koszul homotopy $h_{\alpha,i}\to s_{\alpha,h}$ | avoids a clash with $h$ |
| 6 | Graded free module: $\bigoplus_{i\in I}A(-d_i)$ $\to$ $\bigoplus_{\lambda\in I}A(-i_\lambda)$ | index set element $\lambda$ |

Index sets (such as $i\in I$ before the subsection "Complexes and resolutions"), variable positions $j_r$ in the Koszul proof, and indices in the commented draft notes were left unchanged.

**Affected lines in Lecture 4** (original numbering, 57 lines): 320--322, 324--325, 327, 331--332, 342, 344, 347--348, 370--371, 377, 390, 392, 397, 400, 404, 420, 424, 459--460, 464, 468--469, 480, 494, 514, 558--559, 587, 589, 593, 596--597, 599, 601, 604, 606, 608, 614--615, 618, 620, 625, 640, 642, 684, 686--688, 696, 698, 700, 702.

**Affected lines in the former Lecture 5, now Lecture 6** (original numbering, 36 lines): 10, 12, 16, 19, 22--23, 25--26, 30, 44--45, 48, 52, 54, 56, 59, 62, 64, 71, 74--77, 80--82, 87--88, 90, 97--99, 107, 115--116, 126.

The symbol list entries for chain complexes, homology, Koszul terms, and the graded Betti numbers were changed to the new letters (see item 4).

---

<a id="item-3"></a>
## 3. New Lecture 5: Ext and Tor

**File:** [Lecture_Koszul_S5.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S5.tex) (new content, about 20 000 characters).

Ext is the focus; Tor is introduced briefly and related to Ext by duality, as requested. Everything uses only $D$ and $\bbD$ and the standing $S=\bigoplus\Bbbk e_y$; two **General $S$** remarks record the changes needed otherwise.

| Subsection | Content | Labels |
|---|---|---|
| Ext via projective resolutions | cochain complexes; $\Ext_A^h(M,N)$ from $\Hom_A(P_\bullet,N)$; comparison lemma (proof supplementary); independence and functoriality; $\Ext^0=\Hom$, vanishing for projectives | `def:cochain-complex`, `def:ext`, `lem:comparison`, `prop:ext-well-defined`, `prop:ext-basic` |
| Graded Ext and minimal resolutions | $\Ext_A^h(M,N)_j=H^h(\Hom_A^\Z(P_\bullet,N(j)))$; relation to ordinary Ext; **differentials vanish for minimal resolutions and $N$ with $NA_+=0$**; multiplicities; examples $\Bbbk A_2$, $\Bbbk[x]$, $\Bbbk[\epsilon]/(\epsilon^2)$ | `def:graded-ext`, `rem:graded-ext-ungraded`, `thm:ext-minimal`, `cor:ext-simple`, `rem:ext-general-S`, `ex:ext-A2`, `ex:ext-polynomial-exterior` |
| Tor | $\Tor_h^A(M,N)=H_h(P_\bullet\otimes_AN)$; $\Tor_h^A(M,S)\cong\operatorname{top}_{\mathrm{gr}}P_h$; duality $\Ext^h(M,\bbD N)_j\cong D(\Tor_h(M,N)_{-j})$ | `def:tor`, `prop:tor-top`, `prop:ext-tor-duality`, `rem:tor-general-S` |
| The beginning of the resolution of $S$ | $P_0=A$; $\operatorname{top}_{\mathrm{gr}}P_1\cong A_+/A_+^2$; for quadratic $A$, $\operatorname{top}_{\mathrm{gr}}P_2\cong R$ (proof supplementary) | `prop:resolution-first-terms` |

The identities that the draft note at the top of Lecture 4 asked for are all contained here: $\Hom_A(P_h,S)=\Hom_S(\operatorname{top}_{\mathrm{gr}}P_h,S)$, $\Ext_A^h(M,S)_j\cong D((\operatorname{top}_{\mathrm{gr}}P_h)_{-j})$, the sign $j=-h$ for a linear resolution, and the remark that higher $\Hom_S(-,S)$ plays no role since $S$ is semisimple.
The Yoneda product is **not** introduced; the last paragraph of the section only compares dimensions with $A^!$ up to degree $2$.

---

<a id="item-4"></a>
## 4. File moves and mother-file changes

| File | Change |
|---|---|
| `Lecture_Koszul_S5.tex` | Replaced by the new Ext and Tor lecture. |
| `Lecture_Koszul_S6.tex` | New file containing the former Lecture 5; the section label `sec:koszul-complex` and all other labels are retained. |
| `Lecture_Koszul.tex` | `\input{Lecture_Koszul_S6.tex}` added; symbol list: the group heading now reads "Tops, resolutions, Ext, Tor, and the Koszul complex", four rows were added ($C^\bullet,\delta^h,H^h$; $\Ext_A^h(M,N)$; $\Ext_A^h(M,N)_j$; $\Tor_h^A(M,N)$), and the rows for $C_\bullet,d_h$; $H_h$; $K_h$; $K_\bullet$; $\beta_{h,i,y}$ and $\beta_{h,i}$ use the new letters. |

---

<a id="item-5"></a>
## 5. Exercises

Each lecture ends with a short "Exercises" subsection in the style of Lectures 1--3; questions and hints are separated and hints are given only where needed.

| Lecture | Exercises |
|---|---|
| 4 | Graded Nakayama fails without boundedness below ($\Bbbk[x,x^{-1}]$); the minimal resolution of $\Bbbk$ over $\Bbbk[u,v]/(uv)$; minimal resolutions of the simple modules over $\Bbbk A_3$ |
| 5 | Ext vanishes for projectives, and a converse; $\Ext^1$ as a cokernel and dimension shifting; $\Ext$ of simples over $\Bbbk A_3/(e_{13})$; $\Tor$ and $\Ext$ for $\Bbbk[x]/(x^m)$; $\Tor_1^A(S,S)\cong A_+/A_+^2$ and generation in degree 1 |
| 6 | $(1-t)^nh_{\Bbbk[x_1,\ldots,x_n]}(t)=1$ from the Koszul complex; the resolution of $S$ for a radical-square-zero algebra; $\Bbbk[x]/(x^3)$ is not Koszul |

---

## Flow check

**Lecture 4 $\to$ 5.** Natural. Lecture 4 ends with existence and uniqueness of minimal graded resolutions and the finite generation of successive kernels; Lecture 5 uses exactly Theorem `thm:minimal-resolution`, the criterion `eq:graded-minimal-criterion`, the graded top, and the examples `ex:minimal-A2`, `ex:minimal-polynomial`, `ex:minimal-exterior`. The notation switch (h, i, y) takes effect at the start of Lecture 4's "Complexes and resolutions", so Lectures 4--6 are consistent.

**Lecture 5 $\to$ 6.** Natural, with one gap: Lecture 6 defines a *linear* resolution and Koszul algebras only through $P_h/P_hA_+$, and does not say that this is $\Tor_h^A(S,S)$ or $\Ext_A^h(S,S)_{-h}$. Lecture 5 already proves the facts needed (Proposition `prop:tor-top`, Theorem `thm:ext-minimal`, Proposition `prop:resolution-first-terms`), so the reformulation can be a short statement in your planned Yoneda section; see the suggestion below.

**Lecture 6 $\to$ Yoneda section.** The first terms of the resolution of $S$ (`prop:resolution-first-terms`) match $A^!$ in degrees $0,1,2$, which is the natural entry point for the identification of $\Ext_A^\bullet(S,S)$ with $A^!$.

---

## Open suggestions

These were **not** applied.

1. After Definition `def:koszul-algebra` in Lecture 6, add a remark: by Proposition `prop:tor-top` and Theorem `thm:ext-minimal`, a quadratic $A$ is Koszul if and only if $\Tor_h^A(S,S)_i=0$ for $i\neq h$, if and only if $\Ext_A^h(S,S)_j=0$ for $j\neq-h$; by Proposition `prop:resolution-first-terms` this holds automatically for $h\leq2$. This is the reformulation from the replan, so you may prefer it in the Yoneda section.
2. The draft note at the top of Lecture 4 (`% TODO (ChangeProposal9, ...)`, lines 5--13) mentions "Lectures 6--7"; its content is now covered by Lecture 5. It was left in place as commented source.
3. The Koszul proof in Lecture 6 uses $x_j$ for polynomial variables and $j_r$ for positions of wedge factors; $x$ and $j$ are also the new letters for simples and internal degree, but they never occur in the same sense in that section, so I did not rename them.
4. The ascending-chain remark in Lecture 4 uses $k$ as a chain index; this is not a homological degree, so it was left as is.

---

## Verification

- The mother file compiled with the existing hidden-content setting; the log has no errors and no undefined references. The built-in compile was not run; the local TeX Live build (`latexmk`) was used. The PDF in the course folder was updated.
- Reflowed two overfull lines in Lecture 5. Four small overfull warnings remain in other lectures and were not introduced here.
- Mathematical checks: every proof in Lecture 5 was re-derived by hand, including the degree bookkeeping $\Ext_A^h(M,N)_j\leftrightarrow(\operatorname{top}_{\mathrm{gr}}P_h)_{-j}$, the graded duality sign, and the claim $\operatorname{top}_{\mathrm{gr}}P_2\cong R$.
- Not checked: how the new pages look. No document or preview was opened in the side panel.
