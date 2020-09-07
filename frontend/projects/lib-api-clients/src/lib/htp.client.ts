/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { HttpClient, HttpErrorResponse, HttpHeaders, HttpParams } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';

import { EMPTY, Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';

interface RequestPayload {
      body?: any;
      headers?: HttpHeaders | {
          [header: string]: string | string[];
      };
      params?: HttpParams | {
          [param: string]: string | string[];
      };
      reportProgress?: boolean;
      responseType?: 'arraybuffer' | 'blob' | 'json' | 'text';
      withCredentials?: boolean;
      observe?: string;
}

export interface BaseUrls {
  location_autocomplete: string;
  name_autocomplete: string;
  search: string;
}

@Injectable({
  providedIn: 'root'
})
export class HtpClient {

  constructor(private http: HttpClient,
              // private errors: HttpErrorService,
              @Inject('environment') private env) { }

  private _constructUrl(urlPath: string): string {
      let url = this.env.baseAPIURL;
      url = url.trim();
      if (urlPath) {
          if (urlPath.startsWith('http')) {
              url = urlPath.trim();
          } else {
              urlPath = urlPath.trim();
              if (!url.endsWith('/')) {
                  url = url.concat('/');
              }
              if (urlPath.startsWith('/')) {
                  urlPath = urlPath.substr(1);
              }
              url = url.concat(urlPath);
          }
      }
      return url;
  }

  private _construct_payload(body?: object, queryParams?: object): RequestPayload {
      const payload: RequestPayload = {
          responseType: 'json'
      };
      if (body) {
          payload.body = body;
      }
      if (queryParams) {
          let httpParams = new HttpParams();
          Object.keys(queryParams).forEach(key => {
              httpParams = httpParams.append(key, queryParams[key]);
          });
          payload.params = httpParams;
      }
      return payload;
  }

  private _callHTP<T>(method: string, urlPath: string, payload: object,
                      errorHandler?: (errorResponse: HttpErrorResponse) => Observable<never> | null): Observable<T> {
    const url = this._constructUrl(urlPath);

    function tempErrorHandler() {
        return EMPTY;
    }
    if (!errorHandler) {
      errorHandler = tempErrorHandler;
    // errorHandler = this.errors.handleError;
    }
    return this.http
        .request<T>(method, url, payload)
        .pipe(catchError(errorHandler));
  }

  get<T>(urlPath: string, queryParams?: {}, errorHandler?): Observable<T> {
    const payload = this._construct_payload(null, queryParams);
    return this._callHTP<T>('GET', urlPath, payload, errorHandler);
  }

}
