from __future__ import annotations

from datetime import datetime

from .base import BaseSchema, IDSchema
from .enums import ApprovalStatus, Clan, DataCenter, Gender, Orientation, Race

__all__ = [
    "MemberProfileCharacterCreate",
    "ProfileAdditionalImage",
    "ProfileAdditionalImageCreate",
    "ProfileAdditionalImageUpdate",
    "ProfileCharacter",
    "ProfileCharacterApproveRequest",
    "ProfileCharacterCreate",
    "ProfileCharacterRejectRequest",
    "ProfileCharacterUpdate",
    "ProfilePost",
    "ProfilePostUpsert",
]


class ProfileCharacter(IDSchema):
    guild_id: int
    discord_user_id: int
    is_primary: bool = False
    approval_status: ApprovalStatus = ApprovalStatus.Draft
    submitted_at: datetime | None = None
    reviewed_at: datetime | None = None
    reviewed_by: int | None = None
    rejection_reason: str | None = None

    # --- Main Info & Details ---
    character_name: str
    color: int | None = None
    jobs: str | None = None
    rates: str | None = None

    # --- Images ---
    thumbnail_url: str | None = None
    main_image_url: str | None = None

    # --- At-A-Glance ---
    world: str | None = None
    data_center: DataCenter | None = None
    gender: Gender | None = None
    gender_custom: str | None = None
    pronouns: str | None = None
    race: Race | None = None
    race_custom: str | None = None
    clan: Clan | None = None
    clan_custom: str | None = None
    orientation: Orientation | None = None
    orientation_custom: str | None = None
    height: str | None = None
    age: str | None = None
    mare_code: str | None = None

    # --- Personality ---
    likes: str | None = None
    dislikes: str | None = None
    personality: str | None = None
    about_me: str | None = None


class ProfileCharacterCreate(BaseSchema):
    discord_user_id: int
    character_name: str


class MemberProfileCharacterCreate(BaseSchema):
    """Create payload for the member-scoped router - discord_user_id comes from the caller's
    verified member token, never from the request body."""

    character_name: str


class ProfileCharacterUpdate(BaseSchema):
    character_name: str | None = None
    color: int | None = None
    jobs: str | None = None
    rates: str | None = None
    thumbnail_url: str | None = None
    main_image_url: str | None = None
    world: str | None = None
    data_center: DataCenter | None = None
    gender: Gender | None = None
    gender_custom: str | None = None
    pronouns: str | None = None
    race: Race | None = None
    race_custom: str | None = None
    clan: Clan | None = None
    clan_custom: str | None = None
    orientation: Orientation | None = None
    orientation_custom: str | None = None
    height: str | None = None
    age: str | None = None
    mare_code: str | None = None
    likes: str | None = None
    dislikes: str | None = None
    personality: str | None = None
    about_me: str | None = None


class ProfileCharacterApproveRequest(BaseSchema):
    reviewed_by: int


class ProfileCharacterRejectRequest(BaseSchema):
    reviewed_by: int
    reason: str


class ProfilePost(IDSchema):
    guild_id: int
    character_id: int
    channel_id: int
    message_id: int


class ProfilePostUpsert(BaseSchema):
    channel_id: int
    message_id: int


class ProfileAdditionalImage(IDSchema):
    guild_id: int
    character_id: int
    image_url: str
    caption: str | None = None


class ProfileAdditionalImageCreate(BaseSchema):
    image_url: str
    caption: str | None = None


class ProfileAdditionalImageUpdate(BaseSchema):
    image_url: str | None = None
    caption: str | None = None
