# Imports from Django
from django.conf import settings
from django.urls import include, path
from .views import EndpointsAPIView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # url(r'^hikers/', include('hikers.urls', namespace='hikers')),
    path('endpoints/', EndpointsAPIView.as_view(), name='endpoints'),
    path('', include('hikes.urls')),
]


if settings.DEBUG:
    urlpatterns += [path('docs/', include_docs_urls('HTP API Docs'))]
