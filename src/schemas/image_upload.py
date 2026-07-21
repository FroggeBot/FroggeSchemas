from __future__ import annotations

from .base import BaseSchema

__all__ = [
    "ImageUploadResult",
]


class ImageUploadResult(BaseSchema):
    url: str
