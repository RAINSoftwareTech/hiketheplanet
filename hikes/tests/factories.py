# -*- coding: utf-8 -*-

from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from random import randint, uniform, choice

from hikes.models import Region, Trailhead, Hike


dif_choices = ['0easy', '1moderate', '2difficult']
type_choices = ['loop', 'out_and_back', 'lollipop', 'point_to_point']
hike_choice = choice(type_choices)
difficulty = choice(dif_choices)


def rand_latitude():
    return uniform(41.0, 45.0)


def rand_longitude():
    return uniform(117.0, 124.0)


class RegionFactory(DjangoModelFactory):

    class Meta:
        model = Region

    name = Faker('word')
    num_hikes = randint(0, 600)


class TrailheadFactory(DjangoModelFactory):

    class Meta:
        model = Trailhead

    region = SubFactory(RegionFactory)
    name = Faker('word')
    num_hikes = randint(0, 100)
    latitude = rand_latitude()
    longitude = rand_longitude()


class HikeFactory(DjangoModelFactory):

    class Meta:
        model = Hike

    trailhead = SubFactory(TrailheadFactory)
    name = Faker('word')
    hike_type = hike_choice
    difficulty_level = difficulty
    distance = uniform(0.0, 30.0)
    elevation = randint(0, 2500)
    high_point = randint(0, 3000)
