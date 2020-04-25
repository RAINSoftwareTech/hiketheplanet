# -*- coding: utf-8 -*-

from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from random import choice

from hikes.tests.factories import HikeFactory
from hazards.models import Hazard

hazard_types = ['trail', 'weather', 'permanent', 'other']
hazard = choice(hazard_types)


class HazardFactory(DjangoModelFactory):

    class Meta:
        model = Hazard

    hike = SubFactory(HikeFactory)
    hazard_type = hazard
    description = Faker('text', max_nb_chars=200)
