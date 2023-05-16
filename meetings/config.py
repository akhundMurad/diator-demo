import os
from dataclasses import dataclass, field
from typing import Type, Any, TypeVar
from functools import partial


T = TypeVar("T")


def _get_from_env(var_name: str, type_: Type[T], *, default: Any | None = None) -> T:
    value = os.getenv(var_name, default)
    return type_(value)  # type: ignore


@dataclass(frozen=True, kw_only=True)
class DatabaseConfig:
    connection_string: str = field(
        default_factory=partial(_get_from_env, var_name="DATABASE_CONNECTION_STRING", type_=str)
    )
