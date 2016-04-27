# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory

from core.utils import setup_view

from hikers.views import HikerProfileView
from hikers.tests.factories import UserFactory, HikerFactory


class HikesViewsTests(TestCase):

    def test_views(self):
        user = UserFactory()
        hiker = HikerFactory(hiker=user)
        request = RequestFactory().get('/fake-path')
        view = HikerProfileView(template_name='test_views.html')
        view = setup_view(view, request, user_slug=hiker.slug)
