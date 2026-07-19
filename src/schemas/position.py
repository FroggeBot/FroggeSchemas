from __future__ import annotations

from .base import BaseSchema, IDSchema


class Position(IDSchema):
    guild_id: int
    name: str
    color: int | None = None
    role_id: int | None = None

class PositionCreate(BaseSchema):
    name: str
    color: int | None = None

class PositionUpdate(BaseSchema):
    name: str | None = None
    color: int | None = None
    role_id: int | None = None
