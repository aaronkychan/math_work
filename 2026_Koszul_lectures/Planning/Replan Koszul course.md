### Goals of the Course

Many rings come with a hidden partner (dual), associated to the same data but with structure mirrors the original in some way.  One of the most famous such duality is the Koszul duality. This course develops the tools needed to recognize and construct this duality from ordinary rings and module theory, and their homological algebra.  We will see how the quadratic dual of a Koszul algebra coincides the Yoneda algebra - ring that encodes the extensions of simple modules.  Amongst the many beautiful consequences of this duality theory, we will focus on the BGG correspondence, which roughly relates the graded modules a Koszul algebra to the graded modules over its dual.
### Objectives of the Course

By the end of the course, students should be able to:

1. Confidently work with duality over semisimple algebras for modules over non-commutative graded rings.
2. Define quadratic and Koszul algebras, construct quadratic duals, and verify Koszulness using the Hilbert series criterion.
3. Construct minimal graded free/projective resolutions and the classical Koszul complex directly.
4. Compute the Ext-groups between simple modules and the Yoneda algebra of a graded algebra.

### Suggested Reference Texts for Students

1. **A. Polishchuk, L. Positselski**, _Quadratic Algebras_, AMS University Lecture Series 37 (2005).  
    Primary course reference throughout.
2. **A. Beilinson, V. Ginzburg, W. Soergel, "Koszul duality patterns in representation theory,"**  J. Amer. Math. Soc.  9 (1996), 473–527.  
    Section 2 gives a self-contained, purely ring-theoretic account of Koszul rings, quadratic duals, the Ext-algebra, and the numerical criterion (usable alongside Positselski–Polishchuk for Lectures 3–8); the paper as a whole is the natural source for the BGG-correspondence capstone in Lectures 9–11.
3. **R. Martínez-Villa, "Introduction to Koszul Algebras,"** Revista de la Unión Matemática Argentina 48 (2007), no. 2, 67–95

---

### Lecture-by-Lecture Plan (11 × 90 min)

**Lecture 1 — Graded Rings and Modules.**  
* Graded algebras and graded modules over a field; 
* homogeneous ideals and quotients; 
* Hilbert series and basic operations on them (sums, products, shifts); first examples (polynomial ring, exterior algebra, tensor algebra).
* Graded duals, duals over semisimple rings.

**Lecture 2 — Tensor and Quadratic Algebras.**  
* Tensor algebra
* Algebras generated in degree 1 with relations in degree 2; 
* the space of quadratic relations; 
* quadratic algebras as the natural class for the theory; 
* examples and immediate non-examples.

**Lecture 3 — The Quadratic Dual (revised examples).** 
* Construction of the quadratic dual algebra; 
* duality is an involution; 
* behavior of quadratic duals under direct sum and tensor product of algebras; 
* computing duals in examples:  
	* $T(V)$ versus $T(V)/(V^{\otimes 2})$ 
	* $S(V)$ versus $\bigwedge V$ 
	* monomial quadratic algebras

**Lecture 4 — Minimal Graded Free Resolutions.**  
* Graded free modules and projective modules
* existence and uniqueness of minimal resolutions (graded Nakayama argument); 
* graded Betti numbers; 
* worked resolutions over the polynomial ring and the exterior algebra.

**Lecture 5 —  Koszul complex and Koszul algebras**
* Explicit construction of the Koszul complex resolving the trivial module over the polynomial ring, using the exterior algebra as coefficients; direct verification of exactness by hand.
* Koszul algebras defined as quadratic algebras whose trivial module admits a linear minimal graded free resolution; 

**Lecture 6 — Tor and Ext (computational viewpoint)**
- Define Tor, Ext via resolutions
- reformulation of Koszulness as $ext^i(S,S(j))=0$ for all $i\neq j$.
- example

**Lecture 7 — The Ext-Algebra and Koszul Duality.**  
* The Ext-algebra of the trivial module as a graded algebra (Yoneda product); 
* theorem identifying the Ext-algebra of a Koszul algebra with its quadratic dual; 
* consequences for computing quadratic duals via Ext.

**Lecture 8 — Hilbert Series Criterion and Further Examples.**  
* The numerical (Hilbert series) necessary condition for Koszulness, derived directly from the linear resolution; use as a quick obstruction test; 
* further worked algebraic examples: monomial quadratic algebras (continued from Lecture 4) and their resolutions computed directly by hand; 
* direct sums and tensor products of known Koszul algebras; 
* quadratic algebras $A$ with $h_{A^!}(-t)h_A(t)=1$ but not Koszul  ($h_{E}(-t)h_A(t)\neq 1$)

**Lecture 9 — Grmod A vs LC(A)**  
* Review of basic category theory: category, functor, equivalences.
* For Koszul algebra, show that the category of graded modules of $A^!$ is equivalence to the category of linear complexes $A$

**Lecture 10 — BGG correspondence qgr(A) and stmod(A^!)**  
* Graded modules over the polynomial ring modulo finite-length (torsion) modules; 
* the resulting quotient category qgr;
* Graded modules over the exterior algebra; 
* projective modules and the stable module category (modules modulo projectives)

**Lecture 11 — Left over remarks (optional)**  
* Some remarks about BGG correspondence being consequence of graded derived equivalence.
* Remarks about methods in verifying Koszulness (e.g. Grobner/PBW basis)

---

### Content of course 
Part I — Graded Algebra and Quadratic Duality (Lectures 1–3)

Graded rings and modules, Hilbert series, tensor algebras.
Quadratic algebras as tensor algebras with relations concentrated in degree 2, and construction of the quadratic dual, computed by hand in worked examples.

Part II — Resolutions, the Koszul Complex, Koszul algebra and Yoneda algebra (Lectures 4–8)

Minimal graded resolutions, Koszul complex, leading to the definition of a Koszul algebra.
Tor, Ext, and the Yoneda algebra and identification with the quadratic dual for Koszul algebras; the Hilbert series identity for Koszulness test.

Part III — Koszul Duality and the BGG Correspondence (Lectures 9–11)

Basic categorical language. Equivalence between graded modules over the quadratic dual and linear complexes over the original algebra.  The BGG correspondence between the quotient category qgr over the polynomial ring and the stable module category over the exterior algebra.