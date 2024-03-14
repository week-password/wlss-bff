from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def update_profile_request():
    request_body = {
        "avatar_id": "f6bdfda7-0a5b-4ed5-800f-ac352656abec",
        "description": "NEW John Doe's profile description",
        "name": "John Doe",
    }
    return Predicate(
        method="PUT",
        path="/accounts/1/profile",
        body=request_body,
        headers={"Authorization": "Bearer token"},
    )


@pytest.fixture
def update_profile_response():
    response_body = {
        "account_id": 1,
        "avatar_id": "f6bdfda7-0a5b-4ed5-800f-ac352656abec",
        "description": "NEW John Doe's profile description",
        "name": "John Doe",
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
