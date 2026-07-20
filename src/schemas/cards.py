from __future__ import annotations

from datetime import date, datetime

from pydantic import Field

from .base import BaseSchema, IDSchema
from .enums import ApprovalStatus, CardArrangement, CardRarity

__all__ = [
    "Card",
    "CardBoosterClaimResult",
    "CardBoosterOpenResult",
    "CardBreakdownRarity",
    "CardBreakdownRarityUpdate",
    "CardCollection",
    "CardCraftRequest",
    "CardCraftResult",
    "CardCraftingRecipe",
    "CardCraftingRecipeUpdate",
    "CardCreate",
    "CardDailyRewardTier",
    "CardDailyRewardTierUpdate",
    "CardDismantleResult",
    "CardEconomyConfig",
    "CardEconomyConfigUpdate",
    "CardOwnership",
    "CardRarityStatBand",
    "CardRarityStatBandUpdate",
    "CardSeries",
    "CardSeriesApproveRequest",
    "CardSeriesCreate",
    "CardSeriesRejectRequest",
    "CardSeriesUpdate",
    "CardUpdate",
]


# --- Guild-less / global: platform-admin economy config -------------------------------------


class CardEconomyConfig(IDSchema):
    shard_booster_cost: int = 100
    daily_reward_fallback_min: int = 1
    daily_reward_fallback_max: int = 2


class CardEconomyConfigUpdate(BaseSchema):
    shard_booster_cost: int | None = Field(default=None, ge=1)
    daily_reward_fallback_min: int | None = Field(default=None, ge=0)
    daily_reward_fallback_max: int | None = Field(default=None, ge=0)


class CardCraftingRecipe(IDSchema):
    rarity: CardRarity
    shard_cost: int


class CardCraftingRecipeUpdate(BaseSchema):
    shard_cost: int | None = Field(default=None, ge=0)


class CardBreakdownRarity(IDSchema):
    rarity: CardRarity
    shard_yield: int


class CardBreakdownRarityUpdate(BaseSchema):
    shard_yield: int | None = Field(default=None, ge=0)


class CardDailyRewardTier(IDSchema):
    streak: int
    boosters: int = 0
    shards: int = 0


class CardDailyRewardTierUpdate(BaseSchema):
    boosters: int | None = Field(default=None, ge=0)
    shards: int | None = Field(default=None, ge=0)


class CardRarityStatBand(IDSchema):
    rarity: CardRarity
    total_budget: int
    min_per_stat: int
    max_per_stat: int


class CardRarityStatBandUpdate(BaseSchema):
    total_budget: int | None = Field(default=None, ge=1)
    min_per_stat: int | None = Field(default=None, ge=1)
    max_per_stat: int | None = Field(default=None, ge=1)


# --- Carry guild_id for provenance, reuse ApprovalStatus -------------------------------------


class CardSeries(IDSchema):
    guild_id: int
    name: str
    description: str | None = None
    icon_url: str | None = None
    approval_status: ApprovalStatus = ApprovalStatus.Draft
    submitted_at: datetime | None = None
    reviewed_at: datetime | None = None
    reviewed_by: int | None = None
    rejection_reason: str | None = None
    arrangement: CardArrangement | None = None
    custom_frame_url: str | None = None


class CardSeriesCreate(BaseSchema):
    name: str


class CardSeriesUpdate(BaseSchema):
    name: str | None = None
    description: str | None = None
    icon_url: str | None = None
    arrangement: CardArrangement | None = None


class CardSeriesApproveRequest(BaseSchema):
    reviewed_by: int


class CardSeriesRejectRequest(BaseSchema):
    reviewed_by: int
    reason: str


class Card(IDSchema):
    guild_id: int
    series_id: int
    name: str
    flavor_text: str | None = None
    image_url: str | None = None
    archetype: str | None = None
    rarity: CardRarity = CardRarity.Common
    charm: int = 1
    wit: int = 1
    presence: int = 1
    flaw: int = 1
    is_active: bool = True
    is_nsfw: bool = False
    pending_image_url: str | None = None


class CardCreate(BaseSchema):
    name: str
    rarity: CardRarity = CardRarity.Common
    charm: int = Field(default=1, ge=1)
    wit: int = Field(default=1, ge=1)
    presence: int = Field(default=1, ge=1)
    flaw: int = Field(default=1, ge=1)
    flavor_text: str | None = None
    image_url: str | None = None
    archetype: str | None = None
    is_nsfw: bool = False


class CardUpdate(BaseSchema):
    name: str | None = None
    flavor_text: str | None = None
    image_url: str | None = None
    archetype: str | None = None
    rarity: CardRarity | None = None
    charm: int | None = Field(default=None, ge=1)
    wit: int | None = Field(default=None, ge=1)
    presence: int | None = Field(default=None, ge=1)
    flaw: int | None = Field(default=None, ge=1)
    is_active: bool | None = None
    is_nsfw: bool | None = None


# --- Keyed by Discord user_id only, no guild_id ----------------------------------------------


class CardCollection(BaseSchema):
    discord_user_id: int
    boosters: int = 0
    shards: int = 0
    streak: int = 0
    last_claimed_date: date | None = None


class CardOwnership(IDSchema):
    discord_user_id: int
    card_id: int
    count: int = 1


class CardBoosterClaimResult(BaseSchema):
    collection: CardCollection
    boosters_granted: int
    shards_granted: int
    streak: int


class CardBoosterOpenResult(BaseSchema):
    granted: list[CardOwnership]


class CardDismantleResult(BaseSchema):
    shards_granted: int
    remaining_count: int


class CardCraftRequest(BaseSchema):
    rarity: CardRarity


class CardCraftResult(BaseSchema):
    card: Card
    ownership: CardOwnership
    shards_spent: int
