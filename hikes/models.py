from django.db import models
from django import forms
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import USZipCodeField


class Hike(models.Model):
    name = models.CharField(max_length=180, unique=True)
    type = models.CharField(max_length=128)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    hike = models.ForeignKey(Hike)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True, default='OR')
    zipcode = models.USZipCodeField(max_length=5)
    region = models.CharField(max_length=128)

    def __unicode__(self):
        return self.address

    def miles_from_user(self):
        pass

    def hours_from_user(self):
        pass


class Difficulty(models.Model):
    hike = models.ForeignKey(Hike)
    difficulty_level = models.CharField(max_length=25)
    length = models.IntegerField(default=0)
    elevation = models.IntegerField(default=0)


class Hazard(models.Model):
    hike = models.ForeignKey(Hike)
    trail_maintenance = models.CharField(max_length=200)
    weather_effects = models.CharField(max_length=200)
    user_reports = models.TextField()
    user_reports_date = models.DateTimeField()
    known_challenges = models.TextField


class Sights(models.Model):
    hike = models.ForeignKey(Hike)
    views = models.TextField()
    wildlife = models.TextField()
    # hiker_shared = models.ForeignKey(????) need to link user posted reviews, photos, etc


class Equipment(models.Model):
    hike = models.ForeignKey(Hike)
    trail_map = models.FileField()
    # recommended_gear = list


#start Hiker classes:
class Hiker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    home_address = models.CharField(max_length=128)
    home_city = models.CharField(max_length=70)
    home_state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True, default='OR')
    home_zipcode = models.USZipCodeField(max_length=5)
    health_level = models.CharField(max_length=100)
    avg_walking_pace = models.FloatField(default=2.0)


class HikingLog(models.Model):
    hiker = models.ForeignKey(Hiker)
    diaries = models.TextField()
    

