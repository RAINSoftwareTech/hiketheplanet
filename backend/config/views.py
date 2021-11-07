
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView



class EndpointsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        endpoints = {
            'location_autocomplete':
                reverse('hikes:trailhead-location-autocomplete'),
            'name_autocomplete': reverse('hikes:trailhead-name-autocomplete'),
            'search': reverse('hikes:trailhead-list')
        }
        return Response(endpoints, status=status.HTTP_200_OK)