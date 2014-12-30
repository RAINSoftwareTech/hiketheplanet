from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from hikes import models
from json import dumps

def ajax(request, region_name):
    this_region = models.Region.objects.get(name=region_name)
    trailheads_list = models.Trailhead.objects.filter(region=this_region)
    ajax_region_list = []
    for t in trailheads_list:
        t.url = encode_url(t.name)
        ajax_region_list.append({
            "trailhead": t.name,
            "lat": t.latitude,
            "lon": t.longitude,
            "url": t.url,
            "num hikes": t.num_hikes,
        })

    return HttpResponse(dumps(ajax_region_list), content_type="application/json")

def region(request, region_url):
    context = RequestContext(request)
    context_dict = build_context_dict(models.Region, region_url, 'region')

    try:
        this_region = models.Region.objects.get(name=context_dict['region'])
        trailheads = models.Trailhead.objects.filter(region=this_region).order_by('-latitude')
        context_dict['trailheads'] = trailheads
        context_dict['region'] = this_region
        for t in trailheads:
            t.url = encode_url(t.name)
    except models.Region.DoesNotExist:
        pass

    return render_to_response('hikes/region.html', context_dict, context)
