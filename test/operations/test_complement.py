import unittest
from pygraphnet import Graph, complement

class TestGraphComplement(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph(directed=False)
        comp_g = complement(g)
        self.assertEqual(len(comp_g.vertices), 0)

    def test_undirected_no_edges(self):
        g = Graph(4, directed=False)
        comp_g = complement(g)
        self.assertEqual(len(comp_g.edges), 6)

    def test_directed_no_edges(self):
        g = Graph(4, directed=True)
        comp_g = complement(g)
        self.assertEqual(len(comp_g.edges), 12)

    def test_undirected_full(self):
        g = Graph(3, directed=False)
        for i in g.vertices:
            for j in g.vertices:
                if i != j:
                    g.add_edge(i, j)
        comp_g = complement(g)
        self.assertEqual(len(comp_g.edges), 0)

    def test_directed_full(self):
        g = Graph(3, directed=True)
        for i in g.vertices:
            for j in g.vertices:
                if i != j:
                    g.add_edge(i, j)
        comp_g = complement(g)
        self.assertEqual(len(comp_g.edges), 0)

    def test_mixed_connections_undirected(self):
        g = Graph([(0, 1)], directed=False)  # A simple graph with one edge
        comp_g = complement(g)
        # No additional vertices should be added, only missing edges
        self.assertEqual(len(comp_g.vertices), 2, "Complement should maintain the same vertices")
        self.assertFalse((0, 1) in comp_g.edges or (1, 0) in comp_g.edges, "Complement should not have the original edge")

    def test_mixed_connections_directed(self):
        g = Graph([(0, 1)], directed=True)  # A simple graph with one edge
        comp_g = complement(g)
        # Check for the absence of the original edge and presence of its reverse
        self.assertFalse((0, 1) in comp_g.edges, "Complement should not contain the original edge")
        self.assertTrue((1, 0) in comp_g.edges, "Complement should contain the reverse of the original edge")

if __name__ == '__main__':
    unittest.main()
