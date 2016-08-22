# -*- coding: utf-8 -*-

from rest_framework.serializers import (HyperlinkedModelSerializer,
                                        HyperlinkedRelatedField,
                                        ModelSerializer,
                                        PrimaryKeyRelatedField,
                                        SlugRelatedField)

from hikes.models import CountryRegion, Region, Trailhead, Hike


class CountryRegionSerializer(ModelSerializer):

    class Meta:
        extra_kwargs = {
            'slug': {'read_only': True}
        }
        fields = ('country_abbrev', 'region_name',
                  'description', 'slug')
        model = CountryRegion


class CountryRegionDetailSerializer(CountryRegionSerializer):
    subregions = SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta(CountryRegionSerializer.Meta):
        fields = CountryRegionSerializer.Meta.fields + ('subregions',)


class RegionSerializer(ModelSerializer):

    class Meta:
        extra_kwargs = {
            'num_trailheads': {'read_only': True},
            'slug': {'read_only': True}
        }
        fields = ('name', 'num_trailheads', 'country_region', 'slug')
        model = Region


class RegionDetailSerializer(RegionSerializer):
    trailheads = SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta(RegionSerializer.Meta):
        fields = RegionSerializer.Meta.fields + ('trailheads',)


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
