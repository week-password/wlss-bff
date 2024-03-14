from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs([
    "match_account_login_request_for_nonexistent_account",
    "match_account_login_response_for_nonexistent_account"])
async def test(f):
    result = await f.client.post("/accounts/logins/match", json={"login": "john_smith"})

    assert result.status_code == 404
    assert result.json() == {
        "resource": "Account",
        "description": "Requested resource not found.",
        "details": "Requested resource doesn't exist or has been deleted.",
    }
