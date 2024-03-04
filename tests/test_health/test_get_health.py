from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["get_health_request", "get_health_response"])
async def test_get_health_returns_correct_response(f):
    result = await f.client.get("/health")

    assert result.status_code == 200
    assert result.json() == {"status": "OK"}
