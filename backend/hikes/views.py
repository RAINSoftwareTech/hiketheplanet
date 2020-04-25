# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.forms import HiddenInput, TextInput
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  RedirectView)

from core.views import FormsetCreateView, FormsetUpdateView

from hikes.models import CountryRegion, Region, Trailhead, Hike
from hikes.forms import TrailheadForm, HikeForm, HikeFormset
from hikes.utils import (get_hike_queryset, get_trailhead_queryset,
                         get_region_queryset, get_region_object,
                         get_trailhead_object)

from mixins.permission_mixins import GroupRequiredMixin

CONTRIBUTOR_GROUP = settings.CONTRIBUTOR_GROUP_NAME


class HikeHomeRedirectView(RedirectView):
    """Temporary view to redirect all index calls to PNW region view until
    higher level views and templates can be built.
    """
    def get_redirect_url(self, *args, **kwargs):
        pnw = CountryRegion.objects.get(
            country_abbrev='us',
            region_name__icontains='pacific northwest')
        return reverse_lazy('hikes:broad_region_home',
                            kwargs={'co_region_slug': pnw.slug})


class CountryRegionListView(ListView):
    """View for displaying all larger area regions. Since country region
    objects have geo polygon feature, front end should be clickable map - see
    Leaflet."""
    model = CountryRegion
    template_name = 'hikes/index.html'
    queryset = CountryRegion.objects.all().prefetch_related('subregions')
    context_object_name = 'co_regions'


class RegionListView(ListView):
    """View to display list of regions. """
    model = Region
    context_object_name = 'region_list'
    template_name = 'hikes/index.html'

    def get_queryset(self):
        return get_region_queryset(self.kwargs)


class RegionDetailView(DetailView):
    """View for displaying a Region with its list of Trailheads."""
    model = Region
    template_name = 'hikes/region_detail.html'
    slug_url_kwarg = 'region_slug'
    context_object_name = 'region'

    def get_queryset(self):
        return get_region_queryset(self.kwargs)


class TrailheadDetailView(DetailView):
    """View for displaying trailhead details, including list of hikes."""
    model = Trailhead
    template_name = 'hikes/trailhead_detail.html'
    slug_url_kwarg = 'trailhead_slug'
    context_object_name = 'trailhead'

    def get_queryset(self):
        return get_trailhead_queryset(self.kwargs)


class TrailheadCreateView(GroupRequiredMixin, FormsetCreateView):
    model = Trailhead
    group_required = CONTRIBUTOR_GROUP
    form_class = TrailheadForm
    template_name = 'forms/formsets_form.html'
    formset_classes = [HikeFormset]

    def get_form(self, form_class=None):
        form = super(TrailheadCreateView, self).get_form(form_class)
        if self.kwargs.get('region_slug'):
            region = get_region_object(self.kwargs)
            form.initial['region'] = region
            form.fields['region'].widget.attrs['disabled'] = 'disabled'
            form.fields['new_region'].widget = HiddenInput()
        else:
            form.fields['region'].required = False
            form.fields['new_region'].required = True
            form.fields['region'].widget = HiddenInput()
            form.initial['co_region'] = self.kwargs.get('co_region_slug')
        return form


class TrailheadUpdateView(GroupRequiredMixin, FormsetUpdateView):
    # ToDo: Add get_form override to narrow region field queryset to
    # country region from url kwarg.
    model = Trailhead
    group_required = CONTRIBUTOR_GROUP
    form_class = TrailheadForm
    slug_url_kwarg = 'trailhead_slug'
    template_name = 'forms/formsets_form.html'
    formset_classes = [HikeFormset]

    def get_queryset(self):
        return get_trailhead_queryset(self.kwargs)


class HikeDetailView(DetailView):
    """View for displaying all details for each hike.
    """
    model = Trailhead
    template_name = 'hikes/hike_detail.html'
    slug_url_kwarg = 'hike_slug'
    context_object_name = 'hike'

    def get_queryset(self):
        return get_hike_queryset(self.kwargs)


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
        if self.kwargs.get('trailhead_slug'):
            trailhead = get_trailhead_object(self.kwargs)
            form.initial['region_name'] = trailhead.region.name
            form.fields['region_name'].widget = TextInput()
            form.fields['region_name'].widget.attrs['disabled'] = 'disabled'
            form.initial['trailhead'] = trailhead
            form.fields['trailhead'].widget.attrs['disabled'] = 'disabled'
        return form


class HikeUpdateView(GroupRequiredMixin, UpdateView):
    """View for displaying all details for each hike.
    """
    # ToDo: Add get_form override to narrow trailhead field queryset to
    # country region (sorted by region or alpha?) from url kwarg.
    model = Hike
    group_required = CONTRIBUTOR_GROUP
    form_class = HikeForm
    template_name = 'forms/photo_forms.html'
    slug_url_kwarg = 'hike_slug'
    context_object_name = 'hike'

    def get_queryset(self):
        return get_hike_queryset(self.kwargs)
