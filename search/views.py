import json
from json import dumps
from operator import itemgetter
from urllib import urlopen
from geopy.geocoders import GoogleV3

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from core.utils import encode_url
from hikes.models import Hike, Trailhead, Region
from search.serializers import trailheads_serializer, hikes_serializer
from search.utils import trailheads_as_the_crow_flies


class TrailheadMapListView(ListView):
    """View to supply list of trailheads to maps modal ajax call.
    """
    model = Trailhead
    template_name = 'search/search_list.html'
    context_object_name = 'trailheads'

    def get_queryset(self):
        try:
            region = Region.objects.get(name=self.kwargs['region_name'])
        except Region.DoesNotExist:
            raise ValueError('{} does not represent a saved Region. '
                             'Please check your url or add the '
                             'Region.'.format(self.kwargs['region_name']))
        trailheads = Trailhead.objects.filter(region=region, num_hikes__gt=0)
        return trailheads_serializer(trailheads)


class SearchByHikeName(ListView):
    model = Hike
    template_name = 'search/search_list.html'

    def get_queryset(self):
        search_text = self.request.GET.get('search_text', '')
        hikes = Hike.objects.filter(name__icontains=search_text
                                    ).order_by('name')
        return hikes_serializer(hikes)


class SearchByDistance(ListView):
    model = Hike
    template_name = 'search/search_list.html'

    def get_queryset(self):
        search_text = self.request.GET.get('search_text', '9_97219')
        max_distance, starting_zip = search_text.split('_')
        crow_flies = trailheads_as_the_crow_flies(max_distance, starting_zip)
        hike_list = []
        for trailhead in crow_flies:
            hike_list += trailhead.hikes.all()
        return hikes_serializer(hike_list)
