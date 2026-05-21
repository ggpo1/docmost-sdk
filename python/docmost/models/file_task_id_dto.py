"""Generated from OpenAPI schema FileTaskIdDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class FileTaskIdDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    file_task_id: str = Field(alias="fileTaskId")
