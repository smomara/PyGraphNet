import unittest
from pygraphnet import Graph, cross_product

class TestCrossProduct(unittest.TestCase):
    def setUp(self):
        triangle_edges = [(0, 1), (1, 2), (2, 0)]
        square_edges = [(0, 1), (1, 2), (2, 3), (3, 0)]

        self.undirected_triangle = Graph(triangle_edges, directed=False)
        self.undirected_square = Graph(square_edges, directed=False)
        self.directed_triangle = Graph(triangle_edges, directed=True)
        self.directed_square = Graph(square_edges, directed=True)

    def test_cross_product_directed(self):
        result = cross_product(self.directed_square, self.directed_triangle)
        self.assertTrue(result.directed)
        self.assertEqual(len(result.vertices), 12)
        self.assertIn(((0, 0), (1, 0)), result.edges)
        self.assertNotIn(((1, 0), (0, 0)), result.edges)

    def test_cross_product_undirected(self):
        result = cross_product(self.undirected_square, self.undirected_triangle)
        self.assertFalse(result.directed)
        self.assertEqual(len(result.vertices), 12)
        self.assertIn(((0, 0), (1, 0)), result.edges)
        self.assertIn(((1, 0), (0, 0)), result.edges)

    def test_cross_product_mixed(self):
        result = cross_product(self.undirected_square, self.directed_triangle)
        self.assertTrue(result.directed)
        self.assertEqual(len(result.vertices), 12)
        self.assertIn(((0, 0), (1, 0)), result.edges)
        self.assertIn(((1, 0), (0, 0)), result.edges)