/*
copyright (c) 2021 RAIN Software Technologies.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

Local storage service that leverages localforage so that complete objects may be
stored, rather than only strings or JSON.stringify-ed objects.
*/

import { Injectable } from '@angular/core';

import * as Localforage from 'localforage';
import { from, Observable } from 'rxjs';

const localforage = Localforage;

@Injectable({
  providedIn: 'root'
})
export class LocalStorageService {

  constructor() { }

  set(key: string, value: any): Observable<any> {
    if (value !== null && value !== undefined) {
      return from(localforage.setItem(key, value));
    }
  }

  get(key: string): Observable<any> {
    return from(localforage.getItem(key));
  }

  remove(key: string): Observable<void> {
    return from(localforage.removeItem(key));
  }

  clear(): Observable<void> {
    return from(localforage.clear());
  }

  has(key: string): boolean {
    localforage.keys()
      .then(keys => {
        return keys && keys.includes(key);
      });
    return false;
  }
}
