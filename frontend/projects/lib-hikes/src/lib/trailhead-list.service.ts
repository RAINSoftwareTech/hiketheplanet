/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { Injectable } from '@angular/core';

import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TrailheadListService {
  private trailheadResults = new Subject<any>();

  constructor() { }

  getTrailheads() {
    return this.trailheadResults.asObservable();
  }
}
