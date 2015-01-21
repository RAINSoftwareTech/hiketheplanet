from django.shortcuts import render_to_response
from django.template import RequestContext
from Hiking.utils import encode_url
from hikes.models import Hike
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
            'length': hike.distance,
            'difficulty': hike.difficulty_level,
            'url': hike.url
        })

     # return render_to_response('search.html', {'hikes': hikes}, context)
    return HttpResponse(dumps(ajax_hikes_list), content_type="application/json")
