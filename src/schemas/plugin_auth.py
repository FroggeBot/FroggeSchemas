from __future__ import annotations

from datetime import datetime

from .base import BaseSchema


class PluginPairingCodeCreate(BaseSchema):
    discord_user_id: int
    discord_username: str | None = None

class PluginPairingCodeIssued(BaseSchema):
    code: str
    expires_at: datetime

class PluginTokenRedeemRequest(BaseSchema):
    code: str

class PluginTokenRedeemed(BaseSchema):
    token: str
    discord_user_id: int
    discord_username: str | None = None

class PluginAuthMe(BaseSchema):
    discord_user_id: int
    discord_username: str | None = None
