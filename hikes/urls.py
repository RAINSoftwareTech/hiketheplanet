# -*- coding: utf-8 -*-

from django.conf.urls import url
from hikes.views import (RegionDetailView, RegionListView, TrailheadDetailView,
                         HikeDetailView, TrailheadCreateView,
                         TrailheadUpdateView, HikeCreateView,
                         HikeUpdateView, HikeHomeRedirectView)

urlpatterns = [
    url(
        r'^(?P<co_region_slug>[-\w\d]+)/regions/add/$',
        TrailheadCreateView.as_view(),
        name='region_add'
        ),
    url(
        r'^(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/add/$',
        TrailheadCreateView.as_view(),
        name='trailhead_add'
        ),
    url(
        r'^(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/(?P<trailhead_slug>[-\w\d]+)/edit/$',
        TrailheadUpdateView.as_view(),
        name='trailhead_edit'
        ),
    url(
        r'^(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/(?P<trailhead_slug>[-\w\d]+)/add/$',
        HikeCreateView.as_view(),
        name='hike_add'
        ),
    url(
        r'^(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/(?P<trailhead_slug>[-\w\d]+)/'
        r'hikes/(?P<hike_slug>[-\w\d]+)/edit$',
        HikeUpdateView.as_view(),
        name='hike_edit'
        ),
    url(
        r'^(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/(?P<trailhead_slug>[-\w\d]+)/'
        r'hikes/(?P<hike_slug>[-\w\d]+)/$',
        HikeDetailView.as_view(),
        name='hike_detail'
        ),
    url(
        r'^(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/'
        r'trailheads/(?P<trailhead_slug>[-\w\d]+)/',
        TrailheadDetailView.as_view(),
        name='trailhead_detail'
        ),
    url(
        r'^(?P<co_region_slug>[-\w\d]+)/'
        r'regions/(?P<region_slug>[-\w\d]+)/',
        RegionDetailView.as_view(),
        name='region_detail'
        ),
    url(
        r'^(?P<co_region_slug>[-\w\d]+)/regions/$',
        RegionListView.as_view(template_name='hikes/regions_index.html'),
        name='region_list'
        ),
    url(
        r'^(?P<co_region_slug>[-\w\d]+)/$',
        RegionListView.as_view(),
        name='broad_region_home'
        ),
    url(
        r'^$',
        HikeHomeRedirectView.as_view(),
        name='home'
        ),
]
