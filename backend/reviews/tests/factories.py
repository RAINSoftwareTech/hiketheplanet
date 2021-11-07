# -*- coding: utf-8 -*-

# Imports from Third Party Modules
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

# Local Imports
from hikes.tests.factories import HikeFactory

# Local imports
from ..models import HikePhoto, HikeReview


class HikeReviewFactory(DjangoModelFactory):

    class Meta:
        model = HikeReview

    hike = SubFactory(HikeFactory)
    review = Faker('text', max_nb_chars=200)


class HikePhotoFactory(DjangoModelFactory):

    class Meta:
        model = HikePhoto

    hike = SubFactory(HikeFactory)
    photo = Faker('file_name', extension='jpg')
