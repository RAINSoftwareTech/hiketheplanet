# -*- coding: utf-8 -*-

from django.conf.urls import url
from hikers.views import (HikerProfileView, InactiveRedirect, ProfileRedirect)

urlpatterns = [
    url(
        r'^profile/(?P<user_slug>[-\w\d]+)/$',
        HikerProfileView.as_view(),
        name='hiker_profile'
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
    ]
