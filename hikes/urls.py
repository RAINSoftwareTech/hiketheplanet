from django.conf.urls import patterns, include, url
from hikes import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ajax/', views.ajax, name='ajax'),
    url(r'^dom?$', views.dom, name='dom'),
    url(r'^jsexample?$', views.jsexample, name='jsexample'),
    url(r'^region/(?P<region_url>\w+)/$', views.region, name='region'),
    url(r'^trailhead/(?P<trailhead_url>\w+)/$', views.trailhead, name='trailhead'),
    url(r'^admin/', include(admin.site.urls)),
)
