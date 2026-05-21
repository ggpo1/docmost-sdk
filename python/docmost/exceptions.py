"""Docmost API errors."""
from __future__ import annotations

from typing import Optional

from docmost.models.api_response import ErrorResponse


class DocmostApiError(Exception):
    """Raised when the Docmost API returns an error HTTP status or success=false."""

    def __init__(
        self,
        message: str,
        status_code: int,
        *,
        error: Optional[ErrorResponse] = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error = error
