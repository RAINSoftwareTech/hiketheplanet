# -*- coding: utf-8 -*-

import mock

from django.test import TestCase, RequestFactory

from core.utils import setup_view

from hikes.models import Trailhead, Hike
from hikes.tests.factories import RegionFactory, TrailheadFactory, HikeFactory
from hikes.views import (TrailheadDetailView, HikeDetailView,
                         TrailheadMapListView)


class HikesViewsTests(TestCase):

    def test_trailhead_detail_queryset(self):
        region = RegionFactory()
        trailhead = TrailheadFactory(region=region)
        request = RequestFactory().get('/fake-path')
        view = TrailheadDetailView(template_name='test_views.html')
        view = setup_view(view, request, region_slug=region.slug,
                          trailhead_slug=trailhead.slug)

        qs = view.get_queryset()
        self.assertQuerysetEqual(qs,
                                 map(repr, Trailhead.objects.filter(
                                     region=region)
                                     ))

        view1 = TrailheadDetailView(template_name='test_views.html')
        view1 = setup_view(view1, request, region_slug='bad_region',
                           trailhead_slug=trailhead.slug)
        with self.assertRaises(ValueError):
            view1.get_queryset()

    def test_hike_detail_queryset(self):
        region = RegionFactory()
        trailhead = TrailheadFactory(region=region)
        hike = HikeFactory(trailhead=trailhead)
        request = RequestFactory().get('/fake-path')
        view = HikeDetailView(template_name='test_views.html')
        view = setup_view(view, request, region_slug=region.slug,
                          trailhead_slug=trailhead.slug, hike_slug=hike.slug)

        qs = view.get_queryset()
        self.assertQuerysetEqual(qs,
                                 map(repr, Hike.objects.filter(
                                     trailhead=trailhead)
                                     ))

        view1 = HikeDetailView(template_name='test_views.html')
        view1 = setup_view(view1, request, region_slug='bad_region',
                           trailhead_slug=trailhead.slug, hike_slug=hike.slug)
        with self.assertRaises(ValueError):
            view1.get_queryset()

        view2 = HikeDetailView(template_name='test_views.html')
        view2 = setup_view(view2, request, region_slug=region.slug,
                           trailhead_slug='bad_trailhead', hike_slug=hike.slug)
        with self.assertRaises(ValueError):
            view2.get_queryset()

    @mock.patch('hikes.views.trailheads_map_serializer')
    def test_trailheads_map_queryset(self, mock_serializer):
        mock_serializer.return_value = {'serialized': True}
        region = RegionFactory()
        trailhead = TrailheadFactory(region=region)
        HikeFactory(trailhead=trailhead)
        request = RequestFactory().get('/fake-path')
        view = TrailheadMapListView(template_name='test_views.html')
        view = setup_view(view, request, region_name=region.name)

        qs = view.get_queryset()
        self.assertEquals(qs, mock_serializer.return_value)

        view1 = TrailheadMapListView(template_name='test_views.html')
        view1 = setup_view(view1, request, region_name='Not a Region')
        with self.assertRaises(ValueError):
            view1.get_queryset()
