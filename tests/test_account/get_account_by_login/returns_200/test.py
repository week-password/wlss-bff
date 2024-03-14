from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["get_account_by_login_request", "get_account_by_login_response"])
async def test(f):
    result = await f.client.get("/accounts/logins/john_doe", headers={"Authorization": "Bearer token"})

    assert result.status_code == 200
    assert result.json() == {"id": 1, "login": "john_doe"}
