# -*- coding: utf-8 -*-

# Imports from Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Imports
from core.models import TimeStampedModel
from hikers.models import SET_UNSUBSCRIBED, Hiker
from hikes.models import Hike


class Equipment(TimeStampedModel):
    """Each hike may have multiple equipment recommendations: poles,
    waterproof boots, overnight gear, etc"""
    GEAR_TYPE = (
        ('clothes', _('Apparel')),
        ('footwear', _('Footwear')),
        ('safety', _('Safety/First Aid')),
    )

    hike = models.ForeignKey(
        Hike, on_delete=models.CASCADE,
        related_name='equipment'
    )
    gear_type = models.CharField(max_length=20, choices=GEAR_TYPE)
    recommended_gear = models.CharField(max_length=200)
    explanation = models.TextField()

    # restrict edit to creator and admin
    added_by = models.ForeignKey(
        Hiker, on_delete=SET_UNSUBSCRIBED,
        null=True, related_name='equipment_recommended'
    )

    class Meta:
        verbose_name = 'Equipment'
        ordering = ['gear_type', '-modified']
        indexes = [
            models.Index(fields=['gear_type'], name='gear_idx'),
            models.Index(fields=['recommended_gear'], name='gear_rec_idx'),
        ]

    def __str__(self):
        return f'{self.gear_type} - {self.recommended_gear}'
