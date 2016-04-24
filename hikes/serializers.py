# -*- coding: utf-8 -*-

import json
from django.core.urlresolvers import reverse_lazy
from hikes.models import Hike


def trailheads_map_serializer(trailheads, region):
        trailheads_list = []
        for trailhead in trailheads:
            trailhead_details = {
                'trailhead': trailhead.name,
                'lat': trailhead.latitude,
                'lon': trailhead.longitude,
                'num_hikes': trailhead.num_hikes,
                'url': str(trailhead_url(trailhead, region))
            }
            trailheads_list.append(trailhead_details)
        return json.dumps({
            "success": 1,
            "result": trailheads_list
        })


def trailhead_url(trailhead, region):
    url = reverse_lazy(
            'hikes:trailhead',
            kwargs={'trailhead_slug': trailhead.slug,
                    'region_slug': region.slug})
    if trailhead.num_hikes == 1:
        try:
            hike = Hike.objects.get(trailhead=trailhead)
            url = reverse_lazy(
                'hikes:hike',
                kwargs={'hike_slug': hike.slug,
                        'trailhead_slug': trailhead.slug,
                        'region_slug': region.slug})
        except Hike.DoesNotExist:
            pass
        except Hike.MultipleObjectsReturned:
            hike_count = Hike.objects.filter(trailhead=trailhead).count()
            trailhead.num_hikes = hike_count
            trailhead.save()
    return url
