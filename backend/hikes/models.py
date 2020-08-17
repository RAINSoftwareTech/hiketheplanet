# -*- coding: utf-8 -*-

# Imports from Django
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos import Point
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Imports
from core.models import GeoSlugifiedNameBase, SlugifiedNameBase


class Trailhead(GeoSlugifiedNameBase):
    """Class for capturing base information about trailheads, the places where
    hikes start. presumptively the best approximation of parking locations.
    """
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    point = geomodels.PointField(srid=4326, spatial_index=True)
    state_province = models.ForeignKey(
        'localities.StateProvince',
        related_name='trailheads',
        on_delete=models.PROTECT
    )

    class Meta:
        ordering = ['state_province', 'name']
        constraints = (
            models.UniqueConstraint(
                fields=('state_province', 'name'), name='unique_trailhead'
            ),
        )
        indexes = [
            models.Index(fields=['name'], name='trailhead_idx'),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.point = Point(self.longitude, self.latitude)
        super(Trailhead, self).save(*args, **kwargs)

    def miles_from_user(self, user_profile):
        pass

    def hours_from_user(self, user_profile):
        pass


class Hike(SlugifiedNameBase):
    """Class for capturing hike specific details."""
    DIFFICULTY = (
        ('0easy', _('Easy')),
        ('1moderate', _('Moderate')),
        ('2difficult', _('Difficult')),
    )
    HIKE_TYPES = (
        ('loop', _('Loop')),
        ('out_and_back', _('Out and Back')),
        ('lollipop', _('Lollipop/Dog Bone')),
        ('point_to_point', _('Point-to-Point/Destination')),
    )
    trailhead = models.ForeignKey(
        Trailhead, on_delete=models.CASCADE,
        related_name='hikes'
    )
    name = models.CharField(max_length=180, unique=True)

    hike_type = models.CharField(
        max_length=50, default='loop',
        choices=HIKE_TYPES
    )
    description = models.TextField()

    # likes = models.IntegerField(default=0) - move to popularity/reviews app?
    trail_map = models.FileField(upload_to='trail_maps', null=True)

    # specs
    difficulty_level = models.CharField(
        max_length=20, default="0easy", choices=DIFFICULTY
    )
    difficulty_level_explanation = models.CharField(
        max_length=250, blank=True, default='')
    distance = models.FloatField(default=0.0)
    elevation = models.IntegerField(default=0)
    high_point = models.IntegerField(default=0)

    class Meta:
        ordering = ['difficulty_level', 'distance']
        indexes = [
            models.Index(fields=['hike_type'], name='hike_type_idx'),
            models.Index(fields=['difficulty_level'], name='difficulty_idx'),
        ]

    def __str__(self):
        return self.name
