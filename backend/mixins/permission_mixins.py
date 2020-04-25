# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import redirect

from hikers.utils import get_hiker
from hikers.models import Hiker


class HikerAccessMixin(AccessMixin):
    """
    CBV mixin which verifies that the current user is authenticated nd active.
    """
    inactive_redirect_path = reverse_lazy('hikers:inactive_redirect')
    ownership_failure_path = None
    group_failure_path = None

    def handle_inactive(self):
        if self.raise_exception:
            raise PermissionDenied('Your account is inactive. Please contact '
                                   'the site administrator for reactivation.')
        return redirect(self.inactive_redirect_path)

    def check_owner(self, user):
        return True

    def check_group(self, user):
        return True

    def access_failed(self, path, request, *args, **kwargs):
        if path:
            return redirect(path)
        else:
            return self.handle_no_permission()

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return self.handle_no_permission()
        if not request.user.is_active:
            return self.handle_inactive()
        if not self.check_owner(request.user):
            return self.access_failed(self.ownership_failure_path,
                                      request, *args, **kwargs)
        if not self.check_group(request.user):
            return self.access_failed(self.group_failure_path,
                                      request, *args, **kwargs)

        return super(HikerAccessMixin, self).dispatch(
            request, *args, **kwargs)


class ProfileAccessMixin(HikerAccessMixin):
    ownership_failure_path = reverse_lazy('hikers:profile_redirect')

    def check_owner(self, user):
        try:
            return get_hiker(user) == Hiker.objects.get(
                slug=self.kwargs['user_slug'])
        except Hiker.DoesNotExist:
            return False


class ObjectOwnershipRequiredMixin(HikerAccessMixin):
    superuser_allowed = True
    ownership_failure_path = '/'

    def check_owner(self, user):
        if self.superuser_allowed and user.is_superuser:
            return True
        try:
            owner_object = self.get_object()
        except Http404:
            return False
        try:
            return get_hiker(user) == owner_object.hiker
        except AttributeError:
            raise AttributeError('{} does not have a {} attribute. '
                                 'ObjectOwnershipRequiredMixin should not'
                                 'be used in this view.'.format(self.model,
                                                                'hiker'))


class GroupRequiredMixin(HikerAccessMixin):
    superuser_allowed = True
    group_required = None
    group_failure_path = reverse_lazy('hikers:denied_redirect')

    def check_group(self, user):
        if self.group_required:
            if self.superuser_allowed and user.is_superuser:
                return True
            user_groups = [group.name for group in user.groups.all()]
            return self.group_required in user_groups
        else:
            return True
