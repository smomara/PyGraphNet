from graphviz import Graph as GVGraph
import os
import sys
from IPython.display import Image, display

def visualize(graph, filename='graph', format='png', output_dir=None, show_in_notebook=False):
    dot = GVGraph(comment=f'Graph {graph.id}')

    for vertex in graph.vertices:
        dot.node(str(vertex.id))

    for edge in graph.edges:
        dot.edge(str(edge.u.id), str(edge.v.id))

    # Set up file path
    file_path = filename
    if output_dir:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        file_path = os.path.join(output_dir, filename)

    # Render the graph
    dot.render(file_path, format=format, cleanup=True)
    print(f"Graph rendered as {file_path}.{format}")

    # If in a Jupyter notebook and show_in_notebook is True, display the graph inline
    if show_in_notebook or 'ipykernel' in sys.modules:
        display(Image(filename=f"{file_path}.{format}"))