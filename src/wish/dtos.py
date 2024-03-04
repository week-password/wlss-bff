from __future__ import annotations

from pydantic import Field

from src.shared.fields import IdField
from src.shared.schemas import Schema


class CreateWishBookingRequest(Schema):
    account_id: IdField = Field(..., example=42)
    wish_id: IdField = Field(..., example=17)
