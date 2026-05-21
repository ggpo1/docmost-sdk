"""API envelope types."""
from __future__ import annotations

from typing import Generic, Optional, TypeVar, Union

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(populate_by_name=True)

    data: Optional[T] = Field(default=None, alias="data")
    success: bool = Field(alias="success")
    status: int = Field(alias="status")


class ErrorResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status_code: Optional[int] = Field(default=None, alias="statusCode")
    message: Optional[Union[str, list[str]]] = Field(default=None, alias="message")
    error: Optional[str] = Field(default=None, alias="error")
