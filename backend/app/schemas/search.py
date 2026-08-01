from enum import Enum

from pydantic import BaseModel, Field


class ItemCondition(str, Enum):
    new = "new"
    used = "used"
    refurbished = "refurbished"
    any = "any"


class SearchPreviewRequest(BaseModel):
    query: str = Field(
        min_length=2,
        max_length=200,
        examples=["Sony camera for travel videos"],
    )
    max_budget: float = Field(
        gt=0,
        le=100_000,
        examples=[700],
    )
    condition: ItemCondition = ItemCondition.any
    required_features: list[str] = Field(
        default_factory=list,
        max_length=20,
    )