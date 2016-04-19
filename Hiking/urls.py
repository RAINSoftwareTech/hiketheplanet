from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
from django.contrib.auth.decorators import login_required

admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = patterns('',

    # app Urls
    url(r'', include('hikes.urls')),
    url(r'', include('authentication.urls')),
    url(r'', include(admin.site.urls)),
    url(r'', include('search.urls')),
                       )

#     # login Urls - Todo: move accounts urls
#     url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
#     url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/hikes/'}, name='logout'),
#     url(r'^accounts/loggedin/$', 'Hiking.views.loggedin', name='loggedin'),
#
#     # registration Urls
#     # url(r'^accounts/', include('registration.backends.default.urls')),
# )
#
# if settings.DEBUG:
#     urlpatterns += patterns(
#         'django.views.static',
#         (r'media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}), )
