from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from .base import BaseSchema, IDSchema
from .enums import DisplayType, RedemptionLevel, Repeatability, VIPMessageTemplateType

__all__ = [
    "DisplayType",
    "RedemptionLevel",
    "Repeatability",
    "VIPDisplayPost",
    "VIPDisplayPostCreate",
    "VIPMember",
    "VIPMemberCreate",
    "VIPMembership",
    "VIPMembershipMarkSentUpdate",
    "VIPMemberUpdate",
    "VIPMessageTemplate",
    "VIPMessageTemplateEffective",
    "VIPMessageTemplateType",
    "VIPMessageTemplateUpdate",
    "VIPPerk",
    "VIPPerkCreate",
    "VIPPerkRedemption",
    "VIPPerkRedemptionBulkUpdate",
    "VIPPerkUpdate",
    "VIPTier",
    "VIPTierCreate",
    "VIPTierUpdate",
    "PendingVipRoleSync",
    "PendingVipRoleSyncCreate",
    "VipRoleSyncFailure",
    "render_vip_message_template",
]


# --- VIP Tiers ---
class VIPTier(IDSchema):
    guild_id: int
    name: str
    cost: int = Field(default=0, ge=0)
    role_id: int
    color: int | None = None


class VIPTierCreate(BaseSchema):
    name: str
    cost: int = Field(default=0, ge=0)
    role_id: int
    color: int | None = None


class VIPTierUpdate(BaseSchema):
    name: str | None = None
    cost: int | None = Field(default=None, ge=0)
    role_id: int | None = None
    color: int | None = None


# --- VIP Members ---
class VIPMember(IDSchema):
    guild_id: int
    discord_user_id: int
    tier_id: int
    expires_at: datetime | None = None
    name: str | None = None
    notes: str | None = None
    tier: VIPTier


class VIPMemberCreate(BaseSchema):
    discord_user_id: int
    tier_id: int
    expires_at: datetime | None = None


class VIPMemberUpdate(BaseSchema):
    tier_id: int | None = None
    expires_at: datetime | None = None
    name: str | None = None
    notes: str | None = None


# --- VIP Membership History ---
class VIPMembership(IDSchema):
    guild_id: int
    discord_user_id: int
    tier_id: int | None
    tier_name: str
    started_at: datetime
    ended_at: datetime | None = None
    ended_reason: str | None = None
    warn_sent: bool = False
    expire_sent: bool = False
    tier: VIPTier | None = None


class VIPMembershipMarkSentUpdate(BaseSchema):
    field: Literal["warn_sent", "expire_sent"]


# --- VIP Role Sync (Worker-reconciled outbox for role grants/revokes) ---
class PendingVipRoleSyncCreate(BaseSchema):
    discord_user_id: int
    role_id: int
    action: Literal["grant", "revoke"]
    reason: str


class PendingVipRoleSync(IDSchema):
    guild_id: int
    discord_user_id: int
    role_id: int
    action: Literal["grant", "revoke"]
    reason: str
    created_at: datetime
    attempts: int
    last_error: str | None = None


class VipRoleSyncFailure(BaseSchema):
    error: str


# --- VIP Perks ---
class VIPPerk(IDSchema):
    guild_id: int
    tier_id: int
    text: str
    description: str | None = None
    repeatability: Repeatability = Repeatability.Monthly


class VIPPerkCreate(BaseSchema):
    text: str
    description: str | None = None
    repeatability: Repeatability = Repeatability.Monthly


class VIPPerkUpdate(BaseSchema):
    text: str | None = None
    description: str | None = None
    repeatability: Repeatability | None = None


# --- VIP Perk Redemptions ---
class VIPPerkRedemption(IDSchema):
    guild_id: int
    discord_user_id: int
    perk_id: int
    level: RedemptionLevel


class VIPPerkRedemptionBulkUpdate(BaseSchema):
    perk_ids: list[int]
    level: RedemptionLevel


# --- VIP Display Posts ---
class VIPDisplayPost(IDSchema):
    guild_id: int
    display_type: DisplayType
    channel_id: int
    message_id: int


class VIPDisplayPostCreate(BaseSchema):
    display_type: DisplayType
    channel_id: int
    message_id: int


# --- VIP Message Templates ---
class VIPMessageTemplate(BaseSchema):
    template_type: VIPMessageTemplateType
    title: str | None = None
    description: str | None = None
    is_active: bool = True


class VIPMessageTemplateUpdate(BaseSchema):
    title: str | None = None
    description: str | None = None
    is_active: bool | None = None


class VIPMessageTemplateEffective(BaseSchema):
    title: str
    description: str


class _SafeDict(dict[str, str]):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


def render_vip_message_template(text: str, **variables: str) -> str:
    """Substitute {placeholder} tokens; unrecognized placeholders degrade to literal text instead of raising."""
    return text.format_map(_SafeDict(**variables))

