# -*- coding: utf-8 -*-

# Imports from Django
from django.contrib.gis.db import models as geomodels
from django.db import models
from django.utils.text import slugify

# Imports from Third Party Modules
from localflavor.us.models import USStateField, USZipCodeField
from localflavor.us.us_states import STATE_CHOICES


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AddressBase(models.Model):
    """US addresses base abstract model. """
    address_line1 = models.CharField(blank=True, max_length=50)
    address_line2 = models.CharField(blank=True, max_length=50)
    zipcode = USZipCodeField(blank=True, default='')
    city = models.CharField(blank=True, max_length=50, default='')
    state = USStateField(blank=True, choices=STATE_CHOICES, default='')

    class Meta:
        abstract = True

    @property
    def short_address(self):
        """Return short version of address"""
        city_state = ', '.join([
            elm for elm in (self.city, self.state) if elm]
        )
        address = ', '.join([
            elm for elm in (self.address_line1, city_state) if elm
        ])
        if not address and self.zipcode:
            address = self.zipcode
        elif not address:
            address = 'No Address'
        return address

    def __str__(self):
        return self.short_address


class SlugifiedNameBase(models.Model):
    slug = models.SlugField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SlugifiedNameBase, self).save(*args, **kwargs)


class GeoSlugifiedNameBase(geomodels.Model):
    slug = models.SlugField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(GeoSlugifiedNameBase, self).save(*args, **kwargs)
