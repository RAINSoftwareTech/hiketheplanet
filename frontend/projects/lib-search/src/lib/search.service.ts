import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

export interface AutocompleteSuggestion {
  description: string;
  source?: string;
  placeid?: string;
}
export type SearchType = 'distance' | 'name';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor() { }

  getSuggestions(search: string, searchType: SearchType, sessionToken?: string) {
    return new BehaviorSubject([]).asObservable();
  }
}
