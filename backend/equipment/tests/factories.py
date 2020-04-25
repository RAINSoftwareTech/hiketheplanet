# -*- coding: utf-8 -*-

from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from random import choice

from hikes.tests.factories import HikeFactory
from equipment.models import Equipment

gear_types = ['clothes', 'footware', 'safety']
gear = choice(gear_types)


class EquipmentFactory(DjangoModelFactory):

    class Meta:
        model = Equipment

    hike = SubFactory(HikeFactory)
    gear_type = gear
    recommended_gear = Faker('text', max_nb_chars=200)
    explanation = Faker('text', max_nb_chars=200)
