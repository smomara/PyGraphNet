from graphent.vertex import Vertex
    
class Edge:
    def __init__(self, u: Vertex, v: Vertex) -> None:
        if u == v:
            raise ValueError("loops do not exist in undirected graphs")
        self.u = u
        self.v = v

    def __str__(self) -> str:
        return f"Edge({self.u}, {self.v})"

    def __eq__(self, other: 'Edge') -> bool:
        return (self.u == other.u and self.v == other.v) or (self.u == other.v and self.v == other.u)

    def __contains__(self, vertex: Vertex) -> bool:
        return self.u == vertex or self.v == vertex
    
    def __hash__(self) -> int:
        return hash((self.u, self.v))