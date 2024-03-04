from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["delete_wish_booking_request", "delete_wish_booking_response"])
async def test_delete_wish_booking_returns_204_with_correct_response(f):
    result = await f.client.delete("/accounts/1/wishes/1/bookings/1", headers={"Authorization": "Bearer token"})

    assert result.status_code == 204
    assert result.content == b""
