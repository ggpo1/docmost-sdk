/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { RemoveIconDto, UploadAvatarOrLogoRequest, UploadFileRequest } from '../models/index.js';


export class AttachmentsApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async uploadFile(request: UploadFileRequest): Promise<ApiResponse<unknown>> {
    return this.http.postMultipart(`files/upload`, request as unknown as Record<string, unknown>);
  }

  async getFile(fileId: string, fileName: string): Promise<Response> {
    return this.http.getRaw(`files/${encodeURIComponent(fileId)}/${encodeURIComponent(fileName)}`);
  }

  async getPublicFile(fileId: string, fileName: string, jwt?: string): Promise<Response> {
    const path = `files/public/${encodeURIComponent(fileId)}/${encodeURIComponent(fileName)}`;
    const params: Record<string, string> = {};
    if (jwt !== undefined) params['jwt'] = jwt;
    return this.http.getRaw(path, Object.keys(params).length ? params : undefined);
  }

  async uploadAvatarOrLogo(request: UploadAvatarOrLogoRequest): Promise<ApiResponse<unknown>> {
    return this.http.postMultipart(`attachments/upload-image`, request as unknown as Record<string, unknown>);
  }

  async getLogoOrAvatar(attachmentType: string, fileName: string): Promise<Response> {
    return this.http.getRaw(`attachments/img/${encodeURIComponent(attachmentType)}/${encodeURIComponent(fileName)}`);
  }

  async removeIcon(request: RemoveIconDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`attachments/remove-icon`, request);
  }

}
