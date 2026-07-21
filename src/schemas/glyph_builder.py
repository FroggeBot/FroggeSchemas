from __future__ import annotations

from typing import Literal

from .base import BaseSchema, IDSchema

__all__ = [
    "GlyphMessage",
    "GlyphMessageCreate",
    "GlyphMessageUpdate",
    "GlyphToken",
]


class GlyphToken(BaseSchema):
    """One unit of a composed message - `type="text"` is literal free text, `type="symbol"`
    references a bundled symbol by its stable string key (e.g. "BoxedLetterA", matching the
    Bot's own `bot/cogs/glyph_builder/symbols.py` data - Schemas has no I/O and doesn't hold the
    symbol catalog itself)."""

    type: Literal["text", "symbol"]
    value: str


class GlyphMessage(IDSchema):
    guild_id: int
    name: str
    tokens: list[GlyphToken] = []


class GlyphMessageCreate(BaseSchema):
    name: str


class GlyphMessageUpdate(BaseSchema):
    name: str | None = None
    tokens: list[GlyphToken] | None = None
