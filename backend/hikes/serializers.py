# -*- coding: utf-8 -*-
# Imports from Third Party Modules
import json
from collections import OrderedDict
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoFeatureModelListSerializer
# Local imports
from .models import Hike, Trailhead


class BBoxGeoFeatureModelListSerializer(GeoFeatureModelListSerializer):

    def to_representation(self, data):
        """
        Add GeoJSON compatible formatting to a serialized queryset list
        """
        request = self.context.get('request')
        return OrderedDict((
            ("type", "FeatureCollection"),
            ("features", super().to_representation(data)),
            ("bbox", getattr(request, 'bbox', None))
        ))


class HikeSerializer(serializers.ModelSerializer):
    hike_type = serializers.CharField(source='get_hike_type_display')
    difficulty = serializers.CharField(source='get_difficulty_level_display')
    url = serializers.HyperlinkedIdentityField(
        view_name='hikes:hike-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Hike
        fields = (
            'name', 'distance', 'hike_type', 'difficulty',
            'elevation', 'high_point', 'slug', 'url'
        )


class TrailheadGeoSerializer(GeoFeatureModelSerializer):
    locality = serializers.StringRelatedField(
        source='state_province', read_only=True
    )
    hikes = HikeSerializer(many=True, read_only=True)
    distance_from = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name='hikes:trailhead-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Trailhead
        geo_field = 'point'
        fields = (
            'id', 'name', 'locality', 'slug', 'url', 'distance_from', 'hikes'
        )
        list_serializer_class = BBoxGeoFeatureModelListSerializer

    def get_distance_from(self, obj):
        dist = getattr(obj, 'distance_from', None)
        return dist.mi if dist else None
