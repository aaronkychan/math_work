# Build and baseline-check the basic algebra of the principal 2-block of
# k Sz(8), using Koshita's quiver and relations.

LoadPackage("qpa");
Read("data/principal_quiver.g");
Read("data/relations_A.g");

F := GF(2);
FQ_A := PathAlgebra(F, Q_A);
relations_A := PrincipalRelations(FQ_A);
A := FQ_A / relations_A;

Print("global: finite dimensional = ", IsFiniteDimensional(A), "\n");
Print("global: dimension = ", Dimension(A), "\n");
Print("global: Loewy length = ", LoewyLength(A), "\n");
Print("global: self-injective = ", IsSelfinjectiveAlgebra(A), "\n");
Print("global: symmetric = ", IsSymmetricAlgebra(A), "\n");

# Koshita's presentation has 1192 canonical paths over an algebraically
# closed field.  Over GF(2), this is a useful normalization check as well.
Print("global: Groebner generators = ",
      Length(GroebnerBasisOfIdeal(Ideal(FQ_A, relations_A))), "\n");

SaveAlgebra(A, "results/global_principal_GF2.qpa", "delete");
