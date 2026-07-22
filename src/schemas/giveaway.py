from __future__ import annotations

from datetime import datetime

from pydantic import Field

from .base import BaseSchema, IDSchema

__all__ = [
    "Giveaway",
    "GiveawayCreate",
    "GiveawayEntryCreate",
    "GiveawayEventUpsert",
    "GiveawayPostUpsert",
    "GiveawayRollResult",
    "GiveawayUpdate",
    "PendingGiveawayFinalization",
]


class Giveaway(IDSchema):
    guild_id: int
    created_by: int
    name: str | None = None
    description: str | None = None
    prize: str | None = None
    thumbnail_url: str | None = None
    color: int | None = None
    emoji: str | None = None
    end_at: datetime | None = None
    num_winners: int = 1
    auto_notify: bool = True
    post_to_channel: bool = False
    create_discord_event: bool = False
    channel_id: int | None = None
    message_id: int | None = None
    discord_event_id: int | None = None
    rolled_at: datetime | None = None
    rolled_by: int | None = None
    winner_ids: list[int] = []


class GiveawayCreate(BaseSchema):
    created_by: int


class GiveawayUpdate(BaseSchema):
    name: str | None = None
    description: str | None = None
    prize: str | None = None
    thumbnail_url: str | None = None
    color: int | None = None
    emoji: str | None = None
    end_at: datetime | None = None
    num_winners: int | None = Field(default=None, ge=1, le=10)
    auto_notify: bool | None = None
    post_to_channel: bool | None = None
    create_discord_event: bool | None = None


class GiveawayPostUpsert(BaseSchema):
    channel_id: int
    message_id: int


class GiveawayEventUpsert(BaseSchema):
    discord_event_id: int


class GiveawayEntryCreate(BaseSchema):
    discord_user_id: int


class GiveawayRollResult(BaseSchema):
    winners: list[int]


class PendingGiveawayFinalization(IDSchema):
    guild_id: int
    giveaway_id: int
