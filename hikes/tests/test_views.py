# -*- coding: utf-8 -*-

from mock import patch
from django.test import TestCase, RequestFactory

from core.utils import setup_view

from hikes.tests.factories import RegionFactory, TrailheadFactory, HikeFactory
from hikes.views import (TrailheadDetailView, HikeDetailView,
                         HikeUpdateView)


class HikesViewsTests(TestCase):

    @patch('hikes.views.get_trailhead_queryset')
    def test_trailhead_detail_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        region = RegionFactory()
        trailhead = TrailheadFactory(region=region)
        request = RequestFactory().get('/fake-path')
        view = TrailheadDetailView(template_name='test_views.html')
        view = setup_view(view, request, region_slug=region.slug,
                          trailhead_slug=trailhead.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)
        view1 = HikeUpdateView(template_name='test_views.html')
        view1 = setup_view(view1, request)
        qs1 = view1.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs1)

    @patch('hikes.views.get_hike_queryset')
    def test_hike_detail_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        region = RegionFactory()
        trailhead = TrailheadFactory(region=region)
        hike = HikeFactory(trailhead=trailhead)
        request = RequestFactory().get('/fake-path')
        view = HikeDetailView(template_name='test_views.html')
        view = setup_view(view, request, region_slug=region.slug,
                          trailhead_slug=trailhead.slug, hike_slug=hike.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)
