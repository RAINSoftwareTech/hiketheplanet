from django.db import models

from hikes.models import Hike
from hikers.models import Hiker
from hikers.utils import deleted_hiker_fallback

from core.models import TimeStampedModel

# limit edit/delete of reviews/photos to hiker/admin


class HikeReview(TimeStampedModel):
    """Model for capturing reviews for each hike. Edit/delete should be limited
    to creator and admin. Review is always public. Not to be confused with
    hiker diary entry. Will not be deleted upon hiker deleting account."""
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE,
                             related_name='reviews_by_hike')
    hiker = models.ForeignKey(Hiker, on_delete=models.SET_NULL,
                              null=True,
                              related_name='reviews_by_hiker')
    review = models.TextField()

    class Meta:
        ordering = ['-modified']

    def save(self, *args, **kwargs):
        if not self.hiker:
            self.hiker = deleted_hiker_fallback()
        super(HikeReview, self).save(*args, **kwargs)


class HikePhotos(TimeStampedModel):
    """Model for capturing photos for each hike. Edit/delete should be limited
    to creator and admin. HikePhotos are always public. Not to be confused with
    hiker photos. Will not be deleted upon hiker deleting account."""
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE,
                             related_name='hike_photos')
    hiker = models.ForeignKey(Hiker, on_delete=models.SET_NULL,
                              null=True, related_name='hike_photos_by_hiker')
    photo = models.ImageField(upload_to='hike_photos', blank=True)

    class Meta:
        ordering = ['-modified']

    def save(self, *args, **kwargs):
        if not self.hiker:
            self.hiker = deleted_hiker_fallback()
        super(HikePhotos, self).save(*args, **kwargs)
