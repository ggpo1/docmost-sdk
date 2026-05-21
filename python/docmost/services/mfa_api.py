"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import DisableMfaDto, EnableMfaDto, MfaDto, RegenerateBackupCodesDto


class MFAApi:
    """MFA API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def mfa_setup(self) -> ApiResponse[Any]:
        return self._http.post("mfa/setup", body=None)

    def mfa_enable(self, request: EnableMfaDto) -> ApiResponse[Any]:
        return self._http.post("mfa/enable", body=request.model_dump(by_alias=True, exclude_none=True))

    def mfa_disable(self, request: DisableMfaDto) -> ApiResponse[Any]:
        return self._http.post("mfa/disable", body=request.model_dump(by_alias=True, exclude_none=True))

    def mfa_status(self) -> ApiResponse[Any]:
        return self._http.post("mfa/status", body=None)

    def mfa_regenerate_backup_codes(self, request: RegenerateBackupCodesDto) -> ApiResponse[Any]:
        return self._http.post("mfa/generate-backup-codes", body=request.model_dump(by_alias=True, exclude_none=True))

    def mfa_verify(self, request: MfaDto) -> ApiResponse[Any]:
        return self._http.post("mfa/verify", body=request.model_dump(by_alias=True, exclude_none=True))

    def mfa_validate_access(self) -> ApiResponse[Any]:
        return self._http.post("mfa/validate-access", body=None)

