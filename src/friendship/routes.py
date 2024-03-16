from __future__ import annotations

from typing import Annotated

from api.shared.fields import IdField
from fastapi import APIRouter, Path, status

from src.auth.dependencies import Authorization
from src.friendship import controllers
from src.friendship.dtos import GetIncomingRequestsResponse, GetOutgoingRequestsResponse
from src.shared import swagger as shared_swagger


router = APIRouter(tags=["friendship"])


@router.post(
    "/accounts/{account_id}/friends/outgoing/{friend_id}",
    description="Create friendship request with `account_id` as a sender and `friend_id` as a receiver.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "New friendship request created."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Create friendship request.",
)
async def create_outgoing_request(
    account_id: Annotated[IdField, Path(example=42)],
    friend_id: Annotated[IdField, Path(example=18)],
    authorization: Authorization,
) -> None:
    return await controllers.create_outgoing_request(account_id, friend_id, authorization)


@router.get(
    "/accounts/{account_id}/friends/outgoing",
    description="Get outgoing friendship requests which was sent by `account_id`",
    responses={
        status.HTTP_200_OK: {"description": "Outgoing requests returned."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    status_code=status.HTTP_200_OK,
    summary="Get outgoing requests.",
)
async def get_outgoing_requests(
    account_id: Annotated[IdField, Path(example=42)],
    authorization: Authorization,
) -> GetOutgoingRequestsResponse:
    return await controllers.get_outgoing_requests(account_id, authorization)


@router.delete(
    "/accounts/{account_id}/friends/outgoing/{friend_id}",
    description="Cancel (delete) outgoing friendship request which was sent by `account_id` to `friend_id`.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Outgoing requests cancelled (deleted)."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Cancel (delete) outgoing request.",
)
async def cancel_outgoing_request(
    account_id: Annotated[IdField, Path(example=42)],
    friend_id: Annotated[IdField, Path(example=18)],
    authorization: Authorization,
) -> None:
    return await controllers.cancel_outgoing_request(account_id, friend_id, authorization)


@router.get(
    "/accounts/{account_id}/friends/incoming",
    description="Get incoming friendship requests which was sent by `account_id`",
    status_code=status.HTTP_200_OK,
    summary="Get incoming requests.",
)
async def get_incoming_requests(
    account_id: Annotated[IdField, Path(example=42)],
    authorization: Authorization,
) -> GetIncomingRequestsResponse:
    return await controllers.get_incoming_requests(account_id, authorization)


@router.post(
    "/accounts/{account_id}/friends/accepted/{friend_id}",
    description="Accept friendship request which was sent by `friend_id` to `account_id`.",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Accept incoming friendship request.",
)
async def accept_incoming_request(
    account_id: Annotated[IdField, Path(example=42)],
    friend_id: Annotated[IdField, Path(example=18)],
    authorization: Authorization,
) -> None:
    return await controllers.accept_incoming_request(account_id, friend_id, authorization)


@router.delete(
    "/accounts/{account_id}/friends/incoming/{friend_id}",
    description="Reject incoming friendship request which was sent by `friend_id` to `account_id`.",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Reject incoming request.",
)
async def reject_incoming_request(
    account_id: Annotated[IdField, Path(example=42)],
    friend_id: Annotated[IdField, Path(example=18)],
    authorization: Authorization,
) -> None:
    return await controllers.reject_incoming_request(account_id, friend_id, authorization)
