from django.conf.urls import include, url

from django.contrib import admin

urlpatterns = [
    url(r'', include('hikes.urls', namespace='hikes')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('search.urls')),
    url(r'^hikers/', include('allauth.urls')),
    url(r'^hikers/', include('hikers.urls')),
]
