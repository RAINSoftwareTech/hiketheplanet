from django.db import models


# ie: 'Oregon Coast', 'Columbia Gorge'
class Region(models.Model):
    name = models.CharField(max_length=50)
    num_hikes = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name


# places where hikes start. presumptively the best approximation of parking locations
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


# hikes and relevant one-to-one details
class Hike(models.Model):
    trailhead = models.ForeignKey(Trailhead)
    name = models.CharField(max_length=180, unique=True)
    hike_type = models.CharField(max_length=20,)  # style of Hike: 'Out and Back', 'Loop', 'One Way'
    likes = models.IntegerField(default=0)
    trail_map = models.FileField(upload_to='trail_maps', blank=True)
    difficulty_level = models.CharField(max_length=20, default="Easy")  #levels Easy, Moderate, Difficult
    difficulty_level_explanation = models.CharField(max_length=250, blank=True)  # what makes this hike Easy, Moderate, or Difficult
    distance = models.FloatField(default=0.0)
    elevation = models.IntegerField(default=0)
    high_point = models.IntegerField(default=0)
    description = models.TextField()

    def __unicode__(self):
        return self.name


# each hike may have multiple potential hazards - or none.
# this section is meant to be editable by registered users
class Hazards(models.Model):
    hike = models.ForeignKey(Hike)
    trail_maintenance = models.CharField(max_length=200)
    weather_effects = models.CharField(max_length=200)
    user_reports = models.TextField()
    user_reports_date = models.DateTimeField()
    known_challenges = models.TextField()

    class Meta:
        verbose_name = "Hazards"


# each hike may have multiple Sights to watch for
# this section is meant to be editable by registered users
# and possibly pulled from "share" sections of user diaries
class Sights(models.Model):
    hike = models.ForeignKey(Hike)
    views = models.TextField()
    wildlife = models.TextField()
    # hiker_shared = models.ForeignKey(????) need to link user posted reviews, photos, etc

    class Meta:
        verbose_name = "Sights"


# each hike may have multiple equipment recommendations: poles, waterproof boots, overnight gear, etc
class Equipment(models.Model):
    hike = models.ForeignKey(Hike)
    recommended_gear = models.CharField(max_length=200)

    def __unicode__(self):
        return self.recommended_gear

    class Meta:
        verbose_name = "Equipment"

