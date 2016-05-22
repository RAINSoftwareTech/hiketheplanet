# -*- coding: utf-8 -*-

from datetime import datetime
from django.core.exceptions import ValidationError
from django.test import TestCase

from hikes.tests.factories import HikeFactory
from hikers.models import (Hiker, HikerDiaryEntry, HikerPhoto, FutureHike,
                           MyHike)
from hikers.tests.factories import (HikerFactory, HikerDiaryEntryFactory,
                                    HikerPhotoFactory, FutureHikeFactory,
                                    MyHikeFactory)


class HikerModelsTests(TestCase):

    def setUp(self):  # noqa
        self.test_hike = HikeFactory()
        self.test_hiker = HikerFactory()

    def tearDown(self):  # noqa
        self.test_hike.delete()

    def test_hiker_unicode(self):
        self.assertIsInstance(self.test_hiker, Hiker)
        self.assertEquals(self.test_hiker.hiker.username,
                          self.test_hiker.__unicode__())

    def test_diary_unicode(self):
        date_fmt = '%Y-%m-%d'
        diary0 = HikerDiaryEntryFactory(hike=self.test_hike)
        self.assertIsInstance(diary0, HikerDiaryEntry)
        self.assertIn(diary0.title, diary0.__unicode__())
        self.assertIn(diary0.hike.name, diary0.__unicode__())

        diary1 = HikerDiaryEntryFactory()
        self.assertIn(diary1.title, diary1.__unicode__())
        self.assertIn(diary1.created.strftime(date_fmt), diary1.__unicode__())

        diary2 = HikerDiaryEntryFactory(title='', hike=self.test_hike)
        self.assertIn(diary2.hike.name, diary2.__unicode__())
        self.assertIn(diary2.created.strftime(date_fmt), diary2.__unicode__())

        diary3 = HikerDiaryEntryFactory(title='')
        self.assertEquals(diary3.created.strftime(date_fmt),
                          diary3.__unicode__())

    def test_photo_unicode(self):
        date_fmt = '%Y-%m-%d'
        photo0 = HikerPhotoFactory(hike=self.test_hike)
        self.assertIsInstance(photo0, HikerPhoto)
        self.assertIn(photo0.title, photo0.__unicode__())
        self.assertIn(photo0.hike.name, photo0.__unicode__())

        photo1 = HikerPhotoFactory()
        self.assertIn(photo1.title, photo1.__unicode__())
        self.assertIn(photo1.created.strftime(date_fmt), photo1.__unicode__())

        photo2 = HikerPhotoFactory(title='', hike=self.test_hike)
        self.assertIn(photo2.hike.name, photo2.__unicode__())
        self.assertIn(photo2.created.strftime(date_fmt), photo2.__unicode__())

        photo3 = HikerPhotoFactory(title='')
        self.assertIn(photo3.created.strftime(date_fmt), photo3.__unicode__())
        self.assertIn(photo3.photo.name, photo3.__unicode__())

    def test_future_hike_unicode(self):
        future_hike = FutureHikeFactory(hike=self.test_hike,
                                        hiker=self.test_hiker)
        self.assertIsInstance(future_hike, FutureHike)
        self.assertEquals(future_hike.hike.name, future_hike.__unicode__())

    def test_my_hike_unicode(self):
        my_hike = MyHikeFactory(hike=self.test_hike, hiker=self.test_hiker,
                                rating='0never', last_hiked=None)
        self.assertIsInstance(my_hike, MyHike)
        self.assertIn(my_hike.hike.name, my_hike.__unicode__())
        self.assertIn(my_hike.rating, my_hike.__unicode__())

    def test_my_hike_update_future(self):
        FutureHike.objects.all().delete()
        my_hike = MyHike(hike=self.test_hike, hiker=self.test_hiker,
                         rating='0never')
        self.assertFalse(FutureHike.objects.filter(
            hike=self.test_hike, hiker=self.test_hiker).exists())
        my_hike.update_future_hikes()
        self.assertTrue(FutureHike.objects.filter(
            hike=self.test_hike, hiker=self.test_hiker).exists())
        my_hike.rating = '1loved'
        my_hike.last_hiked = datetime.today()
        my_hike.update_future_hikes()
        self.assertFalse(FutureHike.objects.filter(
            hike=self.test_hike, hiker=self.test_hiker).exists())

    def test_validate_last_hiked(self):
        forgot_date = MyHike(hike=self.test_hike, hiker=self.test_hiker,
                             rating='6hated')
        never_hiked = MyHike(hike=self.test_hike, hiker=self.test_hiker,
                             rating='0never', last_hiked=datetime.today())
        with self.assertRaises(ValidationError):
            forgot_date.last_hiked_validator()
        with self.assertRaises(ValidationError):
            never_hiked.last_hiked_validator()
