# -*- coding: utf-8 -*-

from django.views.generic import CreateView, UpdateView

from mixins.formset_mixins import FormsetViewMixin


class FormsetCreateView(FormsetViewMixin, CreateView):
    pass


class FormsetUpdateView(FormsetViewMixin, UpdateView):

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(FormsetUpdateView, self).get(
            request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(FormsetUpdateView, self).post(
            request, *args, **kwargs)
