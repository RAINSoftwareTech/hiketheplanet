# -*- coding: utf-8 -*-

# Imports from Django
from django.test import RequestFactory, TestCase

# Imports from Third Party Modules
from mock import patch

# Local Imports
from core.utils import setup_view

# Local imports
from ..views import (
    HikeDetailAPIView,
    HikeListAPIView,
    TrailheadDetailAPIView,
    TrailheadListAPIView,
)
from .factories import HikeFactory, TrailheadFactory


class HikesAPIViewsTests(TestCase):

    def setUp(self):  # noqa
        self.request = RequestFactory().get('/fake-path')
        self.trailhead = TrailheadFactory()