# -*- coding: utf-8 -*-

from geopy.geocoders import GoogleV3

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

from hikes.models import Trailhead


def trailheads_as_the_crow_flies(miles, zipcode):
    lower_range = 0
    if int(miles) > 30:
        lower_range = int(miles) - 30
    geolocator = GoogleV3()
    address, coordinates = geolocator.geocode(zipcode)
    starting_point = Point(coordinates[1], coordinates[0])
    return Trailhead.objects.filter(
        point__distance_lte=(starting_point, D(mi=miles)),
        point__distance_gte=(starting_point, D(mi=lower_range))
    ).prefetch_related('hikes').annotate(
        crow_distance=Distance('point', starting_point))
