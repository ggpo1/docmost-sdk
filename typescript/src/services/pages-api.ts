/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { CreatePageDto, DeletePageDto, DuplicatePageDto, MovePageDto, MovePageToSpaceDto, PageHistoryIdDto, PageIdDto, PageInfoDto, UpdatePageDto } from '../models/index.js';


export class PagesApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getPage(request: PageInfoDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/info`, request);
  }

  async createPage(request: CreatePageDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/create`, request);
  }

  async updatePage(request: UpdatePageDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/update`, request);
  }

  async deletePage(request: DeletePageDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/delete`, request);
  }

  async restorePage(request: PageIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/restore`, request);
  }

  async getRecentPages(): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/recent`, undefined);
  }

  async getDeletedPages(): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/trash`, undefined);
  }

  async getPageHistory(): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/history`, undefined);
  }

  async getPageHistoryInfo(request: PageHistoryIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/history/info`, request);
  }

  async getSidebarPages(): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/sidebar-pages`, undefined);
  }

  async movePageToSpace(request: MovePageToSpaceDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/move-to-space`, request);
  }

  async duplicatePage(request: DuplicatePageDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/duplicate`, request);
  }

  async movePage(request: MovePageDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/move`, request);
  }

  async getPageBreadcrumbs(request: PageIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/breadcrumbs`, request);
  }

}
