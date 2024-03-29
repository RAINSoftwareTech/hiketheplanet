/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { Inject, Injectable } from '@angular/core';
import { Router } from '@angular/router';

import { Subject } from 'rxjs';
import { finalize, tap } from 'rxjs/operators';

import { HtpClient } from 'lib-api-clients';

import { GISViewport, SearchOptions } from 'lib-api-clients';

type SearchType = 'geom' | 'name' | 'distance';
@Injectable({
  providedIn: 'root'
})
export class TrailheadListService {
  private trailheadResults = new Subject<any>();
  private searchLoading = new Subject<any>();

  constructor(@Inject('environment') private env: {[key: string]: any},
              private router: Router,
              private htp: HtpClient,) { }

  private _getViewPortHash(viewport: GISViewport): string {
    const coords = [viewport.southwest.lng, viewport.southwest.lat, viewport.northeast.lng, viewport.northeast.lat];
    return coords.join('');
  }

  private _getCacheKey(searchOptions: SearchOptions, searchType?: SearchType) {
    let hash = '';
    searchType = searchType ? searchType : 'geom';
    const descrip = searchType === 'name' ? searchOptions.name : searchType === 'distance' ? searchOptions.distance : '';
    if (descrip) {
      hash = descrip.toString();
    } else if (searchOptions.latitude) {
      hash = `${searchOptions.latitude}|${searchOptions.longitude}`;
    } else if (searchOptions.viewport) {
      hash = this._getViewPortHash(searchOptions.viewport);
    }
    return `hikes:${searchType}:${hash}`;
  }
  private _routeToMap() {
    if (this.router.url !== '') {
      this.router.navigate(['']);
    }
  }

  search(searchOptions: SearchOptions, searchType?: SearchType) {
    searchOptions.cacheOptions = {
      cacheKey: this._getCacheKey(searchOptions, searchType),
      cacheLatestKey: 'hikes:latest'
    };
    this.searchLoading.next(true);
    this._routeToMap();
    this.htp.get(this.env.baseUrls.search, searchOptions).pipe(
      tap(hikes => {
        if (hikes) {
          this.trailheadResults.next(hikes);
        }
      }),
      finalize(() => this.searchLoading.next(false))
    ).subscribe();
  }

  getTrailheads() {
    // TODO: check for hikes:latest cache
    // this.cache;
    return this.trailheadResults.asObservable();
  }

  getLoadingStatus() {
    return this.searchLoading.asObservable();
  }
}
