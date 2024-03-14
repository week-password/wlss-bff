from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client"})
async def test(f):
    result = await f.client.post(
        "/files",
        headers={"Authorization": "Bearer token"},
        files={"file": ("image", b"image binary data", "image/png")},
    )

    assert result.status_code == 422
    assert result.json() == {
        "detail": [
            {
                "type": "enum",
                "loc": ["extension"],
                "msg": "Input should be 'gif', 'jfif', 'jif', 'jpe', 'jpeg', 'jpg', 'png' or 'webp'",
                "input": "",
                "ctx": {"expected": "'gif', 'jfif', 'jif', 'jpe', 'jpeg', 'jpg', 'png' or 'webp'"},
            },
        ],
    }
