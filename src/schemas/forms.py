from __future__ import annotations

from datetime import datetime

from pydantic import Field

from .base import BaseSchema, IDSchema
from .enums import FormQuestionType

__all__ = [
    "Form",
    "FormCreate",
    "FormQuestion",
    "FormQuestionCreate",
    "FormQuestionUpdate",
    "FormResponse",
    "FormResponseAnswer",
    "FormResponseAnswerUpsert",
    "FormUpdate",
]


# --- Form Questions ---
class FormQuestion(IDSchema):
    guild_id: int
    form_id: int
    prompt: str
    question_type: FormQuestionType = FormQuestionType.ShortText
    required: bool = True
    sort_order: int = 0
    options: list[str] = []


class FormQuestionCreate(BaseSchema):
    prompt: str = Field(max_length=80)
    question_type: FormQuestionType = FormQuestionType.ShortText
    required: bool = True


class FormQuestionUpdate(BaseSchema):
    prompt: str | None = Field(default=None, max_length=80)
    question_type: FormQuestionType | None = None
    required: bool | None = None
    options: list[str] | None = None


# --- Forms ---
class Form(IDSchema):
    guild_id: int
    name: str
    description: str | None = None
    pre_prompt: str | None = None
    post_prompt: str | None = None
    post_channel_id: int | None = None
    message_id: int | None = None
    thumbnail_url: str | None = None
    color: int | None = None
    button_label: str = "Fill Out"
    button_emoji: str | None = None
    allow_multiple_responses: bool = False


class FormCreate(BaseSchema):
    name: str = Field(max_length=100)


class FormUpdate(BaseSchema):
    name: str | None = Field(default=None, max_length=100)
    description: str | None = None
    pre_prompt: str | None = None
    post_prompt: str | None = None
    post_channel_id: int | None = None
    message_id: int | None = None
    thumbnail_url: str | None = None
    color: int | None = None
    button_label: str | None = None
    button_emoji: str | None = None
    allow_multiple_responses: bool | None = None


# --- Form Responses ---
class FormResponseAnswer(BaseSchema):
    """A self-contained snapshot of one question's prompt/type alongside the member's answer to
    it - stored as one entry in FormResponse.answers, not a live FK to the (possibly since-edited
    or deleted) FormQuestion, so a submitted response stays fully readable regardless of later
    changes to the form. `question_id` is kept purely so the in-progress fill-out wizard can look
    up whether a draft answer already exists for a given question without depending on array
    position (safe even if a question is deleted mid-fill - that answer just becomes orphaned,
    harmless data)."""

    question_id: int
    question: str
    question_type: FormQuestionType
    answer: str | list[str]


class FormResponseAnswerUpsert(BaseSchema):
    """The Bot only ever sends `question_id` + `answer` - the question's current prompt/type are
    looked up server-side and snapshotted into the stored FormResponseAnswer, never trusted from
    the client."""

    question_id: int
    answer: str | list[str]


class FormResponse(IDSchema):
    guild_id: int
    form_id: int
    discord_user_id: int
    submitted_at: datetime | None = None
    answers: list[FormResponseAnswer] = []
