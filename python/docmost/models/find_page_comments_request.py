"""Generated multipart request FindPageCommentsRequest."""
from __future__ import annotations

from typing import BinaryIO, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class FindPageCommentsRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

    page_id: str = Field(alias="pageId")
    limit: Optional[int] = Field(default=None, alias="limit")
    cursor: Optional[str] = Field(default=None, alias="cursor")
