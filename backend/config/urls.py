# Imports from Django
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^hikers/', include('hikers.urls', namespace='hikers')),
    url(r'', include('hikes.urls', namespace='hikes')),
]

dev_patterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += dev_patterns
