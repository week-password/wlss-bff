from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["create_file_request", "create_file_response"])
async def test(f):
    result = await f.client.post(
        "/files",
        headers={"Authorization": "Bearer token"},
        files={"file": ("image.png", b"image binary data", "image/png")},
    )

    assert result.status_code == 201
    assert result.json() == {
        "id": "d3bb68db-052f-4851-b74d-d9c884fd43df",
        "extension": "png",
        "mimeType": "image/png",
        "size": 17,
    }
