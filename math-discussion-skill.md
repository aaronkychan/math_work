---
name: math-discussion
description: Write and revise rigorous mathematical explanations with explicit objects, symbols, quantifiers, domains, codomains, and proof steps. Use for mathematical discussions, proofs, algebra, representation theory, homological algebra, topology, and TeX notes when vague references or omitted intermediate arguments could cause ambiguity.
---

# Specific Mathematical Writing

## Core rule

Make every mathematical reference explicit. Whenever a sentence refers to an object, name that object or write its symbol. Replace vague references such as "this," "that," "the term," "the map," "the component," "the two signs," and "the remaining part" by the relevant symbol and its precise definition.

## State objects before using them

- Define every symbol before its first use.
- State the ambient category, algebra, module convention, and base field when they matter.
- Distinguish objects with similar names by superscripts or subscripts, for example $\Delta^X_Y$ and $\Delta^Y_Z$.
- Distinguish a primitive idempotent $e_Y\in A$ from a chosen basis vector $\varepsilon_{Y,Z}\in(P_Y)_Z$.
- Distinguish a whole map from its component: write $f:M\to N$ and, for a component with source index $X$ and target index $Y$, write $f_{YX}:M_X\to N_Y$ separately.
- Distinguish a chain, a vertex of a chain, a labelled copy of a summand, and the underlying unlabelled object.
- When using an index or indexing set, state the object that it indexes. If an object has decompositions such as $M\cong\bigoplus_{i\in I}M_i\cong\bigoplus_{j\in J}N_j$, identify an index by its decomposition, for example “the index $i$ in the decomposition $M\cong\bigoplus_{i\in I}M_i$,” especially when $I$ and $J$ have similar or related nature.

## State maps completely

Define maps in the compact form
\[
 f:A\rightarrow B,\qquad a\mapsto f(a).
\]
Always give the domain and codomain. For a component with source index $X$
and target index $Y$, write its domain and codomain explicitly, such as
\[
 f_{YX}:M_X\rightarrow N_Y.
\]
If a map is multiplication, state the side and the element:
\[
 \mu_{X,Y}:P_Y\rightarrow P_X,\qquad p\mapsto b_{XY}p.
\]
Do not call a map "induced" without specifying the source map, the target map, and the induced domain and codomain.

## Make proof logic visible

For each implication:

1. State the hypothesis with its symbols.
2. Introduce the exact witness or vertex being considered.
3. Explain why that witness is relevant.
4. Apply the displayed definition or previously proved equality to that witness.
5. State the resulting conclusion with symbols.

Do not replace this sequence by a sentence such as "the usual argument shows" or "the two terms cancel." In a calculation, write the actual terms, their source, their target, and their coefficients. For example, identify the $j$-th summand and the face deleted from it before comparing it with another summand.

For any proof of a statement of the form "The following are equivalent,"
start the proof by stating the proof strategy: list the implications that will
be proved and the order in which they will be proved. Then divide the proof
into visibly labelled sections for each implication, so the reader can
immediately see which implication is being established. At the start of the proof of each implication, state explicit "Now we prove \((1)\Rightarrow(2)\)" when in discussion; use labels such as \(\underline{(1)\Rightarrow(2)}\) when writing up in LaTeX.

## Structure long proofs

When a proof would be too long to follow as one uninterrupted argument,
divide it into multiple visibly labelled steps. Give each step a small,
specific goal. Use “We claim that ...” only when the argument establishing the
intermediate claim can be completed in one paragraph (roughly fewer than five
lines). Treat “one paragraph” as one short paragraph: if the argument uses
several distinct subarguments, multiple displayed calculations, or roughly
five or more rendered lines, state it separately as a visibly labelled
**Lemma** or **Proposition** and then give its proof. When the length is
borderline, prefer **Lemma** or **Proposition**. Do not introduce a
multi-paragraph argument as “We claim that ...”.

For a short intermediate claim, begin the step with the claim itself and
state any immediate consequence in the same sentence. Use the following
pattern:

```text
Step 1 — [specific goal]

We claim that [precise claim]; in particular, [immediate consequence].

Indeed, [explanation with all relevant objects and calculations]. This
completes the proof of the claim.
```

The words “We claim that ...; in particular, ...” clearly mark the beginning
of the intermediate goal, “Indeed, ...” begins its explanation, and “This
completes the proof of the claim” (or an equivalent sentence) clearly marks
the end. Use this boundary pattern for each intermediate claim in a long
proof; do not force it into a short proof that has no genuine intermediate
goals.

## Algebra and homological notation

- If the discussion combines fields that use complexes differently, state explicitly whether complexes are chain complexes or cochain complexes, and use that convention consistently.
- State whether modules are left or right modules.
- State the degree of every chain group and the domain and range of every differential.
- Keep the original algebraic convention for path classes, arrows, and multiplication. Do not silently reverse path indices.
- In a homotopy calculation, write the exact expression being evaluated, such as $d^{k+1}h^k(p^{(\sigma_\ast)})$, and identify each resulting summand by its chain label.
- Separate a complex from its truncation, augmentation, resolution part, associated graded complex, and homology. Give each object a symbol.

## Writing style

- Prefer symbols to equation-number references when the identity or object has a meaningful name.
- Use dollar delimiters for inline mathematics when preparing TeX for a user who prefers them.
- Avoid unexplained pronouns and nouns with several possible referents.
- Keep explanations concise by using explicit notation rather than repeated prose.
- Preserve the user's notation and terminology unless it is mathematically inconsistent. If two conventions are plausible, ask before changing them.
- Use British English throughout.
- Hyphenate compounds beginning with `non-`, such as `non-zero`, `non-abelian`, and `non-commutative`.
- Always use the Oxford comma in lists of three or more items.
- Use direct phrasing and active voice wherever possible.
- Use “we” rather than “I” in mathematical exposition and proofs. Avoid first-person singular phrasing.

## Bibliography and citations

- Use compact author-initial-and-year labels of the form `[XXXyy]`, never numerical labels or full author-name-and-year labels.
- For a single author, form the label from at most the first three letters of the surname followed by the year, for example, `[Kin24]`.
- For multiple authors, use the authors' initials followed by the year, keeping the label compact and unambiguous.
- Configure the chosen LaTeX bibliography system so that the bibliography labels and in-text citations use this convention consistently.

## Hom and End spaces

- Always label the category in the subscript when writing a Hom or End space, even when the category is clear from context.
- For modules, write the algebra explicitly, for example, `\Hom_A(M,N)` and `\End_A(M)`.
- In homotopy, derived, and other categories, write the category explicitly, for example, `\Hom_{\mathcal K}(X,Y)`, `\Hom_{\mathcal D}(X,Y)`, or `\End_{\mathcal C}(X)`.
- For a stable category, use `\ul{\Hom}_{\underline{\mathcal C}}(X,Y)` when `\underline{\mathcal C}` denotes the stable category. If the stable-category notation is not already clear, define it before use.

## LaTeX notation

Always include the following package setup in LaTeX output:

```latex
\usepackage[hyperpageref]{backref}
\usepackage[pagebackref]{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=red,  %section,table of contents
    filecolor=blue,  %local file link
    urlcolor=orange, %url
    citecolor=violet   %citation
}
\renewcommand*{\backref}[1]{}  
   \renewcommand*{\backrefalt}[4]{
      \ifcase #1 
         Not cited.
      \or
         Cited on page #2.
      \else
         Cited on pages #2.
      \fi}
```

Whenever introducing a new mathematical term, mark the term with `\defn{...}` and include this definition in the preamble:

```latex
\definecolor{darkblue}{rgb}{0,0,0.7} % darkblue color
\newcommand{\defn}[1]{\textsl{\color{darkblue} #1}}
```

For LaTeX output, put the following setup in the preamble, omitting only macros that are not used in the write-up. Preserve the definitions exactly when they are included:

```latex
% Letter
\newcommand{\A}{\mathcal A}
\newcommand{\D}{\mathcal D}
\renewcommand{\H}{\mathcal H}
\newcommand{\T}{\mathcal T}
\newcommand{\U}{\mathcal U}
\newcommand{\V}{\mathcal V}
\newcommand{\W}{\mathcal W}

\newcommand{\RR}{\mathbf{R}}
\newcommand{\LL}{\mathbf{L}}

\newcommand{\NN}{\mathbb N}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\op}{\mathrm{op}}

% Arrow
\newcommand{\mono}{\hookrightarrow}
\newcommand{\epi}{\twoheadrightarrow}
\newcommand{\iso}{\similarrightarrow}
\newcommand{\xto}{\xrightarrow}

% Abelian category
\DeclareMathOperator{\Fac}{Fac}
\DeclareMathOperator{\Sub}{Sub}
\DeclareMathOperator{\Filt}{Filt}
\DeclareMathOperator{\add}{add}
\DeclareMathOperator{\Add}{Add}
\DeclareMathOperator{\rad}{rad}
\ReDeclareMathOperator{\top}{top}
\DeclareMathOperator{\simp}{Sim}
\DeclareMathOperator{\id}{id}
\DeclareMathOperator{\ind}{ind}
\DeclareMathOperator{\cok}{cok}
\DeclareMathOperator{\proj}{proj}
\DeclareMathOperator{\inj}{inj}
\DeclareMathOperator{\colim}{colim}
\DeclareMathOperator{\obj}{obj}
\DeclareMathOperator{\Mod}{\mathcal Mod}
\let\mod\relax
\DeclareMathOperator{\mod}{mod}
\DeclareMathOperator{\fl}{fl}
\DeclareMathOperator{\grmod}{grmod}
\DeclareMathOperator{\Grmod}{Grmod}

% Triangulated category
\DeclareMathOperator{\thick}{thick}
\DeclareMathOperator{\cone}{cone}
\DeclareMathOperator{\per}{per}
\DeclareMathOperator{\pvd}{pvd}
\DeclareMathOperator{\fd}{fd}

% Functor
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\End}{End}
\DeclareMathOperator{\Aut}{Aut}
\DeclareMathOperator{\RHom}{\RR Hom}
\DeclareMathOperator{\REnd}{\RR End}
\DeclareMathOperator*{\Ltensor}{\otimes^{\LL}}
\DeclareMathOperator{\Tot}{Tot}
\DeclareMathOperator{\Ext}{Ext}
\DeclareMathOperator{\Tor}{Tor}

% Others
\newcommand{\ul}[1]{\underline{#1}}
\newcommand{\ol}[1]{\overline{#1}}
\newcommand{\wtilde}{\widetilde}

\newcommand{\Ker}{\operatorname{Ker}}
\newcommand{\Image}{\operatorname{Im}}

% Homological dimension
\DeclareMathOperator{\domdim}{domdim}
\DeclareMathOperator{\fdim}{fdim}
\DeclareMathOperator{\idim}{idim}
\DeclareMathOperator{\pdim}{pdim}
\DeclareMathOperator{\gldim}{gldim}

\DeclareMathOperator{\supp}{supp}
```

If a macro in the requested setup is undefined or incompatible with the selected document preamble, flag the issue and make the smallest necessary correction rather than silently changing the notation.

## Final precision check

Before sending a mathematical explanation or TeX passage, verify:

- every symbol has been defined;
- every map has a domain and codomain;
- every component has its vertex or degree specified;
- every quantified variable has a stated range;
- every use of "this," "that," "the term," or "the map" has an unambiguous symbolic referent;
- every cancellation identifies the two explicit summands and their coefficients;
- edge cases such as empty complexes, degree $0$, and zero summands have been addressed when relevant.
