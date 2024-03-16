from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["get_friendship_requests_request", "get_friendship_requests_response_without_requests"])
async def test(f):
    result = await f.client.delete("/accounts/1/friends/outgoing/2", headers={"Authorization": "Bearer token"})

    assert result.status_code == 404
    assert result.json() == {
        "resource": "Friendship request",
        "description": "Requested resource not found.",
        "details": "Requested resource doesn't exist or has been deleted.",
    }
