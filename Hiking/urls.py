from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hikes/', include('hikes.urls')),
    url(r'^login/', include('authentication.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('search.urls'))
)
