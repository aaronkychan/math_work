# Writing Conventions for the 2026 Koszul Lectures

**Updated:** 21 October 2026.

This guide consolidates the author's instructions, the installed math-discussion skill, and the conventions recorded in the current lecture sources. It is a checklist for future writing, not a claim that every existing passage already complies. It does not authorise changes to the notes.

## 1. Working Sources and Scope

- Read the installed **math-discussion** skill before mathematical drafting or revision, and read [AGENTS.md](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/AGENTS.md).
- The mother file is [Lecture_Koszul.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Lecture_Koszul.tex). Each lecture is one numbered section, in `Lecture_Koszul_S<n>.tex`.
- Follow [Replan Koszul course.md](</Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Planning/Replan Koszul course.md>) for the course trajectory, but respect subsequent decisions and the prerequisites actually established in the notes.
- Read the latest saved sources. Old theorem numbers and proposal snapshots are not substitutes for reading the current text.
- Among course-specific editorial directions, later explicit instructions replace earlier incompatible preferences. **Ask when a notation or convention is uncertain; do not guess.**
- Lectures 1 and 2 have been declared final. Do not revise them or any other lecture outside the requested scope merely to improve consistency.

### Current Degree Zero Convention

The following presentation in the current preamble and Assumption `ass:basic-semisimple` was explicitly confirmed on 21 October 2026:

- From that assumption onward, $S=\bigoplus_{i=1}^n\Bbbk e_i$ unless stated otherwise.
- The main text uses only the $\Bbbk$-linear duals $D$ and $\mathbb D$.
- One-sided $S$-duals and their comparisons belong to advanced material.
- Remarks headed **General $S$** explain the adjustments for arbitrary finite-dimensional semisimple $S$. Results already proved in that generality retain it.

This supersedes the earlier instruction to keep arbitrary semisimple $S$ throughout the main text. AGENTS.md still contains that older wording; follow the confirmed preamble convention above when drafting. Keep results already established for general $S$ general. The split assumption allows several simple modules and does not mean $S=\Bbbk$.

## 2. Audience and Mathematical Viewpoint

- Write as a professional mathematician teaching beginning graduate students. Assume only basic ring and module theory, not familiarity with algebras, categories, advanced ring theory, or homological algebra.
- Each lecture is **90 minutes**. Keep the main route teachable in that time; place lengthy verification and optional theory in the appropriate blocks.
- Be concise, direct, and rigorous. Give brief intuition around definitions and theorems when it helps. Avoid cliches, convoluted phrasing, repeated motivation, and explanations that conceal the main point.
- Do not add a general overview unless requested.
- Introduce every term, operation, action, functor, and symbol before using it. Audit the actual earlier text, rather than assuming that familiar material has already been taught.
- Use category language as an organisational tool. Introduce basic categories, functors, naturality, and short exact sequences without turning them into an obstacle.
- Develop homological algebra for modules, not through general abelian-category theory.
- Follow the non-commutative, representation-theoretic viewpoint of **BGS**: Beilinson--Ginzburg--Soergel, *Koszul duality patterns in representation theory*. Use Grant--Iyama's preliminaries alongside BGS Section 2.7 when checking dual conventions.
- Do not centre the exposition on connected algebras or repeatedly single out $S=\Bbbk$. The polynomial/exterior pair is the principal deliberate field-base example.
- Use several-simple and non-commutative examples: upper triangular algebras, idempotent summands, and quadratic quotients. Write `\Bbbk A_n`, not `UT`; do not require quiver terminology before introducing it.
- Explain idempotents as local identities where useful, together with orthogonal decompositions and corner algebras.
- Never silently assume $S=A_0$ is central in $A$.
- Start with **group gradings**. Afterwards, “graded algebra” means $\mathbb Z$-graded and concentrated in non-negative degrees unless stated otherwise. Graded modules may have negative degrees.
- Avoid semigroup-grading terminology and “$\mathbb Z_{\geq0}$-graded”. This does not prohibit summing over non-negative degrees or using non-negative exponent indices.
- Say **locally finite-dimensional**, not “locally finite”. The defined abbreviation `lfd` is available.
- Do not impose $\Bbbk=\mathbb Q$, characteristic zero, or algebraic closedness without a reason. If only characteristic different from 2 is needed, state that local hypothesis.
- For general finite-dimensional semisimple $\Bbbk$-algebras, Artin--Wedderburn involves matrix rings over division $\Bbbk$-algebras, not necessarily over $\Bbbk$. Explain a split specialisation under its actual hypothesis.

## 3. Definitions, Examples, and Proofs

### Definitions and Placement

- A definition should give the defining data or condition and then stop. Put standing conventions, assumptions, consequences, and motivation outside it.
- Retain the stated type of object, such as “graded vector space”, when revising a definition.
- Replace “satisfying the preceding condition”, “as indicated”, and similar vague pointers by the explicit condition or a precise labelled reference.
- Introduce constructions close to their first genuine use. Do not retain a proposition simply because it is true.
- Do not introduce unnecessary names such as “balanced tensor product” or an unneeded “relative” qualifier.
- Main-text reasoning must not depend on a definition or statement appearing only in supplementary or advanced material.

### Examples

- Give accessible examples with enough calculation for students to reconstruct them.
- An example that only instantiates a definition needs no separate purpose sentence.
- Before an application, counterexample, edge case, or unexpected behaviour, state its precise purpose briefly: which result is applied, hypothesis is needed, or assertion fails.
- Do not make a special case sound significant when the observation holds for every algebra, as with placing an algebra entirely in degree zero.
- Check the property an example is supposed to illustrate. For a non-homogeneous two-sided ideal, $(x-x^2)\subset\Bbbk[x]$ is an agreed simple example.
- Initially use independent spaces $V,W$ for symmetric and exterior algebras, with bases $x_i$ and $y_j$. Only when computing quadratic duals identify $W=D(V)$ and $y_i=x_i^*$.
- Preserve the monomial-counting explanation for symmetric/exterior Hilbert series. Do not silently replace it by an unexplained product formula.

### Proofs and References

- State the hypotheses actually used. Explain where finite generation, finite-dimensionality, boundedness, semisimplicity, or nilpotence enters; remove unnecessary assumptions.
- For equivalent conditions, announce the implication route and label each implication, e.g. `\underline{$(1)\Rightarrow(2)$.}`.
- Split long proofs into short, labelled steps. If an intermediate assertion needs a substantial argument, make it a lemma or proposition, not a long paragraph beginning “We claim”.
- Show the actual terms in a cancellation and the maps in a factorisation. Avoid “the usual argument” when it hides the required reasoning.
- State universal properties using explicit maps, uniqueness, and a commutative diagram.
- When identifying two universal objects, explain that each composite and the identity satisfy the same factorisation condition; uniqueness therefore makes them equal.
- For the tensor-product universal property, use “factorisation (commutative diagram)” and label the arbitrary bilinear map explicitly, e.g. `\forall\ \text{bilinear } b`.
- Do not redraw naturality squares merely to restate a previously established natural isomorphism. Cite that isomorphism and give the particular commuting identity needed.
- Use `\ref`, `\eqref`, and specific hyperlinks when recalling earlier material. Do not expect readers to remember what a remotely introduced $\alpha_M$ or $\beta_N$ denotes.

## 4. Phrasing and Typography

| Prefer | Avoid |
|---|---|
| “degree $i$ component”, “degree 1 generator”, “degree zero part” | “degree-$i$ component”, “degree-one generator” |
| “degree-preserving”, “orientation-preserving”, “orientation-reversing” | Removing these standard hyphens |
| “finite-dimensional”, “two-sided”, “$S$-module” | Removing standard mathematical hyphens indiscriminately |
| “Choose a basis $\{u_i\mid i\in I\}$ of $U$.” | “Choose bases $u_i$, indexed by $i\in I$, of $U$.” |
| “with basis $\{u_i\otimes v_j\mid i\in I,\ j\in J\}$” | Long prose separating elements from their indexing conditions |
| $(v_i)_{1\leq i\leq n}$ | $(v_i)_{i=1}^{n}$ |
| “for all $g,h\in G$” | A bare membership condition appended in parentheses or brackets |
| “the element $u\otimes v$” | “the tensor $u\otimes v$” |
| “the vector $u\otimes v$”, when its vector-space nature matters | Extra terminology without a purpose |
| “tensor product” | “balanced tensor product” |
| “$S$-preserving isomorphism of graded algebras” | “graded isomorphism over $S$” |

- Use British English, the Oxford comma, and “non-X” forms such as “non-zero” and “non-empty”.
- Prefer explicit mathematical symbols to verbose prose, but **avoid auxiliary symbols used only once**. For example, use `h_{\SymAlg(V)}` and `h_{\bigwedge W}`, not new names $P,E$ just for those subscripts.
- Give each map its domain, codomain, and rule; specify the side for a multiplication map.
- Say that a linear map is **induced** by a bilinear formula through a universal property, and identify the source formula and resulting map.
- State whether a family is arbitrary and set-indexed, finite, or otherwise restricted.
- Write direct sums of copies as `M^{\oplus n}`, not ambiguous `M^n`.
- Use numbered `\subsection{...}`, not `\subsection*{...}`. The existing unnumbered front convention and final symbol list are separate matters.
- Keep minor details inline. Reserve displays for important definitions, formulae, calculations, and diagrams.
- Combine short related displays with `\qquad`, “where”, or “such that”. Keep short quantifiers on the displayed line.
- When expanding a displayed definition, retain its existing identifications unless their removal is requested or necessary.

Preferred compact patterns:

```tex
A=\bigoplus_{g\in G}A_g
\quad\text{such that}\quad A_gA_h\subseteq A_{gh}
\quad\text{for all }g,h\in G.

1,x,x^2,\ldots
\quad\text{in degrees}\quad 2,3,4,\ldots,
\quad\text{respectively}.
```

The second pattern describes a shifted example; it is not a convention for the degree of the unit in an unshifted algebra.

## 5. Notation and Macros

Reuse the mother's macros rather than creating aliases.

| Object | Convention |
|---|---|
| Base field and grading group | `\Bbbk`, `\Z` |
| Positive-degree ideal | `A_+`, not `A_{>0}` |
| Algebra radical | `\rad A`; do not abbreviate to $J$ unless notation genuinely becomes unwieldy |
| Module radical | `\rad M` instead of repeated `M\rad A` when $A$ is finite-dimensional |
| Ordinary top | `\top M`, meaning $M/\operatorname{rad}M$ in the established finite-dimensional-algebra setting |
| Graded top | `\grtop M`, displaying $\operatorname{top}_{\mathrm{gr}}M$, defined as $M/MA_+$ |
| Ungraded modules | `\Mod A`: all right modules; `\mod A`: finitely generated right modules |
| Graded modules | `\Grmod A`: all graded right modules with degree-preserving maps |
| Locally finite-dimensional graded modules | `\grmod A`; **not** the finitely generated graded category |
| Graded Hom | `\Hom_A^{\Z}(M,N)`: degree-preserving maps |
| Underlying ungraded Hom | `\Hom_A(M,N)`, with no underline |
| Underlined Hom | Reserved for stable-category morphisms in the later BGG discussion |
| Ungraded linear dual | `D(M)`, not a check accent |
| Graded linear dual | `\bbD(M)`, displaying $\mathbb D(M)$ |
| Right and left $S$-duals | `M^*` and `{}^*N`, with acting sides specified; advanced |
| Graded $S$-duals | The existing `\grstar` macro: `M^{\grstar}` and `{}^{\grstar}N`; advanced |
| Bimodule | `{}_AM_B`; say “a bimodule $ {}_AM_B$”, not “an $(A,B)$-bimodule $M$” |
| Bimodule category | `A\Mod B`, with analogous `A\mod B`, `A\Grmod B`, and `A\grmod B` |
| Additive closure | `\add M` defaults to the right-module category |
| Left-module additive closure | Specify the category, e.g. `\add_{\mod A^\op}(M)` |
| Simple modules | $L_1,\ldots,L_n$; use $n$ for the number of simple-module classes |
| Hilbert series | Lower-case `h_M(t)`, `h_A(t)` |
| Dimension vector | `\dimvec`; a row vector in the Hilbert-series discussion |
| Symmetric algebra | `\SymAlg(V)`; the current macro prints $\mathsf S(V)$ |
| Exterior algebra | `\bigwedge W` |
| Opposite and enveloping algebras | `A^\op`, `A^\en`; preserve the established action convention |
| Operators | Reuse `\Hom`, `\End`, `\Ker`, `\Im`, `\Ext`, `\Tor`, and `\id` |

Additional cautions:

- `\Mod(A^\op)`, the left-module category, is not `(\Mod A)^\op`, the opposite category.
- Keep action-side annotations such as $V_S$ and $ {}_SW$ where useful, even when the ambient category is also written.
- “Finitely generated” and “finite-dimensional” coincide for modules over a finite-dimensional algebra, not over every algebra.
- The shift is `M(d)_j=M_{j+d}`. Thus `A(-d)` has its generator in degree $d$, and `h_{M(d)}(t)=t^{-d}h_M(t)`.
- Do not replace homology notation $H_i$ merely because Hilbert series use lower-case $h$.
- Avoid “augmentation ideal” in exposition; the agreed footnote may mention it as another name for $A_+$.
- Do not give the quotient map $A\to A/A_+$ independent notation before it is needed.
- Do not unnecessarily redefine the self-explanatory phrase “$S$-preserving”.

## 6. Tensor Products, Duals, and Action Sides

- Introduce tensor products of vector spaces before tensor products over an algebra and tensor algebras.
- In general tensor-product statements use an arbitrary algebra $A$ as base; use $S$ when semisimplicity is needed.
- **Course-specific exception:** use $T_S(V)$ for the tensor algebra, keeping its degree zero algebra visible. Do not turn this exception into a general math-discussion-skill rule.
- Introduce outer actions and Hom/tensor functors before relying on them. An action obvious to an expert is still a prerequisite for a beginner.
- Call $\mathbb D$ the **graded $\Bbbk$-linear dual**. Keep both its component decomposition and the Hom description:
  $\mathbb D(V)_i=D(V_{-i})=\operatorname{Hom}_{\Bbbk}^{\mathbb Z}(V,\Bbbk(i))$.
- Introduce the graded linear dual as an extension of the ungraded construction before comparing different duals.
- Display the contravariant functors with their source and target categories. Distinguish an exact contravariant functor from a duality; state the finiteness needed for the bidual map to be an isomorphism.
- Highlight finite-dimensional modules and locally finite-dimensional graded modules. Finite generation over locally finite-dimensional graded $A$ implies local finite-dimensionality, but the graded linear dual need not remain finitely generated.
- Call $V\to D(D(V))$, $v\mapsto(f\mapsto f(v))$, **evaluation**. Keep it distinct from tensor coevaluation; do not call the inverse bidual map “coevaluation” merely because its arrow is reversed.
- For general $S$, record any chosen symmetrising form in a comparison with $D$. Explicitly describe its non-degeneracy condition.
- Since $S$ is not generally central in $A$, do not assign an $A$-action to $\operatorname{Hom}_S(M,S)$ by an unchecked formula. Define the action or specify its transport through the chosen comparison.
- Keep one-sided and two-sided $S$-duals, their comparison theory, separability, and division-algebra symmetrising forms advanced under the confirmed presentation.
- Keep direct sums central. Direct products, tensor/product failure, and completions are normally advanced unless naturally needed in the main argument.
- Include formal power series as the direct-product/completion counterpart of polynomial spaces where appropriate. An infinite product is not an ordinary direct-sum grading.

### Quadratic Duals

- Under `ass:basic-semisimple`, use the current main-text definition $A^!=T_S(D(V))/(R^\perp)$.
- Place $D(V)$ in degree 1 as the generator space of $A^!$; do not confuse this placement with the degree of $\mathbb D(V)$.
- Use `eq:D-tensor-duals`, which reverses tensor factors. Do not insert a naive scalar pairing over a non-central base without checking the tensor-product identities.
- In **General $S$** remarks, point to the advanced one-sided-dual construction or explain the choice of symmetrising form.
- Do not silently change the multiplication convention, reverse path indices, or suppress an opposite algebra.

## 7. Hilbert Series

- The main point is **counting composition factors, with grading recorded by powers of $t$**. Do not bury it in extra constructions.
- For right modules, use the row vector $([M_d:L_j])_{1\leq j\leq n}$ and the series $h_M(t)=\sum_d([M_d:L_j])_{1\leq j\leq n}t^d$.
- Build $h_A(t)$ from one-sided modules: $h_A(t)_{ij}=\sum_{d\geq0}[e_iA_d:L_j]t^d$.
- Retain both indices, but do not introduce a separately named “matrix Hilbert series” or an unnecessary bimodule dimension vector. For a bimodule $U$, use the one-sided multiplicities $[e_iU:L_j]$.
- In general semisimple settings, compute multiplicities through Hom dimensions **over $\operatorname{End}_A(L_j)$**, not automatically over $\Bbbk$; use `eq:composition-Hom`.
- Do not replace the composition-factor explanation by a detour through $L_i\otimes_S A$.
- For general $S$, choose one representative primitive idempotent per simple class; do not assume those representatives sum to $1$.
- Explain coefficient multiplication by summing over the matching middle index, and state the hypotheses for multiplying series.
- Series are formal, not analytic. Algebras give power series; bounded below modules may give Laurent series; finite support gives polynomials or Laurent polynomials. Do not assume every locally finite-dimensional module is bounded below.
- Preserve the derivation from monomial bases for polynomial and exterior examples.
- The Koszul Hilbert-series identity is a necessary numerical test, not an unrestricted converse. The course plan includes examples satisfying the identity without being Koszul.

## 8. Homological Algebra and Future Lectures

### Ordinary Modules First

- Develop projectivity through lifting, exactness of $\operatorname{Hom}_A(P,-)$, split surjections onto $P$, and direct summands of free modules.
- Introduce radical, top, Nakayama, projective covers, complexes, homology, and resolutions for ordinary modules first.
- Keep the nilpotence consequence for finite-dimensional $A$ as a compact remark after Nakayama's lemma.
- Use $\operatorname{rad}M$ in finite-dimensional-algebra cover/minimality criteria. Retain $M\operatorname{rad}A$ when $A$ is arbitrary or the product itself is needed.
- Do not unnecessarily require $M$ or $P$ to be finite-dimensional in the cover criterion and existence results over finite-dimensional $A$. Explain the role of nilpotence. Uniqueness needs no additional finiteness.
- Define minimality using explicit maps onto kernels and a factorisation diagram labelled “proj. cover”.
- Do not use syzygies to define minimality. Mention the terminology afterwards for kernels in a minimal resolution, with independence up to isomorphism explained by uniqueness; normally continue to say “kernel”.
- Then give the graded versions, with degree-preserving maps and the correct boundedness/local finite-dimensionality assumptions.
- Separate homological degree from grading degree. Chain differentials lower the former by 1 and preserve the latter.
- Use graded projective modules in general, not graded free modules without justification.
- Keep graded Betti-number notation advanced.
- Define right/left noetherianity explicitly. Keep its key consequence in the main text: finite generation of successive kernels and terms, not necessity for existence of the bounded below locally finite-dimensional resolution.

### Later Course Development

- Follow the route through the Koszul complex, Koszul algebras, Tor/Ext, the Yoneda algebra, the numerical test, linear complexes, and BGG.
- Keep $S=A/A_+$ with its several simples visible; do not replace it by one selected simple module.
- Derive shift signs from `M(d)_j=M_{j+d}`. Translate an Ext-vanishing diagonal from the plan or a reference rather than copying its indices unchanged.
- Check whether the Yoneda algebra identifies with $A^!$ or its opposite under the course's right-module and product conventions.
- Keep $D,\mathbb D$ in the main route. Add **General $S$** remarks where coordinate idempotents or dual comparisons matter, especially for the Yoneda algebra, Koszul complex, and numerical identity.
- Distinguish ordinary algebra tensor products from graded tensor products with signs.
- Introduce stable/quotient categories when needed, and retain underlined Hom for stable morphisms. Do not assume general categorical machinery in advance.

## 9. Environments, Citations, and Document Layout

### Main, Supplementary, Advanced, and Hidden Material

| Environment | Purpose | Appearance or control |
|---|---|---|
| Main text | Definitions, statements, examples, and arguments needed for the course | Ordinary text |
| `supplementary` | Proofs and routine verifications of main-text statements; optional detail for rigour | Pale green `#E8F5E9`; dark green left border, RGB `(0,0.35,0.20)` |
| `advanced` | Optional theory and extensions not needed for the main lecture | Beige `#EDE8D0`; red left border `#B22222` |
| `hidden` | Retained source material, including solutions, excluded from the ordinary lecture PDF | Controlled by `\showhiddenfalse` / `\showhiddentrue` |

- Preserve the opening examples explaining supplementary and advanced material, and the author's current disclaimer. Do not rewrite them incidentally.
- Keep essential definitions and statements outside optional blocks. Their longer proofs or routine checks may be supplementary.
- Put advanced statements and their advanced proofs together. Avoid redundant nesting of coloured blocks.
- Both coloured environments use `mdframed`, a left border only, and indentation. Preserve the current padding, including 10pt above/below and at page splits; the background must cover the full first line.
- Put `\begin{hidden}` and `\end{hidden}` on separate, unindented lines. Do not replace exclusion by white text, clipping, or another merely visual concealment.
- Compile using the **existing hidden-content setting**. Do not test both settings unless explicitly asked.
- Use `\defn{...}` for newly defined terminology; it currently gives dark blue slanted text.
- Treat `\comm{...}` as the author's editorial comments. Discuss comments asking for an opinion before preparing a proposal.
- Preserve source commented out with `%` or `\iffalse...\fi`, unless its alteration is explicitly requested.

### Citations and Navigation

- Put external literature citations only in advanced material. Internal references to earlier definitions, results, and equations are encouraged throughout.
- Use the local BGS and Grant--Iyama papers when checking conventions. Give precise theorem/page references when citing an external result; do not invent a citation.
- Supply proper published references for advanced facts such as the separability/enveloping-algebra criterion and symmetrising forms over division algebras, rather than relying only on an arXiv article.
- Keep labels stable and use linked `\ref`, `\eqref`, and `\hyperref` references. Check all affected references after moving material.
- Maintain the **List of Symbols** at the end, after a page break and before the bibliography. Each entry needs a short explanation and a link to its first introduction; mark advanced entries accordingly.

### Shared Format

- Preserve the established preamble, originally based on the previous year's quiver/homological-algebra notes. Make only necessary additions.
- Keep the title **Topics in Mathematics Science VII**.
- Put shared macros, formatting, inputs, the symbol list, and the bibliography in `Lecture_Koszul.tex`; keep lecture content in its section file.
- Reuse the theorem, proposition, lemma, corollary, definition, example, exercise, assumption, remark, convention, notation, and proof environments already defined. Preserve the shared section-based theorem and equation numbering.

## 10. Homework and Revision Workflow

### Homework

- The active assignment is [Homework1_v3.tex](/Users/aaronchan/Documents/GitHub/math_work/2026_Koszul_lectures/Homework1_v3.tex), confirmed by the author on 21 October 2026. `Homework1.tex` and `Homework1_v2.tex` are older versions and must not be updated unless requested.
- Use v3 for homework edits and comparisons with the lecture notes. Confirm any future version change with the author rather than inferring authority from filenames or modification times.
- Lecture exercises and homework overlap, but neither collection contains the other. Match mathematical questions, not merely exercise numbers, before synchronising.
- Do not add question titles, reminders of definitions or lecture locations, or unnecessary notices such as “The following parts are independent”.
- Separate the question from its hint and label the hint clearly.
- When an exercise's solution should be withheld, retain the solution in the source after the question using the appropriate exclusion mechanism; do not delete it.
- The current homework uses the `exam` class, `solution` environments, and `\noprintanswers` / `\printanswers`, not the lecture's `hidden` switch.
- Audit prerequisites and replace unexplained instructions such as “check the tensor relations” by the actual identities to check.

### Reading Comments and Proposing Changes

1. Read the latest saved version and the relevant `\comm` comments. If expected comments are missing, ask about saving/syncing rather than assuming their contents.
2. Establish the requested scope. Discuss opinion questions and genuine mathematical choices before writing a change proposal.
3. Unless direct application has been authorised, prepare the proposal and wait for approval before overwriting the user's mathematical text.
4. Use Markdown, never plain text, for proposal files. Continue the `ChangeProposal<N>` sequence in `Planning/`, followed by the affected lecture(s), e.g. `ChangeProposal18_Lecture4.md`. Check the next number when creating it; keep the number when revising it.
5. Give the proposal a matching title, approval status, scope summary, and linked contents or summary table. Number and name each replacement.
6. Make fenced `diff` blocks the primary comparison, with explicit `-`/`+` lines, accurate locations, a legend, and added/removed counts. Do not rely on colour alone.
7. For actual content changes, retain exact existing and proposed passages, preferably in labelled collapsible sections beneath the diff. Never silently abbreviate or rewrite quoted source.
8. **Mechanical terminology/notation changes are the exception:** state the substitution and list the affected files and line numbers. Do not quote every changed line.
9. Before applying approved replacements, reread the affected source. Preserve intervening author edits; ask again if an approved replacement would overwrite a new substantive change.
10. Apply only the approved changes and requested immediate corrections. Do not extend a local task into unrelated lecture revisions, homework edits, or skill updates.

### Verification and Delivery

- After TeX changes, compile the mother project using the built-in `compile_latex_document` check, fix introduced errors, and retain an up-to-date compiled PDF in the course folder as requested.
- An explicit instruction **not to compile** overrides that default. A Markdown-only task does not require TeX compilation.
- Check reference resolution, numbering, overfull text, diagrams, and coloured-block spacing as relevant. Report existing unresolved issues separately from introduced ones.
- Do not change the hidden-content switch for verification.
- **Keep the right side panel closed.** Never open a document, preview, or different tab unless explicitly asked. Provide a file link in the reply instead.
- Keep the final report concise: what changed, verification performed, and any unresolved issue. Do not claim compilation or checking that was not actually performed.
- General style conventions belong in the math-discussion skill when an update is requested; course-specific mathematical choices belong in this guide and the lecture sources.

## 11. Pre-Delivery Checklist

- [ ] Latest source read; user edits and commented-out content preserved.
- [ ] Requested scope and approval respected.
- [ ] Confirmed preamble followed: split semisimple $S$ from `ass:basic-semisimple`, $D,\mathbb D$ in the main text.
- [ ] Every required term, action, symbol, and construction introduced before use.
- [ ] Maps, action sides, grading shifts, and quantifiers explicit.
- [ ] No unnecessary auxiliary symbols, vague references, or unexplained product formulae.
- [ ] Examples have a purpose sentence when they do more than instantiate a definition.
- [ ] Main statements remain visible; optional detail is in the appropriate environment.
- [ ] Notation, hyphens, index ranges, direct-sum powers, and compact displays follow the conventions above.
- [ ] General semisimple caveats, duality hypotheses, and left/right distinctions checked where relevant.
- [ ] Labels and symbol-list entries updated when within scope; compilation completed unless excluded.
- [ ] Side panel remains closed; delivery uses a link.
