"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import ChangePasswordDto, CreateAdminUserDto, ForgotPasswordDto, LoginDto, PasswordResetDto, VerifyUserTokenDto


class AuthApi:
    """Auth API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def login(self, request: LoginDto) -> ApiResponse[Any]:
        return self._http.post("auth/login", body=request.model_dump(by_alias=True, exclude_none=True))

    def setup_workspace(self, request: CreateAdminUserDto) -> ApiResponse[Any]:
        return self._http.post("auth/setup", body=request.model_dump(by_alias=True, exclude_none=True))

    def change_password(self, request: ChangePasswordDto) -> ApiResponse[Any]:
        return self._http.post("auth/change-password", body=request.model_dump(by_alias=True, exclude_none=True))

    def forgot_password(self, request: ForgotPasswordDto) -> ApiResponse[Any]:
        return self._http.post("auth/forgot-password", body=request.model_dump(by_alias=True, exclude_none=True))

    def password_reset(self, request: PasswordResetDto) -> ApiResponse[Any]:
        return self._http.post("auth/password-reset", body=request.model_dump(by_alias=True, exclude_none=True))

    def verify_reset_token(self, request: VerifyUserTokenDto) -> ApiResponse[Any]:
        return self._http.post("auth/verify-token", body=request.model_dump(by_alias=True, exclude_none=True))

    def collab_token(self) -> ApiResponse[Any]:
        return self._http.post("auth/collab-token", body=None)

    def logout(self) -> ApiResponse[Any]:
        return self._http.post("auth/logout", body=None)

