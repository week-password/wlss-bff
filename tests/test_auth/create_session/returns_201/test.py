from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["create_session_request", "create_session_response"])
async def test(f):
    result = await f.client.post("/accounts/sessions", json={"login": "john_doe", "password": "qwerty123"})

    assert result.status_code == 201
    assert result.json() == {
        "session": {
            "id": "f6d7ccf6-8c66-4a78-8ecc-d91cba589263",
            "accountId": 1,
        },
        "tokens": {
            "accessToken": "access token got from backend",
            "refreshToken": "refresh token got from backend",
        },
    }
