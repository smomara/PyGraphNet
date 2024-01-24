import unittest
import numpy as np
from graphent.vertex import Vertex
from graphent.edge import Edge
from graphent.graph import Graph

class TestGraph(unittest.TestCase):
    def test_init(self):
        Graph("G", ['a', 'b', 'c'], [('a', 'b'), ('b', 'c'), ('a', 'c')])
        Graph("G", ['a', 'b', 'c'], [Edge('a', 'b'), Edge('b', 'c'), Edge('a', 'c')])

        with self.assertRaises(ValueError):
            Graph([], [])

    def test_basic_ops(self):
        g = Graph("G", ['a', 'b', 'c'], [Edge('a', 'b'), Edge('b', 'c')])

        self.assertEqual(g.order(), 3)
        self.assertEqual(g.size(), 2)
        self.assertEqual(g.degree('b'), 2)

        self.assertTrue('c' in g)
        self.assertTrue(Edge('b', 'c') in g)
        self.assertFalse('e' in g)
        self.assertFalse(Edge('a', 'c') in g)

        g.del_edge('a', 'b')
        self.assertTrue(Edge('a', 'b') not in g)
        self.assertEqual(g.order(), 3)
        self.assertEqual(g.size(), 1)

        g.add_edge('c', 'a')
        self.assertTrue(Edge('c', 'a') in g)
        self.assertEqual(g.order(), 3)
        self.assertEqual(g.size(), 2)

        g.del_vertex('c')
        self.assertTrue('c' not in g)
        self.assertEqual(g.order(), 2)
        self.assertEqual(g.size(), 0)

        self.assertEqual(g.degree('a'), 0)

    def test_complement(self):
        g = Graph("G", ['a', 'b'])
        complement = g.complement()

        self.assertEqual(g.order(), complement.order())
        self.assertEqual(complement.size(), 1)

    def test_diameter(self):
        vertices = ['a', 'b', 'c', 'd', 'e']
        edges = [
            ('a', 'b'),
            ('b', 'c'),
            ('c', 'd'),
            ('d', 'e'),
        ]
        g = Graph("G", vertices, edges)

        self.assertEqual(g.diameter(), 4)
        self.assertEqual(g.distance('a', 'c'), 2)
        self.assertTrue(['a', 'b', 'c'] in g.geodesics('a', 'c'))

        g.add_edge('a', 'e')
        self.assertEqual(g.diameter(), 2)
        self.assertEqual(g.distance('a', 'e'), 1)
        self.assertTrue(['a', 'e'] in g.geodesics('a', 'e'))

        self.assertEqual(g.distance('a', 'a'), 0)
        self.assertTrue(['a'] in g.geodesics('a', 'a'))
    
    def test_matrices(self):
        vertices = ["a", "b", "c"]
        edges = [("a", "b"), ("b", "c")]
        g = Graph("G", vertices, edges)

        expected_adjacency = np.array([
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ])

        expected_incidence = np.array([
            [1, 0],
            [1, 1],
            [0, 1]
        ])

        adjacency_matrix = g.adjacency_matrix()
        self.assertTrue(np.array_equal(adjacency_matrix, expected_adjacency))

        incidence_matrix = g.incidence_matrix()
        self.assertTrue(np.array_equal(incidence_matrix, expected_incidence))