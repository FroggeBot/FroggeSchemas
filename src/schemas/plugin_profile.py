from __future__ import annotations

from .base import BaseSchema


class PluginProfileSummary(BaseSchema):
    id: int
    guild_id: int
    guild_name: str
    character_name: str
    is_primary: bool
    approval_status: str
    thumbnail_url: str | None = None

class PluginProfileImage(BaseSchema):
    image_url: str
    caption: str | None = None

class PluginProfileDetail(BaseSchema):
    id: int
    guild_id: int
    guild_name: str
    character_name: str
    is_primary: bool
    approval_status: str
    rejection_reason: str | None = None
    color: int | None = None
    jobs: str | None = None
    rates: str | None = None
    thumbnail_url: str | None = None
    main_image_url: str | None = None
    world: str | None = None
    data_center: str | None = None
    gender: str | None = None
    pronouns: str | None = None
    race: str | None = None
    clan: str | None = None
    orientation: str | None = None
    height: str | None = None
    age: str | None = None
    mare_code: str | None = None
    likes: str | None = None
    dislikes: str | None = None
    personality: str | None = None
    about_me: str | None = None
    additional_images: list[PluginProfileImage] = []
