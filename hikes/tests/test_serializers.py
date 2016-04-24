# -*- coding: utf-8 -*-

import json
import mock

from django.core.urlresolvers import reverse_lazy
from django.test import TestCase

from hikes.models import Trailhead
from hikes.serializers import trailheads_map_serializer, trailhead_url
from hikes.tests.factories import RegionFactory, TrailheadFactory, HikeFactory


class HikesSerializersTests(TestCase):

    def setUp(self):  # noqa
        self.region = RegionFactory()
        self.trailhead = TrailheadFactory(region=self.region)
        self.hike = HikeFactory(trailhead=self.trailhead)

    def test_trailhead_url(self):
        self.trailhead.num_hikes = 3
        url0 = trailhead_url(self.trailhead, self.region)
        self.assertIn(self.region.slug, url0)
        self.assertIn(self.trailhead.slug, url0)
        self.assertNotIn(self.hike.slug, url0)

        self.trailhead.num_hikes = 1
        url1 = trailhead_url(self.trailhead, self.region)
        self.assertIn(self.region.slug, url1)
        self.assertIn(self.trailhead.slug, url1)
        self.assertIn(self.hike.slug, url1)

        HikeFactory(trailhead=self.trailhead)
        self.trailhead.num_hikes = 1
        url2 = trailhead_url(self.trailhead, self.region)
        self.assertIn(self.region.slug, url2)
        self.assertIn(self.trailhead.slug, url2)
        self.assertNotIn(self.hike.slug, url2)
        self.assertEquals(self.trailhead.num_hikes, 2)

        trailhead1 = TrailheadFactory(region=self.region)
        trailhead1.num_hikes = 1
        url3 = trailhead_url(trailhead1, self.region)
        self.assertIn(self.region.slug, url3)
        self.assertIn(trailhead1.slug, url3)
        self.assertNotIn('hikes/', str(url3))

    @mock.patch('hikes.serializers.trailhead_url')
    def test_trailheads_map_serializer(self, mock_url):
        mock_url.return_value = reverse_lazy(
            'hikes:trailhead',
            kwargs={'trailhead_slug': self.trailhead.slug,
                    'region_slug': self.region.slug})
        trailheads = Trailhead.objects.all()
        serialized = json.loads(trailheads_map_serializer(trailheads,
                                                          self.region))
        self.assertEquals(len(serialized['result']), trailheads.count())
