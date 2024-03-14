from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["get_file_request", "get_file_response"])
async def test(f):
    result = await f.client.get("/files/d3bb68db-052f-4851-b74d-d9c884fd43df")

    assert result.status_code == 200
    assert result.content == b"image binary data"
