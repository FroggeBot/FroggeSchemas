from __future__ import annotations

from datetime import datetime

from pydantic import Field

from .base import BaseSchema, IDSchema
from .position import Position

__all__ = [
    "Event",
    "EventCreate",
    "EventPosition",
    "EventPositionCreate",
    "EventPost",
    "EventPostCreate",
    "EventShift",
    "EventShiftCreate",
    "EventShiftUpdate",
    "EventSignup",
    "EventSignupCreate",
    "EventUpdate",
]


# --- Events ---
class Event(IDSchema):
    guild_id: int
    name: str
    description: str | None = None
    start_at: datetime
    end_at: datetime | None = None
    image_url: str | None = None


class EventCreate(BaseSchema):
    name: str
    description: str | None = None
    start_at: datetime
    end_at: datetime | None = None
    image_url: str | None = None


class EventUpdate(BaseSchema):
    name: str | None = None
    description: str | None = None
    start_at: datetime | None = None
    end_at: datetime | None = None
    image_url: str | None = None


# --- Event Signups ---
class EventSignup(IDSchema):
    guild_id: int
    event_shift_id: int
    discord_user_id: int


class EventSignupCreate(BaseSchema):
    discord_user_id: int


# --- Event Shifts ---
class EventShift(IDSchema):
    guild_id: int
    event_position_id: int
    start_at: datetime
    end_at: datetime
    capacity: int = Field(default=1, ge=1)
    signups: list[EventSignup] = []


class EventShiftCreate(BaseSchema):
    start_at: datetime
    end_at: datetime
    capacity: int = Field(default=1, ge=1)


class EventShiftUpdate(BaseSchema):
    start_at: datetime | None = None
    end_at: datetime | None = None
    capacity: int | None = Field(default=None, ge=1)


# --- Event Positions ---
class EventPosition(IDSchema):
    guild_id: int
    event_id: int
    position_id: int
    position: Position
    shifts: list[EventShift] = []


class EventPositionCreate(BaseSchema):
    position_id: int


# --- Event Posts ---
class EventPost(IDSchema):
    guild_id: int
    event_id: int
    channel_id: int
    message_id: int


class EventPostCreate(BaseSchema):
    event_id: int
    channel_id: int
    message_id: int
