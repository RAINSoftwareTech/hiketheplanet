import { Component, Input, OnDestroy, OnInit } from '@angular/core';

import { PageEvent } from '@angular/material/paginator';

import { Subscription } from 'rxjs';

import { EmptyFeatureCollection, GeoJSONFeature, GeoJSONFeatureCollection } from '../hikes.interface';
import { TrailheadListService } from '../trailhead-list.service';

@Component({
  selector: 'hikes-trailhead-list',
  templateUrl: './trailhead-list.component.html',
  styleUrls: ['./trailhead-list.component.css']
})
export class TrailheadListComponent implements OnInit, OnDestroy {
  @Input() mobileView = false;
  searchSubscription: Subscription;

  pageSize = 20;
  featureCollection: GeoJSONFeatureCollection = EmptyFeatureCollection;
  pagedTrailheads: GeoJSONFeature[] = [];
  pageEvent: PageEvent;

  constructor(private trailheads: TrailheadListService) { }

  ngOnInit() {
    this.searchSubscription = this.trailheads.getTrailheads().subscribe(trailheadCollection => {
      this.featureCollection = trailheadCollection;
      if (this.featureCollection && this.featureCollection.features.length) {
        this.pagedTrailheads = this.getPagedTrailheads(0);
      }
    });
  }

  getPagedTrailheads(pageIndex: number): GeoJSONFeature[] {
    const end = (pageIndex + 1) * this.pageSize;
    const start = pageIndex * this.pageSize;
    return this.featureCollection.features.slice(start, end);
  }

  ngOnDestroy() {
    if (this.searchSubscription) {
      this.searchSubscription.unsubscribe();
    }
  }

}
