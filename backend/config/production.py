"""Production settings"""

# Imports from Django
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

# Imports from Third Party Modules
from .base import *  # noqa

# -------------- Explicitly set debug state
DEBUG = False

# -------------- DATABASE CONFIGURATION
# CHECK HOST CONFIG BEFORE DEPLOY
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '{{ dbname }}',
        'USER': '{{ dbuser }}',
        'PASSWORD': '{{ dbpassword }}',
        'HOST': '{{ dbhost }}',
        'PORT': '5432',
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

MIDDLEWARE.insert(0, 'django.middleware.cache.UpdateCacheMiddleware')
MIDDLEWARE.extend(
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
SECRET_KEY = '{{ secret_key }}'
# -------------- END SECRET CONFIGURATION


SEND_BROKEN_LINK_EMAILS = True
# -------------- MANAGER CONFIGURATION

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
ADMINS = {{admins}}
MANAGERS = ADMINS
# -------------- END MANAGER CONFIGURATION

ALLOWED_HOSTS = {{host_name}}

MAX_UPLOAD_SIZE_IN_MB = 4

# -------------- SECURITY SETTINGS
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_HTTPONLY = True
# ---------- EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# THESE SETTINGS NEED TO BE CHECKED BEFORE FIRST DEPLOY
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = '{{ email_host }}'
EMAIL_PORT = 587
EMAIL_HOST_USER = '{{ email_user }}'
EMAIL_HOST_PASSWORD = '{{ mail_password }}'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_TO_EMAIL = EMAIL_HOST_USER

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
# ---------- END EMAIL CONFIGURATION
GMAPS_API_KEY = '{{google_api_key}}'
ALLOWED_REFERER_DOMAIN = 'hiketheplanet.info'
