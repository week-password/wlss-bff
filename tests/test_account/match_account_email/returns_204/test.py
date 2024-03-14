from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["match_account_email_request", "match_account_email_response"])
async def test(f):
    result = await f.client.post("/accounts/emails/match", json={"email": "john.doe@mail.com"})

    assert result.status_code == 204
