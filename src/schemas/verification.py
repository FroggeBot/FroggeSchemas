from __future__ import annotations

from datetime import datetime
from typing import Literal

from .base import BaseSchema, IDSchema

__all__ = [
    "VerificationRecord",
    "VerificationRecordCreate",
    "VerificationRoleRelation",
    "VerificationRoleRelationCreate",
    "VerificationRoleRelationUpdate",
]

ProofMethod = Literal["lodestone_code", "unverified"]


class VerificationRecord(IDSchema):
    guild_id: int
    discord_user_id: int
    character_name: str
    lodestone_id: int
    world: str
    verified_at: datetime
    proof_method: ProofMethod


class VerificationRecordCreate(BaseSchema):
    discord_user_id: int
    character_name: str
    lodestone_id: int
    world: str
    proof_method: ProofMethod


class VerificationRoleRelation(IDSchema):
    guild_id: int
    pending_role_id: int
    final_role_id: int
    message: str | None = None


class VerificationRoleRelationCreate(BaseSchema):
    pending_role_id: int
    final_role_id: int
    message: str | None = None


class VerificationRoleRelationUpdate(BaseSchema):
    pending_role_id: int | None = None
    final_role_id: int | None = None
    message: str | None = None
