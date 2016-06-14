# -*- coding: utf-8 -*-

import json

import mock
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase

from hikes.models import Trailhead, Hike
from hikes.tests.factories import RegionFactory, TrailheadFactory, HikeFactory
from search.serializers import (hikes_serializer, trailheads_serializer,
                                trailhead_or_hike_url)


class HikesSerializersTests(TestCase):

    def setUp(self):  # noqa
        self.region = RegionFactory(name='region')
        self.trailhead = TrailheadFactory(region=self.region, name='trailhead')
        self.hike = HikeFactory(trailhead=self.trailhead, name='hike')

    def test_trailhead_url(self):
        self.trailhead.num_hikes = 3
        url0 = trailhead_or_hike_url(self.trailhead)
        self.assertIn(self.region.slug, url0)
        self.assertIn(self.trailhead.slug, url0)
        self.assertNotIn(self.hike.slug, url0)

        self.trailhead.num_hikes = 1
        url1 = trailhead_or_hike_url(self.trailhead)
        self.assertIn(self.region.slug, url1)
        self.assertIn(self.trailhead.slug, url1)
        self.assertIn(self.hike.slug, url1)

        HikeFactory(trailhead=self.trailhead, name='hike2')
        self.trailhead.num_hikes = 1
        url2 = trailhead_or_hike_url(self.trailhead)
        self.assertIn(self.region.slug, url2)
        self.assertIn(self.trailhead.slug, url2)
        self.assertNotIn(self.hike.slug, url2)
        self.assertEquals(self.trailhead.num_hikes, 2)

        trailhead1 = TrailheadFactory(region=self.region, name='trailhead2')
        trailhead1.num_hikes = 1
        url3 = trailhead_or_hike_url(trailhead1)
        self.assertIn(self.region.slug, url3)
        self.assertIn(trailhead1.slug, url3)
        self.assertNotIn('hikes/', str(url3))

    @mock.patch('search.serializers.trailhead_or_hike_url')
    def test_trailheads_serializer(self, mock_url):
        mock_url.return_value = reverse_lazy(
            'hikes:trailhead_detail',
            kwargs={'trailhead_slug': self.trailhead.slug,
                    'region_slug': self.region.slug})
        trailheads = Trailhead.objects.all()
        serialized = json.loads(trailheads_serializer(trailheads))
        self.assertEquals(len(serialized), trailheads.count())

    def test_hikes_serializer(self):
        hikes = Hike.objects.all()
        serialized = json.loads(hikes_serializer(hikes))
        self.assertEquals(len(serialized), hikes.count())
