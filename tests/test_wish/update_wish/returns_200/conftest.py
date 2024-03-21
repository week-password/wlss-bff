from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def update_wish_request():
    request_body = {
        "avatar_id": None,
        "description": "I'm gonna take my NEW horse to the old town road.",
        "title": "NEW Horse",
    }
    return Predicate(
        method="PUT",
        path="/accounts/1/wishes/1",
        body=request_body,
        headers={"Authorization": "Bearer token"},
    )

@pytest.fixture
def update_wish_response():
    response_body = {
        "id": 1,
        "account_id": 1,
        "created_at": "2024-02-28T17:25:38.795Z",
        "avatar_id": None,
        "description": "I'm gonna take my NEW horse to the old town road.",
        "title": "NEW Horse",
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
