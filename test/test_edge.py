import unittest
from graphent.vertex import Vertex
from graphent.edge import Edge

class TestEdge(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Edge('a', 'a')

    def test_eq(self):
        self.assertEqual(Edge('a', 'b'), Edge('a', 'b'))
        self.assertEqual(Edge('a', 'b'), Edge('b', 'a'))

        a, b = Vertex('a'), Vertex('b')
        self.assertEqual(Edge(a, 'b'), Edge('a', b))

    def test_contains(self):
        edge = Edge('a', 'b')
        self.assertTrue('a' in edge)
        self.assertTrue('b' in edge)

if __name__ == '__main__':
    unittest.main()