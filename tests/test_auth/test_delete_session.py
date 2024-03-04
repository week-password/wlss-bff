from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["delete_session_request", "delete_session_response"])
async def test_delete_session_returns_204_with_correct_response(f):
    result = await f.client.delete(
        "/accounts/1/sessions/f6d7ccf6-8c66-4a78-8ecc-d91cba589263",
        headers={"Authorization": "Bearer token"},
    )

    assert result.status_code == 204
    assert result.content == b""
