
from django.contrib.gis.geos import Point, Polygon
import googlemaps
from pyproj import Geod

from django.conf import settings
from core.exceptions import BadRequest
from .models import Hike, Trailhead
RADIUS_MI = 50
COUNTRIES = {'country': 'us'}
def _google_find_place(text):
    if text:
        g_attribs = ['place_id']
        gmaps = googlemaps.Client(settings.GMAPS_API_KEY)
        resp = gmaps.find_place(text, 'textquery', g_attribs)
        if resp['status'] == 'OK':
            return resp['candidates'][0]['place_id']
        else:
            raise BadRequest('Invalid search parameters')


def _get_google_detail(place_id, sessiontoken=None):
    g_attribs = ['types', 'geometry']
    gmaps = googlemaps.Client(settings.GMAPS_API_KEY)
    resp = gmaps.place(place_id, sessiontoken)
    if resp['status'] == 'OK':
        return {key: resp['result'][key] for key in g_attribs}


def _get_bbox_from_center(lat, lon, distance=None):
    distance = distance or 1.5
    distance_m = distance * 1609.34
    g = Geod(ellps='WGS84')
    max_lon = g.fwd(lon, lat, 45, distance_m)[0]
    max_lat = g.fwd(lon, lat, 135, distance_m)[1]
    min_lon = g.fwd(lon, lat, 225, distance_m)[0]
    min_lat = g.fwd(lon, lat, 315, distance_m)[1]
    return max_lon, max_lat, min_lon, min_lat


def _get_center_from_bbox(bbox):
    p = Polygon.from_bbox(bbox)
    return p.centroid.coords


def search_params(location, placeid=None, sessiontoken=None, viewport=None,
                  latitude=None, longitude=None, miles=None, **kwargs):
    miles = int(miles) if miles else 10
    detail = {}
    bbox = None
    search_geom = None
    if not placeid and not viewport and not (latitude and longitude):
        placeid = _google_find_place(location)
    if placeid and not viewport and not (latitude and longitude):
        detail = _get_google_detail(placeid, sessiontoken)

    if detail and not viewport:
        viewport = detail['geometry']['viewport']
    if detail and (not latitude or not longitude):
        latitude = detail['geometry']['location']['lat']
        longitude = detail['geometry']['location']['lng']
    if latitude and longitude:
        bbox = _get_bbox_from_center(latitude, longitude, miles)
        search_geom = Polygon.from_bbox(bbox)
    elif viewport:
        bbox = [
            viewport[key][axis]
            for key in ['southwest', 'northeast']
            for axis in ['lng', 'lat']
        ]
        search_geom = Polygon.from_bbox(bbox)
        if not latitude or not longitude:
            longitude, latitude = _get_center_from_bbox(bbox)
    return search_geom, bbox, Point(longitude, latitude, srid=4326)


def hike_name_autocomplete(text):
    names = []
    if text and len(text) > 3:
        hikes = Hike.objects.filter(
            name__icontains=text
        ).only('name').values_list('name', flat=True)
        t_heads = Trailhead.objects.filter(
            name__icontains=text
        ).only('name').values_list('name', flat=True)
        names = list(hikes[:5])
        t_count = 8 - len(names)
        names = names + list(t_heads[:t_count])
        names = list(set(names))
        names.sort()
    return [{'description': name} for name in names]


def google_autocomplete(search_text, session_token, *args, **kwargs):
    gmaps = googlemaps.Client(settings.GMAPS_API_KEY)
    location = kwargs.get('location')
    options = {
        'location': kwargs.get('location'),
        'radius': RADIUS_MI * 1609.34 if location else None,
        'components': COUNTRIES,
    }
    options = {k: v for k, v in options.items() if v}
    try:
        rsp = gmaps.places_autocomplete(search_text, session_token, **options)
    except googlemaps.exceptions.ApiError as err:
        rsp = []
    suggestions = [
        {
            'description': r['description'],
            'placeid': r['place_id'],
            'source': 'google'
        }
        for r in rsp
    ]
    return suggestions