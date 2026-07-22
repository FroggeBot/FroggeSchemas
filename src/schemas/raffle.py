from __future__ import annotations

from datetime import datetime

from pydantic import Field

from .base import BaseSchema, IDSchema

__all__ = [
    "PendingRaffleFinalization",
    "Raffle",
    "RaffleCreate",
    "RaffleEntry",
    "RaffleEntryCredit",
    "RafflePostUpsert",
    "RaffleRollResult",
    "RaffleUpdate",
]


class Raffle(IDSchema):
    guild_id: int
    created_by: int
    name: str | None = None
    cost_per_ticket: int = 100_000
    winner_pct: int = 50
    num_winners: int = 1
    auto_notify: bool = True
    channel_id: int | None = None
    message_id: int | None = None
    rolled_at: datetime | None = None
    rolled_by: int | None = None
    winner_ids: list[int] = []


class RaffleCreate(BaseSchema):
    created_by: int


class RaffleUpdate(BaseSchema):
    name: str | None = None
    cost_per_ticket: int | None = Field(default=None, ge=1, le=999_999_999)
    winner_pct: int | None = Field(default=None, ge=0, le=100)
    num_winners: int | None = Field(default=None, ge=1, le=10)
    auto_notify: bool | None = None


class RafflePostUpsert(BaseSchema):
    channel_id: int
    message_id: int


class RaffleEntry(IDSchema):
    guild_id: int
    raffle_id: int
    discord_user_id: int
    quantity: int


class RaffleEntryCredit(BaseSchema):
    discord_user_id: int
    quantity: int


class RaffleRollResult(BaseSchema):
    winners: list[int]


class PendingRaffleFinalization(IDSchema):
    guild_id: int
    raffle_id: int
