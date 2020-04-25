from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^hikers/logout/$', logout, {'next_page': 'hikers/login'}),
    url(r'^hikers/', include('allauth.urls')),
    url(r'^hikers/', include('hikers.urls', namespace='hikers')),
    url(r'', include('hikes.urls', namespace='hikes')),
]

dev_patterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += dev_patterns
