from __future__ import annotations

from fastapi import FastAPI

import src.routes


app = FastAPI(
    title="WLSS BFF API",
    description="BFF API for Wish List Sharing Service.",
    openapi_tags=[
        {
            "name": "account",
            "description": "Account-related functionality for managing accounts.",
        },
        {
            "name": "auth",
            "description": "Auth-related functionality for Signing Up/In/Out.",
        },
        {
            "name": "file",
            "description": "File related functionality for downloading and uploading files.",
        },
        {
            "name": "service",
            "description": "Maintenace related functionality.",
        },
        {
            "name": "wish",
            "description": "Wish and wish booking related functionality.",
        },
    ],
)


app.include_router(src.routes.router)
