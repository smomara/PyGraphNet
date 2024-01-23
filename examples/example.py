from graphent.graph import Graph
from graphent.vertex import Vertex
from graphent import visualize

graph = Graph("G")

a = Vertex('a')
b = Vertex('b')

graph.add_vertex(a)
graph.add_vertex(b)
graph.add_vertex('c')
graph.add_vertex('d')
graph.add_vertex('e')

graph.add_edge(a, b)
graph.add_edge('b', 'c')
graph.add_edge('c', 'd')
graph.add_edge('d', 'e')
graph.add_edge('e', 'a')

visualize(graph, "example")

complement = graph.get_complement()
visualize(complement, "complement")

if graph.are_isomorphic(complement):
    print("The graph and its complement are isomorphic")
else:
    print("They are not isomorphic")

graph.del_vertex('e')
visualize(graph, "minus-e")

print(f"Diameter of G: {graph.diameter()}")