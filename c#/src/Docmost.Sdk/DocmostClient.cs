using Docmost.Sdk.Http;
using Docmost.Sdk.Services;

namespace Docmost.Sdk;

/// <summary>
/// Entry point for the Docmost API. Exposes grouped API clients and handles authentication.
/// </summary>
public sealed class DocmostClient : IDisposable
{
    private readonly DocmostHttpClient _http;

    public DocmostClient(string baseUrl, string apiToken)
        : this(new DocmostClientOptions
        {
            BaseUrl = new Uri(baseUrl, UriKind.Absolute),
            ApiToken = apiToken,
        })
    {
    }

    public DocmostClient(string baseUrl, string email, string password, bool loginOnStartup = true)
        : this(new DocmostClientOptions
        {
            BaseUrl = new Uri(baseUrl, UriKind.Absolute),
            Email = email,
            Password = password,
            LoginOnStartup = loginOnStartup,
        })
    {
    }

    public DocmostClient(DocmostClientOptions options)
    {
        if (!string.IsNullOrEmpty(options.ApiToken)
            && (!string.IsNullOrEmpty(options.Email) || !string.IsNullOrEmpty(options.Password)))
        {
            throw new ArgumentException("Use either ApiToken or Email/Password, not both.", nameof(options));
        }

        if (string.IsNullOrEmpty(options.ApiToken)
            && options.LoginOnStartup
            && (string.IsNullOrEmpty(options.Email) || string.IsNullOrEmpty(options.Password)))
        {
            throw new ArgumentException(
                "Email and Password are required for cookie authentication.",
                nameof(options));
        }

        _http = new DocmostHttpClient(options);
        if (options.LoginOnStartup && !string.IsNullOrEmpty(options.Email))
            LoginAsync().GetAwaiter().GetResult();

        Auth = new AuthApi(_http);
        Users = new UsersApi(_http);
        Workspace = new WorkspaceApi(_http);
        Spaces = new SpacesApi(_http);
        Pages = new PagesApi(_http);
        Comments = new CommentsApi(_http);
        Attachments = new AttachmentsApi(_http);
        Search = new SearchApi(_http);
        AttachmentSearch = new AttachmentSearchApi(_http);
        Shares = new SharesApi(_http);
        Groups = new GroupsApi(_http);
        Export = new ExportApi(_http);
        Import = new ImportApi(_http);
        FileTasks = new FileTasksApi(_http);
        Health = new HealthApi(_http);
        Version = new VersionApi(_http);
        ApiKeys = new APIKeysApi(_http);
        Mfa = new MFAApi(_http);
        CommentResolution = new CommentResolutionApi(_http);
        License = new LicenseApi(_http);
        Sso = new SSOApi(_http);
        Ai = new AIApi(_http);
        Cloud = new CloudApi(_http);
    }

    public AuthApi Auth { get; }
    public UsersApi Users { get; }
    public WorkspaceApi Workspace { get; }
    public SpacesApi Spaces { get; }
    public PagesApi Pages { get; }
    public CommentsApi Comments { get; }
    public AttachmentsApi Attachments { get; }
    public SearchApi Search { get; }
    public AttachmentSearchApi AttachmentSearch { get; }
    public SharesApi Shares { get; }
    public GroupsApi Groups { get; }
    public ExportApi Export { get; }
    public ImportApi Import { get; }
    public FileTasksApi FileTasks { get; }
    public HealthApi Health { get; }
    public VersionApi Version { get; }
    public APIKeysApi ApiKeys { get; }
    public MFAApi Mfa { get; }
    public CommentResolutionApi CommentResolution { get; }
    public LicenseApi License { get; }
    public SSOApi Sso { get; }
    public AIApi Ai { get; }
    public CloudApi Cloud { get; }

    /// <summary>Authenticate with email/password (cookie session).</summary>
    public Task LoginAsync(CancellationToken cancellationToken = default) =>
        _http.EnsureAuthenticatedAsync(cancellationToken);

    /// <summary>Clear session cookie.</summary>
    public Task LogoutAsync(CancellationToken cancellationToken = default) =>
        _http.LogoutAsync(cancellationToken);

    public void Dispose() => _http.Dispose();
}
