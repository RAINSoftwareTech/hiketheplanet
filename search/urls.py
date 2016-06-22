from django.conf.urls import url
from search.views import (SearchByDistance, SearchByHikeName,
                          TrailheadMapListView)

urlpatterns = [
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
