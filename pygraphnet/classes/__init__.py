__all__ = ["Graph"]

class Graph:
    """Graph class

    This class supports directed or undirected graphs and can initialize graphs from
    different data formats, including another graph object, an edge list, and an adjacency list.
    """

    def __init__(self, data=None, directed=False):
        self.directed = directed
        self.vertices = set()
        self.edges = set()
        self.adj_list = {}

        # Initialize graph with various data formats
        if isinstance(data, Graph):
            self._init_from_graph(data)
        elif isinstance(data, int):
            self._init_empty_graph(data)
        elif isinstance(data, dict):
            self._init_from_adj_list(data)
        elif hasattr(data, '__iter__'):
            self._init_from_edge_list(data)

    # Graph initialization methods
    def _init_from_graph(self, graph):
        self.directed = graph.directed
        self.vertices = set(graph.vertices)
        self.edges = set(graph.edges)
        self.adj_list = {v: set(neighbors) for v, neighbors in graph.adj_list.items()}

    def _init_empty_graph(self, num_vertices):
        self.vertices = set(range(num_vertices))
        self.adj_list = {v: set() for v in self.vertices}

    def _init_from_adj_list(self, adj_list):
        for v, neighbors in adj_list.items():
            self.add_vertex(v)
            for u in neighbors:
                self.add_vertex(u)
                self.add_edge(v, u)

    def _init_from_edge_list(self, edge_list):
        for v, u in edge_list:
            self.add_vertex(v)
            self.add_vertex(u)
            self.add_edge(v, u)

    # Vertex and edge management
    def add_vertex(self, v):
        self.vertices.add(v)
        if v not in self.adj_list:
            self.adj_list[v] = set()

    def del_vertex(self, v):
        """Remove a vertex and all its associated edges"""
        if v not in self.vertices:
            return
        
        self.vertices.remove(v)

        edges_to_remove = set()
        for edge in self.edges:
            if v in edge:
                edges_to_remove.add(edge)

        for edge in edges_to_remove:
            self.edges.remove(edge)

        self.adj_list.pop(v, None)
        for neighbors in self.adj_list.values():
            neighbors.discard(v)

    def add_edge(self, v, u, bidirectional=False):
        """
        Adds an edge to the graph. If the graph is directed, or bidirectional is False, adds a single directed edge.
        If the graph is undirected or bidirectional is True, adds edges in both directions.

        Parameters:
            v: The starting vertex of the edge.
            u: The ending vertex of the edge.
            bidirectional (bool): If True and the resulting graph is directed, adds the edge in both directions.
                                  This parameter is ignored if the graph is undirected.
        """

        if v not in self.vertices:
            self.add_vertex(v)
        if u not in self.vertices:
            self.add_vertex(u)
            
        if self.directed:
            self.edges.add((v, u))
            self.adj_list[v].add(u)
            if bidirectional:
                self.edges.add((u, v))
                self.adj_list[u].add(v)
        else:
            self.edges.add((v, u))
            self.adj_list[v].add(u)
            self.adj_list[u].add(v)
    
    def del_edge(self, v, u):
        """Remove an edge from the graph"""
        if (v, u) not in self.edges:
            return

        self.edges.remove((v, u))

        if v in self.adj_list:
            self.adj_list[v].discard(u)
        if not self.directed and u in self.adj_list:
            self.adj_list[u].discard(v)