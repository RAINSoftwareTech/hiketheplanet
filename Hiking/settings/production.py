"""Production settings"""


from os import environ

from base import *  # noqa

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the {} env variable".format(setting)
    raise ImproperlyConfigured(error_msg)
# -------------- Explicitly set debug state
DEBUG = False

# -------------- DATABASE CONFIGURATION
# CHECK HOST CONFIG BEFORE DEPLOY
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'hiketheplanet',
        'USER': get_env_setting('DATABASE_USER'),
        'PASSWORD': get_env_setting('DATABASE_PASSWORD'),
        'HOST': '127.0.0.1',
    }
}

# -------------- END DATABASE CONFIGURATION


# -------------- CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }}

MIDDLEWARE_CLASSES.insert(0, 'django.middleware.cache.UpdateCacheMiddleware')
MIDDLEWARE_CLASSES.extend(
    ('django.middleware.cache.FetchFromCacheMiddleware',)
)
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 2
CACHE_MIDDLEWARE_KEY_PREFIX = 'hiketheplanet'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
# -------------- END CACHE CONFIGURATION


# -------------- SECRET CONFIGURATION
# SET SECRET KEY & SETTINGS IN ENV ON SERVER ON FIRST DEPLOY
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('DJANGO_SECRET_KEY')
# -------------- END SECRET CONFIGURATION


SEND_BROKEN_LINK_EMAILS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# -------------- END MANAGER CONFIGURATION

ALLOWED_HOSTS = [
    'www.hiketheplanet.info',
    'hiketheplanet.info']

MAX_UPLOAD_SIZE_IN_MB = 4

# -------------- SECURITY SETTINGS
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_HTTPONLY = True
