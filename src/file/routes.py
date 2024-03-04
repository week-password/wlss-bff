from __future__ import annotations

import pathlib
from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, Path, status

from src.auth.dependencies import AccessToken
from src.file.dependencies import get_new_file, get_tmp_dir
from src.file.dtos import CreateFileRequest, CreateFileResponse, GetFileResponse
from src.shared import swagger as shared_swagger
from src.shared.fields import UuidField


router = APIRouter(tags=["file"])


@router.post(
    "/files",
    description="Upload new file.",
    responses={
        status.HTTP_201_CREATED: {"description": "File uploaded, file info returned."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
    },
    status_code=status.HTTP_201_CREATED,
    summary="Upload file.",
)
async def create_file(  # type: ignore[empty-body]
    background_tasks: BackgroundTasks,  # noqa: ARG001
    new_file: Annotated[CreateFileRequest, Depends(get_new_file)],  # noqa: ARG001
    access_token: AccessToken,  # noqa: ARG001
) -> CreateFileResponse:
    ...  # pragma: no cover


@router.get(
    "/files/{file_id}",
    description="Get (download) uploaded file.",
    responses={
        status.HTTP_200_OK: {"description": "Uploaded file returned."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    status_code=status.HTTP_200_OK,
    summary="Get file.",
)
async def get_file(  # type: ignore[empty-body]
    background_tasks: BackgroundTasks,  # noqa: ARG001
    file_id: Annotated[UuidField, Path(example="47b3d7a9-d7d3-459a-aac1-155997775a0e")],  # noqa: ARG001
    access_token: AccessToken,  # noqa: ARG001
    tmp_dir: Annotated[pathlib.Path, Depends(get_tmp_dir)],  # noqa: ARG001
) -> GetFileResponse:
    ...  # pragma: no cover
