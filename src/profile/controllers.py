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
from src.profile.dtos import GetProfileResponse, UpdateProfileResponse


if TYPE_CHECKING:
    from src.auth.dependencies import Authorization
    from src.profile.dtos import UpdateProfileRequest



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
        account, profile, friendship_requests_response, friendships_response = await asyncio.gather(
            api.account.get_account(account_id, authorization.credentials),
            api.profile.get_profile(account_id, authorization.credentials),
            api.friendship.get_friendship_requests(current_account_id, authorization.credentials),
            api.friendship.get_account_friendships(current_account_id, authorization.credentials),
        )

    friendship_status = FriendshipStatus.NOT_REQUESTED
    for request in friendship_requests_response.requests:
        if (
            request.sender_id == account_id
            and request.receiver_id == current_account_id
            and request.status is FriendshipRequestStatus.PENDING
        ):
            friendship_status = FriendshipStatus.INCOMING_REQUEST
            break

        if (
            request.sender_id == current_account_id
            and request.receiver_id == account_id
            and request.status is FriendshipRequestStatus.PENDING
        ):
            friendship_status = FriendshipStatus.OUTGOING_REQUEST
            break

    for friendship in friendships_response.friendships:
        if friendship.account_id == current_account_id and friendship.friend_id == account_id:
            friendship_status = FriendshipStatus.ACCEPTED_REQUEST
            break

    return GetProfileResponse.model_validate({
            "account": account,
            "avatar_id": profile.avatar_id,
            "description": profile.description,
            "name": profile.name,
            "friendship_status": friendship_status,
        },
        from_attributes=True,
    )


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
