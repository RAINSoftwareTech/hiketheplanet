# -*- coding: utf-8 -*-

from django.conf import settings
from django.views.generic import DetailView, TemplateView

from hikers.models import Hiker
from mixins.permission_mixins import HikerAccessMixin, ProfileAccessMixin


class HikerProfileView(ProfileAccessMixin, DetailView):
    """View for displaying a Region with its list of Trailheads."""
    model = Hiker
    template_name = 'hikers/hiker_profile.html'
    slug_url_kwarg = 'user_slug'
    context_object_name = 'hiker'


class ProfileRedirect(HikerAccessMixin, TemplateView):
    """View to offer redirection options for users attempting to access a
    hiker profile other than their own.
    """
    template_name = 'hikers/hiker_redirect.html'


class InactiveRedirect(TemplateView):
    """View to offer redirection options for inactive users attempting to
    access views that require active, authenticated accounts.
    """
    system_admin_email = settings.ADMINS[0][1]
    template_name = 'hikers/inactive_redirect.html'
