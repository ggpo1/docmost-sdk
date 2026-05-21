/** Multipart request `UploadAvatarOrLogoRequest`. */
export interface UploadAvatarOrLogoRequest {
  file: Blob | Buffer | ReadableStream;
  type: string;
  spaceId?: string | null | undefined;
}
