from __future__ import annotations

from datetime import datetime

from .base import BaseSchema


class PluginVIPMembership(BaseSchema):
    guild_id: int
    guild_name: str
    tier_name: str
    expires_at: datetime | None = None

class PluginVIPHistoryPeriod(BaseSchema):
    tier_name: str
    started_at: datetime
    ended_at: datetime | None = None
    ended_reason: str | None = None

class PluginVIPPerkStatus(BaseSchema):
    text: str
    redemption_status: str
