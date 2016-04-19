from django.db import models

from core.models import TimeStampedModel
from hikes.models import Hike
from hikers.models import Hiker
from hikers.utils import deleted_hiker_fallback


class Hazard(TimeStampedModel):
    """Each hike may have multiple potential hazards - or none. This section
    is meant to be editable by registered users.
    Dates created and modified added by base model
    """
    HAZARD_TYPE = (
        ('trail', 'Trail Damage'),
        ('weather', 'Weather Effects'),
        ('permanent', 'General/On-going Conditions'),
        ('other', 'Other'),
    )
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE,
                             related_name='hazards')
    hazard_type = models.CharField(choices=HAZARD_TYPE, max_length=15)
    description = models.TextField()
    date_resolved = models.DateTimeField(blank=True, null=True)
    reported_by = models.ForeignKey(Hiker, on_delete=models.SET_NULL,
                                    null=True, related_name='reported_hazards')
    resolution_reported_by = models.ForeignKey(Hiker,
                                               on_delete=models.SET_NULL,
                                               null=True,
                                               related_name='resolved_hazards')

    class Meta:
        ordering = ['-created', '-date_resolved']

    def __unicode__(self):
        date_fmt = '%Y-%m-%d %H:%M'
        return '{} - {}'.format(self.hazard_type,
                                self.created.strftime(date_fmt))

    def save(self, *args, **kwargs):
        if not self.reported_by:
            self.reported_by = deleted_hiker_fallback()
        if self.date_resolved and not self.resolution_reported_by:
            self.resolution_reported_by = deleted_hiker_fallback()
        super(Hazard, self).save(*args, **kwargs)
