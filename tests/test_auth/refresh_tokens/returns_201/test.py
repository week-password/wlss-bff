from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["refresh_tokens_request", "refresh_tokens_response"])
async def test(f):
    result = await f.client.post(
        "/accounts/1/sessions/f6d7ccf6-8c66-4a78-8ecc-d91cba589263/tokens",
        headers={"Authorization": "Bearer refresh-token"},
    )

    assert result.status_code == 201
    assert result.json() == {
        "accessToken": "fresh access token got from backend",
        "refreshToken": "fresh refresh token got from backend",
    }
