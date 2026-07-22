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

class PluginVipTierSummary(BaseSchema):
    id: int
    name: str
    cost: int

class PluginVipMemberSummary(BaseSchema):
    id: int
    discord_user_id: int
    display_name: str
    tier_name: str
    expires_at: datetime | None = None

class PluginVipMemberDetail(BaseSchema):
    id: int
    discord_user_id: int
    display_name: str
    tier_id: int
    tier_name: str
    expires_at: datetime | None = None
    notes: str | None = None

class PluginVipAssignRequest(BaseSchema):
    discord_user_id: int
    tier_id: int
