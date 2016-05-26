# -*- coding: utf-8 -*-

from django.conf import settings
from django.views.generic import DetailView, ListView

from core.views import FormsetCreateView, FormsetUpdateView

from hikes.models import Region, Trailhead
from hikes.forms import TrailheadForm, HikeFormset
from hikes.utils import get_hike_queryset, get_trailhead_queryset

from mixins.permission_mixins import GroupRequiredMixin

CONTRIBUTOR_GROUP = settings.CONTRIBUTOR_GROUP_NAME


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
        return get_trailhead_queryset(self)


class HikeDetailView(DetailView):
    """View for displaying all details for each hike.
    """
    model = Trailhead
    template_name = 'hikes/hike_detail.html'
    slug_url_kwarg = 'hike_slug'
    context_object_name = 'hike'

    def get_queryset(self):
        return get_hike_queryset(self)


class TrailheadCreateView(GroupRequiredMixin, FormsetCreateView):
    model = Trailhead
    group_required = CONTRIBUTOR_GROUP
    form_class = TrailheadForm
    template_name = 'hikes/trailhead_form.html'
    formset_classes = [HikeFormset]


class HikeUpdateView(GroupRequiredMixin, FormsetUpdateView):
    # ToDo: Add views and links to preselect hike/trailhead/region for form
    # by kwarg slugs. Add delete views. Add staff_required mixin.
    model = Trailhead
    group_required = CONTRIBUTOR_GROUP
    form_class = TrailheadForm
    slug_url_kwarg = 'trailhead_slug'
    template_name = 'hikes/trailhead_form.html'
    formset_classes = [HikeFormset]

    def get_queryset(self):
        return get_trailhead_queryset(self)
