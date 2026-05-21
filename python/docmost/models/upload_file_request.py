"""Generated multipart request UploadFileRequest."""
from __future__ import annotations

from typing import BinaryIO, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class UploadFileRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

    file: Union[bytes, BinaryIO] = Field(alias="file")
    page_id: str = Field(alias="pageId")
    attachment_id: Optional[str] = Field(default=None, alias="attachmentId")
