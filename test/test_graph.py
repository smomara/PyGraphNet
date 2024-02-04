import unittest
from pygraphnet import Graph

class TestGraph(unittest.TestCase):
    def test_init_empty_graph(self):
        g = Graph(5)
        self.assertEqual(len(g.vertices), 5)
        self.assertFalse(g.directed)

    def test_init_from_graph(self):
        g1 = Graph(5)
        g2 = Graph(g1)
        self.assertEqual(g1.vertices, g2.vertices)
        self.assertEqual(g1.edges, g2.edges)

    def test_init_from_adj_list_undirected(self):
        adj_list = {0: [1, 2], 1: [2], 2: [3], 3: [0, 4], 4: []}
        g = Graph(adj_list)
        self.assertEqual(len(g.vertices), 5)
        self.assertEqual(len(g.edges), 6)
        self.assertEqual(g.adj_list, {
            0: set([1, 2, 3]),
            1: set([0, 2]),
            2: set([0, 1, 3]),
            3: set([0, 2, 4]),
            4: set([3]),
        })

    def test_init_from_adj_list_directed(self):
        adj_list = {0: [1, 2], 1: [2], 2: [3], 3: [0, 4], 4: []}
        g = Graph(adj_list, directed=True)
        self.assertEqual(len(g.vertices), 5)
        self.assertEqual(len(g.edges), 6)
        self.assertNotEqual(g.adj_list, {
            0: set([1, 2, 3]),
            1: set([0, 2]),
            2: set([0, 1, 3]),
            3: set([0, 2, 4]),
            4: set([3]),
        })

    def test_init_from_edge_list_undirected(self):
        edge_list = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
        g = Graph(edge_list)
        self.assertEqual(len(g.vertices), 5)
        self.assertEqual(len(g.edges), 5)
        self.assertEqual(g.adj_list, {
            0: set([1, 4]),
            1: set([0, 2]),
            2: set([1, 3]),
            3: set([2, 4]),
            4: set([0, 3]),
        })
    
    def test_init_from_edge_list_directed(self):
        edge_list = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
        g = Graph(edge_list, directed = True)
        self.assertEqual(len(g.vertices), 5)
        self.assertEqual(len(g.edges), 5)
        self.assertNotEqual(g.adj_list, {
            0: set([1, 4]),
            1: set([0, 2]),
            2: set([1, 3]),
            3: set([2, 4]),
            4: set([0, 3]),
        })

    def test_add_vertex(self):
        g = Graph()
        g.add_vertex(1)
        self.assertIn(1, g.vertices)

    def test_del_vertex(self):
        g = Graph(5)
        g.del_vertex(0)
        self.assertNotIn(0, g.vertices)
        self.assertNotIn((0, 1), g.edges)
        self.assertNotIn(0, g.adj_list)

    def test_add_edge_directed(self):
        g = Graph(directed=True)
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_edge(0, 1)
        self.assertIn((0, 1), g.edges)
        self.assertNotIn((1, 0), g.edges)

    def test_add_edge_bidirectional(self):
        g = Graph(directed=True)
        g.add_edge(0, 1, bidirectional=True)
        self.assertIn((0, 1), g.edges)
        self.assertIn((1, 0), g.edges)
        
    def test_add_edge_undirected(self):
        g = Graph(directed=False)
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_edge(0, 1)
        self.assertIn((0, 1), g.edges)
        self.assertNotIn((1, 0), g.edges)

    def test_del_edge(self):
        g = Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_edge(0, 1)
        g.del_edge(0, 1)
        self.assertNotIn((0, 1), g.edges)
        self.assertNotIn(1, g.adj_list[0])

if __name__ == '__main__':
    unittest.main()