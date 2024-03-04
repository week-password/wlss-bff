from __future__ import annotations

from api.shared.fields import IdField
from pydantic import Field

from src.shared.schemas import Schema


class CreateWishBookingRequest(Schema):
    account_id: IdField = Field(..., example=42)
    wish_id: IdField = Field(..., example=17)
