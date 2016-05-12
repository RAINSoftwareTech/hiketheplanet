# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from localflavor.us.models import PhoneNumberField
from timezones.zones import PRETTY_TIMEZONE_CHOICES

from core.models import TimeStampedModel, AddressBase
from hikes.models import Hike


class Hiker(TimeStampedModel):
    """Hiker personal profile information."""
    # Todo: Add default profile pic. Profile pic locations?? Avg pace function.
    HEALTH_LEVELS = (
        ('0poor', _('Poor')),
        ('1mediocre', _('Mediocre')),
        ('2average', _('Average')),
        ('3moderate', _('Moderately Fit')),
        ('4fit', _('Fit & Active')),
    )

    hiker = models.OneToOneField(User, on_delete=models.CASCADE,
                                 related_name='hiker')
    profile_pic = models.ImageField(upload_to='profile_images', blank=True)
    health_level = models.CharField(max_length=100, default='2average',
                                    choices=HEALTH_LEVELS)
    avg_walking_pace = models.FloatField(default=2.0)
    miles_walked = models.FloatField(default=0.0)
    timezone = models.CharField(max_length=255,
                                choices=PRETTY_TIMEZONE_CHOICES,
                                blank=True, default=b'America/Los_Angeles')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-created']

    # def miles_calculated(self):
    #     # add miles from hike each time hiker checks in/out of hike to
    #     # total miles hiked since date_joined.
    #     pass

    def __unicode__(self):
        return self.hiker.username

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.__unicode__())
        super(Hiker, self).save(*args, **kwargs)


class HikerAddress(AddressBase):
    """Optional model to capture hiker address. Defaults to Portland, 97219
    if hiker chooses not to provide address information.
    Force cell number if emergency/late alerts (future feature) are desired.
    """
    hiker = models.OneToOneField(Hiker, on_delete=models.CASCADE,
                                 related_name='address')
    cell_number = PhoneNumberField(null=True, blank=True)


class HikerDiaryEntry(TimeStampedModel):
    """Model for recording diary/blog entries for each hiker.
    Each entry is private unless otherwise checked. both will be deleted on
    account removal."""
    # Todo: add validation on hike so that it is required if make_public
    hiker = models.ForeignKey(Hiker, on_delete=models.CASCADE,
                              related_name='diaries')
    hike = models.ForeignKey(Hike, on_delete=models.SET_NULL,
                             related_name='diaries_by_hike',
                             blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True,)
    diary_entry = models.TextField()

    make_public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-modified']

    def __unicode__(self):
        date_fmt = '%Y-%m-%d'
        if self.title and self.hike:
            return '{} - {}'.format(self.title, self.hike.name)
        elif self.title:
            return '{} - {}'.format(self.title,
                                    self.created.strftime(date_fmt))
        elif self.hike:
            return '{} - {}'.format(self.hike.name,
                                    self.created.strftime(date_fmt))
        else:
            return self.created.strftime(date_fmt)


class HikerPhoto(TimeStampedModel):
    """Model for user photos. Can optionally be linked to hike or hiker
    diary. Can be public or private; both will be deleted on account
    removal.
    """
    # Todo: add validation on hike so that it is required if make_public
    diary_entry = models.ForeignKey(HikerDiaryEntry,
                                    related_name='diary_photos',
                                    null=True, blank=True)
    hiker = models.ForeignKey(Hiker, on_delete=models.CASCADE,
                              related_name='hiker_photos')
    hike = models.ForeignKey(Hike, on_delete=models.SET_NULL,
                             related_name='hiker_photos_by_hike',
                             blank=True, null=True)

    photo = models.ImageField(upload_to='hike_photos', blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    make_public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-modified']

    def __unicode__(self):
        date_fmt = '%Y-%m-%d'
        if self.title and self.hike:
            return '{} - {}'.format(self.title, self.hike)
        elif self.title:
            return '{} - {}'.format(self.title,
                                    self.created.strftime(date_fmt))
        elif self.hike:
            return '{} - {}'.format(self.hike.name,
                                    self.created.strftime(date_fmt))
        else:
            return '{} - {}'.format(self.photo.name,
                                    self.created.strftime(date_fmt))


class FutureHike(TimeStampedModel):
    """Model for the list of hikes hiker has not yet taken, but might like to.
    Entries to be created/deleted by MyHike save functions.
    """
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE,
                             related_name='future_hikes')
    hiker = models.ForeignKey(Hiker, on_delete=models.CASCADE,
                              related_name='future_hikes_by_hiker')

    class Meta:
        ordering = ['-created']
        unique_together = ("hike", "hiker")

    def __unicode__(self):
        return self.hike.name


class MyHike(models.Model):
    """Model for tracking all hikes hiker wishes to add to their list of
    hikes, with ratings."""
    RATING_CHOICES = (
        ('0never', _('Never Hiked')),
        ('1loved', _('Loved It')),
        ('2liked', _('Liked It')),
        ('3unsure', _('Not Sure')),
        ('4ok', _('It Was Ok')),
        ('5had_better', _('Had Better')),
        ('6hated', _('Hated It')),
    )

    hike = models.ForeignKey(Hike, on_delete=models.CASCADE,
                             related_name='my_hikes')
    hiker = models.ForeignKey(Hiker, on_delete=models.CASCADE,
                              related_name='my_hikes_by_hiker')
    last_hiked = models.DateField(blank=True, null=True)
    rating = models.CharField(max_length=20, choices=RATING_CHOICES,
                              default='0never')

    class Meta:
        ordering = ['rating']
        unique_together = ("hike", "hiker")

    def __unicode__(self):
        return '{} - {}'.format(self.hike.name, self.rating)

    def update_future_hikes(self):
        """Function to add, update, or delete entries from FutureHikes
        depending on whether rating selection is set to never.
        :return: not applicable
        """
        # Todo: Should future hikes be limited to only never hiked hikes??
        if self.rating == '0never':
            FutureHike.objects.update_or_create(hike=self.hike,
                                                hiker=self.hiker,
                                                defaults={'hike': self.hike,
                                                          'hiker': self.hiker})
        elif FutureHike.objects.filter(hike=self.hike,
                                       hiker=self.hiker).exists():
            FutureHike.objects.filter(hike=self.hike,
                                      hiker=self.hiker).delete()

    def last_hiked_validator(self):
        """Function to create a custom validator to enforce required on
        last_hiked date for any value other than never hiked.
        :return: Validation Error
        """
        if not self.rating == '0never' and not self.last_hiked:
            raise ValidationError("Don't forget to add an estimated "
                                  "date for when you last took this hike.")
        elif self.rating == '0never' and self.last_hiked:
            raise ValidationError("You should not have a date for the last"
                                  " time you took this hike. Please remove the"
                                  " date or change your rating.")

    def save(self, *args, **kwargs):
        """Overrides default save function to force validation check on
        last_hiked. On confirmed validation, remainder of default is run and
        updates are made to FutureHikes.
        :param args:
        :param kwargs:
        :return: default function return
        """
        self.last_hiked_validator()
        super(MyHike, self).save(*args, **kwargs)
        self.update_future_hikes()
