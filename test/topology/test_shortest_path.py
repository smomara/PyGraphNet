import unittest
from pygraphnet import Graph, shortest_path

class TestShortestPath(unittest.TestCase):
    def setUp(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
        self.directed_graph = Graph(edges, directed=True)
        self.undirected_graph = Graph(edges, directed=False)
        self.weights = {(0, 1): 2, (1, 2): 2, (2, 3): 2, (3, 4): 10, (4, 0): 2}

    def test_shortest_path_directed_unweighted(self):
        vertices, edges = shortest_path(self.directed_graph, source=0, target=3)
        expected_vertices = [0, 1, 2, 3]
        expected_edges = [(0, 1), (1, 2), (2, 3)]
        self.assertEqual([v for v in vertices], expected_vertices)
        self.assertEqual([e for e in edges], expected_edges)

    def test_shortest_path_directed_weighted(self):
        vertices, edges = shortest_path(self.directed_graph, source=0, target=3, weights=self.weights)
        expected_vertices = [0, 1, 2, 3]
        expected_edges = [(0, 1), (1, 2), (2, 3)]
        self.assertEqual([v for v in vertices], expected_vertices)
        self.assertEqual([e for e in edges], expected_edges)

    def test_shortest_path_undirected_unweighted(self):
        vertices, edges = shortest_path(self.undirected_graph, source=0, target=3)
        expected_vertices = [0, 4, 3]
        expected_edges = [(0, 4), (4, 3)]
        self.assertEqual([v for v in vertices], expected_vertices)
        self.assertEqual([e for e in edges], expected_edges)
    
    def test_shortest_path_undirected_weighted(self):
        vertices, edges = shortest_path(self.undirected_graph, source=3, target=4, weights=self.weights)
        expected_vertices = [3, 2, 1, 0, 4]
        expected_edges = [(3, 2), (2, 1), (1, 0), (0, 4)]
        self.assertEqual([v for v in vertices], expected_vertices)
        self.assertEqual([e for e in edges], expected_edges)