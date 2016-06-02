# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory

from factory import Faker

from hikers.forms import (HikerRegistrationForm, HikerBasicInfoForm,
                          HikerAddressForm)
from hikers.models import Hiker
from hikers.tests.factories import UserFactory, HikerFactory


class HikersFormsTests(TestCase):

    def setUp(self):  # noqa
        self.user = UserFactory()
        self.user1 = UserFactory(first_name=Faker('first_name'),
                                 last_name=Faker('last_name'),
                                 email=Faker('safe_email'))
        self.hiker1 = HikerFactory(hiker=self.user1)
        self.request = RequestFactory().get('/fake-path')
        self.tz = 'US/Eastern'
        self.info_form_data = {'first_name': 'Bob',
                               'last_name': 'Brown',
                               'email': 'bob.brown@yyy.cc',
                               'timezone': self.tz}

    def test_hiker_registration(self):
        self.assertFalse(Hiker.objects.filter(hiker=self.user).exists())
        form_data = {'zipcode': '97219',
                     'city': 'Portland',
                     'state': 'OR',
                     'timezone': self.tz}
        hiker_form = HikerRegistrationForm(data=form_data)
        self.assertTrue(hiker_form.is_valid())
        hiker_form.signup(request=self.request, user=self.user)
        self.assertTrue(Hiker.objects.filter(hiker=self.user).exists())

    def test_hiker_basic_info_init(self):
        with self.assertRaises(ValueError):
            HikerBasicInfoForm(data=self.info_form_data)
        info_form = HikerBasicInfoForm(data=self.info_form_data,
                                       instance=self.hiker1)
        self.assertEquals(info_form.initial['first_name'],
                          self.user1.first_name)

    def test_hiker_basic_save(self):
        info_form = HikerBasicInfoForm(data=self.info_form_data,
                                       instance=self.hiker1)
        self.assertNotEquals(self.user1.last_name,
                             self.info_form_data['last_name'])
        info_form.is_valid()
        info_form.save()
        self.assertEquals(self.user1.last_name,
                          self.info_form_data['last_name'])

    def test_hiker_address_init(self):
        address_form = HikerAddressForm()
        self.assertFalse(address_form.fields['city'].required)
