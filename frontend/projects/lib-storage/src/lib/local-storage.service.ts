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

  public set<T>(key: string, value: T): Observable<T> {
    if (value !== null && value !== undefined) {
      return from(localforage.setItem(key, value));
    }
  }

  public get<T>(key: string): Observable<T> {
    return (from(localforage.getItem(key)) as Observable<T>);
  }

  public remove(key: string): Observable<void> {
    return from(localforage.removeItem(key));
  }

  public clear(): Observable<void> {
    return from(localforage.clear());
  }

  public has(key: string): boolean {
    localforage.keys()
      .then(keys => {
        return keys && keys.includes(key);
      });
    return false;
  }

  public keys(): Observable<string[]> {
    return from(localforage.keys());
  }
}
