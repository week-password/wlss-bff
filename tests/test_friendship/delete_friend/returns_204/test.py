from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["delete_friendships_request", "delete_friendships_response"])
async def test(f):
    result = await f.client.delete("/accounts/1/friends/accepted/2", headers={"Authorization": "Bearer token"})

    assert result.status_code == 204
    assert result.content == b""
