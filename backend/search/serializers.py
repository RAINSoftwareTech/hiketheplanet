# -*- coding: utf-8 -*-

import json
from hikes.models import Hike


def trailheads_serializer(trailheads):
    trailheads_list = []
    for trailhead in trailheads:
        trailhead_details = {
            'trailhead': trailhead.name,
            'lat': trailhead.latitude,
            'lon': trailhead.longitude,
            'num_hikes': trailhead.num_hikes,
            'url': str(trailhead_or_hike_url(trailhead))
        }
        trailheads_list.append(trailhead_details)
    return json.dumps(trailheads_list)


def trailhead_or_hike_url(trailhead):
    url = trailhead.get_absolute_url()
    if trailhead.num_hikes == 1:
        try:
            hike = Hike.objects.get(trailhead=trailhead)
            url = hike.get_absolute_url()
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
            'hikeUrl': str(hike.get_absolute_url())
        }
        try:
            hike_dict['driving_distance'] = '{0:.2f}'.format(
                hike.trailhead.crow_distance.mi)
        except AttributeError:
            pass
        hike_list.append(hike_dict)
    return json.dumps(hike_list)
