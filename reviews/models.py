from django.db import models

from hikes.models import Hike
from hikers.models import Hiker

from core.models import TimeStampedModel

# limit edit/delete of reviews/photos to hiker/admin


class HikeReview(TimeStampedModel):
    """Model for capturing reviews for each hike. Edit/delete should be limited
    to creator and admin. Review is always public. Not to be confused with
    hiker diary entry. Will not be deleted upon hiker deleting account."""
    hike = models.ForeignKey(Hike, related_name='reviews_by_hike')
    hiker = models.ForeignKey(Hiker, related_name='reviews_by_hiker')
    review = models.TextField()

    class Meta:
        ordering = ['-modified']


class HikePhotos(TimeStampedModel):
    """Model for capturing photos for each hike. Edit/delete should be limited
    to creator and admin. HikePhotos are always public. Not to be confused with
    hiker photos. Will not be deleted upon hiker deleting account."""
    hike = models.ForeignKey(Hike)
    hiker = models.ForeignKey(Hiker)
    photo = models.ImageField(upload_to='hike_photos', blank=True)
