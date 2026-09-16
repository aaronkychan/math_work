# Koshita, "An example of relations on the Ext-quiver for the Suzuki
# group Sz(8) in characteristic 2", Theorem 1.
#
# The source works over an algebraically closed field of characteristic 2.
# All displayed plus signs are therefore addition in characteristic 2.
# This function expects a path algebra PA whose generators are named as in
# data/principal_quiver.g.

PrincipalRelations := function(PA)
    local A,B,C,D,F,G,H,I,J,K,L,M;
    local alpha1,alpha2,alpha3,alpha4,alpha5,alpha6;
    local alpha7,alpha8,alpha9,alpha10,alpha11,alpha12;
    local alpha13,alpha14,alpha15,alpha16,alpha17,alpha18;
    local alpha19,alpha20,alpha21,beta1,beta2,beta3;
    local alpha22,alpha23;

    A := PA.A;  B := PA.B;  C := PA.C;  D := PA.D;
    F := PA.F;  G := PA.G;  H := PA.H;  I := PA.I;
    J := PA.J;  K := PA.K;  L := PA.L;  M := PA.M;

    alpha1 := D*A;
    alpha2 := F*B;
    alpha3 := G*C;
    alpha4 := K*H;
    alpha5 := L*I;
    alpha6 := M*J;

    alpha7  := D*B*H;
    alpha8  := F*C*I;
    alpha9  := G*A*J;
    alpha10 := K*F*A;
    alpha11 := L*G*B;
    alpha12 := M*D*C;

    alpha13 := K*F*C*G*B*H;
    alpha14 := L*G*A*D*C*I;
    alpha15 := M*D*B*F*A*J;

    alpha16 := D*C*G*A
              + D*B*F*A*J*M
              + J*M*D*B*F*A;

    alpha17 := F*A*D*B
              + F*C*G*B*H*K
              + H*K*F*C*G*B;

    alpha18 := G*B*F*C
              + G*A*D*C*I*L
              + I*L*G*A*D*C;

    alpha19 := D*B*F*C*G*A
              + D*C*G*B*F*A
              + D*B*F*A*D*B*F*C*G*A
              + D*B*F*A*D*C*I*L*G*A
              + D*B*F*C*G*A*D*B*F*A
              + D*C*G*A*D*B*F*C*G*A
              + D*C*G*B*H*K*F*C*G*A
              + D*C*I*L*G*A*D*B*F*A
              + D*B*F*A*D*C*G*B*F*C*G*A;

    alpha20 := F*C*G*A*D*B
              + F*A*D*C*G*B
              + F*C*G*B*F*C*G*A*D*B
              + F*C*G*B*F*A*J*M*D*B
              + F*C*G*A*D*B*F*C*G*B
              + F*A*D*B*F*C*G*A*D*B
              + F*A*D*C*I*L*G*A*D*B
              + F*A*J*M*D*B*F*C*G*B
              + F*C*G*B*F*A*D*C*G*A*D*B;

    alpha21 := G*A*D*B*F*C
              + G*B*F*A*D*C
              + G*A*D*C*G*A*D*B*F*C
              + G*A*D*C*G*B*H*K*F*C
              + G*A*D*B*F*C*G*A*D*C
              + G*B*F*C*G*A*D*B*F*C
              + G*B*F*A*J*M*D*B*F*C
              + G*B*H*K*F*C*G*A*D*C
              + G*A*D*C*G*B*F*A*D*B*F*C;

    beta1 := A*D*B*F*C*G
            + C*G*B*F*A*D
            + A*D*C*G*B*H*K*F*C*G
            + B*H*K*F*C*G*A*D*C*G
            + C*G*A*D*C*G*B*H*K*F
            + C*G*B*H*K*F*C*G*A*D
            + A*J*M*D*B*F*A*D*B*F*C*G
            + C*G*B*F*A*D*B*F*A*J*M*D
            + A*D*B*F*A*D*C*G*A*D*C*I*L*G
            + C*G*A*D*C*I*L*G*A*D*B*F*A*D
            + C*G*A*D*C*I*L*G*A*D*B*F*C*G*A*D;

    beta2 := B*F*C*G*A*D
            + A*D*C*G*B*F
            + B*F*A*D*C*I*L*G*A*D
            + C*I*L*G*A*D*B*F*A*D
            + A*D*B*F*A*D*C*I*L*G
            + A*D*C*I*L*G*A*D*B*F
            + B*H*K*F*C*G*B*F*C*G*A*D
            + A*D*C*G*B*F*C*G*B*H*K*F
            + B*F*C*G*B*F*A*D*B*F*A*J*M*D
            + A*D*B*F*A*J*M*D*B*F*C*G*B*F
            + A*D*B*F*A*J*M*D*B*F*C*G*A*D*B*F;

    beta3 := C*G*A*D*B*F
            + B*F*A*D*C*G
            + C*G*B*F*A*J*M*D*B*F
            + A*J*M*D*B*F*C*G*B*F
            + B*F*C*G*B*F*A*J*M*D
            + B*F*A*J*M*D*B*F*C*G
            + C*I*L*G*A*D*C*G*A*D*B*F
            + B*F*A*D*C*G*A*D*C*I*L*G
            + C*G*A*D*C*G*B*F*C*G*B*H*K*F
            + B*F*C*G*B*H*K*F*C*G*A*D*C*G
            + B*F*C*G*B*H*K*F*C*G*A*D*B*F*C*G;

    alpha22 := beta1 + beta2;
    alpha23 := beta2 + beta3;

    return [ alpha1, alpha2, alpha3, alpha4, alpha5, alpha6,
             alpha7, alpha8, alpha9, alpha10, alpha11, alpha12,
             alpha13, alpha14, alpha15, alpha16, alpha17, alpha18,
             alpha19, alpha20, alpha21, alpha22, alpha23 ];
end;
