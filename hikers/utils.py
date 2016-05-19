# -*- coding: utf-8 -*-

from hikers.models import Hiker

from django.contrib.auth.models import User

deleted_user = 'deleted_user@hiketheplanet'


def deleted_hiker_fallback():
    empty_user, created = User.objects.get_or_create(username=deleted_user)
    empty_hiker, created = Hiker.objects.get_or_create(
        hiker=empty_user)
    return empty_hiker


def get_hiker(user):
    try:
        hiker = user.hiker
    except AttributeError:
        hiker, created = Hiker.objects.get_or_create(hiker=user)
    return hiker
