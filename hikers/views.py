# -*- coding: utf-8 -*-

from django.views.generic import DetailView

from hikers.models import Hiker


class HikerProfileView(DetailView):
    """View for displaying a Region with its list of Trailheads."""
    model = Hiker
    template_name = 'hikers/hiker_profile.html'
    slug_url_kwarg = 'user_slug'
    context_object_name = 'hiker'
