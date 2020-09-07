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

@Injectable({
  providedIn: 'root'
})
export class TrailheadListService {
  private trailheadResults = new Subject<any>();
  private searchLoading = new Subject<any>();

  constructor(private htp: HtpClient, @Inject('environment') private env, private router: Router) { }

  private _getViewPortHash(viewport): string {
    const coords = [viewport.southwest.lng, viewport.southwest.lat, viewport.northeast.lng, viewport.northeast.lat];
    return coords.join('');
  }

  private _getCacheKey(searchOptions, searchType?) {
    let hash: string;
    searchType = searchType ? searchType : 'geom';
    const descrip = searchType === 'name' ? searchOptions.name : searchType === 'distance' ? searchOptions.distance : null;
    if (descrip) {
      hash = descrip;
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

  search(searchOptions, searchType?) {
    searchOptions.cacheOptions = {
      cacheKey: this._getCacheKey(searchOptions, searchType),
      cacheLatestKey: 'hikes:latest'
    };
    this.searchLoading.next(true);
    this._routeToMap();
    this.htp.get(this.env.baseUrls.search, searchOptions).pipe(
      tap(hikes => {
        console.log(hikes, 'search results')
        if (hikes) {
          this.trailheadResults.next(hikes);
        }
      }),
      finalize(() => this.searchLoading.next(false))
    ).subscribe();
  }

  getTrailheads() {
    // TODO: check for hikes:latest cache
    return this.trailheadResults.asObservable();
  }

  getLoadingStatus() {
    return this.searchLoading.asObservable();
  }
}
