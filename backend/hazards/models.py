# Imports from Django
from django.db import models

# Local Imports
from core.models import TimeStampedModel
from hikers.models import SET_UNSUBSCRIBED, Hiker
from hikes.models import Hike


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
    hike = models.ForeignKey(
        Hike, on_delete=models.CASCADE,
        related_name='hazards'
    )
    hazard_type = models.CharField(choices=HAZARD_TYPE, max_length=15)
    description = models.TextField()
    date_resolved = models.DateTimeField(null=True)
    reported_by = models.ForeignKey(
        Hiker, on_delete=SET_UNSUBSCRIBED,
        null=True, related_name='reported_hazards'
    )
    resolution_reported_by = models.ForeignKey(
        Hiker, on_delete=SET_UNSUBSCRIBED,
        null=True, related_name='resolved_hazards'
    )

    class Meta:
        ordering = ['-created', '-date_resolved']
        indexes = [
            models.Index(fields=['hazard_type'], name='hazard_idx'),
        ]

    def __str__(self):
        return f'{self.hazard_type} - {self.created.isoformat()}'
