# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils.text import slugify

from hikes.models import Region, Trailhead, Hike
from hikes.tests.factories import RegionFactory, TrailheadFactory, HikeFactory


class HikesModelsTests(TestCase):

    def test_region_unicode(self):
        self.region = RegionFactory()
        self.assertIsInstance(self.region, Region)
        self.assertEquals(self.region.name, self.region.__unicode__())

    def test_trailhead_unicode(self):
        self.trailhead = TrailheadFactory()
        self.assertIsInstance(self.trailhead, Trailhead)
        self.assertEquals(self.trailhead.name, self.trailhead.__unicode__())

    def test_hikes_unicode(self):
        self.hike = HikeFactory()
        self.assertIsInstance(self.hike, Hike)
        self.assertEquals(self.hike.name, self.hike.__unicode__())

    def test_slugify_base(self):
        test_name = 'My Slug Name 2016'
        slug_name = slugify(test_name)
        test_slug = RegionFactory(name=test_name)
        test_slug.save()
        self.assertEquals(test_slug.slug, slug_name)

    def test_update_counts(self):
        test_region = RegionFactory(num_trailheads=0)
        test_trailhead = TrailheadFactory(num_hikes=0, region=test_region)
        test_trailhead.save()
        trailhead_count = Trailhead.objects.filter(region=test_region).count()
        self.assertEquals(test_region.num_trailheads, trailhead_count)

        test_hike = HikeFactory(trailhead=test_trailhead)
        test_hike.save()
        hike_count = Hike.objects.filter(trailhead=test_trailhead).count()
        self.assertEquals(test_trailhead.num_hikes, hike_count)
