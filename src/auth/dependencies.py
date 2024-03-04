from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


AccessToken = Annotated[
    HTTPAuthorizationCredentials,
    Depends(
        HTTPBearer(
            scheme_name="Access token",
            description="Short-living token needed to authenticate the request.",
        ),
    ),
]
