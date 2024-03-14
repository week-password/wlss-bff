from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["get_health_request", "get_health_response"])
async def test(f):
    result = await f.client.get("/health")

    assert result.status_code == 200
    assert result.json() == {"status": "OK"}
