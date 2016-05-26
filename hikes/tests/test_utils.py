# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory

from core.utils import setup_view

from hikes.models import Trailhead, Hike
from hikes.tests.factories import RegionFactory, TrailheadFactory, HikeFactory
from hikes.utils import get_hike_queryset
from hikes.views import TrailheadDetailView, HikeDetailView


class HikesUtilsTests(TestCase):

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

        qs = get_hike_queryset(view)
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
