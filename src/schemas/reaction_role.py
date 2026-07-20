from __future__ import annotations

from .base import BaseSchema, IDSchema
from .enums import ReactionRoleMessageType
from .routing import Route

__all__ = [
    "OPTION_CLICK",
    "ReactionRoleOption",
    "ReactionRoleOptionCreate",
    "ReactionRoleOptionUpdate",
    "ReactionRolePanel",
    "ReactionRolePanelCreate",
    "ReactionRolePanelPost",
    "ReactionRolePanelPostCreate",
    "ReactionRolePanelPostRequest",
    "ReactionRolePanelPostRequestCreate",
    "ReactionRolePanelUpdate",
]

# The actual per-click role grant/remove handler, dispatched from the live posted message itself -
# shared with Bot/src/bot/cogs/reaction_roles/constants.py (which imports this rather than
# defining its own copy) and with DiscordUI's render_panel_post, since Worker needs the identical
# route to build a working button without depending on the Bot package at all.
OPTION_CLICK = Route("reaction_roles") / "option" / "click"


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


# --- Reaction Role Panel Post Requests ---
# A lightweight queue: the Dashboard creates one to ask for a panel to be posted to a channel;
# a Worker sweep (reaction_role_post_sweep.py) polls for pending requests, does the actual send,
# registers the resulting ReactionRolePanelPost via the existing endpoint, then deletes the
# request. Exists because the Dashboard has no safe way to build a live interactive Components V2
# message itself (see the Reaction Roles Bot-Mediated Channel Posting plan).
class ReactionRolePanelPostRequest(IDSchema):
    guild_id: int
    panel_id: int
    channel_id: int


class ReactionRolePanelPostRequestCreate(BaseSchema):
    channel_id: int
