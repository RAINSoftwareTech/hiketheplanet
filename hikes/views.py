# Views to display region/trailhead/hike information by list or browse


from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from hikes.models import Region, Trailhead, Hike, Hazards, Sights
from json import dumps
from Hiking.utils import encode_url, build_context_dict
from hikes.forms import HikeForm
from urllib import unquote


@csrf_exempt
def ajax(request, region_name):
    this_region = Region.objects.get(name=region_name)
    trailheads_list = Trailhead.objects.filter(region=this_region).order_by("name")
    ajax_region_list = []
    for t in trailheads_list:
        if t.num_hikes == 1:
            one_hike = Hike.objects.get(trailhead=t)
            t.url = "hike/" + encode_url(one_hike.name)
        else:
            t.url = "trailhead/" + encode_url(t.name)
        ajax_region_list.append({
            "trailhead": t.name,
            "lat": t.latitude,
            "lon": t.longitude,
            "url": t.url,
            "num_hikes": t.num_hikes,
        })

    return HttpResponse(dumps(ajax_region_list), content_type="application/json")


@csrf_exempt
def index(request):
    context = RequestContext(request)
    region_list = Region.objects.order_by('-num_hikes')
    for r in region_list:
        r.url = encode_url(r.name)
    context_dict = {'regions': region_list}
    return render_to_response('hikes/index.html', context_dict, context)


def region(request, region_url):
    context = RequestContext(request)
    context_dict = build_context_dict(Region, region_url, 'region')

    try:
        this_region = Region.objects.get(name=context_dict['region'])
        trailheads = Trailhead.objects.filter(region=this_region).order_by('-name')
        context_dict['trailheads'] = trailheads
        context_dict['region'] = this_region
        for t in trailheads:
            if t.num_hikes == 1:
                one_hike = Hike.objects.get(trailhead=t)
                t.url = "hike/" + encode_url(one_hike.name)
            else:
                t.url = "trailhead/" + encode_url(t.name)
    except Region.DoesNotExist:
        pass

    return render_to_response('hikes/region.html', context_dict, context)


def trailhead(request, trailhead_url):
    context = RequestContext(request)
    context_dict = build_context_dict(Trailhead, trailhead_url, 'trailhead')

    try:
        this_location = Trailhead.objects.get(name=context_dict['trailhead'])
        hikes = Hike.objects.filter(trailhead=this_location)
        context_dict['trailhead'] = this_location
        context_dict['hikes'] = hikes
        context_dict['hiker'] = {'location': "97219"}
        for h in hikes:
            h.url = encode_url(h.name)
    except Trailhead.DoesNotExist:
        pass

    return render_to_response('hikes/trailheads.html', context_dict, context)


def hike(request, hike_url):
    context = RequestContext(request)
    context_dict = build_context_dict(Hike, hike_url, 'hike')
    hike_details = Hike.objects.get(name=context_dict['hike'])
    hazards = Hazards.objects.filter(hike=hike_details)
    sights = Sights.objects.filter(hike=hike_details)

    hiker_pace = 2
    hike_time = hike_details.distance / hiker_pace
    hike_total = round(hike_time * 60, 0)
    print(hike_total)
    hike_hours = int(hike_total // 60)
    print(hike_hours)
    hike_minutes = int(hike_total % 60)

    form = HikeForm()

    hiker_details = {}
    hiker_details['location'] = "97219"
    hiker_details['pace'] = hiker_pace
    hiker_details['hours'] = hike_hours
    hiker_details['minutes'] = hike_minutes

    context_dict['hike'] = hike_details
    context_dict['hazards'] = hazards
    context_dict['sights'] = sights
    context_dict['trailhead'] = hike_details.trailhead
    context_dict['hiker'] = hiker_details

    context_dict['form'] = form

    return render_to_response('hikes/hike.html', context_dict, context)


@login_required
@csrf_exempt
def hikes_ajax(request):
    print(request.method)
    if request.method == 'POST':
        hike_name = unquote(request.POST["hike"])
        print(hike_name)
        hike_details = Hike.objects.get(name=hike_name)
        print(hike_details)
        data = []
        if request.POST.get("description"):
            hike_details.description = unquote(request.POST["description"])

        if request.POST.get("difficulty"):
            hike_details.difficulty_level_explanation = unquote(request.POST["difficulty"])

        try:
            hike_details.trail_map = request.FILES["map"]
        except KeyError:
            pass


        hike_details.save()
        if hike_details.trail_map:
            data.append({
                "description": hike_details.description,
                "difficulty": hike_details.difficulty_level_explanation,
                "map": hike_details.trail_map
            })
        else:
            data.append({
                "description": hike_details.description,
                "difficulty": hike_details.difficulty_level_explanation
            })
        return HttpResponse(dumps(data), content_type="application/json")
    else:
        return Http404