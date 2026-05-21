"""Generated from OpenAPI schema CommentIdDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CommentIdDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    comment_id: str = Field(alias="commentId")
