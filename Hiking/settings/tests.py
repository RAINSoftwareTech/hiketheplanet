from base import *  # noqa

SECRET_KEY = r"{{ secret_key }}"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'Hiking_tests.db'),
    }
}
