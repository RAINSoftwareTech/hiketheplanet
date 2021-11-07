# -*- coding: utf-8 -*-

# Imports from Django
from django.test import TestCase
from django.utils.text import slugify

# Local Imports
from hikes.models import Hike, Trailhead
from hikes.tests.factories import HikeFactory, TrailheadFactory


class HikesModelsTests(TestCase):

    def setUp(self):  # noqa
        self.trailhead = TrailheadFactory()
        self.hike = HikeFactory()

    def test_trailhead_unicode(self):
        self.assertIsInstance(self.trailhead, Trailhead)
        self.assertEquals(self.trailhead.name, self.trailhead.__str__())

    def test_hikes_unicode(self):
        self.assertIsInstance(self.hike, Hike)
        self.assertEquals(self.hike.name, self.hike.__str__())

    def test_slugify_base(self):
        test_name = 'My Slug Name 2016'
        slug_name = slugify(test_name)
        test_slug = TrailheadFactory(name=test_name)
        test_slug.save()
        self.assertEquals(test_slug.slug, slug_name)
