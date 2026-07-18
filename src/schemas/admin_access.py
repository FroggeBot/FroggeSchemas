from __future__ import annotations

from .base import BaseSchema


class AdminAccessConfig(BaseSchema):
    role_ids: list[int]
    user_ids: list[int]

class AdminRoleCreate(BaseSchema):
    role_id: int

class AdminUserCreate(BaseSchema):
    discord_user_id: int
