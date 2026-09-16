# Build the local correspondent B_0(kN), N = 2^(3+3):7, directly from its
# group structure.  Over GF(8), kN is split and basic: N has a normal Sylow
# 2-subgroup and quotient C7, so its seven simples are one-dimensional.
#
# This script deliberately lets QPA choose a valid quiver-with-relations
# presentation via AlgebraAsQuiverAlgebra.  The returned relation list is
# basis-dependent, while the resulting algebra is canonical up to isomorphism.

LoadPackage("qpa");

q := 8;
F := GF(q);
ff := Elements(F);

# Suzuki 2-group A(3,4): (a,b)(c,d)=(a+c,b+d+a*c^4).
PairIndex := function(a,b)
    return (Position(ff,a)-1)*q + Position(ff,b);
end;

PairProduct := function(x,y)
    return [ x[1]+y[1], x[2]+y[2]+x[1]*y[1]^4 ];
end;

pairs := [];
for a in ff do
    for b in ff do
        Add(pairs, [a,b]);
    od;
od;

# Left regular permutations of P on its 64 elements.
LeftRegular := function(g)
    return PermList(List(pairs, x -> PairIndex(
        PairProduct(g,x)[1], PairProduct(g,x)[2])));
end;

P_generators := List(pairs, LeftRegular);
P := Group(P_generators);

# The complement C7 acts by (a,b) |-> (lambda*a, lambda^5*b).
lambda := PrimitiveElement(F);
T := PermList(List(pairs, x -> PairIndex(lambda*x[1], lambda^5*x[2])));
N := Group(Concatenation(P_generators, [T]));

if Size(P) <> 64 then Error("constructed P has wrong order"); fi;
if Size(N) <> 448 then Error("constructed N has wrong order"); fi;

kN := GroupAlgebra(F, N);
blocks := BlocksOfAlgebra(kN);
if Length(blocks) <> 1 then Error("N should have one principal block"); fi;
Braw := blocks[1];

Print("local: |P| = ", Size(P), ", |N| = ", Size(N), "\n");
Print("local: group-algebra dimension = ", Dimension(Braw), "\n");
Print("local: basic = ", IsBasicAlgebra(Braw), "\n");

local_data := AlgebraAsQuiverAlgebra(Braw);
B := local_data[1];
local_images := local_data[2];

Print("local: QPA dimension = ", Dimension(B), "\n");
Print("local: vertices = ", Length(VerticesOfQuiver(QuiverOfPathAlgebra(
    OriginalPathAlgebra(B)))), "\n");
Print("local: arrows = ", Length(ArrowsOfQuiver(QuiverOfPathAlgebra(
    OriginalPathAlgebra(B)))), "\n");
Print("local: finite dimensional = ", IsFiniteDimensional(B), "\n");
Print("local: self-injective = ", IsSelfinjectiveAlgebra(B), "\n");
Print("local: symmetric = ", IsSymmetricAlgebra(B), "\n");

SaveAlgebra(B, "results/local_principal_GF8.qpa", "delete");
