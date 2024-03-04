from __future__ import annotations

from typing import TYPE_CHECKING

from api.client import Api
from api.file import dtos as api_dtos

from src.config import CONFIG
from src.file.dtos import CreateFileResponse, GetFileResponse


if TYPE_CHECKING:
    from pathlib import Path

    from api.shared.fields import UuidField
    from fastapi.security import HTTPAuthorizationCredentials

    from src.file.dtos import CreateFileRequest


async def create_file(
    request_data: CreateFileRequest,
    authorization: HTTPAuthorizationCredentials,
) -> CreateFileResponse:
    api = Api(base_url=CONFIG.BFF_URL)
    api_request_data = api_dtos.CreateFileRequest.from_(request_data)
    response = await api.file.create_file(api_request_data, authorization.credentials)
    return CreateFileResponse.from_(response)


async def get_file(file_id: UuidField, authorization: HTTPAuthorizationCredentials, tmp_dir: Path) -> GetFileResponse:
    api = Api(base_url=CONFIG.BFF_URL)
    tmp_file_path = tmp_dir / str(file_id)
    response = await api.file.get_file(file_id, authorization.credentials, tmp_file_path)
    return GetFileResponse(
        path=response.path,
        status_code=response.status_code,
        media_type=response.media_type,
    )
