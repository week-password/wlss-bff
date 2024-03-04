from __future__ import annotations

import pathlib
from typing import Annotated

from api.shared.fields import UuidField
from fastapi import APIRouter, BackgroundTasks, Depends, Path, status

from src.auth.dependencies import Authorization
from src.file import controllers
from src.file.dependencies import get_new_file, get_tmp_dir
from src.file.dtos import CreateFileRequest, CreateFileResponse, GetFileResponse
from src.shared import swagger as shared_swagger


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
async def create_file(
    background_tasks: BackgroundTasks,  # noqa: ARG001
    request_data: Annotated[CreateFileRequest, Depends(get_new_file)],
    authorization: Authorization,
) -> CreateFileResponse:
    return await controllers.create_file(request_data, authorization)


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
async def get_file(
    background_tasks: BackgroundTasks,  # noqa: ARG001
    file_id: Annotated[UuidField, Path(example="47b3d7a9-d7d3-459a-aac1-155997775a0e")],
    authorization: Authorization,
    tmp_dir: Annotated[pathlib.Path, Depends(get_tmp_dir)],
) -> GetFileResponse:
    return await controllers.get_file(file_id, authorization, tmp_dir)
