"""Helpers for typed API response data."""
from __future__ import annotations

from typing import Any, Optional, Type, TypeVar

from pydantic import BaseModel

from docmost.types import ApiResponse

T = TypeVar("T", bound=BaseModel)


def parse_data(response: ApiResponse[Any], model: Type[T]) -> Optional[T]:
    """Deserialize ``response.data`` into a Pydantic model."""
    if response.data is None:
        return None
    if isinstance(response.data, model):
        return response.data
    if isinstance(response.data, BaseModel):
        return model.model_validate(response.data.model_dump())
    return model.model_validate(response.data)
