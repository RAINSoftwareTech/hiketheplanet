# -*- coding: utf-8 -*-

from django.conf.urls import url
from hikes.api.views import (CountryRegionDetailAPIView,
                             CountryRegionListAPIView,
                             RegionListAPIView,
                             RegionDetailAPIView,
                             TrailheadListAPIView,
                             TrailheadDetailAPIView,
                             HikeListAPIView,
                             HikeDetailAPIView)

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
        r'^country_regions/(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/$',
        RegionDetailAPIView.as_view(),
        name='region_detail'
        ),
    url(
        r'^country_regions/(?P<co_region_slug>[-\w\d]+)/'
        r'regions/$',
        RegionListAPIView.as_view(),
        name='region_list'
        ),
    url(
        r'^country_regions/(?P<co_region_slug>[-\w\d]+)/$',
        CountryRegionDetailAPIView.as_view(),
        name='country_regions_detail'
        ),
    url(
        r'^country_regions/$',
        CountryRegionListAPIView.as_view(),
        name='country_regions_list'
        ),
]
