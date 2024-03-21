from __future__ import annotations

import jwt
import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def access_token():
    return jwt.encode({"account_id": 2}, key="some-secret-key")


@pytest.fixture
def get_account_wishes_request(access_token):
    return Predicate(method="GET", path="/accounts/1/wishes", headers={"Authorization": f"Bearer {access_token}"})


@pytest.fixture
def get_account_wishes_response():
    response_body = {
        "wishes": [
            {
                "id": 1,
                "account_id": 1,
                "avatar_id": "0b928aaa-521f-47ec-8be5-396650e2a187",
                "created_at": "2024-02-28T17:25:38.795Z",
                "description": "I'm gonna take my horse to the old town road.",
                "title": "Horse",
            },
            {
                "id": 2,
                "account_id": 1,
                "avatar_id": "4b94605b-f5e1-40b1-b9fc-c635c9529e3e",
                "created_at": "2024-02-28T17:25:38.795Z",
                "description": "I need some sleep. Time to put the old horse down.",
                "title": "Sleep",
            },
            {
                "id": 3,
                "account_id": 1,
                "avatar_id": "25adf2cd-0e57-451e-968c-2d008ba57e45",
                "created_at": "2024-02-28T17:25:38.795Z",
                "description": "Something sweet, like sweets, or sweather",
                "title": "Sweet",
            },
        ],
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_wish_bookings_request(access_token):
    return Predicate(
        method="GET",
        path="/accounts/1/wishes/bookings",
        headers={"Authorization": f"Bearer {access_token}"},
    )


@pytest.fixture
def get_wish_bookings_response():
    response_body = {
        "wish_bookings": [
            {
                "id": 2,
                "account_id": 2,
                "created_at": "2024-02-28T17:25:38.795Z",
                "wish_id": 2,
            },
            {
                "id": 3,
                "account_id": 3,
                "created_at": "2024-02-28T17:25:38.795Z",
                "wish_id": 3,
            },
        ],
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
