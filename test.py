import numpy as np
from graphent.graph import Graph

def test_matrices():
    vertices = ["a", "b", "c"]
    edges = [("a", "b"), ("b", "c")]
    g = Graph("G", vertices, edges)

    expected_adjacency = np.array([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ])

    expected_incidence = np.array([
        [1, 0],
        [1, 1],
        [0, 1]
    ])

    adjacency_matrix = g.adjacency_matrix()
    print(np.array_equal(adjacency_matrix, expected_adjacency))

    incidence_matrix = g.incidence_matrix()
    print(incidence_matrix)
    print(expected_incidence)
    print(sorted(g.vertices))
    print(sorted(g.edges))
    print(np.array_equal(incidence_matrix, expected_incidence))

test_matrices()