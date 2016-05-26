# -*- coding: utf-8 -*-

from hikes.models import Region, Trailhead, Hike


def get_hike_queryset(object):
    try:
        region = Region.objects.get(slug=object.kwargs['region_slug'])
        trailhead = Trailhead.objects.get(
            region=region, slug=object.kwargs['trailhead_slug'])
        return Hike.objects.filter(
            trailhead=trailhead).select_related('trailhead')
    except Region.DoesNotExist:
        raise ValueError('{} does not represent a saved Region. '
                         'Please check your url or add the '
                         'Region.'.format(object.kwargs['region_slug']))
    except Trailhead.DoesNotExist:
        raise ValueError('{} does not represent a saved Trailhead. '
                         'Please check your url or add the Trailhead.'
                         ''.format(object.kwargs['trailhead_slug']))


def get_trailhead_queryset(object):
        try:
            region = Region.objects.get(slug=object.kwargs['region_slug'])
            return Trailhead.objects.filter(
                region=region).prefetch_related('hikes')
        except Region.DoesNotExist:
            raise ValueError('{} does not represent a saved Region. '
                             'Please check your url or add the '
                             'Region.'.format(object.kwargs['region_slug']))
