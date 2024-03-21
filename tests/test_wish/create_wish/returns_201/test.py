from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["create_wish_request", "create_wish_response"])
async def test(f):
    result = await f.client.post(
        "/accounts/1/wishes",
        json={
            "avatar_id": None,
            "description": "I'm gonna take my horse to the old town road.",
            "title": "Horse",
        },
        headers={"Authorization": "Bearer token"},
    )

    assert result.status_code == 201
    assert result.json() == {
        "id": 1,
        "avatarId": None,
        "description": "I'm gonna take my horse to the old town road.",
        "title": "Horse",
    }
