# -*- coding: utf-8 -*-

from mock import patch
from django.test import TestCase, RequestFactory

from core.utils import setup_view

from hikes.tests.factories import RegionFactory, TrailheadFactory, HikeFactory
from hikes.views import (TrailheadDetailView, HikeDetailView, HikeCreateView,
                         HikeUpdateView, TrailheadCreateView,
                         TrailheadUpdateView)


class HikesViewsTests(TestCase):

    def setUp(self):  # noqa
        self.request = RequestFactory().get('/fake-path')
        self.region = RegionFactory()
        self.trailhead = TrailheadFactory(region=self.region)

    @patch('hikes.views.get_trailhead_queryset')
    def test_trailhead_detail_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        view = TrailheadDetailView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    def test_trailhead_create_view_get_form(self):
        view = TrailheadCreateView(template_name='test_views.html')
        view = setup_view(view, self.request)
        form = view.get_form()
        self.assertTrue(form.fields['new_region'].required)
        self.assertFalse(form.fields['region'].required)
        view = setup_view(view, self.request, region_slug=self.region.slug)
        form = view.get_form()
        self.assertEquals(self.region, form.initial['region'])

    @patch('hikes.views.get_trailhead_queryset')
    def test_trailhead_update_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        view = TrailheadUpdateView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.views.get_hike_queryset')
    def test_hike_detail_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        hike = HikeFactory(trailhead=self.trailhead)
        view = HikeDetailView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          hike_slug=hike.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.views.get_hike_queryset')
    def test_hike_update_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        hike = HikeFactory(trailhead=self.trailhead)
        view = HikeUpdateView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          hike_slug=hike.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    def test_hike_create_view_get_form(self):
        view = HikeCreateView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug)
        form = view.get_form()
        self.assertEquals(self.region.name, form.initial['region_name'])
        self.assertEquals(self.trailhead, form.initial['trailhead'])
