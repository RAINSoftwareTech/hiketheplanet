from django.conf import settings
from django import http
from django.utils.deprecation import MiddlewareMixin
from urllib.parse import urlparse


class AllowedHostsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        referer = request.META.get('HTTP_REFERER')
        origin = request.META.get('HTTP_ORIGIN') or referer
        domain = urlparse(origin).netloc if origin else None
        if domain != settings.ALLOWED_REFERER_DOMAIN:
            msg = 'Permission Denied: Hike the Planet is not a public API.'
            return http.HttpResponseForbidden(msg)
        return None
