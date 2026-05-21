"""Generated multipart request ImportZipRequest."""
from __future__ import annotations

from typing import BinaryIO, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class ImportZipRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

    file: Union[bytes, BinaryIO] = Field(alias="file")
    space_id: str = Field(alias="spaceId")
    source: str = Field(alias="source")
    parent_page_id: Optional[str] = Field(default=None, alias="parentPageId")
