from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"access_token": "access_token", "client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(
    ["get_account_wishes_request", "get_account_wishes_response"],
    ["get_wish_bookings_request", "get_wish_bookings_response"],
)
async def test(f):
    result = await f.client.get("/accounts/1/wishes", headers={"Authorization": f"Bearer {f.access_token}"})

    assert result.status_code == 200
    assert result.json() == [
        {
            "id": 1,
            "avatarId": "0b928aaa-521f-47ec-8be5-396650e2a187",
            "description": "I'm gonna take my horse to the old town road.",
            "title": "Horse",
            "bookingId": None,
            "bookingStatus": "notBooked",
        },
        {
            "id": 2,
            "avatarId": "4b94605b-f5e1-40b1-b9fc-c635c9529e3e",
            "description": "I need some sleep. Time to put the old horse down.",
            "title": "Sleep",
            "bookingId": 2,
            "bookingStatus": "bookedByCurrentAccount",
        },
        {
            "id": 3,
            "avatarId": "25adf2cd-0e57-451e-968c-2d008ba57e45",
            "description": "Something sweet, like sweets, or sweather",
            "title": "Sweet",
            "bookingId": 3,
            "bookingStatus": "bookedByAnotherAccount",
        },
    ]
