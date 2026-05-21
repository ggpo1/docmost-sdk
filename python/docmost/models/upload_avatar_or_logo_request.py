"""Generated multipart request UploadAvatarOrLogoRequest."""
from __future__ import annotations

from typing import BinaryIO, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class UploadAvatarOrLogoRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

    file: Union[bytes, BinaryIO] = Field(alias="file")
    type: str = Field(alias="type")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
