# -*- coding: utf-8 -*-

from django.views.generic import DetailView, ListView

from hikes.models import Region, Trailhead, Hike

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
