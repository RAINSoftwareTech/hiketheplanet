# -*- coding: utf-8 -*-

# Imports from Third Party Modules
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from random import choice

# Local Imports
from hikes.tests.factories import HikeFactory

# Local imports
from ..models import Equipment

gear_types = ['clothes', 'footware', 'safety']
gear = choice(gear_types)


class EquipmentFactory(DjangoModelFactory):

    class Meta:
        model = Equipment

    hike = SubFactory(HikeFactory)
    gear_type = gear
    recommended_gear = Faker('text', max_nb_chars=200)
    explanation = Faker('text', max_nb_chars=200)
