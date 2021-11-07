from django_filters.rest_framework import FilterSet
from django_filters import CharFilter
from .models import Trailhead
from django.db.models import Q
from .search import search_params
from core.exceptions import BadRequest

from django.contrib.gis.db.models.functions import Distance

class TrailheadFilterSet(FilterSet):
    name = CharFilter(method='name_filter')
    location = CharFilter(method='distance_filter')

    class Meta:
        model = Trailhead
        fields = ('name', 'location')

    def name_filter(self, queryset, name, value):
        hike_name = Q(hikes__name__icontains=value)
        trailhead_name = Q(name__icontains=value)
        return queryset.filter(hike_name | trailhead_name).distinct()

    def distance_filter(self, queryset, name, value):
        search_query = self.request.query_params.dict() or self.request.data
        search_query = search_query or {}
        search_query.pop('location', None)
        search_geom, bbox, center = search_params(value, **search_query)
        if not search_geom:
            raise BadRequest('Invalid search parameters')
        self.request.bbox = bbox
        return queryset.filter(point__contained=search_geom).annotate(
            distance_from=Distance('point', center)
        )
