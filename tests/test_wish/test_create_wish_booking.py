from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["create_wish_booking_request", "create_wish_booking_response"])
async def test_create_wish_booking_returns_204_with_correct_response(f):
    result = await f.client.post(
        "/accounts/2/wishes/1/bookings",
        json={"accountId": 1, "wishId": 1},
        headers={"Authorization": "Bearer token"},
    )

    assert result.status_code == 204
    assert result.content == b""
