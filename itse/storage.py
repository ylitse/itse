from typing import (
    Callable,
    Dict,
    List,
    Literal,
    NamedTuple,
    Protocol,
    TypeVar,
    Union,
)


class Connection(Protocol):
    async def connect(self) -> None:
        ...

    async def disconnect(self) -> None:
        ...


StrKind: Literal["StrKind"] = "StrKind"
IntKind: Literal["IntKind"] = "IntKind"
BoolKind: Literal["BoolKind"] = "BoolKind"

Kind = Union[StrKind, IntKind, BoolKind]


class Field(NamedTuple):
    kind: Kind
    required: bool
    unique: bool


class Schema(NamedTuple):
    name: str
    fields: Dict[str, Field]


A = TypeVar("A")


class Storage(Protocol[A]):
    async def items(self) -> List[A]:
        ...

    async def get(self, identifier: str) -> A:
        ...

    async def add(self, a: A) -> str:
        ...

    async def update(self, identifier: str, a: A) -> None:
        ...


StorageMaker = Callable([Connection, Schema], Storage)