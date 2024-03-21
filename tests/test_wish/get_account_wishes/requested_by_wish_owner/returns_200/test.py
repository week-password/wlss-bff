from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({
    "access_token": "access_token_for_account_owner",
    "client": "client",
    "api": "api_configured_with_api_stubs",
})
@pytest.mark.api_stubs(["get_account_wishes_request", "get_account_wishes_response"])
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
            "bookingStatus": None,
        },
        {
            "id": 2,
            "avatarId": "4b94605b-f5e1-40b1-b9fc-c635c9529e3e",
            "description": "I need some sleep. Time to put the old horse down.",
            "title": "Sleep",
            "bookingId": None,
            "bookingStatus": None,
        },
    ]
