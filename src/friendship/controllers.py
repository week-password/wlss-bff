from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

from api.client import Api
from api.friendship.dtos import CreateFriendshipRequestRequest
from api.friendship.enums import FriendshipRequestStatus

from src.config import CONFIG
from src.friendship.dtos import GetAcceptedFriendsResponse, GetIncomingRequestsResponse, GetOutgoingRequestsResponse
from src.friendship.exceptions import FriendshipRequestNotFoundError


if TYPE_CHECKING:
    from fastapi.security import HTTPAuthorizationCredentials
    from wlss.shared.types import Id


async def create_outgoing_request(account_id: Id, friend_id: Id, authorization: HTTPAuthorizationCredentials) -> None:
    api_request_data = CreateFriendshipRequestRequest(sender_id=account_id, receiver_id=friend_id)
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        await api.friendship.create_friendship_request(api_request_data, authorization.credentials)


async def get_outgoing_requests(
    account_id: Id,
    authorization: HTTPAuthorizationCredentials,
) -> GetOutgoingRequestsResponse:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        requests_response = await api.friendship.get_friendship_requests(account_id, authorization.credentials)

        receiver_ids = [
            request.receiver_id
            for request in requests_response.requests
            if (
                request.sender_id == account_id
                and request.status is FriendshipRequestStatus.PENDING
            )
        ]
        accounts_response, profiles_response = await asyncio.gather(
            api.account.get_accounts(authorization.credentials, account_ids=receiver_ids),
            api.profile.get_profiles(account_ids=receiver_ids, token=authorization.credentials),
        )

    accounts_index = {account.id: account for account in accounts_response.accounts}
    profiles_index = {profile.account_id: profile for profile in profiles_response.profiles}

    response_body = []
    for account_id in receiver_ids:
        account = accounts_index.get(account_id)
        profile = profiles_index.get(account_id)
        if not (profile and account):
            continue
        response_body.append(
            {
                "account": account,
                "avatar_id": profile.avatar_id,
                "description": profile.description,
                "name": profile.name,
            },
        )
    return GetOutgoingRequestsResponse.model_validate(response_body, from_attributes=True)


async def cancel_outgoing_request(account_id: Id, friend_id: Id, authorization: HTTPAuthorizationCredentials) -> None:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        requests_response = await api.friendship.get_friendship_requests(account_id, authorization.credentials)

        request_id = None
        for request in requests_response.requests:
            if (
                request.sender_id == account_id
                and request.receiver_id == friend_id
                and request.status is FriendshipRequestStatus.PENDING
            ):
                request_id = request.id
                break
        if request_id is None:
            raise FriendshipRequestNotFoundError()

        await api.friendship.cancel_friendship_request(request_id, authorization.credentials)


async def get_incoming_requests(
    account_id: Id,
    authorization: HTTPAuthorizationCredentials,
) -> GetIncomingRequestsResponse:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        requests_response = await api.friendship.get_friendship_requests(account_id, authorization.credentials)

        sender_ids = [
            request.sender_id
            for request in requests_response.requests
            if (
                request.receiver_id == account_id
                and request.status is FriendshipRequestStatus.PENDING
            )
        ]
        accounts_response, profiles_response = await asyncio.gather(
            api.account.get_accounts(account_ids=sender_ids, token=authorization.credentials),
            api.profile.get_profiles(account_ids=sender_ids, token=authorization.credentials),
        )


    accounts_index = {account.id: account for account in accounts_response.accounts}
    profiles_index = {profile.account_id: profile for profile in profiles_response.profiles}

    response_body = []
    for account_id in sender_ids:
        account = accounts_index.get(account_id)
        profile = profiles_index.get(account_id)
        if not (profile and account):
            continue
        response_body.append(
            {
                "account": account,
                "avatar_id": profile.avatar_id,
                "description": profile.description,
                "name": profile.name,
            },
        )
    return GetIncomingRequestsResponse.model_validate(response_body, from_attributes=True)


async def accept_incoming_request(account_id: Id, friend_id: Id, authorization: HTTPAuthorizationCredentials) -> None:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        requests_response = await api.friendship.get_friendship_requests(account_id, authorization.credentials)

        request_id = None
        for request in requests_response.requests:
            if (
                request.sender_id == friend_id
                and request.receiver_id == account_id
                and request.status is FriendshipRequestStatus.PENDING
            ):
                request_id = request.id
                break
        if request_id is None:
            raise FriendshipRequestNotFoundError()

        await api.friendship.accept_friendship_request(request_id, authorization.credentials)


async def reject_incoming_request(account_id: Id, friend_id: Id, authorization: HTTPAuthorizationCredentials) -> None:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        requests_response = await api.friendship.get_friendship_requests(account_id, authorization.credentials)

        request_id = None
        for request in requests_response.requests:
            if (
                request.sender_id == friend_id
                and request.receiver_id == account_id
                and request.status is FriendshipRequestStatus.PENDING
            ):
                request_id = request.id
                break
        if request_id is None:
            raise FriendshipRequestNotFoundError()

        await api.friendship.reject_friendship_request(request_id, authorization.credentials)


async def get_accepted_friends(
    account_id: Id,
    authorization: HTTPAuthorizationCredentials,
) -> GetAcceptedFriendsResponse:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        response = await api.friendship.get_account_friendships(account_id, authorization.credentials)

    friend_ids = [friendship.friend_id for friendship in response.friendships]

    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        profiles_response, accounts_response = await asyncio.gather(
            api.profile.get_profiles(account_ids=friend_ids, token=authorization.credentials),
            api.account.get_accounts(account_ids=friend_ids, token=authorization.credentials),
        )

    accounts_index = {account.id: account for account in accounts_response.accounts}
    profiles_index = {profile.account_id: profile for profile in profiles_response.profiles}

    response_body = []
    for account_id in friend_ids:
        account = accounts_index.get(account_id)
        profile = profiles_index.get(account_id)
        if not (profile and account):
            continue
        response_body.append(
            {
                "account": accounts_index[account_id],
                "avatar_id": profile.avatar_id,
                "description": profile.description,
                "name": profile.name,
            },
        )

    return GetAcceptedFriendsResponse.model_validate(response_body, from_attributes=True)


async def delete_friend(account_id: Id, friend_id: Id, authorization: HTTPAuthorizationCredentials) -> None:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
         await api.friendship.delete_friendships(account_id, friend_id, authorization.credentials)
