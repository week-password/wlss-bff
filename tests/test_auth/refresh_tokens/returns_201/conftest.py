from __future__ import annotations

import json

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def refresh_tokens_request():
    return Predicate(
        method="POST",
        path="/accounts/1/sessions/f6d7ccf6-8c66-4a78-8ecc-d91cba589263/tokens",
        headers={"Authorization": "Bearer refresh-token"},
    )

@pytest.fixture
def refresh_tokens_response():
    response_body = {
        "access_token": "fresh access token got from backend",
        "refresh_token": "fresh refresh token got from backend",
    }
    return Response(body=json.dumps(response_body), status_code=201, headers={"content-type": "application/json"})
