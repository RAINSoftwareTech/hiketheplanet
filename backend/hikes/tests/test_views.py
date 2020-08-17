# -*- coding: utf-8 -*-

# Imports from Django
from django.test import RequestFactory, TestCase

# Imports from Third Party Modules
import mock

# Local Imports
from core.utils import setup_view

# Local imports
from ..views import SearchByDistance, SearchByHikeName, TrailheadMapListView
from .factories import HikeFactory, TrailheadFactory


class SearchViewsTests(TestCase):

    @mock.patch('search.views.trailheads_serializer')
    def test_trailheads_map_queryset(self, mock_serializer):
        mock_serializer.return_value = {'serialized': True}
        trailhead = TrailheadFactory()
        HikeFactory(trailhead=trailhead)
        request = RequestFactory().get('/fake-path')
        view = TrailheadMapListView(template_name='test_views.html')
        view = setup_view(view, request)

        qs = view.get_queryset()
        self.assertEquals(qs, mock_serializer.return_value)

        view1 = TrailheadMapListView(template_name='test_views.html')
        view1 = setup_view(view1, request, region_name='Not a Region')

    @mock.patch('search.views.hikes_serializer')
    def test_search_by_hike_name_queryset(self, mock_serializer):
        mock_serializer.return_value = {'serialized': True}
        trailhead = TrailheadFactory()
        HikeFactory(trailhead=trailhead, name='Test Hike')
        request = RequestFactory().get('/fake-path/?search_text=hike')
        view = SearchByHikeName(template_name='test_views.html')
        view = setup_view(view, request)

        qs = view.get_queryset()
        self.assertEquals(qs, mock_serializer.return_value)

        view1 = TrailheadMapListView(template_name='test_views.html')
        view1 = setup_view(view1, request, region_name='Not a Region')

    @mock.patch('search.views.trailheads_as_the_crow_flies')
    @mock.patch('search.views.hikes_serializer')
    def test_search_by_distance_queryset(self, mock_serializer, mock_crow):
        mock_serializer.return_value = {'serialized': True}
        trailhead = TrailheadFactory()
        HikeFactory(trailhead=trailhead, name='Test Hike')
        mock_crow.return_value = [trailhead]
        request = RequestFactory().get('/fake-path/?search_text=9_97219')
        view = SearchByDistance(template_name='test_views.html')
        view = setup_view(view, request)

        qs = view.get_queryset()
        self.assertEquals(qs, mock_serializer.return_value)
