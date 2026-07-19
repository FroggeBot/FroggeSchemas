from __future__ import annotations

from .base import BaseSchema


class PluginGuild(BaseSchema):
    guild_id: int
    guild_name: str
