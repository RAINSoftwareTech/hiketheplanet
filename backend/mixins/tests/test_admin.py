# -*- coding: utf-8 -*-

from django.contrib.admin import StackedInline
from django.contrib.admin.sites import AdminSite
from django.test import TestCase, RequestFactory

from mixins.admin_mixins import DynamicExtrasMixin
from mixins.tests.testing_models import TestChildModel, TestParentModel


class AdminMixinsTests(TestCase):
    """Tests for all functions in core Models."""

    class AdminInline(DynamicExtrasMixin, StackedInline):
        model = TestChildModel
        extra = 4

    def test_get_extras(self):
        site = AdminSite()
        form = self.AdminInline(TestParentModel, site)
        request = RequestFactory()
        self.assertEquals(form.extra, form.get_extra(request))
        self.assertEquals(0, form.get_extra(request, obj=True))
