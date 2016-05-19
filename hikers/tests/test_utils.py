# -*- coding: utf-8 -*-

from django.test import TestCase

from hikers.models import Hiker
from hikers.tests.factories import UserFactory
from hikers.utils import deleted_user, deleted_hiker_fallback, get_hiker


class HikersUtilsTests(TestCase):

    def test_deleted_hiker_fallback(self):
        self.assertEquals(deleted_user,
                          deleted_hiker_fallback().hiker.username)

    def test_get_hiker(self):
        empty_user = UserFactory()

        # first show no hiker exists for user
        with self.assertRaises(Hiker.DoesNotExist):
            Hiker.objects.get(hiker=empty_user)
        # but hiker now exists for user after method is run
        hiker = get_hiker(empty_user)
        self.assertEquals(hiker, get_hiker(empty_user))
