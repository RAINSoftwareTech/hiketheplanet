from django.conf.urls import patterns, include, url
from hikes import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Hiking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
