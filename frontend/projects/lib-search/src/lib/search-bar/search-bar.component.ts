/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

import { Observable } from 'rxjs';
import { debounceTime, filter, switchMap } from 'rxjs/operators';
import { v4 as uuidv4 } from 'uuid';

import { TrailheadListService } from 'lib-hikes';

import { AutocompleteService, AutocompleteSuggestion } from '../autocomplete.service';

@Component({
  selector: 'search-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit {
  searchForm: FormGroup;
  sessionToken = uuidv4();
  autoSuggestions$: Observable<AutocompleteSuggestion[]>;
  placeholderText: string;
  distancePlaceholder = 'address, neighborhood, city, or ZIP code';

  searchTypes = [
    {name: 'name', displayName: 'Hike name'},
    {name: 'distance', displayName: 'Distance'},
  ];

  distanceOptions = [
    {name: 5, displayName: '5 miles'},
    {name: 10, displayName: '10 miles'},
    {name: 25, displayName: '25 miles'},
    {name: 50, displayName: '50 miles'},
  ];

  constructor(private autocomplete: AutocompleteService,
              private formBuilder: FormBuilder,
              private trailheads: TrailheadListService) { }

  ngOnInit() {
    this.placeholderText = this.distancePlaceholder;
    this.searchForm = this.formBuilder.group({
      searchControl: [''],
      searchType: ['distance'],
      distance: [25],
    });

    this.autoSuggestions$ = this.searchForm
        .get('searchControl')
        .valueChanges
        .pipe(
          filter(value => {
            return typeof value === 'string' && value.length > 2;
          }),
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
    return this.autocomplete.getSuggestions(search, this.searchForm.get('searchType').value, sessionToken);
  }

  displayFn(suggestion: AutocompleteSuggestion) {
      if (suggestion) { return suggestion.description; }
  }

  onSearch() {
    const searchType = this.searchForm.get('searchType').value;
    const searchCtrl = this.searchForm.get('searchControl').value;
    const searchText = typeof searchCtrl === 'string' ? searchCtrl : searchCtrl.description;
    const searchOptions: any = {
      session_token: this.sessionToken,
      placeid: typeof searchCtrl === 'string' ? null : searchCtrl.placeid ? searchCtrl.placeid : null,
      source:typeof searchCtrl === 'string' ? 'user' : searchCtrl.source ? searchCtrl.source : null,
    }
    if (searchType === 'name') {
      searchOptions.name = searchText;
    } else {
      searchOptions.location = searchText;
      searchOptions.miles = this.searchForm.get('distance').value;
    }
    this.trailheads.search(searchOptions, searchType)
    this.sessionToken = uuidv4();
  }

}
