# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USZipCodeField, USStateField

from django.contrib.gis.db import models as geomodels


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
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50, blank=True)
    zipcode = USZipCodeField(blank=True, default='97219')
    city = models.CharField(max_length=50, default='Portland')
    state = USStateField(choices=STATE_CHOICES, default='OR')

    class Meta:
        abstract = True

    @property
    def short_address(self):
        """Return short version of address"""
        if self.address_line1 and self.city:
            address = "{}, {}".format(self.address_line1, self.city)
        elif self.city:
            address = self.city
        elif self.address_line1:
            address = self.address_line1
        else:
            address = 'No Address'
        return address

    def __unicode__(self):
        return self.short_address


class SlugifiedNameBase(models.Model):
    slug = models.SlugField()

    class Meta:
        abstract = True
        app_label = 'core'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SlugifiedNameBase, self).save(*args, **kwargs)


class GeoSlugifiedNameBase(geomodels.Model):
    slug = models.SlugField()

    class Meta:
        abstract = True
        app_label = 'core'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(GeoSlugifiedNameBase, self).save(*args, **kwargs)
