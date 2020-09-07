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
    /// locate the user
    if (navigator.geolocation) {
       navigator.geolocation.getCurrentPosition(position => {
        this.lat = position.coords.latitude;
        this.lng = position.coords.longitude;
      });
    }
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
  }

  buildMap() {
    const map = this.map;
    const initData = {
      type: 'FeatureCollection',
      features: []
    };
    map.on('load', () => {
      map.addSource('htp', {
        type: 'geojson',
        data: initData,
        cluster: true,
        clusterRadius: 20,
        clusterMaxZoom: 12,
      //  TODO: add clusterProperties
      });
    //  TODO: add layers
    })
  }

  loadMapMarkers(featureCollection) {
    if (featureCollection && featureCollection.features.length) {
      const sourceData = this.map.getSource('htp');
      if (sourceData) {
        sourceData.setData(featureCollection);
      } else {
        this.map.on('load', () => {
          this.map.getSource('htp').setData(featureCollection)
        });
      }
    }
    this.moveMapToMarkers(featureCollection);
  }

  moveMapToMarkers(featureCollection) {
    const bbox = featureCollection.bbox;
    const first = featureCollection.features[0]
    let lng = first ? first.geometry.coordinates[0] : null;
    let lat = first ? first.geometry.coordinates[1] : null;
    if (bbox) {
      lng = (bbox[0] + bbox[2]) / 2
      lat = (bbox[1] + bbox[3]) / 2
    }
    if (lat && lng) {
      this.map.panTo([lng, lat])
    }
  }

}
