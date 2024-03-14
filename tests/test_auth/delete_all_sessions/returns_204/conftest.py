from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def delete_all_sessions_request():
    return Predicate(method="DELETE", path="/accounts/1/sessions", headers={"Authorization": "Bearer token"})


@pytest.fixture
def delete_all_sessions_response():
    return Response(status_code=204, headers={"content-type": "application/json"})
