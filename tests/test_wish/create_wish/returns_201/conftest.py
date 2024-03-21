from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def create_wish_request():
    request_body = {
        "avatar_id": None,
        "description": "I'm gonna take my horse to the old town road.",
        "title": "Horse",
    }
    return Predicate(
        method="POST",
        path="/accounts/1/wishes",
        body=request_body,
        headers={"Authorization": "Bearer token"},
    )

@pytest.fixture
def create_wish_response():
    response_body = {
        "id": 1,
        "account_id": 1,
        "created_at": "2024-02-28T17:25:38.795Z",
        "avatar_id": None,
        "description": "I'm gonna take my horse to the old town road.",
        "title": "Horse",
    }
    return Response(body=response_body, status_code=201, headers={"content-type": "application/json"})
