from __future__ import annotations

from .base import BaseSchema


class PluginPositionSummary(BaseSchema):
    id: int
    name: str

class PluginManageStaffMemberSummary(BaseSchema):
    id: int
    discord_user_id: int
    display_name: str
    is_terminated: bool

class PluginManageStaffMemberDetail(BaseSchema):
    id: int
    discord_user_id: int
    display_name: str
    is_terminated: bool
    birthday: str | None = None
    notes: str | None = None
    positions: list[PluginPositionSummary] = []

class PluginStaffingHireRequest(BaseSchema):
    discord_user_id: int
