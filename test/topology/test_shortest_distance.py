import unittest
from pygraphnet import Graph, shortest_distance

class TestShortestDistance(unittest.TestCase):
    def setUp(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
        self.directed_graph = Graph(edges, directed=True)
        self.undirected_graph = Graph(edges, directed=False)
        self.weights = {(0, 1): 2, (1, 2): 2, (2, 3): 2, (3, 4): 10, (4, 0): 2}
    
    # Directed Graph Tests
    def test_directed_no_source_no_target(self):
        distances = shortest_distance(self.directed_graph)
        expected = {
            0: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4},
            1: {0: 4, 1: 0, 2: 1, 3: 2, 4: 3},
            2: {0: 3, 1: 4, 2: 0, 3: 1, 4: 2},
            3: {0: 2, 1: 3, 2: 4, 3: 0, 4: 1},
            4: {0: 1, 1: 2, 2: 3, 3: 4, 4: 0}
        }
        self.assertEqual(distances, expected)

    def test_directed_with_no_source_and_target(self):
        distance = shortest_distance(self.directed_graph, target=3)
        expected = {0: 3, 1: 2, 2: 1, 3: 0, 4: 4}
        self.assertEqual(distance, expected)

    def test_directed_with_source_no_target(self):
        distances = shortest_distance(self.directed_graph, source=0)
        expected = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
        self.assertEqual(distances, expected)
    
    def test_directed_with_source_and_target(self):
        distance = shortest_distance(self.directed_graph, source=0, target=3)
        self.assertEqual(distance, 3)

    def test_directed_with_weights(self):
        distances = shortest_distance(self.directed_graph, source=0, weights=self.weights)
        expected = {0: 0, 1: 2, 2: 4, 3: 6, 4: 16}
        self.assertEqual(distances, expected)

    # Undirected Graph Tests
    def test_undirected_no_source_no_target(self):
        distances = shortest_distance(self.undirected_graph)
        expected = {
            0: {0: 0, 1: 1, 2: 2, 3: 2, 4: 1},
            1: {0: 1, 1: 0, 2: 1, 3: 2, 4: 2},
            2: {0: 2, 1: 1, 2: 0, 3: 1, 4: 2},
            3: {0: 2, 1: 2, 2: 1, 3: 0, 4: 1},
            4: {0: 1, 1: 2, 2: 2, 3: 1, 4: 0}
        }
        self.assertEqual(distances, expected)

    def test_undirected_with_no_source_and_target(self):
        distance = shortest_distance(self.undirected_graph, target=3)
        expected = {0: 2, 1: 2, 2: 1, 3: 0, 4: 1}
        self.assertEqual(distance, expected)

    def test_undirected_with_source_no_target(self):
        distances = shortest_distance(self.undirected_graph, source=0)
        expected = {0: 0, 1: 1, 2: 2, 3: 2, 4: 1}
        self.assertEqual(distances, expected)

    def test_undirected_with_source_and_target(self):
        distance = shortest_distance(self.undirected_graph, source=0, target=3)
        self.assertEqual(distance, 2)

    def test_undirected_with_weights(self):
        distances = shortest_distance(self.undirected_graph, source=0, weights=self.weights)
        expected = {0: 0, 1: 2, 2: 4, 3: 6, 4: 2}
        self.assertEqual(distances, expected)