import json
from urllib import urlopen, quote
from Hiking.utils import encode_url
from hikes.models import Hike, Trailhead
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from json import dumps
import webbrowser


@csrf_exempt
def search_hikes(request):
    # context = RequestContext(request)
    if request.method == 'GET':
        search_text = request.GET.get('search_text')
    else:
        search_text = ''

    ajax_hikes_list = []
    hikes = Hike.objects.filter(name__contains=search_text).order_by('name')
    for hike in hikes:
        hike.url = encode_url(hike.name)
        ajax_hikes_list.append({
            'hike': hike.name,
            'distance': hike.distance,
            'difficulty': hike.difficulty_level,
            'hikeUrl': hike.url
        })

     # return render_to_response('search.html', {'hikes': hikes}, context)
    return HttpResponse(dumps(ajax_hikes_list), content_type="application/json")


@csrf_exempt
def search_distance(request):
    API_KEY = 'Fmjtd%7Cluu82968l1%2Cag%3Do5-9w1x96'
    URL = 'http://www.mapquestapi.com/search/v2/radius?key={}&origin={}&hostedData={}&radius={}'
    hosted_data = 'mqap.149310_pdxhikes||'

    if request.method == 'GET':
        search_text = request.GET.get('search_text')
    else:
        search_text = ''

    starting_zip = '97219'
    max_distance = 60
    # parameters = search_text.split('_')
    # starting_zip = parameters[1]
    # max_distance = parameters[0]
    # print(starting_zip, max_distance)

    full_url = URL.format(API_KEY, starting_zip, hosted_data, max_distance)
    print(full_url)
    data = urlopen(full_url).read()
    distances = json.loads(data)
    search_results = distances['searchResults']
    results_list = []
    for result in search_results:
        fields = result['fields']
        name = fields['Hike']
        this_hike = Hike.objects.get(name=name)
        results_list.append({
            'hike': name,
            'distance': result['distance'],
            'difficulty': this_hike.difficulty_level,
            'length': this_hike.distance,
            'hike_url': encode_url(this_hike.name)
        })
    # mq_table()

    return HttpResponse(dumps(results_list), content_type="application/json")


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
