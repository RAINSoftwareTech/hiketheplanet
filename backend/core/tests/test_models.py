# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify
from django.test import TestCase

from core.models import AddressBase, SlugifiedNameBase, GeoSlugifiedNameBase


class AddressModel(AddressBase):
    class Meta:
        app_label = 'core'


class TestSlugifiedName(SlugifiedNameBase):
    name = models.CharField(max_length=25)

    class Meta:
        app_label = 'core'


class TestGeoSlugifiedName(GeoSlugifiedNameBase):
    name = models.CharField(max_length=25)

    class Meta:
        app_label = 'core'


class CoreModelTests(TestCase):
    """Tests for all functions in core Models."""

    def setUp(self):  # noqa
        self.address = AddressModel(address_line1='random address')
        self.address1 = AddressModel(city='Random City')
        self.address2 = AddressModel(address_line1='another random address)',
                                     city='')
        self.address3 = AddressModel(city='')
        self.address4 = AddressModel(city='', zipcode='')

    # Tests on Address model short address property method

    def test_address_short_address_all(self):
        self.assertIn(self.address.address_line1, self.address.short_address)
        self.assertIn(self.address.city, self.address.short_address)
        self.assertIn(self.address1.city, self.address1.short_address)
        self.assertEquals(self.address2.address_line1,
                          self.address2.short_address)
        self.assertEquals(self.address3.short_address,
                          self.address3.zipcode)
        self.assertEquals(self.address4.short_address, 'No Address')

    def test_short_address_unicode(self):
        self.assertEquals(self.address.__unicode__(),
                          self.address.short_address)

    def test_slugify_bases(self):
        regular_slug = TestSlugifiedName(name='Name to Slug')
        regular_slug.save()
        self.assertEquals(slugify(regular_slug.name), regular_slug.slug)

        geo_slug = TestGeoSlugifiedName(name='Geoname to Slug')
        geo_slug.save()
        self.assertEquals(slugify(geo_slug.name), geo_slug.slug)
