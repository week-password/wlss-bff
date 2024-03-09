from __future__ import annotations

from typing import Any, TYPE_CHECKING, TypeVar

from pydantic import (
    field_validator,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.shared.environment import get_dotenv_path


if TYPE_CHECKING:
    from typing import Final


T = TypeVar("T", bound=Any)


class _Config(BaseSettings):
    BFF_URL: str

    MOUNTEBANK_SERVER_HOST: str
    MOUNTEBANK_SERVER_PORT: str
    MOUNTEBANK_IMPOSTOR_PORT: str


    model_config = SettingsConfigDict(env_file=get_dotenv_path(), extra="allow", frozen=True)

    @field_validator("*")
    @classmethod
    def validate_types(cls: type[_Config], value: T) -> T:  # pragma: no cover
        """Validate fields of particular types. Mostly it is used to add some constraints to builtin python types."""
        if isinstance(value, str):
            if value.startswith(" ") or value.endswith(" "):
                # leading / trailing whitespaces are disallowed since they're not significant
                msg = "String should not have leading or trailing whitespaces."
                raise ValueError(msg)
            if not value:
                # empty string is disallowed since it's exactly the same as missing value
                msg = "String value should not be blank"
                raise ValueError(msg)
        return value


CONFIG: Final = _Config()
