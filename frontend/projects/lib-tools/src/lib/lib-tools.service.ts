/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LibToolsService {

  constructor() { }

  public isBoolean(value: any): boolean {
    return value === true || value === false;
  }

  public isNumber(value: any): boolean {
    return typeof value === 'number' && !isNaN(value);
  }

  public isEmpty(value: any, attribute?: string) {
    if (value && attribute) {
      value = value.hasOwnProperty(attribute) ? value[attribute] : null;
    }
    return value === undefined || value === null || Number.isNaN(value) ||
      (value instanceof Array && !value.length) ||
      ((value instanceof Map || value instanceof Set) && !value.size) ||
      (typeof value === 'object' && !Object.keys(value).length) ||
      (typeof value === 'string' && !value.trim().length)
  }
}
