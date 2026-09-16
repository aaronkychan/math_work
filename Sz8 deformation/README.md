# Sz(8) principal-block QPA input

This directory contains the first computational milestone from `plan.md`:

* `data/principal_quiver.g` and `data/relations_A.g` give the 7-simple basic
  algebra of the global principal block (B_0(k\mathrm{Sz}(8))), transcribed
  from Koshita's Theorem 1.
* `scripts/build_global.g` constructs and baseline-checks that quotient.
* `scripts/build_local_from_group.g` constructs the local correspondent
  (B_0(kN)), where (N=N_{\mathrm{Sz}(8)}(P)\cong 2^{3+3}:7), over GF(8),
  and asks QPA to produce an isomorphic quiver algebra and its relations.
* `data/local_quiver.g` records the expected 7-vertex Gabriel-quiver
  skeleton: three arrow families with weights 1, 2, and 4 modulo 7.
* `scripts/build_all.g` is the one-command entry point.

## Run

From the project root in GAP:

```gap
Read("scripts/build_global.g");
Read("scripts/build_local_from_group.g");
```

The generated QPA presentations are saved under `results/`.  QPA's
`AlgebraAsQuiverAlgebra` output for the local algebra is intentionally used
as the source of truth for the local relation list: relation generators depend
on the chosen basis, while the finite-dimensional algebra does not.

The global baseline should return dimension 1192, matching the 1192-path basis
reported by Koshita.  The local group algebra has dimension 448.

The local construction uses the standard Suzuki 2-group law

\[
(a,b)(c,d)=(a+c,\,b+d+a c^4), \qquad a,b,c,d\in\mathbb F_8,
\]

and the order-7 automorphism `(a,b) -> (lambda*a,lambda^5*b)`.
