from __future__ import annotations

from fastapi import status

from src.shared.exceptions import NotFoundException


class AccountNotFoundError(NotFoundException):
    resource: str = "Account"

    description = "Requested resource not found."
    details = "Requested resource doesn't exist or has been deleted."
    status_code = status.HTTP_404_NOT_FOUND
