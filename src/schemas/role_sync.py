from __future__ import annotations

from datetime import datetime
from typing import Literal

from .base import BaseSchema, IDSchema

__all__ = [
    "PendingRoleSync",
    "PendingRoleSyncCreate",
    "RoleSyncFailure",
]


# --- Role Sync (Worker-reconciled outbox for role grants/revokes) ---
class PendingRoleSyncCreate(BaseSchema):
    discord_user_id: int
    role_id: int
    action: Literal["grant", "revoke"]
    reason: str


class PendingRoleSync(IDSchema):
    guild_id: int
    discord_user_id: int
    role_id: int
    action: Literal["grant", "revoke"]
    reason: str
    created_at: datetime
    attempts: int
    last_error: str | None = None


class RoleSyncFailure(BaseSchema):
    error: str
