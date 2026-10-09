# Change Proposal 5: Lecture 1

> **Applied on 9 October 2026.** Both citation changes were approved and applied together with Change Proposal 6. The TeX and the PDF in the course folder have been updated.

**Prepared:** 9 October 2026  
**Source:** [2026_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex)

## Scope

Add the missing reference for the equivalence between separability over the base field and semisimplicity of the enveloping algebra. The citation stays inside the advanced remark; the only other change is its bibliography entry. The earlier Grant-Iyama citation concerns the bimodule convention and does not support this equivalence.

## Verified Reference

**Yu. A. Drozd and V. V. Kirichenko, _Finite Dimensional Algebras_, Springer-Verlag, 1994, Theorem 6.1.2, p. 105.** Conditions (1) and (2) of that theorem are precisely the two conditions in the notes. The chapter uses the same definition of separability by semisimplicity after every field extension. [Author-hosted text](https://imath.kiev.ua/~drozd/drozd-kirichenko_en.pdf), [publisher's bibliographic record](https://link.springer.com/book/10.1007/978-3-642-76244-4).

## Replacement Index

| No. | Change | Line changes |
| --- | --- | --- |
| **1** | [Cite the semisimplicity-separability equivalence](#replacement-1) | `+1` / `-1` |
| **2** | [Add the bibliography entry](#replacement-2) | `+6` / `-0` |

**Review together:** Replacement 1 uses the bibliography entry supplied by Replacement 2.

**Diff legend:** `-` removes a line; `+` adds a line; a leading space retains context. Hunk numbers refer to the current TeX and the proposed version with both changes applied. Both full, exact passages appear below each diff.

## Checks

- [x] The theorem explicitly states the required equivalence.
- [x] Both existing passages match the current TeX uniquely.
- [x] The citation is inside the existing advanced block.
- [x] The new bibliography key `DK94` is not already in use.
- [x] Both changes applied to the existing TeX file.
- [x] Built-in compilation and PDF export succeeded with the existing hidden-content setting.
- [x] The citation and bibliography entry resolve correctly and were visually checked.

---

<a id="replacement-1"></a>

## Replacement 1: Cite the semisimplicity-separability equivalence

**Source:** [line 716](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:716)  
**Purpose:** Add the precise theorem citation inside the existing advanced remark; do not change the mathematical statement.

### Line-by-Line Diff

**Added:** `+1` lines &nbsp; **Removed:** `-1` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -716,4 +716,4 @@
-We record the following fact without proof:
+By \cite[Theorem~6.1.2, p.~105]{DK94},
 \[
 S^\en\text{ is semisimple}
 \quad\Longleftrightarrow\quad
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
We record the following fact without proof:
\[
S^\en\text{ is semisimple}
\quad\Longleftrightarrow\quad
S\text{ is separable over }\Bbbk.
\]
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
By \cite[Theorem~6.1.2, p.~105]{DK94},
\[
S^\en\text{ is semisimple}
\quad\Longleftrightarrow\quad
S\text{ is separable over }\Bbbk.
\]
```

</details>

[Back to the replacement index](#replacement-index)

---

<a id="replacement-2"></a>

## Replacement 2: Add the bibliography entry

**Source:** [line 2726](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/2026_Koszul.tex:2726)  
**Purpose:** Supply the reference used in Replacement 1, with the publisher's DOI.

### Line-by-Line Diff

**Added:** `+6` lines &nbsp; **Removed:** `-0` lines

```diff
--- existing/2026_Koszul.tex
+++ proposed/2026_Koszul.tex
@@ -2726 +2726,7 @@
+\bibitem[DK94]{DK94}
+Yu.~A.~Drozd and V.~V.~Kirichenko,
+\emph{Finite Dimensional Algebras},
+Springer-Verlag, Berlin, 1994,
+\href{https://doi.org/10.1007/978-3-642-76244-4}{doi:10.1007/978-3-642-76244-4}.
+
 \bibitem[DNN17]{DNN17}
```

<details>
<summary><strong>Existing content: full exact TeX</strong></summary>

```tex
\bibitem[DNN17]{DNN17}
```

</details>

<details>
<summary><strong>Proposed replacement: full exact TeX</strong></summary>

```tex
\bibitem[DK94]{DK94}
Yu.~A.~Drozd and V.~V.~Kirichenko,
\emph{Finite Dimensional Algebras},
Springer-Verlag, Berlin, 1994,
\href{https://doi.org/10.1007/978-3-642-76244-4}{doi:10.1007/978-3-642-76244-4}.

\bibitem[DNN17]{DNN17}
```

</details>

[Back to the replacement index](#replacement-index)

---
