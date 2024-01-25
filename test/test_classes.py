import unittest
import graphent
from graphent import Graph

class TestClasses(unittest.TestCase):
    def test_path(self):
        n = 5
        p = graphent.path(n)

        self.assertEqual(p.order(), n)
        self.assertEqual(p.size(), n - 1)

        vertices_list = sorted(p.vertices)
        self.assertTrue(p.distance(vertices_list[0], vertices_list[-1]) == (n-1))

        if n > 1:
            self.assertEqual(p.degree(vertices_list[0]), 1)
            self.assertEqual(p.degree(vertices_list[-1]), 1)

            for vertex in vertices_list[1:-1]:
                self.assertEqual(p.degree(vertex), 2)

    def test_cycle(self):
        n = 5
        c = graphent.cycle(n)

        self.assertEqual(c.order(), n)
        self.assertEqual(c.size(), n)

        vertices_list = sorted(c.vertices)
        for i in range(n):
            self.assertEqual(c.distance(vertices_list[i], vertices_list[(i+1)%n]), 1)

        for vertex in vertices_list:
            self.assertEqual(c.degree(vertex), 2)

        if n % 2 == 0:
            self.assertEqual(c.distance(vertices_list[0], vertices_list[n//2]), n//2)
        else:
            self.assertEqual(c.distance(vertices_list[0], vertices_list[n//2]), n//2)

    def test_complete_graph(self):
        n = 5
        k = graphent.complete_graph(n)

        expected_edges = n * (n-1) // 2
        self.assertEqual(k.order(), n)
        self.assertEqual(k.size(), expected_edges)

        vertices_list = sorted(k.vertices)
        for vertex in vertices_list:
            self.assertEqual(k.degree(vertex), n-1)

        for i, u in enumerate(vertices_list):
            for v in vertices_list[i+1:]:
                self.assertEqual(k.distance(u, v), 1)

if __name__ == '__main__':
    unittest.main()