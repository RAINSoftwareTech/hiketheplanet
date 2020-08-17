# Imports from Django
from django.utils import timezone

# Imports from Third Party Modules
import pytz

default_tz_name = 'America/Los_Angeles'


class TimezoneMiddleware(object):

    def get_tz_name(self, request):
        """Return pacific US if user not logged in."""
        user = request.user
        try:
            return user.hiker.timezone
        except AttributeError:
            return default_tz_name

    def process_request(self, request):
        tzname = self.get_tz_name(request)
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
