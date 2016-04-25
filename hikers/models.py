from django.contrib.auth.models import User
from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from django.utils import timezone


# this might warrant splitting off into a separate but linked app
# Hiker personal profile information. Hike tracking. Photo sharing. Hike Diary. etc
# start Hiker classes:
class Hiker(models.Model):
    hiker = models.ForeignKey(User)
    profile_pic = models.ImageField(upload_to='profile_images', blank=True)
    home_address = models.CharField(max_length=128, blank=True)
    home_city = models.CharField(max_length=70, default='Portland')
    home_state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True, default='OR')
    home_zipcode = models.CharField(max_length=5, default='97219')
    health_level = models.CharField(max_length=100, default='Average')
    avg_walking_pace = models.FloatField(default=2.0)
    miles_walked = models.FloatField(default=0.0)

    #add miles from hike each time hiker checks in/out of hike to total miles hiked
    # since date_joined
    def miles_calculated(self):
        pass

    def __unicode__(self):
        return self.hiker.username


class HikingDiary(models.Model):
    hiker = models.ForeignKey(Hiker)
    title = models.CharField(max_length=200)
    diary_entry = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title


# this might belong more to Hikes than to Hikers
class HikeReview(models.Model):
    hike = models.ForeignKey(Hike)
    hiker = models.ForeignKey(Hiker)
    review = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created_date = timezone.now()
        self.save()


class HikePhotos(models.Model):
    hike = models.ForeignKey(Hike)
    hiker = models.ForeignKey(Hiker)
    photo = models.ImageField(upload_to='hike_photos', blank=True)
    make_public = models.BooleanField()
    date_added = models.DateTimeField(default=timezone.now())


class MyHikes(models.Model):
    # RATING_CHOICES = ('Never Hiked', 'Loved It', 'Liked It', 'Not Sure', 'It Was Ok', 'Had Better', 'Hated It')
    hike = models.ForeignKey(Hike)
    hiker = models.ForeignKey(Hiker)
    last_hiked = models.DateTimeField(blank=True, null=True)
    rating = models.CharField(max_length=20)

    def add_to_future_hikes(self):
        pass


class FutureHikes(models.Model):
    hike = models.ForeignKey(Hike)
    hiker = models.ForeignKey(Hiker)