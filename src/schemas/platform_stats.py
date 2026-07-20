from __future__ import annotations

from .base import BaseSchema


class PlatformStats(BaseSchema):
    guild_count: int
    active_vip_count: int
    upcoming_event_count: int
    approved_character_count: int
    active_staff_count: int
