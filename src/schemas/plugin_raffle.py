from __future__ import annotations

from datetime import datetime

from .base import IDSchema


class PluginRaffleSummary(IDSchema):
    guild_id: int
    name: str | None = None
    cost_per_ticket: int
    winner_pct: int
    entrant_count: int
    total_tickets: int
    my_ticket_count: int
    is_rolled: bool
    rolled_at: datetime | None = None
    is_winner: bool
    winner_count: int
    discord_link: str | None = None
