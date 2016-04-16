from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel
from hikes.models import Hike
from hikers.models import Hiker
from hikers.utils import deleted_hiker_fallback


class Sight(TimeStampedModel):
    """Each hike may have multiple Sights to watch for. This section is meant
    to be editable by registered users and possibly pulled from "share"
    sections of user diaries."""
    SIGHT_TYPE = (
        ('0view', _('View')),
        ('1wildlife', _('Wildlife')),
        ('2flora', _('Plants')),
    )
    TIME_OF_DAY = (
        ('0sunrise', _('Sunrise')),
        ('1morning', _('Morning')),
        ('2midday', _('Midday')),
        ('3evening', _('Early Evening')),
        ('4sunset', _('Sunset')),
        ('5dark', _('After Dark')),
    )
    SEASON = (
        ('3winter', _('Winter')),
        ('0spring', _('Spring')),
        ('1summer', _('Summer')),
        ('2fall', _('Fall')),
    )
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE,
                             related_name='sights')
    type = models.CharField(choices=SIGHT_TYPE, max_length=10)
    description = models.TextField()
    best_time = models.CharField(choices=TIME_OF_DAY, max_length=10)
    best_season = models.CharField(choices=SEASON, max_length=8)

    # restrict edit to creator and admin
    added_by = models.ForeignKey(Hiker, on_delete=models.SET_NULL,
                                 null=True, related_name='sights_added')

    class Meta:
        ordering = ['type', 'best_season', 'best_time', '-modified']

    def __unicode__(self):
        return self.type

    def save(self, *args, **kwargs):
        if not self.added_by:
            self.added_by = deleted_hiker_fallback()
        super(Sight, self).save(*args, **kwargs)
