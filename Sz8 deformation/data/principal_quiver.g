# Quiver for the basic algebra of the principal 2-block of Sz(8).
#
# Vertex convention (Koshita, Theorem 1):
#   1 = V_empty, 2 = V_(0), 3 = V_(1), 4 = V_(2),
#   5 = V_(1,2), 6 = V_(0,2), 7 = V_(0,1).
#
# QPA writes a path in the order in which its arrows are traversed.
# Thus D*A means first D and then A, matching the dot notation in the paper.

Q_A := Quiver(7, [
    [1,2,"A"], [1,3,"B"], [1,4,"C"],
    [2,1,"D"], [3,1,"F"], [4,1,"G"],
    [3,7,"H"], [4,5,"I"], [2,6,"J"],
    [7,3,"K"], [5,4,"L"], [6,2,"M"]
]);
