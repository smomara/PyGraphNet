from graphviz import Graph as GVGraph
import os
import sys
from IPython.display import Image, display
from graphent.graph import Graph

def visualize(graph: Graph, filename=None, format='png', output_dir=None, notebook=True):
    if not filename:
        filename = str(graph.id) if graph.id else "graph"
    dot = GVGraph(comment=f'Graph {graph.id}')

    for vertex in graph.vertices:
        dot.node(str(vertex.id))

    for edge in graph.edges:
        dot.edge(str(edge.u.id), str(edge.v.id))

    file_path = filename
    if output_dir:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        file_path = os.path.join(output_dir, filename)

    dot.render(file_path, format=format, cleanup=True)

    if notebook or 'ipykernel' in sys.modules:
        # Display the graph inline if in a Jupyter notebook
        display(Image(filename=f"{file_path}.{format}"))
    else:
        print(f"Graph rendered as {file_path}.{format}")

def path(n: int) -> Graph:
    vertices = [str(i+1) for i in range(n)]
    edges = [(u, v) for u, v in zip(vertices, vertices[1:])]
    p = Graph(f"P{n}", vertices=vertices, edges=edges)
    return p

def cycle(n: int) -> Graph:
    vertices = [str(i+1) for i in range(n)]
    edges = [(u, v) for u, v in zip(vertices, vertices[1:] + [vertices[0]])]
    c = Graph(f"C{n}", vertices=vertices, edges=edges)
    return c

def complete_graph(n: int) -> Graph:
    vertices = [str(i+1) for i in range(n)]
    edges = [(u, v) for i, u in enumerate(vertices) for v in vertices[i+1:]]
    k = Graph(f"K{n}", vertices=vertices, edges=edges)
    return k