# -*- coding: utf-8 -*-

# Imports from Django
from django.conf.urls import url

# Local imports
from .views import (
    HikeDetailAPIView,
    HikeListAPIView,
    SearchByDistance,
    SearchByHikeName,
    TrailheadDetailAPIView,
    TrailheadListAPIView,
    TrailheadMapListView,
)

app_name = 'hikes'

urlpatterns = [
    url(
        r'^country_regions/(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/(?P<trailhead_slug>[-\w\d]+)/'
        r'hikes/(?P<hike_slug>[-\w\d]+)/$',
        HikeDetailAPIView.as_view(),
        name='hike_detail'
    ),
    url(
        r'^country_regions/(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/(?P<trailhead_slug>[-\w\d]+)/'
        r'hikes/$',
        HikeListAPIView.as_view(),
        name='hike_list'
    ),
    url(
        r'^country_regions/(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/(?P<trailhead_slug>[-\w\d]+)/$',
        TrailheadDetailAPIView.as_view(),
        name='trailhead_detail'
    ),
    url(
        r'^country_regions/(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/$',
        TrailheadListAPIView.as_view(),
        name='trailhead_list'
    ),
    url(
        r'^distance/(?P<co_region_slug>[\w|\W]+)/(?P<region_slug>[\w|\W]+)/$',
        SearchByDistance.as_view(),
        name='by_distance_region'),
    url(
        r'^distance/(?P<co_region_slug>[\w|\W]+)/$',
        SearchByDistance.as_view(),
        name='by_distance_broad_region'),
    url(
        r'^distance/$',
        SearchByDistance.as_view(),
        name='by_distance'),
    url(
        r'^maps/(?P<co_region_slug>[\w|\W]+)/(?P<region_slug>[\w|\W]+)/$',
        TrailheadMapListView.as_view(),
        name='by_map'
    ),
    url(
        r'^(?P<co_region_slug>[\w|\W]+)/(?P<region_slug>[\w|\W]+)/$',
        SearchByHikeName.as_view(),
        name='by_name_region'
    ),
    url(
        r'^(?P<co_region_slug>[\w|\W]+)/$',
        SearchByHikeName.as_view(),
        name='by_name_broad_region'
    ),
    url(
        r'^$',
        SearchByHikeName.as_view(),
        name='by_name'
    ),
]
