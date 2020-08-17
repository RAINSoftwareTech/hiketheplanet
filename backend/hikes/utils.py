# -*- coding: utf-8 -*-
# Imports from Django
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.http import Http404

# Imports from Third Party Modules
from geopy import GoogleV3

# Local imports
from .models import Hike, Trailhead


def get_trailhead_queryset(kwargs):
    filter_params = get_filter_params_from_kwargs(kwargs, 'trailhead')
    if filter_params:
        return Trailhead.objects.filter(**filter_params
                                        ).select_related('region')
    else:
        return Trailhead.objects.all().select_related('region')


def get_trailhead_object(kwargs):
    try:
        trailheads = get_trailhead_queryset(kwargs)
        return trailheads.get(slug=kwargs['trailhead_slug'])
    except Trailhead.DoesNotExist:
        raise Http404('{} does not represent a saved Trailhead. '
                      'Please check your url or contact the site '
                      'administrator.'.format(kwargs['trailhead_slug']))
    except KeyError:
        return None


def get_hike_queryset(kwargs):
    filter_params = get_filter_params_from_kwargs(kwargs, 'hike')
    if filter_params:
        return Hike.objects.filter(**filter_params).select_related('trailhead')
    else:
        return Hike.objects.all().select_related('trailhead')


def get_hike_object(kwargs):
    try:
        hikes = get_hike_queryset(kwargs)
        return hikes.get(slug=kwargs['hike_slug'])
    except Hike.DoesNotExist:
        raise Http404('{} does not represent a saved Hike. '
                      'Please check your url or contact the site '
                      'administrator.'.format(kwargs['hike_slug']))
    except KeyError:
        return None


def get_filter_params_from_kwargs(kwargs, hikes_model):
    """Expects url kwargs from a view. Returns a dict to be used in a queryset
    filter for models from the hikes app, containing the field or field
    hierarchy and the relevant foreign key related object.
    :param kwargs: dict of key value pairs. generally view url kwargs
    :param hikes_model: string name of model from hikes app.
    :return: dict with field name or field name hierarchy as key and relevant
    object as value.
    """
    MODEL_MAP = {
        'hike': {'filter_key': 'trailhead',
                 'method': get_trailhead_object},
    }
    filter_keys = []
    filter_object = None
    while hikes_model in MODEL_MAP.keys():
        key = MODEL_MAP[hikes_model]['filter_key']
        filter_keys.append(key)
        filter_object = MODEL_MAP[hikes_model]['method'](kwargs)
        if filter_object:
            break
        else:
            hikes_model = key
    if filter_object:
        key = '__'.join(filter_keys)
        return {key: filter_object}
    else:
        return None


def trailheads_as_the_crow_flies(miles, zipcode, kwargs):
    trailheads = get_trailhead_queryset(kwargs)
    lower_range = 0
    if int(miles) > 30:
        lower_range = int(miles) - 30
    geolocator = GoogleV3()
    address, coordinates = geolocator.geocode(zipcode)
    starting_point = Point(coordinates[1], coordinates[0])
    return trailheads.filter(
        point__distance_lte=(starting_point, D(mi=miles)),
        point__distance_gte=(starting_point, D(mi=lower_range))
    ).prefetch_related('hikes').annotate(
        crow_distance=Distance('point', starting_point))
