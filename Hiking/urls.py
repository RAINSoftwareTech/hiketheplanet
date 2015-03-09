from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # app Urls
    url(r'^hikes/', include('hikes.urls')),
    url(r'^login/', include('authentication.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('search.urls')),

    # login Urls
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/hikes/'}, name='logout'),
    url(r'^accounts/loggedin/$', 'Hiking.views.loggedin', name='loggedin'),

    # registration Urls
    url(r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
