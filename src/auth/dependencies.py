from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


Authorization = Annotated[
    HTTPAuthorizationCredentials,
    Depends(
        HTTPBearer(
            scheme_name="Access token",
            description="Short-living token needed to authenticate the request.",
        ),
    ),
]


AuthorizationRefresh = Annotated[
    HTTPAuthorizationCredentials,
    Depends(
        HTTPBearer(
            scheme_name="Refresh token",
            description="Long-living token needed to refresh expired tokens.",
        ),
    ),
]
