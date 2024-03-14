from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["delete_wish_request", "delete_wish_response"])
async def test(f):
    result = await f.client.delete("/accounts/1/wishes/1", headers={"Authorization": "Bearer token"})

    assert result.status_code == 204
    assert result.content == b""
