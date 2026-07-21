from __future__ import annotations

from datetime import datetime

from pydantic import Field

from .base import BaseSchema, IDSchema

__all__ = [
    "CustomEmbed",
    "CustomEmbedCreate",
    "CustomEmbedField",
    "CustomEmbedFieldCreate",
    "CustomEmbedFieldUpdate",
    "CustomEmbedPost",
    "CustomEmbedPostCreate",
    "CustomEmbedUpdate",
]


# --- Custom Embed Fields ---
class CustomEmbedField(IDSchema):
    guild_id: int
    custom_embed_id: int
    name: str
    value: str
    inline: bool = True
    sort_order: int = 0


class CustomEmbedFieldCreate(BaseSchema):
    name: str = Field(max_length=256)
    value: str = Field(max_length=1024)
    inline: bool = True


class CustomEmbedFieldUpdate(BaseSchema):
    name: str | None = Field(default=None, max_length=256)
    value: str | None = Field(default=None, max_length=1024)
    inline: bool | None = None


# --- Custom Embed Posts ---
class CustomEmbedPost(IDSchema):
    guild_id: int
    custom_embed_id: int
    channel_id: int
    message_id: int


class CustomEmbedPostCreate(BaseSchema):
    custom_embed_id: int
    channel_id: int
    message_id: int


# --- Custom Embeds ---
class CustomEmbed(IDSchema):
    guild_id: int
    name: str
    title: str | None = None
    description: str | None = None
    color: int | None = None
    url: str | None = None
    timestamp: datetime | None = None
    header_text: str | None = None
    header_icon_url: str | None = None
    header_url: str | None = None
    footer_text: str | None = None
    footer_icon_url: str | None = None
    thumbnail_url: str | None = None
    main_image_url: str | None = None


class CustomEmbedCreate(BaseSchema):
    """title/description/color are optional here (unlike FormCreate's bare `name`) so the Bot's
    Add flow can create v6-style demo-prefilled content in one call rather than create-then-patch."""

    name: str = Field(max_length=100)
    title: str | None = Field(default=None, max_length=256)
    description: str | None = Field(default=None, max_length=4096)
    color: int | None = None


class CustomEmbedUpdate(BaseSchema):
    name: str | None = Field(default=None, max_length=100)
    title: str | None = Field(default=None, max_length=256)
    description: str | None = Field(default=None, max_length=4096)
    color: int | None = None
    url: str | None = None
    timestamp: datetime | None = None
    header_text: str | None = Field(default=None, max_length=256)
    header_icon_url: str | None = None
    header_url: str | None = None
    footer_text: str | None = Field(default=None, max_length=2048)
    footer_icon_url: str | None = None
    thumbnail_url: str | None = None
    main_image_url: str | None = None
