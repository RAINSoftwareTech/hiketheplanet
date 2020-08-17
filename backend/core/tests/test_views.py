# -*- coding: utf-8 -*-

# Imports from Django
from django.test import RequestFactory, TestCase

# Imports from Third Party Modules
from mock import MagicMock, patch

# Local Imports
from mixins.tests.testing_models import (
    TestChildFormset,
    TestParentForm,
    TestParentModel,
)

# Local imports
from ..utils import setup_view
from ..views import FormsetUpdateView


class CoreViewsTests(TestCase):
    """Tests for all functions in core Models."""

    class FormsetView(FormsetUpdateView):
        pass

    @patch.object(FormsetView, 'get_object')
    def test_get(self, mock_get_object):
        request = RequestFactory().get('/fake-path')
        view = self.FormsetView(template_name='test_views.html',
                                model=TestParentModel,
                                form_class=TestParentForm,
                                formset_classes=(TestChildFormset,))
        view = setup_view(view, request, pk=1)
        view.get(request)
        mock_get_object.assert_called()

    @patch.object(FormsetView, 'get_object')
    @patch.object(FormsetView, 'get_form_formsets')
    @patch.object(FormsetView, 'form_invalid')
    def test_post(self, mock_form_invalid, mock_get_formsets, mock_get_object):
        form = MagicMock()
        form.is_valid = MagicMock()
        form.is_valid.return_value = False
        formset = MagicMock()
        formset.is_valid = MagicMock()
        formset.is_valid.return_value = True
        mock_get_formsets.return_value = {'form': form, 'formsets': [formset]}
        mock_form_invalid.return_value = 'invalid'
        request = RequestFactory().get('/fake-path')
        view = self.FormsetView(template_name='test_views.html',
                                model=TestParentModel,
                                form_class=TestParentForm,
                                formset_classes=(TestChildFormset,))
        view = setup_view(view, request, pk=1)
        view.post(request)
        mock_get_object.assert_called()
