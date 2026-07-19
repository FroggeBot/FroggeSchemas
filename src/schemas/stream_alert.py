from __future__ import annotations

from datetime import datetime

from .base import BaseSchema, IDSchema

__all__ = [
    "TrackedStream",
    "TrackedStreamCreate",
    "TrackedStreamLiveUpdate",
    "TrackedStreamSyncTarget",
    "TrackedStreamUpdate",
]


class TrackedStream(IDSchema):
    guild_id: int
    twitch_username: str
    channel_id: int
    role_id: int | None = None
    live_since: datetime | None = None


class TrackedStreamCreate(BaseSchema):
    twitch_username: str
    channel_id: int
    role_id: int | None = None


class TrackedStreamUpdate(BaseSchema):
    channel_id: int | None = None
    role_id: int | None = None


class TrackedStreamLiveUpdate(BaseSchema):
    live_since: datetime | None


class TrackedStreamSyncTarget(BaseSchema):
    guild_id: int
    id: int
    twitch_username: str
    channel_id: int
    role_id: int | None
    live_since: datetime | None
