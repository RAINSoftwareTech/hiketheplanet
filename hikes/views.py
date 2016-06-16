# -*- coding: utf-8 -*-

from django.conf import settings
from django.forms import HiddenInput, TextInput
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from core.views import FormsetCreateView, FormsetUpdateView

from hikes.models import Region, Trailhead, Hike
from hikes.forms import TrailheadForm, HikeForm, HikeFormset
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


class TrailheadCreateView(GroupRequiredMixin, FormsetCreateView):
    model = Trailhead
    group_required = CONTRIBUTOR_GROUP
    form_class = TrailheadForm
    template_name = 'forms/formsets_form.html'
    formset_classes = [HikeFormset]

    def get_form(self, form_class=None):
        form = super(TrailheadCreateView, self).get_form(form_class)
        region_slug = self.kwargs.get('region_slug')
        if region_slug:
            region = Region.objects.get(slug=region_slug)
            form.initial['region'] = region
            form.fields['region'].widget.attrs['disabled'] = 'disabled'
            form.fields['new_region'].widget = HiddenInput()
        else:
            form.fields['region'].required = False
            form.fields['new_region'].required = True
            form.fields['region'].widget = HiddenInput()
        return form


class TrailheadUpdateView(GroupRequiredMixin, FormsetUpdateView):
    # ToDo: Add views and links to preselect hike/trailhead/region for form
    # by kwarg slugs. Add delete views. Add staff_required mixin.
    model = Trailhead
    group_required = CONTRIBUTOR_GROUP
    form_class = TrailheadForm
    slug_url_kwarg = 'trailhead_slug'
    template_name = 'forms/formsets_form.html'
    formset_classes = [HikeFormset]

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


class HikeCreateView(GroupRequiredMixin, CreateView):
    """View for displaying all details for each hike.
    """
    model = Hike
    group_required = CONTRIBUTOR_GROUP
    form_class = HikeForm
    template_name = 'forms/photo_forms.html'
    slug_url_kwarg = 'hike_slug'
    context_object_name = 'hike'

    def get_form(self, form_class=None):
        form = super(HikeCreateView, self).get_form(form_class)
        region_slug = self.kwargs.get('region_slug')
        trailhead_slug = self.kwargs.get('trailhead_slug')
        if region_slug and trailhead_slug:
            region = Region.objects.get(slug=region_slug)
            trailhead = Trailhead.objects.get(slug=trailhead_slug,
                                              region=region)
            form.initial['region_name'] = region.name
            form.fields['region_name'].widget = TextInput()
            form.fields['region_name'].widget.attrs['disabled'] = 'disabled'
            form.initial['trailhead'] = trailhead
            form.fields['trailhead'].widget.attrs['disabled'] = 'disabled'
        return form


class HikeUpdateView(GroupRequiredMixin, UpdateView):
    """View for displaying all details for each hike.
    """
    model = Hike
    group_required = CONTRIBUTOR_GROUP
    form_class = HikeForm
    template_name = 'forms/photo_forms.html'
    slug_url_kwarg = 'hike_slug'
    context_object_name = 'hike'

    def get_queryset(self):
        return get_hike_queryset(self)
