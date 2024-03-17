from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def delete_friendships_request():
    return Predicate(method="DELETE", path="/accounts/1/friendships/2", headers={"Authorization": "Bearer token"})


@pytest.fixture
def delete_friendships_response():
    return Response(status_code=204)
