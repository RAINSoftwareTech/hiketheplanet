# -*- coding: utf-8 -*-

from mock import patch, MagicMock

from django.http import HttpResponseRedirect
from django.test import TestCase, RequestFactory
from django.views.generic import CreateView

from core.utils import setup_view

from mixins.formset_mixins import FormsetViewMixin
from mixins.tests.testing_models import (TestParentModel, TestChildModel,
                                         TestChildFormset, TestParentForm)


def mock_render(context):
    return {'render': context}


def mock_context(*args, **kwargs):
    return{'context': (args, kwargs)}


class FormsetMixinsTests(TestCase):
    """Tests for all functions in core Models."""

    class FormsetView(FormsetViewMixin, CreateView):
        pass

    def test_get_form_formset(self):
        request = RequestFactory().get('/fake-path')
        view = self.FormsetView(template_name='test_views.html',
                                model=TestParentModel,
                                form_class=TestParentForm,
                                formset_classes=(TestChildFormset,))
        view = setup_view(view, request)
        forms_dict = view.get_form_formsets()
        self.assertIn('form', forms_dict.keys())

        formsets = forms_dict['formsets']
        self.assertIsInstance(formsets[0], TestChildFormset)

        view1 = self.FormsetView(template_name='test_views.html',
                                 model=TestParentModel,
                                 form_class=TestParentForm)
        view1 = setup_view(view1, request)
        forms_dict1 = view1.get_form_formsets()
        self.assertIn('form', forms_dict1.keys())
        self.assertEquals(0, len(forms_dict1['formsets']))

        view2 = self.FormsetView(template_name='test_views.html',
                                 model=TestParentModel,
                                 form_class=TestParentForm,
                                 formset_classes=['string'])
        view2 = setup_view(view2, request)
        with self.assertRaises(ValueError):
            view2.get_form_formsets()

        view2 = self.FormsetView(template_name='test_views.html',
                                 model=TestParentModel,
                                 form_class=TestParentForm,
                                 formset_classes=[TestChildModel])
        view2 = setup_view(view2, request)
        with self.assertRaises(ValueError):
            view2.get_form_formsets()

        view3 = self.FormsetView(template_name='test_views.html',
                                 model=TestParentModel,
                                 form_class=TestParentForm,
                                 formset_classes=TestChildFormset)
        view3 = setup_view(view3, request)
        with self.assertRaises(TypeError):
            view3.get_form_formsets()

    @patch.object(FormsetView, 'get_form_formsets')
    @patch.object(FormsetView, 'get_context_data', side_effect=mock_context)
    @patch.object(FormsetView, 'render_to_response', side_effect=mock_render)
    def test_get(self, mock_render_func, mock_context_func, mock_get_formsets):
        mock_get_formsets.return_value = {'form': 'form',
                                          'formsets': 'formset'}
        request = RequestFactory().get('/fake-path')
        view = self.FormsetView(template_name='test_views.html',
                                model=TestParentModel,
                                form_class=TestParentForm,
                                formset_classes=(TestChildFormset,))
        view = setup_view(view, request)
        view.get(request)
        mock_render_func.assert_called()
        mock_context_func.assert_called()
        mock_get_formsets.assert_called()

    @patch.object(FormsetView, 'get_form_formsets')
    @patch.object(FormsetView, 'form_valid')
    @patch.object(FormsetView, 'form_invalid')
    def test_post(self, mock_form_invalid, mock_form_valid, mock_get_formsets):
        form = MagicMock()
        form.is_valid = MagicMock()
        form.is_valid.return_value = False
        formset = MagicMock()
        formset.is_valid = MagicMock()
        formset.is_valid.return_value = True
        mock_get_formsets.return_value = {'form': form, 'formsets': [formset]}
        mock_form_invalid.return_value = 'invalid'
        mock_form_valid.return_value = 'valid'
        request = RequestFactory().get('/fake-path')
        view = self.FormsetView(template_name='test_views.html',
                                model=TestParentModel,
                                form_class=TestParentForm,
                                formset_classes=(TestChildFormset,))
        view = setup_view(view, request)

        self.assertEquals(mock_form_invalid.return_value, view.post(request))

        form.is_valid.return_value = True
        self.assertEquals(mock_form_valid.return_value, view.post(request))

        formset.is_valid.return_value = False
        self.assertEquals(mock_form_invalid.return_value, view.post(request))

    @patch.object(FormsetView, 'get_context_data', side_effect=mock_context)
    @patch.object(FormsetView, 'render_to_response', side_effect=mock_render)
    def test_form_invalid(self, mock_render_func, mock_context_func):
        request = RequestFactory().get('/fake-path')
        view = self.FormsetView(template_name='test_views.html',
                                model=TestParentModel,
                                form_class=TestParentForm,
                                formset_classes=(TestChildFormset,))
        view = setup_view(view, request)
        view.form_invalid({'form': 'form', 'formset': 'formset'})
        mock_render_func.assert_called()
        mock_context_func.assert_called()

    def test_form_valid(self):
        request = RequestFactory().get('/fake-path')
        view = self.FormsetView(template_name='test_views.html',
                                model=TestParentModel,
                                form_class=TestParentForm,
                                formset_classes=(TestChildFormset,))
        view = setup_view(view, request)
        form = MagicMock()
        form.is_valid = MagicMock()
        form.is_valid.return_value = False
        formset = MagicMock()
        formset.is_valid = MagicMock()
        formset.is_valid.return_value = True
        self.assertIsInstance(view.form_valid(form, [formset]),
                              HttpResponseRedirect)
