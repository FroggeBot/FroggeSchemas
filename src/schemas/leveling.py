from __future__ import annotations

import math
from datetime import datetime

from .base import BaseSchema, IDSchema

__all__ = [
    "LevelingAwardResult",
    "LevelingMember",
    "LevelingMessageXpRequest",
    "LevelingProgress",
    "LevelingRoleReward",
    "LevelingRoleRewardCreate",
    "LevelingSettings",
    "LevelingSettingsUpdate",
    "LevelingVoiceSessionClosed",
    "LevelingVoiceSessionStart",
    "LevelingVoiceXpRequest",
    "level_for_total_xp",
    "total_xp_for_level",
    "xp_progress",
]


# --- XP curve (pure functions, no I/O) ---
# The one place this curve is defined - imported by both the API's award_xp (level-diff
# bookkeeping) and the Bot's /rank display, so they can never drift out of sync with each other.
# Cumulative XP required to reach a level: the gap between consecutive levels grows linearly
# (55 XP for 0->1, 65 for 1->2, 75 for 2->3, ...) - fast early levels, slower later ones. Not
# admin-configurable in v1 (a deliberate scope cut).
def total_xp_for_level(level: int) -> int:
    if level <= 0:
        return 0
    return 5 * level * level + 50 * level


def level_for_total_xp(total_xp: int) -> int:
    """Inverse of total_xp_for_level via the quadratic formula (closed-form, O(1)), with a
    boundary-correction loop to guard against integer-sqrt truncation at the edges."""
    if total_xp <= 0:
        return 0
    level = (-50 + math.isqrt(2500 + 20 * total_xp)) // 10
    while total_xp_for_level(level + 1) <= total_xp:
        level += 1
    while level > 0 and total_xp_for_level(level) > total_xp:
        level -= 1
    return level


class LevelingProgress(BaseSchema):
    level: int
    total_xp: int
    xp_into_level: int
    xp_for_next_level: int


def xp_progress(total_xp: int) -> LevelingProgress:
    level = level_for_total_xp(total_xp)
    floor = total_xp_for_level(level)
    ceiling = total_xp_for_level(level + 1)
    return LevelingProgress(
        level=level, total_xp=total_xp, xp_into_level=total_xp - floor, xp_for_next_level=ceiling - floor
    )


# --- Settings ---
class LevelingSettings(BaseSchema):
    enabled: bool = False
    xp_min: int = 15
    xp_max: int = 25
    message_cooldown_seconds: int = 60
    voice_xp_per_minute: int = 5
    require_other_member_in_voice: bool = True
    excluded_channel_ids: list[int] = []
    excluded_role_ids: list[int] = []
    announcement_channel_id: int | None = None


class LevelingSettingsUpdate(BaseSchema):
    enabled: bool | None = None
    xp_min: int | None = None
    xp_max: int | None = None
    message_cooldown_seconds: int | None = None
    voice_xp_per_minute: int | None = None
    require_other_member_in_voice: bool | None = None
    excluded_channel_ids: list[int] | None = None
    excluded_role_ids: list[int] | None = None
    announcement_channel_id: int | None = None


# --- Members ---
class LevelingMember(IDSchema):
    guild_id: int
    discord_user_id: int
    total_xp: int
    last_message_at: datetime | None = None


class LevelingAwardResult(BaseSchema):
    """Returned by every XP-granting call - single source of truth for whether the Bot should fire
    a role-grant/announcement, mirroring FinancePayoutService.mark_paid's discipline of the
    mutation method itself deciding+reporting the state transition, not the caller re-deriving it."""

    member: LevelingMember
    previous_level: int
    new_level: int
    leveled_up: bool


# --- Award request bodies ---
class LevelingMessageXpRequest(BaseSchema):
    amount: int
    cooldown_seconds: int


class LevelingVoiceXpRequest(BaseSchema):
    amount: int


# --- Voice sessions ---
# Deliberately not a full mirror of LevelingVoiceSessionModel - just the two fields the Bot
# actually needs back to compute elapsed minutes itself (which channel, when it started).
class LevelingVoiceSessionStart(BaseSchema):
    channel_id: int


class LevelingVoiceSessionClosed(BaseSchema):
    channel_id: int
    started_at: datetime


# --- Role rewards ---
class LevelingRoleReward(IDSchema):
    guild_id: int
    level: int
    role_id: int


class LevelingRoleRewardCreate(BaseSchema):
    level: int
    role_id: int
