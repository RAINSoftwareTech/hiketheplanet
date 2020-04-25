# -*- coding: utf-8 -*-

from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos import Point
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from core.models import SlugifiedNameBase, GeoSlugifiedNameBase


class CountryRegion(geomodels.Model):
    """Class for holding greater, country wide regional specs. ie: Pacific
    Northwest-US.
    """
    country_abbrev = models.CharField(max_length=2)
    region_name = models.CharField(max_length=30)
    description = models.TextField()
    geom = geomodels.MultiPolygonField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['country_abbrev', 'region_name']
        unique_together = ('country_abbrev', 'region_name')

    def __unicode__(self):
        return '{} - {}'.format(self.region_name.title(),
                                self.country_abbrev.upper())

    def save(self, *args, **kwargs):
        self.slug = slugify('{}-{}'.format(self.region_name,
                                           self.country_abbrev))
        super(CountryRegion, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('hikes:broad_region_home',
                       kwargs={'co_region_slug': self.slug})


class Region(SlugifiedNameBase):
    """Class for holding list of Regions: ie: 'Oregon Coast', 'Columbia Gorge'.
    """
    name = models.CharField(max_length=50, unique=True)
    num_trailheads = models.IntegerField(default=1)
    country_region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE,
                                       related_name='subregions')

    class Meta:
        ordering = ['country_region', 'name']
        unique_together = ('country_region', 'name')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hikes:region_detail',
                       kwargs={'co_region_slug': self.country_region.slug,
                               'region_slug': self.slug})


class Trailhead(GeoSlugifiedNameBase):
    """Class for capturing base information about trailheads, the places where
    hikes start. presumptively the best approximation of parking locations.
    """
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name='trailheads')
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    num_hikes = models.IntegerField(default=1)

    point = geomodels.PointField(srid=4326)

    class Meta:
        ordering = ['region', '-num_hikes']
        unique_together = ('region', 'name')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hikes:trailhead_detail',
                       kwargs={'co_region_slug':
                               self.region.country_region.slug,
                               'region_slug': self.region.slug,
                               'trailhead_slug': self.slug})

    def save(self, *args, **kwargs):
        self.point = Point(self.longitude, self.latitude)
        super(Trailhead, self).save(*args, **kwargs)
        trailhead_count = Trailhead.objects.filter(region=self.region).count()
        self.region.num_trailheads = trailhead_count
        self.region.save()

    # def miles_from_user(self):
    #     pass
    #
    # def hours_from_user(self):
    #     pass


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
    trailhead = models.ForeignKey(Trailhead, on_delete=models.CASCADE,
                                  related_name='hikes')
    name = models.CharField(max_length=180, unique=True)

    hike_type = models.CharField(max_length=50, default='loop',
                                 choices=HIKE_TYPES)
    description = models.TextField()

    # likes = models.IntegerField(default=0) - move to popularity/reviews app?
    trail_map = models.FileField(upload_to='trail_maps', blank=True)

    # specs
    difficulty_level = models.CharField(max_length=20, default="0easy",
                                        choices=DIFFICULTY)
    difficulty_level_explanation = models.CharField(max_length=250, blank=True)
    distance = models.FloatField(default=0.0)
    elevation = models.IntegerField(default=0)
    high_point = models.IntegerField(default=0)

    class Meta:
        ordering = ['difficulty_level', 'distance']
        unique_together = ('trailhead', 'name')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hikes:hike_detail',
                       kwargs={'co_region_slug':
                               self.trailhead.region.country_region.slug,
                               'region_slug': self.trailhead.region.slug,
                               'trailhead_slug': self.trailhead.slug,
                               'hike_slug': self.slug})

    def save(self, *args, **kwargs):
        super(Hike, self).save(*args, **kwargs)
        hike_count = Hike.objects.filter(trailhead=self.trailhead).count()
        self.trailhead.num_hikes = hike_count
        self.trailhead.save()
