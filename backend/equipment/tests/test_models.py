# -*- coding: utf-8 -*-

# Imports from Django
from django.test import TestCase

# Imports from Third Party Modules
import mock

# Local Imports
from hikers.tests.factories import HikerFactory

# Local imports
from ..models import Equipment
from .factories import EquipmentFactory


class EquipmentModelTests(TestCase):

    def setUp(self):  # noqa
        self.equipment = EquipmentFactory()

    def test_equipment_unicode(self):
        self.assertIsInstance(self.equipment, Equipment)
        self.assertIn(self.equipment.recommended_gear,
                      self.equipment.__str__())
        self.assertIn(self.equipment.gear_type,
                      self.equipment.__str__())

    @mock.patch('equipment.models.deleted_hiker_fallback')
    def test_equipment_save(self, mock_deleted_hiker_fallback):
        added = HikerFactory()
        empty = HikerFactory()
        mock_deleted_hiker_fallback.return_value = empty
        equipment = EquipmentFactory(added_by=added)
        equipment.save()
        self.assertFalse(mock_deleted_hiker_fallback.called)

        equipment.added_by = None
        equipment.save()
        self.assertTrue(mock_deleted_hiker_fallback.called)
