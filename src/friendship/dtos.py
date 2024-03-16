from __future__ import annotations

from api.account.fields import AccountLoginField
from api.profile.fields import ProfileDescriptionField, ProfileNameField
from api.shared.fields import IdField, UuidField
from pydantic import Field, RootModel

from src.shared.schemas import Schema


class GetOutgoingRequestsResponse(RootModel):  # type: ignore[type-arg]
    root: list[_Friend]
    class _Friend(Schema):
        account: _Account
        class _Account(Schema):
            id: IdField = Field(..., example=42)
            login: AccountLoginField = Field(..., example="john_doe")
        avatar_id: UuidField | None = Field(..., example="b9dd3a32-aee8-4a6b-a519-def9ca30c9ec")
        description: ProfileDescriptionField | None = Field(..., example="Who da heck is John Doe?")
        name: ProfileNameField = Field(..., example="John Doe")
