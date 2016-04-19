# -*- coding: utf-8 -*-

from factory.django import DjangoModelFactory
from factory import Faker, SubFactory

from hikes.tests.factories import HikeFactory
from reviews.models import HikeReview, HikePhoto


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
