from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Body, Path, status

from src.auth.dependencies import AccessToken
from src.shared import swagger as shared_swagger
from src.shared.fields import IdField
from src.wish.dtos import CreateWishBookingRequest


router = APIRouter(tags=["wish"])


@router.delete(
    "/accounts/{account_id}/wishes/{wish_id}",
    description="Delete particular wish and related bookings.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Wish and related bookings are deleted."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete particular wish.",
)
async def delete_wish(
    account_id: Annotated[IdField, Path(example=42)],  # noqa: ARG001
    wish_id: Annotated[IdField, Path(example=17)],  # noqa: ARG001
    access_token: AccessToken,  # noqa: ARG001
) -> None:
    ...  # pragma: no cover


@router.post(
    "/accounts/{account_id}/wishes/{wish_id}/bookings",
    description="Book particular wish for particular account.",
    responses={
        status.HTTP_201_CREATED: {"description": "Wish booking is created successfully. Booking info returned."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    status_code=status.HTTP_201_CREATED,
    summary="Book particular wish.",
)
async def create_wish_booking(
    account_id: Annotated[IdField, Path(example=42)],  # noqa: ARG001
    request_data: Annotated[CreateWishBookingRequest, Body()],  # noqa: ARG001
    access_token: AccessToken,  # noqa: ARG001
) -> None:
    ...  # pragma: no cover


@router.delete(
    "/bookings/{booking_id}",
    description="Delete particular wish booking.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Wish Booking has been removed."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete wish booking.",
)
async def delete_wish_booking(
    booking_id: Annotated[IdField, Path(example=42)],  # noqa: ARG001
    access_token: AccessToken,  # noqa: ARG001
) -> None:
    ...  # pragma: no cover
