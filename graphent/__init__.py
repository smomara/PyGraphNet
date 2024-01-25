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