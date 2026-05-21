"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import RemoveIconDto, UploadAvatarOrLogoRequest, UploadFileRequest


class AttachmentsApi:
    """Attachments API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def upload_file(self, request: UploadFileRequest) -> ApiResponse[Any]:
        path = "files/upload"
        files: dict[str, tuple[str, bytes | Any, str]] = {}
        data: dict[str, str] = {}
        raw = request.file
        content = raw.read() if hasattr(raw, 'read') else raw
        files["file"] = ("upload.bin", content, "application/octet-stream")
        if request.page_id is not None: data["pageId"] = str(request.page_id)
        if request.attachment_id is not None: data["attachmentId"] = str(request.attachment_id)
        return self._http.post_multipart(path, data=data or None, files=files or None)

    def get_file(self, fileId: str, fileName: str) -> httpx.Response:
        return self._http.get_raw(f"files/{DocmostHttpClient.escape_path_segment(fileId)}/{DocmostHttpClient.escape_path_segment(fileName)}")

    def get_public_file(self, fileId: str, fileName: str, jwt: Optional[str] = None) -> httpx.Response:
        path = f"files/public/{DocmostHttpClient.escape_path_segment(fileId)}/{DocmostHttpClient.escape_path_segment(fileName)}"
        params: dict[str, str] = {}
        if jwt is not None:
            params['jwt'] = jwt
        return self._http.get_raw(path, params=params or None)

    def upload_avatar_or_logo(self, request: UploadAvatarOrLogoRequest) -> ApiResponse[Any]:
        path = "attachments/upload-image"
        files: dict[str, tuple[str, bytes | Any, str]] = {}
        data: dict[str, str] = {}
        raw = request.file
        content = raw.read() if hasattr(raw, 'read') else raw
        files["file"] = ("upload.bin", content, "application/octet-stream")
        if request.type is not None: data["type"] = str(request.type)
        if request.space_id is not None: data["spaceId"] = str(request.space_id)
        return self._http.post_multipart(path, data=data or None, files=files or None)

    def get_logo_or_avatar(self, attachmentType: str, fileName: str) -> httpx.Response:
        return self._http.get_raw(f"attachments/img/{DocmostHttpClient.escape_path_segment(attachmentType)}/{DocmostHttpClient.escape_path_segment(fileName)}")

    def remove_icon(self, request: RemoveIconDto) -> ApiResponse[Any]:
        return self._http.post("attachments/remove-icon", body=request.model_dump(by_alias=True, exclude_none=True))

