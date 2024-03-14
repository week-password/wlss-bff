from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def delete_wish_request():
    return Predicate(
        method="DELETE",
        path="/accounts/1/wishes/1",
        headers={"Authorization": "Bearer token"},
    )


@pytest.fixture
def delete_wish_response():
    return Response(body=None, status_code=204)
