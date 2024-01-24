import numpy as np
from typing import Union, Set, Optional, Iterable
from itertools import permutations
from collections import deque

class Vertex:
    def __init__(self, id: Union[int, str, float]) -> None:
        if isinstance(id, str):
            if len(id) > 1:
                raise ValueError("id must be a single character string")
            id = id.lower()
        self.id = id

    def __repr__(self) -> str:
        return f"Vertex({self.id})"

    def __lt__(self, other: Union['Vertex', int, float, str]) -> bool:
        if not isinstance(other, Vertex):
            other = Vertex(other)
        
        sid = self.id
        oid = other.id
        if isinstance(sid, str): sid = ord(sid)-ord('a') 
        if isinstance(oid, str): oid = ord(oid)-ord('a')
        return sid < oid

    def __eq__(self, other: Union['Vertex', int, float, str]) -> bool:
        if not isinstance(other, Vertex): other = Vertex(other)
        return self.id == other.id

    def __hash__(self) -> int:
        return hash((self.id, type(self.id)))
    
def get_vertex(vertex: Union[Vertex, int, float, str]) -> Vertex:
    return vertex if isinstance(vertex, Vertex) else Vertex(vertex)

class Edge:
    def __init__(self, u: Vertex, v: Vertex) -> None:
        u = get_vertex(u)
        v = get_vertex(v)
        if u == v:
            raise ValueError("loops do not exist in undirected graphs")
        self.u, self.v = sorted([u, v])

    def __repr__(self) -> str:
        return f"Edge({self.u}, {self.v})"

    def __eq__(self, other: 'Edge') -> bool:
        return {self.u, self.v} == {other.u, other.v}
    
    def __lt__(self, other: 'Edge') -> bool:
        return (self.u, self.v) < (other.u, other.v)

    def __contains__(self, vertex: Vertex) -> bool:
        vertex = get_vertex(vertex)
        return vertex in {self.u, self.v}
    
    def __hash__(self) -> int:
        return hash(frozenset([self.u, self.v]))

class Graph:
    def __init__(self, id: Union[int, str, float], vertices: Optional[Iterable[Union[Vertex, int, str, float]]] = None, edges: Optional[Iterable[Union[Edge, tuple]]] = None) -> None:
        if not (isinstance(id, (int, str, float))):
            raise ValueError("id must be of type int, char, or float")
        self.id = id
        self.vertices: Set[Vertex] = set()
        self.edges: Set[Edge] = set()

        if vertices is not None:
            for vertex in vertices:
                self.add_vertex(vertex)

        if edges is not None:
            for edge in edges:
                self.add_edge(edge)

    def order(self) -> int:
        return len(self.vertices)
    
    def size(self) -> int:
        return len(self.edges)
    
    def degree(self, vertex: Union[Vertex, int, str, float]) -> int:
        vertex = get_vertex(vertex)

        if vertex not in self.vertices:
            raise ValueError("Vertex not in graph")

        return sum(vertex in edge for edge in self.edges)

    def add_vertex(self, vertex: Union[Vertex, int, str, float]) -> None:
        vertex = get_vertex(vertex)
        self.vertices.add(vertex)
    
    def del_vertex(self, vertex: Union[Vertex, int, str, float]) -> None:
        vertex = get_vertex(vertex)
        if vertex in self.vertices:
            self.edges = {edge for edge in self.edges if vertex not in edge}
            self.vertices.remove(vertex)

    def add_edge(self, edge: Union[Edge, tuple]) -> None:
        if not isinstance(edge, Edge):
            edge = Edge(*[get_vertex(v) for v in edge])
        
        self.vertices.update([edge.u, edge.v])
        self.edges.add(edge)
    
    def del_edge(self, edge: Union[Edge, tuple]) -> None:
        if not isinstance(edge, Edge):
            edge = Edge(*[get_vertex(v) for v in edge])

        self.edges.discard(edge)

    def complement(self) -> 'Graph':
        complement_graph = Graph(f"Complement of {self.id}")

        for vertex in self.vertices:
            complement_graph.add_vertex(vertex)

        vertices_list = list(self.vertices)
        for i, u in enumerate(vertices_list):
            for v in vertices_list[i+1:]:
                if Edge(u, v) not in self:
                    complement_graph.add_edge((u, v))

        return complement_graph
    
    def geodesics(self, start: Union[Vertex, int, str, float], end: Union[Vertex, int, str, float]) -> list:
        if not isinstance(start, Vertex):
            start = Vertex(start)
        if not isinstance(end, Vertex):
            end = Vertex(end)

        if start not in self.vertices or end not in self.vertices:
            raise ValueError("Start or end vertex not in graph")

        if start == end:
            return [[start]]

        paths = []
        queue = deque([(start, [start])])
        visited = {start: 0}

        while queue:
            current_vertex, path = queue.popleft()
            if current_vertex == end:
                paths.append(path)
                continue

            for edge in self.edges:
                next_vertex = edge.v if edge.u == current_vertex else (edge.u if edge.v == current_vertex else None)
                if next_vertex and (next_vertex not in visited or visited[next_vertex] == len(path)):
                    visited[next_vertex] = len(path)
                    queue.append((next_vertex, path + [next_vertex]))

        return paths

    def distance(self, u: Union[Vertex, float, int, str], v: Union[Vertex, float, int, str]) -> int:
        if not isinstance(u, Vertex):
            u = Vertex(u)
        if not isinstance(v, Vertex):
            v = Vertex(v)
        if u == v:
            return 0
        
        # BFS
        # TODO: possible speedup?
        visited = set()
        queue = deque([(u, 0)])
        while queue:
            current_vertex, distance = queue.popleft()
            if current_vertex == v:
                return distance
            
            visited.add(current_vertex)
            for edge in self.edges:
                if edge.u == current_vertex and edge.v not in visited:
                    queue.append((edge.v, distance+1))
                elif edge.v == current_vertex and edge.u not in visited:
                    queue.append((edge.u, distance+1))
            
        return float('inf') # return infinity if no path exists
    
    def diameter(self) -> int:
        max_distance = 0
        vertex_list = list(self.vertices) # convert set to list so it can be indexed to reduce run time
        for i, u in enumerate(vertex_list):
            for v in vertex_list[i+1:]:
                if u != v:
                    distance = self.distance(u, v)
                    max_distance = max(max_distance, distance)
        return max_distance

    def adjacency_matrix(self) -> np.ndarray:
        vertex_list = sorted(self.vertices)
        index_map = {v: i for i, v in enumerate(vertex_list)}
        matrix = np.zeros((len(vertex_list), len(vertex_list)), dtype=int)

        for edge in self.edges:
            matrix[index_map[edge.u], index_map[edge.v]] = 1
            matrix[index_map[edge.v], index_map[edge.u]] = 1  # For undirected graph

        return matrix

    def incidence_matrix(self) -> np.ndarray:
        vertex_list = sorted(self.vertices)
        edge_list = sorted(self.edges) # need to sort so its same every time
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
    
    def isomorphic(self, other: 'Graph') -> bool:
        if len(self.vertices) != len(other.vertices) or len(self.edges) != len(other.edges):
            return False
        
        self_matrix = self.adjacency_matrix()
        other_matrix = other.adjacency_matrix()

        for p in permutations(range(len(self.vertices))):
            permuted = self_matrix[np.ix_(p, p)]
            if np.array_equal(permuted, other_matrix):
                return True
        return False
    
    def __contains__(self, x: Union[Edge, Vertex, int, float, str]) -> bool:
        if isinstance(x, Edge):
            for edge in self.edges:
                if x == edge: return True
            return False
        if not isinstance(x, Vertex):
            x = Vertex(x)
        return x in self.vertices
    
    def __repr__(self) -> str:
        vertices_str = ', '.join(str(v) for v in sorted(self.vertices))
        edges_str = ', '.join(str(e) for e in self.edges)
        return f"Graph {self.id}(Vertices({vertices_str}), Edges({edges_str}))"