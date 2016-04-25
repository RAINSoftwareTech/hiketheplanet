# -*- coding: utf-8 -*-

from django.views.generic import DetailView, ListView

from hikes.models import Region, Trailhead, Hike
from hikes.serializers import trailheads_map_serializer

# from hikes.forms import HikeForm


class RegionListView(ListView):
    """View to display list of regions. """
    model = Region
    context_object_name = 'region_list'
    template_name = 'hikes/index.html'


class RegionDetailView(DetailView):
    """View for displaying a Region with its list of Trailheads."""
    model = Region
    template_name = 'hikes/region_detail.html'
    slug_url_kwarg = 'region_slug'
    queryset = Region.objects.prefetch_related('trailheads')
    context_object_name = 'region'


class TrailheadDetailView(DetailView):
    """View for displaying trailhead details, including list of hikes."""
    model = Trailhead
    template_name = 'hikes/trailhead_detail.html'
    slug_url_kwarg = 'trailhead_slug'
    context_object_name = 'trailhead'

    def get_queryset(self):
        try:
            region = Region.objects.get(slug=self.kwargs['region_slug'])
            return Trailhead.objects.filter(
                region=region).prefetch_related('hikes')
        except Region.DoesNotExist:
            raise ValueError('{} does not represent a saved Region. '
                             'Please check your url or add the '
                             'Region.'.format(self.kwargs['region_slug']))


class HikeDetailView(DetailView):
    """View for displaying all details for each hike.
    """
    model = Trailhead
    template_name = 'hikes/hike_detail.html'
    slug_url_kwarg = 'hike_slug'
    context_object_name = 'hike'

    def get_queryset(self):
        try:
            region = Region.objects.get(slug=self.kwargs['region_slug'])
            trailhead = Trailhead.objects.get(
                region=region, slug=self.kwargs['trailhead_slug'])
            return Hike.objects.filter(
                trailhead=trailhead).select_related('trailhead')
        except Region.DoesNotExist:
            raise ValueError('{} does not represent a saved Region. '
                             'Please check your url or add the '
                             'Region.'.format(self.kwargs['region_slug']))
        except Trailhead.DoesNotExist:
            raise ValueError('{} does not represent a saved Trailhead. '
                             'Please check your url or add the Trailhead.'
                             ''.format(self.kwargs['trailhead_slug']))


class TrailheadMapListView(ListView):
    """View to supply list of trailheads to maps modal ajax call.
    """
    model = Trailhead
    template_name = 'hikes/browse_map_modal.html'
    context_object_name = 'trailheads'

    def get_queryset(self):
        try:
            region = Region.objects.get(name=self.kwargs['region_name'])
        except Region.DoesNotExist:
            raise ValueError('{} does not represent a saved Region. '
                             'Please check your url or add the '
                             'Region.'.format(self.kwargs['region_name']))
        trailheads = Trailhead.objects.filter(region=region, num_hikes__gt=0)
        return trailheads_map_serializer(trailheads, region)

# def trailhead(request, trailhead_url):
#     context = RequestContext(request)
#     context_dict = build_context_dict(Trailhead, trailhead_url, 'trailhead')
#
#     try:
#         this_location = Trailhead.objects.get(name=context_dict['trailhead'])
#         hikes = Hike.objects.filter(trailhead=this_location)
#         context_dict['trailhead'] = this_location
#         context_dict['hikes'] = hikes
#         context_dict['hiker'] = {'location': "97219"}
#         for h in hikes:
#             h.url = encode_url(h.name)
#     except Trailhead.DoesNotExist:
#         pass
#
#     return render_to_response('hikes/trailhead.html', context_dict, context)
#
#
# def hike(request, hike_url):
#     context = RequestContext(request)
#     context_dict = build_context_dict(Hike, hike_url, 'hike')
#     hike_details = Hike.objects.get(name=context_dict['hike'])
#     hazards = Hazards.objects.filter(hike=hike_details)
#     sights = Sights.objects.filter(hike=hike_details)
#
#     hiker_pace = 2
#     hike_time = hike_details.distance / hiker_pace
#     hike_total = round(hike_time * 60, 0)
#     print(hike_total)
#     hike_hours = int(hike_total // 60)
#     print(hike_hours)
#     hike_minutes = int(hike_total % 60)
#
#     form = HikeForm()
#
#     hiker_details = {}
#     hiker_details['location'] = "97219"
#     hiker_details['pace'] = hiker_pace
#     hiker_details['hours'] = hike_hours
#     hiker_details['minutes'] = hike_minutes
#
#     context_dict['hike'] = hike_details
#     context_dict['hazards'] = hazards
#     context_dict['sights'] = sights
#     context_dict['trailhead'] = hike_details.trailhead
#     context_dict['hiker'] = hiker_details
#
#     context_dict['form'] = form
#
#     return render_to_response('hikes/hike.html', context_dict, context)
#
#
# @login_required
# @csrf_exempt
# def hikes_ajax(request):
#     print(request.method)
#     if request.method == 'POST':
#         hike_name = unquote(request.POST["hike"])
#         print(hike_name)
#         hike_details = Hike.objects.get(name=hike_name)
#         print(hike_details)
#         data = []
#         if request.POST.get("description"):
#             hike_details.description = unquote(request.POST["description"])
#
#         if request.POST.get("difficulty"):
#             hike_details.difficulty_level_explanation = unquote(
        # request.POST["difficulty"])
#
#         try:
#             hike_details.trail_map = request.FILES["map"]
#         except KeyError:
#             pass
#
#
#         hike_details.save()
#         if hike_details.trail_map:
#             data.append({
#                 "description": hike_details.description,
#                 "difficulty": hike_details.difficulty_level_explanation,
#                 "map": hike_details.trail_map
#             })
#         else:
#             data.append({
#                 "description": hike_details.description,
#                 "difficulty": hike_details.difficulty_level_explanation
#             })
#         return HttpResponse(dumps(data), content_type="application/json")
#     else:
#         return Http404
