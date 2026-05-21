"""Generated from OpenAPI schema ErrorResponse."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ErrorResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status_code: Optional[int] = Field(default=None, alias="statusCode")
    message: Optional[dict[str, object]] = Field(default=None, alias="message")
    error: Optional[str] = Field(default=None, alias="error")
