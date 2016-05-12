from django.conf.urls import url
from search.views import (SearchByDistance, SearchByHikeName,
                          TrailheadMapListView)

urlpatterns = [
    url(
        r'^distance/$',
        SearchByDistance.as_view(),
        name='search_distance'),
    url(
        r'^maps/(?P<region_name>[\w|\W]+)/$',
        TrailheadMapListView.as_view(),
        name='trailheads_map'
        ),
    url(
        r'^$',
        SearchByHikeName.as_view(),
        name='search_name'
    ),
]
