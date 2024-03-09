from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["get_accounts_request_for_two_accounts", "get_accounts_response_for_two_accounts"])
async def test_get_accounts_returns_200_with_correct_response(f):
    result = await f.client.get(
        "/accounts",
        params={"id": [1], "login": ["john_smith"]},
        headers={"Authorization": "Bearer token"},
    )

    assert result.status_code == 200
    assert result.json() == [
        {"id": 1, "login": "john_doe"},
        {"id": 2, "login": "john_smith"},
    ]
