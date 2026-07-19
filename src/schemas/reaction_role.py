from __future__ import annotations

from .base import BaseSchema, IDSchema
from .enums import ReactionRoleMessageType

__all__ = [
    "ReactionRoleOption",
    "ReactionRoleOptionCreate",
    "ReactionRoleOptionUpdate",
    "ReactionRolePanel",
    "ReactionRolePanelCreate",
    "ReactionRolePanelPost",
    "ReactionRolePanelPostCreate",
    "ReactionRolePanelUpdate",
]


# --- Reaction Role Options ---
class ReactionRoleOption(IDSchema):
    guild_id: int
    panel_id: int
    role_id: int
    label: str | None = None
    emoji: str | None = None


class ReactionRoleOptionCreate(BaseSchema):
    role_id: int


class ReactionRoleOptionUpdate(BaseSchema):
    label: str | None = None
    emoji: str | None = None


# --- Reaction Role Panels ---
class ReactionRolePanel(IDSchema):
    guild_id: int
    title: str | None = None
    description: str | None = None
    thumbnail_url: str | None = None
    color: int | None = None
    message_type: ReactionRoleMessageType = ReactionRoleMessageType.Normal


class ReactionRolePanelCreate(BaseSchema):
    title: str


class ReactionRolePanelUpdate(BaseSchema):
    title: str | None = None
    description: str | None = None
    thumbnail_url: str | None = None
    color: int | None = None
    message_type: ReactionRoleMessageType | None = None


# --- Reaction Role Panel Posts ---
class ReactionRolePanelPost(IDSchema):
    guild_id: int
    panel_id: int
    channel_id: int
    message_id: int


class ReactionRolePanelPostCreate(BaseSchema):
    panel_id: int
    channel_id: int
    message_id: int
