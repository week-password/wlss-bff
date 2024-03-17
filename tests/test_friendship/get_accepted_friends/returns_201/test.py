from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(
    ["get_account_friendships_request", "get_account_friendships_response"],
    ["get_accounts_request", "get_accounts_response"],
    ["get_profiles_request", "get_profiles_response"],
)
async def test(f):
    result = await f.client.get("/accounts/1/friends/accepted", headers={"Authorization": "Bearer token"})

    assert result.status_code == 200
    assert result.json() == [
        {
            "account": {
                "id": 2,
                "login": "john_smith",
            },
            "avatarId": None,
            "description": "One more 'John' in out testing?",
            "name": "John Smith",
        },
    ]
