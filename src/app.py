from __future__ import annotations

from typing import TYPE_CHECKING

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import src.routes
from src.shared.exceptions import NotFoundException, TooLargeException


if TYPE_CHECKING:
    from fastapi import Request


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
            "name": "profile",
            "description": "Profile related functionality for managing profiles.",
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


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://185.154.195.26",
        "http://185.154.195.26:80",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(httpx.HTTPError)
def handle_http_error(_: Request, exception: httpx.HTTPStatusError) -> JSONResponse:
    return JSONResponse(
        status_code=exception.response.status_code,
        content=exception.response.json(),
    )


@app.exception_handler(NotFoundException)
async def handle_not_found(_: Request, exception: NotFoundException) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "resource": exception.resource,
            "description": exception.description,
            "details": exception.details,
        },
    )


@app.exception_handler(TooLargeException)
async def handle_too_large(_: Request, exception: TooLargeException) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "resource": exception.resource,
            "description": exception.description,
            "details": exception.details,
        },
    )
