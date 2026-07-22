from __future__ import annotations

from .base import BaseSchema


class PluginResolveCharacterResponse(BaseSchema):
    discord_user_id: int
    character_name: str
