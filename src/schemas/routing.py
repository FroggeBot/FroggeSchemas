from __future__ import annotations

__all__ = [
    "Route",
    "build_custom_id",
    "parse_custom_id",
]

_SEPARATOR = ":"
_MAX_CUSTOM_ID_LENGTH = 100


class Route:
    """Builds a dotted custom_id namespace.

    Immutable, like pathlib.Path: each / returns a new Route rather
    than mutating in place.
    """

    __slots__ = ("_parts",)

    def __init__(self, *parts: str) -> None:
        self._parts = parts

    def __truediv__(self, part: str) -> Route:
        return Route(*self._parts, part)

    def __str__(self) -> str:
        return ".".join(self._parts)

    def __repr__(self) -> str:
        return f"Route({str(self)!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Route):
            return self._parts == other._parts
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self._parts)


def build_custom_id(namespace: Route | str, *args: str | int) -> str:
    namespace_str = str(namespace)
    assert _SEPARATOR not in namespace_str, f"Namespace cannot contain separator {_SEPARATOR!r}"
    parts = [namespace_str, *(str(a) for a in args)]
    for part in parts[1:]:
        assert _SEPARATOR not in part, f"Argument {part!r} cannot contain separator {_SEPARATOR!r}"

    custom_id = _SEPARATOR.join(parts)
    assert len(custom_id) <= _MAX_CUSTOM_ID_LENGTH, (
        f"custom_id {custom_id!r} is {len(custom_id)} chars, over the {_MAX_CUSTOM_ID_LENGTH} limit"
    )
    return custom_id


def parse_custom_id(custom_id: str) -> tuple[str, list[str]]:
    namespace, *args = custom_id.split(_SEPARATOR)
    return namespace, args
