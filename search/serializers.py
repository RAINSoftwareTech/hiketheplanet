# -*- coding: utf-8 -*-

import json
from django.core.urlresolvers import reverse_lazy
from hikes.models import Hike


def trailheads_serializer(trailheads):
    trailheads_list = []
    for trailhead in trailheads:
        trailhead_details = {
            'trailhead': trailhead.name,
            'lat': trailhead.latitude,
            'lon': trailhead.longitude,
            'num_hikes': trailhead.num_hikes,
            'url': str(trailhead_url(trailhead))
        }
        trailheads_list.append(trailhead_details)
    return json.dumps(trailheads_list)


def trailhead_url(trailhead):
    url = reverse_lazy(
            'hikes:trailhead_detail',
            kwargs={'trailhead_slug': trailhead.slug,
                    'region_slug': trailhead.region.slug})
    if trailhead.num_hikes == 1:
        try:
            hike = Hike.objects.get(trailhead=trailhead)
            url = reverse_lazy(
                'hikes:hike_detail',
                kwargs={'hike_slug': hike.slug,
                        'trailhead_slug': trailhead.slug,
                        'region_slug': trailhead.region.slug})
        except Hike.DoesNotExist:
            pass
        except Hike.MultipleObjectsReturned:
            hike_count = Hike.objects.filter(trailhead=trailhead).count()
            trailhead.num_hikes = hike_count
            trailhead.save()
    return url


def hikes_serializer(hikes):
    hike_list = []
    for hike in hikes:
        hike_dict = {
            'hike': hike.name,
            'distance': hike.distance,
            'difficulty': hike.get_difficulty_level_display(),
            'hikeUrl': str(hike_url(hike))
        }
        try:
            hike_dict['driving_distance'] = '{0:.2f}'.format(
                hike.trailhead.crow_distance.mi)
        except AttributeError:
            pass
        hike_list.append(hike_dict)
    return json.dumps(hike_list)


def hike_url(hike):
    return reverse_lazy('hikes:hike_detail',
                        kwargs={'hike_slug': hike.slug,
                                'trailhead_slug': hike.trailhead.slug,
                                'region_slug': hike.trailhead.region.slug})
