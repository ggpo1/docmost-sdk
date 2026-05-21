/** Multipart request `FindPageCommentsRequest`. */
export interface FindPageCommentsRequest {
  pageId: string;
  limit?: number | null | undefined;
  cursor?: string | null | undefined;
}
