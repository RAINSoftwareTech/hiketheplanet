# -*- coding: utf-8 -*-

# Imports from Third Party Modules
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from random import choice

# Local Imports
from hikes.tests.factories import HikeFactory

# Local imports
from ..models import Sight

sights = ['0view', '1wildlife', '2flora']
time_of_day = ['0sunrise', '1morning', '2midday', '3evening',
               '4sunset', '5dark']
seasons = ['3winter', '0spring', '1summer', '2fall']
view_type = choice(sights)
time_to_see = choice(time_of_day)
season = choice(seasons)


class SightFactory(DjangoModelFactory):

    class Meta:
        model = Sight

    hike = SubFactory(HikeFactory)
    sight_type = view_type
    description = Faker('text', max_nb_chars=200)
    best_time = time_to_see
    best_season = season
