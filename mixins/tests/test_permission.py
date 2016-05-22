# -*- coding: utf-8 -*-

from mock import patch

from django.contrib.auth.models import AnonymousUser, Group
from django.core.exceptions import PermissionDenied
from django.test import TestCase, RequestFactory
from django.views.generic import DetailView, TemplateView

from core.utils import setup_view
from hikers.models import Hiker, HikerDiaryEntry
from hikers.tests.factories import (HikerFactory, HikerDiaryEntryFactory,
                                    UserFactory)
from hikes.models import Region
from hikes.tests.factories import RegionFactory

from mixins.permission_mixins import (HikerAccessMixin, ProfileAccessMixin,
                                      GroupRequiredMixin,
                                      ObjectOwnershipRequiredMixin)


class PermissionMixinsTests(TestCase):
    """Tests for all functions in core Models."""

    class HikerAccessView(HikerAccessMixin, TemplateView):
        pass

    class GroupReqView(GroupRequiredMixin, TemplateView):
        pass

    class ProfileAccessView(ProfileAccessMixin, DetailView):
        pass

    class OwnerReqView(ObjectOwnershipRequiredMixin, DetailView):
        pass

    def setUp(self):  # noqa
        self.region = RegionFactory()
        self.hiker1 = HikerFactory()
        self.hiker2 = HikerFactory()
        self.diary = HikerDiaryEntryFactory(hiker=self.hiker1)
        self.user_no_profile = UserFactory()

    @patch.object(HikerAccessView, 'check_owner')
    @patch.object(HikerAccessView, 'check_group')
    @patch.object(HikerAccessView, 'access_failed')
    @patch.object(HikerAccessView, 'handle_inactive')
    @patch.object(HikerAccessView, 'handle_no_permission')
    def test_hiker_access_dispatch(self, mock_no_permission, mock_inactive,
                                   mock_access_failed, mock_group, mock_owner):
        mock_owner.return_value = True
        mock_group.return_value = True
        mock_inactive.return_value = 'inactive'
        mock_no_permission.return_value = 'no permission'
        request = RequestFactory().get('/fake-path')
        view = self.HikerAccessView(template_name='test_views.html',
                                    model=Hiker,
                                    ownership_failure_path='owner fail',
                                    group_failure_path='group fail')
        view = setup_view(view, request)

        # unauthenticated user
        request.user = AnonymousUser()
        self.assertEquals(mock_no_permission.return_value,
                          view.dispatch(request))

        # user with no permissions flags
        request.user = self.user_no_profile
        self.assertEquals(200, view.dispatch(request).status_code)

        # inactive user
        request.user.is_active = False
        self.assertEquals(mock_inactive.return_value, view.dispatch(request))

        # check methods return false
        request.user.is_active = True
        mock_owner.return_value = False
        mock_group.return_value = False
        view.dispatch(request)
        mock_access_failed.assert_called_with(view.ownership_failure_path,
                                              request)

        mock_owner.return_value = True
        view.dispatch(request)

        mock_access_failed.assert_called_with(view.group_failure_path, request)

    @patch.object(HikerAccessView, 'handle_no_permission')
    @patch('mixins.permission_mixins.redirect')
    def test_hiker_access_methods(self, mock_redirect, mock_no_permission):
        mock_redirect.return_value = 'inactive redirect'
        mock_no_permission.return_value = 'no permission'
        request = RequestFactory().get('/fake-path')
        user = None
        view = self.HikerAccessView(template_name='test_views.html',
                                    model=Hiker,
                                    group_failure_path='group fail')
        view = setup_view(view, request)

        self.assertEquals(mock_redirect.return_value, view.handle_inactive())
        view.raise_exception = True
        with self.assertRaises(PermissionDenied):
            view.handle_inactive()

        self.assertTrue(view.check_owner(user))
        self.assertTrue(view.check_group(user))

        self.assertEquals(mock_no_permission.return_value,
                          view.access_failed(view.ownership_failure_path,
                                             request))

        mock_redirect.return_value = 'access failed redirect'
        self.assertEquals(mock_redirect.return_value,
                          view.access_failed(view.group_failure_path,
                                             request))

    def test_profile_access(self):
        request = RequestFactory().get('/fake-path')
        request.user = self.user_no_profile
        view = self.ProfileAccessView(
            template_name='test_views.html',
            model=Hiker)
        view = setup_view(view, request, user_slug=self.hiker1.slug)

        # returns false since profile attempted does not belong to user
        self.assertFalse(view.check_owner(request.user))

        # test method with correct user
        self.assertTrue(view.check_owner(self.hiker1.hiker))

        # check method with non-existent profile
        view = setup_view(view, request, user_slug='not-a-user')
        self.assertFalse(view.check_owner(self.hiker1.hiker))

    def test_owner_required(self):
        request = RequestFactory().get('/fake-path')
        view = self.OwnerReqView(
            template_name='test_views.html',
            model=HikerDiaryEntry)
        view = setup_view(view, request, pk=self.diary.pk)

        # valid object, user not superuser
        self.assertTrue(view.check_owner(self.hiker1.hiker))
        self.assertFalse(view.check_owner(self.hiker2.hiker))

        # user is superuser and superuser_allowed
        self.user_no_profile.is_superuser = True
        self.assertTrue(view.check_owner(self.user_no_profile))

        # user is superuser but not owner, and not superuser_allowed
        view.superuser_allowed = False
        self.assertFalse(view.check_owner(self.user_no_profile))

        # non-existent object
        view = setup_view(view, request, pk=9999)
        self.assertFalse(view.check_owner(self.hiker1.hiker))
        self.assertFalse(view.check_owner(self.hiker2.hiker))

        # mixin used on view for model with no ownership field
        view = self.OwnerReqView(
            template_name='test_views.html',
            model=Region)
        view = setup_view(view, request, pk=self.region.pk)
        with self.assertRaises(AttributeError):
            view.check_owner(self.hiker1.hiker)

    def test_group_required(self):
        request = RequestFactory().get('/fake-path')
        view = self.GroupReqView(
            template_name='test_views.html',
            model=HikerDiaryEntry)
        view = setup_view(view, request)
        group_name = 'test_group'
        group = Group.objects.create(name=group_name)

        # user not superuser, group None
        self.assertTrue(view.check_group(self.hiker1.hiker))

        # user is superuser and superuser_allowed
        view.group_required = group_name
        self.user_no_profile.is_superuser = True
        self.assertTrue(view.check_group(self.user_no_profile))

        # user is superuser but not group, and not superuser_allowed
        view.superuser_allowed = False
        self.assertFalse(view.check_group(self.user_no_profile))

        group_user = self.hiker1.hiker
        group_user.groups.add(group)
        self.assertTrue(view.check_group(group_user))
