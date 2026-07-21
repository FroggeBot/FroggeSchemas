from __future__ import annotations

from datetime import datetime

from .base import IDSchema

__all__ = [
    "ActivityLog",
]


class ActivityLog(IDSchema):
    guild_id: int
    actor_discord_user_id: int
    module: str
    action: str
    summary: str
    target_id: int | None = None
    created_at: datetime
