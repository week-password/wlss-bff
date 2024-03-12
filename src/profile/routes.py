from __future__ import annotations

from api.shared.fields import IdField
from fastapi import APIRouter, status

from src.auth.dependencies import Authorization
from src.profile import controllers
from src.profile.dtos import GetProfileResponse, UpdateProfileRequest, UpdateProfileResponse
from src.shared import swagger as shared_swagger


router = APIRouter(tags=["profile"])


@router.get(
    "/accounts/{account_id}/profile",
    description="Get profile info.",
    responses={
        status.HTTP_200_OK: {"description": "Profile info returned."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    status_code=status.HTTP_200_OK,
    summary="Get profile.",
)
async def get_profile(account_id: IdField, authorization: Authorization) -> GetProfileResponse:
    return await controllers.get_profile(account_id, authorization)


@router.put(
    "/accounts/{account_id}/profile",
    description="Update Profile info.",
    responses={
        status.HTTP_200_OK: {"description": "Profile info is updated. Profile returned."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    status_code=status.HTTP_200_OK,
    summary="Update profile info.",
)
async def update_profile(
    account_id: IdField,
    request_data: UpdateProfileRequest,
    authorization: Authorization,
) -> UpdateProfileResponse:
    return await controllers.update_profile(account_id, request_data, authorization)
