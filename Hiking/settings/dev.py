"""Development settings and globals."""

from base import *  # noqa

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = r"{{ secret_key }}"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
# TEMPLATES[0]['TEMPLATE_DEBUG'] = DEBUG

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'hiking',
        'USER': 'fableturas',
        'PASSWORD': 'HikeThePlanet',
        'HOST': '127.0.0.1',
    }
}

# ------------- CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# ------------- END CACHE CONFIGURATION
