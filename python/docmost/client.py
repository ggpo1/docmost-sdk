"""Docmost API client."""
from __future__ import annotations

from typing import Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.services.ai_api import AIApi
from docmost.services.api_keys_api import APIKeysApi
from docmost.services.attachment_search_api import AttachmentSearchApi
from docmost.services.attachments_api import AttachmentsApi
from docmost.services.auth_api import AuthApi
from docmost.services.cloud_api import CloudApi
from docmost.services.comment_resolution_api import CommentResolutionApi
from docmost.services.comments_api import CommentsApi
from docmost.services.export_api import ExportApi
from docmost.services.file_tasks_api import FileTasksApi
from docmost.services.groups_api import GroupsApi
from docmost.services.health_api import HealthApi
from docmost.services.import_api import ImportApi
from docmost.services.license_api import LicenseApi
from docmost.services.mfa_api import MFAApi
from docmost.services.pages_api import PagesApi
from docmost.services.search_api import SearchApi
from docmost.services.shares_api import SharesApi
from docmost.services.spaces_api import SpacesApi
from docmost.services.sso_api import SSOApi
from docmost.services.users_api import UsersApi
from docmost.services.version_api import VersionApi
from docmost.services.workspace_api import WorkspaceApi


class DocmostClient:
    """
    Client for the Docmost REST API.

    Authentication:
    - ``api_token``: Bearer token (recommended for automation)
    - ``email`` + ``password``: cookie session via ``/auth/login``
    """

    def __init__(
        self,
        base_url: str,
        *,
        api_token: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        login_on_startup: bool = True,
        timeout: float = 100.0,
        http_client: Optional[httpx.Client] = None,
    ) -> None:
        import httpx  # local import to keep package import light

        self._http = DocmostHttpClient(
            base_url,
            api_token=api_token,
            email=email,
            password=password,
            timeout=timeout,
            client=http_client,
        )
        if login_on_startup and email and not api_token:
            self._http.login()

        self.auth = AuthApi(self._http)
        self.users = UsersApi(self._http)
        self.workspace = WorkspaceApi(self._http)
        self.spaces = SpacesApi(self._http)
        self.pages = PagesApi(self._http)
        self.comments = CommentsApi(self._http)
        self.attachments = AttachmentsApi(self._http)
        self.search = SearchApi(self._http)
        self.attachment_search = AttachmentSearchApi(self._http)
        self.shares = SharesApi(self._http)
        self.groups = GroupsApi(self._http)
        self.export = ExportApi(self._http)
        self.import_ = ImportApi(self._http)
        self.file_tasks = FileTasksApi(self._http)
        self.health = HealthApi(self._http)
        self.version = VersionApi(self._http)
        self.api_keys = APIKeysApi(self._http)
        self.mfa = MFAApi(self._http)
        self.comment_resolution = CommentResolutionApi(self._http)
        self.license = LicenseApi(self._http)
        self.sso = SSOApi(self._http)
        self.ai = AIApi(self._http)
        self.cloud = CloudApi(self._http)

    def login(self) -> None:
        """Authenticate with email/password."""
        self._http.login()

    def logout(self) -> None:
        """Clear session cookie."""
        self._http.logout()

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> DocmostClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
