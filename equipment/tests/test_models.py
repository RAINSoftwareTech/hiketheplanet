# -*- coding: utf-8 -*-

import mock

from django.test import TestCase

from hikers.tests.factories import HikerFactory

from equipment.models import Equipment
from equipment.tests.factories import EquipmentFactory


class EquipmentModelTests(TestCase):

    def setUp(self):  # noqa
        self.equipment = EquipmentFactory()

    def test_equipment_unicode(self):
        self.assertIsInstance(self.equipment, Equipment)
        self.assertIn(self.equipment.recommended_gear,
                      self.equipment.__unicode__())
        self.assertIn(self.equipment.gear_type,
                      self.equipment.__unicode__())

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
