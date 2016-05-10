import json
from json import dumps
from operator import itemgetter
from urllib import urlopen

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from core.utils import encode_url
from hikes.models import Hike, Trailhead, Region
from search.serializers import trailheads_serializer, hikes_serializer


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
        return trailheads_serializer(trailheads, region)


class SearchByHikeName(ListView):
    model = Hike
    template_name = 'search/search_list.html'

    def get_queryset(self):
        search_text = self.request.GET.get('search_text', '')
        hikes = Hike.objects.filter(name__icontains=search_text
                                    ).order_by('name')
        return hikes_serializer(hikes)


@csrf_exempt
def search_distance(request):
    API_KEY = 'Fmjtd%7Cluu82968l1%2Cag%3Do5-9w1x96'
    URL = 'http://www.mapquestapi.com/search/v2/radius?key={}&origin={}&hostedData={}&radius={}&maxMatches=800'
    geo_url ='http://open.mapquestapi.com/geocoding/v1/address?key={}&location={}&maxResults=1'
    hosted_data = 'mqap.149310_pdxhikes||'

    if request.method == 'GET':
        search_text = request.GET.get('search_text')
    else:
        search_text = ''

    # starting_zip = '97219'
    # max_distance = 60
    parameters = search_text.split('_')
    starting_zip = parameters[1]
    max_distance = parameters[0]
    print(starting_zip, max_distance)

    full_geo = geo_url.format(API_KEY, starting_zip)
    print(full_geo)
    geo_data = urlopen(full_geo).read()
    print(geo_data)
    geo_details = json.loads(geo_data)
    print(geo_details)

    start_lat = geo_details['results'][0]['locations'][0]['latLng']['lat']
    print(start_lat)
    start_lon = geo_details['results'][0]['locations'][0]['latLng']['lng']
    print(start_lon)
    start_latlon = str(start_lat) + ',' + str(start_lon)
    print(start_latlon)

    full_url = URL.format(API_KEY, start_latlon, hosted_data, max_distance)
    print(full_url)
    data = urlopen(full_url).read()
    distances = json.loads(data)
    search_results = distances['searchResults']
    results_list = []
    for result in search_results:
        fields = result['fields']
        name = fields['Hike']
        this_hike = Hike.objects.get(name=name)
        print(this_hike)
        results_list.append({
            'hike': name,
            'distance': result['distance'],
            'difficulty': this_hike.difficulty_level,
            'length': this_hike.distance,
            'hike_url': encode_url(this_hike.name)
        })
    sorted_results = sorted(results_list, key=itemgetter('distance'), reverse=True)
    return HttpResponse(dumps(sorted_results), content_type="application/json")


def mq_table():
    hikes = Hike.objects.all().order_by('name')
    table = open('mqtable.csv', 'w')
    table.write('Hike,Lat,Lon\n')
    for hike in hikes:
        location = hike.trailhead
        new_line = str(hike.name) + ',' + str(location.latitude) + ',' + str(location.longitude) + '\n'
        table.write(new_line)
        print(new_line)
    table.close()
