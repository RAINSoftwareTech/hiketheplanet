# -*- coding: utf-8 -*-

from django.conf.urls import url
from hikers.views import (HikerProfileView)

urlpatterns = [
    url(
        r'^profile/(?P<user_slug>[-\w\d]+)/$',
        HikerProfileView.as_view(),
        name='hiker_profile'
        ),
]
