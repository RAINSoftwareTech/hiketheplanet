# -*- coding: utf-8 -*-

# Imports from Django
from django.test import TestCase
from django.urls import reverse_lazy

# Imports from Third Party Modules
import json
import mock

# Local imports
from ..models import Hike, Trailhead
from ..serializers import hikes_serializer, trailheads_serializer
from .factories import HikeFactory, TrailheadFactory


class HikesSerializersTests(TestCase):

    def setUp(self):  # noqa
        self.trailhead = TrailheadFactory(name='trailhead')
        self.hike = HikeFactory(trailhead=self.trailhead, name='hike')

    @mock.patch('search.serializers.trailhead_or_hike_url')
    def test_trailheads_serializer(self, mock_url):
        mock_url.return_value = reverse_lazy(
            'hikes:trailhead_detail',
            kwargs={'trailhead_slug': self.trailhead.slug})
        trailheads = Trailhead.objects.all()
        serialized = json.loads(trailheads_serializer(trailheads))
        self.assertEquals(len(serialized), trailheads.count())

    def test_hikes_serializer(self):
        hikes = Hike.objects.all()
        serialized = json.loads(hikes_serializer(hikes))
        self.assertEquals(len(serialized), hikes.count())
