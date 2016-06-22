# -*- coding: utf-8 -*-

from mock import patch
from django.test import TestCase, RequestFactory

from core.utils import setup_view

from hikes.models import CountryRegion
from hikes.tests.factories import (CountryRegionFactory, RegionFactory,
                                   TrailheadFactory, HikeFactory)
from hikes.views import (HikeHomeRedirectView, RegionListView,
                         RegionDetailView, TrailheadDetailView,
                         TrailheadCreateView, TrailheadUpdateView,
                         HikeDetailView, HikeCreateView,
                         HikeUpdateView)


class HikesViewsTests(TestCase):

    def setUp(self):  # noqa
        self.request = RequestFactory().get('/fake-path')
        self.co_region = CountryRegionFactory()
        self.region = RegionFactory(country_region=self.co_region)
        self.trailhead = TrailheadFactory(region=self.region)

    def test_hike_home_redirect_url(self):
        CountryRegion.objects.create(region_name='pacific northwest',
                                     country_abbrev='us',
                                     slug='pacific-northwest-us')
        view = HikeHomeRedirectView()
        view = setup_view(view, self.request)
        self.assertIn('pacific-northwest', view.get_redirect_url())

    @patch('hikes.views.get_region_queryset')
    def test_region_list_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        view = RegionListView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.views.get_region_queryset')
    def test_region_detail_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        view = RegionDetailView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.views.get_trailhead_queryset')
    def test_trailhead_detail_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        view = TrailheadDetailView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    def test_trailhead_create_view_get_form(self):
        view = TrailheadCreateView(template_name='test_views.html')
        view = setup_view(view, self.request,
                          co_region_slug=self.co_region.slug)
        form = view.get_form()
        self.assertTrue(form.fields['new_region'].required)
        self.assertFalse(form.fields['region'].required)
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          co_region_slug=self.co_region.slug)
        form = view.get_form()
        self.assertEquals(self.region, form.initial['region'])

    @patch('hikes.views.get_trailhead_queryset')
    def test_trailhead_update_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        view = TrailheadUpdateView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.views.get_hike_queryset')
    def test_hike_detail_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        hike = HikeFactory(trailhead=self.trailhead)
        view = HikeDetailView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          hike_slug=hike.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    @patch('hikes.views.get_hike_queryset')
    def test_hike_update_queryset(self, mock_queryset):
        mock_queryset.return_value = 'queryset'
        hike = HikeFactory(trailhead=self.trailhead)
        view = HikeUpdateView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          hike_slug=hike.slug,
                          co_region_slug=self.co_region.slug)

        qs = view.get_queryset()
        self.assertEquals(mock_queryset.return_value, qs)

    def test_hike_create_view_get_form(self):
        view = HikeCreateView(template_name='test_views.html')
        view = setup_view(view, self.request, region_slug=self.region.slug,
                          trailhead_slug=self.trailhead.slug,
                          co_region_slug=self.co_region.slug)
        form = view.get_form()
        self.assertEquals(self.region.name, form.initial['region_name'])
        self.assertEquals(self.trailhead, form.initial['trailhead'])
