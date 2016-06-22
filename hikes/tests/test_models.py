# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils.text import slugify

from hikes.models import CountryRegion, Region, Trailhead, Hike
from hikes.tests.factories import (CountryRegionFactory, RegionFactory,
                                   TrailheadFactory, HikeFactory)


class HikesModelsTests(TestCase):

    def setUp(self):  # noqa
        self.country_region = CountryRegionFactory()
        self.region = RegionFactory()
        self.trailhead = TrailheadFactory()
        self.hike = HikeFactory()

    def test_country_region_unicode(self):
        self.assertIsInstance(self.country_region, CountryRegion)
        self.assertIn(self.country_region.country_abbrev,
                      self.country_region.__unicode__())
        self.assertIn(self.country_region.region_name,
                      self.country_region.__unicode__())

    def test_region_unicode(self):
        self.assertIsInstance(self.region, Region)
        self.assertEquals(self.region.name, self.region.__unicode__())

    def test_trailhead_unicode(self):
        self.assertIsInstance(self.trailhead, Trailhead)
        self.assertEquals(self.trailhead.name, self.trailhead.__unicode__())

    def test_hikes_unicode(self):
        self.assertIsInstance(self.hike, Hike)
        self.assertEquals(self.hike.name, self.hike.__unicode__())

    def test_slugify_base(self):
        test_name = 'My Slug Name 2016'
        slug_name = slugify(test_name)
        test_slug = RegionFactory(name=test_name)
        test_slug.save()
        self.assertEquals(test_slug.slug, slug_name)

    def test_country_region_save(self):
        test_name = 'My Region Name 2016'
        test_co = 'us'
        slug_name = slugify('{}-{}'.format(test_name, test_co))
        test_slug = CountryRegionFactory(region_name=test_name,
                                         country_abbrev=test_co)
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

    def test_absolute_urls(self):
        co_region = CountryRegionFactory()
        region = RegionFactory(country_region=co_region)
        trailhead = TrailheadFactory(region=region)
        hike = HikeFactory(trailhead=trailhead)
        self.assertIn(co_region.slug, co_region.get_absolute_url())
        self.assertIn(region.slug, region.get_absolute_url())
        self.assertIn(region.slug, trailhead.get_absolute_url())
        self.assertIn(trailhead.slug, trailhead.get_absolute_url())
        self.assertIn(region.slug, hike.get_absolute_url())
        self.assertIn(trailhead.slug, hike.get_absolute_url())
        self.assertIn(hike.slug, hike.get_absolute_url())
