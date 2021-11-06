/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';

import { EMPTY, Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { ApiToolsService } from './api-tools.service';

export interface BaseUrls {
  location_autocomplete: string;
  name_autocomplete: string;
  search: string;
}

@Injectable({
  providedIn: 'root'
})
export class HtpClient {
  baseUrl: string;

  constructor(@Inject('environment') private env,
              // private errors: HttpErrorService,
              private http: HttpClient,
              private apiTools: ApiToolsService) {
    this.baseUrl = this.env.baseAPIURL;
  }

  private _callHTP<T>(method: string, urlPath: string, payload: object,
                      errorHandler?: (errorResponse: HttpErrorResponse) => Observable<never> | null): Observable<T> {
    const url = this.apiTools.constructUrl(this.baseUrl, urlPath);

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
    const payload = this.apiTools.constructPayload(null, queryParams);
    return this._callHTP<T>('GET', urlPath, payload, errorHandler);
  }

}
