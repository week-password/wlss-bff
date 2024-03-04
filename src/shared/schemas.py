from __future__ import annotations

from typing import TypeVar

from api.shared import schemas as api_schemas
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


T = TypeVar("T", bound=BaseModel)


class Schema(api_schemas.Schema):
    """Customized 'BaseModel' class from pydantic."""

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    @classmethod
    def from_(cls: type[T], model: api_schemas.Schema) -> T:
        return cls.model_validate(model.model_dump())


class HTTPError(Schema):
    """Base schema for errors."""

    description: str
    details: str


class NotAuthenticatedResponse(HTTPError):  # noqa: N818
    """Schema for 401 UNAUTHORIZED response."""


class NotFoundResponse(HTTPError):  # noqa: N818
    """Schema for 404 NOT FOUND error."""

    resource: str


class NotAllowedResponse(HTTPError):  # noqa: N818
    """Schema for 403 FORBIDDEN error."""

    action: str
