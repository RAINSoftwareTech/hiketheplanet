export interface Coordinates {
  lat: number;
  lng: number;
}
export interface TrailheadHike {
  difficulty: string;
  distance: number;
  elevation: number;
  high_point: number;
  hike_type: string;
  name: string;
  slug: string;
  url: string;
}

export interface TrailheadProperty {
  distance_from: number;
  hikes: TrailheadHike[];
  locality: string;
  name: string;
  slug: string;
  url: string;
  photo_url: string;
}

export interface GeoJSONGeometry {
  type: string;
  coordinates: [number, number];
}

export interface GeoJSONFeature {
  type: string;
  id: number;
  geometry: GeoJSONGeometry;
  properties: TrailheadProperty;
}

export interface GeoJSONFeatureCollection {
  type: string;
  features: GeoJSONFeature[];
  bbox?: number[];
}

export const EmptyFeatureCollection: GeoJSONFeatureCollection = {
  type: 'FeatureCollection',
  features: []
};

export interface GISViewport {
  southwest: Coordinates;
  northeast: Coordinates;
}

export interface SearchOptions {
  session_token?: string;
  placeid?: string;
  source?: string;
  name?: string;
  location?: string;
  distance?: number;
  cacheOptions?: any;
  latitude?: number;
  longitude?: number;
  viewport?: GISViewport;
}
