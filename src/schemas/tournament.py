from __future__ import annotations

from datetime import datetime

from .base import BaseSchema, IDSchema
from .enums import TournamentStatus

__all__ = [
    "Tournament",
    "TournamentCreate",
    "TournamentEntrant",
    "TournamentEntrantCreate",
    "TournamentMatch",
    "TournamentMatchResultReport",
    "TournamentPostUpsert",
    "TournamentUpdate",
]


class Tournament(IDSchema):
    guild_id: int
    created_by: int
    name: str | None = None
    description: str | None = None
    thumbnail_url: str | None = None
    color: int | None = None
    emoji: str | None = None
    status: TournamentStatus = TournamentStatus.SignupsOpen
    channel_id: int | None = None
    message_id: int | None = None
    bracket_generated_at: datetime | None = None
    winner_entrant_id: int | None = None


class TournamentCreate(BaseSchema):
    created_by: int


class TournamentUpdate(BaseSchema):
    name: str | None = None
    description: str | None = None
    thumbnail_url: str | None = None
    color: int | None = None
    emoji: str | None = None


class TournamentPostUpsert(BaseSchema):
    channel_id: int
    message_id: int


class TournamentEntrant(IDSchema):
    guild_id: int
    tournament_id: int
    discord_user_id: int


class TournamentEntrantCreate(BaseSchema):
    discord_user_id: int


class TournamentMatch(IDSchema):
    guild_id: int
    tournament_id: int
    round_number: int
    slot_in_round: int
    entrant_a_id: int | None = None
    entrant_b_id: int | None = None
    winner_entrant_id: int | None = None
    is_bye: bool = False


class TournamentMatchResultReport(BaseSchema):
    winner_entrant_id: int
