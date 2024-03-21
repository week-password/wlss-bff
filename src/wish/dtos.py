from __future__ import annotations

from api.shared.fields import IdField, UuidField
from api.wish.fields import WishDescriptionField, WishTitleField
from pydantic import Field, RootModel

from src.shared.schemas import Schema
from src.wish.enums import BookingStatus


class CreateWishRequest(Schema):
    avatar_id: UuidField | None = Field(..., example="b9dd3a32-aee8-4a6b-a519-def9ca30c9ec")
    description: WishDescriptionField = Field(..., example="I'm gonna take my horse to the old town road.")
    title: WishTitleField = Field(..., example="Horse")


class CreateWishResponse(Schema):
    id: IdField = Field(..., example=42)
    avatar_id: UuidField | None = Field(..., example="b9dd3a32-aee8-4a6b-a519-def9ca30c9ec")
    description: WishDescriptionField = Field(..., example="I'm gonna take my horse to the old town road.")
    title: WishTitleField = Field(..., example="Horse")


class UpdateWishRequest(Schema):
    avatar_id: UuidField | None = Field(..., example="b9dd3a32-aee8-4a6b-a519-def9ca30c9ec")
    description: WishDescriptionField = Field(..., example="I'm gonna take my NEW horse to the old town road.")
    title: WishTitleField = Field(..., example="NEW Horse")


class UpdateWishResponse(Schema):
    id: IdField = Field(..., example=18)
    avatar_id: UuidField | None = Field(..., example="b9dd3a32-aee8-4a6b-a519-def9ca30c9ec")
    description: WishDescriptionField = Field(..., example="I'm gonna take my NEW horse to the old town road.")
    title: WishTitleField = Field(..., example="NEW Horse")


class GetAccountWishesResponse(RootModel):  # type: ignore[type-arg]
    root: list[_Wish]
    class _Wish(Schema):
        id: IdField = Field(..., example=42)
        avatar_id: UuidField | None = Field(..., example="b9dd3a32-aee8-4a6b-a519-def9ca30c9ec")
        description: WishDescriptionField = Field(..., example="I'm gonna take my horse to the old town road.")
        title: WishTitleField = Field(..., example="Horse")
        booking_id: IdField | None = Field(..., example=1)
        booking_status: BookingStatus | None = Field(..., example="bookedByCurrentAccount")


class CreateWishBookingRequest(Schema):
    account_id: IdField = Field(..., example=42)
    wish_id: IdField = Field(..., example=17)
