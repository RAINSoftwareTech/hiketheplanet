# -*- coding: utf-8 -*-

import mock

from django.test import TestCase

from hikers.tests.factories import HikerFactory

from sights.models import Sight
from sights.tests.factories import SightFactory


class SightModelTests(TestCase):

    def test_hike_sight_unicode(self):
        sight = SightFactory()
        self.assertIsInstance(sight, Sight)
        self.assertIn(sight.sight_type,
                      sight.__unicode__())
        self.assertIn(sight.hike.name,
                      sight.__unicode__())

    @mock.patch('sights.models.deleted_hiker_fallback')
    def test_hike_sight_save(self, mock_deleted_hiker_fallback):
        added = HikerFactory()
        empty = HikerFactory()
        mock_deleted_hiker_fallback.return_value = empty
        hike_sight = SightFactory(added_by=added)
        hike_sight.save()
        self.assertFalse(mock_deleted_hiker_fallback.called)

        hike_sight.added_by = None
        hike_sight.save()
        self.assertTrue(mock_deleted_hiker_fallback.called)
