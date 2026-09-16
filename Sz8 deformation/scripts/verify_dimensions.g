# One-shot verification of the two presentations.

Read("scripts/build_global.g");
Read("scripts/build_local_from_group.g");

if Dimension(A) <> 1192 then
    Error("global dimension check failed");
fi;
if Dimension(B) <> 448 then
    Error("local dimension check failed");
fi;

Print("dimension checks passed\n");
