# -*- coding: utf-8 -*-
# Imports from Django

# Imports from Third Party Modules
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Local imports
from .models import Trailhead, Hike
from .serializers import (
    TrailheadGeoSerializer,
    HikeSerializer
)
from .filtersets import TrailheadFilterSet
from core.permissions import IsAuthorizedContributorOrReadOnly
from .search import hike_name_autocomplete, google_autocomplete
from core.utils import get_key_from_request


class TrailheadsViewSet(ReadOnlyModelViewSet):
    queryset = Trailhead.objects.all()
    lookup_field = 'slug'
    serializer_class = TrailheadGeoSerializer
    filterset_class = TrailheadFilterSet

    @action(methods=['GET'], detail=False)
    def name_autocomplete(self, request, *args, **kwargs):
        search_text = get_key_from_request(request, 'search_text')
        names = hike_name_autocomplete(search_text)
        return Response(names, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def location_autocomplete(self, request, *args, **kwargs):
        search_query = self.request.query_params.dict() or self.request.data
        suggestions = google_autocomplete(**search_query)
        return Response(suggestions, status.HTTP_200_OK)


class HikesViewSet(ModelViewSet):
    queryset = Hike.objects.all()
    lookup_field = 'slug'
    serializer_class = HikeSerializer
    permission_classes = (IsAuthorizedContributorOrReadOnly,)