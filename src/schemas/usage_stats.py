from __future__ import annotations

from datetime import datetime

from .base import BaseSchema

__all__ = [
    "CommandUsageRecord",
    "CommandUsageStat",
    "GuildGrowthBucket",
    "InteractionUsageRecord",
    "InteractionUsageStat",
]


class CommandUsageRecord(BaseSchema):
    command_name: str


class CommandUsageStat(BaseSchema):
    command_name: str
    use_count: int
    last_used_at: datetime


class InteractionUsageRecord(BaseSchema):
    namespace: str


class InteractionUsageStat(BaseSchema):
    namespace: str
    use_count: int
    last_used_at: datetime


class GuildGrowthBucket(BaseSchema):
    month: str
    new_guilds: int
    cumulative_total: int
