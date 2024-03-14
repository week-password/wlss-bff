from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["match_account_login_request", "match_account_login_response"])
async def test(f):
    result = await f.client.post("/accounts/logins/match", json={"login": "john_doe"})

    assert result.status_code == 204
