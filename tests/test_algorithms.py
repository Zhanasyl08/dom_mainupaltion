import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from algorithms import DSU, dsu, kruskal, prim, scc, topo, dag, reconstruct_route


class GraphTests(unittest.TestCase):
    def test_dsu(self):
        self.assertEqual(dsu(5, [[0, 1], [1, 2], [3, 4], [2, 4]]),
                         [[4, 2], [3, 3], [2, 3], [1, 5]])

    def test_repeated_union(self):
        self.assertEqual(dsu(3, [[0, 1], [1, 0]]), [[2, 2], [2, 2]])

    def test_mst(self):
        edges = [[0, 1, 3], [1, 2, -2], [0, 2, 8], [3, 3, -10]]
        for algorithm in (kruskal, prim):
            result = algorithm(5, edges)
            self.assertEqual(result['cost'], 1)
            self.assertEqual(result['components'], 3)
            self.assertEqual(set(result['edge_ids']), {0, 1})

    def test_parallel_edges(self):
        for algorithm in (kruskal, prim):
            self.assertEqual(algorithm(2, [[0, 1, 7], [0, 1, 2]])['cost'], 2)

    def test_scc(self):
        result = scc(5, [[0, 1], [1, 0], [1, 2], [2, 3], [3, 2]])
        self.assertEqual(result['components'], 3)
        a = result['labels']
        self.assertEqual(a[0], a[1])
        self.assertEqual(a[2], a[3])
        self.assertNotEqual(a[1], a[2])
        self.assertNotEqual(a[4], a[0])
        self.assertIn([a[1], a[2]], result['condensation'])

    def test_topo(self):
        edges = [[0, 1], [1, 2], [0, 2]]
        result = topo(3, edges)
        self.assertTrue(result['acyclic'])
        pos = {v: i for i, v in enumerate(result['order'])}
        self.assertTrue(all(pos[u] < pos[v] for u, v in edges))
        self.assertEqual(topo(2, [[0, 1], [1, 0]]), {"acyclic": False, "order": []})

    def test_dag(self):
        edges = [[0, 1, 5], [0, 2, 2], [2, 1, -4], [1, 3, 1]]
        result = dag(5, edges, 0)
        self.assertEqual(result['distance'], [0, -2, 2, -1, None])
        self.assertEqual(reconstruct_route(3, result['parent_edge'], edges, 0), [0, 2, 1, 3])
        self.assertEqual(reconstruct_route(4, result['parent_edge'], edges, 0), [])
        self.assertEqual(reconstruct_route(0, result['parent_edge'], edges, 0), [0])
        self.assertEqual(dag(2, [[0, 1, 1], [1, 0, 1]], 0),
                         {"acyclic": False, "distance": [], "parent_edge": []})

    def test_empty_and_deep(self):
        self.assertEqual(kruskal(0, []), {"cost": 0, "edge_ids": [], "components": 0})
        self.assertEqual(scc(0, []), {"components": 0, "labels": [], "condensation": []})
        edges = [[i, i + 1] for i in range(29999)]
        self.assertTrue(topo(30000, edges)['acyclic'])
        self.assertEqual(scc(30000, edges)['components'], 30000)


if __name__ == '__main__':
    unittest.main()
