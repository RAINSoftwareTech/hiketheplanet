from django.conf.urls import patterns, include, url
from hikes import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ajax/(?P<region_name>[\w|\W]+)/$', views.ajax, name='ajax'),
    url(r'^region/(?P<region_url>\w+)/$', views.region, name='region'),
    url(r'^trailhead/(?P<trailhead_url>\w+)/$', views.trailhead, name='trailhead'),
    url(r'^hike/(?P<hike_url>\w+)/$', views.hike, name='hike'),
    url(r'^hikesajax/$', views.hikes_ajax, name='hike ajax'),
    url(r'^admin/', include(admin.site.urls)),
)
