# -*- coding: utf-8 -*-

# Imports from Django
from django.urls import include, path

# Local imports
from .views import (
    TrailheadsViewSet, HikesViewSet
)
from core.routers import OptionalSlashRouter
app_name = 'hikes'

router = OptionalSlashRouter()
router.include_format_suffixes = False
router.register(
    r'trailheads', TrailheadsViewSet, basename='trailhead'
)
router.register(
    r'hikes', HikesViewSet, basename='hike'
)

urlpatterns = [
    path('', include(router.urls)),
]
