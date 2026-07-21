from __future__ import annotations

from datetime import datetime

from pydantic import Field

from .base import BaseSchema, IDSchema

__all__ = [
    "TimeClockEntry",
    "TimeClockEntryCreate",
    "TimeClockEntryUpdate",
]


class TimeClockEntry(IDSchema):
    guild_id: int
    staff_member_id: int
    clocked_in_at: datetime
    clocked_out_at: datetime | None = None
    note: str | None = None
    # Both computed server-side (never stored) - avoids v6's TimeClock module's exact bug class,
    # a stored `duration` that only worked once `_out` was set, with no reassignment discipline.
    duration_seconds: int | None = None
    is_open: bool = True


class TimeClockEntryCreate(BaseSchema):
    """Admin manual-entry creation - self-service clock-in goes through the dedicated
    clock-in action endpoint instead, never this schema."""

    staff_member_id: int
    clocked_in_at: datetime
    clocked_out_at: datetime | None = None
    note: str | None = Field(default=None, max_length=500)


class TimeClockEntryUpdate(BaseSchema):
    clocked_in_at: datetime | None = None
    clocked_out_at: datetime | None = None
    note: str | None = Field(default=None, max_length=500)
