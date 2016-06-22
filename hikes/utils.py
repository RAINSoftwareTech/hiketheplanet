# -*- coding: utf-8 -*-

from django.http import Http404

from hikes.models import CountryRegion, Region, Trailhead, Hike


def get_country_region_object(kwargs):
    try:
        return CountryRegion.objects.get(slug=kwargs['co_region_slug'])
    except CountryRegion.DoesNotExist:
        raise Http404('{} does not represent a saved Country Region. '
                      'Please check your url or contact the site '
                      'administrator.'.format(kwargs['co_region_slug']))
    except KeyError:
        return None


def get_region_queryset(kwargs):
    filter_params = get_filter_params_from_kwargs(kwargs, 'region')
    if filter_params:
        return Region.objects.filter(
            **filter_params).select_related(
            'country_region').prefetch_related('trailheads')
    else:
        return Region.objects.all().select_related(
            'country_region').prefetch_related('trailheads')


def get_region_object(kwargs):
    try:
        regions = get_region_queryset(kwargs)
        return regions.get(slug=kwargs['region_slug'])
    except Region.DoesNotExist:
        raise Http404('{} does not represent a saved Region. '
                      'Please check your url or contact the site '
                      'administrator.'.format(kwargs['region_slug']))
    except KeyError:
        return None


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
         'trailhead': {'filter_key': 'region',
                       'method': get_region_object},
         'region': {'filter_key': 'country_region',
                    'method': get_country_region_object}
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
