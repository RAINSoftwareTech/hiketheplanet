# -*- coding: utf-8 -*-

from mock import patch
from django.test import TestCase, RequestFactory

from core.utils import setup_view

from hikes.api.views import (RegionListAPIView, RegionDetailAPIView,
                             TrailheadListAPIView, TrailheadDetailAPIView,
                             HikeListAPIView, HikeDetailAPIView)
from hikes.tests.factories import (CountryRegionFactory, RegionFactory,
                                   TrailheadFactory, HikeFactory)


class HikesAPIViewsTests(TestCase):

    def setUp(self):  # noqa
        self.request = RequestFactory().get('/fake-path')
        self.co_region = CountryRegionFactory()
        self.region = RegionFactory(country_region=self.co_region)
        self.trailhead = TrailheadFactory(region=self.region)

    @patch('hikes.api.views.get_region_queryset')
    def test_region_list_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        view = RegionListAPIView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.api.views.get_region_queryset')
    def test_region_detail_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        view = RegionDetailAPIView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.api.views.get_trailhead_queryset')
    def test_trailhead_detail_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        view = TrailheadDetailAPIView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.api.views.get_trailhead_queryset')
    def test_trailhead_list_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        view = TrailheadListAPIView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.api.views.get_hike_queryset')
    def test_hike_detail_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        hike = HikeFactory(trailhead=self.trailhead)
        view = HikeDetailAPIView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          hike_slug=hike.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.api.views.get_hike_queryset')
    def test_hike_list_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        hike = HikeFactory(trailhead=self.trailhead)
        view = HikeListAPIView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          hike_slug=hike.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)
