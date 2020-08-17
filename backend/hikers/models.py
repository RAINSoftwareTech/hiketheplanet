# -*- coding: utf-8 -*-

# Imports from Django

# Imports from Django
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

# Imports from Third Party Modules
from pytz import common_timezones

# Local Imports
from core.models import AddressBase, TimeStampedModel
from core.utils import (
    hiker_photos_upload_path,
    profile_pics_upload_path,
    title_hike_or_date_str,
    unique_slugify,
    validate_file_has_extension,
    validate_file_upload_size,
)
from hikes.models import Hike

TIMEZONES = tuple(zip(common_timezones, common_timezones))
unsubscribed_user = 'unsubscribed@hiketheplanet'
User = get_user_model()


def SET_UNSUBSCRIBED(collector, field, sub_objs, using):
    collector.add_field_update(
        field, Hiker.objects.get(hiker__username=unsubscribed_user), sub_objs
    )


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

    hiker = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='hiker'
    )
    profile_pic = models.ImageField(
        upload_to=profile_pics_upload_path, null=True,
        validators=[validate_file_upload_size, validate_file_has_extension]
    )
    health_level = models.CharField(
        max_length=100, default='2average', choices=HEALTH_LEVELS
    )
    avg_walking_pace = models.FloatField(default=2.0)
    miles_walked = models.FloatField(default=0.0)
    timezone = models.CharField(
        max_length=255, choices=TIMEZONES,
        blank=True, default='America/Los_Angeles'
    )
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-created']

    # def miles_calculated(self):
    #     # add miles from hike each time hiker checks in/out of hike to
    #     # total miles hiked since date_joined.
    #     pass

    def __str__(self):
        return self.hiker.username

    def get_absolute_url(self):
        return reverse('hikers:profile', kwargs={'user_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.__str__())
        return super(Hiker, self).save(*args, **kwargs)


class HikerAddress(AddressBase):
    """Optional model to capture hiker address.
    Force cell number if emergency/late alerts (future feature) are desired.
    """
    hiker = models.OneToOneField(Hiker, on_delete=models.CASCADE,
                                 related_name='address')
    cell_number = models.CharField(null=True, max_length=20)

    def get_absolute_url(self):
        return reverse('hikers:profile',
                       kwargs={'user_slug': self.hiker.slug})


class HikerDiaryEntry(TimeStampedModel):
    """Model for recording diary/blog entries for each hiker.
    Each entry is private unless otherwise checked. both will be deleted on
    account removal."""
    hiker = models.ForeignKey(
        Hiker, on_delete=models.CASCADE,
        related_name='diaries'
    )
    # TODO: add validation on hike so that it is required if make_public
    hike = models.ForeignKey(
        Hike, on_delete=models.SET_NULL,
        related_name='diaries_by_hike', null=True
    )
    title = models.CharField(max_length=200, blank=True, default='untitled')
    diary_entry = models.TextField()

    make_public = models.BooleanField(default=False)
    slug = models.SlugField()

    class Meta:
        ordering = ['-modified']

    def __str__(self):
        return title_hike_or_date_str(self)

    def get_absolute_url(self):
        return reverse(
            'hikers:diaries',
            kwargs={'user_slug': self.hiker.slug}
        )

    def get_delete_url(self):
        if not self.pk:
            return None
        return reverse(
            'hikers:diaries_delete',
            kwargs={'user_slug': self.hiker.slug, 'diary_slug': self.slug}
        )

    def save(self, *args, **kwargs):
        hiker_qs = HikerDiaryEntry.objects.filter(hiker=self.hiker)
        self.slug = unique_slugify(hiker_qs, self.__str__())
        return super(HikerDiaryEntry, self).save(*args, **kwargs)


class HikerPhoto(TimeStampedModel):
    """Model for user photos. Can optionally be linked to hike or hiker
    diary. Can be public or private; both will be deleted on account
    removal.
    """
    # TODO: add validation on hike so that it is required if make_public
    diary_entry = models.ForeignKey(
        HikerDiaryEntry,
        related_name='diary_photos',
        null=True, on_delete=models.CASCADE
    )
    hiker = models.ForeignKey(
        Hiker, on_delete=models.CASCADE,
        related_name='hiker_photos'
    )
    hike = models.ForeignKey(
        Hike, on_delete=models.SET_NULL,
        related_name='hiker_photos_by_hike', null=True
    )

    photo = models.ImageField(
        upload_to=hiker_photos_upload_path,
        validators=[validate_file_upload_size, validate_file_has_extension]
    )
    title = models.CharField(max_length=100, blank=True, default='untitled')

    make_public = models.BooleanField(default=False)
    slug = models.SlugField()

    class Meta:
        ordering = ['-modified']

    def __str__(self):
        return title_hike_or_date_str(self)

    def get_absolute_url(self):
        # todo: can probably get rid of this once serializers are rebuilt
        return reverse(
            'hikers:photos',
            kwargs={'user_slug': self.hiker.slug}
        )

    def get_delete_url(self):
        if not self.pk:
            return None
        return reverse(
            'hikers:photos_delete',
            kwargs={'user_slug': self.hiker.slug, 'photo_slug': self.slug}
        )

    def save(self, *args, **kwargs):
        hiker_qs = HikerPhoto.objects.filter(hiker=self.hiker)
        self.slug = unique_slugify(hiker_qs, self.__str__())
        super(HikerPhoto, self).save(*args, **kwargs)


class FutureHike(TimeStampedModel):
    """Model for the list of hikes hiker has not yet taken, but might like to.
    Entries to be created/deleted by MyHike save functions.
    """
    hike = models.ForeignKey(
        Hike, on_delete=models.CASCADE,
        related_name='future_hikes'
    )
    hiker = models.ForeignKey(
        Hiker, on_delete=models.CASCADE,
        related_name='future_hikes_by_hiker'
    )

    class Meta:
        ordering = ['-created']
        unique_together = ("hike", "hiker")

    def __str__(self):
        return self.hike.name

    def get_absolute_url(self):
        # todo: do I wnt to add a separate listview for future hikes
        return reverse(
            'hikers:myhikes',
            kwargs={'user_slug': self.hiker.slug}
        )


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

    hike = models.ForeignKey(
        Hike, on_delete=models.CASCADE,
        related_name='my_hikes'
    )
    hiker = models.ForeignKey(
        Hiker, on_delete=models.CASCADE,
        related_name='my_hikes_by_hiker'
    )
    last_hiked = models.DateField(null=True)
    rating = models.CharField(
        max_length=20, choices=RATING_CHOICES, default='0never'
    )

    class Meta:
        ordering = ['rating']
        unique_together = ("hike", "hiker")

    def __str__(self):
        return f'{self.hike.name} - {self.rating}'

    def get_absolute_url(self):
        return reverse(
            'hikers:myhikes',
            kwargs={'user_slug': self.hiker.slug}
        )

    def update_future_hikes(self):
        """Function to add, update, or delete entries from FutureHikes
        depending on whether rating selection is set to never.
        :return: not applicable
        """
        # Todo: Should future hikes be limited to only never hiked hikes??
        if self.rating == '0never':
            FutureHike.objects.update_or_create(
                hike=self.hike, hiker=self.hiker,
                defaults={'hike': self.hike, 'hiker': self.hiker}
            )
        elif FutureHike.objects.filter(hike=self.hike,
                                       hiker=self.hiker).exists():
            FutureHike.objects.filter(
                hike=self.hike, hiker=self.hiker
            ).delete()

    def last_hiked_validator(self):
        """Function to create a custom validator to enforce required on
        last_hiked date for any value other than never hiked.
        :return: Validation Error
        """
        if not self.rating == '0never' and not self.last_hiked:
            raise ValidationError(
                "Don't forget to add an estimated "
                "date for when you last took this hike."
            )
        elif self.rating == '0never' and self.last_hiked:
            raise ValidationError(
                "You should not have a date for the last"
                " time you took this hike. Please remove the"
                " date or change your rating."
            )

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
