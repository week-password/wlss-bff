from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"access_token": "access_token", "client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["create_wish_booking_request", "create_wish_booking_response"])
async def test(f):
    result = await f.client.post("/accounts/2/wishes/1/bookings", headers={"Authorization": f"Bearer {f.access_token}"})

    assert result.status_code == 204
    assert result.content == b""
