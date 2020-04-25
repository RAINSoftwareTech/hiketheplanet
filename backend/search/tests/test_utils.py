# -*- coding: utf-8 -*-

from django.test import TestCase

from geopy.geocoders import GoogleV3

from hikes.models import Trailhead
from hikes.tests.factories import RegionFactory, TrailheadFactory, HikeFactory
from search.utils import trailheads_as_the_crow_flies


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
