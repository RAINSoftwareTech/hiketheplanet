from django.contrib.auth.models import User
from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from django.utils import timezone


# ie: 'Oregon Coast', 'Columbia Gorge'
class Region(models.Model):
    name = models.CharField(max_length=50)
    num_hikes = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name


class Trailhead(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    num_hikes = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

    def miles_from_user(self):
        pass

    def hours_from_user(self):
        pass


class Hike(models.Model):
    # TYPE_CHOICES = ('Out and Back', 'Loop', 'One Way')

    trailhead = models.ForeignKey(Trailhead)
    name = models.CharField(max_length=180, unique=True)
    hike_type = models.CharField(max_length=20, default="Easy")
    likes = models.IntegerField(default=0)
    trail_map = models.FileField(upload_to='trail_maps', blank=True)
    difficulty_level = models.CharField(max_length=20)
    difficulty_level_explanation = models.TextField()
    distance = models.FloatField(default=0.0)
    elevation = models.IntegerField(default=0)
    high_point = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Hazards(models.Model):
    hike = models.ForeignKey(Hike)
    trail_maintenance = models.CharField(max_length=200)
    weather_effects = models.CharField(max_length=200)
    user_reports = models.TextField()
    user_reports_date = models.DateTimeField()
    known_challenges = models.TextField()


class Sights(models.Model):
    hike = models.ForeignKey(Hike)
    views = models.TextField()
    wildlife = models.TextField()
    # hiker_shared = models.ForeignKey(????) need to link user posted reviews, photos, etc


class Equipment(models.Model):
    hike = models.ForeignKey(Hike)
    recommended_gear = models.CharField(max_length=200)

    def __unicode__(self):
        return self.recommended_gear


#start Hiker classes:
class Hiker(models.Model):
    hiker = models.OneToOneField(User)
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
