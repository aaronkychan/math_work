# Referee-style review of `paper2-via-Morse-theory.tex`

*Distance algebras of finite distributive lattices are Gorenstein* (A. Chan, B. Xing). Version dated 27 Oct 2026, 2344 lines. All line numbers refer to this file.

This is an exposition-only review. I did not check the mathematics. In a few places a sentence is wrong or inconsistent as written. I mark those "(check)" and give the reason.

---

## Part I. General comments

### 1. What the paper does, and what the reader sees first

The paper makes four contributions:

1. A strict-chain projective resolution of each indecomposable injective I_X.
2. The bound pdim I_X ≤ |P|−2 for |P| ≥ 3, which gives the Gorenstein property.
3. A Morse-theoretic minimal resolution whose multiplicities are reduced Betti numbers of strict upsets.
4. Multiplicity results (free in degrees 0 and 1, arbitrary in higher degrees).

There is also an unannounced fifth result: pdim I_X = reg k[S_X] (Subsection "Projective dimension and Castelnuovo–Mumford regularity", lines 1763–1908).

The mathematics is organised sensibly, and the running example P = {1<2} ⊔ {3} is a real strength. The problems are in how the paper is packaged. In order of importance:

**(a) The introduction undersells and misdescribes the results.**
- Main Theorem 2 (lines 60–66) says "we construct a minimal projective resolution" but never says what it is. The core result of the Morse section is the formula [P_min,k : P_Z] = dim H̃_{k−1}(Δ^{>Z̲}). It appears only in the abstract and in Theorem 4.4, not in the introduction.
- Neither the formula for pdim I_X (Cor. 4.6) nor the exact self-injective dimension idim Σ = max_X pdim I_X is stated as a main result. Line 56 claims "this also computes the self-injective dimension", but no displayed statement does this (see detail comment on line 1566).
- The regularity theorem is mentioned nowhere in the abstract or introduction, and the organisation paragraph (line 70) skips it.
- The abstract says the self-injective dimensions are "bounded by the diameter of the Hasse graph". The body proves |P|−1 and |P|−2. The diameter is |P|, but the reader has to work that out. Say "at most |P|−2 (for |P| ≥ 3)".
- Main Theorem 1 has three items, of which (2) and (3) are essentially one statement. |P| ≤ 2 is dealt with by hand in Example 2.12. I suggest one item: "if |P| ≥ 3 then ≤ |P|−2+idim_R R; if |P| ≤ 2 see Example …".
- The introduction contains no example and no sentence of proof strategy. Two or three lines would help: "I_X is the colimit of the diagram Z ↦ P_Z over the poset D_X, and the resolution is its bar construction". This is the content of the appendix, and it is the best idea in the paper. It currently sits on page 30 as a "retrospective".
- The introduction should state the contrast with the companion paper more sharply. Auslander–Gorenstein holds only for products of chains (line 33), but Iwanaga–Gorenstein holds always. The phrase "under the corresponding assumptions on the coefficient ring" (line 33) is empty.

**(b) Preliminaries are too long, and much of them is not "just in time".**
- About 600 lines (89–770) precede the first new construction.
- Roughly 150 lines serve only one later argument. These are the link, face poset and barycentric subdivision definitions, the Munkres lemma, the order-homotopy lemma, and the cone discussion (lines 402–494). They are used only in the regularity subsection and in Prop. 3.x (exactness).
- Lemma 2.8 (lines 500–532) is used once.
- The duality lemma and corollary (lines 125–213), which re-prove standard facts from lattice theory, are about 90 lines.
- My suggestion is to move each tool to where it is first used. Better still, move the regularity subsection and its tools into a short final section or an appendix, and announce it in the introduction. See Part II for a proposed outline.

**(c) Notation is heavy and has several collisions.** The worst ones:
- The poset P and the modules P_x, P_Z.
- The order ideal X and the bipartite halves X ⊔ Y in §5.2, where Y also names an order ideal in §5.1.
- ∂_k means the simplicial boundary in §2 and in Prop. 3.x, but the "internal part of d_k" in §4.2, within 20 lines of ∂^Z_k = −∂_{k−1}.
- δ is the coboundary in Lemma 2.8 and the "external part of d" in §4.2.
- "S" is the simple module S_Z, the complex S_X, the polynomial ring S_K, and a face S ⊆ P.
- 𝓜 is a Morse matching in §4 and the ambient category in the appendix. M is also a thin module there.
- 𝒟 versus 𝒟_X; Q_G (double quiver) versus Q (poset, §2.4) versus Q_2 (square, line 671); A_n (path graph) versus A (algebra).
- The algebra is written Σ_G, Σ_L, Σ_{𝒥(P)}, Σ_P and A, sometimes within one page. A is never introduced before its first use on line 777.
- The underline Z̲ = X ⊕ Z is carried through every formula, although D_X is only a re-ordering of 𝒥(P). By Lemma 2.10 (line 615), Z̲ ⊆ T̲ iff Z lies on a geodesic from X to T. Defining a partial order ⪯_X on 𝒥(P) by "Z ⪯_X T iff d(X,T) = d(X,Z)+d(Z,T)" would remove the underlines from Sections 3–5. The set-theoretic description would then be a lemma, used only when computing.

**(d) The symmetric-difference machinery can be reorganised.**
- The element ∇^{Y,Z}_X (line 559) is the median (majority) of X, Y, Z. It is symmetric, so the subscript/superscript notation misleads. Call it m(X,Y,Z), or maj(X,Y,Z), and say once that it is an order ideal because 𝒥(P) is distributive.
- Item (5) of Lemma 2.9 (lines 570–579) states a special case and then the general case. State only the general case.
- Items (1)–(3) are "left to the reader" (line 596), but (3) is not an exercise at the level of (1).

**(e) Repetition.**
- The proof that d² = 0 appears twice: Prop. 3.1 (lines 820–860) and the appendix (lines 2205–2225). The check d_0 d_1 = 0 also appears twice (lines 984–988 and 2218–2223).
- The remark that the bound |P|−2 is attained appears twice (lines 1332–1334 and 1760).
- Paragraphs at lines 1000 and 1002 say the same thing.
- Cor. 2.2 and Cor. 2.5 largely overlap. So do Cor. 3.x (bound |P|−1) and Prop. 3.x (bound |P|−2). Together with the Main Theorem items, the same bound is stated five times.

**(f) The source contains unfinished editing.**
- Stray macros are live in the text: `\bhx{…}`, `\old{…}`, `\new{Note that .}`, `\xnew{…}` and `\comment{…}`. The worst case is `\bhx{...}` wrapping all of Main Theorem 1 (lines 38–53).
- "Thick arrow" is used in Definition 4.1 (line 1365), but the item that defines it is commented out (lines 1358–1360).
- The acknowledgements to Iyama, Asao and Wakatsuki are commented out (line 83).
- Details are in Part II.

**(g) Prose style.**
- The prose is generally clear but over-uses "Note that", "Thus", "Indeed" and "In particular". Several "Thus"/"which means" connectives are non-sequiturs (lines 249, 718).
- "this note", "these notes" and "this paper" are used interchangeably (lines 78, 252). Choose "paper".
- Some informal asides should be cut: "special gadget" (1344), "striking resemblance" (1764), "feels very close to" (1779), "this shows a non-resolution" (2234).
- Grammar errors cluster in the AI statement, the Morse prose, the regularity motivation and the appendix. They are listed below.

### 2. The appendix: can it be shortened?

**Assessment.** Yes, comfortably. The appendix is about 218 lines (2120–2337), roughly 9% of the paper. It is logically optional. Its main point is the identification 𝒞_{I_X} ≅ 𝒟_X (line 2228), together with the one-sentence consequence that 𝒫_• is the normalized simplicial replacement of Z ↦ P_Z. Most of the remaining length verifies a translation to Riehl's formalism that has no content here: G is the constant functor at a point.

**Where the length goes.**

| Lines | Content | Verdict |
|---|---|---|
| 2127–2165 | thin module, normalised basis, Q_M, C_M, F_M | keep, tighten (~25 lines) |
| 2167–2192 | definition of P_k(M), d_k | keep |
| 2194–2225 | Prop. A.1 and its proof | the proof duplicates Prop. 3.1; replace by "same proof as Prop. 3.1" |
| 2227–2234 | Examples (I_X; simple module) | keep the first and merge into the section below; reduce the second to one sentence |
| 2236–2256 | translation table to Riehl's B_k(G,𝒟,F) | cut |
| 2260–2271 | simplicial modules, constant simplicial module, terminal sSet | cut |
| 2273–2292 | face maps in the bar construction | cut |
| 2294–2326 | degeneracies, normalisation | cut; one sentence plus a citation |
| 2328–2337 | H_k = L_k colim | keep and promote to the first paragraph |

**Proposed shape (about 70–80 lines, roughly 60% shorter).**

1. **A.1 Setup (≈25 lines).** Thin module M with a normalised basis, the category 𝒞_M, the functor F_M, and 𝒫_•(M). Define the category directly as "objects (Q_M)_0, one morphism y → x for each path x ⇝ y". The direction problem at line 2150 disappears.
2. **A.2 Statement (≈5 lines).** 𝒫_•(M) is a complex, "by the same proof as in Prop. 3.1" (or the other way round: prove the general statement once here and make Prop. 3.1 the one-line special case).
3. **A.3 Identification (≈10 lines).** 𝒫_•(M) is the normalized chain complex of the simplicial replacement of F_M [Rie14, Def. 4.2.1]. This is the standard complex ⊕_{x_0→…→x_k} F(x_0) computing derived colimits. Hence H_0 = colim F_M and H_k = L_k colim F_M. One citation to a textbook for "Moore normalisation of a simplicial object" replaces lines 2294–2326. If you want to keep the table, keep it without the surrounding prose.
4. **A.4 The punchline (≈5 lines).** Specialise to M = I_X (Example A.x). Then Thm 3.2 says exactly that colim_{𝒟_X} P_Z ≅ I_X and L_k colim = 0 for k > 0. The sentence at line 2337 ("this will not be the case") is too vague to carry the point.

**Also consider moving the key observation out of the appendix.**
- Section 3.1 would be better motivated if it opened with "𝒟_X is the poset category C_{I_X}; 𝒫_• is the bar construction of Z ↦ P_Z".
- The appendix could then shrink to a half-page remark.
- Prop. 3.1 becomes "d² = 0 holds because F is a functor", with the explicit check (about 15 lines) removed.
- The "Use of AI" paragraph says the appendix "records our retrospect explanation of why one should consider such a construction". That explanation is exactly this two-line observation, and it deserves to be in the body.

**A speculative suggestion (not checked).** The proof of Thm 3.2 (Props. 3.4–3.5, lines 1052–1191) shows, for each W, that 𝒫_•e_W is acyclic. The diagram Z ↦ P_Z e_W is rank one, with transition maps either an isomorphism or zero according to Lemma 3.3. If one phrased the proof as a computation of L_• colim of that diagram, the appendix would become load-bearing rather than retrospective. Prop. 3.4 is also the order-homotopy Lemma 2.7 with coefficients (the formula for h at lines 1099–1107 is the same as at lines 486–487). The proof could say so and shrink by about half.

### 3. Other structural suggestions (ranked by effort/benefit)

1. Put the regularity material (lines 1763–1908) in its own short section, or in an appendix, announced in the introduction, together with the tools it uses (Munkres lemma, order homotopy, links and subdivision). This removes about 150 lines from the preliminaries and makes §4 end at Example 4.7.
2. Move Lemma 2.8 into the proof of Prop. 3.x (lines 1257–1330), the only place it is used, or state it there.
3. Shorten Lemma 2.1, Cor. 2.2 and Cor. 2.5 by citing [IK22], [GN01] and [IKWY15] for the dimension formula and keeping only what is specific to Σ_G. Merge Cor. 2.2 and Cor. 2.5 into one statement.
4. Merge Cor. 3.x (bound |P|−1) and Prop. 3.x (bound |P|−2) into a single proposition with the |P| ≤ 2 cases listed.
5. Introduce the "median" and the geodesic order ⪯_X as in (c) and (d) above, and delete the underline notation.
6. Rename the bipartition in §5.2 (e.g. M ⊔ N, minimal and non-minimal elements) and the Stanley–Reisner complex (e.g. 𝒦_X).
7. Retitle Section 5. "Multiplicity in low degrees" describes only §5.1; §5.2 is about high degrees. "Multiplicities" would do.
8. Remove `\tableofcontents` (line 26) for a paper of this size, if it is headed to a journal.

---

## Part II. Detailed comments

Tags: **[typo]**, **[phrasing]**, **[notation]**, **[structure]**, **[content]** (likely a real error or something that needs justification), **[cut]**.

### Title, abstract, introduction

- **L4** [phrasing] The title promises only Gorensteinness, but half the paper is about minimal resolutions and multiplicities. Consider a subtitle ("…, and their minimal resolutions") or "… are Gorenstein: minimal resolutions via algebraic Morse theory".
- **L23** [content] "bounded by the diameter of the Hasse graph" does not match Theorem 1. Say "at most |P|−2" and mention the diameter, if at all, in a remark. "Turns out to be exact everywhere" is also vague. "Special case of the simplicial bar construction, which we show to be exact" would do.
- **L33** [typo] "we studies" → "we study". [phrasing] The last sentence ("under the corresponding assumptions on the coefficient ring") says nothing. Say what the contrast is: the property that fails for non-chain products (Auslander) versus the property that always holds (Gorenstein).
- **L35** [phrasing] "indexed by strict chains in a symmetric-difference poset" is not understandable before D_X is defined. Say "strict chains in the poset 𝒟_X of Section 2.6" or give one clause of definition.
- **L35–38** [structure] "These resolutions have length at most |P|−1. Together with … this gives our first main result" is misleading, because item (3) of the theorem uses an extra splitting argument. Say so.
- **L38–53** [structure] `\bhx{\textnormal{(see …)} …}` wraps the whole statement, and the cross-reference is inside the braces. Move the "(see …)" outside the theorem body, as is done for Main Theorem 2.
- **L56** [content] "This also computes the self-injective dimension": no displayed statement does this. See the comment on L1566.
- **L58–66** [content] Main Theorem 2 should state, over a field, the formula [P_min,k : P_Z] = dim H̃_{k−1}(Δ^{>Z̲}) and the pdim formula. The hypothesis R = 𝕜 is also missing from the statement. Item 2, "Multiplicities can be arbitrarily large in every higher projective degree", has an unclear quantifier. Write: "for every k ≥ 2 and m ≥ 1 there exist P and X with [P_min,k : P_X] = m".
- **L58** [phrasing] "The combinatorics of order ideals forces multiplicity-freeness in the first two terms" would be clearer as "in degrees 0 and 1".
- **L70** [typo] "Sections~\ref{…} proves" → "Section … proves". [content] The organisation paragraph omits the regularity subsection and the appendix's content apart from one clause.
- **L74** [phrasing] "free over R" here, but "finitely generated projective" elsewhere (lines 97, 120). Choose one. "finite direct sum of direct summands" → "finite direct sums of direct summands".
- **L78** [phrasing] The "Use of AI" paragraph has several garbled sentences. "after we calculated the projective cover of the first syzygy" cites the wrong thing: the label points to the subsection on multiplicity-freeness. "The appendix records our retrospect explanation in why one should consider such construction" → "…records, in retrospect, why this complex is natural". "ChatGPT also suggested the strategy to show is exactness, helped us to refine …, the entire subsection …, and some of the figures throughout this notes" is not a grammatical list. Separate "suggested", "helped refine" and "contributed". Also: "this notes" → "this paper".
- **L83** [content] The acknowledgements to Iyama, Asao and Wakatsuki are commented out. Intentional?

### Section 2.1 (duality and Gorenstein algebras)

- **L99–105** [phrasing] "Iwanaga–Gorenstein" is used for rings and "Gorenstein R-algebra" for the relative notion. A one-sentence summary of how they relate (IG over a field; Gorenstein over a Gorenstein base) would help.
- **L122** [structure] Leftover macros: `\old{some facts} \bhx{the following fact} \comment{…}`. Also "we recall the following fact … The following formulation can be found in …" says the same thing twice. Merge into one sentence.
- **L125–138** [cut] The lemma is standard, and the proof (14 lines) can be replaced by a citation to [BBIKP25, §2] and [CR81, §25] with a one-line sketch.
- **L141** [phrasing] "A ≅ D(A) as right A-modules" is the Frobenius property over a general R. "Self-injective" is only correct over a field. Say "Frobenius (self-injective when R is a field)".
- **L143–213** [cut] The proof of Cor. 2.2 is 40 lines. It could cite [GN01, Prop. 1.1(3)] and [IKWY15, Lemma 4.17] (see line 169) for the inequalities and keep only the new equalities. "When R = 𝕜, both inequalities are equalities" (line 164) is justified only by line 212 and the unproved assertion at line 140 that relative and ordinary injective dimensions agree over a field. Prove or cite it.
- **L163 and L210** [phrasing] The same statement (A is IG if the three dimensions are finite) is made twice. Delete one.
- **L212** [phrasing] "the claim immediately follows" → "the claim follows immediately".

### Section 2.2 (distance algebra)

- **L223** [phrasing] A display `$$d(x,y)=d_G(x,y),$$` inside a running sentence. Use inline math or a proper display.
- **L249** [phrasing] "Thus, each Σ_G is an R-algebra" does not follow from the preceding sentence. Say "Thus Σ_G is a free R-algebra of rank |V|²".
- **L250** [phrasing] "canonical (internal ℝ-)grading" is confusing. Path length gives a ℤ-grading; magnitude homology has an ℝ-grading for metric spaces.
- **L252** [phrasing] "that we concern in this note" → "that we consider in this paper". Also, A is not declared as Σ_{𝒥(P)} until line 777 (see Notation). Add "write A = Σ_L" here.
- **L268** [structure] The multiplicity definition (inside `\bhx`) should say it is for R = 𝕜. Krull–Schmidt can fail over general R, and the definition is used only over a field.
- **L270–285** [cut] The treatment of the anti-involution τ (lines 270–285), τ_*, and (3.x) is about 15 lines. It is needed only to say pdim_{Σ^op} D(Σ) = pdim_Σ D(Σ). Consider reducing it to "τ gives Σ ≅ Σ^op, hence all left/right statements are equivalent".
- **L304–327** [structure] See comment (e): merge with Cor. 2.2.

### Sections 2.3–2.4 (topological preliminaries)

- **L350** [typo] "the the inherited ordering". [content] "We allow the void complex ∅, which has no faces" and, at line 352, Δ(∅) = {∅}: two different things are written ∅. Then line 394 writes H̃_{−1}(∅) = R, which is the value for {∅}, not for the void complex. Use ∅ for the void complex and {∅} for the complex with only the empty face, throughout. This also affects Examples 2.13 (lines 754–755), the proof of Prop. 5.1 (line 1947) and Lemma 3.x (line 1235).
- **L374** [cut] Ordinary homology H_r is defined here but hardly used. Define reduced homology only.
- **L400** [typo] `'$;R$'` has mismatched quotes; use ``…''.
- **L405–418** [cut] Cones are acyclic: standard. A reference or two lines suffice.
- **L434** [content] "the order complex of the power set 2^E … is a (|E|−1)-simplex on E" is not correct as stated. The order complex of 2^E (with ∅ and E) is a cone of dimension |E|. The (|E|−1)-simplex on E is the simplicial complex 2^E itself. Say "the simplex 2^E (as a simplicial complex)" and then "its barycentric subdivision is Δ(2^E ∖ {∅})".
- **L445–458** [phrasing] 𝓕(K)_{>F} is defined in the lemma and redefined in the proof.
- **L483–493** [phrasing] "This is the chain-complex version of [Bjo95, Thm 10.11] … We can verify it directly … routine to check": choose a lean option (cite) or give the verification. The same formula is later reused in Prop. 3.4.
- **L500–532** [cut] See General comment 3 (move to Prop. 3.x or compress). "Compact, locally contractible, non-empty, proper subspace": say which hypothesis of [Hat02, 3.44] each clause serves. H̃_{−1} of a non-empty space is a convention issue, so it may be cleaner to avoid it.
- **L559** [notation] ∇^{Y,Z}_X: rename to the median, as discussed above.
- **L570–579** [structure] State the general form of (5) only.
- **L596** [phrasing] "elementary set theory exercise which we leave for the reader to check" → "elementary and left to the reader".
- **L626** [phrasing] "Every edge in the Hasse graph … changes an order ideal by exactly one element" is fine. [structure] The two-step path construction could use one diagram sentence.

### Sections 2.5–2.6 (lattices, examples, strict upsets)

- **L635–652** [notation] The proof uses `\underline{\Rightarrow}` and `\underline{\Leftarrow}`; plain (⇒), (⇐) is more standard.
- **L658** [notation] "Σ_P" → "Σ_{𝒥(P)}".
- **L659** [notation] "𝒥(P) = {∅ ⊂ (∗)}" is odd. Write {∅ ⊂ {∗}}.
- **L670–671** [notation] "Σ_{J(P)}" and "J(P)" without calligraphic J; "Q_2" clashes with Q_G. Use "□" or "C_2 × C_2" for the square.
- **L677** [phrasing] "deduce self-injective of Σ" → "deduce that Σ is self-injective".
- **L714** [typo] "strictly larger than Z" → "than Z̲".
- **L718** [phrasing] "which means that it is a subcomplex of Δ_X" is a non sequitur; replace "which means that" with "and".
- **L720** [notation] The label `subsec:eg1` is for an example, so the label name is misleading (cosmetic). The same applies to `subsec:eg2`, `subsec:eg3`.
- **L744** [typo] "Δ_X^{\underline{Z}}" (missing ">"). "Hasse diagram of Δ" should be "Hasse diagram of 𝒟".
- **L748–768** [notation] The table is indexed by Z, but the conclusions at lines 761–767 are indexed by Z̲ (e.g. "H̃_0(Δ^{>3̲}_{[1]})"). Index both consistently, or add a column Z̲. The notation {∅̲} in the rows Z = [3], [123] looks like the minimal element ∅̲ = X̲ of 𝒟_X, not the complex {∅}. Write "{∅}" and say it is the complex with only the empty face.

### Section 3 (the strict-chain resolution)

- **L777** [notation] "A-module" is used before A is introduced.
- **L786, L795** [notation] Three notations coexist for the same object: Δ(𝒟_X)_k, Δ_{X,k} and (implicitly) Δ_X,k. Pick one. At line 795, "projective A-module P_Z over all k-chains" should read P_{Z_0} and "modules".
- **L788** [phrasing] "for a strict chain and it is understood that …" → "for a strict chain, where Z_i denotes …".
- **L798** [typo] The (k−1)-simplex Z̲_*^{\hat 0} lies in Δ^{>Z̲_0}, not Δ^{>Z̲}.
- **L809** [typo] "by by left-multiplying".
- **L857** [phrasing] "On the other hand, if i=0, then the case when and j>1 implies that" is garbled. Say "if i = 0 and j > 1, both sides are induced by μ_{Z_1,Z_0}".
- **L820–860** [cut] See General comment (e). Prop. 3.1 and Prop. A.1 are the same argument.
- **L884** [typo] "represeting".
- **L886–979** [structure] The first figure is about 14 cm tall and carries many labels. Consider reducing it, or splitting the colours into two panels. Cross-check line 1634, which says "blue" but the figure uses cyan.
- **L995** [phrasing] "The main theorem we want to show" clashes with "Main Theorem" in the introduction. Say "The key technical result".
- **L1000 and L1002** [structure] Two consecutive paragraphs say the same thing. Merge.
- **L1004–1019** [structure] See General comment 3.4. Also the proof's first case (P ∖ X ∈ 𝒥(P)) is needed in both Cor. 3.x and Prop. 3.x. Do it once.
- **L1021–1023** [structure] The remark on join-irreducibles would sit better in the introduction.
- **L1033–1040** [typo] The lemma uses (U,V,W), but the proof uses Z̲, Ȳ. The equivalences refer to the wrong variables. Rewrite with U, V, W.
- **L1071–1145** [cut] This is the longest proof of the section. "Comparing this with the expansion of h_{k−1}d_k yields" (line 1133) hides the verification. Say that h is the order-homotopy of Lemma 2.7 for r_W ≤ id with coefficient maps, and isolate the one identity b_{Z_iT_i}b_{T_iW} = b_{Z_iW} that makes the coefficients behave. Lines 1139–1144 (deducing that ρ is a chain map from d(id − ιρ) = (id − ιρ)d) could be replaced by a direct remark that ρ is the map induced by an order-preserving map and so commutes with d.
- **L1162** [phrasing] "(Z̲_1 ∖ Y̲) ∩ W̲ ≠ ∅" is immediate from Y̲ < Z̲_1 ≤ W̲. Say so in one clause.
- **L1174–1180** [notation] The shift [1] and the sign conventions are used here without comment (the sign check is commented out at line 1181). The same convention is re-introduced at line 1432 with an extra sign, ∂^Z_k = −∂_{k−1}. Set the convention once in §2.3.
- **L1293** [typo] "C_{|P|−3}(Δ^{>Z̲})" should be Δ^{>X̲}.
- **L1328** [phrasing] "we can truncate the resolution by one more term" needs one more sentence: the cokernel of a split mono is a direct summand of P_{|P|−2}, hence projective.
- **L1332–1334** [content] "The bound … is optimal" overclaims. The cited example has |P| = 3 only. Say "attained for |P| = 3" or prove it for all |P| (check). The remark also duplicates line 1760. Keep one.

### Section 4 (Morse theory)

- **L1344** [phrasing] "special gadget" and "homotopic" (→ "homotopy equivalent"). "This usage of algebraic Morse theory we use follows" → "Our use of algebraic Morse theory follows [CLZ26, §3]".
- **L1346–1383, L1385–1390** [structure] Definition 4.1(5) and Prop. 4.2 handle infinite zigzag paths, which never occur here, since all complexes are finite. State the definition in the finite case ("a partial matching such that Q^𝓜 has no oriented cycle"), or say once that finiteness makes the local finiteness automatic. That cuts about 15 lines.
- **L1365** [content] "thick and dotted arrows alternate": "thick" is not defined, because the item defining it is commented out (lines 1358–1360). Say "unmatched" or restore the definition.
- **L1424–1426** [phrasing] "while those of δ is induced" → "are induced"; "every matrix component arising from δ are still radical maps" → "is". The "solution" paragraph (lines 1426–1428) claims this is "what usual homological perturbation theory does", which is a stretch. Say "as in the perturbation lemma".
- **L1436 and L1455** [notation] Two meanings of ∂_k in 20 lines: simplicial boundary versus "internal part of d_k". Rename the latter (d^{int}_k) and the other part (d^{ext}_k), or use μ-notation for δ.
- **L1460** [content] `\new{Note that .}`: unfinished. **L1462–1463**: `\old{…}` and `\comment{…}` leftovers; delete.
- **L1465–1477** [phrasing] The display with a braced `cases` followed by "for all k ≥ 1" is hard to read. List the three conditions below the display.
- **L1500** [typo] "for all Z ∈ 𝒫" should be Z ∈ 𝒥(P).
- **L1525** [phrasing] "it follows from Proposition … that showing 𝓜 has no infinite zigzag path will suffice" → "by Proposition …, it suffices to show that …".
- **L1555** [phrasing] "the sum is finite because Q^𝓜 is finite and its zigzag paths have bounded length" repeats line 1541. One mention suffices.
- **L1560–1564** [structure] This remark is standard and could sit before Cor. 4.6.
- **L1566–1585** [content] Cor. 4.6 is labelled "IG" but states only a per-X pdim formula. Add the displayed formula idim Σ = max_X pdim I_X = max{k : H̃_{k−1}(Δ^{>Z̲}) ≠ 0 for some X, Z}, since line 56 claims it. "Σ_L" is used but L is undefined in this section; write Σ_{𝒥(P)}. "(1) k = |P|" should be "k ≥ |P|".
- **L1584** [typo] "vansihing".
- **L1589** [typo] "indecmposable".
- **L1634** [phrasing] A very long paragraph. Split into (i) which arrows are matched, (ii) the change of basis, (iii) the critical summands. "Blue" versus the cyan in Figure 1 (see line 886).
- **L1763–1779** [structure] See General comment 3.1. The motivation (lines 1771–1779) is rambling and informal. Replace it by "Let 𝒮_X be the simplicial complex generated by 𝒟_X, i.e. the set of all subsets of members of 𝒟_X". The reader needs only the definition, the statement, and a one-sentence reason (D_X is closed under intersection).
- **L1765–1767** [notation] "for some Z ∈ L": L is undefined here. It should read 𝒥(P). Also "pdim_A" at line 1784.
- **L1771** [phrasing] "striking resemblance" → "agrees with". "it is an application (Lemma …) of a more well-known Hochster's formula" is ungrammatical.
- **L1775** [typo] "thoerem". **L1779** [phrasing] "which feels very close to what Δ^{>Z̲} describes" → delete.
- **L1777** [notation] 𝒮_X, S_K, S_Z, S ⊆ P: four uses of S.
- **L1802** [typo] "the we have an order ideal".
- **L1821–1823, L1827–1830** [notation] The poset "(Z̲, 1̂]" is not defined; it is 𝒟_X^{>Z̲}. "F ⊆ j_Zc_Z" is missing its argument: it should read F ⊆ j_Zc_Z(F). "Now applies Lemma … and get that" → "Lemma … now gives".
- **L1833** [typo] "Δ(𝓕(𝒮_X)_{\underline{Z}})" is missing ">".
- **L1883–1893** [cut] The proof of Lemma 4.14 (Hochster's formula in local-cohomology form) is a chain of equalities whose last step silently identifies F with the support of the multidegree and re-indexes. Either cite the exact statement in [HH11] or add a sentence on this identification. The lemma itself is standard, so a citation plus two sentences would do. The label is also misspelt (`lem:Hochshster easier`; cosmetic).

### Section 5 (multiplicities)

- **L1913** [phrasing] Section title: see General comment 3.7.
- **L1916–1920** [structure] Leftover `\old{…}\comment{…}\xnew{moved to Section 2}`. Delete.
- **L1928** [phrasing] "we see some possible behavior exhibit by these multiplicities" → "we exhibit some possible behaviours of these multiplicities".
- **L1931** [phrasing] "Multiplicity-free in degree zero and one" → "Degrees zero and one".
- **L1947** [content] "the 1-skeleton … is just the point ∅": the complex {∅} has no vertices. Also the formula "β = #components − 1" needs the empty case treated separately, which is done here but confusingly.
- **L1957–1963** [cut] Case (b) is dual to case (a). Complementation Y ↦ P ∖ Y preserves X ⊕ Z, exchanges ⊆ and ⊇, and sends 𝒥(P) to 𝒥(P^op), so (b) for (P,X) is (a) for (P^op, P∖X). Say so and delete seven lines (the duality should be checked).
- **L1977** [typo] "arbitrary large" → "arbitrarily large".
- **L1979–1986** [content] "Specifying such a B is equivalent to specifying a height-two poset" is not quite true. Isolated vertices in Y become minimal elements, so the correspondence is not a bijection. You need only the direction B ↦ P_B. [notation] X, Y here collide with the order ideal X (the choice is deliberate: X is the set of minimal elements) and the Y of §5.1. Rename the bipartition.
- **L1991–1996** [typo] "[𝒫_min,k : P_X] = β_{X,k} = H̃_{k−1}(Δ^{>X̲})": the last two are not equal (a number versus a vector space). Write dim H̃.
- **L2002** [typo] "y ∈ U ∩ y" should be "U ∩ Y".
- **L2011** [phrasing] "reduced homology of dimension greater than one" → "some reduced homology group of dimension at least 2".
- **L2013** [phrasing] "Consider a bipartition B of C_6 ⊔ K_2" → "Let B be the bipartite graph C_6 ⊔ K_2 with parts …".
- **L2100–2118** [content, check] **Possible off-by-one.** By Prop. 5.2, [𝒫_min,j : P_X] = dim H̃_{j−1}(Ind B). Nagel–Reiner gives Ind(B_K) ≃ ΣK. With K = ⋁_m S^{k−1}, we get ΣK = ⋁_m S^k, with H̃_k of dimension m. That gives multiplicity m in degree **k+1**, not k. This matches the concrete example (S²∨S² gives degree 3, line 2095). To obtain degree k, one needs K = ⋁_m S^{k−2} (for k = 2, K is m+1 points). Please recheck both Example 5.4 ("for m ≥ 1 and k ≥ 2, K = ⋁ S^{k−1}") and the proof of the Corollary. Also, "Example" at line 2100 is really a remark.

### Appendix

- **L2125** [typo] "economoical". [content] "For some modules, this construction always gives a complex of projectives, although the complex need not be exact": the complex of projectives exists for every thin module of the type described. Say "For every such thin module this gives a complex of projectives, exact at degree 0 only under an additional condition (see below)".
- **L2127** [notation] "for every i ∈ Q_0" → x. The indices x_k and i_k are mixed in lines 2175, 2178–2181 and 2218 (leftover renaming).
- **L2139** [phrasing] The acyclicity of Q_M could be one sentence. It is used only to say that C_M has no non-identity isomorphisms (line 2318).
- **L2150–2152** [notation] 𝒞_M(y,x) is defined with μ_p : P_y → P_x for p : x → y, so a morphism x_0 → x_1 in a string corresponds to a path x_1 ⇝ x_0 in Q_M. Spell this out, or define 𝒞_M with the direction reversed.
- **L2164** [content] The colimit display is inconsistent with the definition of μ_p. It sums over "m ∈ P_x" and writes "(m − mp)A", i.e. a right action by p. With μ_p : P_y → P_x given by left multiplication, the relation should be ι_y(m) ∼ ι_x(pm) for m ∈ P_y (check).
- **L2175, L2178–2181** [typo] "deleting i_r": should be x_r. "F_M(i_0)": should be F_M(x_0).
- **L2194–2203** [content] Prop. A.1 asserts that the complex is "exact at 𝒫_0(M) when M is faithful". The proof (lines 2205–2225) shows only that it is a complex. The faithfulness claim is not proved, and it is not the relevant condition. Exactness at 𝒫_0 means colim F_M → M is an isomorphism (as the display at line 2164 shows). For M = I_X, which is not faithful in general (see the commented note at line 2229), exactness holds anyway by Theorem 3.2. Either justify the claim, replace it by "exact at 𝒫_0 iff colim F_M → M is an isomorphism", or drop it.
- **L2206** [typo] "the homomorphism defines analogous to" → "defined analogously to". **L2218**: "the the".
- **L2205–2225** [cut] See the table in General comment 2. Replace by "as in Prop. 3.1".
- **L2227–2230** [structure] This example is the link to the body of the paper. Move its content to the start of Section 3.1.
- **L2232–2234** [cut] The simple-module example can be a single sentence. "This shows a non-resolution 𝒫_•" is not meaningful; say "so in general 𝒫_• is not exact".
- **L2236** [phrasing] "the proof we shown here is specialized case of the reason exactly the reason why the simplicial bar construction yields a complex" is garbled. Rewrite: "this does not give an independent proof of Prop. A.1; it is the same argument".
- **L2238–2256** [cut] The table. The row G = ∗ and the footnote on simplicial tensoring serve no purpose, since G is a point.
- **L2265** [notation] "x ∈ 𝒞_M = Q_M": 𝒞_M is the path category of Q_M, so only the object sets agree.
- **L2267** [notation] "d_0 → d_1 → … → d_k" uses d_j for objects, while d_0, d_k denote differentials elsewhere. Also 𝒟 versus 𝒟_X (lines 2243, 2267).
- **L2280–2292** [notation] Three symbols for faces: ∂^{(r)}_k, ε_r and (in the proof at line 2206) ε_i. The proof also writes "0 < r < n" at line 2286 where k is meant.
- **L2294–2326** [cut] The degeneracy identities and normalisation are textbook (Moore complex). Cite.
- **L2328–2337** [phrasing] "this will not be the case" is ambiguous. State the positive claim: for M = I_X, colim F = I_X and L_k colim F = 0 for k > 0. Promote it to the first paragraph of the appendix.

---

## Part III. Suggested order of work

1. Strip the editing macros, fix the broken references, typos and index slips (all items tagged [typo] and [content] above). The two items to check mathematically are L2100–2118 (off-by-one) and L2164 (direction of the relation).
2. Rewrite the abstract and Main Theorems 1–2 (formula for the resolution; self-injective dimension; regularity; merge items (2) and (3)).
3. Move the "why it works" paragraph (bar construction of 𝒟_X) into Section 3.1, then shrink the appendix to about 70–80 lines as outlined.
4. Move the regularity subsection and its tools to the end, or to a second appendix.
5. Rename the colliding symbols: Σ/A, ∂/δ, S, X/Y in §5.2, 𝓜, and the median ∇.
6. Optional: replace the underline notation by the geodesic order ⪯_X.

I estimate steps 3–4 and the Part I.3 items together would shorten the paper by 15–20%. They also take the new material from about line 770 to about line 400.
