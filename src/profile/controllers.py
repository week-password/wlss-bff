from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import jwt
from api.client import Api
from api.friendship.enums import FriendshipRequestStatus
from api.profile import dtos as api_dtos
from wlss.shared.types import Id

from src.config import CONFIG
from src.friendship.enums import FriendshipStatus
from src.profile.dtos import GetProfileResponse, SearchProfilesResponse, UpdateProfileResponse


if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Self

    from src.auth.dependencies import Authorization
    from src.profile.dtos import UpdateProfileRequest


class AccountFriendshipsData:
    def __init__(
        self: Self,
        subject_account_id: Id,
        friend_ids: Iterable[Id],
        incoming_request_sender_ids: Iterable[Id],
        outgoing_request_receiver_ids: Iterable[Id],
    ) -> None:
        self._subject_account_id = subject_account_id
        self._friend_ids = friend_ids
        self._incoming_request_sender_ids = incoming_request_sender_ids
        self._outgoing_request_receiver_ids = outgoing_request_receiver_ids

    @classmethod
    async def fetch_account_data(
        cls: type[AccountFriendshipsData],
        account_id: Id,
        token: str,
    ) -> AccountFriendshipsData:
        async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
            requests_response, friendships_response = await asyncio.gather(
                api.friendship.get_friendship_requests(account_id, token),
                api.friendship.get_account_friendships(account_id, token),
            )

        friend_ids = {
            friendship.friend_id
            for friendship in friendships_response.friendships
            if friendship.account_id == account_id
        }
        incoming_request_sender_ids = {
            request.sender_id
            for request in requests_response.requests
            if (
                request.status is FriendshipRequestStatus.PENDING
                and request.receiver_id == account_id
            )
        }
        outgoing_request_receiver_ids = {
            request.receiver_id
            for request in requests_response.requests
            if (
                request.status is FriendshipRequestStatus.PENDING
                and request.sender_id == account_id
            )
        }
        return cls(account_id, friend_ids, incoming_request_sender_ids, outgoing_request_receiver_ids)

    def get_friendship_status_for(self: Self, object_account_id: Id) -> FriendshipStatus | None:
        if self._subject_account_id == object_account_id:
            return None
        if object_account_id in self._friend_ids:
            return FriendshipStatus.ACCEPTED_REQUEST
        if object_account_id in self._outgoing_request_receiver_ids:
            return FriendshipStatus.OUTGOING_REQUEST
        if object_account_id in self._incoming_request_sender_ids:
            return FriendshipStatus.INCOMING_REQUEST
        return FriendshipStatus.NOT_REQUESTED


async def get_profile(account_id: Id, authorization: Authorization) -> GetProfileResponse:
    token_payload = jwt.decode(authorization.credentials, options={"verify_signature": False})
    current_account_id = Id(token_payload["account_id"])

    if account_id == current_account_id:
        async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
            account, profile = await asyncio.gather(
                api.account.get_account(account_id, authorization.credentials),
                api.profile.get_profile(account_id, authorization.credentials),
            )
        return GetProfileResponse.model_validate({
                "account": account,
                "avatar_id": profile.avatar_id,
                "description": profile.description,
                "name": profile.name,
                "friendship_status": None,
            },
            from_attributes=True,
        )

    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        account, profile, friendships_data = await asyncio.gather(
            api.account.get_account(account_id, authorization.credentials),
            api.profile.get_profile(account_id, authorization.credentials),
            AccountFriendshipsData.fetch_account_data(current_account_id, authorization.credentials),
        )

    return GetProfileResponse.model_validate({
            "account": account,
            "avatar_id": profile.avatar_id,
            "description": profile.description,
            "name": profile.name,
            "friendship_status": friendships_data.get_friendship_status_for(account_id),
        },
        from_attributes=True,
    )


async def search_profiles(authorization: Authorization) -> SearchProfilesResponse:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        profiles_response = await api.profile.search_profiles(authorization.credentials)

        account_ids = [profile.account_id for profile in profiles_response.profiles]

        token_payload = jwt.decode(authorization.credentials, options={"verify_signature": False})
        current_account_id = Id(token_payload["account_id"])

        accounts_response, friendships_data = await asyncio.gather(
            api.account.get_accounts(authorization.credentials, account_ids),
            AccountFriendshipsData.fetch_account_data(current_account_id, authorization.credentials),
        )

        accounts_index = {account.id: account for account in accounts_response.accounts}
        profiles_index = {profile.account_id: profile for profile in profiles_response.profiles}

        response_body = []
        for account_id in account_ids:
            account = accounts_index.get(account_id)
            profile = profiles_index.get(account_id)
            if not (account and profile):
                continue

            response_body.append(
                {
                    "account": account,
                    "avatar_id": profile.avatar_id,
                    "description": profile.description,
                    "name": profile.name,
                    "friendship_status": friendships_data.get_friendship_status_for(account_id),
                },
            )
    return SearchProfilesResponse.model_validate(response_body, from_attributes=True)


async def update_profile(
    account_id: Id,
    request_data: UpdateProfileRequest,
    authorization: Authorization,
) -> UpdateProfileResponse:
    api_request_data = api_dtos.UpdateProfileRequest(
        avatar_id=request_data.avatar_id,
        description=request_data.description,
        name=request_data.name,
    )

    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        profile = await api.profile.update_profile(account_id, api_request_data, authorization.credentials)

    return UpdateProfileResponse(
        avatar_id=profile.avatar_id,
        description=profile.description,
        name=profile.name,
    )
