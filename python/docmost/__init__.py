"""Docmost REST API client for Python."""
from docmost.client import DocmostClient
from docmost.exceptions import DocmostApiError
from docmost.response import parse_data
from docmost.types import ApiResponse, ErrorResponse

__version__ = "1.0.0"
__all__ = [
    "DocmostClient",
    "DocmostApiError",
    "ApiResponse",
    "ErrorResponse",
    "parse_data",
    "__version__",
]
