from __future__ import annotations

import re
from datetime import datetime

from pydantic import field_validator

from .base import BaseSchema, IDSchema
from .position import Position

__all__ = [
    "StaffEmploymentPeriod",
    "StaffEmploymentPeriodCreate",
    "StaffEmploymentPeriodUpdate",
    "StaffMember",
    "StaffMemberCreate",
    "StaffMemberUpdate",
    "is_signup_qualified",
]

_BIRTHDAY_PATTERN = re.compile(r"^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")


def _check_birthday(value: str) -> str:
    if not _BIRTHDAY_PATTERN.match(value):
        raise ValueError(f"Invalid birthday {value!r}: expected 'MM-DD' (no year).")
    return value


# --- Staff Members ---
class StaffMember(IDSchema):
    guild_id: int
    discord_user_id: int
    name: str | None = None
    birthday: str | None = None  # "MM-DD", no year — matches v6, a birthday not a DOB
    notes: str | None = None  # admin-only, mirrors VIPMember.notes
    is_terminated: bool  # computed server-side: no employment period currently open
    terminated_at: datetime | None = None  # computed server-side: most recent period's ended_at
    positions: list[Position] = []  # qualifications, nested to avoid N+1 on the detail screen

    @field_validator("birthday")
    @classmethod
    def _validate_birthday(cls, value: str | None) -> str | None:
        return _check_birthday(value) if value is not None else None


class StaffMemberCreate(BaseSchema):
    discord_user_id: int


class StaffMemberUpdate(BaseSchema):
    name: str | None = None
    birthday: str | None = None
    notes: str | None = None

    @field_validator("birthday")
    @classmethod
    def _validate_birthday(cls, value: str | None) -> str | None:
        return _check_birthday(value) if value is not None else None


# --- Staff Employment History ---
class StaffEmploymentPeriod(IDSchema):
    guild_id: int
    staff_member_id: int
    started_at: datetime
    ended_at: datetime | None = None
    # No `ended_reason` in v6's own model — added anyway for consistency with VIPMembership,
    # which already proved the pattern out ("resigned" vs "terminated" vs "seasonal end").
    ended_reason: str | None = None


class StaffEmploymentPeriodCreate(BaseSchema):
    started_at: datetime


class StaffEmploymentPeriodUpdate(BaseSchema):
    started_at: datetime | None = None
    ended_at: datetime | None = None
    ended_reason: str | None = None


# --- Events qualification-gating (Part 2 of the sequencing plan) ---
def is_signup_qualified(position_id: int, qualified_position_ids: set[int] | None) -> bool:
    """Pure eligibility check for Events' opt-in staffing-qualification gate.

    `qualified_position_ids` is the caller's set of qualified Position ids as returned by
    `StaffMemberService.get_qualified_position_ids` — `None` means the caller isn't an active
    (non-terminated) staff member at all, which is always unqualified regardless of position.
    """
    if qualified_position_ids is None:
        return False
    return position_id in qualified_position_ids
