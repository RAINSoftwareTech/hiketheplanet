/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { Inject, Injectable } from '@angular/core';

import mapboxgl from 'mapbox-gl/dist/mapbox-gl';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MapService {
  private activeMapPoint = new Subject<any>();
  private activeMapCluster = new Subject<any>();
  map: mapboxgl.Map;
  styleLink = 'mapbox://styles/mapbox/outdoors-v11';
  lat = 45.5051064;
  lng = -122.6750261;

  constructor(@Inject('environment') private env) {
    mapboxgl.accessToken = this.env.mapboxToken;
  }

  initializeMap() {
    // initialize mapbox map
    this.map = new mapboxgl.Map({
        container: 'map',
        style: this.styleLink,
        zoom: 10,
        maxZoom: 19,
        minZoom: 3,
        center: [this.lng, this.lat]
    });
    this.map.addControl(new mapboxgl.NavigationControl());

    /// locate the user
    if (navigator.geolocation) {
       navigator.geolocation.getCurrentPosition(position => {
        this.lat = position.coords.latitude;
        this.lng = position.coords.longitude;
      });
    }}

  loadMapMarkers(results) {}
}
