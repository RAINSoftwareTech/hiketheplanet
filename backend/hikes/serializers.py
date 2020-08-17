# -*- coding: utf-8 -*-
# Imports from Third Party Modules
import json
from rest_framework.serializers import ModelSerializer, SlugRelatedField

# Local imports
from .models import Hike, Trailhead


class TrailheadSerializer(ModelSerializer):

    class Meta:
        extra_kwargs = {
            'num_hikes': {'read_only': True},
            'slug': {'read_only': True}
        }
        fields = ('name', 'num_hikes', 'region', 'slug')
        model = Trailhead


class TrailheadDetailSerializer(TrailheadSerializer):
    hikes = SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta(TrailheadSerializer.Meta):
        fields = TrailheadSerializer.Meta.fields + ('latitude',
                                                    'longitude',
                                                    'hikes')


class HikeSerializer(ModelSerializer):

    class Meta:
        extra_kwargs = {
            'slug': {'read_only': True}
        }
        fields = ('name', 'difficulty_level', 'distance', 'elevation', 'slug')
        model = Hike


class HikeDetailSerializer(ModelSerializer):

    class Meta(HikeSerializer.Meta):
        fields = ('name', 'hike_type', 'description',
                  'difficulty_level', 'difficulty_level_explanation',
                  'distance', 'elevation', 'high_point')


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