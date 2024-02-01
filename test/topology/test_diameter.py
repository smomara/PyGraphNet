import unittest
from pygraphnet import Graph, diameter

class TestShortestPath(unittest.TestCase):
    def setUp(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
        self.directed_graph = Graph(edges, directed=True)
        self.undirected_graph = Graph(edges, directed=False)
        self.weights = {(0, 1): 2, (1, 2): 2, (2, 3): 2, (3, 4): 10, (4, 0): 2}

    def test_undirected_no_weights(self):
        result = diameter(self.undirected_graph)
        expected = (2, (0, 2))
        self.assertEqual(result, expected)
    
    def test_undirected_weights(self):
        result = diameter(self.undirected_graph, self.weights)
        expected = (8, (3, 4))
        self.assertEqual(result, expected)
    
    def test_directed_no_weights(self):
        result = diameter(self.directed_graph)
        expected = (4, (0, 4))
        self.assertEqual(result, expected)
    
    def test_directed_weights(self):
        result = diameter(self.directed_graph, self.weights)
        expected = (16, (0, 4))
        self.assertEqual(result, expected)