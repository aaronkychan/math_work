#!/usr/bin/env python3
"""Exact tests of standard/costandard candidates for graded tree path algebras.

All algebras have zero differential. Arrow degrees lie in {0, -1, -2}.
Every orientation and every vertex order are tested. Modules are right modules;
the path (v0,...,vl) starts at v0. The order gives increasing ranks.

Delta_v is the quotient of e_v A spanned by paths all of whose vertices have
rank at most rank(v). Nabla_v is the submodule of D(A e_v) with the same path
restriction, and its basis paths END at v. Right action on Delta appends a
path; right action on Nabla removes a matching path prefix.

For Delta_v, the projective resolution has P_v in degree 0 and one generator
of degree deg(p)-1 for each first-hit path p into a later vertex. Its
differential sends that generator to p. The script constructs Hom complexes
from this resolution to each target module and computes their differential
ranks over Q. Thus the graded Euler characteristic alone is never used as a
substitute for computing derived Hom.

The result is a finite computation, not a proof for arbitrary arrow degrees.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


def matrix_rank(matrix: list[list[int]]) -> int:
    """Exact Gaussian elimination over Q; matrices in this test are tiny."""
    if not matrix or not matrix[0]:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot = 0
    for col in range(cols):
        candidate = next((r for r in range(pivot, rows) if a[r][col]), None)
        if candidate is None:
            continue
        a[pivot], a[candidate] = a[candidate], a[pivot]
        scale = a[pivot][col]
        a[pivot] = [x / scale for x in a[pivot]]
        for row in range(pivot + 1, rows):
            if a[row][col]:
                factor = a[row][col]
                a[row] = [x - factor * y for x, y in zip(a[row], a[pivot])]
        pivot += 1
        if pivot == rows:
            break
    return pivot


class PathAlgebra:
    def __init__(self, n: int, arrows: tuple[tuple[int, int, int], ...]):
        self.n = n
        self.arrows = arrows
        self.arrow_degree = {(u, v): d for u, v, d in arrows}
        outgoing: dict[int, list[int]] = defaultdict(list)
        for u, v, _ in arrows:
            outgoing[u].append(v)
        self.paths: list[tuple[int, ...]] = []

        def extend(path: tuple[int, ...]) -> None:
            self.paths.append(path)
            for w in outgoing[path[-1]]:
                assert w not in path, "The input must be acyclic."
                extend(path + (w,))

        for v in range(n):
            extend((v,))
        self.degree = {
            p: sum(self.arrow_degree[edge] for edge in zip(p, p[1:]))
            for p in self.paths
        }
        self.start = {v: [p for p in self.paths if p[0] == v] for v in range(n)}
        self.end = {v: [p for p in self.paths if p[-1] == v] for v in range(n)}
        self.m = 1 - min(self.degree.values())


class Module:
    def __init__(self, algebra: PathAlgebra, vertex: int, ranks: dict[int, int],
                 kind: str):
        self.algebra = algebra
        self.kind = kind
        candidates = algebra.start[vertex] if kind == "standard" else algebra.end[vertex]
        self.basis = tuple(p for p in candidates
                           if all(ranks[u] <= ranks[vertex] for u in p))
        self.basis_set = set(self.basis)
        self.anchor = {p: p[-1] if kind == "standard" else p[0] for p in self.basis}
        self.degree = {p: algebra.degree[p] * (1 if kind == "standard" else -1)
                       for p in self.basis}

    def action(self, basis_path: tuple[int, ...], path: tuple[int, ...]):
        if self.anchor[basis_path] != path[0]:
            return None
        if self.kind == "standard":
            result = basis_path + path[1:]
            return result if result in self.basis_set else None
        if basis_path[:len(path)] != path:
            return None
        result = basis_path[len(path) - 1:]
        assert result in self.basis_set, "The proposed costandard is not a submodule."
        return result


def check_module(module: Module) -> None:
    """Verify unit, degree, and associativity directly on the path basis."""
    algebra = module.algebra
    for basis_path in module.basis:
        assert module.action(basis_path, (module.anchor[basis_path],)) == basis_path
        for p in algebra.paths:
            image = module.action(basis_path, p)
            if image is not None:
                assert module.degree[image] == module.degree[basis_path] + algebra.degree[p]
            for q in algebra.start[p[-1]]:
                pq = p + q[1:]
                twice = None if image is None else module.action(image, q)
                assert twice == module.action(basis_path, pq), "The right action is not associative."


def first_hit_paths(algebra: PathAlgebra, vertex: int, ranks: dict[int, int]):
    return tuple(p for p in algebra.start[vertex]
                 if ranks[p[-1]] > ranks[vertex]
                 and all(ranks[u] <= ranks[vertex] for u in p[:-1]))


def check_kernel(algebra: PathAlgebra, vertex: int, ranks: dict[int, int],
                 standard: Module, prefixes: tuple[tuple[int, ...], ...]) -> None:
    """Check a degree-preserving isomorphism sum_p P_end(p)[-deg(p)] -> K_v."""
    expected = set(algebra.start[vertex]) - standard.basis_set
    images = []
    for p in prefixes:
        assert ranks[p[-1]] > ranks[vertex]
        for q in algebra.start[p[-1]]:
            pq = p + q[1:]
            assert algebra.degree[pq] == algebra.degree[p] + algebra.degree[q]
            images.append(pq)
    assert len(images) == len(set(images)), "The projective-kernel map is not injective."
    assert set(images) == expected, "The projective-kernel map does not have image K_v."


def derived_hom(algebra: PathAlgebra, source: int,
                prefixes: tuple[tuple[int, ...], ...], target: Module):
    """Return dimensions of H^q(Hom(R_source,target)) in every non-zero degree.

    A Hom basis item is (resolution generator, target basis path). The main
    generator is indexed by -1; first-hit generators have indices 0,1,... .
    The sign in the Hom differential is common to an entire homogeneous map
    and has no effect on the ranks recorded here.
    """
    groups: dict[int, list[tuple[int, tuple[int, ...]]]] = defaultdict(list)
    for b in target.basis:
        if target.anchor[b] == source:
            groups[target.degree[b]].append((-1, b))
        for i, prefix in enumerate(prefixes):
            if target.anchor[b] == prefix[-1]:
                degree = target.degree[b] - (algebra.degree[prefix] - 1)
                groups[degree].append((i, b))
    ranks = {}
    nonzero_differentials = 0
    for degree, domain in groups.items():
        codomain = groups.get(degree + 1, [])
        row_index = {item: row for row, item in enumerate(codomain)}
        matrix = [[0] * len(domain) for _ in codomain]
        for col, (generator, b) in enumerate(domain):
            if generator != -1:
                continue
            for i, prefix in enumerate(prefixes):
                image = target.action(b, prefix)
                if image is not None:
                    assert (i, image) in row_index, "The Hom differential has the wrong degree."
                    matrix[row_index[(i, image)]][col] += 1
        ranks[degree] = matrix_rank(matrix)
        # In a tree, every target vertex space has dimension at most one.
        # Consequently at most one column is non-zero; its entries are 1.
        # This also certifies that every recorded rank is characteristic independent.
        active_columns = [col for col in range(len(domain))
                          if any(matrix[row][col] for row in range(len(codomain)))]
        assert len(active_columns) <= 1
        assert all(entry in (0, 1) for row in matrix for entry in row)
        if ranks[degree]:
            nonzero_differentials += 1
    result = {}
    for degree, basis in groups.items():
        dimension = len(basis) - ranks.get(degree, 0) - ranks.get(degree - 1, 0)
        assert dimension >= 0
        if dimension:
            result[degree] = dimension
    return result, nonzero_differentials


def test_order(algebra: PathAlgebra, order: tuple[int, ...]):
    ranks = {v: i for i, v in enumerate(order)}
    standards = [Module(algebra, v, ranks, "standard") for v in range(algebra.n)]
    costandards = [Module(algebra, v, ranks, "costandard") for v in range(algebra.n)]
    kernels = [first_hit_paths(algebra, v, ranks) for v in range(algebra.n)]
    for module in standards + costandards:
        check_module(module)
    for v in range(algebra.n):
        check_kernel(algebra, v, ranks, standards[v], kernels[v])
    generated = set()
    for v in reversed(order):
        assert all(p[-1] in generated for p in kernels[v])
        generated.add(v)
    assert generated == set(range(algebra.n)), "The descending generation certificate failed."
    for module in standards:
        assert all(1 - algebra.m <= d <= 0 for d in module.degree.values())
    for module in costandards:
        assert all(0 <= d <= algebra.m - 1 for d in module.degree.values())

    hom_count = 0
    differential_count = 0
    for source in range(algebra.n):
        for target in range(algebra.n):
            cohomology, differentials = derived_hom(
                algebra, source, kernels[source], standards[target])
            hom_count += 1
            differential_count += differentials
            if source == target:
                assert cohomology == {0: 1}, ("Self-exceptionality", source, cohomology)
            if ranks[source] > ranks[target]:
                assert cohomology == {}, ("Backward semiorthogonality", source, target, cohomology)
            cohomology, differentials = derived_hom(
                algebra, source, kernels[source], costandards[target])
            hom_count += 1
            differential_count += differentials
            expected = {0: 1} if source == target else {}
            assert cohomology == expected, ("Standard-costandard pairing", source, target, cohomology)

    return {
        "hom_complexes": hom_count,
        "hom_differentials_with_positive_rank": differential_count,
        "standard_amplitude": -min(d for x in standards for d in x.degree.values()),
        "costandard_amplitude": max(d for x in costandards for d in x.degree.values()),
        "positive_degree_costandard": any(d > 0 for x in costandards for d in x.degree.values()),
        "nonzero_kernel_generator_degree": any(algebra.degree[p] < 0 for ps in kernels for p in ps),
    }


def empty_summary():
    return {
        "algebras": 0,
        "orders": 0,
        "hom_complexes": 0,
        "hom_differentials_with_positive_rank": 0,
        "orders_with_positive_degree_costandard": 0,
        "orders_with_negative_degree_kernel_generator": 0,
        "algebras_by_minimal_m": Counter(),
        "orders_by_minimal_m": Counter(),
        "orders_by_standard_costandard_amplitudes": Counter(),
    }


def run():
    graphs = {
        "A1": (1, ()),
        "A2": (2, ((0, 1),)),
        "A3": (3, ((0, 1), (1, 2))),
        "A4": (4, ((0, 1), (1, 2), (2, 3))),
        "D4": (4, ((0, 1), (0, 2), (0, 3))),
    }
    report = {
        "specification": {
            "field_for_rank_computation": "Q",
            "differential": 0,
            "arrow_degrees": [0, -1, -2],
            "orientation_enumeration": "every labelled orientation",
            "order_enumeration": "every vertex permutation",
            "minimal_m": "1 - minimum degree of any path",
            "standard": "quotient spanned by paths starting at v whose vertices have rank <= rank(v)",
            "costandard": "submodule of D(Ae_v) dual to paths ending at v whose vertices have rank <= rank(v)",
            "independent_hom_check": "exact ranks of Hom-complex differentials from first-hit projective resolutions",
            "characteristic_independence_check": "each differential has at most one non-zero column, with every non-zero entry equal to 1",
            "module_action_checks": "unit, grading, and associativity checked on every basis path",
            "scope": "The computation establishes the explicitly listed finite cases, not arbitrary grades.",
        },
        "graphs": {},
        "failures": [],
    }
    for name, (n, edges) in graphs.items():
        summaries = {"nontrivial_grading": empty_summary(), "zero_grading_control": empty_summary()}
        for reversals in product((False, True), repeat=len(edges)):
            oriented = tuple((v, u) if reverse else (u, v)
                             for (u, v), reverse in zip(edges, reversals))
            for degrees in product((0, -1, -2), repeat=len(edges)):
                algebra = PathAlgebra(n, tuple((u, v, d) for (u, v), d in zip(oriented, degrees)))
                summary = summaries["nontrivial_grading" if any(degrees) else "zero_grading_control"]
                summary["algebras"] += 1
                summary["algebras_by_minimal_m"][str(algebra.m)] += 1
                for order in permutations(range(n)):
                    summary["orders"] += 1
                    summary["orders_by_minimal_m"][str(algebra.m)] += 1
                    try:
                        result = test_order(algebra, order)
                    except AssertionError as error:
                        report["failures"].append({
                            "graph": name,
                            "arrows": [[u + 1, v + 1, d] for u, v, d in algebra.arrows],
                            "order": [v + 1 for v in order],
                            "error": str(error),
                        })
                        continue
                    for key in ("hom_complexes", "hom_differentials_with_positive_rank"):
                        summary[key] += result[key]
                    summary["orders_with_positive_degree_costandard"] += result["positive_degree_costandard"]
                    summary["orders_with_negative_degree_kernel_generator"] += result["nonzero_kernel_generator_degree"]
                    key = f"{result['standard_amplitude']},{result['costandard_amplitude']}"
                    summary["orders_by_standard_costandard_amplitudes"][key] += 1
        report["graphs"][name] = summaries
    report["totals"] = {}
    for group in ("nontrivial_grading", "zero_grading_control"):
        report["totals"][group] = {
            key: sum(graph[group][key] for graph in report["graphs"].values())
            for key in ("algebras", "orders", "hom_complexes", "hom_differentials_with_positive_rank",
                        "orders_with_positive_degree_costandard", "orders_with_negative_degree_kernel_generator")
        }
    report["totals"]["failures"] = len(report["failures"])
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("graded_path_results.json"))
    args = parser.parse_args()
    report = run()
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output), "totals": report["totals"]}, indent=2))
    if report["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
