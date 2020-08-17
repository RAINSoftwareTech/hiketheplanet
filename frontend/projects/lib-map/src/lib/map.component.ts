/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { Component, OnDestroy, OnInit } from '@angular/core';

import { Subscription } from 'rxjs';

import { TrailheadListService } from 'lib-hikes';

import { MapService} from './map.service';

@Component({
  selector: 'map-component',
  template: `
    <div class="map" id="map"></div>
  `,
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit, OnDestroy {
  hikeSubscription: Subscription;

  constructor(private maps: MapService, private trailheads: TrailheadListService) { }

  ngOnInit(): void {
    this.maps.initializeMap();
    this.trailheads.getTrailheads().subscribe(results => {
      this.maps.loadMapMarkers(results);
    });
  }

  ngOnDestroy(): void {
    if (this.hikeSubscription) {
      this.hikeSubscription.unsubscribe();
    }
  }

}
