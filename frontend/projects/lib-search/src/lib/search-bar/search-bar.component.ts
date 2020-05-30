/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';

import { Observable, Subscription } from 'rxjs';
import { debounceTime, switchMap } from 'rxjs/operators';
import * as uuid from 'uuid';

import { AutocompleteSuggestion, SearchService, SearchType } from '../search.service';

@Component({
  selector: 'search-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit, OnDestroy {
  searchForm: FormGroup;
  sessionToken = uuid.v4();
  addrSuggestions$: Observable<AutocompleteSuggestion[]>;
  searchSubscription: Subscription;
  placeholderText: string;
  distancePlaceholder = 'address, neighborhood, city, or ZIP code';

  searchTypes = [
    {name: 'distance', displayName: 'Distance'},
    {name: 'name', displayName: 'Hike name'}
  ];

  distanceOptions = [
    {name: 5, displayName: '5 miles'},
    {name: 10, displayName: '10 miles'},
    {name: 25, displayName: '25 miles'},
    {name: 50, displayName: '50 miles'},
  ];

  constructor(private search: SearchService, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.placeholderText = this.distancePlaceholder;
    this.searchForm = this.formBuilder.group({
      searchControl: [''],
      searchType: ['distance'],
      distance: [25],
    });

    this.addrSuggestions$ = this.searchForm
        .get('searchControl')
        .valueChanges
        .pipe(
          debounceTime(300),
          switchMap(value => this.populateAutoComplete(value, this.sessionToken))
        );

    this.searchForm.get('searchType').valueChanges.subscribe(value => {
      if (value === 'distance') {
        this.placeholderText = this.distancePlaceholder;
      } else {
        this.placeholderText = 'hike or trailhead name';
      }
    });

    this.searchForm.get('distance').valueChanges.subscribe(() => {
      this.onSearch();
    })
  }

  populateAutoComplete(search: string, sessionToken: string) {
    search = search ? search : '';
    return this.search.getSuggestions(search, this.searchForm.get('searchType').value, sessionToken);
  }

  ngOnDestroy(): void {
    if (this.searchSubscription) {
      this.searchSubscription.unsubscribe();
    }
  }

  displayFn(suggestion: AutocompleteSuggestion) {
      if (suggestion) { return suggestion.description; }
  }

  onSearch() {
    console.log('search')
  }

}
