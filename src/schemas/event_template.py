from __future__ import annotations

from datetime import datetime

from pydantic import Field

from .base import BaseSchema, IDSchema
from .event import Event

__all__ = [
    "EventTemplate",
    "EventTemplateApplyRequest",
    "EventTemplateApplyResult",
    "EventTemplateCreate",
    "EventTemplateData",
    "EventTemplatePosition",
    "EventTemplatePositionCreate",
    "EventTemplateShift",
    "EventTemplateShiftCreate",
    "EventTemplateShiftUpdate",
    "EventTemplateUpdate",
]


# --- Event Template Shifts (blob entries) ---
class EventTemplateShift(BaseSchema):
    key: int
    start_offset_minutes: int
    end_offset_minutes: int
    capacity: int = Field(default=1, ge=1)


class EventTemplateShiftCreate(BaseSchema):
    start_offset_minutes: int
    end_offset_minutes: int
    capacity: int = Field(default=1, ge=1)


class EventTemplateShiftUpdate(BaseSchema):
    start_offset_minutes: int | None = None
    end_offset_minutes: int | None = None
    capacity: int | None = Field(default=None, ge=1)


# --- Event Template Positions (blob entries) ---
class EventTemplatePosition(BaseSchema):
    key: int
    position_id: int
    position_name: str
    position_color: int | None = None
    shifts: list[EventTemplateShift] = []


class EventTemplatePositionCreate(BaseSchema):
    position_id: int


# --- Event Templates ---
class EventTemplateData(BaseSchema):
    description: str | None = None
    address: str | None = None
    image_url: str | None = None
    duration_minutes: int | None = None
    positions: list[EventTemplatePosition] = []


class EventTemplate(IDSchema):
    guild_id: int
    name: str
    data: EventTemplateData


class EventTemplateCreate(BaseSchema):
    name: str
    data: EventTemplateData = EventTemplateData()


class EventTemplateUpdate(BaseSchema):
    name: str | None = None
    description: str | None = None
    address: str | None = None
    image_url: str | None = None


class EventTemplateApplyRequest(BaseSchema):
    start_at: datetime


class EventTemplateApplyResult(BaseSchema):
    event: Event
    skipped_position_names: list[str] = []
