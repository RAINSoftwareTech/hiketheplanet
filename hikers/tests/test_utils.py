# -*- coding: utf-8 -*-

from django.test import TestCase

from hikers.utils import deleted_user, deleted_hiker_fallback


class HikersUtilsTests(TestCase):

    def test_deleted_hiker_fallback(self):
        self.assertEquals(deleted_user,
                          deleted_hiker_fallback().hiker.username)
