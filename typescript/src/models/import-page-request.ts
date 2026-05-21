/** Multipart request `ImportPageRequest`. */
export interface ImportPageRequest {
  file: Blob | Buffer | ReadableStream;
  spaceId: string;
  parentPageId?: string | null | undefined;
}
