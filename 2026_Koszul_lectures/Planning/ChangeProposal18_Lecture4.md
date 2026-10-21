# Change Proposal 18: Lecture 4

> **Status: approved and applied on 21 October 2026, with one modification: the exercise is in the main text, not in `advanced`, because Homework 1 now uses part of it. The `hidden` solution was kept. The mother file compiled without errors and without undefined references.**

**Prepared:** 21 October 2026, against the current saved [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex).

## Scope

Address the **2 active `\comm` comments** in Lecture 4 (lines 533 and 717). Lectures 1--3 and 5, the homework, the preamble, the hidden-content setting, and commented-out material are unchanged.

## Reading the Proposal

In each diff, **`-` removes a line**, **`+` adds a line**, and an unmarked line is retained context. Source locations refer to the saved file before changes.

## Contents

| Replacement | Change |
|---|---|
| [1](#replacement-1) | Turn the $\Bbbk[x]$ example into an exercise |
| [2](#replacement-2) | Relate right noetherian to the ACC |
| [Checks](#checks) | Comment coverage and open questions |

---

<a id="replacement-1"></a>
## Replacement 1: Turn the $\Bbbk[x]$ example into an exercise

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:533), lines 533--550. **Changes:** +23 / -18 lines.

Comment: "turn this to an exercise".
**As approved:** the exercise is in the main text, **not** inside `advanced`, because Homework 1 uses part of it. It is preceded by a sentence stating which results it tests (Lemma `lem:graded-radical` and existence of projective covers).
The question and hint are separate, the hint is labelled and given only for the harder part (2), and the former argument is kept as the solution in a `hidden` block (not deleted).
The label `ex:graded-radical-infinite` is not referenced anywhere, so its removal breaks nothing.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -533,18 +533,23 @@
-\begin{advanced}\comm{turn this to an exercise}
-\begin{example}\label{ex:graded-radical-infinite}
-The equality $A_+=\rad A$ can fail when $A$ is infinite-dimensional.
-Take $A=\Bbbk[x]$ with $\deg x=1$.
-Then $A_+=(x)$, whereas $\rad A=0$.
-Indeed, if $0\neq f\in\rad A$, then $xf\in\rad A$, and the first paragraph of the proof of Lemma~\ref{lem:nakayama} gives a right inverse to $1-xf$.
-This is impossible because $1-xf$ has positive degree.
-In particular, $A/\rad A=A$, whereas $\grtop A=\Bbbk$.
-
-Over this algebra, even the ordinary module $\Bbbk=A/(x)$ has no projective cover.
-Suppose $p:P\to\Bbbk$ were one, and choose $u\in P$ with $p(u)=1$.
-Then $p(uA)=\Bbbk$, so $P=uA$.
-The surjection $A\to P$, $a\mapsto ua$, splits because $P$ is projective.
-The resulting projection $A\to A$ is multiplication by an idempotent $e\neq0$, and $P\cong eA$.
-Since $\Bbbk[x]$ has no idempotents other than $0$ and $1$, we have $P\cong A$.
-But every surjection $A\to\Bbbk$ maps the proper submodule $(x-1)A$ onto $\Bbbk$, contradicting the cover property.
-\end{example}
-\end{advanced}
+The following exercise shows that Lemma~\ref{lem:graded-radical} fails for infinite-dimensional $A$, and that projective covers need not exist over such $A$.
+
+\begin{exercise}
+Let $A=\Bbbk[x]$ with $\deg x=1$.
+\begin{enumerate}
+\item Prove that $\rad A=0$ whereas $A_+=(x)$.
+In particular, $A/\rad A=A$, whereas $\grtop A=\Bbbk$.
+\item Prove that the ordinary module $\Bbbk=A/(x)$ has no projective cover.
+\end{enumerate}
+\emph{Hint for (2).} Show that a projective cover would be isomorphic to $A$, and find a proper submodule of $A$ mapping onto $\Bbbk$.
+\end{exercise}
+
+\begin{hidden}
+\emph{Solution.}
+(1) If $0\neq f\in\rad A$, then $xf\in\rad A$, so $1-xf$ has a right inverse.
+This is impossible because $1-xf$ has positive degree.
+(2) Suppose $p:P\to\Bbbk$ is a projective cover, and choose $u\in P$ with $p(u)=1$.
+Then $p(uA)=\Bbbk$, so $P=uA$.
+The surjection $A\to P$, $a\mapsto ua$, splits because $P$ is projective.
+The resulting projection $A\to A$ is multiplication by an idempotent $e\neq0$, and $P\cong eA$.
+Since $\Bbbk[x]$ has no idempotents other than $0$ and $1$, we have $P\cong A$.
+But every surjection $A\to\Bbbk$ maps the proper submodule $(x-1)A$ onto $\Bbbk$, contradicting the cover property.
+\end{hidden}
```

<details>
<summary><strong>Existing content: exact passage replaced</strong></summary>

```tex
\begin{advanced}\comm{turn this to an exercise}
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

<details>
<summary><strong>Applied replacement: exact TeX</strong></summary>

```tex
The following exercise shows that Lemma~\ref{lem:graded-radical} fails for infinite-dimensional $A$, and that projective covers need not exist over such $A$.

\begin{exercise}
Let $A=\Bbbk[x]$ with $\deg x=1$.
\begin{enumerate}
\item Prove that $\rad A=0$ whereas $A_+=(x)$.
In particular, $A/\rad A=A$, whereas $\grtop A=\Bbbk$.
\item Prove that the ordinary module $\Bbbk=A/(x)$ has no projective cover.
\end{enumerate}
\emph{Hint for (2).} Show that a projective cover would be isomorphic to $A$, and find a proper submodule of $A$ mapping onto $\Bbbk$.
\end{exercise}

\begin{hidden}
\emph{Solution.}
(1) If $0\neq f\in\rad A$, then $xf\in\rad A$, so $1-xf$ has a right inverse.
This is impossible because $1-xf$ has positive degree.
(2) Suppose $p:P\to\Bbbk$ is a projective cover, and choose $u\in P$ with $p(u)=1$.
Then $p(uA)=\Bbbk$, so $P=uA$.
The surjection $A\to P$, $a\mapsto ua$, splits because $P$ is projective.
The resulting projection $A\to A$ is multiplication by an idempotent $e\neq0$, and $P\cong eA$.
Since $\Bbbk[x]$ has no idempotents other than $0$ and $1$, we have $P\cong A$.
But every surjection $A\to\Bbbk$ maps the proper submodule $(x-1)A$ onto $\Bbbk$, contradicting the cover property.
\end{hidden}
```

</details>

---

<a id="replacement-2"></a>
## Replacement 2: Relate right noetherian to the ACC

**Source:** [Lecture_Koszul_S4.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul_S4.tex:717), line 717. **Changes:** +18 / -1 lines (the comment line).

Comment: "add remark about relation to noetherian (ACC) ring?" This asks for an opinion; my recommendation is **yes**, for two reasons.
Students will know noetherian rings through the ACC, so the module-theoretic definition in Definition (`def:noetherian-algebra`) should be linked to it before it is used in Corollary (`cor:noetherian-minimal-resolution`).
The remark also records that the hypothesis is not automatic, which is why that corollary is stated with it.
The equivalence is only stated in the main text; its proof is supplementary and is not used later.

```diff
--- a/Lecture_Koszul_S4.tex
+++ b/Lecture_Koszul_S4.tex
@@ -712,6 +712,23 @@
 \begin{definition}\label{def:noetherian-algebra}
 An algebra $A$ is \defn{right noetherian} if every submodule of every finitely generated right $A$-module is finitely generated.
 It is \defn{left noetherian} if the same condition holds for left $A$-modules.
 It is \defn{noetherian} if it is both right and left noetherian.
 \end{definition}
-\comm{add remark about relation to noetherian (ACC) ring?}
+\begin{remark}\label{rem:noetherian-acc}
+$A$ is right noetherian if and only if every ascending chain $I_1\subseteq I_2\subseteq\cdots$ of right ideals of $A$ stabilises, that is, if $A$ satisfies the \defn{ascending chain condition} (ACC) on right ideals; the analogous statement holds on the left.
+Finite-dimensional algebras and $\Bbbk[x_1,\ldots,x_m]$ are noetherian, whereas the free algebra $\Bbbk\langle x,y\rangle$ is not.
+Thus the hypothesis of Corollary~\ref{cor:noetherian-minimal-resolution} is not automatic.
+\end{remark}
+
+\begin{supplementary}
+Suppose that every submodule of a finitely generated module is finitely generated.
+Then the union of a chain $I_1\subseteq I_2\subseteq\cdots$ of right ideals is a finitely generated right ideal, and its generators lie in some $I_k$; so the chain stabilises at $I_k$.
+
+Conversely, assume the ACC.
+Every right ideal $I$ is finitely generated: otherwise choose inductively $u_{k+1}\in I\setminus(u_1A+\cdots+u_kA)$, which gives a strictly ascending chain.
+We show by induction on $m$ that every submodule $U\subseteq A^{\oplus m}$ is finitely generated; the case $m=1$ was just proved.
+For $m>1$, let $\pi:A^{\oplus m}\to A$ be the projection onto the last coordinate.
+Then $U\cap\Ker\pi$ is a submodule of $A^{\oplus(m-1)}$ and $\pi(U)$ is a right ideal, so both are finitely generated.
+Generators of $U\cap\Ker\pi$ together with lifts to $U$ of generators of $\pi(U)$ generate $U$.
+Finally, a finitely generated module is a quotient $A^{\oplus m}/K$, and each submodule of it has the form $U/K$ with $K\subseteq U\subseteq A^{\oplus m}$, hence is finitely generated.
+\end{supplementary}
```

<details>
<summary><strong>Existing content: exact passage to replace</strong></summary>

```tex
\begin{definition}\label{def:noetherian-algebra}
An algebra $A$ is \defn{right noetherian} if every submodule of every finitely generated right $A$-module is finitely generated.
It is \defn{left noetherian} if the same condition holds for left $A$-modules.
It is \defn{noetherian} if it is both right and left noetherian.
\end{definition}
\comm{add remark about relation to noetherian (ACC) ring?}
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
\begin{remark}\label{rem:noetherian-acc}
$A$ is right noetherian if and only if every ascending chain $I_1\subseteq I_2\subseteq\cdots$ of right ideals of $A$ stabilises, that is, if $A$ satisfies the \defn{ascending chain condition} (ACC) on right ideals; the analogous statement holds on the left.
Finite-dimensional algebras and $\Bbbk[x_1,\ldots,x_m]$ are noetherian, whereas the free algebra $\Bbbk\langle x,y\rangle$ is not.
Thus the hypothesis of Corollary~\ref{cor:noetherian-minimal-resolution} is not automatic.
\end{remark}

\begin{supplementary}
Suppose that every submodule of a finitely generated module is finitely generated.
Then the union of a chain $I_1\subseteq I_2\subseteq\cdots$ of right ideals is a finitely generated right ideal, and its generators lie in some $I_k$; so the chain stabilises at $I_k$.

Conversely, assume the ACC.
Every right ideal $I$ is finitely generated: otherwise choose inductively $u_{k+1}\in I\setminus(u_1A+\cdots+u_kA)$, which gives a strictly ascending chain.
We show by induction on $m$ that every submodule $U\subseteq A^{\oplus m}$ is finitely generated; the case $m=1$ was just proved.
For $m>1$, let $\pi:A^{\oplus m}\to A$ be the projection onto the last coordinate.
Then $U\cap\Ker\pi$ is a submodule of $A^{\oplus(m-1)}$ and $\pi(U)$ is a right ideal, so both are finitely generated.
Generators of $U\cap\Ker\pi$ together with lifts to $U$ of generators of $\pi(U)$ generate $U$.
Finally, a finitely generated module is a quotient $A^{\oplus m}/K$, and each submodule of it has the form $U/K$ with $K\subseteq U\subseteq A^{\oplus m}$, hence is finitely generated.
\end{supplementary}
```

</details>

---

## Checks

### Comment Coverage

| Original comment | Proposed response |
|---|---|
| 533: turn this to an exercise | Replacement 1 |
| 717: add remark about relation to noetherian (ACC) ring? | Replacement 2 (added as proposed, on your instruction) |

### Mathematical Dependencies

- The exercise uses only that $\rad A$ makes $1-a$ right invertible, and the characterisations of projectives from Proposition (`prop:projective-characterisations`); no supplementary material is needed in the main route.
- The ACC remark is not used elsewhere. The ``free algebra $\Bbbk\langle x,y\rangle$ is not noetherian'' statement is a standard fact quoted without proof.

### Open Questions for You

1. Exercise placement: resolved by you — main text, not `advanced`.
2. Solution: kept in a `hidden` block, as proposed.

### Verification Status

Applied to Lecture 4 only; `Lecture_Koszul.pdf` was rebuilt with the existing hidden-content setting. No document or preview was opened in the side panel.
