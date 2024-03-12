from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["update_profile_request", "update_profile_response"])
async def test_update_profile_returns_200_with_correct_response(f):
    result = await f.client.put(
        "/accounts/1/profile",
        json={
            "avatarId": "f6bdfda7-0a5b-4ed5-800f-ac352656abec",
            "description": "NEW John Doe's profile description",
            "name": "John Doe",
        },
        headers={"Authorization": "Bearer token"},
    )

    assert result.status_code == 200
    assert result.json() == {
        "avatarId": "f6bdfda7-0a5b-4ed5-800f-ac352656abec",
        "description": "NEW John Doe's profile description",
        "name": "John Doe",
    }
