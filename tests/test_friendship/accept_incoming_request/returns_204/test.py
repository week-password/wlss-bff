from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(
    ["get_friendship_requests_request", "get_friendship_requests_response"],
    ["accept_friendship_request_request", "accept_friendship_request_response"],
)
async def test(f):
    result = await f.client.post("/accounts/1/friends/accepted/3", headers={"Authorization": "Bearer token"})

    assert result.status_code == 204
    assert result.content == b""
