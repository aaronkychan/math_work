#!/usr/bin/env python3
"""Exact tests for three acyclic path dgas with d(c)=ab.

Run from any directory:
    python3 testing/differential_path_tests.py

The script writes differential_path_results.json next to this source file.
No third-party packages are required. All linear algebra uses rational numbers.

For a vertex order r, the tested objects are
    K_v = e_v A e_{>v} A,
    Delta_v = e_v A / K_v,
    Nabla_v = Hom_k((A / A e_{>v} A)e_v, k).
The amplitude tests concern these particular objects. A failed amplitude test
does not establish nonexistence of a different structure for the same order.

The script also checks the path-basis conditions used in a mathematical proof
of full exceptionality and the prescribed derived pairing: finite semi-free
kernels on later projectives and the unique first-hit path bijection. Those
structural checks are separate from the exact cohomology calculations. The
script does not independently construct all derived Hom complexes.

The proof uses K_u -> P_u -> Delta_u. A finite semi-free filtration of K_u
has factors shifted P_w with r(w)>r(u), which vanish against Delta_v when
r(u)>=r(v). This proves the required exceptional semiorthogonality and scalar
self-endomorphisms. Descending induction gives generation of per A; finite
exceptional projections give per A=D_fd(A). For r(u)<r(v), the unique first-hit
path decomposition makes Hom_A(P_u,Nabla_v)->Hom_A(K_u,Nabla_v) an isomorphism
of dg complexes. For r(u)>r(v) both complexes vanish; for u=v the complexes
are k and zero. The resulting derived pairing is k in degree zero precisely
when u=v. These are mathematical deductions from the checked hypotheses,
not separate numerical derived-Hom calculations.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path


def rank_of_columns(columns, dimension):
    if not columns:
        return 0
    rows = [[Fraction(column[i]) for column in columns]
            for i in range(dimension)]
    return len(rref(rows, len(columns))[1])


def rref(rows, column_count):
    matrix = [[Fraction(x) for x in row] for row in rows]
    pivot_columns = []
    row_index = 0
    for column in range(column_count):
        pivot = next((j for j in range(row_index, len(matrix))
                      if matrix[j][column]), None)
        if pivot is None:
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        scale = matrix[row_index][column]
        matrix[row_index] = [x / scale for x in matrix[row_index]]
        for j in range(len(matrix)):
            if j != row_index and matrix[j][column]:
                scale = matrix[j][column]
                matrix[j] = [x - scale * y
                             for x, y in zip(matrix[j], matrix[row_index])]
        pivot_columns.append(column)
        row_index += 1
        if row_index == len(matrix):
            break
    return matrix, pivot_columns


def nullspace(rows, column_count):
    matrix, pivots = rref(rows, column_count)
    vectors = []
    for free_column in range(column_count):
        if free_column in pivots:
            continue
        vector = [Fraction(0)] * column_count
        vector[free_column] = Fraction(1)
        for row_index, pivot in enumerate(pivots):
            vector[pivot] = -matrix[row_index][free_column]
        vectors.append(vector)
    return vectors


class PathDGA:
    def __init__(self, vertices, arrows, differential):
        self.vertices = tuple(vertices)
        self.arrows = arrows
        self.generator_differential = differential
        self.paths = []
        for vertex in self.vertices:
            self._extend(vertex, vertex, (), (vertex,), 0)
        self.path_index = {(p['start'], p['word']): p for p in self.paths}
        self.differential = {}
        for path in self.paths:
            image = defaultdict(Fraction)
            prefix_degree = 0
            for i, arrow in enumerate(path['word']):
                sign = -1 if prefix_degree % 2 else 1
                for coefficient, replacement in differential.get(arrow, []):
                    word = path['word'][:i] + tuple(replacement) + path['word'][i+1:]
                    target = (path['start'], word)
                    assert target in self.path_index
                    assert self.path_index[target]['degree'] == path['degree'] + 1
                    image[target] += sign * coefficient
                prefix_degree += arrows[arrow][2]
            self.differential[self.key(path)] = {
                key: value for key, value in image.items() if value
            }
        for path in self.paths:
            square = defaultdict(Fraction)
            for middle, first in self.differential[self.key(path)].items():
                for target, second in self.differential[middle].items():
                    square[target] += first * second
            assert all(value == 0 for value in square.values())
        for left in self.paths:
            for right in self.paths:
                if left['end'] != right['start']:
                    continue
                product = (left['start'], left['word'] + right['word'])
                assert product in self.path_index
                leibniz_image = defaultdict(Fraction)
                for target, coefficient in self.differential[self.key(left)].items():
                    leibniz_image[(left['start'], target[1] + right['word'])] += coefficient
                sign = -1 if left['degree'] % 2 else 1
                for target, coefficient in self.differential[self.key(right)].items():
                    leibniz_image[(left['start'], left['word'] + target[1])] += sign * coefficient
                leibniz_image = {key: value for key, value in leibniz_image.items() if value}
                assert self.differential[product] == leibniz_image

    @staticmethod
    def key(path):
        return path['start'], path['word']

    @staticmethod
    def label(path):
        return ''.join(path['word']) if path['word'] else f"e{path['start']}"

    def _extend(self, start, end, word, vertices, degree):
        self.paths.append(dict(start=start, end=end, word=word,
                               vertices=vertices, degree=degree))
        for arrow, (source, target, arrow_degree) in self.arrows.items():
            if source == end:
                assert target not in vertices, 'The quiver must be acyclic.'
                self._extend(start, target, word + (arrow,),
                             vertices + (target,), degree + arrow_degree)

    def cohomology(self, selected, kind, module_vertex='end'):
        """Compute cohomology of a path subcomplex or path quotient complex."""
        keys = {self.key(path) for path in selected}
        by_degree = defaultdict(list)
        for path in selected:
            by_degree[path['degree']].append(path)
        differential = {}
        for path in selected:
            raw_image = self.differential[self.key(path)]
            if kind == 'subcomplex':
                assert all(target in keys for target in raw_image)
            differential[self.key(path)] = {
                target: value for target, value in raw_image.items() if target in keys
            }
        for source in keys:
            square = defaultdict(Fraction)
            for middle, coefficient in differential[source].items():
                for target, next_coefficient in differential[middle].items():
                    square[target] += coefficient * next_coefficient
            assert all(value == 0 for value in square.values())
        result = {}
        for degree in sorted(by_degree):
            basis = by_degree[degree]
            next_basis = by_degree[degree + 1]
            previous_basis = by_degree[degree - 1]
            rows = [[differential[self.key(source)].get(self.key(target), 0)
                     for source in basis] for target in next_basis]
            cycles = nullspace(rows, len(basis))
            boundaries = [
                [differential[self.key(source)].get(self.key(target), 0)
                 for target in basis] for source in previous_basis
            ]
            span = list(boundaries)
            span_rank = rank_of_columns(span, len(basis))
            representatives = []
            for cycle in cycles:
                enlarged_rank = rank_of_columns(span + [cycle], len(basis))
                if enlarged_rank == span_rank:
                    continue
                span.append(cycle)
                span_rank = enlarged_rank
                support = [path for path, coefficient in zip(basis, cycle) if coefficient]
                vertices = {path[module_vertex] for path in support}
                assert len(vertices) == 1
                representatives.append({
                    'module_vertex': next(iter(vertices)),
                    'terms': [
                        {'path': self.label(path), 'coefficient': str(coefficient)}
                        for path, coefficient in zip(basis, cycle) if coefficient
                    ],
                })
            if representatives:
                result[str(degree)] = {
                    'dimension': len(representatives),
                    'dimension_by_vertex': dict(sorted(Counter(
                        representative['module_vertex']
                        for representative in representatives).items())),
                    'representatives': representatives,
                }
        return result

    def first_hit_generators(self, vertex, rank):
        return [path for path in self.paths
                if path['start'] == vertex and path['word']
                and rank[path['end']] > rank[vertex]
                and all(rank[w] <= rank[vertex] for w in path['vertices'][:-1])]

    def structural_checks(self, rank):
        for vertex in self.vertices:
            ideal = {self.key(path) for path in self.paths
                     if any(rank[w] > rank[vertex] for w in path['vertices'])}
            for source in ideal:
                assert all(target in ideal for target in self.differential[source])
        generators = {v: self.first_hit_generators(v, rank) for v in self.vertices}
        for vertex in self.vertices:
            generator_keys = {self.key(path) for path in generators[vertex]}
            for generator in generators[vertex]:
                for target_key in self.differential[self.key(generator)]:
                    target = self.path_index[target_key]
                    first = next(i for i, w in enumerate(target['vertices'])
                                 if rank[w] > rank[vertex])
                    prefix = self.path_index[(vertex, target['word'][:first])]
                    assert self.key(prefix) in generator_keys
                    assert prefix['degree'] > generator['degree']
        for u in self.vertices:
            for v in self.vertices:
                domain_paths = [path for path in self.paths
                                if path['start'] == u and path['end'] == v
                                and all(rank[w] <= rank[v] for w in path['vertices'])]
                target_pairs = []
                for prefix in generators[u]:
                    for suffix in self.paths:
                        if (suffix['start'] == prefix['end'] and suffix['end'] == v
                                and all(rank[w] <= rank[v] for w in suffix['vertices'])):
                            target_pairs.append((u, prefix['word'] + suffix['word']))
                if rank[u] < rank[v]:
                    assert Counter(self.key(path) for path in domain_paths) == Counter(target_pairs)
                elif u == v:
                    assert [self.key(path) for path in domain_paths] == [(u, ())]
                    assert not target_pairs
                else:
                    assert not domain_paths and not target_pairs
        return {
            'all_rank_ideals_d_stable': True,
            'finite_semi_free_kernels_on_later_projectives': True,
            'first_hit_path_bijections_for_derived_pairing': True,
            'full_exceptionality_and_paired_costandards':
                'Follow from these checked structural conditions by the proof in the script docstring and accompanying discussion.',
        }


def dual_cohomology(left_cohomology):
    result = {}
    for degree, data in left_cohomology.items():
        result[str(-int(degree))] = {
            'dimension': data['dimension'],
            'dimension_by_vertex': data['dimension_by_vertex'],
            'dual_to_representatives': data['representatives'],
        }
    return dict(sorted(result.items(), key=lambda item: int(item[0])))


def test_example(name, h_degree, widths):
    arrows = {'a': (1, 2, 0), 'b': (2, 3, 0), 'c': (1, 3, -1)}
    vertices = [1, 2, 3]
    if h_degree is not None:
        vertices.append(4)
        arrows['h'] = (3, 4, h_degree)
    algebra = PathDGA(vertices, arrows, {'c': [(1, ('a', 'b'))]})
    algebra_cohomology = algebra.cohomology(algebra.paths, 'subcomplex')
    orders = []
    for order in permutations(vertices):
        rank = {vertex: position for position, vertex in enumerate(order)}
        objects = {}
        for vertex in vertices:
            starts = [p for p in algebra.paths if p['start'] == vertex]
            allowed = lambda p: all(rank[w] <= rank[vertex] for w in p['vertices'])
            standards = [p for p in starts if allowed(p)]
            kernels = [p for p in starts if not allowed(p)]
            left_quotients = [p for p in algebra.paths if p['end'] == vertex and allowed(p)]
            objects[str(vertex)] = {
                'standard_cohomology': algebra.cohomology(standards, 'quotient'),
                'kernel_cohomology': algebra.cohomology(kernels, 'subcomplex'),
                'costandard_cohomology': dual_cohomology(algebra.cohomology(
                    left_quotients, 'quotient', module_vertex='start')),
                'standard_graded_basis': [algebra.label(p) for p in standards],
                'kernel_graded_basis': [algebra.label(p) for p in kernels],
                'left_quotient_graded_basis': [algebra.label(p) for p in left_quotients],
            }
        amplitude_tests = {}
        for width in widths:
            failures = []
            for vertex in vertices:
                for label in ('standard', 'kernel', 'costandard'):
                    lower, upper = ((0, width - 1) if label == 'costandard'
                                    else (1 - width, 0))
                    for degree, data in objects[str(vertex)][label + '_cohomology'].items():
                        if not lower <= int(degree) <= upper:
                            failures.append({
                                'condition': label + '_amplitude', 'vertex': vertex,
                                'degree': int(degree), 'allowed_degrees': [lower, upper],
                                'cohomology': data,
                            })
            amplitude_tests[str(width)] = {'passes': not failures, 'failures': failures}
        orders.append({
            'order': list(order), 'order_label': ''.join(map(str, order)),
            'structural_checks': algebra.structural_checks(rank),
            'objects': objects, 'amplitude_tests': amplitude_tests,
        })
    summary = {}
    for width in widths:
        passed = [row['order_label'] for row in orders if row['amplitude_tests'][str(width)]['passes']]
        failed = [row['order_label'] for row in orders if not row['amplitude_tests'][str(width)]['passes']]
        summary[str(width)] = {'passed': len(passed), 'failed': len(failed),
                               'passing_orders': passed, 'failing_orders': failed}
    return {
        'name': name,
        'arrows': {key: {'source': value[0], 'target': value[1], 'degree': value[2]}
                   for key, value in arrows.items()},
        'differential': {'c': 'ab', 'all_other_arrows': '0'},
        'differential_has_degree_plus_one_on_every_path': True,
        'd_squared_checked_on_every_path': True,
        'graded_leibniz_checked_on_every_composable_pair_of_paths': True,
        'algebra_cohomology': algebra_cohomology,
        'minimal_cohomological_width': 1 - min(map(int, algebra_cohomology)),
        'raw_path_width': 1 - min(path['degree'] for path in algebra.paths),
        'summary_by_width': summary,
        'orders': orders,
    }


def main():
    examples = [
        test_example('three_vertex_bypass', None, [1, 2]),
        test_example('four_vertex_bypass_h_degree_zero', 0, [1, 2]),
        test_example('four_vertex_bypass_h_degree_minus_one', -1, [2, 3]),
    ]
    expected_failures = [
        {'1': ['132', '312'], '2': []},
        {'1': ['1324', '1342', '1432', '3124', '3142', '3412', '4132', '4312'], '2': []},
        {'2': ['1342', '3142', '3412', '4312'], '3': []},
    ]
    for example, expected in zip(examples, expected_failures):
        for width, failures in expected.items():
            assert example['summary_by_width'][width]['failing_orders'] == failures
    new_example = examples[-1]
    for row in new_example['orders']:
        for vertex_data in row['objects'].values():
            assert all(-1 <= int(degree) <= 0
                       for degree in vertex_data['kernel_cohomology'])
        for failure in row['amplitude_tests']['2']['failures']:
            if row['order_label'] in ('3412', '4312'):
                assert (failure['condition'], failure['vertex'], failure['degree']) == (
                    'standard_amplitude', 1, -2)
                witness = failure['cohomology']['representatives']
            else:
                assert row['order_label'] in ('1342', '3142')
                assert (failure['condition'], failure['vertex'], failure['degree']) == (
                    'costandard_amplitude', 4, 2)
                witness = failure['cohomology']['dual_to_representatives']
            assert len(witness) == 1
            assert witness[0]['terms'] == [{'path': 'ch', 'coefficient': '1'}]
    result = {
        'scope': 'Canonical standard quotients, kernel complexes, and paired costandards for all vertex orders.',
        'computational_scope': 'Exact cohomological-window checks plus explicit differential, ideal-stability, and path-basis checks. Derived Hom vanishing and fullness are mathematical deductions from the semi-free proof; independently resolved derived Hom complexes are not computed.',
        'conventions': {
            'modules': 'right dg modules',
            'path_multiplication': 'left to right; e_source a = a = a e_target',
            'differential_degree': 1,
            'shift': 'H^q(X[s]) = H^(q+s)(X)',
            'arithmetic': 'exact rational linear algebra',
            'field_note': 'All non-zero differential matrices in these examples have independent entries ±1, so the displayed dimensions hold over every field.',
            'amplitudes': {'standard_and_kernel': '[1-m,0]', 'costandard': '[0,m-1]'},
        },
        'limitation': 'Failure of this canonical construction does not by itself exclude other choices of standards.',
        'examples': examples,
    }
    output = Path(__file__).with_name('differential_path_results.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    for example in examples:
        print(example['name'],
              'cohomological_width=' + str(example['minimal_cohomological_width']),
              'raw_path_width=' + str(example['raw_path_width']))
        for width, data in example['summary_by_width'].items():
            print('  m=' + width, 'pass=' + str(data['passed']),
                  'fail=' + str(data['failed']),
                  'failed_orders=' + ','.join(data['failing_orders']))
    print('Results:', output)


if __name__ == '__main__':
    main()
