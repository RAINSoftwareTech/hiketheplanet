# -*- coding: utf-8 -*-

from django.conf.urls import url
from hikers.views import (HikerProfileView, HikerBasicInfoUpdateView,
                          HikerStatsUpdateView, HikerAddressUpdateView,
                          HikerDiaryEntriesView, HikerDairyEntryCreateView,
                          HikerPhotosView, HikerPhotosCreateView,
                          HikerHikesView, InactiveRedirect,
                          ProfileRedirect, ProfileIndexRedirect,
                          PermissionDeniedRedirect)

urlpatterns = [
    url(
        r'^(?P<user_slug>[-\w\d]+)/myhikes',
        HikerHikesView.as_view(),
        name='hiker_hikes'
        ),
    url(
        r'^(?P<user_slug>[-\w\d]+)/photos/new/$',
        HikerPhotosCreateView.as_view(),
        name='hiker_photos_new'
        ),
    url(
        r'^(?P<user_slug>[-\w\d]+)/photos/?$',
        HikerPhotosView.as_view(),
        name='hiker_photos'
        ),
    url(
        r'^(?P<user_slug>[-\w\d]+)/diaries/new/$',
        HikerDairyEntryCreateView.as_view(),
        name='hiker_diaries_new'
        ),
    url(
        r'^(?P<user_slug>[-\w\d]+)/diaries/?$',
        HikerDiaryEntriesView.as_view(),
        name='hiker_diaries'
        ),
    url(
        r'^invalid_profile/$',
        ProfileRedirect.as_view(),
        name='profile_redirect'
        ),
    url(
        r'^denied/$',
        PermissionDeniedRedirect.as_view(),
        name='denied_redirect'
        ),
    url(
        r'^inactive/$',
        InactiveRedirect.as_view(),
        name='inactive_redirect'
        ),
    url(
        r'^(?P<user_slug>[-\w\d]+)/stats/edit/$',
        HikerStatsUpdateView.as_view(),
        name='hiker_stats_edit'
        ),
    url(
        r'^(?P<user_slug>[-\w\d]+)/address/edit/$',
        HikerAddressUpdateView.as_view(),
        name='hiker_address_edit'
        ),
    url(
        r'^(?P<user_slug>[-\w\d]+)/edit/$',
        HikerBasicInfoUpdateView.as_view(),
        name='hiker_profile_edit'
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
