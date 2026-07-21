from __future__ import annotations

from pydantic import Field, field_validator

from .base import BaseSchema


class ContactMessage(BaseSchema):
    """Submitted from the Frogge Tech Solutions site's contact form. `honeypot` is a hidden field
    real users never fill in - non-empty means a bot, and the router silently drops those rather
    than erroring (an error just tells a bot to adapt)."""

    name: str = Field(min_length=1, max_length=200)
    email: str = Field(min_length=3, max_length=320)
    message: str = Field(min_length=1, max_length=5000)
    honeypot: str = ""

    @field_validator("email")
    @classmethod
    def _check_email_shape(cls, value: str) -> str:
        local, _, domain = value.partition("@")
        if not local or "." not in domain or domain.startswith(".") or domain.endswith("."):
            raise ValueError("Not a valid email address.")
        return value
