# -*- coding: utf-8 -*-

# Imports from Third Party Modules
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from random import choice

# Local Imports
from hikes.tests.factories import HikeFactory

# Local imports
from ..models import Hazard

hazard_types = ['trail', 'weather', 'permanent', 'other']
hazard = choice(hazard_types)


class HazardFactory(DjangoModelFactory):

    class Meta:
        model = Hazard

    hike = SubFactory(HikeFactory)
    hazard_type = hazard
    description = Faker('text', max_nb_chars=200)
