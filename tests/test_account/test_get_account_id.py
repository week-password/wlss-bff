from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["get_account_id_request", "get_account_id_response"])
async def test_get_account_id_returns_200_with_correct_response(f):
    result = await f.client.get("/accounts/logins/john_doe/id", headers={"Authorization": "Bearer token"})

    assert result.status_code == 200
    assert result.json() == {"id": 42}


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["get_account_id_request", "get_account_id_404_response"])
async def test_get_account_id_with_nonexistent_account_returns_404_with_correct_response(f):
    result = await f.client.get("/accounts/logins/john_doe/id", headers={"Authorization": "Bearer token"})

    assert result.status_code == 404
    assert result.json() == {
        "resource": "Account",
        "description": "Requested resource not found.",
        "details": "Requested resource doesn't exist or has been deleted.",
    }
