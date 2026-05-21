/** Multipart request `ImportZipRequest`. */
export interface ImportZipRequest {
  file: Blob | Buffer | ReadableStream;
  spaceId: string;
  source: string;
  parentPageId?: string | null | undefined;
}
