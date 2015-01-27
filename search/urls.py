from django.conf.urls import patterns, url
from search import views

urlpatterns = patterns('',
    url(r'^$', views.search_hikes, name='search'),
    url(r'^distance/$', views.search_distance, name='distance'),
    )