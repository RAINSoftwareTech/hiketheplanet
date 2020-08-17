# -*- coding: utf-8 -*-
# Imports from Django
from django.views.generic import ListView

# Imports from Third Party Modules
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

# Local imports
from .models import Hike, Trailhead
from .serializers import (
    HikeDetailSerializer,
    HikeSerializer,
    TrailheadDetailSerializer,
    TrailheadSerializer,
    hikes_serializer,
    trailheads_serializer,
)
from .utils import (
    get_hike_queryset,
    get_trailhead_queryset,
    trailheads_as_the_crow_flies,
)


class TrailheadListAPIView(ListCreateAPIView):
    queryset = Trailhead.objects.all()
    serializer_class = TrailheadSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return get_trailhead_queryset(self.kwargs)


class TrailheadDetailAPIView(RetrieveUpdateAPIView):
    queryset = Trailhead.objects.all()
    serializer_class = TrailheadDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'trailhead_slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return get_trailhead_queryset(self.kwargs)


class HikeListAPIView(ListCreateAPIView):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return get_hike_queryset(self.kwargs)


class HikeDetailAPIView(RetrieveUpdateAPIView):
    queryset = Hike.objects.all()
    serializer_class = HikeDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'hike_slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return get_hike_queryset(self.kwargs)


class TrailheadMapListView(ListView):
    """View to supply list of trailheads to maps modal ajax call.
    """
    model = Trailhead
    template_name = 'search/search_list.html'
    context_object_name = 'trailheads'

    def get_queryset(self):
        trailheads = get_trailhead_queryset(self.kwargs)
        return trailheads_serializer(trailheads)


class SearchByHikeName(ListView):
    model = Hike
    template_name = 'search/search_list.html'

    def get_queryset(self):
        hikes = get_hike_queryset(self.kwargs)
        search_text = self.request.GET.get('search_text', '')
        hikes = hikes.filter(name__icontains=search_text).order_by('name')
        return hikes_serializer(hikes)


class SearchByDistance(ListView):
    model = Hike
    template_name = 'search/search_list.html'

    def get_queryset(self):
        search_text = self.request.GET.get('search_text', '9_97219')
        max_distance, starting_zip = search_text.split('_')
        crow_flies = trailheads_as_the_crow_flies(
            max_distance, starting_zip, self.kwargs)
        hike_list = []
        for trailhead in crow_flies:
            hike_list += trailhead.hikes.all()
        return hikes_serializer(hike_list)