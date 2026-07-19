from __future__ import annotations

from datetime import datetime

from .base import IDSchema


class PluginGiveawaySummary(IDSchema):
    guild_id: int
    name: str | None = None
    prize: str | None = None
    end_at: datetime | None = None
    entrant_count: int
    is_entered: bool
    is_rolled: bool
    rolled_at: datetime | None = None
    is_winner: bool
    winner_count: int
    discord_link: str | None = None
