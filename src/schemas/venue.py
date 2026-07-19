from __future__ import annotations

from datetime import datetime

from .base import BaseSchema

__all__ = [
    "VenueLink",
    "VenueLinkPostUpsert",
    "VenueLinkSnapshotUpdate",
    "VenueLinkSyncTarget",
    "VenueLinkUpsert",
    "VenueNotice",
    "VenueSnapshot",
]

class VenueNotice(BaseSchema):
    message: str
    type: str

class VenueSnapshot(BaseSchema):
    name: str
    banner_uri: str | None = None
    description: str
    location_text: str
    website: str | None = None
    discord_invite: str | None = None
    hiring: bool = False
    sfw: bool = True
    tags: list[str] = []
    approved: bool = True
    is_open_now: bool
    next_change_at: datetime | None = None
    active_notices: list[VenueNotice] = []

class VenueLink(BaseSchema):
    guild_id: int
    ffxivvenues_id: str
    channel_id: int | None = None
    message_id: int | None = None
    last_synced_at: datetime | None = None
    snapshot: VenueSnapshot | None = None

class VenueLinkUpsert(BaseSchema):
    ffxivvenues_id: str
    snapshot: VenueSnapshot

class VenueLinkPostUpsert(BaseSchema):
    channel_id: int
    message_id: int

class VenueLinkSnapshotUpdate(BaseSchema):
    snapshot: VenueSnapshot

class VenueLinkSyncTarget(BaseSchema):
    guild_id: int
    ffxivvenues_id: str
    channel_id: int | None
    message_id: int | None
