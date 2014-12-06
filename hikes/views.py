from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from hikes import models
from json import dumps


@csrf_exempt
def ajax(request):
    if request.method =="POST":
        region = models.Region()
        region.region = request.POST["region"]
        region.save()

    region_list = list(models.Region.objects.order_by('-num_hikes'))
    ajax_region_list = []
    for r in region_list:
        ajax_region_list.append({
            "region": r.region,
            "number of hikes": str(r.num_hikes),
        })

    return HttpResponse(dumps(ajax_region_list), content_type="application/json")


def dom(request):
    if request.method == "POST":
        print request.POST
    return render(request, 'hikes/dom.html')


def jsexample(request):
    return render(request, 'hikes/jsexample.html')


def index(request):
    context = RequestContext(request)
    region_list = models.Region.objects.order_by('-num_hikes')
    location_list = models.Location.objects.all()
    context_dict = {'regions': region_list, 'locations': location_list}
    for region in region_list:
        region.url = encode_url(region.region)
    return render_to_response('hikes/index.html', context_dict, context)


def hike(request):
    pass


def region(request, region_url):
    context = RequestContext(request)
    region_names_list = models.Region.objects.values_list('region', flat=True)
    region_name = decode_url(region_url, region_names_list)
    context_dict = {'region': region_name}

    try:
        this_region = models.Region.objects.get(region=region_name)
        locations = models.Location.objects.filter(region=this_region)
        context_dict['locations'] = locations
        context_dict['region'] = this_region
        for location in locations:
            location.url = encode_url(location.trailhead)
    except models.Region.DoesNotExist:
        pass

    return render_to_response('hikes/region.html', context_dict, context)


def trailhead(request, trailhead_url):
    context = RequestContext(request)
    trailhead_names_list = models.Location.objects.values_list('trailhead', flat=True)
    trailhead_name = decode_url(trailhead_url, trailhead_names_list)
    context_dict = {'trailhead': trailhead_name}

    try:
        this_location = models.Location.objects.get(trailhead=trailhead_name)
        hikes = models.Hike.objects.filter(location=this_location)
        context_dict['trailhead'] = this_location
        context_dict['hikes'] = hikes
        for hike in hikes:
            hike.url = encode_url(hike.name)
    except models.Region.DoesNotExist:
        pass

    return render_to_response('hikes/trailheads.html', context_dict, context)


def register(request):
    context = RequestContext(request)
    registered = False

    pass


def encode_url(name):
    to_keep = 'abcdefghijklmnopqrstuvwxyz '
    lower_name = name.lower()
    clean_name = lower_name
    for char in lower_name:
        if char not in to_keep:
            clean_name = lower_name.replace(char, '')
    clean_name = clean_name.replace('  ', ' ')
    return clean_name.replace(' ', '_')


def decode_url(url, field_list):
    url_name = url.replace('_', ' ')
    url_name = url_name.title()
    for name in field_list:
        if name.startswith(url_name[:6]):
            return name
    return url_name
