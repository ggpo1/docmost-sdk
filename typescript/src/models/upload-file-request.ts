/** Multipart request `UploadFileRequest`. */
export interface UploadFileRequest {
  file: Blob | Buffer | ReadableStream;
  pageId: string;
  attachmentId?: string | null | undefined;
}
