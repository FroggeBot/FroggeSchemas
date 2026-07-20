from __future__ import annotations

from datetime import datetime

from pydantic import Field

from .base import BaseSchema, IDSchema
from .enums import FinanceCurrency, FinanceEntryType, FinancePayoutStatus

__all__ = [
    "FinanceCategoryTotal",
    "FinancePayout",
    "FinancePayoutCreate",
    "FinanceSummary",
    "FinanceTransaction",
    "FinanceTransactionCreate",
    "FinanceTransactionUpdate",
]


# --- Finance Transactions ---
class FinanceTransaction(IDSchema):
    guild_id: int
    currency: FinanceCurrency
    entry_type: FinanceEntryType
    amount: int
    category: str
    memo: str | None = None
    recorded_by: int
    created_at: datetime


class FinanceTransactionCreate(BaseSchema):
    currency: FinanceCurrency
    entry_type: FinanceEntryType
    amount: int = Field(gt=0)
    category: str = Field(max_length=50)
    memo: str | None = Field(default=None, max_length=500)
    recorded_by: int


class FinanceTransactionUpdate(BaseSchema):
    amount: int | None = Field(default=None, gt=0)
    category: str | None = Field(default=None, max_length=50)
    memo: str | None = Field(default=None, max_length=500)


# --- Finance Payouts ---
class FinancePayout(IDSchema):
    guild_id: int
    staff_member_id: int
    currency: FinanceCurrency
    amount: int
    status: FinancePayoutStatus = FinancePayoutStatus.Pending
    note: str | None = None
    created_by: int
    created_at: datetime
    paid_at: datetime | None = None
    paid_by: int | None = None
    transaction_id: int | None = None


class FinancePayoutCreate(BaseSchema):
    staff_member_id: int
    currency: FinanceCurrency
    amount: int = Field(gt=0)
    note: str | None = Field(default=None, max_length=500)
    created_by: int


# --- Reporting ---
class FinanceCategoryTotal(BaseSchema):
    category: str
    total: int


class FinanceSummary(BaseSchema):
    currency: FinanceCurrency
    period_start: datetime
    period_end: datetime
    total_revenue: int
    total_expense: int
    total_payout: int
    net: int
    category_totals: list[FinanceCategoryTotal] = []
    transaction_count: int
