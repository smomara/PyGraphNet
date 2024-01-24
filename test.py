import numpy as np
from graphent.graph import Graph, Edge, Vertex

va = Vertex('a')
edge_a, edge_b = Edge(va, 'b'), Edge('b', 'a')
print(edge_a == edge_b)