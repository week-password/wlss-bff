from __future__ import annotations

from unittest.mock import patch

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client"})
@patch("src.file.dependencies.MAX_SIZE", 10)  # lower max size to improve test's performance
async def test(f):
    large_image_data = b"x" * 11
    result = await f.client.post(
        "/files",
        headers={"Authorization": "Bearer token"},
        files={"file": ("image.png", large_image_data, "image/png")},
    )

    assert result.status_code == 413
    assert result.json() == {
        "resource": "file",
        "description": "File size is too large.",
        "details": "File size is too large and it cannot be handled.",
    }
