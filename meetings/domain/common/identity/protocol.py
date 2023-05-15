from typing import Callable, Protocol, TypeVar

IdentityType = TypeVar("IdentityType", covariant=True)


class IdentityProtocol(Protocol[IdentityType]):
    @property
    def value_generator(self) -> Callable[[], IdentityType]:
        raise NotImplementedError

    @property
    def value(self) -> IdentityType:
        raise NotImplementedError

    @classmethod
    def from_string(cls, plain_str: str) -> "IdentityProtocol":
        raise NotImplementedError

    def __eq__(self, identity: "IdentityProtocol") -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
