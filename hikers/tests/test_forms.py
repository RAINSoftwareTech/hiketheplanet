# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory

from hikers.forms import HikerRegistrationForm
from hikers.models import Hiker
from hikers.tests.factories import UserFactory


class HikesViewsTests(TestCase):

    def test_views(self):
        user = UserFactory()
        self.assertFalse(Hiker.objects.filter(hiker=user).exists())
        request = RequestFactory().get('/fake-path')
        form_data = {'zipcode': '97219',
                     'city': 'Portland',
                     'state': 'OR',
                     'timezone': 'America/Los_Angeles'}
        hiker_form = HikerRegistrationForm(data=form_data)
        self.assertTrue(hiker_form.is_valid())
        hiker_form.signup(request=request, user=user)
        self.assertTrue(Hiker.objects.filter(hiker=user).exists())
