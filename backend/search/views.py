# -*- coding: utf-8 -*-

from django.views.generic import ListView

from hikes.models import Hike, Trailhead
from hikes.utils import (get_trailhead_queryset, get_hike_queryset)
from search.serializers import trailheads_serializer, hikes_serializer
from search.utils import trailheads_as_the_crow_flies


class TrailheadMapListView(ListView):
    """View to supply list of trailheads to maps modal ajax call.
    """
    model = Trailhead
    template_name = 'search/search_list.html'
    context_object_name = 'trailheads'

    def get_queryset(self):
        trailheads = get_trailhead_queryset(self.kwargs)
        return trailheads_serializer(trailheads)


class SearchByHikeName(ListView):
    model = Hike
    template_name = 'search/search_list.html'

    def get_queryset(self):
        hikes = get_hike_queryset(self.kwargs)
        search_text = self.request.GET.get('search_text', '')
        hikes = hikes.filter(name__icontains=search_text).order_by('name')
        return hikes_serializer(hikes)


class SearchByDistance(ListView):
    model = Hike
    template_name = 'search/search_list.html'

    def get_queryset(self):
        search_text = self.request.GET.get('search_text', '9_97219')
        max_distance, starting_zip = search_text.split('_')
        crow_flies = trailheads_as_the_crow_flies(
            max_distance, starting_zip, self.kwargs)
        hike_list = []
        for trailhead in crow_flies:
            hike_list += trailhead.hikes.all()
        return hikes_serializer(hike_list)
