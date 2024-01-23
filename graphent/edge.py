from graphent.vertex import Vertex
    
class Edge:
    def __init__(self, u: Vertex, v: Vertex) -> None:
        self.u = u
        self.v = v

    def __str__(self) -> str:
        return f"Edge({self.u}, {self.v})"

    def __eq__(self, other: 'Edge') -> bool:
        return self.u == other.u and self.v == other.v or self.u == other.v and self.v == other.u
    
    def __hash__(self) -> int:
        return hash((self.u, self.v))