import unittest
from graphent.graph import Vertex

class TestVertex(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(Vertex('a'), Vertex('a'))
        self.assertNotEqual(Vertex(3.14), Vertex(3))
        self.assertNotEqual(Vertex(1), Vertex('b'))
    
    def test_lt(self):
        self.assertTrue(Vertex('a') < Vertex('b'))
        self.assertTrue(Vertex(1) < Vertex('z'))
        self.assertTrue(Vertex(14) < Vertex("dog"))

if __name__ == '__main__':
    unittest.main()