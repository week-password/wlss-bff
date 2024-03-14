from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({
    "access_token": "access_token_of_profile_owner",
    "client": "client",
    "api": "api_configured_with_api_stubs",
})
@pytest.mark.api_stubs(
    ["get_account_request_from_account_owner", "get_account_response_for_account_owner"],
    ["get_profile_request_from_profile_owner", "get_profile_response_for_profile_owner"],
)
async def test(f):
    result = await f.client.get(
        "/accounts/1/profile", headers={"Authorization": f"Bearer {f.access_token}"})

    assert result.status_code == 200
    assert result.json() == {
        "account": {
            "id": 1,
            "login": "john_doe",
        },
        "avatarId": "3d859b6b-b1ce-4a30-b6bc-c62fc8992630",
        "description": "Who da heck is John Doe?",
        "name": "John Doe",
        "friendshipStatus": None,
    }
