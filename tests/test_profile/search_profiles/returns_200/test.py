from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({
    "access_token": "access_token",
    "client": "client",
    "api": "api_configured_with_api_stubs",
})
@pytest.mark.api_stubs(
    ["search_profiles_request", "search_profiles_response"],
    ["get_accounts_request", "get_accounts_response"],
    ["get_friendship_requests_request", "get_friendship_requests_response"],
    ["get_account_friendships_request", "get_account_friendships_response"],
)
async def test(f):
    result = await f.client.get("/profiles", headers={"Authorization": f"Bearer {f.access_token}"})

    assert result.status_code == 200
    assert result.json() == [
        {
            "account": {
                "id": 1,
                "login": "john_doe",
            },
            "avatarId": None,
            "description": None,
            "name": "John Doe",
            "friendshipStatus": None,
        },
        {
            "account": {
                "id": 2,
                "login": "john_smith",
            },
            "avatarId": None,
            "description": None,
            "name": "John Smith",
            "friendshipStatus": "notRequested",
        },
    ]
