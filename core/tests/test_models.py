# -*- coding: utf-8 -*-

from django.test import TestCase

from core.models import AddressBase


class AddressModel(AddressBase):
    pass


class CoreModelTests(TestCase):
    """Tests for all functions in core Models."""

    def setUp(self):  # noqa
        self.address = AddressModel(address_line1='random address')
        self.address1 = AddressModel(city='Random City')
        self.address2 = AddressModel(address_line1='another random address)',
                                     city='')
        self.address3 = AddressModel(city='')

    # Tests on Address model short address property method

    def test_address_short_address_all(self):
        self.assertIn(self.address.address_line1, self.address.short_address)
        self.assertIn(self.address.city, self.address.short_address)
        self.assertEquals(self.address1.city, self.address1.short_address)
        self.assertEquals(self.address2.address_line1,
                          self.address2.short_address)
        self.assertEquals(self.address3.short_address, 'No Address')

    def test_short_address_unicode(self):
        self.assertEquals(self.address.__unicode__(),
                          self.address.short_address)
