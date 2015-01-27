import json
from urllib import urlopen, quote
from Hiking.utils import encode_url
from hikes.models import Hike, Trailhead
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from json import dumps


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
    # URL = 'http://www.mapquestapi.com/directions/v1/route?key={}&from={}&to={}'
    URL = 'http://www.mapquestapi.com/directions/v1/routematrix?key={}&json={}'
    starting_zip = '97219'
    max_distance = 60
    matrix_json = {}
    matrix_json['options'] = {'allToAll': 'false'}

    distance_list = []
    # hikes = Hike.objects.all().order_by('name')
    hikes = Trailhead.objects.all().order_by('name')
    for hike in hikes:
        # location = hike.trailhead
        lat = hike.latitude
        lon = hike.longitude
        lat_lon = str(lat) + ',' + str(lon)

        matrix_json['locations'] = [starting_zip, lat_lon]

        # full_url = URL.format(API_KEY, quote(starting_zip), quote(lat_lon))
        full_url = URL.format(API_KEY, matrix_json)
        print(full_url)
        data = urlopen(full_url).read()
        directions = json.loads(data)
        print(directions)
        # distance = directions['route']['distance']
        distance = directions['distance'][1]
        print(distance)

        if distance <= max_distance:
            hike.url = encode_url(hike.name)
            distance_list.append({
                'hike': hike.name,
                'distance': distance,
                # 'length': hike.distance,
                # 'difficulty': hike.difficulty_level,
                'hike_url': hike.url
            })

    return HttpResponse(dumps(distance_list), content_type="application/json")
