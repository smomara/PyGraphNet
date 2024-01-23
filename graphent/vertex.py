from typing import Union

class Vertex:
    def __init__(self, id: Union[int, str, float]) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Vertex({self.id})"

    def __lt__(self, other: 'Vertex') -> bool:
        return self.id < other.id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vertex):
            other = Vertex(other)
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)