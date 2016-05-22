# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory

from core.utils import setup_view

from hikers.models import HikerDiaryEntry, HikerPhoto, MyHike
from hikers.views import (HikerDiaryEntriesView, HikerPhotosView,
                          HikerHikesView, ProfileIndexRedirect)
from hikers.tests.factories import (UserFactory, HikerFactory,
                                    HikerDiaryEntryFactory, HikerPhotoFactory,
                                    MyHikeFactory)


class HikesViewsTests(TestCase):

    def setUp(self):  # noqa
        self.user = UserFactory()
        self.hiker = HikerFactory(hiker=self.user)
        self.request = RequestFactory().get('/fake-path')
        self.request.user = self.user

    def test_profile_index_redirect(self):
        view = ProfileIndexRedirect(template_name='test_views.html')
        view = setup_view(view, self.request, user_slug=self.hiker.slug)
        self.assertIn(self.hiker.slug, view.get_redirect_url())

    def test_diary_entry_view(self):
        view = HikerDiaryEntriesView(template_name='test_views.html')
        view = setup_view(view, self.request, user_slug=self.hiker.slug)
        HikerDiaryEntryFactory(hiker=self.hiker)
        HikerDiaryEntryFactory()
        self.assertQuerysetEqual(
            view.get_queryset(),
            map(repr, HikerDiaryEntry.objects.filter(hiker=self.hiker)))

    def test_photos_view(self):
        view = HikerPhotosView(template_name='test_views.html')
        view = setup_view(view, self.request, user_slug=self.hiker.slug)
        HikerPhotoFactory(hiker=self.hiker)
        HikerPhotoFactory()
        self.assertQuerysetEqual(
            view.get_queryset(),
            map(repr, HikerPhoto.objects.filter(hiker=self.hiker)))

    def test_hikers_hikes_view(self):
        view = HikerHikesView(template_name='test_views.html')
        view = setup_view(view, self.request, user_slug=self.hiker.slug)
        MyHikeFactory(hiker=self.hiker)
        MyHikeFactory()
        self.assertQuerysetEqual(
            view.get_queryset(),
            map(repr, MyHike.objects.filter(hiker=self.hiker)))
