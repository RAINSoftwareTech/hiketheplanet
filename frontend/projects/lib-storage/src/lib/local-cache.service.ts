/*
copyright (c) 2021 RAIN Software Technologies.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

Frontend caching service.
This code borrows heavily from the ckimrie RxJS observable caching gist.
https://gist.github.com/ckimrie/63334b6ad2873bd9db7ccbbf8ccdfd53
 */

import { HttpRequest } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';

import * as Localforage from 'localforage';
import { EMPTY, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { LibToolsService } from 'lib-tools';

import { LocalStorageService } from './local-storage.service';

const localforage = Localforage;
interface CacheStorageRecord {
  expires: Date;
  value: any;
}

export interface CacheOptions {
  cacheKey?: string;
  cacheLatestKey?: string;
  cacheExpires?: number | string | Date;
  cleanParams?: boolean;
  cacheAttribute?: string;
  hasCachedMeta?: true;
}

@Injectable({
  providedIn: 'root'
})
export class LocalCacheService {
  private readonly defaultExpires: number = 24 * 60 * 60; // 24 hours

  constructor(@Inject('environment') private env: {[key: string]: any},
              private localStorage: LocalStorageService,
              private tools: LibToolsService) {
    this.defaultExpires = this.env.defaultExpires ? this.env.defaultExpires : this.defaultExpires;
  }

  public put<T>(key: string, value: T, expires?: number | string | Date, nestedAttribute?: string): Observable<T> {
    const _expires = this._generateExpirationDate(expires);
    if (!this.tools.isEmpty(value, nestedAttribute)) {
      return this.localStorage.set<CacheStorageRecord>(key, {expires: _expires, value})
        .pipe(map(val => val.value));
    }
    return EMPTY;
  }

  public get<T>(key: string): Observable<T> {
    return this.localStorage.get<CacheStorageRecord>(key)
      .pipe(map(cachedVal => {
        let value = cachedVal ? cachedVal.value : null;
        if (value) {
          if (Date.now() > new Date(cachedVal.expires).getTime()) {
            this.expire(key);
            value = null;
          }
        }
        return value;
      }));
  }

  public expire(key: string): Observable<void>  {
    return this.localStorage.remove(key);
  }

  public clear(): void  {
    // Clear only 'cache' items, not all of the apps localstorage
    // this.localStorage.keys()
    //   .subscribe(keys => {
    //   for (const key of keys) {
    //     this.localStorage.get(key)
    //       .pipe(
    //         filter(value => this._isCacheStorageRecord(value as CacheStorageRecord)),
    //         take(1)
    //       )
    //       .subscribe(() => this.localStorage.remove(key))
    //   }
    // })
    localforage.iterate((value, key) => {
      if (this._isCacheStorageRecord(value as CacheStorageRecord)) {
        this.expire(key);
      }
    }).then();
  }

  public getRequestCacheOptions(req: HttpRequest<any>): CacheOptions {
    let paramOptions = req.params ? req.params.get('cacheOptions') : null;
    const bodyOptions = req.body ? req.body.cacheOptions : null;
    if (paramOptions) {
      paramOptions = JSON.parse(paramOptions);
    }
    return paramOptions ? paramOptions : bodyOptions ? bodyOptions : {};
  }

  private _isCacheStorageRecord(value: CacheStorageRecord): value is CacheStorageRecord {
    return value && (value as CacheStorageRecord).expires !== undefined;
  }

  private _expiresToDate(expires?: number | string | Date): Date {
    let expiresAsDate = new Date();
    expires = expires ? expires : this.defaultExpires;
    if (this.tools.isNumber(expires)) {
      expiresAsDate = new Date(Date.now() + Math.abs((expires as number)) * 1000);  // Now + (num secs converted to miliseconds)
    } else if (typeof expires === 'string') {
      expiresAsDate = new Date(expires);
    } else if (expires instanceof Date) {
      expiresAsDate = expires as Date;
    }
    return expiresAsDate;
  }

  private _generateExpirationDate(expires?: string | number | Date): Date {
    const expireDate: Date = this._expiresToDate(expires);

    // Dont allow expiry dates in the past
    if (expireDate.getTime() <= Date.now()) {
      throw new Error('Expires must resolve to a future datetime.');
    }

    return expireDate;
  }
}
