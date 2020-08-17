# -*- coding: utf-8 -*-

# Imports from Django
from django.http import Http404
from django.test import RequestFactory, TestCase
from django.views.generic import TemplateView

# Imports from Third Party Modules
from geopy import GoogleV3

# Local Imports
from core.utils import setup_view
from hikes.models import Hike, Trailhead
from hikes.utils import (
    get_hike_object,
    get_hike_queryset,
    get_trailhead_object,
    get_trailhead_queryset,
)

# Local imports
from ..models import Trailhead
from ..utils import trailheads_as_the_crow_flies
from .factories import HikeFactory, TrailheadFactory


class TestView(TemplateView):
    pass


class HikesUtilsTests(TestCase):

    def setUp(self):  # noqa
        self.trailhead = TrailheadFactory()
        self.hike = HikeFactory(trailhead=self.trailhead)

        self.request = RequestFactory().get('/fake-path')
        view = TemplateView(template_name='test_views.html')
        self.view = setup_view(view, self.request,
                               trailhead_slug=self.trailhead.slug,
                               hike_slug=self.hike.slug)

    def test_get_trailhead_object(self):
        self.assertEquals(self.trailhead,
                          get_trailhead_object(self.view.kwargs))
        self.view.kwargs['trailhead_slug'] = 'bad slug'
        with self.assertRaisesMessage(
                Http404, 'does not represent a saved Trailhead'):
            get_trailhead_object(self.view.kwargs)
        self.assertIsNone(get_trailhead_object({}))

    def test_get_hike_object(self):
        self.assertEquals(self.hike,
                          get_hike_object(self.view.kwargs))
        self.view.kwargs['hike_slug'] = 'bad slug'
        with self.assertRaisesMessage(
                Http404, 'does not represent a saved Hike'):
            get_hike_object(self.view.kwargs)
        self.assertIsNone(get_hike_object({}))

    # def test_get_trailhead_queryset(self):
    #     qs = get_trailhead_queryset(self.view.kwargs)
    #     self.assertQuerysetEqual(qs, map(repr, Trailhead.objects.filter()))

    def test_get_hike_queryset(self):
        qs = get_hike_queryset(self.view.kwargs)
        self.assertQuerysetEqual(qs, map(repr, Hike.objects.filter(
            trailhead=self.trailhead)))


class SearchUtilsTests(TestCase):

    def setUp(self):  # noqa
        geolocator = GoogleV3()
        address, coordinates = geolocator.geocode('97219')
        self.region = RegionFactory()
        self.trailhead = TrailheadFactory(region=self.region,
                                          latitude=coordinates[0],
                                          longitude=coordinates[1])
        self.hike = HikeFactory(trailhead=self.trailhead)

    def test_trailheads_as_the_crow_flies(self):
        trails = trailheads_as_the_crow_flies('8', '97219', {})
        self.assertIsInstance(trails[0], Trailhead)
        self.assertIn(self.trailhead, trails)

        trails = trailheads_as_the_crow_flies('150', '97219', {})
        self.assertNotIn(self.trailhead, trails)
