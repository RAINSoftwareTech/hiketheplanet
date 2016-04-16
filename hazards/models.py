from django.db import models

from core.models import TimeStampedModel
from hikes.models import Hike
from hikers.models import Hiker


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
    hike = models.ForeignKey(Hike, related_name='hazards')
    type = models.CharField(choices=HAZARD_TYPE, max_length=15)
    description = models.TextField()
    date_resolved = models.DateTimeField(blank=True, null=True)
    reported_by = models.ForeignKey(Hiker, related_name='reported_hazards')
    resolution_reported_by = models.ForeignKey(Hiker,
                                               related_name='resolved_hazards')

    class Meta:
        ordering = ['-created', '-date_resolved']

    def __unicode__(self):
        return self.type
