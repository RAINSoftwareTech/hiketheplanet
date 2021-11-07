import { HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { LibToolsService } from 'lib-tools';

export interface RequestOptions {
  body?: any;
  headers?: HttpHeaders | {
      [header: string]: string | string[];
  };
  observe?: 'body' | 'events' | 'response';
  params?: HttpParams | {
      [param: string]: string | string[];
  };
  responseType?: 'arraybuffer' | 'blob' | 'json' | 'text';
  reportProgress?: boolean;
  withCredentials?: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class ApiToolsService {

  constructor(private tools: LibToolsService) { }

  constructHeaders(contentType?: string): HttpHeaders | undefined {
    const headers: { [key: string]: any } = {};
    if (contentType !== 'NONE') {
      if (!contentType) {
        contentType = 'application/json';
      }
      headers['Content-Type'] = contentType;
    }
    return Object.keys(headers).length ? new HttpHeaders(headers) : undefined;
  }

  constructQueryParams(params: { [key: string]: any }): HttpParams | undefined {
    let httpParams = new HttpParams();
    for (let [key, val] of Object.entries(params)) {
      if (!this.tools.isEmpty(val)) {
        if (val instanceof Date) {
          val = (val as Date).toISOString();
        } else if (typeof val === 'object') {
          val = JSON.stringify(val);
        }
        httpParams = httpParams.append(key, val);
      }
    }
    return httpParams.keys().length ? httpParams : undefined;
  }

  constructUrl(baseUrl: string, urlPath?: string): string {
    baseUrl = baseUrl.trim();
    urlPath = urlPath ? urlPath.trim() : urlPath;
    let url: URL;
    try {
      url = new URL(baseUrl);
    }
    catch (err) {
      url = new URL(`https://${baseUrl}`);
    }
    if (urlPath) {
      url = new URL(urlPath, url);
    }
    return url.href.endsWith('/') ? url.href : url.href.concat('/');
  }

  constructBody(body: { [key: string]: any }, filePost = false): { [key: string]: any } | undefined {
    let payloadBody;
    if (!this.tools.isEmpty(body)) {
      if (filePost) {
        const fd = new FormData();
        for (const [key, val] of Object.entries(body)) {
          fd.append(key, val);
        }
        payloadBody = fd;
      } else {
        payloadBody = body;
      }
    }
    return payloadBody;
  }

  constructPayload(body?: { [key: string]: any }, queryParams?: { [key: string]: any },
                   contentType?: string, filePost = false): RequestOptions {
    const payload: RequestOptions = {
      responseType: 'json',
    };
    const headers = this.constructHeaders(contentType);
    const params = !!queryParams ? this.constructQueryParams(queryParams) : undefined;
    body = !!body ? this.constructBody(body, filePost) : undefined;
    if (headers) {
      payload.headers = headers;
    }
    if (params) {
      payload.params = params;
    }
    if (body) {
      payload.body = body;
    }
    return payload;
  }

  constructFilePayload(method = 'GET', body?: any, queryParams?: { [key: string]: any },
                       contentType?: string, buffer = false): RequestOptions {
    const getRequest = method === 'GET';
    contentType = !getRequest ? 'NONE' : contentType;
    const payload = this.constructPayload(body, queryParams, contentType, !getRequest);
    payload.responseType = buffer === true ? 'arraybuffer' : getRequest ? 'blob' : 'json';
    payload.reportProgress = true;
    payload.observe = 'events';
    return payload;
  }

}
