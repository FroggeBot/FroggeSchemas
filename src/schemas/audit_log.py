from __future__ import annotations

from .base import BaseSchema

__all__ = [
    "AuditLogSettings",
    "AuditLogSettingsUpdate",
]


class AuditLogSettings(BaseSchema):
    guild_id: int
    channel_id: int | None = None

    # Message Events
    log_message_deleted: bool = False
    color_message_deleted: int | None = None
    log_message_edited: bool = False
    color_message_edited: int | None = None

    # Join/Leave
    log_member_joined: bool = False
    color_member_joined: int | None = None
    log_member_left: bool = False
    color_member_left: int | None = None

    # Server
    log_channel_created: bool = False
    color_channel_created: int | None = None
    log_channel_updated: bool = False
    color_channel_updated: int | None = None
    log_channel_deleted: bool = False
    color_channel_deleted: int | None = None
    log_role_created: bool = False
    color_role_created: int | None = None
    log_role_updated: bool = False
    color_role_updated: int | None = None
    log_role_deleted: bool = False
    color_role_deleted: int | None = None
    log_server_updated: bool = False
    color_server_updated: int | None = None
    log_emoji_updated: bool = False
    color_emoji_updated: int | None = None

    # Members
    log_member_name_changed: bool = False
    color_member_name_changed: int | None = None
    log_member_avatar_changed: bool = False
    color_member_avatar_changed: int | None = None
    log_member_banned: bool = False
    color_member_banned: int | None = None
    log_member_unbanned: bool = False
    color_member_unbanned: int | None = None
    log_member_timed_out: bool = False
    color_member_timed_out: int | None = None
    log_member_timeout_removed: bool = False
    color_member_timeout_removed: int | None = None

    # Voice
    log_voice_joined: bool = False
    color_voice_joined: int | None = None
    log_voice_moved: bool = False
    color_voice_moved: int | None = None
    log_voice_left: bool = False
    color_voice_left: int | None = None


class AuditLogSettingsUpdate(BaseSchema):
    channel_id: int | None = None

    log_message_deleted: bool | None = None
    color_message_deleted: int | None = None
    log_message_edited: bool | None = None
    color_message_edited: int | None = None

    log_member_joined: bool | None = None
    color_member_joined: int | None = None
    log_member_left: bool | None = None
    color_member_left: int | None = None

    log_channel_created: bool | None = None
    color_channel_created: int | None = None
    log_channel_updated: bool | None = None
    color_channel_updated: int | None = None
    log_channel_deleted: bool | None = None
    color_channel_deleted: int | None = None
    log_role_created: bool | None = None
    color_role_created: int | None = None
    log_role_updated: bool | None = None
    color_role_updated: int | None = None
    log_role_deleted: bool | None = None
    color_role_deleted: int | None = None
    log_server_updated: bool | None = None
    color_server_updated: int | None = None
    log_emoji_updated: bool | None = None
    color_emoji_updated: int | None = None

    log_member_name_changed: bool | None = None
    color_member_name_changed: int | None = None
    log_member_avatar_changed: bool | None = None
    color_member_avatar_changed: int | None = None
    log_member_banned: bool | None = None
    color_member_banned: int | None = None
    log_member_unbanned: bool | None = None
    color_member_unbanned: int | None = None
    log_member_timed_out: bool | None = None
    color_member_timed_out: int | None = None
    log_member_timeout_removed: bool | None = None
    color_member_timeout_removed: int | None = None

    log_voice_joined: bool | None = None
    color_voice_joined: int | None = None
    log_voice_moved: bool | None = None
    color_voice_moved: int | None = None
    log_voice_left: bool | None = None
    color_voice_left: int | None = None
