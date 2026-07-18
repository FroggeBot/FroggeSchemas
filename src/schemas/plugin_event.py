from __future__ import annotations

from datetime import datetime

from .base import BaseSchema, IDSchema


class PluginEventGuild(BaseSchema):
    guild_id: int
    guild_name: str

class PluginEventSummary(IDSchema):
    guild_id: int
    name: str
    description: str | None = None
    start_at: datetime
    end_at: datetime | None = None
    image_url: str | None = None

class PluginShiftDetail(IDSchema):
    start_at: datetime
    end_at: datetime
    capacity: int
    signup_count: int
    is_signed_up: bool
    is_locked: bool

class PluginPositionDetail(BaseSchema):
    position_name: str
    shifts: list[PluginShiftDetail]

class PluginEventDetail(PluginEventSummary):
    positions: list[PluginPositionDetail]
