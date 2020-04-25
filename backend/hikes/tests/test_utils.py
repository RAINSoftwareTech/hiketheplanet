# -*- coding: utf-8 -*-

from django.http import Http404
from django.test import TestCase, RequestFactory
from django.views.generic import TemplateView

from core.utils import setup_view

from hikes.models import Region, Trailhead, Hike
from hikes.tests.factories import (CountryRegionFactory, RegionFactory,
                                   TrailheadFactory, HikeFactory)
from hikes.utils import (get_country_region_object, get_region_queryset,
                         get_region_object, get_trailhead_queryset,
                         get_trailhead_object, get_hike_queryset,
                         get_hike_object)


class TestView(TemplateView):
    pass


class HikesUtilsTests(TestCase):

    def setUp(self):  # noqa
        self.co_region = CountryRegionFactory()
        self.region = RegionFactory(country_region=self.co_region)
        self.trailhead = TrailheadFactory(region=self.region)
        self.hike = HikeFactory(trailhead=self.trailhead)

        self.request = RequestFactory().get('/fake-path')
        view = TemplateView(template_name='test_views.html')
        self.view = setup_view(view, self.request,
                               co_region_slug=self.co_region.slug,
                               region_slug=self.region.slug,
                               trailhead_slug=self.trailhead.slug,
                               hike_slug=self.hike.slug)

    def test_get_country_region_object(self):
        self.assertEquals(self.co_region,
                          get_country_region_object(self.view.kwargs))
        self.view.kwargs['co_region_slug'] = 'bad slug'
        with self.assertRaisesMessage(
                Http404, 'does not represent a saved Country Region'):
            get_country_region_object(self.view.kwargs)
        self.assertIsNone(get_country_region_object({}))

    def test_get_region_object(self):
        self.assertEquals(self.region,
                          get_region_object(self.view.kwargs))
        self.view.kwargs['region_slug'] = 'bad slug'
        with self.assertRaisesMessage(
                Http404, 'does not represent a saved Region'):
            get_region_object(self.view.kwargs)
        self.assertIsNone(get_region_object({}))

    def test_get_trailhead_object(self):
        self.assertEquals(self.trailhead,
                          get_trailhead_object(self.view.kwargs))
        self.view.kwargs['trailhead_slug'] = 'bad slug'
        with self.assertRaisesMessage(
                Http404, 'does not represent a saved Trailhead'):
            get_trailhead_object(self.view.kwargs)
        self.assertIsNone(get_trailhead_object({}))

    def test_get_hike_object(self):
        self.assertEquals(self.hike,
                          get_hike_object(self.view.kwargs))
        self.view.kwargs['hike_slug'] = 'bad slug'
        with self.assertRaisesMessage(
                Http404, 'does not represent a saved Hike'):
            get_hike_object(self.view.kwargs)
        self.assertIsNone(get_hike_object({}))

    def test_get_region_queryset(self):
        qs = get_region_queryset(self.view.kwargs)
        self.assertQuerysetEqual(qs, map(repr, Region.objects.filter(
                                     country_region=self.co_region)))

    def test_get_trailhead_queryset(self):
        qs = get_trailhead_queryset(self.view.kwargs)
        self.assertQuerysetEqual(qs, map(repr, Trailhead.objects.filter(
                                     region=self.region)))

    def test_get_hike_queryset(self):
        qs = get_hike_queryset(self.view.kwargs)
        self.assertQuerysetEqual(qs, map(repr, Hike.objects.filter(
                                     trailhead=self.trailhead)))
