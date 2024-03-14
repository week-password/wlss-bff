from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"access_token": "access_token", "client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(
    ["get_account_request", "get_account_response"],
    ["get_profile_request", "get_profile_response"],
    ["get_account_friendships_request", "get_account_friendships_response"],
    ["get_friendship_requests_request", "get_friendship_requests_response_with_one_outgoing_request"],
)
async def test(f):
    result = await f.client.get("/accounts/1/profile", headers={"Authorization": f"Bearer {f.access_token}"})

    assert result.status_code == 200
    assert result.json() == {
        "account": {
            "id": 1,
            "login": "john_doe",
        },
        "avatarId": "3d859b6b-b1ce-4a30-b6bc-c62fc8992630",
        "description": "Who da heck is John Doe?",
        "name": "John Doe",
        "friendshipStatus": "outgoingRequest",
    }
