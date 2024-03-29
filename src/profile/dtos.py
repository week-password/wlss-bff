from __future__ import annotations

from api.account.fields import AccountLoginField
from api.profile.fields import ProfileDescriptionField, ProfileNameField
from api.shared.fields import IdField, UuidField
from pydantic import Field, RootModel

from src.friendship.enums import FriendshipStatus
from src.shared.schemas import Schema


class GetProfileResponse(Schema):
    account: _Account
    class _Account(Schema):
        id: IdField = Field(..., example=42)
        login: AccountLoginField = Field(..., example="john_doe")

    avatar_id: UuidField | None = Field(..., example="f6bdfda7-0a5b-4ed5-800f-ac352656abec")
    description: ProfileDescriptionField | None = Field(..., example="Who da heck is John Doe?")
    name: ProfileNameField = Field(..., example="John Doe")
    friendship_status: FriendshipStatus | None = Field(..., example="incomingRequest")


class SearchProfilesResponse(RootModel):  # type: ignore[type-arg]
    root: list[_Profile]
    class _Profile(Schema):
        account: _Account
        class _Account(Schema):
            id: IdField = Field(..., example=42)
            login: AccountLoginField = Field(..., example="john_doe")

        avatar_id: UuidField | None = Field(..., example="f6bdfda7-0a5b-4ed5-800f-ac352656abec")
        description: ProfileDescriptionField | None = Field(..., example="Who da heck is John Doe?")
        name: ProfileNameField = Field(..., example="John Doe")
        friendship_status: FriendshipStatus | None = Field(..., example="incomingRequest")


class UpdateProfileRequest(Schema):
    avatar_id: UuidField | None = Field(..., example="f6bdfda7-0a5b-4ed5-800f-ac352656abec")
    description: ProfileDescriptionField | None = Field(..., example="Who da heck is John Doe?")
    name: ProfileNameField = Field(..., example="John Doe")


class UpdateProfileResponse(Schema):
    avatar_id: UuidField | None = Field(..., example="f6bdfda7-0a5b-4ed5-800f-ac352656abec")
    description: ProfileDescriptionField | None = Field(..., example="Who da heck is John Doe?")
    name: ProfileNameField = Field(..., example="John Doe")
