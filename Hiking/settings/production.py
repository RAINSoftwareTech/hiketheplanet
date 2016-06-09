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


# -------------- DATABASE CONFIGURATION
# CHECK HOST CONFIG BEFORE DEPLOY
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'hiketheplanet',
        'USER': 'fableturas',
        'PASSWORD': '********',
        'HOST': '127.0.0.1',
    }
}

# -------------- END DATABASE CONFIGURATION


# -------------- CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {}
# -------------- END CACHE CONFIGURATION


# -------------- SECRET CONFIGURATION
# SET SECRET KEY & SETTINGS IN ENV ON SERVER ON FIRST DEPLOY
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('HIKING_SECRET_KEY')
# -------------- END SECRET CONFIGURATION

# -------------- MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Fable', 'fable@raintechpdx.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# -------------- END MANAGER CONFIGURATION

ALLOWED_HOSTS = [
    '.hiketheplanet.??'
]

MAX_UPLOAD_SIZE_IN_MB = 4
