"""Generated from OpenAPI schema UpdateCommentDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UpdateCommentDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    comment_id: str = Field(alias="commentId")
    content: str = Field(alias="content")
