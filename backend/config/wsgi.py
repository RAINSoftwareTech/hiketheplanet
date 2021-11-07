"""
WSGI config for Hike the Planet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

# Imports from Django
from django.core.wsgi import get_wsgi_application

# Imports from Third Party Modules
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()
