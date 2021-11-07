# -*- coding: utf-8 -*-

# Imports from Django
from django.test import TestCase

# Imports from Third Party Modules
import mock

# Local Imports
from hikers.tests.factories import HikerFactory

# Local imports
from ..models import HikePhoto, HikeReview
from .factories import HikePhotoFactory, HikeReviewFactory


class ReviewModelTests(TestCase):

    def test_hike_review_unicode(self):
        date_fmt = '%Y-%m-%d'
        review = HikeReviewFactory()
        self.assertIsInstance(review, HikeReview)
        self.assertIn(review.created.strftime(date_fmt),
                      review.__str__())
        self.assertIn(review.hike.name,
                      review.__str__())

    @mock.patch('reviews.models.deleted_hiker_fallback')
    def test_hike_review_save(self, mock_deleted_hiker_fallback):
        added = HikerFactory()
        empty = HikerFactory()
        mock_deleted_hiker_fallback.return_value = empty
        hike_review = HikeReviewFactory(hiker=added)
        hike_review.save()
        self.assertFalse(mock_deleted_hiker_fallback.called)

        hike_review.hiker = None
        hike_review.save()
        self.assertTrue(mock_deleted_hiker_fallback.called)

    def test_hike_photo_unicode(self):
        date_fmt = '%Y-%m-%d'
        photo = HikePhotoFactory()
        self.assertIsInstance(photo, HikePhoto)
        self.assertIn(photo.created.strftime(date_fmt),
                      photo.__str__())
        self.assertIn(photo.hike.name,
                      photo.__str__())

    @mock.patch('reviews.models.deleted_hiker_fallback')
    def test_hike_photo_save(self, mock_deleted_hiker_fallback):
        added = HikerFactory()
        empty = HikerFactory()
        mock_deleted_hiker_fallback.return_value = empty
        hike_photo = HikePhotoFactory(hiker=added)
        hike_photo.save()
        self.assertFalse(mock_deleted_hiker_fallback.called)

        hike_photo.hiker = None
        hike_photo.save()
        self.assertTrue(mock_deleted_hiker_fallback.called)
