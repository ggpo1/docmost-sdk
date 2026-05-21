"""HTTP transport with Bearer and cookie session auth."""
from __future__ import annotations

import threading
from typing import Any, Mapping, Optional
from urllib.parse import quote

import httpx

from docmost.exceptions import DocmostApiError
from docmost.models.api_response import ApiResponse, ErrorResponse
from docmost.models.login_dto import LoginDto


class DocmostHttpClient:
    def __init__(
        self,
        base_url: str,
        *,
        api_token: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        timeout: float = 100.0,
        client: Optional[httpx.Client] = None,
    ) -> None:
        if api_token and (email or password):
            raise ValueError("Use either api_token or email/password, not both.")

        self._api_token = api_token
        self._email = email
        self._password = password
        self._logged_in = False
        self._login_lock = threading.Lock()

        api_base = base_url.rstrip("/") + "/api/"
        self._client = client or httpx.Client(
            base_url=api_base,
            timeout=timeout,
            follow_redirects=True,
        )
        self._owns_client = client is None

    def close(self) -> None:
        if self._owns_client:
            self._client.close()

    def __enter__(self) -> DocmostHttpClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def ensure_authenticated(self) -> None:
        if self._api_token:
            return
        if not self._email or not self._password:
            raise RuntimeError("Provide api_token or email and password.")
        if self._logged_in:
            return
        with self._login_lock:
            if self._logged_in:
                return
            self._login()
            self._logged_in = True

    def login(self) -> None:
        """Authenticate with email/password (cookie session)."""
        if self._api_token:
            return
        with self._login_lock:
            self._login()
            self._logged_in = True

    def logout(self) -> ApiResponse[Any]:
        self.post("auth/logout", body=None)
        self._logged_in = False
        return ApiResponse[Any](data=None, success=True, status=200)

    def _login(self) -> None:
        payload = LoginDto(email=self._email or "", password=self._password or "")
        response = self._client.post(
            "auth/login",
            json=payload.model_dump(by_alias=True, exclude_none=True),
        )
        self._raise_for_status(response)
        envelope = ApiResponse[Any].model_validate(response.json())
        if not envelope.success:
            raise DocmostApiError("Login failed.", envelope.status)

    def _headers(self) -> dict[str, str]:
        if self._api_token:
            return {"Authorization": f"Bearer {self._api_token}"}
        return {}

    def post(self, path: str, *, body: Optional[Mapping[str, Any]]) -> ApiResponse[Any]:
        self.ensure_authenticated()
        response = self._client.post(
            path.lstrip("/"),
            json=body,
            headers=self._headers(),
        )
        return self._parse_envelope(response)

    def get(
        self,
        path: str,
        *,
        params: Optional[dict[str, str]] = None,
    ) -> ApiResponse[Any]:
        self.ensure_authenticated()
        response = self._client.get(
            path.lstrip("/"),
            params=params,
            headers=self._headers(),
        )
        return self._parse_envelope(response)

    def get_raw(
        self,
        path: str,
        *,
        params: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        self.ensure_authenticated()
        response = self._client.get(
            path.lstrip("/"),
            params=params,
            headers=self._headers(),
        )
        self._raise_for_status(response)
        return response

    def post_multipart(
        self,
        path: str,
        *,
        data: Optional[dict[str, str]],
        files: Optional[dict[str, tuple[str, Any, str]]],
    ) -> ApiResponse[Any]:
        self.ensure_authenticated()
        response = self._client.post(
            path.lstrip("/"),
            data=data,
            files=files,
            headers=self._headers(),
        )
        return self._parse_envelope(response)

    @staticmethod
    def _parse_envelope(response: httpx.Response) -> ApiResponse[Any]:
        DocmostHttpClient._raise_for_status(response)
        envelope = ApiResponse[Any].model_validate(response.json())
        if not envelope.success:
            raise DocmostApiError(
                f"API returned success=false (status {envelope.status}).",
                envelope.status,
            )
        return envelope

    @staticmethod
    def _raise_for_status(response: httpx.Response) -> None:
        if response.is_success:
            return
        error: Optional[ErrorResponse] = None
        try:
            error = ErrorResponse.model_validate(response.json())
        except Exception:
            pass
        message = (
            (error.error if error else None)
            or (str(error.message) if error and error.message else None)
            or response.reason_phrase
            or "Request failed."
        )
        raise DocmostApiError(message, response.status_code, error=error)

    @staticmethod
    def escape_path_segment(value: str) -> str:
        return quote(value, safe="")
