# -*- coding: utf-8 -*-

from django.conf.urls import url
from hikes.views import (RegionDetailView, RegionListView, TrailheadDetailView,
                         HikeDetailView)

urlpatterns = [
    url(
        r'^regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/(?P<trailhead_slug>[-\w\d]+)/'
        r'hikes/(?P<hike_slug>[-\w\d]+)/$',
        HikeDetailView.as_view(),
        name='hike'
        ),
    url(
        r'^regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/(?P<trailhead_slug>[-\w\d]+)/$',
        TrailheadDetailView.as_view(),
        name='trailhead'
        ),
    url(
        r'^regions/(?P<region_slug>[-\w\d]+)/$',
        RegionDetailView.as_view(),
        name='region'
        ),
    url(
        r'^$',
        RegionListView.as_view(),
        name='region_list'
        ),
]
