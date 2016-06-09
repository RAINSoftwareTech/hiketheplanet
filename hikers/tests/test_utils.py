# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.test import TestCase, RequestFactory
from mock import MagicMock

from hikers.models import Hiker, HikerDiaryEntry
from hikers.tests.factories import UserFactory, HikerFactory
from hikers.utils import (deleted_user, deleted_hiker_fallback, get_hiker,
                          HikerCreateView)

from core.utils import setup_view


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

    def test_hiker_create_view_valid(self):
        request = RequestFactory().get('/fake-path')
        view = HikerCreateView(template_name='test_views.html',
                               model=HikerDiaryEntry)
        view = setup_view(view, request)
        request.user = UserFactory()
        request.user.hiker = HikerFactory()
        form = MagicMock()
        form.is_valid = MagicMock()
        form.is_valid.return_value = True
        self.assertIsInstance(view.form_valid(form),
                              HttpResponseRedirect)
