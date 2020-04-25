# -*- coding: utf-8 -*-

import pytz

from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from django.utils import timezone

from mock import patch

from hikers.tests.factories import UserFactory, HikerFactory
from middleware.timezones import TimezoneMiddleware, default_tz_name


class TimezoneTests(TestCase):

    def setUp(self):  # noqa
        self.request = RequestFactory().get('/fake-path')
        self.tz = TimezoneMiddleware()

    def test_timezone_middleware(self):
        self.request.user = AnonymousUser()
        self.assertEquals(self.tz.get_tz_name(self.request), default_tz_name)

        self.request.user = UserFactory()
        self.assertEquals(self.tz.get_tz_name(self.request), default_tz_name)

        test_tz = 'Pacific/Honolulu'
        self.request.user.hiker = HikerFactory()
        self.request.user.hiker.timezone = test_tz
        self.assertEquals(self.tz.get_tz_name(self.request), test_tz)

    @patch.object(TimezoneMiddleware, 'get_tz_name')
    def test_process_request(self, mock_tz_name):
        mock_tz_name.return_value = None
        self.tz.process_request(self.request)
        self.assertFalse(hasattr(timezone._active, 'value'))
        mock_tz_name.return_value = default_tz_name
        self.tz.process_request(self.request)
        self.assertTrue(hasattr(timezone._active, 'value'))
        self.assertEquals(timezone._active.value,
                          pytz.timezone(default_tz_name))
