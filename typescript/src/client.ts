/** Docmost API client. */
import { DocmostHttpClient } from './http-client.js';
import type { DocmostClientOptions } from './types.js';
import { AIApi } from './services/ai-api.js';
import { APIKeysApi } from './services/api-keys-api.js';
import { AttachmentSearchApi } from './services/attachment-search-api.js';
import { AttachmentsApi } from './services/attachments-api.js';
import { AuthApi } from './services/auth-api.js';
import { CloudApi } from './services/cloud-api.js';
import { CommentResolutionApi } from './services/comment-resolution-api.js';
import { CommentsApi } from './services/comments-api.js';
import { ExportApi } from './services/export-api.js';
import { FileTasksApi } from './services/file-tasks-api.js';
import { GroupsApi } from './services/groups-api.js';
import { HealthApi } from './services/health-api.js';
import { ImportApi } from './services/import-api.js';
import { LicenseApi } from './services/license-api.js';
import { MFAApi } from './services/mfa-api.js';
import { PagesApi } from './services/pages-api.js';
import { SearchApi } from './services/search-api.js';
import { SharesApi } from './services/shares-api.js';
import { SpacesApi } from './services/spaces-api.js';
import { SSOApi } from './services/sso-api.js';
import { UsersApi } from './services/users-api.js';
import { VersionApi } from './services/version-api.js';
import { WorkspaceApi } from './services/workspace-api.js';

export class DocmostClient {
  private readonly http: DocmostHttpClient;

  readonly auth: AuthApi;
  readonly users: UsersApi;
  readonly workspace: WorkspaceApi;
  readonly spaces: SpacesApi;
  readonly pages: PagesApi;
  readonly comments: CommentsApi;
  readonly attachments: AttachmentsApi;
  readonly search: SearchApi;
  readonly attachmentSearch: AttachmentSearchApi;
  readonly shares: SharesApi;
  readonly groups: GroupsApi;
  readonly export: ExportApi;
  readonly importApi: ImportApi;
  readonly fileTasks: FileTasksApi;
  readonly health: HealthApi;
  readonly version: VersionApi;
  readonly apiKeys: APIKeysApi;
  readonly mfa: MFAApi;
  readonly commentResolution: CommentResolutionApi;
  readonly license: LicenseApi;
  readonly sso: SSOApi;
  readonly ai: AIApi;
  readonly cloud: CloudApi;

  constructor(baseUrlOrOptions: string | DocmostClientOptions, legacyApiToken?: string) {
    const options: DocmostClientOptions =
      typeof baseUrlOrOptions === 'string'
        ? { baseUrl: baseUrlOrOptions, apiToken: legacyApiToken }
        : baseUrlOrOptions;

    if (
      options.apiToken &&
      (options.email !== undefined || options.password !== undefined)
    ) {
      throw new Error('Use either apiToken or email/password, not both.');
    }

    this.http = new DocmostHttpClient(options.baseUrl, {
      apiToken: options.apiToken,
      email: options.email,
      password: options.password,
      timeoutMs: options.timeoutMs,
    });

    this.auth = new AuthApi(this.http);
    this.users = new UsersApi(this.http);
    this.workspace = new WorkspaceApi(this.http);
    this.spaces = new SpacesApi(this.http);
    this.pages = new PagesApi(this.http);
    this.comments = new CommentsApi(this.http);
    this.attachments = new AttachmentsApi(this.http);
    this.search = new SearchApi(this.http);
    this.attachmentSearch = new AttachmentSearchApi(this.http);
    this.shares = new SharesApi(this.http);
    this.groups = new GroupsApi(this.http);
    this.export = new ExportApi(this.http);
    this.importApi = new ImportApi(this.http);
    this.fileTasks = new FileTasksApi(this.http);
    this.health = new HealthApi(this.http);
    this.version = new VersionApi(this.http);
    this.apiKeys = new APIKeysApi(this.http);
    this.mfa = new MFAApi(this.http);
    this.commentResolution = new CommentResolutionApi(this.http);
    this.license = new LicenseApi(this.http);
    this.sso = new SSOApi(this.http);
    this.ai = new AIApi(this.http);
    this.cloud = new CloudApi(this.http);
  }

  /**
   * Create a client and optionally log in (email/password) before use.
   */
  static async create(options: DocmostClientOptions): Promise<DocmostClient> {
    const client = new DocmostClient({ ...options, loginOnStartup: false });
    if (options.loginOnStartup !== false && options.email && options.password && !options.apiToken) {
      await client.login();
    }
    return client;
  }

  /** Authenticate with email/password (cookie session). */
  login(): Promise<void> {
    return this.http.login();
  }

  /** Clear session cookie. */
  logout(): Promise<import('./types.js').ApiResponse<unknown>> {
    return this.http.logout();
  }
}
