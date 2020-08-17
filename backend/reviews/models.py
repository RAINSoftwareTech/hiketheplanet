# Imports from Django
from django.db import models

# Local Imports
from core.models import TimeStampedModel
from hikers.models import SET_UNSUBSCRIBED, Hiker
from hikes.models import Hike

# limit edit/delete of reviews/photos to hiker/admin


class HikeReview(TimeStampedModel):
    """Model for capturing reviews for each hike. Edit/delete should be limited
    to creator and admin. Review is always public. Not to be confused with
    hiker diary entry. Will not be deleted upon hiker deleting account."""
    hike = models.ForeignKey(
        Hike, on_delete=models.CASCADE,
        related_name='reviews_by_hike'
    )
    hiker = models.ForeignKey(
        Hiker, on_delete=SET_UNSUBSCRIBED,
        null=True, related_name='reviews_by_hiker'
    )
    review = models.TextField()

    class Meta:
        ordering = ['-modified']

    def __str__(self):
        return f'{self.hike.name} - {self.created.date().isoformat()}'


class HikePhoto(TimeStampedModel):
    """Model for capturing photos for each hike. Edit/delete should be limited
    to creator and admin. HikePhotos are always public. Not to be confused with
    hiker photos. Will not be deleted upon hiker deleting account."""
    hike = models.ForeignKey(
        Hike, on_delete=models.CASCADE,
        related_name='hike_photos'
    )
    hiker = models.ForeignKey(
        Hiker, on_delete=SET_UNSUBSCRIBED,
        null=True, related_name='hike_photos_by_hiker'
    )
    photo = models.ImageField(upload_to='hike_photos')

    class Meta:
        ordering = ['-modified']

    def __str__(self):
        return f'{self.hike.name} - {self.created.date().isoformat()}'