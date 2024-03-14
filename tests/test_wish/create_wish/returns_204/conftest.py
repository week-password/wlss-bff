from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def create_wish_booking_request():
    return Predicate(
        method="POST",
        path="/accounts/2/wishes/1/bookings",
        body={"account_id": 1},
        headers={"Authorization": "Bearer token"},
    )

@pytest.fixture
def create_wish_booking_response():
    response_body = {
        "account_id": 1,
        "created_at": "2024-02-28T17:25:38.795Z",
        "wish_id": 1,
    }
    return Response(body=response_body, status_code=201, headers={"content-type": "application/json"})
