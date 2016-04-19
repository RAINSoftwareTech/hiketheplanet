# -*- coding: utf-8 -*-

from django.test import TestCase

from hikes.models import Region, Trailhead, Hike
from hikes.tests.factories import RegionFactory, TrailheadFactory, HikeFactory


class HikesModelsTests(TestCase):

    def setUp(self):  # noqa
        self.region = RegionFactory()
        self.trailhead = TrailheadFactory()
        self.hike = HikeFactory()

    def test_region_unicode(self):
        self.assertIsInstance(self.region, Region)
        self.assertEquals(self.region.name, self.region.__unicode__())

    def test_trailhead_unicode(self):
        self.assertIsInstance(self.trailhead, Trailhead)
        self.assertEquals(self.trailhead.name, self.trailhead.__unicode__())

    def test_hikes_unicode(self):
        self.assertIsInstance(self.hike, Hike)
        self.assertEquals(self.hike.name, self.hike.__unicode__())
