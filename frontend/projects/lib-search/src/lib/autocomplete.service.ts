import { Inject, Injectable } from '@angular/core';

import { EMPTY, Observable } from 'rxjs';

import { HtpClient } from 'lib-api-clients';

export interface AutocompleteSuggestion {
  description: string;
  source?: string;
  placeid?: string;
}
export type SearchType = 'distance' | 'name';

@Injectable({
  providedIn: 'root'
})
export class AutocompleteService {
  userLocation?: number[];

  constructor(private htp: HtpClient, @Inject('environment') private env: {[key: string]: any}) {
  /// locate the user
  if (navigator.geolocation) {
     navigator.geolocation.getCurrentPosition(position => {
       this.userLocation = [position.coords.latitude, position.coords.longitude];
     });
  } }

  getSuggestions(search: string, searchType: SearchType, sessionToken?: string): Observable<AutocompleteSuggestion[]> {
    function errorHandler() {
        return EMPTY;
    }
    const cacheOptions = {cacheKey: `autocomplete:${searchType}:${search}`};
    const url = searchType === 'name' ? this.env.baseUrls.name_autocomplete : this.env.baseUrls.location_autocomplete;
    const searchParams = {
      location: this.userLocation,
      cacheOptions,
      session_token: sessionToken,
      search_text: search
    };
    return this.htp.get<AutocompleteSuggestion[]>(url, searchParams, errorHandler);
  }
}
