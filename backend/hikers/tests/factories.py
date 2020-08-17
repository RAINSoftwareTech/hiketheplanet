# -*- coding: utf-8 -*-

# Imports from Django
from django.contrib.auth import get_user_model

# Imports from Third Party Modules
import datetime
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from random import choice, uniform

# Local Imports
from hikes.tests.factories import HikeFactory

# Local imports
from ..models import (
    FutureHike,
    Hiker,
    HikerAddress,
    HikerDiaryEntry,
    HikerPhoto,
    MyHike,
)

User = get_user_model()

HEALTH_LEVELS = ['0poor', '1mediocre', '2average', '3moderate', '4fit']
health = choice(HEALTH_LEVELS)
RATING_CHOICES = ['0never', '1loved', '2liked', '3unsure', '4ok',
                  '5had_better', '6hated']
hike_rating = choice(RATING_CHOICES)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker('user_name')


class HikerFactory(DjangoModelFactory):

    class Meta:
        model = Hiker

    hiker = SubFactory(UserFactory)
    health_level = health
    avg_walking_pace = uniform(0.1, 4.5)
    miles_walked = uniform(0.1, 1000.0)


class HikerAddressFactory(DjangoModelFactory):

    class Meta:
        model = HikerAddress

    hiker = SubFactory(HikerFactory)


class HikerDiaryEntryFactory(DjangoModelFactory):

    class Meta:
        model = HikerDiaryEntry

    hiker = SubFactory(HikerFactory)
    title = Faker('text', max_nb_chars=200)


class HikerPhotoFactory(DjangoModelFactory):

    class Meta:
        model = HikerPhoto

    hiker = SubFactory(HikerFactory)
    title = Faker('text', max_nb_chars=10)
    photo = Faker('file_name', extension='jpg')


class FutureHikeFactory(DjangoModelFactory):

    class Meta:
        model = FutureHike

    hike = SubFactory(HikeFactory)
    hiker = SubFactory(HikerFactory)


class MyHikeFactory(DjangoModelFactory):

    class Meta:
        model = MyHike

    hike = SubFactory(HikeFactory)
    hiker = SubFactory(HikerFactory)
    rating = hike_rating
    last_hiked = datetime.datetime.today() if not rating == '0never' else None
