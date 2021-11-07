/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';

import { EMPTY, Observable, ObservableInput } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { ApiToolsService } from './api-tools.service';

export interface BaseUrls {
  location_autocomplete: string;
  name_autocomplete: string;
  search: string;
}
export type ErrorHandler = (err: any, caught: Observable<any>) => ObservableInput<any>;
@Injectable({
  providedIn: 'root'
})
export class HtpClient {
  baseUrl: string;

  constructor(@Inject('environment') private env: {[key: string]: any},
              // private errors: HttpErrorService,
              private http: HttpClient,
              private apiTools: ApiToolsService) {
    this.baseUrl = this.env.baseAPIURL;
  }

  private _callHTP<T>(method: string, urlPath: string, payload: object,
                      errorHandler?: ErrorHandler): Observable<T> {
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

  get<T>(urlPath: string, queryParams?: {}, errorHandler?: ErrorHandler): Observable<T> {
    const payload = this.apiTools.constructPayload(undefined, queryParams);
    return this._callHTP<T>('GET', urlPath, payload, errorHandler);
  }

}
