from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["update_wish_request", "update_wish_response"])
async def test(f):
    result = await f.client.put(
        "/accounts/1/wishes/1",
        json={
            "avatar_id": None,
            "description": "I'm gonna take my NEW horse to the old town road.",
            "title": "NEW Horse",
        },
        headers={"Authorization": "Bearer token"},
    )

    assert result.status_code == 200
    assert result.json() == {
        "id": 1,
        "avatarId": None,
        "description": "I'm gonna take my NEW horse to the old town road.",
        "title": "NEW Horse",
    }
