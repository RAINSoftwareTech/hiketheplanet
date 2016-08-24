# -*- coding: utf-8 -*-

from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from hikes.api.serializers import (CountryRegionSerializer,
                                   CountryRegionDetailSerializer,
                                   RegionSerializer,
                                   RegionDetailSerializer,
                                   TrailheadSerializer,
                                   TrailheadDetailSerializer,
                                   HikeSerializer,
                                   HikeDetailSerializer)
from hikes.models import CountryRegion, Region, Trailhead, Hike
from hikes.utils import (get_region_queryset,
                         get_trailhead_queryset,
                         get_hike_queryset)


class CountryRegionListAPIView(ListAPIView):
    queryset = CountryRegion.objects.all()
    serializer_class = CountryRegionSerializer


class CountryRegionDetailAPIView(RetrieveUpdateAPIView):
    queryset = CountryRegion.objects.all()
    serializer_class = CountryRegionDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'co_region_slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class RegionListAPIView(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return get_region_queryset(self.kwargs)


class RegionDetailAPIView(RetrieveUpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'region_slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return get_region_queryset(self.kwargs)


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
