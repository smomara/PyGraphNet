from pygraphnet import Graph

"""
graph operations
    union (TODO)
    cross_product
    complement
"""

__all__ = ['cross_product', 'complement']

def cross_product(g1, g2):
    """
    Creates the Cartesian product of two graphs. If either of the input graphs is directed,
    the resulting graph will also be directed. For undirected edges from an undirected graph,
    edges will be added bidirectionally in the resulting graph if it is directed.

    Parameters:
        g1 (Graph): The first input graph, can be either directed or undirected.
        g2 (Graph): The second input graph, can be either directed or undirected.

    Returns:
        Graph: A new graph representing the Cartesian product of g1 and g2. The graph will be
               directed if either of the input graphs is directed.
    """

    # Determine if the resulting graph should be directed
    directed_result = g1.directed or g2.directed
    result = Graph(directed=directed_result)

    for v1 in g1.vertices:
        for v2 in g2.vertices:
            # For each edge in g1, add corresponding edges in the product
            for u1 in g1.adj_list[v1]:
                result.add_edge((v1, v2), (u1, v2), bidirectional=((not g1.directed) and directed_result))
            # For each edge in g2, add corresponding edges in the product
            for u2 in g2.adj_list[v2]:
                result.add_edge((v1, v2), (v1, u2), bidirectional=((not g2.directed) and directed_result))

    return result

def complement(g):
    """
    Creates the complement of a graph, whether directed or undirected.

    For an undirected graph, two vertices are connected in the complement if they are not connected in the original graph.
    For a directed graph, an edge from u to v exists in the complement if and only if such an edge does not exist in the original graph.

    Parameters:
        g (Graph): The input graph, can be either directed or undirected.

    Returns:
        Graph: The complement of the input graph, preserving the directedness of the input.
    """

    # preserve directedness
    result = Graph(directed=g.directed)

    for v in g.vertices:
        result.add_vertex(v)

    for v in g.vertices:
        for u in g.vertices:
            if v != u: # skip self-loops
                if g.directed:
                    # just check one direction for directed
                    if u not in g.adj_list[v]:
                        result.add_edge(v, u)
                else:
                    # check edge absence in both directions for undirected graphs
                    if (v not in g.adj_list[u] and u not in g.adj_list[v] and
                        v not in result.adj_list[u] and u not in result.adj_list[v]):
                        result.add_edge(v, u)
    
    return result