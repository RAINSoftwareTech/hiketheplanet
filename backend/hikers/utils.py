# -*- coding: utf-8 -*-

# Imports from Django
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

# Local imports
from .models import Hiker


def get_hiker(user):
    try:
        hiker = user.hiker
    except AttributeError:
        hiker, created = Hiker.objects.get_or_create(hiker=user)
    return hiker


class HikerCreateView(CreateView):

    def form_valid(self, form):
        hiker_object = form.save(commit=False)
        hiker_object.hiker = get_hiker(self.request.user)
        return super(HikerCreateView, self).form_valid(form)


class HikerUpdateView(UpdateView):

    def get_queryset(self):
        """Filter queryset to only return objects for the user profile defined
        by url kwargs. ProfileAccessMixin handles bad user_slug.
        :return: queryset of model objects associated with current hiker.
        """
        hiker = Hiker.objects.get(slug=self.kwargs['user_slug'])
        return self.model.objects.filter(hiker=hiker)


class HikerDeleteView(DeleteView):
    success_url_name = None

    def get_queryset(self):
        """Filter queryset to only return objects for the user profile defined
        by url kwargs. ProfileAccessMixin handles bad user_slug.
        :return: queryset of model objects associated with current hiker.
        """
        hiker = Hiker.objects.get(slug=self.kwargs['user_slug'])
        return self.model.objects.filter(hiker=hiker)

    def get_success_url(self):
        """
        Returns the supplied success URL.
        """
        if self.success_url_name:
            # Forcing possible reverse_lazy evaluation
            return reverse_lazy(self.success_url_name,
                                kwargs={'user_slug': self.kwargs['user_slug']})
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url_name.")
