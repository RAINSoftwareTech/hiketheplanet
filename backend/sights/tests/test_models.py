# -*- coding: utf-8 -*-

# Imports from Django
from django.test import TestCase

# Imports from Third Party Modules
import mock

# Local Imports
from hikers.tests.factories import HikerFactory

# Local imports
from ..models import Sight
from .factories import SightFactory


class SightModelTests(TestCase):

    def test_hike_sight_unicode(self):
        sight = SightFactory()
        self.assertIsInstance(sight, Sight)
        self.assertIn(sight.sight_type,
                      sight.__str__())
        self.assertIn(sight.hike.name,
                      sight.__str__())

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
