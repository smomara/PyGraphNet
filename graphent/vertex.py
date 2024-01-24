from typing import Union

class Vertex:
    def __init__(self, id: Union[int, str, float]) -> None:
        if isinstance(id, str):
            if len(id) > 1:
                raise ValueError("id must be a single character string")
            id = id.lower()
        self.id = id

    def __str__(self) -> str:
        return f"Vertex({self.id})"

    def __lt__(self, other: Union['Vertex', int, float, str]) -> bool:
        if not isinstance(other, Vertex):
            other = Vertex(other)
        
        sid = self.id
        oid = other.id
        if isinstance(sid, str): sid = ord(sid)-ord('a') 
        if isinstance(oid, str): oid = ord(oid)-ord('a')
        print(sid, oid)
        return sid < oid

    def __eq__(self, other: Union['Vertex', int, float, str]) -> bool:
        if not isinstance(other, Vertex):
            other = Vertex(other)

        return self.id == other.id and type(self.id) == type(other.id)

    def __hash__(self) -> int:
        return hash((self.id, type(self.id)))