import pytz

from django.utils import timezone


class TimezoneMiddleware(object):

    def get_tz_name(self, request):
        """Return pacific US if user not logged in."""
        user = request.user
        if user:
            return user.hiker.timezone
        else:
            return 'America/Los_Angeles'

    def process_request(self, request):
        tzname = self.get_tz_name(request)
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
