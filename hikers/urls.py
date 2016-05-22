# -*- coding: utf-8 -*-

from django.conf.urls import url
from hikers.views import (HikerProfileView, HikerDiaryEntriesView,
                          HikerPhotosView, HikerHikesView, InactiveRedirect,
                          ProfileRedirect, ProfileIndexRedirect)

urlpatterns = [
    url(
        r'^(?P<user_slug>[-\w\d]+)/myhikes',
        HikerHikesView.as_view(),
        name='hiker_hikes'
        ),
    url(
        r'^(?P<user_slug>[-\w\d]+)/photos',
        HikerPhotosView.as_view(),
        name='hiker_photos'
        ),
    url(
        r'^(?P<user_slug>[-\w\d]+)/diaries',
        HikerDiaryEntriesView.as_view(),
        name='hiker_diaries'
        ),
    url(
        r'^invalid_profile/$',
        ProfileRedirect.as_view(),
        name='profile_redirect'
        ),
    url(
        r'^inactive/$',
        InactiveRedirect.as_view(),
        name='inactive_redirect'
        ),
    url(
        r'^(?P<user_slug>[-\w\d]+)/$',
        HikerProfileView.as_view(),
        name='hiker_profile'
        ),
    url(
        r'^',
        ProfileIndexRedirect.as_view(),
        name='index_redirect'
        ),
    ]
