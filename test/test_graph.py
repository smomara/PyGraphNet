import unittest
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

        g.add_edge('a', 'e')
        self.assertEqual(g.diameter(), 2)
        self.assertEqual(g.distance('a', 'e'), 1)

        self.assertEqual(g.distance('a', 'a'), 0)