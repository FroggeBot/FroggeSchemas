from __future__ import annotations

from datetime import datetime
from zoneinfo import available_timezones

from pydantic import Field, field_validator

from .base import BaseSchema

_VALID_TIMEZONES = available_timezones()


def _check_timezone(value: str) -> str:
    if value not in _VALID_TIMEZONES:
        raise ValueError(f"Invalid IANA timezone: {value!r}")
    return value


class GuildConfiguration(BaseSchema):
    guild_id: int
    timezone: str = "UTC"
    log_channel_id: int | None = None
    accent_color: int = 0x2F6B4F
    vip_warning_threshold_days: int | None = Field(default=3, ge=1)
    event_lockout_minutes: int | None = Field(default=None, ge=1)
    profile_approval_required: bool = True
    verified_role_id: int | None = None
    require_lodestone_proof: bool = True
    require_captcha: bool = True
    change_name: bool = True
    staff_role_id: int | None = None
    require_staffing_qualification: bool = False
    card_game_enabled: bool = False

    @field_validator("timezone")
    @classmethod
    def _validate_timezone(cls, value: str) -> str:
        return _check_timezone(value)

class GuildConfigurationUpdate(BaseSchema):
    timezone: str | None = None
    log_channel_id: int | None = None
    accent_color: int | None = None
    vip_warning_threshold_days: int | None = Field(default=None, ge=1)
    event_lockout_minutes: int | None = Field(default=None, ge=1)
    profile_approval_required: bool | None = None
    verified_role_id: int | None = None
    require_lodestone_proof: bool | None = None
    require_captcha: bool | None = None
    change_name: bool | None = None
    staff_role_id: int | None = None
    require_staffing_qualification: bool | None = None
    card_game_enabled: bool | None = None

    @field_validator("timezone")
    @classmethod
    def _validate_timezone(cls, value: str | None) -> str | None:
        return _check_timezone(value) if value is not None else None

class GuildSubscription(BaseSchema):
    guild_id: int
    tier: str = "free"
    status: str = "active"
    renewed_at: datetime | None = None
    expires_at: datetime | None = None
    discord_subscription_id: str | None = None
    granted_by: int | None = None
    note: str | None = None

class GuildSubscriptionGrantRequest(BaseSchema):
    tier: str
    status: str = "active"
    expires_at: datetime | None = None
    granted_by: int
    note: str | None = None

class Guild(BaseSchema):
    guild_id: int
    name: str
    created_at: datetime
    configuration: GuildConfiguration
    subscription: GuildSubscription

class GuildWelcomePost(BaseSchema):
    guild_id: int
    channel_id: int
    message_id: int
    posted_at: datetime

class GuildWelcomePostUpsert(BaseSchema):
    channel_id: int
    message_id: int

class GuildWarningThreshold(BaseSchema):
    guild_id: int
    vip_warning_threshold_days: int | None

class GuildLockoutThreshold(BaseSchema):
    guild_id: int
    event_lockout_minutes: int | None

class GuildLogChannelId(BaseSchema):
    guild_id: int
    log_channel_id: int | None
