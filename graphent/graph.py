import numpy as np
from typing import Union, Set
from graphviz import Graph as GVGraph
from itertools import permutations

from graphent.vertex import Vertex
from graphent.edge import Edge

class Graph:
    def __init__(self, id: Union[int, str, float]) -> None:
        self.id = id
        self.vertices: Set[Vertex] = set()
        self.edges: Set[Edge] = set()

    def add_vertex(self, vertex: Union[Vertex, int, str, float]) -> Vertex:
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)
        self.vertices.add(vertex)
        return vertex

    def add_edge(self, u: Union[Vertex, int, str, float], v: Union[Vertex, int, str, float]) -> Edge:
        u = self.add_vertex(u)
        v = self.add_vertex(v)
        edge = Edge(u, v)
        if not self.is_edge(edge):
            self.edges.add(edge)
        return edge
    
    def is_edge(self, e: Edge) -> bool:
        for edge in self.edges:
            if edge == e:
                return True
        return False

    def get_complement(self) -> 'Graph':
        complement_graph = Graph(f"Complement of {self.id}")

        for vertex in self.vertices:
            complement_graph.add_vertex(vertex)

        for u in self.vertices:
            for v in self.vertices:
                if u != v and not self.is_edge(Edge(u, v)):
                    complement_graph.add_edge(u, v)

        return complement_graph

    def get_adjacency_matrix(self) -> np.ndarray:
        vertex_list = sorted(self.vertices)
        index_map = {v: i for i, v in enumerate(vertex_list)}
        matrix = np.zeros((len(vertex_list), len(vertex_list)), dtype=int)

        for edge in self.edges:
            matrix[index_map[edge.u], index_map[edge.v]] = 1
            matrix[index_map[edge.v], index_map[edge.u]] = 1  # For undirected graph

        return matrix

    def get_incidence_matrix(self) -> np.ndarray:
        vertex_list = sorted(self.vertices)
        edge_list = list(self.edges)
        vertex_index_map = {v: i for i, v in enumerate(vertex_list)}
        edge_index_map = {e: i for i, e in enumerate(edge_list)}
        matrix = np.zeros((len(vertex_list), len(edge_list)), dtype=int)

        for edge in self.edges:
            u_index = vertex_index_map[edge.u]
            v_index = vertex_index_map[edge.v]
            e_index = edge_index_map[edge]
            matrix[u_index, e_index] = 1
            matrix[v_index, e_index] = 1

        return matrix
    
    def are_isomorphic(self, other: 'Graph') -> bool:
        if len(self.vertices) != len(other.vertices) or len(self.edges) != len(other.edges):
            return False
        
        self_matrix = self.get_adjacency_matrix()
        other_matrix = other.get_adjacency_matrix()

        for p in permutations(range(len(self.vertices))):
            permuted = self_matrix[np.ix_(p, p)]
            if np.array_equal(permuted, other_matrix):
                return True
        return False

    
    def visualize(self, filename='graph', format='png'):
        dot = GVGraph(comment=f'Graph {self.id}')

        for vertex in self.vertices:
            dot.node(str(vertex.id))

        for edge in self.edges:
            dot.edge(str(edge.u.id), str(edge.v.id))

        dot.render(filename, format=format, cleanup=True)
        print(f"Graph rendered as {filename}.{format}")

    def __str__(self) -> str:
        vertices_str = ', '.join(str(v) for v in sorted(self.vertices))
        edges_str = ', '.join(str(e) for e in self.edges)
        return f"Graph {self.id}(Vertices({vertices_str}), Edges({edges_str}))"