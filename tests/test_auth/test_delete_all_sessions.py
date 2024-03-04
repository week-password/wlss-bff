from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["delete_all_sessions_request", "delete_all_sessions_response"])
async def test_delete_all_sessions_returns_204_with_correct_response(f):
    result = await f.client.delete("/accounts/1/sessions", headers={"Authorization": "Bearer token"})

    assert result.status_code == 204
    assert result.content == b""
