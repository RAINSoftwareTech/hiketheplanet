# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel
from hikes.models import Hike
from hikers.models import Hiker
from hikers.utils import deleted_hiker_fallback


class Equipment(TimeStampedModel):
    """Each hike may have multiple equipment recommendations: poles,
    waterproof boots, overnight gear, etc"""
    GEAR_TYPE = (
        ('clothes', _('Apparel')),
        ('footwear', _('Footwear')),
        ('safety', _('Safety/First Aid')),
    )

    hike = models.ForeignKey(Hike, on_delete=models.CASCADE,
                             related_name='equipment')
    gear_type = models.CharField(max_length=20, choices=GEAR_TYPE)
    recommended_gear = models.CharField(max_length=200)
    explanation = models.TextField()

    # restrict edit to creator and admin
    added_by = models.ForeignKey(Hiker, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='equipment_recommended')

    class Meta:
        verbose_name = "Equipment"
        ordering = ['gear_type', '-modified']

    def __unicode__(self):
        return "{} - {}".format(self.gear_type, self.recommended_gear)

    def save(self, *args, **kwargs):
        if not self.added_by:
            self.added_by = deleted_hiker_fallback()
        super(Equipment, self).save(*args, **kwargs)
